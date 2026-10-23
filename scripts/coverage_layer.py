#!/usr/bin/env python3
"""coverage_layer.py — conta quantas regras/testes citam cada técnica ATT&CK
num diretório (Sigma, Atomic Red Team, Splunk, Elastic ou suas próprias regras)
e gera uma camada do ATT&CK Navigator. Somente stdlib.

Isto mede QUANTIDADE DE ARTEFATOS que citam a técnica, não cobertura de
detecção. Use como mapa de onde há material para começar, nunca como prova.

Uso:
    git clone --depth 1 https://github.com/SigmaHQ/sigma.git
    python3 scripts/coverage_layer.py sigma/rules --name "Sigma" -o sigma-layer.json
    git clone --depth 1 https://github.com/redcanaryco/atomic-red-team.git
    python3 scripts/coverage_layer.py atomic-red-team/atomics --mode dirs --name "Atomic" -o atomic-layer.json
    python3 scripts/coverage_layer.py sigma/rules --tsv > sigma.tsv
    python3 scripts/coverage_layer.py --merge sigma-layer.json atomic-layer.json -o lacunas.json

--mode tags  procura IDs no conteúdo (attack.t1059.001, T1059.001...)  [padrão]
--mode dirs  usa nomes de diretório no formato T1234 ou T1234.001 (Atomic)
--merge      combina duas camadas: score 1 = só a 1ª tem, 2 = só a 2ª, 3 = ambas
"""
import argparse
import json
import re
import signal
import sys
from collections import Counter
from pathlib import Path

TAG = re.compile(r"(?<![A-Za-z0-9])(?:attack\.)?t(\d{4})(?:\.(\d{3}))?(?![0-9])", re.I)
DIR = re.compile(r"^T(\d{4})(?:\.(\d{3}))?$", re.I)
EXT = {".yml", ".yaml", ".toml", ".json", ".md", ".txt", ".kql", ".spl", ".sigma"}


def scan(root, mode):
    c = Counter()
    root = Path(root)
    if mode == "dirs":
        for p in root.iterdir():
            m = DIR.match(p.name)
            if p.is_dir() and m:
                c[f"T{m.group(1)}" + (f".{m.group(2)}" if m.group(2) else "")] += 1
        return c
    for f in root.rglob("*"):
        if f.suffix.lower() not in EXT or not f.is_file():
            continue
        txt = f.read_text(encoding="utf-8", errors="ignore")
        ids = set()
        for m in TAG.finditer(txt):
            ids.add(f"T{m.group(1)}" + (f".{m.group(2)}" if m.group(2) else ""))
        for t in ids:
            c[t] += 1
    return c


def layer(name, counts, desc):
    mx = max(counts.values()) if counts else 1
    return {
        "name": name,
        "versions": {"attack": "20", "navigator": "5.3.2", "layer": "4.5"},
        "domain": "enterprise-attack",
        "description": desc,
        "gradient": {"colors": ["#e8f1ff", "#1f6feb"], "minValue": 0, "maxValue": mx},
        "legendItems": [{"label": "0 artefatos", "color": "#ffffff"}, {"label": f"{mx} artefatos", "color": "#1f6feb"}],
        "techniques": [{"techniqueID": t, "score": n, "comment": f"{n} artefato(s) citam esta técnica"} for t, n in sorted(counts.items())],
    }


def merge(a_path, b_path):
    a = json.load(open(a_path, encoding="utf-8"))
    b = json.load(open(b_path, encoding="utf-8"))
    sa = {t["techniqueID"] for t in a["techniques"]}
    sb = {t["techniqueID"] for t in b["techniques"]}
    techs = []
    for t in sorted(sa | sb):
        s = (1 if t in sa else 0) + (2 if t in sb else 0)
        label = {1: f"só {a['name']}", 2: f"só {b['name']}", 3: "ambos"}[s]
        techs.append({"techniqueID": t, "score": s, "comment": label})
    return {
        "name": f"{a['name']} × {b['name']}", "versions": a["versions"], "domain": a["domain"],
        "description": "1 = só a primeira camada; 2 = só a segunda; 3 = ambas. Técnicas sem cor não aparecem em nenhuma.",
        "gradient": {"colors": ["#f4a261", "#2a9d8f", "#264653"], "minValue": 1, "maxValue": 3},
        "legendItems": [{"label": f"só {a['name']}", "color": "#f4a261"}, {"label": f"só {b['name']}", "color": "#2a9d8f"}, {"label": "ambos", "color": "#264653"}],
        "techniques": techs,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", nargs="?")
    ap.add_argument("--mode", default="tags", choices=["tags", "dirs"])
    ap.add_argument("--name", default="Cobertura de artefatos")
    ap.add_argument("--tsv", action="store_true")
    ap.add_argument("--merge", nargs=2, metavar=("A", "B"))
    ap.add_argument("-o", "--output")
    a = ap.parse_args()

    if a.merge:
        out = merge(*a.merge)
    else:
        if not a.path:
            ap.error("informe o diretório ou use --merge")
        counts = scan(a.path, a.mode)
        print(f"# {len(counts)} técnicas citadas em {a.path}", file=sys.stderr)
        if a.tsv:
            print("tecnica\tartefatos")
            for t, n in counts.most_common():
                print(f"{t}\t{n}")
            return
        out = layer(a.name, counts, f"Artefatos em {a.path} que citam cada técnica. Não equivale a cobertura de detecção.")
    text = json.dumps(out, ensure_ascii=False, indent=2)
    if a.output:
        Path(a.output).write_text(text + "\n", encoding="utf-8")
        print(f"camada gravada em {a.output} ({len(out['techniques'])} técnicas)", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
