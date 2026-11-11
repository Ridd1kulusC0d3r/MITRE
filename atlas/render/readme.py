"""Bloco de números do README (entre <!-- stats:start --> e <!-- stats:end -->)."""
import re
from collections import Counter

STATS = re.compile(r"<!-- stats:start -->.*?<!-- stats:end -->", re.S)


def stats_block(d):
    c_owner = Counter(e["owner_type"] for e in d["entries"])
    c_status = Counter(e["status"] for e in d["entries"])
    layers = len({e["layer"] for e in d["entries"]})
    n = len(d["entries"])
    rels = sum(len(e.get("relations", [])) for e in d["entries"])
    return ("<!-- stats:start -->\n"
            f"| 📦 Entradas | 🟦 MITRE | 🟩 CTID | 🟨🟧 Comunidade e fornecedores | 🔗 Relações | 🧱 Camadas | ✅ Ativos | 🗄️ Históricos |\n"
            "|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"
            f"| **{n}** | {c_owner['mitre']} | {c_owner['ctid']} | {c_owner['comunidade'] + c_owner['fornecedor']} "
            f"| {rels} | {layers} | {c_status['ativo']} | {len(d['historical'])} |\n"
            "<!-- stats:end -->")


def render(d, current):
    return STATS.sub(lambda _: stats_block(d), current)
