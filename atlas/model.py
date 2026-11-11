"""Carga, gravação e validação da fonte do catálogo.

A fonte fica fragmentada (um arquivo por entrada) para que revisões paralelas
não conflitem. `load()` remonta o agregado no formato do schema 2.0, que é o que
os renderizadores e os scripts de análise consomem.
"""
import json
import re
from collections import Counter
from datetime import date, datetime, timedelta, timezone

from atlas.paths import Paths

SCHEMA = "2.0"
TZ_NAME = "America/Sao_Paulo"

# ordem das chaves no agregado data/ecosystem.json (compatível com o schema 2.0)
TOP_ORDER = ["schema_version", "reviewed_on", "timezone", "scope", "verification_limits",
             "entries", "historical", "repository_checks", "vocab",
             "mitre_attack_archived", "attack_release"]
# chaves do agregado que vivem em data/meta.json
META_KEYS = ["schema_version", "timezone", "scope", "verification_limits",
             "mitre_attack_archived", "attack_release"]

# ordem canônica das chaves de uma entrada; também é a lista de chaves permitidas
ENTRY_KEYS = ["id", "name", "url", "origin", "owner_type", "layer", "domains", "legacy_category",
              "purpose", "output", "priority", "status", "version", "formats", "relations",
              "notes", "repo", "archived", "license_api", "pushed_at", "latest_release",
              "reviewed_on", "verification"]
REQUIRED = ["id", "name", "url", "origin", "owner_type", "layer", "domains", "purpose",
            "output", "priority", "status", "reviewed_on", "verification"]
LIST_KEYS = ("domains", "formats", "relations")
VOCAB_KEYS = ("owner_type", "layer", "status", "priority")

ID_RE = re.compile(r"E\d{3}")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
DATETIME_RE = re.compile(r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?)?")


