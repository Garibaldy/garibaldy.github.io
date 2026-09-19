#!/usr/bin/env python3
"""
Captura el sitio por bloques (secciones) con Playwright.
Uso:
  py -3 scripts/capture_blocks.py --target vercel
  py -3 scripts/capture_blocks.py --target local
  py -3 scripts/capture_blocks.py --target both

Requisito: py -3 -m pip install playwright && py -3 -m playwright install chromium
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "review"

VERCEL_URL = "https://intrepidux.vercel.app/"
LOCAL_URL = "http://127.0.0.1:8765/"

# Selectores: nuestro HTML usa #id; Vercel usa las mismas anclas en muchas secciones
BLOCKS = [
    ("01-hero", "#inicio, .hero, section.hero"),
    ("02-problema", "#problema"),
    ("03-servicios", "#servicios"),
    ("04-proceso", "#proceso"),
    ("05-sectores", "#sectores"),
    ("06-clientes", "#clientes"),
    ("07-testimonios", "#testimonios, #experiencias, .ix-experiences"),
    ("08-por-que", "#por-que"),
    ("09-faq", "#faq"),
    ("10-contacto", "#contacto"),
    ("11-footer", "footer, .footer"),
]

VIEWPORT = {"width": 1440, "height": 900}


def first_visible(page, selector_csv: str):
    for sel in selector_csv.split(","):
        sel = sel.strip()
        loc = page.locator(sel).first
        try:
            if loc.count() == 0:
                continue
            loc.wait_for(state="visible", timeout=8000)
            return loc
        except Exception:
            continue
    return None


def capture_site(playwright, name: str, url: str) -> None:
    out_dir = OUT / name
    out_dir.mkdir(parents=True, exist_ok=True)
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(url, wait_until="networkidle", timeout=120_000)
    page.wait_for_timeout(2000)

    # Full viewport (above the fold)
    page.screenshot(path=str(out_dir / "00-viewport-top.png"), full_page=False)

    missing = []
    for block_id, selectors in BLOCKS:
        loc = first_visible(page, selectors)
        if not loc:
            missing.append(block_id)
            continue
        loc.screenshot(path=str(out_dir / f"{block_id}.png"))

    # Full page en trozos verticales si la página es muy larga
    height = page.evaluate("() => document.documentElement.scrollHeight")
    step = 9000
    y = 0
    chunk = 0
    while y < height:
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(400)
        page.screenshot(path=str(out_dir / f"full-chunk-{chunk:02d}.png"), full_page=False)
        y += step
        chunk += 1

    browser.close()
    print(f"[{name}] guardado en {out_dir}")
    if missing:
        print(f"[{name}] sin selector: {', '.join(missing)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        choices=("vercel", "local", "both"),
        default="vercel",
    )
    args = parser.parse_args()

    with sync_playwright() as p:
        if args.target in ("vercel", "both"):
            capture_site(p, "vercel", VERCEL_URL)
        if args.target in ("local", "both"):
            capture_site(p, "local", LOCAL_URL)

    return 0


if __name__ == "__main__":
    sys.exit(main())
