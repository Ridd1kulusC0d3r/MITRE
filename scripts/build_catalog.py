#!/usr/bin/env python3
"""build_catalog.py — gera docs/catalogo.md, data/ecosystem.csv e o bloco de
estatísticas do README a partir de data/ecosystem.json (fonte única).

Somente stdlib. Uso:
    python3 scripts/build_catalog.py          # valida e regenera
    python3 scripts/build_catalog.py --check  # valida; falha se algo estiver desatualizado (CI)
"""
import csv
import io
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "ecosystem.json"
CATALOG = ROOT / "docs" / "catalogo.md"
CSV_OUT = ROOT / "data" / "ecosystem.csv"
README = ROOT / "README.md"
TRILHA = ROOT / "data" / "trilha.json"
TRILHA_MD = ROOT / "docs" / "trilha.md"
JS_OUT = ROOT / "assets" / "ecosystem.js"

LAYER_ORDER = ["adversario", "modelagem", "telemetria", "deteccao", "defesa", "engano",
               "validacao", "resposta", "vulnerabilidade", "cti", "maturidade",
               "dados", "conformidade", "padrao", "formacao"]
LAYER_ICON = {"adversario": "🎯", "modelagem": "🧭", "telemetria": "📡", "deteccao": "🔎",
              "defesa": "🛡️", "engano": "🎭", "validacao": "🧪", "resposta": "🚑",
              "vulnerabilidade": "🩹", "cti": "🕵️", "maturidade": "📈", "dados": "🗄️",
              "conformidade": "⚙️", "padrao": "📐", "formacao": "🎓"}
OWNER_BADGE = {"mitre": "🟦", "ctid": "🟩", "colaboracao": "🟪", "governanca-aberta": "🟫",
               "governo": "⬛", "padrao": "⬜", "comunidade": "🟨", "fornecedor": "🟧", "outro": "◻️"}
STATUS_BADGE = {"ativo": "✅", "baixa-atividade": "⏸️", "parado": "🧊", "n/v": "❔"}
REQUIRED = ["id", "name", "url", "origin", "owner_type", "layer", "domains", "purpose",
            "output", "priority", "status", "reviewed_on", "verification"]
CSV_FIELDS = ["id", "name", "url", "origin", "owner_type", "layer", "domains", "priority",
              "status", "version", "formats", "relations", "purpose", "output", "notes",
              "license_api", "archived", "pushed_at", "reviewed_on", "verification"]


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def validate(d):
    errs = []
    vocab = d["vocab"]
    ids = [e.get("id") for e in d["entries"]]
    dup = [i for i, n in Counter(ids).items() if n > 1]
    if dup:
        errs.append(f"IDs duplicados: {dup}")
    idset = set(ids)
    names = Counter(e["name"].lower() for e in d["entries"])
    errs += [f"nome duplicado: {n}" for n, c in names.items() if c > 1]
    for e in d["entries"]:
        where = e.get("id", "?")
        for f in REQUIRED:
            if f not in e or e[f] in (None, "", []):
                errs.append(f"{where}: campo obrigatório ausente: {f}")
        if not re.fullmatch(r"E\d{3}", e.get("id", "")):
            errs.append(f"{where}: id fora do padrão E000")
        if not str(e.get("url", "")).startswith("https://"):
            errs.append(f"{where}: url deve usar https")
        for key in ("owner_type", "layer", "status", "priority"):
            if e.get(key) not in vocab[key]:
                errs.append(f"{where}: {key} inválido: {e.get(key)}")
        for dom in e.get("domains", []):
            if dom not in vocab["domains"]:
                errs.append(f"{where}: domínio inválido: {dom}")
        for r in e.get("relations", []):
            if r not in idset:
                errs.append(f"{where}: relação aponta para id inexistente: {r}")
            if r == e.get("id"):
                errs.append(f"{where}: relação consigo mesmo")
    return errs


