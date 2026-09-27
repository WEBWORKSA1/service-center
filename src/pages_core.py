"""Core pages: home, find, categories, get-quote (lead-gen), costs, brands, faq."""

TESTIMONIALS = [
    ("The cost estimator told me my dryer fix should be ~$180. First quote said $420 — I walked. Second shop did it for $165.", "Priya R.", "Toronto"),
    ("Three quotes for a MacBook screen in under an hour. Picked the authorized shop and saved $110.", "Marcus D.", "Austin"),
    ("Followed the flame-sensor guide before calling anyone. Ten minutes, zero dollars, furnace works.", "Elena K.", "Chicago"),
]

BRANDS = [
    ("Phones & Tablets", [("Apple Support", "https://support.apple.com/repair"), ("Samsung Support", "https://www.samsung.com/us/support/"), ("Google Pixel Support", "https://support.google.com/pixelphone"), ("OnePlus Support", "https://www.oneplus.com/support"), ("Motorola Support", "https://www.motorola.com/us/support")]),
    ("Computers", [("Dell Support", "https://www.dell.com/support"), ("HP Support", "https://support.hp.com"), ("Lenovo Support", "https://support.lenovo.com"), ("ASUS Support", "https://www.asus.com/support/"), ("Acer Support", "https://www.acer.com/support"), ("Microsoft Surface", "https://support.microsoft.com/surface")]),
    ("TVs, Consoles & Electronics", [("Sony Support", "https://www.sony.com/electronics/support"), ("LG Support", "https://www.lg.com/us/support"), ("PlayStation Support", "https://www.playstation.com/support/"), ("Xbox Support", "https://support.xbox.com"), ("Nintendo Support", "https://support.nintendo.com"), ("Canon Support", "https://www.usa.canon.com/support")]),
    ("Appliances", [("Whirlpool Service", "https://www.whirlpool.com/services.html"), ("GE Appliances Service", "https://www.geappliances.com/ge/service-and-support/"), ("Bosch Home Service", "https://www.bosch-home.com/us/service"), ("LG Appliances", "https://www.lg.com/us/support"), ("Samsung Appliances", "https://www.samsung.com/us/support/"), ("Dyson Support", "https://www.dyson.com/support")]),
    ("Auto", [("Toyota Owners", "https://www.toyota.com/owners/"), ("Honda Owners", "https://owners.honda.com"), ("Ford Support", "https://www.ford.com/support/"), ("Tesla Service", "https://www.tesla.com/service"), ("Hyundai Owners", "https://owners.hyundaiusa.com"), ("BMW Service", "https://www.bmwusa.com/service.html")]),
    ("Home Systems", [("Carrier Support", "https://www.carrier.com/residential/en/us/support/"), ("Trane Support", "https://www.trane.com/residential/en/support/"), ("Rheem Support", "https://www.rheem.com/support/"), ("Lennox Support", "https://www.lennox.com/support"), ("Kohler Support", "https://www.kohler.com/en/support")]),
]

