# Especificación — métricas web → CRM (Odoo Community)

**Versión:** 2026-10-23 · **Owner:** David / pipeline Intrepidux

## Etapas CRM

`New` → `Qualified` → `Proposition` → `Won` / `Lost` (con motivo de pérdida)

## Etiquetas de nicho (`nicho:`)

| Valor | Página / origen |
|-------|-----------------|
| `ecf` | `/facturacion-electronica/` |
| `distribuidora` | `/industrias/distribuidoras-importadoras/` |
| `ferreteria` | `/industrias/ferreterias/` |
| `constructora` | `/industrias/constructoras/` |
| `clinica` | `/industrias/clinicas-dentales/` |
| `nomina` | `/nomina/` |
| `l2-mediana` | `/integraciones/` |
| `otro` | Home y resto |

## UTM — convención

**Fuente (`utm_source`):**

`web-organico` · `web-ia` · `whatsapp` · `google-ads` · `calido` · `frio` · `referido` · `linkedin` · `instagram`

**Campaña (`utm_campaign`):**

- `ecf-15n-2026` — urgencia plazo DGII  
- `nicho-<x>` — ej. `nicho-distribuidora`, `nicho-nomina`

**Medio (`utm_medium`):** `cpc` · `social` · `email` · `referral` · (vacío en orgánico)

**Contenido (`utm_content`):** variante CTA (`hero`, `faq`, `banner-15n`, `footer-wa`)

### Ejemplos

```
?utm_source=web-organico&utm_campaign=ecf-15n-2026&utm_content=banner-15n
?utm_source=whatsapp&utm_campaign=nicho-distribuidora
?utm_source=google-ads&utm_campaign=ecf-15n-2026&utm_medium=cpc
```

[PENDIENTE DAVID] Presupuesto y tope de `google-ads`; no publicar en web.

## Formulario web (campos ocultos — implementación futura)

| Campo | Ejemplo |
|-------|---------|
| `nicho` | `ecf` |
| `landing` | `/facturacion-electronica/` |
| `utm_source` | … |
| `utm_campaign` | … |
| `utm_medium` | … |
| `utm_content` | … |

Campos visibles recomendados (plan):

- ¿Cuántas facturas emites al mes?  
- ¿Cómo nos encontraste? (incluye «ChatGPT u otra IA»)

## GA4 — eventos

| Evento | Cuándo | Parámetros |
|--------|--------|------------|
| `generate_lead` | POST formulario Odoo 201 | `method`, `nicho`, `landing` |
| `whatsapp_click` | Clic en `wa.me` | `nicho`, `landing`, `link_url` |

Configurar como **conversiones** en GA4 cuando exista Measurement ID en `js/analytics-config.js`.

## KPIs (referencia plan 60 días)

| Métrica | ~Día 30 (20 nov) | ~Día 60 (18 dic) |
|---------|------------------|------------------|
| Leads reales web | ≥ 6 | 10–15 / mes |
| Diagnósticos/demos | ≥ 3 | 5 / mes |
| Propuestas / cierres | ≥ 2 / ≥ 1 | 5 / 2 al mes |
| Páginas indexadas | ≥ 6 | ≥ 10 |
| Presencia IA (10×3 consultas) | línea base | ≥ 3/30 |

Revisión: lunes en ritmo de pipeline (Odoo).

## WhatsApp → CRM

Texto precargado con prefijo de nicho (ver `docs/oferta-ecf-a-tiempo.md`). Operador etiqueta lead manualmente hasta automatización.
