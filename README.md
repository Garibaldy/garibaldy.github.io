# garibaldy.github.io

Sitio estático de [Intrepidux](https://intrepidux.vercel.app/) (shadow copy editable en HTML + Bootstrap).

- **Inicio:** https://garibaldy.github.io/
- **Servicio suspendido:** https://garibaldy.github.io/servicio-suspendido/

## Cómo editar

| Quiero cambiar… | Archivo |
|-----------------|---------|
| Textos, secciones, enlaces del menú | `index.html` |
| Colores, tipografía, look tipo Vercel | `css/intrepidux-vercel.css` (importado desde `css/theme.css`) |
| Formulario (pasos, validación, envío) | `js/main.js` + bloque `#contacto` en `index.html` |
| Logo, favicon, hero | `assets/logo.png`, `assets/favicon.ico`, `assets/img/hero-laptop.png` |
| Logos de clientes (franja) | `assets/img/clientes-iconos.png` y sección `#clientes` en `index.html` |

## Vista local

Abre `index.html` en el navegador o sirve la carpeta con cualquier servidor estático.

## Capturas para comparar con Vercel (automático)

No hace falta [Screenshot Machine](https://www.screenshotmachine.com/website-screenshot-generator.php) manual: en la API usan `1440xfull` (altura `full`, no 9999).

```powershell
cd c:\Users\David\Documents\garibaldy.github.io
py -3 -m pip install playwright
py -3 -m playwright install chromium

# Solo referencia Vercel
py -3 scripts\capture_blocks.py --target vercel

# Local (en otra terminal: py -3 -m http.server 8765)
py -3 scripts\capture_blocks.py --target local

# Ambos
py -3 scripts\capture_blocks.py --target both
```

Salida: `assets/review/vercel/*.png` y `assets/review/local/*.png` (por sección + chunks de página larga).

Opcional con API key: `scripts/capture_screenshotmachine.ps1` y `$env:SCREENSHOT_MACHINE_KEY`.

## Stack

- Bootstrap 5.3 (CDN)
- Sin build: solo subir archivos a GitHub Pages (`master`).

## Estado del plan

- **Pasada 1** (conversión, SEO, a11y básica): aplicada.
- **Pasadas 2–3** (marca fina vs Vercel, craft/motion): pendientes.
