# CHANGELOG — www.intrepidux.com (W1)

**Rama:** `web/w1-seo-hub-ecf`  
**Fecha:** 2026-10-23  
**Alcance:** SEO técnico, GA4 (placeholder), hub `/facturacion-electronica/`, banner 15N, AEO base (`llms.txt`), docs oferta/CRM/GBP.

**PR:** https://github.com/Garibaldy/garibaldy.github.io/pull/2

## Cambios por archivo

| Archivo | Cambio | Motivo |
|---------|--------|--------|
| `robots.txt` | Nuevo | Corregir 404; permitir crawlers IA (GPTBot, OAI-SearchBot, PerplexityBot); apuntar sitemap |
| `sitemap.xml` | Nuevo | Listar URLs públicas reales (home, hub e-CF, integraciones, privacidad, terms) |
| `facturacion-electronica/index.html` | Nuevo | Hub L1 según plan: secciones, tabla FG, pasos, integración, nichos, FAQ, JSON-LD |
| `css/ecf-hub.css` | Nuevo | Estilos del hub alineados a tokens existentes |
| `css/banner-15n.css` | Nuevo | Estilos banner plazo DGII |
| `js/site-config.js` | Nuevo | Toggle `IX_BANNER_15N_ENABLED` y fecha auto-ocultar |
| `js/banner-15n.js` | Nuevo | Componente banner 15N (dismiss por sesión) |
| `js/analytics-config.js` | Actualizado | Documentación única del Measurement ID GA4 (placeholder, vacío = sin tracking) |
| `js/analytics-cta.js` | Nuevo | Evento `whatsapp_click` con `nicho` y `landing` |
| `js/main.js` | Actualizado | Evento `generate_lead` incluye `nicho` y `landing` |
| `index.html` | Actualizado | Banner 15N + scripts analytics/CTA; `data-ix-nicho` en body |
| `llms.txt` | Nuevo | AEO: mapa del sitio para asistentes |
| `docs/oferta-ecf-a-tiempo.md` | Nuevo | Argumentario y objeciones (sin publicar precios/plazos) |
| `docs/crm-metricas-web.md` | Nuevo | UTM, etiquetas nicho, eventos GA4, KPIs |
| `docs/aeo-gbp-linkedin.md` | Nuevo | Notas GBP/LinkedIn/Bing (solo doc, no envíos) |
| `css/niche-industria.css` | Nuevo | Estilos compartidos páginas de nicho |
| `facturacion-electronica/index.html` | Actualizado | Prueba social [PENDIENTE], FAQ oferta e-CF a Tiempo |

**No incluido en W1 (fuera de alcance o bloqueado):**

| Tema | Estado |
|------|--------|
| LinkedIn `linkedin.com/intrepiduxerp` | **TODO:** no se pudo confirmar URL `/company/…` (LinkedIn devuelve 999 a bots; búsqueda web no listó página de empresa). El enlace actual responde HTTP 200 como vanity URL. **David:** confirmar URL canónica y actualizar footer en `index.html` y `terms/index.html`. |
| Hero home e-CF / mención DGII en portada | Pendiente decisión hero A/B/C (plan) |
| `/nomina/`, nichos `/industrias/…`, `/blog/` | Semanas W2–W6 |
| ID GA4 real | David pega `G-…` en `js/analytics-config.js` |
| `erp.intrepidux.com`, `dental.intrepidux.com` | Otros repos — no tocados |

## Placeholders visibles en el hub

- Bloque **Decisiones comerciales [PENDIENTE DAVID]**: hero final, garantía, precio e-CF, días hábiles, cupos semanales.
- Tope mensual Facturador Gratuito: `[PENDIENTE: confirmar tope con DGII]`.
- Tarjetas de nicho sin enlaces hasta publicar páginas W2–W6.
- `/odoo/` mencionado como página futura.
- Sin aliados estratégicos (requieren permiso escrito).
- Sin cifras de clientes, logos nuevos ni testimonios inventados (solo cita ya en portada).

