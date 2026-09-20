"""Export numbered section redesign mockups (01, 03, 06) to PNG via Playwright."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "assets/review"

EXPORTS = [
    ("1-problema-redesigns-mockups.html", "1-problema-redesigns.png"),
    ("2-proceso-redesigns-mockups.html", "2-proceso-redesigns.png"),
    ("3-por-que-redesigns-mockups.html", "3-por-que-redesigns.png"),
]


def export_one(page, html_name: str, png_name: str) -> None:
    html = REVIEW / html_name
    out = REVIEW / png_name
    if not html.exists():
        raise SystemExit(f"Missing {html}")
    url = html.as_uri()
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(600)
    height = page.evaluate("() => document.body.scrollHeight")
    page.set_viewport_size({"width": 1280, "height": max(int(height) + 48, 900)})
    page.screenshot(path=str(out), full_page=True)
    print("wrote", out)


def main():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        for html_name, png_name in EXPORTS:
            export_one(page, html_name, png_name)
        browser.close()


if __name__ == "__main__":
    main()
