import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "assets/review/vercel-home.html"
h = p.read_text(encoding="utf-8", errors="ignore")
idx = h.find('id="contacto"')
if idx < 0:
    idx = h.find("contacto")
out = Path(__file__).resolve().parents[1] / "assets/review/vercel-contact-snippet.html"
out.write_text(h[idx : idx + 12000], encoding="utf-8")
print("wrote", out, "len", len(h[idx : idx + 12000]))
