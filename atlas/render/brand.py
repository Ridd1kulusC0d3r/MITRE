"""Marca: símbolo, favicon e imagem social (SVG; o PNG sai de scripts/render_social.py).

Símbolo: grade 3×3 de células arredondadas com a diagonal ascendente acesa e uma
rota ligando-as. Lê-se como a matriz ATT&CK percorrida do adversário à resposta.
Funciona em uma cor (currentColor) e em 16 px.
"""
from atlas.render.text import xml


def mark_shapes(lit, dim, route, x=0, y=0, size=64, dim_opacity=0.35):
    s = size / 64
    cells = []
    for r in range(3):
        for c in range(3):
            cx, cy = x + (4 + c * 20) * s, y + (4 + r * 20) * s
            on = (r + c) == 2
            fill = lit if on else dim
            op = "" if on else f' fill-opacity="{dim_opacity}"'
            cells.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{16 * s:.1f}" height="{16 * s:.1f}" rx="{4 * s:.1f}" fill="{fill}"{op}/>')
    p = [(x + (12 + c * 20) * s, y + (12 + r * 20) * s) for r, c in ((2, 0), (1, 1), (0, 2))]
    path = (f'<path d="M{p[0][0]:.1f} {p[0][1]:.1f} L{p[1][0]:.1f} {p[1][1]:.1f} L{p[2][0]:.1f} {p[2][1]:.1f}" '
            f'stroke="{route}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" fill="none"/>')
    return "".join(cells) + path


def mark(th):
    b = th.brand
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="{xml(th.name)}">'
            f'<!-- GERADO por python3 -m atlas build -->{mark_shapes(b["teal"], b["dim"], b["night"])}</svg>\n')


def favicon(th):
    b = th.brand
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 64 64">'
            f'<!-- GERADO por python3 -m atlas build --><rect width="64" height="64" rx="14" fill="{b["night"]}"/>'
            f'{mark_shapes(b["teal"], b["mist"], b["night"], x=6, y=6, size=52, dim_opacity=0.28)}</svg>\n')


def social(d, th):
    """1280×640 para a pré-visualização do GitHub (convertida em PNG por scripts/render_social.py)."""
    b, FONT, MONO = th.brand, th.font, th.mono
    n = len(d["entries"])
    by_id = {e["id"]: e for e in d["entries"]}

    def ver(i):
        return next((t for t in by_id[i].get("version", "").split() if any(c.isdigit() for c in t)), "")
    chips = [f"ATT&CK {ver('E001')}", f"D3FEND {ver('E002')}", f"ATLAS {ver('E004')}", f"{n} recursos"]
    x, chip_svg = 96, []
    for ch in chips:
        w = 26 + 11 * len(ch)
        chip_svg.append(f'<rect x="{x}" y="430" width="{w:.0f}" height="48" rx="24" fill="{b["white"]}" fill-opacity="0.07" stroke="{b["white"]}" stroke-opacity="0.22"/>'
                        f'<text x="{x + w / 2:.0f}" y="461" text-anchor="middle" {MONO} font-size="19" fill="{b["mist"]}">{xml(ch)}</text>')
        x += w + 14
    stripes = "".join(f'<rect x="{96 + i * (1088 / 15):.1f}" y="560" width="{1088 / 15 - 6:.1f}" height="8" rx="4" fill="{th.layer_color[k]}"/>'
                      for i, k in enumerate(th.layer_order))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">
  <!-- GERADO por python3 -m atlas build -->
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{b["night"]}"/><stop offset="0.6" stop-color="{b["night_2"]}"/><stop offset="1" stop-color="{b["dusk"]}"/></linearGradient></defs>
  <rect width="1280" height="640" fill="url(#g)"/>
  {mark_shapes(b["teal"], b["dim"], b["night"], x=96, y=96, size=96)}
  <text x="96" y="290" {FONT} font-size="76" font-weight="800" fill="{b["white"]}">MITRE <tspan fill="{b["teal"]}">Ecosystem</tspan> Atlas</text>
  <text x="98" y="352" {FONT} font-size="32" fill="{b["mist"]}">{xml(th.tagline)} · curadoria em português</text>
  {''.join(chip_svg)}
  {stripes}
  <text x="96" y="608" {FONT} font-size="18" fill="{b["faint"]}">{xml(th.disclaimer[:1].upper() + th.disclaimer[1:])}</text>
</svg>
'''
