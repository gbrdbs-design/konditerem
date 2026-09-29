// konditeremberendezesek.hu – prototípus interakciók
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  // Mobil menü
  const toggle = $(".nav__toggle");
  if (toggle) {
    const close = () => { document.body.classList.remove("nav-open"); toggle.setAttribute("aria-expanded", "false"); };
    toggle.addEventListener("click", () => {
      const open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    $$(".site-header .nav__menu a").forEach(a => a.addEventListener("click", close));
    document.addEventListener("keydown", e => { if (e.key === "Escape") close(); });
  }

  // Görgetéskor tapadó fejléc
  const header = $(".site-header");
  if (header) {
    const spacer = document.createElement("div");
    const barMode = header.classList.contains("site-header--bar");
    header.after(spacer);
    const threshold = barMode ? header.offsetHeight : 400;
    const onScroll = () => {
      const stick = window.scrollY > threshold;
      if (stick === header.classList.contains("is-sticky")) return;
      header.classList.toggle("is-sticky", stick);
      spacer.style.height = stick && barMode ? header.offsetHeight + "px" : "0";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // GYIK harmonika
  $$(".faq__item").forEach(item => {
    const btn = $(".faq__q", item);
    btn.addEventListener("click", () => {
      const open = !item.classList.contains("is-open");
      $$(".faq__item.is-open", item.parentElement).forEach(o => { o.classList.remove("is-open"); $(".faq__q", o).setAttribute("aria-expanded", "false"); });
      item.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
  });

  // Karusszel pöttyök (mobilon görgethető sávok)
  $$("[data-carousel]").forEach(track => {
    const dots = document.getElementById(track.dataset.carousel);
    if (!dots) return;
    const slides = Array.from(track.children);
    dots.innerHTML = "";
    slides.forEach((s, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", `${i + 1}. elem`);
      b.addEventListener("click", () => track.scrollTo({ left: s.offsetLeft - track.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: "smooth" }));
      dots.appendChild(b);
    });
    const update = () => {
      const center = track.scrollLeft + track.clientWidth / 2;
      let best = 0, dist = Infinity;
      slides.forEach((s, i) => {
        const c = s.offsetLeft - track.offsetLeft + s.clientWidth / 2;
        if (Math.abs(c - center) < dist) { dist = Math.abs(c - center); best = i; }
      });
      Array.from(dots.children).forEach((d, i) => d.setAttribute("aria-current", String(i === best)));
    };
    track.addEventListener("scroll", () => requestAnimationFrame(update), { passive: true });
    window.addEventListener("resize", update);
    update();
  });

  // Termékgaléria nyilak
  $$(".gallery").forEach(g => {
    const track = $(".gallery__track", g);
    const step = () => (track.firstElementChild ? track.firstElementChild.clientWidth + 30 : 300);
    $(".gallery__arrow--prev", g)?.addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
    $(".gallery__arrow--next", g)?.addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));
  });

  // Rendezés (prototípus: csak a sorrendet fordítja)
  const sort = $("#sort");
  if (sort) {
    sort.addEventListener("change", () => {
      const list = $(".products");
      Array.from(list.children).reverse().forEach(el => list.appendChild(el));
    });
  }

  // Lapozó
  const pager = $(".pager");
  if (pager) {
    const pages = $$(".pager__pages button", pager);
    const prev = $(".pager__arrow--prev", pager), next = $(".pager__arrow--next", pager);
    let cur = 0;
    const set = i => {
      cur = Math.max(0, Math.min(pages.length - 1, i));
      pages.forEach((p, j) => j === cur ? p.setAttribute("aria-current", "page") : p.removeAttribute("aria-current"));
      prev.disabled = cur === 0; next.disabled = cur === pages.length - 1;
      $(".products")?.scrollIntoView({ behavior: "smooth", block: "start" });
    };
    pages.forEach((p, i) => p.addEventListener("click", () => set(i)));
    prev.addEventListener("click", () => set(cur - 1));
    next.addEventListener("click", () => set(cur + 1));
    prev.disabled = true;
  }

  // Ajánlatkérő űrlap
  const form = $(".form");
  if (form) {
    const file = $('input[type="file"]', form), fileName = $(".file-name", form);
    file?.addEventListener("change", () => { fileName.textContent = file.files.length ? file.files[0].name : ""; });
    form.addEventListener("submit", e => {
      e.preventDefault();
      let ok = true;
      $$("[required]", form).forEach(inp => {
        const field = inp.closest(".field");
        const valid = inp.value.trim() !== "" && (inp.type !== "email" || /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inp.value));
        field.classList.toggle("has-error", !valid);
        if (!valid) ok = false;
      });
      if (!ok) { $(".has-error input, .has-error textarea", form)?.focus(); return; }
      form.classList.add("is-sent");
      form.reset();
      if (fileName) fileName.textContent = "";
    });
    $$("input, textarea", form).forEach(inp => inp.addEventListener("input", () => inp.closest(".field")?.classList.remove("has-error")));
  }
})();
