"""assets/mapa-camadas-{dark,light}.svg"""
from atlas.render.text import FOUNDATION, MAIN_FLOW, fit, xml


def render(d, th, mode="dark"):
    """Mapa de camadas: fluxo principal, apoios e fundação, com ícone, contagem e exemplos."""
    FONT, MONO = th.font, th.mono
    m = th.mode(mode)
    v = d["vocab"]["layer"]
    groups = {}
    for e in d["entries"]:
        groups.setdefault(e["layer"], []).append(e)
    for k in groups:
        groups[k].sort(key=lambda e: (e["priority"], e["name"]))

    def node(k, x, y, w, h=132):
        items = groups.get(k, [])
        col, ink = th.layer_color[k], th.layer_ink(k, mode)
        inner = w - 28
        lines = "".join(f'<text x="{x + 14:.0f}" y="{y + 84 + i * 16}" {FONT} font-size="12" fill="{m["ink"]}" fill-opacity="0.82">{xml(fit(e["name"], inner, 6.1))}</text>'
                        for i, e in enumerate(items[:3]))
        return (f'<g><rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{h}" rx="12" fill="{m["surface"]}" stroke="{col}" stroke-width="1.5"/>'
                f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="5" rx="2.5" fill="{col}"/>'
                + th.icon(k, size=18, stroke=2, color=ink, x=f"{x + 12:.0f}", y=y + 17)
                + f'<text x="{x + 36:.0f}" y="{y + 32}" {FONT} font-size="15" font-weight="700" fill="{m["ink"]}">{xml(fit(th.layer_title[k], inner - 24, 8.0))}</text>'
                f'<text x="{x + w - 14:.0f}" y="{y + 57}" text-anchor="end" {MONO} font-size="15" font-weight="700" fill="{ink}">{len(items)}</text>'
                f'<text x="{x + 14:.0f}" y="{y + 56}" {FONT} font-size="11" fill="{m["muted"]}">{xml(fit(v[k], inner - 36, 5.5))}</text>{lines}</g>')

    arrow, loop = m["muted"], m["line"]
    parts = []
    left, avail, gap, y = 40, 1200, 24, 196
    w = (avail - gap * (len(MAIN_FLOW) - 1)) / len(MAIN_FLOW)
    xs = [left + i * (w + gap) for i in range(len(MAIN_FLOW))]
    for i, k in enumerate(MAIN_FLOW):
        parts.append(node(k, xs[i], y, w))
        if i < len(MAIN_FLOW) - 1:
            ax = xs[i] + w
            parts.append(f'<path d="M{ax + 3:.0f} {y + 66} H{ax + gap - 5:.0f}" stroke="{arrow}" stroke-width="2.5" marker-end="url(#arr)"/>')
    loop_y = y + 132 + 22
    parts.append(f'<path d="M{xs[-1] + w / 2:.0f} {y + 134} V{loop_y} H{xs[0] + w / 2:.0f} V{y + 140}" fill="none" stroke="{arrow}" stroke-opacity="0.6" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>'
                 f'<rect x="550" y="{loop_y - 10}" width="180" height="20" fill="{m["bg"]}"/>'
                 f'<text x="640" y="{loop_y + 4}" text-anchor="middle" {FONT} font-size="12" fill="{m["muted"]}">lacunas viram novo ciclo</text>')
    for k, a, b in (("defesa", 1, 2), ("engano", 3, 4)):
        cx = (xs[a] + xs[b] + w) / 2
        parts.append(node(k, cx - w / 2, 34, w))
        parts.append(f'<path d="M{cx:.0f} 168 V{y - 4}" stroke="{th.layer_color[k]}" stroke-width="2" stroke-dasharray="4 4"/>')
    parts.append(f'<text x="{xs[5]:.0f}" y="74" {FONT} font-size="13" fill="{m["muted"]}">Contramedidas e deception</text>'
                 f'<text x="{xs[5]:.0f}" y="94" {FONT} font-size="13" fill="{m["muted"]}">entram entre o cenário</text>'
                 f'<text x="{xs[5]:.0f}" y="114" {FONT} font-size="13" fill="{m["muted"]}">e a validação.</text>')
    by = loop_y + 46
    parts.append(f'<text x="40" y="{by - 12}" {MONO} font-size="12" letter-spacing="2" fill="{m["muted"]}">FUNDAÇÃO · ALIMENTA TODAS AS CAMADAS</text>')
    bw = (avail - 5 * 16) / 6
    for i, k in enumerate(FOUNDATION):
        parts.append(node(k, left + i * (bw + 16), by, bw, h=124))
    height = by + 124 + 28
    n = len(d["entries"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-label="Mapa de camadas do ecossistema com {n} recursos">
  <!-- GERADO por python3 -m atlas build a partir de data/entries e design/tokens.json -->
  <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{arrow}"/></marker></defs>
  <rect x="0.5" y="0.5" width="1279" height="{height - 1}" rx="18" fill="{m["bg"]}" stroke="{m["line"]}"/>
  <text x="40" y="50" {FONT} font-size="20" font-weight="800" fill="{m["ink"]}">Mapa de camadas</text>
  <text x="40" y="72" {FONT} font-size="13" fill="{m["muted"]}">{n} recursos · número = itens na camada</text>
  {''.join(parts)}
</svg>
'''
