#!/usr/bin/env python3
"""attack_diff.py — compara duas versões do ATT&CK e mostra o que mudou para
quem mantém regras de detecção: técnicas novas, revogadas (com substituta),
depreciadas, renomeadas e táticas alteradas. Somente stdlib.

Uso:
    python3 scripts/attack_diff.py 19.2 20.0
    python3 scripts/attack_diff.py 18.1 20.0 --domain enterprise --rules regras/   # cruza com suas regras

Com --rules, procura IDs (T1234 ou T1234.001) em arquivos de texto da pasta e
aponta quais regras citam técnicas revogadas ou depreciadas na versão nova.
"""
import argparse
import signal
import json
import re
import urllib.request
from pathlib import Path

BASE = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master"
TID = re.compile(r"\bT\d{4}(?:\.\d{3})?\b", re.I)


def bundle(domain, version):
    url = f"{BASE}/{domain}-attack/{domain}-attack-{version}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "mitre-ecosystem-atlas/2.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["objects"]


def eid(o):
    for r in o.get("external_references", []):
        if r.get("source_name") == "mitre-attack":
            return r.get("external_id")


def index(objs):
    pats = {}
    tactics = {}
    revoked_by = {}
    by_ref = {o["id"]: o for o in objs}
    for o in objs:
        if o["type"] == "attack-pattern":
            pats[eid(o)] = o
        elif o["type"] == "x-mitre-tactic":
            tactics[eid(o)] = o
        elif o["type"] == "relationship" and o.get("relationship_type") == "revoked-by":
            src, dst = by_ref.get(o["source_ref"]), by_ref.get(o["target_ref"])
            if src and dst:
                revoked_by[eid(src)] = eid(dst)
    return pats, tactics, revoked_by


def state(o):
    if o.get("revoked"):
        return "revogada"
    if o.get("x_mitre_deprecated"):
        return "depreciada"
    return "ativa"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--domain", default="enterprise", choices=["enterprise", "mobile", "ics"])
    ap.add_argument("--rules", help="pasta com regras (Sigma, KQL, SPL...) para cruzar IDs")
    a = ap.parse_args()

    op, ot, _ = index(bundle(a.domain, a.old))
    np_, nt, nrev = index(bundle(a.domain, a.new))

    added = sorted(k for k, o in np_.items() if state(o) == "ativa" and (k not in op or state(op[k]) != "ativa"))
    gone = sorted(k for k, o in np_.items() if state(o) != "ativa" and k in op and state(op[k]) == "ativa")
    renamed = sorted(k for k, o in np_.items() if k in op and state(o) == "ativa" and state(op[k]) == "ativa" and o["name"] != op[k]["name"])
    t_added = sorted(set(k for k, o in nt.items() if state(o) == "ativa") - set(k for k, o in ot.items() if state(o) == "ativa"))
    t_renamed = sorted(k for k in nt if k in ot and nt[k]["name"] != ot[k]["name"])

    print(f"# ATT&CK {a.domain}: {a.old} → {a.new}\n")
    print(f"## Táticas novas ({len(t_added)})")
    for k in t_added:
        print(f"- {k} {nt[k]['name']}")
    print(f"\n## Táticas renomeadas ({len(t_renamed)})")
    for k in t_renamed:
        print(f"- {k}: {ot[k]['name']} → {nt[k]['name']}")
    print(f"\n## Técnicas novas ou reativadas ({len(added)})")
    for k in added:
        print(f"- {k} {np_[k]['name']}")
    print(f"\n## Técnicas que saíram ({len(gone)})")
    for k in gone:
        dest = nrev.get(k)
        tail = f" → substituída por {dest} {np_[dest]['name']}" if dest and dest in np_ else ""
        print(f"- {k} {np_[k]['name']} ({state(np_[k])}){tail}")
    print(f"\n## Técnicas renomeadas ({len(renamed)})")
    for k in renamed:
        print(f"- {k}: {op[k]['name']} → {np_[k]['name']}")

    if a.rules:
        print("\n## Regras que citam técnicas fora de uso na versão nova\n")
        hits = 0
        for f in sorted(Path(a.rules).rglob("*")):
            if not f.is_file() or f.stat().st_size > 2_000_000:
                continue
            try:
                txt = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for t in sorted({m.upper() for m in TID.findall(txt)}):
                o = np_.get(t)
                if o and state(o) != "ativa":
                    hits += 1
                    dest = nrev.get(t)
                    print(f"- `{f}` cita {t} ({state(o)})" + (f" → usar {dest}" if dest else ""))
        if not hits:
            print("Nenhuma regra cita técnicas revogadas ou depreciadas.")


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # permite usar com head/less
    main()