def today():
    """Data de hoje no fuso do projeto (com recuo para UTC-3 se não houver tzdata)."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo(TZ_NAME)).date()
    except Exception:  # noqa: BLE001 — tzdata ausente
        return datetime.now(timezone(timedelta(hours=-3))).date()


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dumps(obj), encoding="utf-8")


def canonical(entry):
    known = [k for k in ENTRY_KEYS if k in entry]
    extra = [k for k in entry if k not in ENTRY_KEYS]
    return {k: entry[k] for k in known + extra}


def entry_files(p):
    return sorted(p.entries.glob("*.json"))


def load(p=None):
    """Remonta o agregado (schema 2.0) a partir da fonte fragmentada."""
    p = p or Paths()
    meta = read_json(p.meta)
    entries = [read_json(f) for f in entry_files(p)]
    parts = dict(meta)
    parts["entries"] = entries
    parts["historical"] = read_json(p.historical)
    parts["repository_checks"] = read_json(p.repo_checks)
    parts["vocab"] = read_json(p.vocab)
    parts["reviewed_on"] = max((e.get("reviewed_on", "") for e in entries), default="")
    out = {k: parts[k] for k in TOP_ORDER if k in parts}
    out.update({k: v for k, v in parts.items() if k not in out})
    return out


def load_trilha(p=None):
    return read_json((p or Paths()).trilha)


def save_entry(p, entry):
    write_json(p.entries / f"{entry['id']}.json", canonical(entry))


def split(aggregate, p=None):
    """Grava a fonte fragmentada a partir de um agregado schema 2.0."""
    p = p or Paths()
    p.entries.mkdir(parents=True, exist_ok=True)
    for f in entry_files(p):
        f.unlink()
    for e in aggregate["entries"]:
        save_entry(p, e)
    write_json(p.vocab, aggregate["vocab"])
    write_json(p.historical, aggregate["historical"])
    write_json(p.repo_checks, aggregate.get("repository_checks", []))
    write_json(p.meta, {k: aggregate[k] for k in META_KEYS if k in aggregate})


def next_id(d):
    nums = [int(e["id"][1:]) for e in d["entries"] if ID_RE.fullmatch(e.get("id", ""))]
    return f"E{max(nums, default=0) + 1:03d}"


def _is_date(v):
    if not isinstance(v, str) or not DATE_RE.fullmatch(v):
        return False
    try:
        date.fromisoformat(v)
        return True
    except ValueError:
        return False


def validate(d, trilha=None, p=None, today_=None):
    """Devolve (erros, avisos). Erro bloqueia o build; aviso só informa."""
    errs, warns = [], []
    vocab = d["vocab"]
    entries = d["entries"]
    ids = [e.get("id") for e in entries]
    idset = set(ids)
    limit = (today_ or today()) + timedelta(days=1)

    def where(e):
        i = e.get("id", "?")
        return f"data/entries/{i}.json" if p else i

    if p is not None:
        for f in entry_files(p):
            e = read_json(f)
            if f.stem != e.get("id"):
                errs.append(f"{p.rel(f)}: nome do arquivo difere do id ({e.get('id')})")
    errs += [f"id duplicado: {i}" for i, n in Counter(ids).items() if n > 1]
    errs += [f"nome duplicado: {n}" for n, c in Counter(e.get("name", "").lower() for e in entries).items() if c > 1]

    for e in entries:
        w = where(e)
        for f in REQUIRED:
            if e.get(f) in (None, "", []):
                errs.append(f"{w}: campo obrigatório ausente: {f}")
        for k in e:
            if k not in ENTRY_KEYS:
                errs.append(f"{w}: chave desconhecida: {k} (permitidas: ver atlas/model.py ENTRY_KEYS)")
        if not ID_RE.fullmatch(e.get("id", "")):
            errs.append(f"{w}: id fora do padrão E000")
        if not str(e.get("url", "")).startswith("https://"):
            errs.append(f"{w}: url deve usar https")
        for key in VOCAB_KEYS:
            if e.get(key) not in vocab[key]:
                errs.append(f"{w}: {key} inválido: {e.get(key)!r} (válidos: {', '.join(vocab[key])})")
        for key in LIST_KEYS:
            v = e.get(key, [])
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                errs.append(f"{w}: {key} deve ser lista de textos")
            elif len(v) != len(set(v)):
                errs.append(f"{w}: {key} com item repetido")
        for dom in e.get("domains", []):
            if dom not in vocab["domains"]:
                errs.append(f"{w}: domínio inválido: {dom}")
        for r in e.get("relations", []):
            if r not in idset:
                errs.append(f"{w}: relação aponta para id inexistente: {r}")
            if r == e.get("id"):
                errs.append(f"{w}: relação consigo mesmo")
        if "archived" in e and not isinstance(e["archived"], bool):
            errs.append(f"{w}: archived deve ser true/false")
        rv = e.get("reviewed_on")
        if rv and not _is_date(rv):
            errs.append(f"{w}: reviewed_on fora do formato AAAA-MM-DD: {rv}")
        elif rv and date.fromisoformat(rv) > limit:
            errs.append(f"{w}: reviewed_on no futuro: {rv}")
        pa = e.get("pushed_at")
        if pa and not DATETIME_RE.fullmatch(str(pa)):
            errs.append(f"{w}: pushed_at fora do ISO 8601: {pa}")
        if e.get("archived") and e.get("status") == "ativo":
            warns.append(f"{w}: repositório arquivado com status 'ativo'")

    for h in d.get("historical", []):
        for f in ("name", "url", "note"):
            if not h.get(f):
                errs.append(f"historical '{h.get('name', '?')}': campo ausente: {f}")

    if trilha is not None:
        bad = [f"{a['id']}→{r}" for s in trilha["semanas"] for a in s["acoes"]
               for r in a.get("ref", []) if r not in idset]
        if bad:
            errs.append("trilha referencia entradas inexistentes: " + ", ".join(bad))

    by_id = {e["id"]: e for e in entries if "id" in e}
    urls = Counter(e.get("url", "").rstrip("/").lower() for e in entries)
    dup = [u for u, n in urls.items() if n > 1]
    if dup:
        warns.append(f"{len(dup)} URL(s) compartilhadas por mais de uma entrada (ok para portais com várias ferramentas): "
                     + ", ".join(dup))
    oneway = [(e["id"], r) for e in entries for r in e.get("relations", [])
              if r in by_id and e["id"] not in by_id[r].get("relations", [])]
    if oneway:
        warns.append(f"{len(oneway)} relação(ões) sem recíproca (ex.: {', '.join(f'{a}→{b}' for a, b in oneway[:5])})")
    nover = [e["id"] for e in entries if e.get("status") == "ativo" and not e.get("version")]
    if nover:
        warns.append(f"{len(nover)} entrada(s) ativas sem 'version' (ex.: {', '.join(nover[:8])})")
    return errs, warns
