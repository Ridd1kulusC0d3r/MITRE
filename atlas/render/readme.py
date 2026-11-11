"""Blocos gerados do README. Cada bloco fica entre <!-- nome:start --> e <!-- nome:end -->;
o texto fora dos marcadores é escrito à mão e preservado."""
import re
from collections import Counter
from urllib.parse import quote


def _block(name):
    return re.compile(rf"<!-- {name}:start -->.*?<!-- {name}:end -->", re.S)


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


def _shield(label, message, color, link, extra=""):
    def enc(s):
        return quote(str(s).replace("-", "--").replace("_", "__"), safe="")
    return f"[![{label}](https://img.shields.io/badge/{enc(label)}-{enc(message)}-{color}?style=flat-square{extra})]({link})"


def _ver(d, i):
    e = next((x for x in d["entries"] if x["id"] == i), {})
    return next((t for t in e.get("version", "").split() if any(c.isdigit() for c in t)), "?")


def br_date(iso):
    y, m, dd = iso.split("-")
    return f"{dd}/{m}/{y}"


def hero_block(d, th):
    c = th.badge_colors
    badges = [
        _shield("ATT&CK", _ver(d, "E001"), c["attack"], "https://attack.mitre.org/"),
        _shield("D3FEND", _ver(d, "E002"), c["d3fend"], "https://d3fend.mitre.org/"),
        _shield("ATLAS", _ver(d, "E004"), c["atlas"], "https://atlas.mitre.org/"),
        _shield("Python", "stdlib only", c["python"], "atlas/", "&logo=python&logoColor=white"),
        _shield("revisão", br_date(d["reviewed_on"]), c["review"], "docs/historico-e-manutencao.md"),
        _shield("idioma", "pt-BR", c["lang"], "#"),
    ]
    alt = f"{th.name} — {th.tagline.lower()}: {len(d['entries'])} recursos em 15 camadas"
    return ("<!-- hero:start -->\n"
            "<picture>\n"
            '  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">\n'
            f'  <img src="assets/banner-light.svg" alt="{alt}" width="100%">\n'
            "</picture>\n\n" + "\n".join(badges) + "\n<!-- hero:end -->")


def map_block(d):
    alt = ("Mapa de camadas: adversário, modelagem, telemetria, detecção, validação, resposta e maturidade, "
           "com defesa e engano como apoio e uma fundação de vulnerabilidade, CTI, dados, conformidade, padrões e formação")
    return ("<!-- map:start -->\n<picture>\n"
            '  <source media="(prefers-color-scheme: dark)" srcset="assets/mapa-camadas-dark.svg">\n'
            f'  <img src="assets/mapa-camadas-light.svg" alt="{alt}" width="100%">\n'
            "</picture>\n<!-- map:end -->")


def reviewed_block(d):
    return f"<!-- reviewed:start -->**{br_date(d['reviewed_on'])}**<!-- reviewed:end -->"


def render(d, current, th=None):
    blocks = {"stats": stats_block(d), "reviewed": reviewed_block(d), "map": map_block(d)}
    if th is not None:
        blocks["hero"] = hero_block(d, th)
    out = current
    for name, content in blocks.items():
        out = _block(name).sub(lambda _, c=content: c, out)
    return out
