/** @deprecated Fase A usa HTML estático en `partials/footer-fase-a-*.html`. */
(function () {
  if (document.querySelector(".ix-footer-niche")) return;
  var root = document.body.getAttribute("data-ix-root");
  if (!root) return;
  /* legacy inject — no-op if static footer present */
})();
