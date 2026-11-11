"""docs/catalogo.md"""
import io
from collections import OrderedDict

from atlas.render.text import md_escape


def render(d, th):
    v = d["vocab"]
    by_id = {e["id"]: e for e in d["entries"]}
    groups = OrderedDict((k, []) for k in th.layer_order)
    for e in d["entries"]:
        groups[e["layer"]].append(e)
    out = io.StringIO()
    w = out.write
    w("<!-- ARQUIVO GERADO por python3 -m atlas build a partir de data/ecosystem.json. Não edite à mão. -->\n\n")
    w("# 🗺️ Catálogo do ecossistema\n\n")
    w("[← Início](../README.md) · [Explorador interativo](../index.html) · [Crosswalks](crosswalks.md) · "
      "[Novidades 2026](novidades-2026.md) · [Histórico](historico-e-manutencao.md)\n\n")
    total = len(d["entries"])
    w(f"Revisão: **{d['reviewed_on']}** · **{total} entradas** (frameworks, ferramentas, dados, padrões e publicações). "
      "P1 = comece aqui; P2 = aprofunde por necessidade. Não é ranking de mercado.\n\n")
    w("**Legenda.** Origem: " + " · ".join(f"{th.owner_badge[k]} {lbl}" for k, lbl in v["owner_type"].items()) + "  \n")
    w("Status: " + " · ".join(f"{th.status_badge[k]} {lbl}" for k, lbl in v["status"].items()) + "\n\n")
    w("## Índice por camada\n\n| Camada | Pergunta | Itens |\n|---|---|:---:|\n")
    for k, items in groups.items():
        if items:
            w(f"| {th.layer_icon[k]} [{k}](#{k}) | {v['layer'][k]} | {len(items)} |\n")
    w("\n")
    for k, items in groups.items():
        if not items:
            continue
        items.sort(key=lambda e: (e["priority"], e["name"].lower()))
        w(f"<a id=\"{k}\"></a>\n## {th.layer_icon[k]} {v['layer'][k]}\n\n")
        w("| | Projeto | Origem | Para que usar | Versão / estado | Domínios | Prio |\n|:-:|---|---|---|---|---|:-:|\n")
        for e in items:
            ver = e.get("version", "—")
            doms = ", ".join(v["domains"][x] for x in e["domains"])
            w(f"| {th.status_badge[e['status']]} | **[{md_escape(e['name'])}]({e['url']})** `{e['id']}` "
              f"| {th.owner_badge[e['owner_type']]} {md_escape(e['origin'])} | {md_escape(e['purpose'])} "
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
