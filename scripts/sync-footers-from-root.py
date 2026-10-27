#!/usr/bin/env python3
"""Regenera partials/footer-home-{1,2}.html e index.html desde partials/footer-home-root.html."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
partial = ROOT / "partials/footer-home-root.html"
text = partial.read_text()
footer = re.sub(r"^<!--.*?-->\n", "", text, count=1).strip()
if not footer.startswith("<footer"):
    raise SystemExit("footer-home-root.html: bloque <footer> no encontrado")


def with_prefix(prefix: str) -> str:
    f = footer
    f = re.sub(r'src="assets/', f'src="{prefix}assets/', f)
    for p in ("integraciones/", "facturacion-electronica/", "industrias/", "privacidad/", "terms/"):
        f = f.replace(f'href="{p}"', f'href="{prefix}{p}"')
    for anchor in ("inicio", "servicios", "proceso", "casos", "por-que", "contacto", "sectores"):
        f = f.replace(f'href="#{anchor}"', f'href="{prefix}index.html#{anchor}"')
    return f


for depth, name in (("../", "footer-home-1.html"), ("../../", "footer-home-2.html")):
    out = f"<!-- Generado desde footer-home-root.html (profundidad {depth.strip() or 'root'}) — no editar a mano; ejecutar scripts/sync-footers-from-root.py -->\n"
    out += with_prefix(depth) + "\n"
    (ROOT / "partials" / name).write_text(out)

index = ROOT / "index.html"
html = index.read_text()
html = re.sub(r"<footer class=\"ix-footer\">.*?</footer>", footer, html, count=1, flags=re.S)
index.write_text(html)
print("OK: index.html + footer-home-1.html + footer-home-2.html")
