"""assets/banner-{dark,light}.svg

Lado esquerdo: marca, título, versões. Lado direito: o catálogo como dado — uma
coluna por camada (fluxo, apoio, fundação), um bloco por recurso.
"""
from atlas.render.brand import mark_shapes
from atlas.render.text import FOUNDATION, MAIN_FLOW, SUPPORT, xml

GROUPS = [("FLUXO", MAIN_FLOW), ("APOIO", SUPPORT), ("FUNDAÇÃO", FOUNDATION)]


def render(d, th, mode="dark"):
    FONT, MONO = th.font, th.mono
    b, m = th.brand, th.mode(mode)
    dark = mode == "dark"
    title, sub, kicker = (b["white"], b["mist"], b["dim"]) if dark else (m["ink"], m["muted"], m["muted"])
    accent = b["teal"] if dark else b["teal_deep"]
    n = len(d["entries"])
    by_id = {e["id"]: e for e in d["entries"]}
    count = {}
    for e in d["entries"]:
        count[e["layer"]] = count.get(e["layer"], 0) + 1

    def ver(i):
        return next((t for t in by_id[i].get("version", "").split() if any(c.isdigit() for c in t)), "")

    chips = [f"ATT&CK {ver('E001')}", f"D3FEND {ver('E002')}", f"ATLAS {ver('E004')}", f"{n} recursos"]
    chip_svg, x = [], 64
    for ch in chips:
        w = 18 + 8.4 * len(ch)
        fill = f'fill="{b["white"]}" fill-opacity="0.07" stroke="{b["white"]}" stroke-opacity="0.22"' if dark \
            else f'fill="{m["surface"]}" stroke="{m["line"]}"'
        chip_svg.append(f'<rect x="{x}" y="222" width="{w:.0f}" height="34" rx="17" {fill}/>'
                        f'<text x="{x + w / 2:.0f}" y="244" text-anchor="middle" {MONO} font-size="14" fill="{sub}">{xml(ch)}</text>')
        x += w + 12

    # colunas de dados: 15 camadas, bloco 18×9, passo vertical 12
    cols, cx, base_y = [], 812, 286
    unit = max(1, -(-max(count.values(), default=1) // 20))  # 1 bloco = `unit` recursos (no máximo 20 blocos)
    for label, keys in GROUPS:
        gx = cx
        for k in keys:
            blocks = -(-count.get(k, 0) // unit)
            col = th.layer_color[k]
            for i in range(blocks):
                cols.append(f'<rect x="{cx}" y="{base_y - 9 - i * 12}" width="18" height="9" rx="2.5" fill="{col}" opacity="{0.92 - 0.02 * i:.2f}"/>')
            cx += 26
        cols.append(f'<text x="{gx}" y="{base_y + 20}" {MONO} font-size="10" letter-spacing="1.5" fill="{kicker}">{label}</text>')
        cx += 14
    top_blocks = max(-(-c // unit) for c in count.values())
    legend = f"1 bloco = {unit} recurso{'s' if unit > 1 else ''}"
    if dark:
        bg = (f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{b["night"]}"/>'
              f'<stop offset="0.6" stop-color="{b["night_2"]}"/><stop offset="1" stop-color="{b["dusk"]}"/></linearGradient>')
    else:
        bg = (f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{m["surface"]}"/>'
              f'<stop offset="1" stop-color="{m["surface_2"]}"/></linearGradient>')
    border = "" if dark else f' stroke="{m["line"]}"'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="320" viewBox="0 0 1280 320" role="img" aria-label="{xml(th.name)}: {n} recursos mapeados em 15 camadas">
  <!-- GERADO por python3 -m atlas build a partir de data/entries e design/tokens.json -->
  <defs>{bg}</defs>
  <rect x="0.5" y="0.5" width="1279" height="319" rx="18" fill="url(#bg)"{border}/>
  {mark_shapes(accent, kicker, b["night"] if dark else m["surface"], x=64, y=46, size=40)}
  <text x="118" y="72" {MONO} font-size="13" letter-spacing="3.5" fill="{kicker}">CTI · DETECTION ENGINEERING · PURPLE TEAM · IR</text>
  <text x="62" y="148" {FONT} font-size="56" font-weight="800" fill="{title}">MITRE <tspan fill="{accent}">Ecosystem</tspan> Atlas</text>
  <text x="64" y="192" {FONT} font-size="23" fill="{sub}">{xml(th.tagline)} · curadoria em português</text>
  {''.join(chip_svg)}
  <text x="64" y="296" {FONT} font-size="13" fill="{kicker}">Revisão {d["reviewed_on"]} · {xml(th.disclaimer)}</text>
  {''.join(cols)}
  <text x="{cx - 14}" y="{base_y - 9 - top_blocks * 12 - 4}" text-anchor="end" {MONO} font-size="10" fill="{kicker}">{legend}</text>
</svg>
'''
