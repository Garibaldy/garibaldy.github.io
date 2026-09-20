(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reducedMotion.matches) {
    document.documentElement.classList.add("ix-reduced-motion");
  }
  reducedMotion.addEventListener?.("change", (e) => {
    document.documentElement.classList.toggle("ix-reduced-motion", e.matches);
  });

  const geminiBtn = document.querySelector("[data-gemini-open]");
  if (geminiBtn) {
    const aiQuery =
      "Como líder evaluando Intrepidux para ERP, consultoría y software a medida, revisa https://www.intrepidux.com/ y explica qué hace la empresa, para quién es, módulos ERP listados y enfoque de implementación. Responde en español, práctico, sin inventar precios ni garantías.";
    geminiBtn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(aiQuery);
      } catch (_) {
        /* clipboard optional */
      }
      window.open("https://gemini.google.com/app", "_blank", "noopener,noreferrer");
    });
  }
})();

(function () {
  const ODOO_LEAD_URL = "https://erp.intrepidux.com/itx/lead";

  const form = document.getElementById("lead-form");
  if (!form) return;

  const step1 = document.getElementById("lead-step-1");
  const step2 = document.getElementById("lead-step-2");
  const progress = document.querySelector("[data-progress]");
  const contactPct = document.querySelector("[data-contact-pct]");
  const stepTitle = document.querySelector("[data-contact-step-title]");
  const nextBtn = document.querySelector("[data-form-next]");
  const backBtn = document.querySelector("[data-form-back]");
  const submitBtn = document.querySelector("[data-form-submit]");
  const submitFeedback = document.getElementById("lead-submit-feedback");
  const successPanel = document.getElementById("lead-success");
  const honeypot = document.getElementById("lead-honeypot");
  const formFooter = form.querySelector(".ix-embedded-form-footer");

  const submitDefaultHtml = submitBtn?.innerHTML ?? "";

  function setFormProgress(percent, title) {
    if (progress) {
      progress.style.width = `${percent}%`;
      const bar = progress.closest('[role="progressbar"]');
      if (bar) bar.setAttribute("aria-valuenow", String(percent));
    }
    if (contactPct) contactPct.textContent = `${percent}%`;
    if (stepTitle && title) stepTitle.textContent = title;
  }

  function setStepUi(step) {
    const onStep2 = step === 2;
    step1?.classList.toggle("d-none", onStep2);
    step2?.classList.toggle("d-none", !onStep2);
    backBtn?.classList.toggle("d-none", !onStep2);
    nextBtn?.classList.toggle("d-none", onStep2);
    submitBtn?.classList.toggle("d-none", !onStep2);
    setFormProgress(onStep2 ? 50 : 25, onStep2 ? "Tu operación" : "Identificación");
  }

  function clearFieldState(input) {
    input.removeAttribute("aria-invalid");
    input.classList.remove("is-invalid");
  }

  function markInvalid(input, messageId) {
    input.setAttribute("aria-invalid", "true");
    input.classList.add("is-invalid");
    const msg = document.getElementById(messageId);
    if (msg) msg.textContent = "Completa este campo.";
  }

  function validateStep1() {
    const name = form.querySelector("#lead-name");
    const email = form.querySelector("#lead-email");
    let ok = true;

    ["lead-name-error", "lead-email-error"].forEach((id) => {
      const el = document.getElementById(id);
      if (el) el.textContent = "";
    });
    [name, email].forEach(clearFieldState);

    if (!name.value.trim()) {
      markInvalid(name, "lead-name-error");
      ok = false;
    }
    if (!email.value.trim() || !email.validity.valid) {
      markInvalid(email, "lead-email-error");
      ok = false;
    }
    return ok;
  }

  function validateStep2() {
    const required = step2?.querySelectorAll("[required]") || [];
    let ok = true;
    required.forEach((el) => {
      clearFieldState(el);
      if (!el.value.trim()) {
        el.setAttribute("aria-invalid", "true");
        el.classList.add("is-invalid");
        ok = false;
      }
    });
    return ok;
  }

  function buildLeadPayload() {
    const data = new FormData(form);
    const telefono = (data.get("telefono") || "").toString().trim();
    return {
      nombre: (data.get("nombre") || "").toString().trim(),
      email: (data.get("email") || "").toString().trim(),
      empresa: (data.get("empresa") || "").toString().trim(),
      telefono,
      sector: (data.get("sector") || "").toString().trim(),
      personas: (data.get("personas") || "").toString().trim(),
      info: data.getAll("info").map((v) => v.toString()),
      problema: (data.get("problema") || "").toString().trim(),
      website: window.location.hostname || "www.intrepidux.com",
      _honeypot: (data.get("_honeypot") || "").toString(),
    };
  }

  function setSubmitting(active) {
    if (!submitBtn) return;
    submitBtn.disabled = active;
    if (active) {
      submitBtn.textContent = "Enviando…";
    } else {
      submitBtn.innerHTML = submitDefaultHtml;
    }
  }

  function showSuccess() {
    step1?.classList.add("d-none");
    step2?.classList.add("d-none");
    formFooter?.classList.add("d-none");
    successPanel?.classList.remove("d-none");
    setFormProgress(100, "Listo");
    if (submitFeedback) submitFeedback.textContent = "";
  }

  function fetchOptions() {
    const opts = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(buildLeadPayload()),
    };
    if (typeof AbortSignal !== "undefined" && typeof AbortSignal.timeout === "function") {
      opts.signal = AbortSignal.timeout(30000);
    }
    return opts;
  }

  nextBtn?.addEventListener("click", () => {
    if (!validateStep1()) return;
    setStepUi(2);
    step2?.querySelector("input, select, textarea")?.focus();
  });

  backBtn?.addEventListener("click", () => {
    setStepUi(1);
    step1?.querySelector("input")?.focus();
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!validateStep2()) return;

    if (honeypot?.value.trim()) {
      return;
    }

    if (submitFeedback) submitFeedback.textContent = "";
    setSubmitting(true);

    let succeeded = false;
    try {
      const res = await fetch(ODOO_LEAD_URL, fetchOptions());
      const data = await res.json().catch(() => ({}));

      if (res.status === 201 && data.ok) {
        succeeded = true;
        showSuccess();
        return;
      }

      const message =
        (typeof data.error === "string" && data.error) ||
        "No pudimos enviar tu solicitud. Intenta de nuevo o escríbenos a proyecto@intrepidux.com.";
      if (submitFeedback) submitFeedback.textContent = message;
    } catch {
      if (submitFeedback) {
        submitFeedback.textContent =
          "Error de conexión. Comprueba tu red e inténtalo de nuevo, o escríbenos a proyecto@intrepidux.com.";
      }
    } finally {
      if (!succeeded) setSubmitting(false);
    }
  });
})();
