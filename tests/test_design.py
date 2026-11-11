"""Testes da identidade visual: a paleta e os tokens cumprem o que o plano promete.

- camadas distinguíveis em visão normal e em deuteranopia (ΔE CIE76);
- texto dos temas com contraste WCAG AA (4,5:1);
- cor de camada usada como texto legível nos dois temas;
- ícones são SVG válido; toda var(--x) usada no CSS do site existe.
"""
import json
import re
import unittest
import xml.etree.ElementTree as ET

from atlas.color import contrast, deutan, min_pair
from atlas.paths import REPO, Paths
from atlas.theme import Theme

MIN_DE_NORMAL = 20
MIN_DE_DEUTAN = 7


class TestPalette(unittest.TestCase):
    def setUp(self):
        self.th = Theme(Paths())

    def test_layers_complete(self):
        vocab_layers = set(json.loads((REPO / "data" / "vocab.json").read_text(encoding="utf-8"))["layer"])
        self.assertEqual(set(self.th.layer_order), vocab_layers)
        for k in self.th.layer_order:
            with self.subTest(k):
                self.assertTrue(self.th.layer_title[k] and self.th.layer_svg[k] and self.th.layer_color[k])

    def test_distinct_normal_vision(self):
        a, b, de = min_pair(self.th.layer_color)
        self.assertGreaterEqual(de, MIN_DE_NORMAL, f"{a} × {b}: ΔE {de:.1f}")

    def test_distinct_deuteranopia(self):
        a, b, de = min_pair(self.th.layer_color, deutan)
        self.assertGreaterEqual(de, MIN_DE_DEUTAN, f"{a} × {b}: ΔE {de:.1f} em deuteranopia")

    def test_theme_text_contrast(self):
        for mode in ("light", "dark"):
            m = self.th.mode(mode)
            for fg, bg in (("ink", "bg"), ("ink", "surface"), ("muted", "surface"), ("muted", "bg"),
                           ("accent", "surface"), ("accent_ink", "accent"), ("code_ink", "code_bg")):
                with self.subTest(f"{mode}: {fg} sobre {bg}"):
                    self.assertGreaterEqual(contrast(m[fg], m[bg]), 4.5)

    def test_layer_ink_contrast(self):
        for mode in ("light", "dark"):
            surface = self.th.mode(mode)["surface"]
            for k in self.th.layer_order:
                with self.subTest(f"{mode}: {k}"):
                    self.assertGreaterEqual(contrast(self.th.layer_ink(k, mode), surface), 4.5)

    def test_brand_band_contrast(self):
        b = self.th.brand
        for fg in ("white", "mist", "teal", "dim"):
            with self.subTest(fg):
                self.assertGreaterEqual(contrast(b[fg], b["night"]), 4.5)


class TestAssets(unittest.TestCase):
    def setUp(self):
        self.th = Theme(Paths())

    def test_icons_are_valid_svg(self):
        for k in self.th.layer_order:
            with self.subTest(k):
                ET.fromstring(self.th.icon(k))

    def test_css_variables_defined(self):
        tokens = self.th.css()
        app = (REPO / "site" / "app.css").read_text(encoding="utf-8")
        defined = set(re.findall(r"(--[\w-]+)\s*:", tokens + app))
        used = set(re.findall(r"var\((--[\w-]+)", app))
        self.assertEqual(sorted(used - defined), [])


if __name__ == "__main__":
    unittest.main()
