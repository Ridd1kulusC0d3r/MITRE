"""python3 -m atlas <comando>

  check                 valida a fonte (data/entries, vocab, trilha…); avisos não bloqueiam
  build [--out DIR]     regenera os derivados (no repositório ou em DIR)
  build --check         falha se algum derivado versionado estiver desatualizado
  new campo=valor …     cria a próxima entrada (E###) e carimba reviewed_on com hoje
  set E### campo=valor  altera campos e carimba reviewed_on; 'campo=' remove o campo
  show E###             imprime a entrada
  split [ARQUIVO]       migra um agregado schema 2.0 (padrão: data/ecosystem.json) para a fonte
  generated             lista os arquivos que só o build escreve (usado pelo CI)
  site DIR              monta em DIR o site estático publicado no GitHub Pages

Listas (domains, formats, relations) usam ';' como separador. archived aceita true/false.
"""
import argparse
import json
import sys
from pathlib import Path

from atlas import model, render
from atlas.paths import Paths


def _report(errs, warns, quiet=False):
    for w in warns:
        if not quiet:
            print(f"⚠️  {w}")
    if errs:
        print(f"❌ {len(errs)} erro(s) de validação:")
        for e in errs:
            print(f"  - {e}")
        return 1
    return 0


def _parse_pairs(pairs):
    out = {}
    for pair in pairs:
        if "=" not in pair:
            raise SystemExit(f"argumento sem '=': {pair}")
        k, v = pair.split("=", 1)
        k = k.strip()
        if v == "":
            out[k] = None
        elif k in model.LIST_KEYS:
            out[k] = [x.strip() for x in v.split(";") if x.strip()]
        elif k == "archived":
            if v.lower() not in ("true", "false"):
                raise SystemExit("archived aceita true ou false")
            out[k] = v.lower() == "true"
        else:
            out[k] = v
    return out


def _validate_all(p, d=None):
    d = d if d is not None else model.load(p)
    return model.validate(d, model.load_trilha(p), p)


def cmd_check(p, a):
    errs, warns = _validate_all(p)
    rc = _report(errs, warns, a.quiet)
    if not rc:
        print(f"✅ {len(model.entry_files(p))} entradas válidas.")
    return rc


def cmd_build(p, a):
    errs, warns = _validate_all(p)
    if _report(errs, warns, quiet=True):
        return 1
    targets = render.build(p)
    if a.check:
        stale = [p.rel(f) for f, c in targets.items() if not f.exists() or f.read_text(encoding="utf-8") != c]
        if stale:
            print("❌ Derivados desatualizados:", *stale)
            print("   Rode: python3 -m atlas build")
            return 1
        print(f"✅ {len(targets)} derivados em dia.")
        return 0
    out_root = Path(a.out).resolve() if a.out else p.root
    for f, content in targets.items():
        dest = out_root / f.relative_to(p.root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
    print(f"✅ {len(model.entry_files(p))} entradas; gerados em {out_root}: "
          + ", ".join(p.rel(f) for f in targets))
    return 0


def _commit_entry(p, entry, previous):
    """Grava a entrada, valida tudo e desfaz se houver erro."""
    path = p.entries / f"{entry['id']}.json"
    model.save_entry(p, entry)
    errs, warns = _validate_all(p)
    mine = [e for e in errs if entry["id"] in e]
    if errs:
        if previous is None:
            path.unlink()
        else:
            model.save_entry(p, previous)
        _report(mine or errs, [])
        print("Nada foi gravado.")
        return 1
    print(json.dumps(model.canonical(entry), ensure_ascii=False, indent=2))
    print(f"✅ gravado em {p.rel(path)}")
    return 0


def cmd_new(p, a):
    d = model.load(p)
    fields = _parse_pairs(a.pairs)
    entry = {"id": model.next_id(d)}
    entry.update({k: v for k, v in fields.items() if v is not None})
    entry.setdefault("reviewed_on", model.today().isoformat())
    return _commit_entry(p, entry, None)


def cmd_set(p, a):
    path = p.entries / f"{a.id}.json"
    if not path.exists():
        print(f"❌ {a.id} não existe")
        return 1
    previous = model.read_json(path)
    entry = dict(previous)
    fields = _parse_pairs(a.pairs)
    if "id" in fields:
        print("❌ o id não muda; crie outra entrada")
        return 1
    for k, v in fields.items():
        if v is None:
            entry.pop(k, None)
        else:
            entry[k] = v
    if "reviewed_on" not in fields:
        entry["reviewed_on"] = model.today().isoformat()
    return _commit_entry(p, entry, previous)


def cmd_show(p, a):
    path = p.entries / f"{a.id}.json"
    if not path.exists():
        print(f"❌ {a.id} não existe")
        return 1
    print(path.read_text(encoding="utf-8"), end="")
    return 0


def cmd_split(p, a):
    src = Path(a.file) if a.file else p.bundle_json
    model.split(model.read_json(src), p)
    print(f"✅ fonte gravada a partir de {src}: {len(model.entry_files(p))} entradas em {p.rel(p.entries)}")
    return 0


def cmd_generated(p, a):
    for f in render.generated(p):
        print(p.rel(f))
    return 0


SITE_FILES = ["index.html", "assets", "data/ecosystem.json", "data/ecosystem.csv",
              "crosswalks", "layers", "site"]


def cmd_site(p, a):
    """Site estático: build em memória + arquivos públicos; não toca no repositório."""
    import shutil
    errs, warns = _validate_all(p)
    if _report(errs, warns, quiet=True):
        return 1
    out = Path(a.dir).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for rel in SITE_FILES:
        src = p.root / rel
        if src.is_dir():
            shutil.copytree(src, out / rel, ignore=shutil.ignore_patterns("*.py", "__pycache__"))
        elif src.exists():
            (out / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, out / rel)
    for f, content in render.build(p).items():
        if f.suffix in (".json", ".csv", ".js", ".svg", ".png"):
            dest = out / f.relative_to(p.root)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"✅ site montado em {out}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python3 -m atlas", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", help=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("check", help="valida a fonte")
    s.add_argument("-q", "--quiet", action="store_true", help="não mostra avisos")
    s = sub.add_parser("build", help="regenera os derivados")
    s.add_argument("--out", help="grava em outro diretório (ex.: dist)")
    s.add_argument("--check", action="store_true", help="só confere se os derivados estão em dia")
    s = sub.add_parser("new", help="cria entrada")
    s.add_argument("pairs", nargs="+", metavar="campo=valor")
    s = sub.add_parser("set", help="altera entrada")
    s.add_argument("id")
    s.add_argument("pairs", nargs="+", metavar="campo=valor")
    s = sub.add_parser("show", help="mostra entrada")
    s.add_argument("id")
    s = sub.add_parser("split", help="migra agregado para fonte fragmentada")
    s.add_argument("file", nargs="?")
    sub.add_parser("generated", help="lista derivados")
    s = sub.add_parser("site", help="monta o site estático")
    s.add_argument("dir")
    a = ap.parse_args(argv)
    p = Paths(a.root) if a.root else Paths()
    return {"check": cmd_check, "build": cmd_build, "new": cmd_new, "set": cmd_set,
            "show": cmd_show, "split": cmd_split, "generated": cmd_generated,
            "site": cmd_site}[a.cmd](p, a)


if __name__ == "__main__":
    sys.exit(main())
