(function () {
  function pageNicho() {
    const fromBody = document.body?.dataset?.ixNicho;
    if (fromBody && String(fromBody).trim()) return String(fromBody).trim();
    return typeof window.IX_DEFAULT_NICHO === "string" ? window.IX_DEFAULT_NICHO : "otro";
  }

  function pageLanding() {
    const fromBody = document.body?.dataset?.ixLanding;
    if (fromBody && String(fromBody).trim()) return String(fromBody).trim();
    return window.location.pathname || "/";
  }

  function isWhatsAppHref(href) {
    if (!href) return false;
    try {
      const u = new URL(href, window.location.origin);
      return u.hostname === "wa.me" || u.hostname.endsWith(".wa.me");
    } catch {
      return href.indexOf("wa.me/") !== -1;
    }
  }

  document.addEventListener(
    "click",
    function (e) {
      const anchor = e.target.closest("a[href]");
      if (!anchor || !isWhatsAppHref(anchor.getAttribute("href"))) return;
      window.ixTrackEvent?.("whatsapp_click", {
        nicho: anchor.dataset.ixNicho || pageNicho(),
        landing: anchor.dataset.ixLanding || pageLanding(),
        link_url: anchor.getAttribute("href"),
      });
    },
    true
  );
})();
