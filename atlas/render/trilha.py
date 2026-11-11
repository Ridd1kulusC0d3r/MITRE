"""docs/trilha.md"""
import io


def render(t, d):
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
