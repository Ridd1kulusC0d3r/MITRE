#!/usr/bin/env python3
"""d3fend_xwalk.py — contramedidas D3FEND para técnicas ATT&CK, com alerta para
técnicas revogadas. Somente stdlib.

Fonte: arquivo de mapeamentos completo publicado pelo D3FEND
(d3fend-full-mappings.json, resultado SPARQL). Como os nomes de coluna mudam
entre versões, o script detecta colunas cujo valor contém o ID ATT&CK e
colunas de técnica defensiva automaticamente. Rode --show-columns na primeira
vez para conferir.

Contexto: o issue #709 do d3fend-ontology relata que a ontologia 1.6.0 ainda
mapeia técnicas revogadas no ATT&CK v19. Use --check-revoked para cruzar com o
ATT&CK e descobrir a substituta.

Uso:
    python3 scripts/d3fend_xwalk.py T1059.001
    python3 scripts/d3fend_xwalk.py T1562.001 --check-revoked
    python3 scripts/d3fend_xwalk.py --file d3fend-full-mappings.json --show-columns
"""
import argparse
import json
import re
import signal
import urllib.request

D3FEND_URL = "https://d3fend.mitre.org/ontologies/d3fend/{v}/d3fend-full-mappings.json"
ATTACK_URL = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-{v}.json"
TID = re.compile(r"T\d{4}(?:\.\d{3})?$")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mitre-ecosystem-atlas/2.0"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.load(r)


def local_name(v):
    return re.split(r"[#/]", v)[-1]


def revoked_map(version):
    objs = fetch(ATTACK_URL.format(v=version))["objects"]
    by_ref = {o["id"]: o for o in objs}

    def eid(o):
        return next((r["external_id"] for r in o.get("external_references", []) if r.get("source_name") == "mitre-attack"), None)

    status, sub = {}, {}
    for o in objs:
        if o["type"] == "attack-pattern":
            status[eid(o)] = "revogada" if o.get("revoked") else "depreciada" if o.get("x_mitre_deprecated") else "ativa"
        elif o["type"] == "relationship" and o.get("relationship_type") == "revoked-by":
            s, t = by_ref.get(o["source_ref"]), by_ref.get(o["target_ref"])
            if s and t:
                sub[eid(s)] = eid(t)
    return status, sub


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("technique", nargs="?", help="ex.: T1059 ou T1059.001")
    ap.add_argument("--d3fend-version", default="1.6.0")
    ap.add_argument("--attack-version", default="20.0")
    ap.add_argument("--file", help="d3fend-full-mappings.json local")
    ap.add_argument("--show-columns", action="store_true")
    ap.add_argument("--check-revoked", action="store_true")
    a = ap.parse_args()

    data = json.load(open(a.file, encoding="utf-8")) if a.file else fetch(D3FEND_URL.format(v=a.d3fend_version))
    rows = data.get("results", {}).get("bindings", [])
    if not rows:
        raise SystemExit("Formato inesperado: sem results.bindings.")
    if a.show_columns or not a.technique:
        print("Colunas:", ", ".join(rows[0].keys()))
        print("Exemplo:", {k: v.get("value") for k, v in rows[0].items()})
        return

    tech = a.technique.upper()
    found = {}
    for b in rows:
        flat = {k: v.get("value", "") for k, v in b.items()}
        att_cols = [k for k, v in flat.items() if TID.match(local_name(v))]
        if not any(local_name(flat[k]) == tech for k in att_cols):
            continue
        defense = [k for k in flat if "def" in k.lower() and "label" in k.lower()] or \
                  [k for k in flat if "def" in k.lower() and k not in att_cols]
        tactic = [k for k in flat if "tactic" in k.lower()]
        key = tuple(local_name(flat[k]) if flat[k].startswith("http") else flat[k] for k in defense)
        found[key] = ", ".join(local_name(flat[k]) for k in tactic) if tactic else ""

    if a.check_revoked:
        status, sub = revoked_map(a.attack_version)
        st = status.get(tech, "inexistente")
        msg = f"{tech} no ATT&CK {a.attack_version}: {st}"
        if tech in sub:
            msg += f" → substituta {sub[tech]}. Pesquise também: python3 scripts/d3fend_xwalk.py {sub[tech]}"
        print(msg)

    if not found:
        print(f"Nenhum mapeamento D3FEND {a.d3fend_version} para {tech}.")
        return
    print(f"\n{len(found)} contramedidas D3FEND {a.d3fend_version} para {tech}:")
    for k, tac in sorted(found.items()):
        print(f"- {' · '.join(k)}" + (f"  [{tac}]" if tac else ""))
    print("\nLembrete: mapeamento ontológico é hipótese de controle, não prova de bloqueio.")


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
