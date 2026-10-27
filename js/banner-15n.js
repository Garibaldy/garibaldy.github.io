(function () {
  if (!window.IX_BANNER_15N_ENABLED) return;

  const hideAfter = window.IX_BANNER_15N_HIDE_AFTER;
  if (hideAfter) {
    const cutoff = new Date(hideAfter + "T00:00:00");
    if (!Number.isNaN(cutoff.getTime()) && Date.now() >= cutoff.getTime()) return;
  }

  const hubHref = "/facturacion-electronica/";
  const banner = document.createElement("div");
  banner.className = "ix-banner-15n";
  banner.setAttribute("role", "region");
  banner.setAttribute("aria-label", "Plazo facturación electrónica DGII");
  banner.innerHTML =
    '<div class="ix-banner-15n-inner">' +
    '<p><strong>Plazo DGII e-CF:</strong> Pequeños, Micro y No Clasificados — referencia <time datetime="2026-11-15">15 nov 2026</time>. ' +
    'Confirma obligación y plazos en fuentes oficiales antes de decidir.</p>' +
    '<a class="ix-banner-15n-cta" href="' +
    hubHref +
    '">Guía facturación electrónica</a>' +
    '<button type="button" class="ix-banner-15n-dismiss" aria-label="Cerrar aviso">×</button>' +
    "</div>";

  document.body.insertBefore(banner, document.body.firstChild);

  banner.querySelector(".ix-banner-15n-dismiss")?.addEventListener("click", function () {
    banner.remove();
    try {
      sessionStorage.setItem("ix-banner-15n-dismissed", "1");
    } catch (_) {
      /* optional */
    }
  });

  try {
    if (sessionStorage.getItem("ix-banner-15n-dismissed") === "1") banner.remove();
  } catch (_) {
    /* optional */
  }
})();
