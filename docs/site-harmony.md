# Armonía del sitio (chrome unificado)

## Regla

Todas las páginas públicas de marketing comparten:

1. **Header Fase B** — `ix-header-site` + 7 enlaces + CTA (plantilla `partials/header-fase-b-root.html`).
2. **Footer home** — bloque completo de `index.html` (`partials/footer-home-root.html`).
3. **DOM** — `skip link` → `header` → `main#main-content` → `footer` (el header **no** va dentro de `main`).

Excepción: `servicio-suspendido/` (página técnica aislada, sin chrome de marketing).

## Mantenimiento

| Cambio | Comando |
|--------|---------|
| Footer | Editar `partials/footer-home-root.html` → `python3 scripts/sync-footers-from-root.py` |
| Nav | Editar `partials/header-fase-b-root.html` → `python3 scripts/sync-headers-from-root.py` (+ marcar `active` en cada HTML de sector) |
| Verificación | `python3 scripts/site-harmony-check.py` |

## Páginas cubiertas por `site-harmony-check.py`

Home, 404, integraciones, hub e-CF, guía 15N, índice y landings de industrias, nómina, términos, privacidad.