def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def render_catalog(d):
    v = d["vocab"]
    by_id = {e["id"]: e for e in d["entries"]}
    groups = OrderedDict((k, []) for k in LAYER_ORDER)
    for e in d["entries"]:
        groups[e["layer"]].append(e)
    out = io.StringIO()
    w = out.write
    w("<!-- ARQUIVO GERADO por scripts/build_catalog.py a partir de data/ecosystem.json. Não edite à mão. -->\n\n")
    w("# 🗺️ Catálogo do ecossistema\n\n")
    w("[← Início](../README.md) · [Explorador interativo](../index.html) · [Crosswalks](crosswalks.md) · "
      "[Novidades 2026](novidades-2026.md) · [Histórico](historico-e-manutencao.md)\n\n")
    total = len(d["entries"])
    w(f"Revisão: **{d['reviewed_on']}** · **{total} entradas** (frameworks, ferramentas, dados, padrões e publicações). "
      "P1 = comece aqui; P2 = aprofunde por necessidade. Não é ranking de mercado.\n\n")
    w("**Legenda.** Origem: " + " · ".join(f"{OWNER_BADGE[k]} {lbl}" for k, lbl in v["owner_type"].items()) + "  \n")
    w("Status: " + " · ".join(f"{STATUS_BADGE[k]} {lbl}" for k, lbl in v["status"].items()) + "\n\n")
    w("## Índice por camada\n\n| Camada | Pergunta | Itens |\n|---|---|:---:|\n")
    for k, items in groups.items():
        if items:
            w(f"| {LAYER_ICON[k]} [{k}](#{k}) | {v['layer'][k]} | {len(items)} |\n")
    w("\n")
    for k, items in groups.items():
        if not items:
            continue
        items.sort(key=lambda e: (e["priority"], e["name"].lower()))
        w(f"<a id=\"{k}\"></a>\n## {LAYER_ICON[k]} {v['layer'][k]}\n\n")
        w("| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |\n|:-:|---|---|---|---|---|:-:|\n")
        for e in items:
            ver = e.get("version", "—")
            doms = ", ".join(v["domains"][x] for x in e["domains"])
            w(f"| {STATUS_BADGE[e['status']]} | **[{md_escape(e['name'])}]({e['url']})** `{e['id']}` "
              f"| {OWNER_BADGE[e['owner_type']]} {md_escape(e['origin'])} | {md_escape(e['purpose'])} "
              f"| {md_escape(ver)} | {doms} | {e['priority']} |\n")
        notes = [e for e in items if e.get("notes") or e.get("relations")]
        if notes:
            w("\n<details><summary>Notas e relações</summary>\n\n")
            for e in notes:
                rel = ", ".join(f"{by_id[r]['name']}" for r in e.get("relations", []))
                line = f"- **{md_escape(e['name'])}** — entrega: {md_escape(e['output'])}."
                if e.get("notes"):
                    line += f" {md_escape(e['notes'])}"
                if rel:
                    line += f" ↔ {rel}."
                w(line + "\n")
            w("\n</details>\n\n")
    w("## 🗄️ Itens históricos e depreciados\n\n| Item | Situação |\n|---|---|\n")
    for h in d["historical"]:
        w(f"| [{md_escape(h['name'])}]({h['url']}) | {md_escape(h['note'])} |\n")
    w("\n---\n\n")
    w(f"_Limites da verificação:_ {md_escape(d['verification_limits'])}\n")
    return out.getvalue()


def render_csv(d):
    out = io.StringIO()
    wr = csv.DictWriter(out, fieldnames=CSV_FIELDS, extrasaction="ignore", lineterminator="\n")
    wr.writeheader()
    for e in d["entries"]:
        row = dict(e)
        for k in ("domains", "formats", "relations"):
            row[k] = ";".join(e.get(k, []))
        wr.writerow(row)
    return out.getvalue()


def render_trilha(t, d):
    by_id = {e["id"]: e for e in d["entries"]}
    out = io.StringIO()
    w = out.write
    w("<!-- ARQUIVO GERADO por scripts/build_catalog.py a partir de data/trilha.json. Não edite à mão. -->\n\n")
    w(f"# 🧗 {t['titulo']}\n\n")
    w("[← Início](../README.md) · [Versão interativa (uma ação por vez)](../index.html#trilha) · [Catálogo](catalogo.md)\n\n")
    w(f"> {t['principio']} Marque a caixa, faça a próxima. No explorador, o progresso fica salvo no seu navegador.\n\n")
    w("| Semana | Tema | Entrega |\n|:-:|---|---|\n")
    for s in t["semanas"]:
        w(f"| {s['n']} | [{s['tema']}](#semana-{s['n']}) | {s['entrega']} |\n")
    for s in t["semanas"]:
        w(f"\n<a id=\"semana-{s['n']}\"></a>\n## Semana {s['n']} · {s['tema']}\n\n**Entrega:** {s['entrega']}\n\n")
        for a in s["acoes"]:
            line = f"- [ ] **{a['id']}** {a['texto']}"
            refs = [by_id[r] for r in a.get("ref", [])]
            if refs:
                line += " — " + ", ".join(f"[{r['name']}]({r['url']})" for r in refs)
            w(line + "\n")
            if a.get("cmd"):
                w(f"  ```bash\n  {a['cmd']}\n  ```\n")
    return out.getvalue()


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def render_js(d, t):
    payload = {"catalog": d, "trilha": t,
               "substituicoes": read_tsv(ROOT / "crosswalks" / "attack-v18.1-v20.0-substituicoes.tsv")}
    return ("// ARQUIVO GERADO por scripts/build_catalog.py. Não edite à mão.\n"
            "// Carregado por index.html via <script>, o que funciona também abrindo o arquivo localmente.\n"
            "window.ECOSYSTEM = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n")


