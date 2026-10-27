# CHANGELOG consolidado — plan web nichos (W1–W6)

**Rama única:** `web/w1-seo-hub-ecf`  
**PR:** https://github.com/Garibaldy/garibaldy.github.io/pull/2  
**Fecha:** 2026-10-23 · **Autor commits:** Garibaldy \<davidcv9@gmail.com\>

Entrega en **un solo PR** (hub + nichos + SEO/AEO + docs). Sin precios, garantías, plazos comerciales ni testimonios/logos inventados.

---

## 1. SEO técnico (W1)

| Archivo | Qué |
|---------|-----|
| `robots.txt` | Allow + GPTBot/OAI-SearchBot/PerplexityBot + sitemap |
| `sitemap.xml` | Todas las URLs públicas listadas abajo |
| `index.html` | `canonical`, JSON-LD `Organization`, nav «Facturación e-CF», placeholders prueba social |
| `js/analytics-config.js` | **Único** punto GA4 (`IX_GA_MEASUREMENT_ID`, vacío = off) |
| `js/analytics.js` / `js/analytics-cta.js` | gtag + `generate_lead` / `whatsapp_click` (`nicho`, `landing`) |
| `js/main.js` | `generate_lead` con parámetros de página |

**Verificar:** `/robots.txt`, `/sitemap.xml`, view-source home (schema).

---

## 2. Hub e-CF + banner 15N (W1)

| Archivo | Qué |
|---------|-----|
| `facturacion-electronica/index.html` | Hub L1: plazo DGII, tabla FG, pasos, integración, nichos, FAQ×14, oferta FAQ, prueba social |
| `css/ecf-hub.css` | Estilos hub |
| `js/site-config.js` | `IX_BANNER_15N_ENABLED`, `IX_BANNER_15N_HIDE_AFTER` |
| `js/banner-15n.js` + `css/banner-15n.css` | Banner toggle (home + páginas que cargan script) |

**Placeholders hub:** garantía, precio, N días, cupos, tope FG [DGII], hero A/B/C.

---

## 3. Guía plazo 15 nov (W2)

| Archivo | Qué |
|---------|-----|
| `facturacion-electronica/fecha-limite-15-noviembre/index.html` | Guía sobria + enlaces DGII |

---

## 4. Nichos (W2–W6)

| URL | Rama lógica | WhatsApp |
|-----|-------------|----------|
| `/industrias/` | Índice | — |
| `/industrias/distribuidoras-importadoras/` | W2 | `[DIS]` |
| `/nomina/` | W3 TSS + ponchador | `[NOM]` |
| `/industrias/ferreterias/` | W4 + callout 15N | `[FER]` |
| `/industrias/constructoras/` | W5 ponchador/obra | `[CON]` |
| `/industrias/clinicas-dentales/` | W6 | `[DEN]` |

| Archivo compartido | Qué |
|--------------------|-----|
| `css/niche-industria.css` | Layout nichos + `.ix-niche-social-placeholder` |

Cada nicho: enlace al hub e-CF, bloque **[PENDIENTE]** prueba social, sin Odoo en H1.

---

## 5. AEO (W2–W6 doc + sitio)

| Archivo | Qué |
|---------|-----|
| `llms.txt` | Mapa para asistentes |
| `docs/aeo-gbp-linkedin.md` | Notas GBP/LinkedIn/Bing (**solo doc**, no envíos) |
| FAQ + JSON-LD | Hub (FAQPage dinámico), Service/Breadcrumb en nichos principales |

---

## 6. Documentación comercial / CRM (no publicada en CTAs)

| Archivo | Qué |
|---------|-----|
| `docs/oferta-ecf-a-tiempo.md` | Argumentario + objeciones |
| `docs/crm-metricas-web.md` | UTM, etiquetas nicho, eventos GA4, KPIs 30/60 días |

---

## 7. Prueba social (placeholders)

- Home `#testimonios`: cita existente + caja [PENDIENTE] logos/casos  
- Hub e-CF: testimonio portada + [PENDIENTE] aliados/clientes  
- Cada nicho: `.ix-niche-social-placeholder`  

**No** añadidos: logos Glowicom, stats, nombres de clientes nuevos.

---

## 8. Pendientes David (checklist)

- [ ] `IX_GA_MEASUREMENT_ID` real en `js/analytics-config.js`  
- [ ] Hero home e-CF vs operación (A/B/C)  
- [ ] Garantía, precio e-CF, N días, cupos, ads  
- [ ] LinkedIn URL `/company/…` (footer sigue `linkedin.com/intrepiduxerp` — **TODO**)  
- [ ] Tope Facturador Gratuito (tabla hub)  
- [ ] Permisos aliados FE y casos por nicho  
- [ ] Campos ocultos UTM/nicho en formulario Odoo  
- [ ] `/odoo/`, `/integraciones/api-nomina/`, `/blog/` — fuera de este PR  

---

## 9. Preview local

```bash
python3 -m http.server 8080
```

URLs clave: `/`, `/facturacion-electronica/`, `/nomina/`, `/industrias/distribuidoras-importadoras/`, `/industrias/ferreterias/`, ferreterías → guía 15 nov.

---

## 10. Home ↔ nichos (conexión)

- Nav: Integraciones antes que e-CF; link `industrias/`
- Hero: CTA primario → integraciones; secundario contacto; línea e-CF hub
- `#sectores`: mismas 6 rutas que `/industrias/` + medianas → integraciones
- Footer EXPLORAR: hub e-CF + industrias

## 11. UX nichos (Hormozi — solo `/industrias/*` y `/nomina/`)

- `css/offer-ux.css` importado vía `niche-industria.css`
- Por página: ecuación de valor (`.ix-value-grid`), stack (`.ix-stack`), pasos post-CTA (`.ix-next-steps`), banda CTA, sticky móvil
- Home y hub e-CF **sin** estos bloques

## 12. Fuera de alcance

- `erp.intrepidux.com`, `dental.intrepidux.com` (otros repos)  
- Merge a `master` (David decide)  
- PR #3 obsoleto — usar solo **PR #2**
