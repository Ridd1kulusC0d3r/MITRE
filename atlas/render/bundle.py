"""data/ecosystem.json (agregado schema 2.0) e assets/ecosystem.js (dados do explorador)."""
import csv
import json

from atlas.model import dumps


def render_json(d):
    return dumps(d)


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def render_js(d, t, substituicoes_path, ui=None):
    payload = {"catalog": d, "trilha": t, "substituicoes": read_tsv(substituicoes_path)}
    if ui is not None:
        payload["ui"] = ui
    return ("// ARQUIVO GERADO por python3 -m atlas build. Não edite à mão.\n"
            "// Carregado por index.html via <script>, o que funciona também abrindo o arquivo localmente.\n"
            "window.ECOSYSTEM = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n")