def pages(k):
    L, ad, band, crumbs, rel, CATS, CAT = k["layout"], k["ad"], k["cta_band"], k["crumbs"], k["rel"], k["CATEGORIES"], k["CAT"]
    out = []

    # ---------------- HOME ----------------
    r = rel(0)
    cat_tiles = "".join(f'<a class="card cat-tile" href="{r}categories/{s}/"><div class="icon">{i}</div><b>{n}</b><span>{d}</span></a>' for s, i, n, d in CATS)
    cat_opts = "".join(f'<option value="{s}">{n}</option>' for s, i, n, d in CATS)
    testis = "".join(f'<div class="card"><p class="quote">“{q}”</p><div class="quote-who"><i>{w[0]}</i>{w} · {c}</div></div>' for q, w, c in TESTIMONIALS)
    home = f"""
<section class="hero"><div class="container">
  <span class="chip">🔧 Phones · Computers · Electronics · Appliances · Auto · Home</span>
  <h1 class="mt-2">Find a trusted <span>service center</span>.<br>Know the fair price first.</h1>
  <p class="lead">Compare vetted repair shops near you, estimate what the fix should cost, and get up to 3 free quotes — or fix it yourself with our step-by-step guides.</p>
  <form class="searchbar" action="{r}find/" method="get" role="search">
    <select name="cat" aria-label="Category"><option value="">What needs fixing?</option>{cat_opts}</select>
    <input name="q" placeholder="Brand, device or problem (e.g. Samsung fridge)" aria-label="Search">
    <button class="btn btn-accent" type="submit">Search</button>
  </form>
  <div class="hero-chips"><a class="chip" href="{r}get-quote/?cat=phones">📱 Cracked screen</a><a class="chip" href="{r}get-quote/?cat=appliances">🧺 Washer won't spin</a><a class="chip" href="{r}get-quote/?cat=auto">🚗 Check-engine light</a><a class="chip" href="{r}get-quote/?cat=home">❄️ AC not cooling</a><a class="chip" href="{r}costs/">💲 What should it cost?</a></div>
  <div class="hero-stats"><div><b>6</b>service categories</div><div><b>30+</b>repair cost benchmarks</div><div><b>3</b>free quotes per request</div><div><b>$0</b>for consumers, always</div></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Browse</span><h2>What needs service today?</h2></div><a class="btn btn-outline" href="{r}find/">Open the directory →</a></div>
  <div class="grid grid-6">{cat_tiles}</div>
</div></section>

<section class="section tight" style="background:var(--surface)"><div class="container">
  <div class="grid grid-3 steps">
    <div class="step"><h3>Describe the problem</h3><p class="muted">Pick a category, tell us what's wrong and where you are. Takes 60 seconds. No account needed.</p></div>
    <div class="step"><h3>Compare up to 3 quotes</h3><p class="muted">Vetted local centers respond with pricing and turnaround. Our benchmarks show you if a quote is fair.</p></div>
    <div class="step"><h3>Book — or DIY</h3><p class="muted">Choose the best offer, or follow our guide and video and fix it yourself for the price of a part.</p></div>
  </div>
  <div class="trust-row mt-3"><span>Free for consumers</span><span>No spam — your details go only to the centers you choose</span><span>Independent: not owned by any brand or repair chain</span><span>Fair-price benchmarks on every request</span></div>
</div></section>

<section class="section"><div class="container">
  <div class="layout-side">
    <div>
      <div class="section-head"><div><span class="eyebrow">Get quotes</span><h2>Get up to 3 free quotes in minutes</h2></div></div>
      <div class="wizard">
        <div class="wizard-head"><h2>What do you need fixed?</h2><p>Free · No obligation · Local vetted centers only</p><div class="progress"><i></i></div></div>
        <div class="wizard-body">
          <form data-form="Quick Quote (Home)" data-success="Request received! Up to 3 vetted centers will contact you shortly. Check your email for a confirmation.">
            <input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
            <input type="hidden" name="category" required><input type="hidden" name="urgency" required>
            <div class="wstep active"><h3>1 · Category</h3><div class="option-grid" data-field="category">{''.join(f'<div class="option" data-value="{s}"><span class="ic">{i}</span>{n}</div>' for s, i, n, d in CATS)}</div></div>
            <div class="wstep"><h3>2 · How urgent?</h3><div class="option-grid" data-field="urgency"><div class="option" data-value="Emergency (today)"><span class="ic">🚨</span>Today</div><div class="option" data-value="This week"><span class="ic">📅</span>This week</div><div class="option" data-value="Just researching"><span class="ic">🔍</span>Just researching</div></div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button></div></div>
            <div class="wstep"><h3>3 · Tell us more</h3><div class="form"><div><label>What's the problem?</label><textarea name="problem" required placeholder="e.g. Samsung fridge not cooling, freezer works. Model RF28…"></textarea></div><div class="row"><div><label>ZIP / postal code or city</label><input name="location" required placeholder="10001 or Montréal"></div><div><label>Brand / model (optional)</label><input name="brand"></div></div></div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
            <div class="wstep"><h3>4 · Where should quotes go?</h3><div class="form"><div class="row"><div><label>Name</label><input name="name" required></div><div><label>Phone</label><input name="phone" type="tel" required></div></div><div><label>Email</label><input name="email" type="email" required></div><label class="consent"><input type="checkbox" name="consent" required> I agree to be contacted by up to 3 service centers about this request and accept the <a href="{r}privacy/">privacy policy</a>.</label><button class="btn btn-accent btn-lg btn-block" type="submit">Get My Free Quotes →</button><div class="form-status"></div></div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button></div></div>
          </form>
          <div class="wizard-done" style="display:none"><h3>✅ You're all set</h3><p>While you wait, check the <a href="{r}costs/">fair-price estimator</a> so you know a good quote when you see one.</p></div>
        </div>
      </div>
    </div>
    <aside>
      {ad("sidebar", "sticky-side")}
    </aside>
  </div>
</div></section>

<section class="section" style="background:var(--surface)"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Know before you go</span><h2>What should the repair cost?</h2><p>Real-world price ranges for 30+ common jobs, with a DIY difficulty call on each.</p></div><a class="btn btn-primary" href="{r}costs/">Open the estimator →</a></div>
  <div class="grid grid-4">
    <div class="card"><div class="icon">📱</div><h3>Phone screen</h3><p class="price-range" style="font-size:1.4rem">$80 – $350</p><p class="muted small">Flagships top the range; aftermarket panels save 30–50%.</p></div>
    <div class="card"><div class="icon">🧊</div><h3>Fridge not cooling</h3><p class="price-range" style="font-size:1.4rem">$200 – $650</p><p class="muted small">Fans and thermostats cheap; sealed-system work expensive.</p></div>
    <div class="card"><div class="icon">🛑</div><h3>Brakes (per axle)</h3><p class="price-range" style="font-size:1.4rem">$180 – $500</p><p class="muted small">Pads + rotors. Luxury vehicles run higher.</p></div>
    <div class="card"><div class="icon">❄️</div><h3>AC repair</h3><p class="price-range" style="font-size:1.4rem">$150 – $1,500</p><p class="muted small">A capacitor is $150; a compressor is $1,500+.</p></div>
  </div>
</div></section>

{ad("inArticle")}

<section class="section"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Fix it yourself</span><h2>Popular repair guides</h2></div><a class="btn btn-outline" href="{r}guides/">All guides →</a></div>
  <div class="grid grid-3">
    <a class="card" href="{r}guides/dryer-not-heating/"><span class="badge brand">Appliances</span><h3>Dryer runs but no heat: the 3 parts to check</h3><p class="muted small">Thermal fuse, heating element, cycling thermostat — in that order.</p></a>
    <a class="card" href="{r}guides/phone-screen-repair-vs-replace/"><span class="badge brand">Phones</span><h3>Cracked screen: repair, replace or trade in?</h3><p class="muted small">A decision table by device age and repair quote.</p></a>
    <a class="card" href="{r}guides/check-engine-light/"><span class="badge brand">Auto</span><h3>Check-engine light on? Read the code before you pay</h3><p class="muted small">$20 OBD-II reader, the 6 most common codes and what they cost.</p></a>
  </div>
</div></section>

<section class="section" style="background:var(--surface)"><div class="container">
  <div class="section-head"><div><span class="eyebrow">Results</span><h2>What people say</h2></div></div>
  <div class="grid grid-3">{testis}</div>
  <p class="small muted mt-2">Testimonials are illustrative examples of the outcomes the platform is designed for; replace with verified user reviews as they arrive.</p>
</div></section>

<section class="section"><div class="container">
  <div class="grid grid-3">
    <div class="card"><div class="icon">🏪</div><h3>Own a service center?</h3><p class="muted">Claim your listing, receive qualified local leads and get featured placement.</p><a class="btn btn-primary btn-sm" href="{r}partners/">List your business →</a></div>
    <div class="card accent"><div class="icon">📣</div><h3>Advertise or sponsor</h3><p class="muted">Reach high-intent repair buyers at the exact moment they're deciding.</p><a class="btn btn-accent btn-sm" href="{r}advertise/">See rate card →</a></div>
    <div class="card"><div class="icon">♥</div><h3>Support independent guides</h3><p class="muted">We keep guides free and ad-light. Chip in to fund testing, tools and writers.</p><a class="btn btn-outline btn-sm" href="{r}support/">Support us →</a></div>
  </div>
</div></section>

<section class="section tight"><div class="container">
  <div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap">
    <div><h3 style="margin:0">Get the fair-price newsletter</h3><p class="muted small" style="margin:0">One email a week: new cost benchmarks, guides and contests. No spam.</p></div>
    <form class="newsletter" data-form="Newsletter" data-success="Subscribed — welcome!"><input type="text" name="_honey" class="honeypot" tabindex="-1"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><button class="btn btn-primary">Subscribe</button><div class="form-status"></div></form>
  </div>
</div></section>
"""
    out.append(dict(path="index.html", html=L("index.html", "Find Trusted Repair & Service Centers, Fair Prices & Free Quotes", "Compare vetted repair and service centers for phones, computers, electronics, appliances, cars and homes. Estimate fair repair costs, get up to 3 free quotes, or fix it yourself with step-by-step guides.", home, 0)))

    # ---------------- FIND (directory) ----------------
    r = rel(1)
    find = f"""
{crumbs(r, [("", "Find a service center")])}
<section class="section tight"><div class="container">
  <span class="eyebrow">Directory</span><h1>Find a service center near you</h1>
  <p class="muted" style="max-width:720px">Filter by category, city, brand or service. Featured partners appear first. Can't find a match? <a href="{r}get-quote/">Post a request</a> and vetted centers come to you.</p>
  <div id="directory">
    <div class="filters">
      <input id="f-q" placeholder="Search brand, service or shop name" aria-label="Search">
      <select id="f-cat" aria-label="Category"><option value="">All categories</option>{''.join(f'<option value="{s}">{n}</option>' for s, i, n, d in CATS)}</select>
      <select id="f-city" aria-label="City"><option value="">All cities</option></select>
      <select id="f-sort" aria-label="Sort"><option value="rating">Top rated</option><option value="reviews">Most reviewed</option></select>
    </div>
    <div class="flex between mb-2"><b id="dir-count">Loading…</b><a class="small" href="{r}partners/">+ Add your service center</a></div>
    <div class="layout-side">
      <div id="dir-list" class="grid" style="grid-template-columns:1fr"></div>
      <aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Official brand support</h3><p class="muted small">Under warranty? Start with the manufacturer's own authorized-service locator.</p><a class="btn btn-outline btn-sm" href="{r}brands/">Brand support links →</a></div></aside>
    </div>
  </div>
</div></section>
{band(r)}
"""
    out.append(dict(path="find/index.html", html=L("find/index.html", "Service Center Directory — Find Repair Shops Near You", "Search and compare authorized and independent repair & service centers by category, city, brand and rating.", find, 1)))

    # ---------------- CATEGORY PAGES ----------------
    CAT_COPY = {
        "phones": ("Phone & tablet repair", "Cracked screens, dying batteries, charging ports and water damage — compare authorized and independent phone repair centers, check what it should cost, and decide whether to repair, replace or trade in.", ["Screen replacement", "Battery replacement", "Charging port", "Water damage", "Back glass", "Camera"], ["phone-screen-repair-vs-replace"]),
        "computers": ("Computer & laptop repair", "Laptop screens, SSD upgrades, data recovery, malware removal and keyboards. Find certified repair centers or follow our upgrade guides.", ["Laptop screen", "SSD upgrade", "Data recovery", "Virus removal", "Keyboard", "Battery"], ["laptop-slow-fix-or-replace"]),
        "electronics": ("TV, console & electronics repair", "TVs with no backlight, consoles with dead HDMI ports, speakers, cameras and drones. Know when repair beats replacement.", ["TV repair", "Game console", "Audio & speakers", "Camera & lens", "Drone", "Smart home"], ["tv-repair-or-replace"]),
        "appliances": ("Home appliance repair", "Refrigerators, washers, dryers, dishwashers, ovens and microwaves. Get fair-price quotes from local appliance technicians — or fix the common stuff yourself.", ["Refrigerator", "Washer", "Dryer", "Dishwasher", "Oven & range", "Microwave"], ["dryer-not-heating", "fridge-not-cooling"]),
        "auto": ("Auto repair & vehicle service", "Brakes, diagnostics, AC, batteries, tires and scheduled maintenance. Compare dealer service centers and independent garages with transparent price benchmarks.", ["Brakes", "Check-engine diagnostics", "Oil change", "AC service", "Battery", "Tires & alignment"], ["check-engine-light"]),
        "home": ("HVAC, plumbing & electrical", "Furnaces, air conditioners, water heaters, leaks, drains and wiring. Emergency and scheduled service from licensed local pros.", ["AC repair", "Furnace repair", "Water heater", "Plumbing & drains", "Electrical", "Garage door"], ["furnace-not-igniting"]),
    }
    for s, i, n, d in CATS:
        r = rel(2)
        h, intro, jobs, guides = CAT_COPY[s]
        job_chips = "".join(f'<a class="chip" style="background:var(--surface-2);color:var(--ink);border-color:var(--line)" href="{r}get-quote/?cat={s}">{j}</a>' for j in jobs)
        guide_cards = "".join(f'<a class="card" href="{r}guides/{g}/"><span class="badge brand">Guide</span><h3>{g.replace("-", " ").capitalize()}</h3></a>' for g in guides)
        body = f"""
{crumbs(r, [("categories/", "Categories"), ("", n)])}
<section class="hero" style="padding:48px 0"><div class="container"><span class="chip">{i} {n}</span><h1 class="mt-2">{h}</h1><p class="lead">{intro}</p>
<div class="flex mt-2"><a class="btn btn-accent btn-lg" href="{r}get-quote/?cat={s}">Get 3 free quotes</a><a class="btn btn-light btn-lg" href="{r}find/?cat={s}">Browse centers</a><a class="btn btn-outline btn-lg" style="color:#fff;border-color:#3b4b7a" href="{r}costs/?cat={s}">Cost estimator</a></div>
<div class="hero-chips">{job_chips}</div></div></section>
<section class="section"><div class="container"><div class="layout-side"><div>
  <h2>Common {n.lower()} jobs &amp; what they cost</h2>
  <div id="estimator" class="estimate-box"><div class="form"><div class="row"><div><label>Category</label><select id="e-cat">{''.join(f'<option value="{s2}"{" selected" if s2 == s else ""}>{n2}</option>' for s2, _, n2, _ in CATS)}</select></div><div><label>Job</label><select id="e-job"></select></div></div><div><label>Cost of living in your area</label><select id="e-region"><option value="avg">Average</option><option value="low">Lower-cost region</option><option value="high">Major metro / high-cost</option></select></div></div><div id="e-out" class="mt-3"></div></div>
  {ad("inArticle")}
  <h2 class="mt-4">Repair or replace?</h2>
  <p>Rule of thumb used across the industry: if the repair quote exceeds <b>50% of the replacement cost</b> and the item is past half its expected lifespan, replacement usually wins. Under warranty? Always start with the <a href="{r}brands/">manufacturer's authorized service</a> — unauthorized repairs can void coverage.</p>
  <h2 class="mt-4">Guides for {n.lower()}</h2><div class="grid grid-2">{guide_cards}<a class="card" href="{r}guides/"><span class="badge">Library</span><h3>All repair guides →</h3></a></div>
  <h2 class="mt-4">Videos</h2><div data-yt="{s}" class="grid grid-2"><div class="card"><p class="muted">Curated {n.lower()} videos appear here once the channel is connected in <code>config.js</code>. Meanwhile, browse the <a href="{r}videos/">video library</a>.</p></div></div>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>
{band(r, f"Get {n.lower()} quotes now", "Free, fast and no obligation. Up to 3 vetted local centers.", "Get Free Quotes", f"get-quote/?cat={s}")}
"""
        out.append(dict(path=f"categories/{s}/index.html", html=L(f"categories/{s}/index.html", f"{h} — Find Centers, Costs & Free Quotes", intro, body, 2)))

    r = rel(1)
    cats_index = f"""{crumbs(r, [("", "Categories")])}<section class="section tight"><div class="container"><h1>All service categories</h1><div class="grid grid-3 mt-3">{''.join(f'<a class="card cat-tile" href="{r}categories/{s}/"><div class="icon">{i}</div><b>{n}</b><span>{d}</span></a>' for s, i, n, d in CATS)}</div></div></section>{band(r)}"""
    out.append(dict(path="categories/index.html", html=L("categories/index.html", "Service Categories", "Browse every repair and service category on Service.Center.", cats_index, 1)))

    # ---------------- GET QUOTE (dedicated lead-gen) ----------------
    r = rel(1)
    quote = f"""
<section class="hero" style="padding:44px 0 30px"><div class="container center"><span class="chip">⚡ Average first response: under 2 hours</span><h1 class="mt-2">Get up to 3 free repair quotes</h1><p class="lead" style="margin:0 auto">One request. Vetted local service centers compete. You compare with our fair-price benchmark and choose — or walk away. Always free.</p></div></section>
<section class="section"><div class="container"><div class="layout-side"><div>
  <div class="wizard">
    <div class="wizard-head"><h2>Describe your repair</h2><p>Takes about 60 seconds</p><div class="progress"><i></i></div></div>
    <div class="wizard-body">
      <form data-form="Lead — Get Quote" data-success="Request received! Up to 3 vetted centers will contact you shortly.">
        <input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">
        <input type="hidden" name="category" required><input type="hidden" name="urgency" required><input type="hidden" name="service_type" required>
        <div class="wstep active"><h3>1 · What needs service?</h3><div class="option-grid" data-field="category">{''.join(f'<div class="option" data-value="{s}"><span class="ic">{i}</span>{n}</div>' for s, i, n, d in CATS)}</div></div>
        <div class="wstep"><h3>2 · What kind of help?</h3><div class="option-grid" data-field="service_type"><div class="option" data-value="Repair"><span class="ic">🔧</span>Repair</div><div class="option" data-value="Diagnosis / inspection"><span class="ic">🔍</span>Diagnose</div><div class="option" data-value="Maintenance"><span class="ic">🗓</span>Maintenance</div><div class="option" data-value="Installation"><span class="ic">📦</span>Install</div><div class="option" data-value="Upgrade"><span class="ic">⬆️</span>Upgrade</div><div class="option" data-value="Not sure"><span class="ic">🤷</span>Not sure</div></div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button></div></div>
        <div class="wstep"><h3>3 · How urgent?</h3><div class="option-grid" data-field="urgency"><div class="option" data-value="Emergency (today)"><span class="ic">🚨</span>Today</div><div class="option" data-value="Within 3 days"><span class="ic">⏱</span>Within 3 days</div><div class="option" data-value="This week"><span class="ic">📅</span>This week</div><div class="option" data-value="Flexible"><span class="ic">🧘</span>Flexible</div><div class="option" data-value="Just researching"><span class="ic">🔍</span>Just researching</div></div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button></div></div>
        <div class="wstep"><h3>4 · Details</h3><div class="form">
          <div><label>Describe the problem</label><textarea name="problem" required placeholder="What's happening, since when, any error codes, sounds or smells?"></textarea><div class="hint">More detail = more accurate quotes.</div></div>
          <div class="row"><div><label>Brand &amp; model</label><input name="brand" placeholder="e.g. LG WM3900 / 2019 Honda Civic"></div><div><label>Age of item</label><select name="age"><option>Under 1 year (may be under warranty)</option><option>1–3 years</option><option>3–7 years</option><option>7+ years</option><option>Unknown</option></select></div></div>
          <div class="row"><div><label>ZIP / postal code or city</label><input name="location" required></div><div><label>Preferred service</label><select name="mode"><option>Drop-off at center</option><option>On-site / at home</option><option>Mail-in</option><option>Remote (if possible)</option><option>No preference</option></select></div></div>
          <div><label>Budget range (optional)</label><select name="budget"><option value="">Not sure</option><option>Under $100</option><option>$100–$250</option><option>$250–$500</option><option>$500–$1,000</option><option>$1,000+</option></select></div>
          <div><label>Photo or video link (optional)</label><input name="media" placeholder="Paste a Drive/Dropbox/Imgur link"></div>
        </div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
        <div class="wstep"><h3>5 · Where should quotes go?</h3><div class="form">
          <div class="row"><div><label>Full name</label><input name="name" required></div><div><label>Phone</label><input name="phone" type="tel" required></div></div>
          <div><label>Email</label><input name="email" type="email" required></div>
          <div><label>Best time to reach you</label><select name="reach"><option>Anytime</option><option>Morning</option><option>Afternoon</option><option>Evening</option><option>Text / email only</option></select></div>
          <label class="consent"><input type="checkbox" name="consent" required> I agree to be contacted by up to 3 service centers about this request and accept the <a href="{r}privacy/">privacy policy</a> and <a href="{r}terms/">terms</a>.</label>
          <button class="btn btn-accent btn-lg btn-block" type="submit">Get My Free Quotes →</button><div class="form-status"></div>
        </div><div class="wizard-nav"><button type="button" class="btn btn-outline" data-prev>← Back</button></div></div>
      </form>
      <div class="wizard-done" style="display:none"><h3>✅ Request received</h3><p>Next: check the <a href="{r}costs/">fair-price estimator</a> so you'll know a good quote when you see one, and read <a href="{r}guides/how-to-compare-repair-quotes/">how to compare repair quotes</a>.</p></div>
      <div class="trust-row"><span>100% free</span><span>No obligation</span><span>Only vetted centers</span><span>Your data never sold</span></div>
    </div>
  </div>
  <div class="grid grid-3 mt-4">
    <div class="card"><div class="icon">🛡</div><h3>Vetted only</h3><p class="muted small">Business verification, review screening and complaint monitoring before any center receives a lead.</p></div>
    <div class="card"><div class="icon">💲</div><h3>Fair-price check</h3><p class="muted small">Every request comes with our benchmark range so you can spot an inflated quote instantly.</p></div>
    <div class="card"><div class="icon">🔒</div><h3>Privacy first</h3><p class="muted small">Your details go only to the centers matched to your request. Never sold to lists.</p></div>
  </div>
  <h2 class="mt-4">Frequently asked</h2>
  <details><summary>Is this really free?</summary><p>Yes — consumers never pay. Service centers pay a small fee for qualified leads or a monthly featured-listing subscription, which funds the platform.</p></details>
  <details><summary>How many centers will contact me?</summary><p>At most three. You can stop at any time by replying "stop" to any message.</p></details>
  <details><summary>Do I have to accept a quote?</summary><p>No. Compare, negotiate or walk away. Many people use the quotes purely to check a dealer's price.</p></details>
  <details><summary>What if nobody in my area is listed yet?</summary><p>We manually source and vet a center for you, usually within a business day, and add them to the directory.</p></details>
</div><aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Are you a service center?</h3><p class="muted small">Receive these requests directly.</p><a class="btn btn-primary btn-sm" href="{r}partners/">Join the network →</a></div></aside></div></div></section>
"""
    out.append(dict(path="get-quote/index.html", html=L("get-quote/index.html", "Get Free Repair Quotes from Vetted Service Centers", "Describe your repair once and receive up to 3 free quotes from vetted local service centers. Free, fast, no obligation.", quote, 1)))

    # ---------------- COSTS ----------------
    r = rel(1)
    costs = f"""
{crumbs(r, [("", "Cost estimator")])}
<section class="section tight"><div class="container"><div class="layout-side"><div>
  <span class="eyebrow">Fair-price benchmarks</span><h1>Repair cost estimator</h1>
  <p class="muted" style="max-width:700px">Typical price ranges for 30+ common repairs across six categories, adjusted for your region, with a DIY-difficulty call on each. Ranges reflect widely reported market rates; treat them as a sanity check, not a quote.</p>
  <div id="estimator" class="estimate-box mt-3"><div class="form"><div class="row"><div><label>Category</label><select id="e-cat">{''.join(f'<option value="{s}">{n}</option>' for s, i, n, d in CATS)}</select></div><div><label>Job</label><select id="e-job"></select></div></div><div><label>Cost of living in your area</label><select id="e-region"><option value="avg">Average</option><option value="low">Lower-cost region (−18%)</option><option value="high">Major metro / high-cost (+28%)</option></select></div></div><div id="e-out" class="mt-3"></div></div>
  {ad("inArticle")}
  <h2 class="mt-4">How to use a benchmark</h2>
  <ol><li><b>Ask for an itemized quote</b> — parts, labour hours, diagnostic fee, taxes.</li><li><b>Ask if the diagnostic fee is credited</b> toward the repair (most reputable centers do this).</li><li><b>Compare against the typical figure above</b>; more than ~25% over deserves a second quote.</li><li><b>Check the warranty</b> on parts and labour — 90 days is the floor, 1 year is good.</li></ol>
  <p><a class="btn btn-accent" href="{r}get-quote/">Get 3 quotes to compare →</a></p>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>
"""
    out.append(dict(path="costs/index.html", html=L("costs/index.html", "Repair Cost Estimator — What Should It Cost?", "Instant fair-price ranges for 30+ phone, computer, electronics, appliance, auto and home repairs, adjusted for your region.", costs, 1)))

    # ---------------- BRANDS ----------------
    r = rel(1)
    def brand_list(items):
        return "".join('<li><a href="%s" rel="noopener nofollow" target="_blank">%s</a></li>' % (u, n) for n, u in items)
    brand_blocks = "".join('<div class="card"><h3>%s</h3><ul style="padding-left:1.1em">%s</ul></div>' % (g, brand_list(items)) for g, items in BRANDS)
    brands = f"""
{crumbs(r, [("", "Brand support links")])}
<section class="section tight"><div class="container"><span class="eyebrow">Under warranty?</span><h1>Official brand support &amp; authorized service locators</h1><p class="muted" style="max-width:760px">If your device or vehicle is still under warranty, start with the manufacturer's own authorized-service channel. These links go to each brand's official support site. Service.Center is not affiliated with any of them.</p>
<div class="grid grid-3 mt-3">{brand_blocks}</div>
<div class="callout mt-3"><b>Out of warranty?</b> Independent centers are typically 20–40% cheaper for the same job. <a href="{r}get-quote/">Get 3 quotes</a> and compare.</div>
</div></section>{ad("inArticle")}{band(r)}
"""
    out.append(dict(path="brands/index.html", html=L("brands/index.html", "Official Brand Support & Authorized Service Locators", "Direct links to official manufacturer support and authorized service locators for phones, computers, electronics, appliances, vehicles and home systems.", brands, 1)))

    # ---------------- FAQ ----------------
    r = rel(1)
    faq_items = [
        ("What is Service.Center?", "An independent platform that helps you find and compare repair & service centers, estimate fair prices, get free quotes, and learn to fix things yourself."),
        ("Is Service.Center affiliated with any brand?", "No. We are not affiliated with, endorsed by, or an agent of any manufacturer, franchise or repair chain. Brand names appear for identification only."),
        ("How does the site make money?", "Service centers pay for qualified leads and featured listings; we run display ads on informational pages; some product links are affiliate links; readers can also donate. Consumers never pay."),
        ("How are service centers vetted?", "Business registration check, review screening across public platforms, complaint monitoring, and removal for repeated negative outcomes."),
        ("Are the cost estimates accurate?", "They are benchmark ranges compiled from public price data and industry reporting. Actual quotes depend on your model, region and the specific fault."),
        ("Can I list my business?", "Yes — basic listings are free; featured placement and lead packages are paid. See the Partners page."),
        ("How do I remove my data?", "Use the contact page and request deletion; we respond within 7 days."),
    ]
    faq = f"""{crumbs(r, [("", "FAQ")])}<section class="section tight"><div class="container"><h1>Frequently asked questions</h1><div class="mt-3" style="max-width:820px">{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq_items)}</div></div></section>{band(r)}"""
    faq_ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_items]}) + "</script>"
    out.append(dict(path="faq/index.html", html=L("faq/index.html", "FAQ", "Answers about how Service.Center works, vetting, pricing accuracy and privacy.", faq, 1, extra_head=faq_ld)))
    return out
