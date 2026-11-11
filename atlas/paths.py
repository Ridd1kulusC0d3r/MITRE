"""Caminhos do repositório. `Paths(root)` permite apontar para outra árvore (testes)."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


class Paths:
    def __init__(self, root=REPO):
        self.root = Path(root)
        d = self.root / "data"
        self.entries = d / "entries"
        self.vocab = d / "vocab.json"
        self.historical = d / "historical.json"
        self.meta = d / "meta.json"
        self.repo_checks = d / "repository_checks.json"
        self.trilha = d / "trilha.json"
        self.tokens = self.root / "design" / "tokens.json"
        self.substituicoes = self.root / "crosswalks" / "attack-v18.1-v20.0-substituicoes.tsv"
        # derivados
        self.bundle_json = d / "ecosystem.json"
        self.csv = d / "ecosystem.csv"
        self.catalog = self.root / "docs" / "catalogo.md"
        self.trilha_md = self.root / "docs" / "trilha.md"
        self.bundle_js = self.root / "assets" / "ecosystem.js"
        self.readme = self.root / "README.md"

    def rel(self, p):
        return str(Path(p).relative_to(self.root))
