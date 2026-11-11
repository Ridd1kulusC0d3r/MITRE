"""assets/banner.svg"""
from atlas.render.text import MAIN_FLOW, xml


def render(d, th):
    """Banner 1280×320 com uma 'matriz' estilizada à direita (decorativa, determinística)."""
    FONT, MONO = th.font, th.mono
    flow_colors = [th.layer_color[k] for k in MAIN_FLOW]
    n = len(d["entries"])
    by_id = {e["id"]: e for e in d["entries"]}

    def ver(i):  # primeiro token com dígitos da versão registrada
        return next(t for t in by_id[i]["version"].split() if any(c.isdigit() for c in t))

    chips = [f"ATT&CK {ver('E001')}", f"D3FEND {ver('E002')}", f"ATLAS {ver('E004')}", f"{n} recursos"]
    cells = []
    seed = 7
    cols, rows = 15, 9
    for c in range(cols):
        for r in range(rows):
            seed = (seed * 1103515245 + 12345) % 2 ** 31
            if (seed >> 8) % 100 < 18:
                continue
            lvl = (seed >> 3) % 5
            op = [0.10, 0.18, 0.32, 0.55, 0.85][lvl]
            color = flow_colors[(c + r * 2) % 7]
            cells.append(f'<rect x="{760 + c * 32}" y="{40 + r * 28}" width="27" height="22" rx="4" fill="{color}" opacity="{op}"/>')
    chip_svg, x = [], 64
    for ch in chips:
        w = 18 + 8.4 * len(ch)
        chip_svg.append(f'<rect x="{x}" y="226" width="{w:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity="0.08" stroke="#ffffff" stroke-opacity="0.22"/>'
                        f'<text x="{x + w / 2:.0f}" y="248" text-anchor="middle" {MONO} font-size="14" fill="#e6edf3">{xml(ch)}</text>')
        x += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="320" viewBox="0 0 1280 320" role="img" aria-label="MITRE Ecosystem Atlas: {n} recursos mapeados">
  <!-- GERADO por scripts/build_catalog.py -->
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1020"/><stop offset="0.6" stop-color="#111a33"/><stop offset="1" stop-color="#1a1240"/>
    </linearGradient>
    <linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#0b1020" stop-opacity="1"/><stop offset="0.35" stop-color="#0b1020" stop-opacity="0"/></linearGradient>
  </defs>
  <rect width="1280" height="320" rx="18" fill="url(#bg)"/>
  {''.join(cells)}
  <rect x="740" y="0" width="540" height="320" fill="url(#fade)"/>
  <text x="64" y="84" {MONO} font-size="15" letter-spacing="4" fill="#7d8bb0">CTI · DETECTION ENGINEERING · PURPLE TEAM · IR</text>
  <text x="62" y="146" {FONT} font-size="58" font-weight="800" fill="#ffffff">MITRE <tspan fill="#7ee0d6">Ecosystem</tspan> Atlas</text>
  <text x="64" y="192" {FONT} font-size="24" fill="#c9d1e9">Da inteligência à defesa validada · curadoria em português</text>
  {''.join(chip_svg)}
  <text x="64" y="296" {FONT} font-size="13" fill="#6b7896">Revisão {d["reviewed_on"]} · independente, sem afiliação ou endosso da MITRE</text>
</svg>
'''
