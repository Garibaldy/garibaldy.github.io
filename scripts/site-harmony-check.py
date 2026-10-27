#!/usr/bin/env python3
"""Lista desvíos del chrome unificado (nav 7 ítems, footer home, header fuera de main)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = [
    "index.html",
    "404.html",
    "integraciones/index.html",
    "facturacion-electronica/index.html",
    "facturacion-electronica/fecha-limite-15-noviembre/index.html",
    "industrias/index.html",
    "nomina/index.html",
    "industrias/ferreterias/index.html",
    "industrias/distribuidoras-importadoras/index.html",
    "industrias/constructoras/index.html",
    "industrias/clinicas-dentales/index.html",
    "terms/index.html",
    "privacidad/index.html",
]
NAV_LABELS = (
    "Soluciones",
    "Integraciones",
    "Facturación e-CF",
    "Industrias",
    "Cómo trabajamos",
    "Casos",
    "Nosotros",
)
issues: list[str] = []

for rel in PUBLIC:
    p = ROOT / rel
    if not p.exists():
        issues.append(f"{rel}: missing file")
        continue
    t = p.read_text()
    if "ix-header-site" not in t:
        issues.append(f"{rel}: sin header Fase B")
    if re.search(r"<main[^>]*>\s*<header class=\"ix-header-site\"", t, re.S):
        issues.append(f"{rel}: header dentro de main")
    for label in NAV_LABELS:
        if label not in t:
            issues.append(f"{rel}: nav sin «{label}»")
    if "ix-footer-niche" in t:
        issues.append(f"{rel}: footer niche obsoleto")
    if "Implementamos ERP y desarrollamos software a medida" not in t and rel != "index.html":
        if "ix-footer" in t and rel not in ("404.html",):
            issues.append(f"{rel}: footer no es el de home")
    if rel == "404.html" and "facturacion-electronica/" not in t:
        issues.append(f"{rel}: footer sin e-CF")
    if "#sectores" in t and "index.html#sectores" not in t and rel not in ("index.html",):
        issues.append(f"{rel}: enlace obsoleto #sectores en nav/footer")

if issues:
    print("ARMONÍA — problemas:\n")
    print("\n".join(f"  - {i}" for i in issues))
    sys.exit(1)
print("ARMONÍA OK — chrome unificado en páginas públicas listadas.")
sys.exit(0)
