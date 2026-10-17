# garibaldy.github.io

Sitio estático de [Intrepidux](https://www.intrepidux.com/) (HTML + Bootstrap, sin build). Se publica con **GitHub Pages**; el dominio custom está en `CNAME` → `www.intrepidux.com`.

## URLs

| Página | Ruta |
|--------|------|
| Inicio | https://www.intrepidux.com/ |
| Integraciones | https://www.intrepidux.com/integraciones/ |
| Términos | https://www.intrepidux.com/terms/ |
| Privacidad | https://www.intrepidux.com/privacidad/ |
| Servicio suspendido | https://www.intrepidux.com/servicio-suspendido/ |

También responde en https://garibaldy.github.io/ si abres el Pages del repo sin custom domain.

## Cómo editar

| Quiero cambiar… | Archivo |
|-----------------|---------|
| Textos, secciones, enlaces del menú | `index.html` |
| Colores, tipografía, layout | `css/intrepidux-vercel.css` (entrada vía `css/theme.css`) |
| Formulario (pasos, validación, envío) | `js/main.js` + bloque `#contacto` en `index.html` |
| Google Analytics 4 | `js/analytics-config.js` → `G-…` (vacío = sin tracking) |
| Logo, favicon, hero | `assets/logo.png`, `assets/favicon.ico`, `assets/img/hero-laptop.png` |
| Iconos footer (AI + redes) | `assets/img/icons/*.png` |
| Logos de clientes (franja) | `assets/img/clientes-iconos.png` y `#clientes` en `index.html` |
| Landing integraciones | `integraciones/index.html` |

## Vista local

Sirve la carpeta con un servidor estático (evita `file://` para rutas y el formulario):

```powershell
cd c:\Users\David\Documents\garibaldy.github.io
py -3 -m http.server 8765
```

Abre http://localhost:8765/

## Capturas por sección (opcional)

Requiere Playwright. Con el servidor local arriba en otra terminal:

```powershell
py -3 -m pip install playwright
py -3 -m playwright install chromium
py -3 scripts\capture_blocks.py --target local
```

Salida: `assets/review/local/*.png`

## Stack

- Bootstrap 5.3 (CDN)
- Deploy: push a la rama configurada en GitHub Pages (p. ej. `master`)
