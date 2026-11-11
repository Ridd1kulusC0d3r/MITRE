"""Testes do pacote atlas. Rode: python3 -m unittest -v

Os testes de saída usam tests/fixtures/repo (4 entradas congeladas), não os
dados reais, para que a atualização diária do catálogo não quebre o CI.
Para regenerar os golden files depois de uma mudança intencional de layout:
    ATLAS_UPDATE_GOLDEN=1 python3 -m unittest tests.test_atlas
"""
import copy
import io
import json
import os
import re
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path

from atlas import model, render
from atlas.cli import main as cli
from atlas.paths import REPO, Paths
from atlas.render.text import fit, xml

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "repo"
GOLDEN = HERE / "golden"


def fixture_copy():
    tmp = Path(tempfile.mkdtemp(prefix="atlas-"))
    shutil.copytree(FIXTURE, tmp, dirs_exist_ok=True)
    (tmp / "design").mkdir()
    shutil.copy(REPO / "design" / "tokens.json", tmp / "design" / "tokens.json")
    return tmp


def run(*argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = cli(list(argv))
    return rc, buf.getvalue()


class FixtureCase(unittest.TestCase):
    def setUp(self):
        self.root = fixture_copy()
        self.p = Paths(self.root)
        self.d = model.load(self.p)
        self.t = model.load_trilha(self.p)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def errors(self, d):
        return model.validate(d, self.t, today_=date(2026, 11, 11))[0]


class TestValidation(FixtureCase):
    def test_fixture_is_valid(self):
        self.assertEqual(self.errors(self.d), [])

    def mutate(self, fn):
        d = copy.deepcopy(self.d)
        fn(d["entries"][0])
        return " | ".join(self.errors(d))

    def test_rules(self):
        cases = {
            "campo obrigatório ausente: purpose": lambda e: e.pop("purpose"),
            "chave desconhecida: foo": lambda e: e.__setitem__("foo", 1),
            "id fora do padrão": lambda e: e.__setitem__("id", "X1"),
            "url deve usar https": lambda e: e.__setitem__("url", "http://x"),
            "layer inválido": lambda e: e.__setitem__("layer", "nada"),
            "domínio inválido": lambda e: e.__setitem__("domains", ["marte"]),
            "id inexistente: E999": lambda e: e.__setitem__("relations", ["E999"]),
            "relação consigo mesmo": lambda e: e.__setitem__("relations", [e["id"]]),
            "item repetido": lambda e: e.__setitem__("formats", ["a", "a"]),
            "deve ser lista": lambda e: e.__setitem__("domains", "enterprise"),
            "archived deve ser": lambda e: e.__setitem__("archived", "sim"),
            "reviewed_on fora do formato": lambda e: e.__setitem__("reviewed_on", "11/11/2026"),
            "reviewed_on no futuro": lambda e: e.__setitem__("reviewed_on", "2030-01-01"),
            "pushed_at fora do ISO": lambda e: e.__setitem__("pushed_at", "ontem"),
        }
        for expected, fn in cases.items():
            with self.subTest(expected):
                self.assertIn(expected, self.mutate(fn))

    def test_duplicates(self):
        d = copy.deepcopy(self.d)
        d["entries"].append(dict(d["entries"][0]))
        joined = " | ".join(self.errors(d))
        self.assertIn("id duplicado", joined)
        self.assertIn("nome duplicado", joined)

    def test_trilha_ref(self):
        t = copy.deepcopy(self.t)
        t["semanas"][0]["acoes"][0]["ref"] = ["E777"]
        errs = model.validate(self.d, t, today_=date(2026, 11, 11))[0]
        self.assertTrue(any("E777" in e for e in errs))

    def test_filename_must_match_id(self):
        (self.p.entries / "E001.json").rename(self.p.entries / "E900.json")
        errs = model.validate(model.load(self.p), self.t, self.p, date(2026, 11, 11))[0]
        self.assertTrue(any("nome do arquivo difere" in e for e in errs))

    def test_warnings_do_not_block(self):
        errs, warns = model.validate(self.d, self.t, today_=date(2026, 11, 11))
        self.assertEqual(errs, [])
        self.assertTrue(any("sem recíproca" in w for w in warns))


class TestModel(FixtureCase):
    def test_reviewed_on_is_derived(self):
        self.assertEqual(self.d["reviewed_on"], "2026-11-02")

    def test_split_load_roundtrip(self):
        other = Paths(Path(tempfile.mkdtemp(prefix="atlas-rt-")))
        try:
            model.split(self.d, other)
            self.assertEqual(model.load(other), self.d)
        finally:
            shutil.rmtree(other.root, ignore_errors=True)

    def test_top_level_order(self):
        self.assertEqual([k for k in self.d if k in model.TOP_ORDER],
                         [k for k in model.TOP_ORDER if k in self.d])

    def test_next_id(self):
        self.assertEqual(model.next_id(self.d), "E014")


class TestRender(FixtureCase):
    def test_golden(self):
        out = render.build(self.p, self.d, self.t)
        update = os.environ.get("ATLAS_UPDATE_GOLDEN")
        for path, content in out.items():
            g = GOLDEN / path.name
            with self.subTest(path.name):
                if update:
                    GOLDEN.mkdir(exist_ok=True)
                    g.write_text(content, encoding="utf-8")
                self.assertTrue(g.exists(), f"golden ausente: {g} (rode com ATLAS_UPDATE_GOLDEN=1)")
                self.assertEqual(content, g.read_text(encoding="utf-8"), f"{path.name} mudou")

    def test_deterministic(self):
        self.assertEqual(render.build(self.p, self.d, self.t), render.build(self.p, self.d, self.t))

    def test_bundle_is_aggregate(self):
        out = render.build(self.p, self.d, self.t)
        self.assertEqual(json.loads(out[self.p.bundle_json]), self.d)

    def test_readme_keeps_free_text(self):
        out = render.build(self.p, self.d, self.t)[self.p.readme]
        self.assertIn("texto livre", out)
        self.assertIn("| **4** |", out)

    def test_text_helpers(self):
        self.assertEqual(xml('a<b>&"'), "a&lt;b&gt;&amp;&quot;")
        self.assertEqual(fit("curto", 200, 6), "curto")
        cut = fit("um texto bem comprido que não cabe", 60, 6)
        self.assertTrue(cut.endswith("…") and len(cut) <= 10)


class TestCli(FixtureCase):
    def root_arg(self):
        return ["--root", str(self.root)]

    def test_new_and_set(self):
        rc, _ = run(*self.root_arg(), "new", "name=Ferramenta X", "url=https://example.org/x",
                    "origin=Comunidade", "owner_type=comunidade", "layer=deteccao",
                    "domains=enterprise", "purpose=Testar", "output=Regras", "priority=P2",
                    "status=ativo", "verification=teste")
        self.assertEqual(rc, 0)
        e = model.read_json(self.p.entries / "E014.json")
        self.assertEqual(e["reviewed_on"], model.today().isoformat())
        rc, _ = run(*self.root_arg(), "set", "E014", "version=1.0", "formats=STIX;JSON", "notes=")
        self.assertEqual(rc, 0)
        e = model.read_json(self.p.entries / "E014.json")
        self.assertEqual(e["formats"], ["STIX", "JSON"])
        self.assertEqual(list(e)[0], "id")

    def test_set_rolls_back_invalid(self):
        before = (self.p.entries / "E001.json").read_text(encoding="utf-8")
        rc, out = run(*self.root_arg(), "set", "E001", "layer=nada")
        self.assertEqual(rc, 1)
        self.assertIn("Nada foi gravado", out)
        self.assertEqual((self.p.entries / "E001.json").read_text(encoding="utf-8"), before)

    def test_new_invalid_leaves_no_file(self):
        rc, _ = run(*self.root_arg(), "new", "name=Incompleta")
        self.assertEqual(rc, 1)
        self.assertFalse((self.p.entries / "E014.json").exists())

    def test_build_out_and_check(self):
        out = self.root / "dist"
        self.assertEqual(run(*self.root_arg(), "build", "--out", str(out))[0], 0)
        self.assertTrue((out / "docs" / "catalogo.md").exists())
        self.assertEqual(run(*self.root_arg(), "build", "--check")[0], 1)
        run(*self.root_arg(), "build")
        self.assertEqual(run(*self.root_arg(), "build", "--check")[0], 0)


class TestRepository(unittest.TestCase):
    """Integração: a fonte real do repositório é válida."""

    def test_source_valid(self):
        p = Paths()
        errs, _ = model.validate(model.load(p), model.load_trilha(p), p)
        self.assertEqual(errs, [], "\n".join(errs))

    def test_no_color_literal_outside_tokens(self):
        """Cor só em design/tokens.json; renderizadores e site leem de lá."""
        hexcolor = re.compile(r"#[0-9a-fA-F]{6}\b")
        allowed = {"theme.py", "color.py"}
        offenders = []
        for f in list((REPO / "atlas").rglob("*.py")) + list((REPO / "site").rglob("*.*")):
            if f.name in allowed or f.name.startswith("tokens"):
                continue
            if hexcolor.search(f.read_text(encoding="utf-8")):
                offenders.append(str(f.relative_to(REPO)))
        if not (REPO / "site").exists():
            self.skipTest("site/ ainda não existe")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
