/**
 * Configuración global del sitio (un solo lugar para toggles de W1).
 * David: edita aquí antes de publicar cambios de campaña.
 */
(function () {
  /** Banner urgencia DGII e-CF (Pequeños, Micro, No Clasificados). */
  window.IX_BANNER_15N_ENABLED = true;

  /**
   * Fecha ISO (medianoche local del navegador) tras la cual el banner se oculta solo.
   * null = solo IX_BANNER_15N_ENABLED controla visibilidad.
   */
  window.IX_BANNER_15N_HIDE_AFTER = "2026-11-16";

  /** Parámetros GA4 por defecto para páginas sin data-ix-nicho en <body>. */
  window.IX_DEFAULT_NICHO = "otro";
})();
