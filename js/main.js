(function () {
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

  nextBtn?.addEventListener("click", () => {
    if (!validateStep1()) return;
    setStepUi(2);
    step2?.querySelector("input, select, textarea")?.focus();
  });

  backBtn?.addEventListener("click", () => {
    setStepUi(1);
    step1?.querySelector("input")?.focus();
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
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
    if (!ok) return;

    const data = new FormData(form);
    const body = [...data.entries()]
      .map(([k, v]) => `${k}: ${v}`)
      .join("\n");
    window.location.href = `mailto:proyecto@intrepidux.com?subject=${encodeURIComponent(
      "Evaluación inicial Intrepidux"
    )}&body=${encodeURIComponent(body)}`;
  });
})();
