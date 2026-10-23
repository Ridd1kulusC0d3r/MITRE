#!/usr/bin/env python3
"""attack_dump.py — lista técnicas ATT&CK ativas por tática, com CAPEC e
quantidade de Detection Strategies. Somente stdlib.

Uso:
    python3 scripts/attack_dump.py                         # enterprise, versão 20.0, Markdown
    python3 scripts/attack_dump.py --domain ics --version 20.0
    python3 scripts/attack_dump.py --format tsv > tecnicas.tsv
    python3 scripts/attack_dump.py --file enterprise-attack-20.0.json   # bundle local

Saída de contagem vai para stderr; a listagem vai para stdout.
"""
import argparse
import signal
import json
import sys
import urllib.request
from collections import defaultdict

BASE = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mitre-ecosystem-atlas/2.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def load_bundle(domain, version, path=None):
    if path:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    name = f"{domain}-attack"
    suffix = f"-{version}" if version != "latest" else ""
    return fetch(f"{BASE}/{name}/{name}{suffix}.json")


def ext_id(obj, source="mitre-attack"):
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == source:
            return ref.get("external_id")
    return None


def active(o):
    return not o.get("revoked") and not o.get("x_mitre_deprecated")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", default="enterprise", choices=["enterprise", "mobile", "ics"])
    ap.add_argument("--version", default="20.0", help="ex.: 20.0, 19.2 ou latest")
    ap.add_argument("--file", help="bundle STIX local (ignora --domain/--version)")
    ap.add_argument("--format", default="md", choices=["md", "tsv"])
    a = ap.parse_args()

    objs = load_bundle(a.domain, a.version, a.file)["objects"]
    by_ref = {o["id"]: o for o in objs}

    # Detection Strategies por técnica (relationship 'detects')
    dets = defaultdict(int)
    for o in objs:
        if o["type"] == "relationship" and o.get("relationship_type") == "detects" and active(o):
            src = by_ref.get(o["source_ref"], {})
            if src.get("type") == "x-mitre-detection-strategy":
                dets[o["target_ref"]] += 1

    tactics = {o["x_mitre_shortname"]: (ext_id(o), o["name"])
               for o in objs if o["type"] == "x-mitre-tactic" and active(o)}
    by_tactic = defaultdict(list)
    for o in objs:
        if o["type"] != "attack-pattern" or not active(o):
            continue
        capec = [r["external_id"] for r in o.get("external_references", []) if r.get("source_name") == "capec"]
        for kc in o.get("kill_chain_phases", []):
            by_tactic[kc["phase_name"]].append((ext_id(o), o["name"], capec, dets.get(o["id"], 0)))

    counts = defaultdict(int)
    for o in objs:
        if active(o) and o["type"] not in ("relationship", "marking-definition", "identity"):
            t = o["type"]
            if t == "attack-pattern":
                t = "subtécnica" if o.get("x_mitre_is_subtechnique") else "técnica"
            counts[t] += 1
    print(json.dumps(dict(sorted(counts.items())), ensure_ascii=False, indent=2), file=sys.stderr)

    order = sorted(tactics.items(), key=lambda x: x[1][0])
    if a.format == "tsv":
        print("tatica_id\ttatica\ttecnica_id\ttecnica\tcapec\tdetection_strategies")
        for short, (taid, tname) in order:
            for tid, name, capec, n in sorted(by_tactic[short]):
                print(f"{taid}\t{tname}\t{tid}\t{name}\t{','.join(capec)}\t{n}")
        return
    print(f"# ATT&CK {a.domain} {a.version}\n")
    for short, (taid, tname) in order:
        items = sorted(by_tactic[short])
        print(f"\n## {taid} · {tname} ({len(items)})\n")
        for tid, name, capec, n in items:
            extra = []
            if capec:
                extra.append("CAPEC " + ", ".join(capec))
            extra.append(f"{n} Detection Strateg{'y' if n == 1 else 'ies'}")
            print(f"- [{tid}](https://attack.mitre.org/techniques/{tid.replace('.', '/')}/) {name} — {'; '.join(extra)}")


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # permite usar com head/less
    main()