LAYER_COLOR = {"adversario": "#f85149", "modelagem": "#f0883e", "telemetria": "#d29922",
               "deteccao": "#3fb950", "validacao": "#2ea7a0", "resposta": "#388bfd",
               "maturidade": "#a371f7", "defesa": "#39c5cf", "engano": "#db61a2",
               "vulnerabilidade": "#c38b5f", "cti": "#8b949e", "dados": "#6e7681",
               "conformidade": "#768390", "padrao": "#636e7b", "formacao": "#9ea700"}
FONT = "font-family=\"'Segoe UI', 'Helvetica Neue', Arial, sans-serif\""
MONO = "font-family=\"'SFMono-Regular', Consolas, 'Liberation Mono', monospace\""


def xml(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def render_banner(d):
    """Banner 1280×320 com uma 'matriz' estilizada à direita (decorativa, determinística)."""
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
            color = list(LAYER_COLOR.values())[(c + r * 2) % 7]
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


def fit(text, width, px):
    """Corta o texto na última palavra que cabe em `width` pixels (estimativa: px por caractere)."""
    text = str(text)
    maxch = max(4, int(width / px))
    if len(text) <= maxch:
        return text
    cut = text[:maxch - 1]
    if " " in cut[maxch // 2:]:
        cut = cut[:cut.rfind(" ")]
    return cut.rstrip(" ·,-") + "…"


def render_map(d):
    """Mapa de camadas: fluxo principal, apoios e fundação, com contagens e exemplos."""
    v = d["vocab"]["layer"]
    groups = {}
    for e in d["entries"]:
        groups.setdefault(e["layer"], []).append(e)
    for k in groups:
        groups[k].sort(key=lambda e: (e["priority"], e["name"]))
    titles = {"adversario": "Adversário", "modelagem": "Modelagem", "telemetria": "Telemetria",
              "deteccao": "Detecção", "validacao": "Validação", "resposta": "Resposta",
              "maturidade": "Maturidade", "defesa": "Defesa", "engano": "Engano",
              "vulnerabilidade": "Vulnerabilidade", "cti": "CTI", "dados": "Dados e APIs",
              "conformidade": "Conformidade", "padrao": "Padrões", "formacao": "Formação"}

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

    main = ["adversario", "modelagem", "telemetria", "deteccao", "validacao", "resposta", "maturidade"]
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
    base = ["vulnerabilidade", "cti", "dados", "conformidade", "padrao", "formacao"]
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


def main():
    check = "--check" in sys.argv
    d = load()
    errs = validate(d)
    if errs:
        print("❌ Validação falhou:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    trilha = json.loads(TRILHA.read_text(encoding="utf-8"))
    known = {e["id"] for e in d["entries"]}
    bad = [a["id"] for s in trilha["semanas"] for a in s["acoes"] for r in a.get("ref", []) if r not in known]
    if bad:
        print("❌ Trilha referencia entradas inexistentes nas ações:", bad)
        sys.exit(1)
    targets = {CATALOG: render_catalog(d), CSV_OUT: render_csv(d),
               TRILHA_MD: render_trilha(trilha, d), JS_OUT: render_js(d, trilha),
               ROOT / "assets" / "banner.svg": render_banner(d),
               ROOT / "assets" / "mapa-camadas.svg": render_map(d)}
    readme = README.read_text(encoding="utf-8")
    new_readme = re.sub(r"<!-- stats:start -->.*?<!-- stats:end -->", stats_block(d), readme, flags=re.S)
    targets[README] = new_readme
    stale = [p for p, content in targets.items()
             if not p.exists() or p.read_text(encoding="utf-8") != content]
    if check:
        if stale:
            print("❌ Arquivos desatualizados (rode scripts/build_catalog.py):", *[str(p.relative_to(ROOT)) for p in stale])
            sys.exit(1)
        print(f"✅ {len(d['entries'])} entradas válidas; arquivos gerados em dia.")
        return
    for p, content in targets.items():
        p.write_text(content, encoding="utf-8")
    print(f"✅ {len(d['entries'])} entradas válidas; gerados: " + ", ".join(str(p.relative_to(ROOT)) for p in targets))


if __name__ == "__main__":
    main()
