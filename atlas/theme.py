"""Identidade visual: lê design/tokens.json e expõe o que os renderizadores usam."""
import json
from functools import lru_cache

from atlas.paths import Paths


@lru_cache(maxsize=None)
def _load(path):
    return json.loads(open(path, encoding="utf-8").read())


class Theme:
    def __init__(self, p=None):
        t = _load(str((p or Paths()).tokens))
        self.tokens = t
        self.layer_order = list(t["layers"])
        self.layer_color = {k: v["color"] for k, v in t["layers"].items()}
        self.layer_icon = {k: v["emoji"] for k, v in t["layers"].items()}
        self.layer_title = {k: v["title"] for k, v in t["layers"].items()}
        self.owner_badge = t["owner_badge"]
        self.status_badge = t["status_badge"]
        self.font = f'font-family="{t["font"]["svg_sans"]}"'
        self.mono = f'font-family="{t["font"]["svg_mono"]}"'
