"""Registro dos arquivos derivados. `build(p)` devolve {caminho: conteúdo}."""
from atlas import model
from atlas.render import banner, bundle, catalog, layer_map, readme, table, trilha
from atlas.theme import Theme


def build(p, d=None, t=None):
    d = d if d is not None else model.load(p)
    t = t if t is not None else model.load_trilha(p)
    th = Theme(p)
    out = {
        p.bundle_json: bundle.render_json(d),
        p.csv: table.render(d),
        p.catalog: catalog.render(d, th),
        p.trilha_md: trilha.render(t, d),
        p.bundle_js: bundle.render_js(d, t, p.substituicoes),
        p.banner: banner.render(d, th),
        p.layer_map: layer_map.render(d, th),
    }
    if p.readme.exists():
        out[p.readme] = readme.render(d, p.readme.read_text(encoding="utf-8"))
    return out


def generated(p):
    """Arquivos que só o build escreve (o README tem só um bloco gerado e fica fora)."""
    return [p.bundle_json, p.csv, p.catalog, p.trilha_md, p.bundle_js, p.banner, p.layer_map]
