"""Utilitários de texto compartilhados pelos renderizadores."""


def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def xml(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


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


MAIN_FLOW = ["adversario", "modelagem", "telemetria", "deteccao", "validacao", "resposta", "maturidade"]
SUPPORT = ["defesa", "engano"]
FOUNDATION = ["vulnerabilidade", "cti", "dados", "conformidade", "padrao", "formacao"]
