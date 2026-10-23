#!/usr/bin/env python3
"""capec_xwalk.py — cadeia CWE → CAPEC → ATT&CK a partir dos dados STIX oficiais,
conferindo cada técnica contra uma versão do ATT&CK. Somente stdlib.

O CAPEC é publicado em STIX 2.1 no repositório mitre/cti. Mapeamentos CAPEC →
ATT&CK são mantidos pelo CAPEC e podem citar técnicas que o ATT&CK já revogou;
o script marca esses casos e indica a substituta quando o ATT&CK declara uma.

Uso:
    python3 scripts/capec_xwalk.py > crosswalks/cwe-capec-attack.tsv
    python3 scripts/capec_xwalk.py --cwe CWE-79          # filtra por fraqueza
    python3 scripts/capec_xwalk.py --attack-version 20.0 --stale-only
"""
import argparse
import json
import signal
import sys
import urllib.request

CAPEC_URL = "https://raw.githubusercontent.com/mitre/cti/master/capec/2.1/stix-capec.json"
ATTACK_URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-{v}.json"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mitre-ecosystem-atlas/2.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["objects"]


def attack_index(version):
    objs = fetch(ATTACK_URL.format(v=version))
    by_ref = {o["id"]: o for o in objs}

    def eid(o):
        return next((r["external_id"] for r in o.get("external_references", []) if r.get("source_name") == "mitre-attack"), None)

    tech, revoked_by = {}, {}
    for o in objs:
        if o["type"] == "attack-pattern":
            st = "revogada" if o.get("revoked") else "depreciada" if o.get("x_mitre_deprecated") else "ativa"
            tech[eid(o)] = (o["name"], st)
        elif o["type"] == "relationship" and o.get("relationship_type") == "revoked-by":
            s, t = by_ref.get(o["source_ref"]), by_ref.get(o["target_ref"])
            if s and t:
                revoked_by[eid(s)] = eid(t)
    return tech, revoked_by


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cwe", help="ex.: CWE-79")
    ap.add_argument("--attack-version", default="20.0")
    ap.add_argument("--stale-only", action="store_true", help="só mapeamentos para técnicas fora de uso")
    a = ap.parse_args()

    tech, revoked_by = attack_index(a.attack_version)
    rows, stale = 0, 0
    print("capec_id\tcapec\tcwe\tattack_id\tattack_nome\tattack_status\tsubstituta")
    for o in fetch(CAPEC_URL):
        if o["type"] != "attack-pattern" or o.get("revoked") or o.get("x_capec_status") == "Deprecated":
            continue
        refs = o.get("external_references", [])
        capec = next((r["external_id"] for r in refs if r.get("source_name") == "capec"), "")
        cwes = sorted({r["external_id"] for r in refs if r.get("source_name") == "cwe"})
        atts = sorted({"T" + r["external_id"].lstrip("T") for r in refs if r.get("source_name") == "ATTACK"})
        if a.cwe and a.cwe.upper() not in cwes:
            continue
        for t in atts:
            name, st = tech.get(t, ("(não existe nesta versão)", "inexistente"))
            sub = revoked_by.get(t, "")
            if st != "ativa":
                stale += 1
            elif a.stale_only:
                continue
            rows += 1
            print(f"{capec}\t{o['name']}\t{','.join(cwes)}\t{t}\t{name}\t{st}\t{sub}")
    print(f"# {rows} linhas; {stale} apontam para técnicas fora de uso no ATT&CK {a.attack_version}", file=sys.stderr)


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
