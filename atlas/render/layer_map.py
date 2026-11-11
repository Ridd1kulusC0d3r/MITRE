"""assets/mapa-camadas.svg"""
from atlas.render.text import FOUNDATION, MAIN_FLOW, fit, xml


def render(d, th):
    """Mapa de camadas: fluxo principal, apoios e fundação, com contagens e exemplos."""
    FONT, MONO, LAYER_COLOR = th.font, th.mono, th.layer_color
    v = d["vocab"]["layer"]
    groups = {}
    for e in d["entries"]:
        groups.setdefault(e["layer"], []).append(e)
    for k in groups:
        groups[k].sort(key=lambda e: (e["priority"], e["name"]))
    titles = th.layer_title

    def node(k, x, y, w, h=132):
        items = groups.get(k, [])
        col = LAYER_COLOR[k]
        inner = w - 28
        lines = "".join(f'<text x="{x + 14:.0f}" y="{y + 84 + i * 16}" {FONT} font-size="12" fill="#c9d1d9">{xml(fit(e["name"], inner, 6.1))}</text>'
                        for i, e in enumerate(items[:3]))
        return (f'<g><rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{h}" rx="12" fill="#161b22" stroke="{col}" stroke-width="2"/>'
                f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="6" rx="3" fill="{col}"/>'
                f'<text x="{x + 14:.0f}" y="{y + 32}" {FONT} font-size="16" font-weight="700" fill="#f0f6fc">{xml(fit(titles[k], inner - 22, 8.4))}</text>'
                f'<text x="{x + w - 14:.0f}" y="{y + 32}" text-anchor="end" {MONO} font-size="15" font-weight="700" fill="{col}">{len(items)}</text>'
                f'<text x="{x + 14:.0f}" y="{y + 54}" {FONT} font-size="11" fill="#8b949e">{xml(fit(v[k], inner, 5.5))}</text>{lines}</g>')

    main = MAIN_FLOW
    parts = []
    left, avail, gap, y = 40, 1200, 24, 196
    w = (avail - gap * (len(main) - 1)) / len(main)
    xs = [left + i * (w + gap) for i in range(len(main))]
    for i, k in enumerate(main):
        parts.append(node(k, xs[i], y, w))
        if i < len(main) - 1:
            ax = xs[i] + w
            parts.append(f'<path d="M{ax + 3:.0f} {y + 66} H{ax + gap - 5:.0f}" stroke="#6e7681" stroke-width="2.5" marker-end="url(#arr)"/>')
    loop_y = y + 132 + 22
    parts.append(f'<path d="M{xs[-1] + w / 2:.0f} {y + 134} V{loop_y} H{xs[0] + w / 2:.0f} V{y + 140}" fill="none" stroke="#484f58" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>'
                 f'<rect x="560" y="{loop_y - 10}" width="160" height="20" fill="#0d1117"/>'
                 f'<text x="640" y="{loop_y + 4}" text-anchor="middle" {FONT} font-size="12" fill="#8b949e">lacunas viram novo ciclo</text>')
    # apoios acima, centrados sobre modelagem→telemetria e detecção→validação
    for k, a, b in (("defesa", 1, 2), ("engano", 3, 4)):
        cx = (xs[a] + xs[b] + w) / 2
        parts.append(node(k, cx - w / 2, 34, w))
        parts.append(f'<path d="M{cx:.0f} 168 V{y - 4}" stroke="{LAYER_COLOR[k]}" stroke-width="2" stroke-dasharray="4 4"/>')
    parts.append(f'<text x="{xs[5]:.0f}" y="74" {FONT} font-size="13" fill="#8b949e">Contramedidas e deception</text>'
                 f'<text x="{xs[5]:.0f}" y="94" {FONT} font-size="13" fill="#8b949e">entram entre o cenário</text>'
                 f'<text x="{xs[5]:.0f}" y="114" {FONT} font-size="13" fill="#8b949e">e a validação.</text>')
    base = FOUNDATION
    by = loop_y + 46
    parts.append(f'<text x="40" y="{by - 12}" {MONO} font-size="12" letter-spacing="2" fill="#6e7681">FUNDAÇÃO · ALIMENTA TODAS AS CAMADAS</text>')
    bw = (avail - 5 * 16) / 6
    for i, k in enumerate(base):
        parts.append(node(k, left + i * (bw + 16), by, bw, h=124))
    height = by + 124 + 28
    n = len(d["entries"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-label="Mapa de camadas do ecossistema com {n} recursos">
  <!-- GERADO por scripts/build_catalog.py -->
  <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#8b949e"/></marker></defs>
  <rect width="1280" height="{height}" rx="18" fill="#0d1117"/>
  <text x="40" y="50" {FONT} font-size="20" font-weight="800" fill="#f0f6fc">Mapa de camadas</text>
  <text x="40" y="72" {FONT} font-size="13" fill="#8b949e">{n} recursos · número = itens na camada</text>
  {''.join(parts)}
</svg>
'''
