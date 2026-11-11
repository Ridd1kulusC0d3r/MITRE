"""Identidade visual: lê design/tokens.json e expõe o que os renderizadores usam.

Única porta de entrada de cor no código. Nenhum outro módulo de atlas/ ou site/
contém literal de cor (tests/test_atlas.py confere).
"""
import json
from functools import lru_cache
from pathlib import Path

from atlas.color import readable_on
from atlas.paths import Paths


@lru_cache(maxsize=None)
def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


class Theme:
    def __init__(self, p=None):
        t = _load(str((p or Paths()).tokens))
        self.tokens = t
        self.name = t.get("name", "MITRE Ecosystem Atlas")
        self.tagline = t.get("tagline", "")
        self.disclaimer = t.get("disclaimer", "")
        self.repo_url = t.get("repo_url", "")
        self.brand = t.get("brand", {})
        self.modes = t.get("theme", {})
        self.layer_order = list(t["layers"])
        self.layer_color = {k: v["color"] for k, v in t["layers"].items()}
        self.layer_icon = {k: v["emoji"] for k, v in t["layers"].items()}
        self.layer_title = {k: v["title"] for k, v in t["layers"].items()}
        self.layer_svg = {k: v.get("icon", "") for k, v in t["layers"].items()}
        self.owner_badge = t["owner_badge"]
        self.status_badge = t["status_badge"]
        f = t["font"]
        self.font = f'font-family="{f["svg_sans"]}"'
        self.mono = f'font-family="{f["svg_mono"]}"'
        self.badge_colors = t.get("badge_colors", {})
        self.radius = t.get("radius", {})

    def mode(self, name):
        return self.modes[name]

    def layer_ink(self, k, mode):
        """Cor da camada legível como texto (4,5:1) sobre a superfície do tema."""
        surface = self.modes[mode]["surface"]
        toward = "#000000" if mode == "light" else "#ffffff"
        return readable_on(self.layer_color[k], surface, 4.5, toward)

    def icon(self, k, size=24, stroke=1.8, color="currentColor", x=None, y=None):
        """Ícone de camada como <svg> embutível (traço único, grade 24)."""
        pos = f' x="{x}" y="{y}"' if x is not None else ""
        return (f'<svg{pos} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
                f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                f'{self.layer_svg[k].replace(chr(39), chr(34))}</svg>')

    def css(self):
        """assets/tokens.css: variáveis CSS para os dois temas + cores de camada."""
        def block(mode):
            m = self.modes[mode]
            lines = [f"--{k.replace('_', '-')}:{v};" for k, v in m.items()]
            lines += [f"--l-{k}:{self.layer_color[k]};--l-{k}-ink:{self.layer_ink(k, mode)};" for k in self.layer_order]
            return "".join(lines)
        b = self.brand
        brand = "".join(f"--brand-{k.replace('_', '-')}:{v};" for k, v in b.items())
        f = self.tokens["font"]
        r = "".join(f"--r-{k}:{v}px;" for k, v in self.radius.items())
        light, dark = block("light"), block("dark")
        return ("/* ARQUIVO GERADO por python3 -m atlas build a partir de design/tokens.json. Não edite à mão. */\n"
                f":root{{{brand}{r}--sans:{f['sans']};--mono:{f['mono']};{light}color-scheme:light}}\n"
                f"@media (prefers-color-scheme:dark){{:root:not([data-theme=\"light\"]){{{dark}color-scheme:dark}}}}\n"
                f":root[data-theme=\"dark\"]{{{dark}color-scheme:dark}}\n"
                + "".join(f".l-{k}{{--c:var(--l-{k});--c-ink:var(--l-{k}-ink)}}" for k in self.layer_order) + "\n")
