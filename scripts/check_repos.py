#!/usr/bin/env python3
"""check_repos.py — atualiza sinais de manutenção (archived, licença, pushed_at,
último release) das entradas hospedadas no GitHub. Somente stdlib.

Lê data/ecosystem.json, consulta a API do GitHub e imprime um relatório em
Markdown com o que mudou. Com --write grava os novos valores no JSON.

Uso:
    GITHUB_TOKEN=... python3 scripts/check_repos.py            # relatório
    GITHUB_TOKEN=... python3 scripts/check_repos.py --write    # relatório + grava
    python3 scripts/check_repos.py --stale-days 365            # destaca repos parados

Sem token, a API limita a 60 requisições/hora (insuficiente para o catálogo).
Variável GITHUB_API permite apontar para outro endpoint (testes).
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "ecosystem.json"
API = os.environ.get("GITHUB_API", "https://api.github.com")
GH = re.compile(r"https://github\.com/([^/]+)/([^/#?]+)")


def get(path):
    headers = {"User-Agent": "mitre-ecosystem-atlas/2.0", "Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def repo_of(e):
    if e.get("repo"):
        return e["repo"]
    m = GH.match(e["url"])
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}" if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--stale-days", type=int, default=540)
    a = ap.parse_args()

    d = json.loads(DATA.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    changes, stale, missing = [], [], []
    for e in d["entries"]:
        repo = repo_of(e)
        if not repo:
            continue
        info = get(f"/repos/{repo}")
        if info is None:
            missing.append((e["id"], e["name"], repo))
            continue
        rel = get(f"/repos/{repo}/releases/latest")
        new = {
            "archived": info.get("archived"),
            "license_api": (info.get("license") or {}).get("spdx_id"),
            "pushed_at": info.get("pushed_at"),
        }
        if rel and rel.get("tag_name"):
            new["latest_release"] = f"{rel['tag_name']} · {rel.get('published_at', '')[:10]}"
        diff = {k: (e.get(k), v) for k, v in new.items() if e.get(k) != v}
        if diff:
            changes.append((e["id"], e["name"], diff))
            if a.write:
                e.update(new)
        if new["pushed_at"]:
            age = (now - datetime.fromisoformat(new["pushed_at"].replace("Z", "+00:00"))).days
            if age > a.stale_days and e["status"] == "ativo":
                stale.append((e["id"], e["name"], age))
        if new["archived"] and e["status"] != "parado":
            stale.append((e["id"], e["name"], "ARQUIVADO"))

    print(f"# Verificação de repositórios — {now:%Y-%m-%d %H:%M} UTC\n")
    print(f"## Mudanças ({len(changes)})\n")
    for i, n, diff in changes:
        print(f"- **{n}** `{i}`: " + "; ".join(f"{k}: `{o}` → `{v}`" for k, (o, v) in diff.items()))
    print(f"\n## Revisar status ({len(stale)})\n")
    for i, n, age in stale:
        print(f"- **{n}** `{i}`: " + (age if isinstance(age, str) else f"sem push há {age} dias, mas marcado como ativo"))
    print(f"\n## Não encontrados ({len(missing)})\n")
    for i, n, r in missing:
        print(f"- **{n}** `{i}`: {r}")
    if a.write and changes:
        DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON atualizado. Rode scripts/build_catalog.py para regenerar o catálogo.", file=sys.stderr)


if __name__ == "__main__":
    main()
