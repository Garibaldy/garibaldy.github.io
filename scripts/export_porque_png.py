"""Export por-que-redesigns-mockups.html to PNG via Playwright."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "assets/review/por-que-redesigns-mockups.html"
OUT = ROOT / "assets/review/por-que-redesigns.png"


def main():
    if not HTML.exists():
        raise SystemExit(f"Missing {HTML}")
    from playwright.sync_api import sync_playwright

    url = HTML.as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(500)
        height = page.evaluate("() => document.body.scrollHeight")
        page.set_viewport_size({"width": 1280, "height": max(height + 40, 900)})
        page.screenshot(path=str(OUT), full_page=True)
        browser.close()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
