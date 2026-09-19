import re
from pathlib import Path

css_path = Path(r"C:\Users\David\AppData\Local\Temp\ix-vercel.css")
if not css_path.exists():
    css_path = Path(__file__).resolve().parents[1] / "assets/review/vercel.css"

css = css_path.read_text(encoding="utf-8", errors="ignore")
keys = [
    "contact-copy",
    "contact-form-card",
    "embedded-form",
    "section-kicker",
    "button-orange",
    ".cta",
    "#contacto",
]
for key in keys:
    pat = re.compile(r"\.[^{]*" + re.escape(key.replace(".", "")) + r"[^{]*\{[^}]+\}", re.I)
    hits = pat.findall(css)
    if not hits:
        # try simpler
        idx = css.find(key)
        if idx >= 0:
            print(f"\n=== {key} (context) ===\n", css[idx : idx + 400][:400])
    else:
        print(f"\n=== {key} ({len(hits)} rules) ===")
        for h in hits[:8]:
            print(h[:500])
