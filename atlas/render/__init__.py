"""Registro dos arquivos derivados. `build(p)` devolve {caminho: conteúdo}."""
from atlas import model
from atlas.render import banner, brand, bundle, catalog, layer_map, readme, table, trilha
from atlas.theme import Theme


def build(p, d=None, t=None):
    d = d if d is not None else model.load(p)
    t = t if t is not None else model.load_trilha(p)
    th = Theme(p)
    a = p.root / "assets"
    out = {
        p.bundle_json: bundle.render_json(d),
        p.csv: table.render(d),
        p.catalog: catalog.render(d, th),
        p.trilha_md: trilha.render(t, d),
        p.bundle_js: bundle.render_js(d, t, p.substituicoes, ui(th)),
        a / "tokens.css": th.css(),
        a / "banner-dark.svg": banner.render(d, th, "dark"),
        a / "banner-light.svg": banner.render(d, th, "light"),
        a / "mapa-camadas-dark.svg": layer_map.render(d, th, "dark"),
        a / "mapa-camadas-light.svg": layer_map.render(d, th, "light"),
        a / "mark.svg": brand.mark(th),
        a / "favicon.svg": brand.favicon(th),
        a / "social.svg": brand.social(d, th),
    }
    if p.readme.exists():
        out[p.readme] = readme.render(d, p.readme.read_text(encoding="utf-8"), th)
    return out


def ui(th):
    """Metadados de apresentação que o explorador consome (sem cores: elas vêm do CSS)."""
    return {"layers": {k: {"title": th.layer_title[k], "icon": th.layer_svg[k]} for k in th.layer_order},
            "order": th.layer_order, "name": th.name, "repo_url": th.repo_url, "disclaimer": th.disclaimer}


def generated(p):
    """Arquivos que só o build escreve (o README tem só blocos gerados e fica fora)."""
    a = p.root / "assets"
    return [p.bundle_json, p.csv, p.catalog, p.trilha_md, p.bundle_js, a / "tokens.css",
            a / "banner-dark.svg", a / "banner-light.svg", a / "mapa-camadas-dark.svg",
            a / "mapa-camadas-light.svg", a / "mark.svg", a / "favicon.svg", a / "social.svg"]