## Configuración operativa

```javascript
// js/site-config.js
IX_BANNER_15N_ENABLED = true;      // false = apagar banner en todo el sitio que carga banner-15n.js
IX_BANNER_15N_HIDE_AFTER = "2026-11-16";

// js/analytics-config.js
IX_GA_MEASUREMENT_ID = "";         // pegar G-XXXXXXXXXX de GA4 para activar gtag
```

## Checklist — decisiones pendientes (David)

- [ ] Hero home: variante A, B o C (e-CF 15N vs operación post-16 nov)
- [ ] Texto de garantía publicable (recomendación interna: tipos 1 + 4)
- [ ] Presentación de precio e-CF (recomendación A: diagnóstico 20 min, sin cifra nueva)
- [ ] Publicar o no plazo en N días hábiles
- [ ] Cupos semanales reales (o no usar escasez)
- [ ] Pegar Measurement ID GA4 en `js/analytics-config.js`
- [ ] Confirmar URL LinkedIn empresa y corregir footer si aplica
- [ ] Confirmar tope Facturador Gratuito con DGII antes de quitar placeholder en tabla
- [ ] Permisos de aliados (WebPOS, VBS, LifterDO, Gestión Simple) antes de franja en home/hub

## Cómo verificar (preview local)

```bash
cd /ruta/al/repo
python3 -m http.server 8080
```

| Verificación | URL / acción |
|--------------|----------------|
| robots.txt | http://localhost:8080/robots.txt |
| sitemap.xml | http://localhost:8080/sitemap.xml |
| Hub e-CF | http://localhost:8080/facturacion-electronica/ |
| Banner 15N | Home y hub — toggle en `js/site-config.js` |
| GA4 sin ID | Consola de red: no debe cargar `gtag/js` si `IX_GA_MEASUREMENT_ID` está vacío |
| GA4 con ID | Pegar ID de prueba/staging → cargar página → Tag Assistant / DebugView |
| whatsapp_click | Clic en WhatsApp del hub → evento (con ID configurado) |
| generate_lead | Enviar formulario home (Odoo CRM) → evento con `nicho`, `landing` |
| JSON-LD | [Rich Results Test](https://search.google.com/test/rich-results) con URL publicada |
| Canonical / title hub | Ver `<head>` de `/facturacion-electronica/` |

---

# CHANGELOG — W2 (distribuidoras)

**Rama:** `web/w2-distribuidoras` (base: `web/w1-seo-hub-ecf`)  
**PR:** (al crear)  
**Alcance:** Página distribuidoras, índice industrias, guía plazo 15 nov, sitemap.

| Archivo | Cambio |
|---------|--------|
| `industrias/distribuidoras-importadoras/index.html` | Nicho #2: inventario + e-CF, FAQ, JSON-LD |
| `industrias/index.html` | Índice de sectores |
| `facturacion-electronica/fecha-limite-15-noviembre/index.html` | Guía sobria plazo DGII |
| `facturacion-electronica/index.html` | Enlace tarjeta distribuidoras |
| `sitemap.xml` | URLs W2 |

**Verificar:** `/industrias/distribuidoras-importadoras/`, `/facturacion-electronica/fecha-limite-15-noviembre/`, WhatsApp `[DIS]`.

---

# CHANGELOG — W3 (nómina)

**Rama:** `web/w3-nomina` (base: `web/w2-distribuidoras`)

| Archivo | Cambio |
|---------|--------|
| `nomina/index.html` | Página TSS → nómina → ponchador → banco, FAQ, turnos secundarios |
| `industrias/index.html` | Enlace nómina |
| `facturacion-electronica/index.html` | Enlace a `/nomina/` |
| `sitemap.xml` | `/nomina/` |

**Verificar:** `/nomina/`, WhatsApp `[NOM]`, sin LaborPay ni precios.
