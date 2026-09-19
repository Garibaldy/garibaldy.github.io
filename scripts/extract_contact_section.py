from pathlib import Path
import re

h = Path(__file__).resolve().parents[1].joinpath("assets/review/vercel-home.html").read_text(
    encoding="utf-8", errors="ignore"
)
m = re.search(r'<section[^>]*id="contacto"[^>]*>', h)
if m:
    start = m.start()
    print(m.group(0))
else:
    start = h.find('id="contacto"') - 50
    print("no section tag", h[start : start + 80])

end = h.find("</section>", start)
block = h[start:end + 10] if end > start else h[start : start + 5000]
Path(__file__).resolve().parents[1].joinpath("assets/review/vercel-contact-section.html").write_text(
    block, encoding="utf-8"
)
print("len", len(block))
