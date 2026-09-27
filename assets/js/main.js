/* ============================================================
   Service.Center — site runtime
   ============================================================ */
(function () {
  "use strict";
  const C = window.SC_CONFIG || {};
  const ROOT = document.body.dataset.root || "./";
  const $ = (s, el) => (el || document).querySelector(s);
  const $$ = (s, el) => Array.from((el || document).querySelectorAll(s));

  /* ---------- contact address (decoded only on demand) ---------- */
  function contactAddr() {
    try { return atob(C.contactKey || ""); } catch (e) { return ""; }
  }
  function mailto(subject, body) {
    const a = contactAddr();
    let u = "mailto:" + a;
    const q = [];
    if (subject) q.push("subject=" + encodeURIComponent(subject));
    if (body) q.push("body=" + encodeURIComponent(body));
    return q.length ? u + "?" + q.join("&") : u;
  }
  // Any element with data-contact="Subject" becomes a live contact link on click
  $$("[data-contact]").forEach(el => {
    el.setAttribute("href", "#contact");
    el.addEventListener("click", e => {
      e.preventDefault();
      window.location.href = mailto(el.dataset.contact || "Service.Center inquiry");
    });
  });

  /* ---------- nav / theme ---------- */
  const toggle = $(".nav-toggle"), links = $(".nav-links");
  if (toggle && links) toggle.addEventListener("click", () => links.classList.toggle("open"));
  const themeBtn = $(".theme-toggle");
  const savedTheme = safeGet("sc-theme");
  if (savedTheme) document.documentElement.dataset.theme = savedTheme;
  if (themeBtn) themeBtn.addEventListener("click", () => {
    const cur = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = cur; safeSet("sc-theme", cur);
  });
  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  /* ---------- toast ---------- */
  const toast = document.createElement("div"); toast.className = "toast"; document.body.appendChild(toast);
  function say(msg, ms) { toast.textContent = msg; toast.classList.add("show"); setTimeout(() => toast.classList.remove("show"), ms || 2600); }

  /* ---------- ads ---------- */
  if (C.adsenseClient) {
    const s = document.createElement("script");
    s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
    document.head.appendChild(s);
    $$(".ad-slot").forEach(slot => {
      const key = slot.dataset.slot || "inArticle";
      const id = (C.adSlots || {})[key];
      if (!id) return;
      slot.classList.add("live"); slot.innerHTML = "";
      const ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.setAttribute("data-ad-client", C.adsenseClient);
      ins.setAttribute("data-ad-slot", id);
      ins.setAttribute("data-ad-format", slot.dataset.format || "auto");
      ins.setAttribute("data-full-width-responsive", "true");
      slot.appendChild(ins);
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  } else {
    $$(".ad-slot").forEach(slot => { if (!slot.textContent.trim()) slot.textContent = "Advertisement"; });
  }

  /* ---------- analytics ---------- */
  if (C.ga4) {
    const g = document.createElement("script"); g.async = true;
    g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; function gtag() { dataLayer.push(arguments); }
    gtag("js", new Date()); gtag("config", C.ga4);
  }
  if (C.plausibleDomain) {
    const p = document.createElement("script"); p.defer = true; p.dataset.domain = C.plausibleDomain;
    p.src = "https://plausible.io/js/script.js"; document.head.appendChild(p);
  }

  /* ---------- forms ---------- */
  function endpoint() {
    if (C.formEndpoint) return C.formEndpoint;
    return "https://formsubmit.co/ajax/" + contactAddr();
  }
  $$("form[data-form]").forEach(form => {
    form.addEventListener("submit", async e => {
      e.preventDefault();
      const status = $(".form-status", form) || form.appendChild(Object.assign(document.createElement("div"), { className: "form-status" }));
      const hp = $("input[name=_honey]", form); if (hp && hp.value) return;
      const btn = $("button[type=submit]", form); const label = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      const data = Object.fromEntries(new FormData(form).entries());
      data._subject = "[Service.Center] " + (form.dataset.form || "Form") + (data.category ? " · " + data.category : "");
      data._template = "table"; data._captcha = "false";
      data.page = location.href; data.submitted_at = new Date().toISOString();
      try {
        const r = await fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) });
        if (!r.ok) throw new Error("relay " + r.status);
        status.className = "form-status ok";
        status.textContent = form.dataset.success || "Thanks! We received your request and will respond shortly.";
        form.reset(); form.dispatchEvent(new CustomEvent("sc:sent", { detail: data }));
        try { const log = JSON.parse(safeGet("sc-leads") || "[]"); log.push(data); safeSet("sc-leads", JSON.stringify(log.slice(-50))); } catch (e) {}
        if (C.formRedirect) location.href = C.formRedirect;
      } catch (err) {
        // Fallback: open the user's mail client with the form contents (address never rendered on page)
        status.className = "form-status err";
        status.innerHTML = "Our relay is busy. <a href='#' id='mf'>Click here to send via your email app</a> instead.";
        $("#mf", status).addEventListener("click", ev => {
          ev.preventDefault();
          const body = Object.entries(data).filter(([k]) => !k.startsWith("_")).map(([k, v]) => k + ": " + v).join("\n");
          location.href = mailto(data._subject, body);
        });
      } finally { if (btn) { btn.disabled = false; btn.textContent = label; } }
    });
  });

  /* ---------- lead wizard ---------- */
  const wiz = $(".wizard");
  if (wiz) {
    const steps = $$(".wstep", wiz); let i = 0; const bar = $(".progress i", wiz);
    const show = n => { steps.forEach((s, k) => s.classList.toggle("active", k === n)); i = n; if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%"; if (n > 0) wiz.scrollIntoView({ behavior: "smooth", block: "start" }); };
    $$(".option", wiz).forEach(o => o.addEventListener("click", () => {
      const grp = o.closest(".option-grid"); $$(".option", grp).forEach(x => x.classList.remove("selected")); o.classList.add("selected");
      const inp = $("input[name=" + grp.dataset.field + "]", wiz); if (inp) inp.value = o.dataset.value || o.textContent.trim();
      if (grp.dataset.auto !== "false") setTimeout(() => next(), 180);
    }));
    function valid(n) {
      const s = steps[n]; let ok = true;
      $$("[required]", s).forEach(f => { if (!f.value) { ok = false; f.classList.add("invalid"); f.focus(); } });
      return ok;
    }
    function next() { if (!valid(i)) return say("Please pick an option to continue"); if (i < steps.length - 1) show(i + 1); }
    $$("[data-next]", wiz).forEach(b => b.addEventListener("click", next));
    $$("[data-prev]", wiz).forEach(b => b.addEventListener("click", () => i > 0 && show(i - 1)));
    const pre = new URLSearchParams(location.search).get("cat");
    if (pre) { const o = $(".option[data-value='" + pre + "']", wiz); if (o) { o.click(); } }
    $("form", wiz) && $("form", wiz).addEventListener("sc:sent", () => { const done = $(".wizard-done", wiz); if (done) { steps.forEach(s => s.classList.remove("active")); done.style.display = "block"; if (bar) bar.style.width = "100%"; } });
    show(0);
  }

  /* ---------- directory ---------- */
  const dir = $("#directory");
  if (dir) {
    fetch(ROOT + "data/centers.json").then(r => r.json()).then(data => {
      const list = $("#dir-list"), q = $("#f-q"), cat = $("#f-cat"), city = $("#f-city"), sort = $("#f-sort"), count = $("#dir-count");
      const params = new URLSearchParams(location.search);
      if (params.get("cat") && cat) cat.value = params.get("cat");
      if (params.get("q") && q) q.value = params.get("q");
      if (params.get("city") && city) city.value = params.get("city");
      const cities = [...new Set(data.map(d => d.city))].sort();
      cities.forEach(c => { const o = document.createElement("option"); o.value = c; o.textContent = c; city.appendChild(o); });
      function render() {
        let rows = data.filter(d => (!cat.value || d.category === cat.value) && (!city.value || d.city === city.value) &&
          (!q.value || (d.name + " " + d.brands.join(" ") + " " + d.services.join(" ") + " " + d.city).toLowerCase().includes(q.value.toLowerCase())));
        if (sort.value === "rating") rows.sort((a, b) => b.rating - a.rating);
        if (sort.value === "reviews") rows.sort((a, b) => b.reviews - a.reviews);
        rows.sort((a, b) => (b.featured ? 1 : 0) - (a.featured ? 1 : 0));
        count.textContent = rows.length + " service center" + (rows.length === 1 ? "" : "s");
        list.innerHTML = rows.map(card).join("") || "<div class='card center'><p>No matches yet in this area. <a href='" + ROOT + "get-quote/'>Get free quotes</a> and we'll route your request to vetted partners.</p></div>";
      }
      function card(d) {
        const stars = "★".repeat(Math.round(d.rating)) + "☆".repeat(5 - Math.round(d.rating));
        return `<article class="card listing">
          <div class="avatar">${d.icon}</div>
          <div>
            <div class="title">${d.name} ${d.featured ? '<span class="badge accent">Featured</span>' : ''} ${d.demo ? '<span class="badge demo">Demo listing</span>' : ''} ${d.authorized ? '<span class="badge ok">Authorized</span>' : ''}</div>
            <div class="meta"><span class="stars">${stars}</span> <span>${d.rating.toFixed(1)} (${d.reviews} reviews)</span> <span>📍 ${d.city}</span> <span>⏱ ${d.turnaround}</span></div>
            <div class="mt-1 small">${d.services.join(" · ")}</div>
            <div class="mt-1">${d.brands.map(b => `<span class="badge">${b}</span>`).join(" ")}</div>
          </div>
          <div class="actions">
            <a class="btn btn-primary btn-sm" href="${ROOT}get-quote/?cat=${d.category}&ref=${encodeURIComponent(d.name)}">Get quote</a>
            <a class="btn btn-outline btn-sm" href="${ROOT}partners/?claim=${encodeURIComponent(d.name)}">Claim listing</a>
          </div></article>`;
      }
      [q, cat, city, sort].forEach(el => el.addEventListener("input", render));
      render();
    }).catch(() => { $("#dir-list").innerHTML = "<div class='card'>Directory data could not be loaded.</div>"; });
  }

  /* ---------- cost estimator ---------- */
  const est = $("#estimator");
  if (est) {
    fetch(ROOT + "data/costs.json").then(r => r.json()).then(costs => {
      const cat = $("#e-cat"), job = $("#e-job"), out = $("#e-out"), region = $("#e-region");
      const mult = { avg: 1, low: 0.82, high: 1.28 };
      function fillJobs() { job.innerHTML = costs.filter(c => c.category === cat.value).map(c => `<option value="${c.job}">${c.job}</option>`).join(""); calc(); }
      function calc() {
        const c = costs.find(x => x.category === cat.value && x.job === job.value); if (!c) return;
        const m = mult[region.value] || 1, lo = Math.round(c.low * m), hi = Math.round(c.high * m), typ = Math.round(c.typical * m);
        const pos = Math.min(95, Math.max(5, (typ - lo) / (hi - lo) * 100));
        out.innerHTML = `<div class="small muted">Estimated cost · ${c.job}</div>
          <div class="price-range">$${lo.toLocaleString()} – $${hi.toLocaleString()}</div>
          <div class="range-bar"><i style="left:${pos}%"></i></div>
          <div class="small">Typical: <b>$${typ.toLocaleString()}</b> · ${c.note}</div>
          <div class="callout blue mt-2"><b>DIY-able?</b> ${c.diy} </div>
          <a class="btn btn-accent mt-2" href="${ROOT}get-quote/?cat=${cat.value}">Get 3 free quotes for this job →</a>`;
      }
      const pre = new URLSearchParams(location.search).get("cat"); if (pre) cat.value = pre;
      cat.addEventListener("change", fillJobs); job.addEventListener("change", calc); region.addEventListener("change", calc);
      fillJobs();
    });
  }

  /* ---------- YouTube ---------- */
  const yt = C.youtube || {};
  $$("[data-yt]").forEach(box => {
    const key = box.dataset.yt; let ids = [];
    if (key === "featured") ids = yt.featured || [];
    else if (yt.byCategory && yt.byCategory[key]) ids = yt.byCategory[key];
    const list = Array.isArray(ids) ? ids : [];
    if (typeof ids === "string" && ids) { box.innerHTML = `<div class="video-wrap"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/videoseries?list=${ids}" allowfullscreen title="Playlist"></iframe></div>`; return; }
    if (!list.length && yt.channelId && key === "featured") { box.innerHTML = `<div class="video-wrap"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/videoseries?list=UU${yt.channelId.slice(2)}" allowfullscreen title="Channel uploads"></iframe></div>`; return; }
    if (!list.length) return; // keep the placeholder markup authored in the page
    box.innerHTML = list.map(id => `<div class="video-wrap"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/${id}" allowfullscreen title="Video"></iframe></div>`).join("");
  });

  /* ---------- support links ---------- */
  const sup = C.support || {};
  $$("[data-support]").forEach(a => { const u = sup[a.dataset.support]; if (u) { a.href = u; a.target = "_blank"; a.rel = "noopener"; } else { a.classList.add("btn-outline"); a.classList.remove("btn-primary", "btn-accent"); a.addEventListener("click", e => { e.preventDefault(); location.href = mailto("Support Service.Center — " + a.dataset.support); }); } });

  /* ---------- social ---------- */
  const soc = C.social || {};
  $$("[data-social]").forEach(a => { const u = soc[a.dataset.social]; if (u) a.href = u; else a.style.display = "none"; });

  /* ---------- countdown ---------- */
  $$("[data-countdown]").forEach(el => {
    const end = new Date(el.dataset.countdown).getTime();
    const tick = () => { const d = Math.max(0, end - Date.now()); const s = Math.floor(d / 1000);
      el.innerHTML = [["Days", Math.floor(s / 86400)], ["Hours", Math.floor(s % 86400 / 3600)], ["Min", Math.floor(s % 3600 / 60)], ["Sec", s % 60]].map(([l, v]) => `<div><b>${String(v).padStart(2, "0")}</b><span>${l}</span></div>`).join(""); };
    tick(); setInterval(tick, 1000);
  });

  /* ---------- share ---------- */
  $$("[data-share]").forEach(b => b.addEventListener("click", async () => {
    const d = { title: document.title, url: location.href };
    if (navigator.share) { try { await navigator.share(d); } catch (e) {} } else { try { await navigator.clipboard.writeText(d.url); say("Link copied"); } catch (e) {} }
  }));

  /* ---------- year ---------- */
  $$("[data-year]").forEach(el => el.textContent = new Date().getFullYear());

  /* ---------- affiliate tagging ---------- */
  const aff = C.affiliate || {};
  if (aff.amazonTag) $$("a[href*='amazon.']").forEach(a => { try { const u = new URL(a.href); u.searchParams.set("tag", aff.amazonTag); a.href = u.toString(); a.rel = "sponsored noopener"; } catch (e) {} });
})();
