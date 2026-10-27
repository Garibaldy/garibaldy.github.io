/**
 * Footer compacto Fase A — mismos links EXPLORAR que la home.
 * data-ix-root: profundidad relativa al root del sitio ("../" desde /nomina/, "../../" desde /industrias/x/).
 */
(function () {
  var root = document.body.getAttribute("data-ix-root");
  if (!root) return;

  var footer = document.createElement("footer");
  footer.className = "ix-footer ix-footer-niche";
  footer.innerHTML =
    '<div class="ix-footer-top container">' +
    '<div class="ix-footer-brand-block">' +
    '<a class="ix-footer-brand" href="' +
    root +
    'index.html#inicio" aria-label="Intrepidux inicio">' +
    '<img src="' +
    root +
    'assets/img/footer-logo.png" alt="Intrepidux" width="120" height="40"/>' +
    "</a>" +
    "<p>Integraciones, e-CF e industrias en República Dominicana.</p>" +
    "</div>" +
    '<nav class="ix-footer-links" aria-label="Navegación del pie de página">' +
    "<div><small>EXPLORAR</small>" +
    '<a href="' +
    root +
    'integraciones/">Integraciones</a>' +
    '<a href="' +
    root +
    'facturacion-electronica/">Facturación e-CF</a>' +
    '<a href="' +
    root +
    'industrias/">Industrias</a>' +
    '<a href="' +
    root +
    'index.html#contacto">Contacto</a>' +
    "</div>" +
    '<div class="mt-3"><small>CONTACTO</small>' +
    '<a href="mailto:proyecto@intrepidux.com">proyecto@intrepidux.com</a>' +
    '<a href="tel:+18296101505">+1 (829) 610-1505</a>' +
    "</div></nav></div>" +
    '<div class="ix-footer-bottom container">' +
    "<span>© Intrepidux 2026</span>" +
    "<span>" +
    '<a href="' +
    root +
    'privacidad/">Privacidad</a> · <a href="' +
    root +
    'terms/">Términos</a>' +
    "</span></div>";

  var sticky = document.querySelector(".ix-sticky-cta");
  if (sticky) {
    document.body.insertBefore(footer, sticky);
  } else {
    document.body.appendChild(footer);
  }
})();
