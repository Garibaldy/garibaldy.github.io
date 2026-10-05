(function () {
  const id =
    typeof window.IX_GA_MEASUREMENT_ID === "string" ? window.IX_GA_MEASUREMENT_ID.trim() : "";
  if (!/^G-[A-Z0-9]+$/i.test(id)) {
    return;
  }

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  window.ixTrackEvent = function (eventName, params) {
    gtag("event", eventName, params || {});
  };

  gtag("js", new Date());
  gtag("config", id, {
    send_page_view: true,
    anonymize_ip: true,
  });

  const link = document.createElement("link");
  link.rel = "preconnect";
  link.href = "https://www.googletagmanager.com";
  document.head.appendChild(link);

  const script = document.createElement("script");
  script.async = true;
  script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
  document.head.appendChild(script);
})();
