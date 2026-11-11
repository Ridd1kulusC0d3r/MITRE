#!/usr/bin/env python3
"""monitor.py — relatório de manutenção do catálogo. Somente stdlib.

1. Compara a versão do ATT&CK publicada (attack-stix-data/index.json) com a do catálogo (E001).
2. Roda check_repos.py (precisa de GITHUB_TOKEN para não estourar o limite da API).
3. Escreve o relatório em $GITHUB_STEP_SUMMARY (ou na saída padrão).
4. Com --issue: abre ou atualiza uma issue com rótulo "monitor" quando há algo a
   fazer; fecha a issue aberta quando está tudo em dia. Requer REPO=dono/nome.

Uso:
    python3 scripts/monitor.py                 # só relatório
    GITHUB_TOKEN=... REPO=dono/repo python3 scripts/monitor.py --issue
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from atlas import model  # noqa: E402

INDEX = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/index.json"
API = os.environ.get("GITHUB_API", "https://api.github.com")
TITLE = "Monitor: itens do catálogo para revisar"
LABEL = "monitor"


def http(url, method="GET", body=None):
    headers = {"User-Agent": "mitre-ecosystem-atlas/2.1", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN") and url.startswith(API):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def attack_section(d):
    atual = next(e["version"] for e in d["entries"] if e["id"] == "E001").split()[0].lstrip("v")
    lines, novo = ["## ATT&CK\n"], False
    try:
        idx = http(INDEX)
    except Exception as exc:  # noqa: BLE001
        return [f"## ATT&CK\n\n- ⚠️ index.json inacessível: {exc}\n"], False
    for c in idx["collections"]:
        v = c["versions"][0]
        diff = v["version"] != atual
        novo |= diff
        flag = "🆕 **nova versão — atualizar o catálogo**" if diff else "em dia"
        lines.append(f"- {c['name']}: {v['version']} ({v['modified'][:10]}) — catálogo: {atual} · {flag}")
    return lines + [""], novo


def repos_section():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_repos.py")],
                       capture_output=True, text=True)
    err = (r.stderr.strip().splitlines() or ["sem saída"])[-1][:300]
    out = r.stdout if r.returncode == 0 else f"## Repositórios\n\n- ⚠️ check_repos.py falhou: `{err}`\n"
    counts = {k: int(n) for k, n in re.findall(r"^## (Revisar status|Não encontrados) \((\d+)\)", out, re.M)}
    return out, counts.get("Revisar status", 0) + counts.get("Não encontrados", 0) + (r.returncode != 0)


def upsert_issue(repo, body, actionable):
    base = f"{API}/repos/{repo}/issues"
    found = http(f"{base}?state=open&labels={LABEL}&per_page=10")
    open_issue = next((i for i in found if i.get("title") == TITLE and "pull_request" not in i), None)
    if actionable:
        if open_issue:
            http(f"{base}/{open_issue['number']}", "PATCH", {"body": body})
            return f"issue #{open_issue['number']} atualizada"
        new = http(base, "POST", {"title": TITLE, "body": body, "labels": [LABEL]})
        return f"issue #{new['number']} aberta"
    if open_issue:
        http(f"{base}/{open_issue['number']}/comments", "POST", {"body": "Tudo em dia nesta execução. Fechando."})
        http(f"{base}/{open_issue['number']}", "PATCH", {"state": "closed", "state_reason": "completed"})
        return f"issue #{open_issue['number']} fechada"
    return "nada a fazer"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--issue", action="store_true", help="abre/atualiza/fecha a issue de monitoramento")
    a = ap.parse_args()
    d = model.load()
    att, novo = attack_section(d)
    repos, pend = repos_section()
    actionable = novo or pend > 0
    body = ("\n".join(att) + "\n" + repos
            + "\n---\n_Gerado por `scripts/monitor.py` (workflow monitor). "
              "Registre mudanças com `python3 -m atlas set E### campo=valor`._\n")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(body)
    else:
        print(body)
    if a.issue:
        repo = os.environ.get("REPO")
        if not repo:
            sys.exit("--issue requer REPO=dono/nome")
        print(upsert_issue(repo, body, actionable), file=sys.stderr)


if __name__ == "__main__":
    main()
