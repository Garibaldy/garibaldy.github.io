#!/usr/bin/env python3
"""Aplica chrome unificado: header fuera de <main>, footers desde partials, páginas legales/404."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADER_IN_MAIN = re.compile(
    r"(<main id=\"main-content\">)\s*(<header class=\"ix-header-site border-bottom bg-white sticky-top\">.*?</header>)",
    re.S,
)

FOOTER_NICHE = re.compile(r"<footer class=\"ix-footer ix-footer-niche\">.*?</footer>\s*", re.S)
OLD_FOOTER_404 = re.compile(r"<footer class=\"ix-footer\">.*?</footer>\s*", re.S)


def load_partial(name: str) -> str:
    text = (ROOT / "partials" / name).read_text()
    return re.sub(r"^<!--.*?-->\n", "", text, count=1).strip() + "\n\n  "


def move_header_outside_main(html: str) -> str:
    return HEADER_IN_MAIN.sub(r"\2\n\n  \1", html)


def fix_index_structure(html: str) -> str:
    """Header hermano de main, sin nav dentro del hero."""
    html = re.sub(r"\n{3,}", "\n\n", html)
    if "<main id=\"main-content\">" in html and "ix-header-site" in html.split("<main id=\"main-content\">")[0]:
        return html
    return html


def main() -> None:
    footer1 = load_partial("footer-home-1.html")
    footer_root = load_partial("footer-home-root.html")
    skip_header1 = load_partial("header-fase-b-1.html")

    # Hub + integraciones: header fuera de main
    for rel in ("integraciones/index.html", "facturacion-electronica/index.html"):
        p = ROOT / rel
        t = move_header_outside_main(p.read_text())
        p.write_text(t)
        print("header→outside main:", rel)

    # 404 footer = home root
    p404 = ROOT / "404.html"
    t404 = p404.read_text()
    if "Pregúntale a la AI" not in t404 or "facturacion-electronica" not in t404:
        t404 = OLD_FOOTER_404.sub(footer_root, t404, count=1)
        if "main.js" not in t404:
            t404 = t404.replace(
                "</body>",
                '  <script src="js/main.js"></script>\n</body>',
                1,
            )
        p404.write_text(t404)
        print("404 footer synced")

    # Términos: nav + footer
    terms = ROOT / "terms/index.html"
    tt = terms.read_text()
    tt = re.sub(
        r"<nav id=\"mainNav\" class=\"ix-nav navbar navbar-expand-lg container\" aria-label=\"Principal\">.*?</nav>\s*",
        "",
        tt,
        count=1,
        flags=re.S,
    )
    if "ix-header-site" not in tt:
        tt = tt.replace(
            'href="#main-content">Saltar al contenido principal</a>\n\n',
            'href="#main-content">Saltar al contenido principal</a>\n\n  ' + skip_header1,
            1,
        )
    if "facturacion-electronica/" not in tt:
        tt = re.sub(r"<footer class=\"ix-footer\">.*?</footer>\s*", footer1, tt, count=1, flags=re.S)
    terms.write_text(tt)
    print("terms nav+footer synced")

    # Privacidad: shell completo
    priv = ROOT / "privacidad/index.html"
    pt = priv.read_text()
    if "ix-header-site" not in pt:
        main_block = re.search(
            r"(<main class=\"privacy-content\">.*?</main>)", pt, re.S
        ).group(1)
        main_block = main_block.replace(
            '<main class="privacy-content">',
            '<main id="main-content" class="privacy-content">',
            1,
        )
        pt = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Política de privacidad de Intrepidux S.R.L.">
  <title>Privacidad | Intrepidux</title>
  <link rel="icon" href="../assets/favicon.ico" type="image/x-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="../css/theme.css" rel="stylesheet">
  <style>
    .privacy-content {{ max-width: 720px; margin: 0 auto; padding: 4rem 1.25rem; }}
    .privacy-content h1 {{ font-family: var(--ix-font-display); font-weight: 700; color: var(--ink); font-size: 2rem; margin-bottom: 1.5rem; }}
    .privacy-content p {{ color: var(--ink-soft); line-height: 1.65; }}
  </style>
</head>
<body class="ix-body">
  {skip_header1}
  {main_block}

  {footer1}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../js/site-config.js"></script>
  <script src="../js/analytics-config.js"></script>
  <script src="../js/analytics.js"></script>
  <script src="../js/analytics-cta.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""
        priv.write_text(pt)
        print("privacidad shell added")

    # index: header fuera de main si quedó dentro
    idx = ROOT / "index.html"
    it = move_header_outside_main(idx.read_text())
    it = re.sub(
        r"(<body class=\"ix-body\"[^>]*>\s*<a class=\"visually-hidden-focusable[^>]*></a>\s*)\n+\s*(<header class=\"ix-header-site)",
        r"\1\n  \2",
        it,
        count=1,
        flags=re.S,
    )
    it = re.sub(
        r"</header>\s*\n+\s*(<main id=\"main-content\">)",
        r"</header>\n\n  \1",
        it,
        count=1,
    )
    idx.write_text(it)
    print("index structure tidy")

    print("Done.")


if __name__ == "__main__":
    main()
