#!/usr/bin/env python3
"""Regenera partials/header-fase-b-{1,2}.html e inserta header en index.html desde header-fase-b-root.html."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = (
    '<a class="visually-hidden-focusable position-absolute top-0 start-0 z-3 p-3 bg-white" '
    'href="#main-content">Saltar al contenido principal</a>\n'
)
partial = ROOT / "partials/header-fase-b-root.html"
header = re.sub(r"^<!--.*?-->\n", "", partial.read_text(), count=1).strip()


def with_prefix(prefix: str) -> str:
    f = header
    f = re.sub(r'src="assets/', f'src="{prefix}assets/', f)
    for p in ("integraciones/", "facturacion-electronica/", "industrias/"):
        f = f.replace(f'href="{p}"', f'href="{prefix}{p}"')
    for anchor in ("inicio", "servicios", "proceso", "casos", "por-que", "contacto"):
        f = f.replace(f'href="#{anchor}"', f'href="{prefix}index.html#{anchor}"')
    return f


for depth, name in (("../", "header-fase-b-1.html"), ("../../", "header-fase-b-2.html")):
    note = (
        f"<!-- Generado desde header-fase-b-root.html ({depth.strip() or 'root'}) — "
        "marcar un nav-link con active; ejecutar scripts/sync-headers-from-root.py -->\n"
    )
    (ROOT / "partials" / name).write_text(note + SKIP + with_prefix(depth) + "\n")

index = ROOT / "index.html"
html = index.read_text()
html = re.sub(
    r"\n      <nav id=\"mainNav\" class=\"ix-nav navbar navbar-expand-lg\" aria-label=\"Principal\">.*?</nav>\n",
    "\n",
    html,
    count=1,
    flags=re.S,
)
if "ix-header-site" not in html[: html.find("<main")]:
    html = re.sub(
        r"(<a class=\"visually-hidden-focusable[^>]*>Saltar al contenido principal</a>\s*\n)",
        r"\1\n  " + header + "\n\n  ",
        html,
        count=1,
    )
index.write_text(html)
print("OK: index.html + header-fase-b-1/2")
