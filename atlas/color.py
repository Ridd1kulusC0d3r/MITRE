"""Cor: contraste WCAG 2.x, distância perceptual (CIE76 em Lab) e simulação de
deuteranopia (Machado, Oliveira e Fernandes, 2009, severidade 1.0). Somente stdlib."""


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def to_hex(c):
    return "#" + "".join(f"{round(max(0, min(1, x)) * 255):02x}" for x in c)


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def luminance(h):
    r, g, b = (_lin(x) for x in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def lab(h):
    r, g, b = (_lin(x) for x in rgb(h))
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e(a, b):
    return sum((p - q) ** 2 for p, q in zip(lab(a), lab(b))) ** 0.5


_DEUTAN = ((0.367322, 0.860646, -0.227968),
           (0.280085, 0.672501, 0.047413),
           (-0.011820, 0.042940, 0.968881))


def deutan(h):
    lin = [_lin(x) for x in rgb(h)]
    out = [sum(m * c for m, c in zip(row, lin)) for row in _DEUTAN]
    return to_hex([_gam(max(0, min(1, v))) for v in out])


def mix(a, b, t):
    return to_hex([x + (y - x) * t for x, y in zip(rgb(a), rgb(b))])


def readable_on(color, background, ratio=4.5, toward="#000000"):
    """Escurece (ou clareia) `color` até atingir `ratio` de contraste sobre `background`."""
    t = 0.0
    c = color
    while contrast(c, background) < ratio and t < 1:
        t += 0.02
        c = mix(color, toward, t)
    return c


def min_pair(colors, transform=lambda x: x):
    """Menor ΔE entre pares (nome_a, nome_b, ΔE)."""
    items = list(colors.items())
    best = None
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            d = delta_e(transform(items[i][1]), transform(items[j][1]))
            if best is None or d < best[2]:
                best = (items[i][0], items[j][0], d)
    return best
