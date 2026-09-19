from pathlib import Path
import re

css = Path(r"C:\Users\David\AppData\Local\Temp\ix-vercel.css").read_text(encoding="utf-8", errors="ignore")
selectors = [
    "contact-section",
    "contact-copy",
    "contact-form-card",
    "embedded-form",
    "section-kicker",
    "button-orange",
    "section-pad",
]
out_lines = []
for sel in selectors:
    for m in re.finditer(r"[^\{]*" + sel + r"[^\{]*\{", css):
        start = m.start()
        depth = 0
        i = css.find("{", start)
        j = i
        while j < len(css):
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
                if depth == 0:
                    chunk = css[start : j + 1]
                    if len(chunk) < 2000 and sel in chunk:
                        out_lines.append(chunk)
                    break
            j += 1

path = Path(__file__).resolve().parents[1] / "assets/review/vercel-contact-css-extract.txt"
path.write_text("\n\n".join(out_lines[:40]), encoding="utf-8")
print("rules", len(out_lines), "->", path)
