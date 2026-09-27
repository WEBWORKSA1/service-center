"""Content pages: guides (articles), videos."""
import json

GUIDES = [
 dict(slug="dryer-not-heating", cat="appliances", title="Dryer runs but no heat: the 3 parts to check (in order)", minutes=6, cost="$15–$60 in parts",
  summary="Ninety percent of no-heat dryers come down to a thermal fuse, heating element or cycling thermostat. Here's how to test each with a $15 multimeter.",
  body="""
<h2>Before you start</h2><p>Unplug the dryer. For gas dryers, also close the gas valve. Pull the machine away from the wall and remove the back or lower front panel (model-specific — check the sticker inside the door for the model number and search "<i>model</i> service manual").</p>
<div class="callout"><b>Safety:</b> Electric dryers run on 240 V. Never test with power connected. If you're not comfortable, <a href="../../get-quote/?cat=appliances">get a quote</a> — this is a $100–$350 job.</div>
<h2>1. Thermal fuse (most common)</h2><p>A one-shot safety fuse near the blower housing or heating element. It blows when the dryer overheats — usually because the vent is clogged. Set your multimeter to continuity; a good fuse beeps, a bad one is silent. <b>Replace the fuse AND clean the vent</b> or it will blow again.</p>
<h2>2. Heating element</h2><p>A coil in a metal housing. Look for a visible break in the coil, or test continuity across the terminals (a good element reads roughly 8–15 Ω). Part cost: $25–$60.</p>
<h2>3. Cycling thermostat / high-limit thermostat</h2><p>Small round discs mounted on the heater housing. Test continuity at room temperature: they should be closed (continuity). If open, replace.</p>
<h2>Gas dryers: igniter and flame sensor</h2><p>If the igniter glows but no flame appears, the gas valve coils are the usual culprit ($20–$40). If the igniter never glows, test the igniter and the thermal fuse.</p>
<h2>When to call a pro</h2><ul><li>Burning smell that persists after cleaning lint</li><li>Control board errors</li><li>Any gas-line concern</li></ul>
<table class="table"><tr><th>Fix</th><th>DIY part</th><th>Pro quote</th></tr><tr><td>Thermal fuse</td><td>$10–$20</td><td>$100–$180</td></tr><tr><td>Heating element</td><td>$25–$60</td><td>$150–$300</td></tr><tr><td>Thermostat</td><td>$15–$30</td><td>$120–$220</td></tr></table>
"""),
 dict(slug="fridge-not-cooling", cat="appliances", title="Refrigerator not cooling: a 10-minute diagnosis before you pay $350", minutes=7, cost="$0–$80 DIY",
  summary="Freezer cold but fridge warm? Both warm? Clicking sounds? Each symptom points to a different part — and only one of them is expensive.",
  body="""
<h2>Symptom → likely cause</h2>
<table class="table"><tr><th>Symptom</th><th>Likely cause</th><th>DIY?</th><th>Typical pro cost</th></tr>
<tr><td>Freezer cold, fridge warm</td><td>Evaporator fan or damper, or frost-blocked airflow (defrost system)</td><td>Fan: yes. Defrost: often</td><td>$150–$300</td></tr>
<tr><td>Both warm, compressor humming</td><td>Condenser fan or dirty condenser coils</td><td>Yes</td><td>$100–$250</td></tr>
<tr><td>Both warm, clicking every few minutes</td><td>Start relay / capacitor; if not, compressor</td><td>Relay: yes ($20–$40)</td><td>$150 relay / $600+ compressor</td></tr>
<tr><td>Both warm, dead silent</td><td>Power, control board, thermostat</td><td>Check outlet first</td><td>$150–$400</td></tr>
<tr><td>Runs constantly, slightly warm</td><td>Door gasket, coils, low refrigerant (sealed system)</td><td>Gasket &amp; coils yes</td><td>$100 / $400+</td></tr></table>
<h2>Do this first (free)</h2><ol><li>Vacuum the condenser coils (bottom front or rear).</li><li>Check the door seal with a paper test — if a sheet slides out easily, the gasket is shot.</li><li>Make sure the freezer fan runs when the door switch is pressed.</li><li>Check the temperature dials weren't bumped.</li></ol>
<div class="callout blue"><b>The one expensive fault:</b> sealed-system (compressor / refrigerant) work. Under warranty, go through the <a href="../../brands/">manufacturer</a>. Out of warranty on a fridge older than 8 years, replacement usually wins.</div>
"""),
 dict(slug="phone-screen-repair-vs-replace", cat="phones", title="Cracked screen: repair, replace or trade in? A decision table", minutes=5, cost="$80–$350 repair",
  summary="Screen repair prices range from $80 to $350+. Whether it's worth it depends on device age, quote, and resale value — use this table.",
  body="""
<h2>The 3-question test</h2><ol><li><b>Is the quote under 35% of the phone's current resale value?</b> If yes, repair.</li><li><b>Is the phone under 3 years old?</b> If yes, lean repair (OEM part if flagship).</li><li><b>Does the screen still work (touch, no lines)?</b> If yes and only glass is cracked, a cheaper glass-only refurb may be possible at specialist shops.</li></ol>
<table class="table"><tr><th>Device age</th><th>Quote</th><th>Verdict</th></tr><tr><td>&lt; 2 years</td><td>Any</td><td>Repair with OEM / authorized part</td></tr><tr><td>2–4 years</td><td>&lt; $150</td><td>Repair (aftermarket OK)</td></tr><tr><td>2–4 years</td><td>&gt; $150</td><td>Compare against trade-in value first</td></tr><tr><td>4+ years</td><td>&gt; $100</td><td>Replace; sell for parts</td></tr></table>
<h2>OEM vs aftermarket screens</h2><p>OEM panels keep True Tone / colour accuracy / fingerprint sensors working and preserve warranty. Aftermarket panels save 30–50% but can dim, mis-register touch, or trigger "unknown part" warnings. For flagships under 2 years old, pay for OEM.</p>
<h2>Authorized vs independent</h2><p>Authorized centers charge more but keep warranty and water resistance ratings intact. Independent shops are cheaper and faster. Out of warranty, an independent shop with strong reviews is the value pick.</p>
<p><a class="btn btn-accent" href="../../get-quote/?cat=phones">Get 3 screen-repair quotes →</a></p>
"""),
 dict(slug="check-engine-light", cat="auto", title="Check-engine light on? Read the code before you pay for a diagnosis", minutes=6, cost="$20 OBD-II reader",
  summary="A $20 reader tells you what a $120 diagnostic fee would. Here are the six most common codes, what they mean and what the fix usually costs.",
  body="""
<h2>Step 1: plug in a reader</h2><p>Every car since 1996 has an OBD-II port under the dash. A basic Bluetooth reader costs $15–$30 and pairs with a free phone app. Many auto-parts stores also scan for free.</p>
<h2>The six most common codes</h2>
<table class="table"><tr><th>Code</th><th>Meaning</th><th>Common fix</th><th>Typical cost</th></tr>
<tr><td>P0420</td><td>Catalyst efficiency below threshold</td><td>O2 sensor or catalytic converter</td><td>$150 / $900–$2,500</td></tr>
<tr><td>P0300–P0308</td><td>Misfire (cylinder #)</td><td>Spark plugs, coil pack</td><td>$120–$400</td></tr>
<tr><td>P0171 / P0174</td><td>System too lean</td><td>Vacuum leak, MAF sensor, fuel pump</td><td>$100–$600</td></tr>
<tr><td>P0455 / P0442</td><td>EVAP leak (large / small)</td><td>Gas cap, purge valve</td><td>$15–$250</td></tr>
<tr><td>P0128</td><td>Coolant below thermostat temp</td><td>Thermostat</td><td>$150–$350</td></tr>
<tr><td>P0401</td><td>EGR flow insufficient</td><td>Clean or replace EGR valve</td><td>$150–$500</td></tr></table>
<div class="callout"><b>Flashing check-engine light</b> = active misfire that can destroy the catalytic converter. Stop driving and get it towed or seen the same day.</div>
<h2>Step 2: don't just clear it</h2><p>Clearing the code without fixing the cause also erases the readiness monitors — you'll fail an emissions test until they reset.</p>
<p><a class="btn btn-accent" href="../../get-quote/?cat=auto">Get 3 repair quotes with your code →</a></p>
"""),
 dict(slug="furnace-not-igniting", cat="home", title="Furnace clicks but won't ignite: the 5-minute flame-sensor fix", minutes=5, cost="$0",
  summary="The most common furnace no-heat call is a dirty flame sensor. It takes a piece of fine sandpaper and five minutes.",
  body="""
<h2>Symptom</h2><p>Furnace starts, igniter glows or clicks, burners light for 3–5 seconds, then shut off. Repeats 3 times, then locks out.</p>
<h2>Fix</h2><ol><li>Turn off power at the switch on the furnace and close the gas valve.</li><li>Remove the burner compartment door.</li><li>Find the flame sensor: a thin metal rod on a ceramic base with one wire, positioned in the flame path opposite the igniter.</li><li>Remove the single screw, slide it out, and gently polish the rod with fine (400+) sandpaper or steel wool. Wipe clean.</li><li>Reinstall, restore gas and power, and test.</li></ol>
<div class="callout"><b>Stop and call a pro if:</b> you smell gas, the igniter never glows, or the burner flames are yellow/orange instead of blue. Cracked heat exchangers and gas-valve faults are not DIY.</div>
<h2>Other quick checks</h2><ul><li>Thermostat set to Heat and calling above room temperature</li><li>Filter not clogged (a blocked filter trips the high-limit switch)</li><li>Condensate drain not blocked (high-efficiency units)</li><li>Exhaust and intake pipes clear of snow, nests or debris</li></ul>
<p>Still no heat? Service calls run $80–$250 and a furnace repair typically $150–$1,200. <a href="../../get-quote/?cat=home">Get 3 quotes →</a></p>
"""),
 dict(slug="laptop-slow-fix-or-replace", cat="computers", title="Slow laptop: the $60 upgrade that beats a $900 replacement", minutes=6, cost="$40–$120",
  summary="Most 'slow' laptops from the last 8 years are fixed by two upgrades and one cleanup. Here's the order and what a shop will charge.",
  body="""
<h2>Diagnose in 2 minutes</h2><p>Open Task Manager (Windows) or Activity Monitor (Mac). If the disk sits at 100% or memory is constantly above 85%, hardware is the bottleneck. If CPU is pegged by one process, it's software.</p>
<h2>Upgrade order</h2><ol><li><b>Hard drive → SSD</b> ($40–$90 for 1 TB). The single biggest speed-up ever available for older machines. Most Windows laptops: 15-minute swap with a cloning tool. Most Macs since 2016: soldered — skip.</li><li><b>RAM to 16 GB</b> ($30–$60). Only if memory is the bottleneck and slots are accessible.</li><li><b>Clean install of the OS</b> ($0). Removes years of accumulated junk.</li><li><b>Thermal repaste + fan clean</b> ($10). Fixes throttling on machines 4+ years old.</li></ol>
<table class="table"><tr><th>Job</th><th>DIY</th><th>Shop</th></tr><tr><td>SSD upgrade + migration</td><td>$40–$90</td><td>$120–$350</td></tr><tr><td>RAM upgrade</td><td>$30–$60</td><td>$80–$150</td></tr><tr><td>OS clean install + tune-up</td><td>$0</td><td>$80–$150</td></tr></table>
<h2>When to replace instead</h2><p>Soldered 4 GB RAM, no SSD option, or a CPU older than 2014. If total upgrades exceed 40% of a comparable new machine, replace.</p>
<p><a class="btn btn-accent" href="../../get-quote/?cat=computers">Get 3 upgrade quotes →</a></p>
"""),
 dict(slug="tv-repair-or-replace", cat="electronics", title="TV won't turn on or has no picture: repair or replace?", minutes=5, cost="$20–$120 in boards",
  summary="Power boards, backlights and T-con boards cover most TV failures. Two are cheap; one is tedious. Here's how to tell which one you have.",
  body="""
<h2>Symptom guide</h2>
<table class="table"><tr><th>Symptom</th><th>Likely part</th><th>DIY</th><th>Pro cost</th></tr>
<tr><td>Dead — no standby light</td><td>Power supply board</td><td>Moderate ($30–$80 board)</td><td>$120–$250</td></tr>
<tr><td>Sound but black screen; image visible with flashlight</td><td>LED backlight strips</td><td>Tedious (full teardown)</td><td>$150–$400</td></tr>
<tr><td>Vertical lines, half-screen, colour bands</td><td>T-con board or panel</td><td>T-con easy ($20–$60); panel = replace TV</td><td>$120–$250 / N/A</td></tr>
<tr><td>Cracked screen</td><td>Panel</td><td>No</td><td>Usually exceeds TV value</td></tr></table>
<h2>The replacement math</h2><p>If a quote exceeds 50% of a comparable new TV, replace. For a 4-year-old 55" set worth $350 new, a $200 backlight repair is borderline; a $120 power-board repair is worth it.</p>
<div class="callout"><b>Capacitor warning:</b> power boards hold charge after unplugging. Wait 10 minutes and avoid touching component legs.</div>
<p><a class="btn btn-accent" href="../../get-quote/?cat=electronics">Get 3 TV repair quotes →</a></p>
"""),
 dict(slug="how-to-compare-repair-quotes", cat="all", title="How to compare repair quotes (and spot the padded one)", minutes=4, cost="Free",
  summary="Three quotes for the same job can differ by 2×. Here's the checklist we use to normalize them.",
  body="""
<h2>Make every quote answer the same 7 questions</h2><ol><li>Is it itemized — parts, labour hours, rate, diagnostic fee, tax?</li><li>Is the diagnostic fee credited toward the repair?</li><li>OEM, OEM-equivalent or aftermarket parts?</li><li>Warranty on parts and labour — and in writing?</li><li>Turnaround time and whether a loaner/courtesy service exists?</li><li>What happens if they find something else — do they call before proceeding?</li><li>Payment terms: deposit? Card fees?</li></ol>
<h2>Red flags</h2><ul><li>Refuses to itemize or put the warranty in writing</li><li>"Special today only" pricing pressure</li><li>Quote far below the <a href="../../costs/">benchmark</a> — often a bait fee with add-ons later</li><li>No physical address or business registration</li></ul>
<h2>Green flags</h2><ul><li>Explains the fault and shows you the failed part</li><li>Offers a cheaper repair-vs-replace opinion when appropriate</li><li>Consistent reviews across two or more platforms</li></ul>
<p><a class="btn btn-accent" href="../../get-quote/">Get 3 quotes to compare →</a></p>
"""),
]

def pages(k):
    L, ad, band, crumbs, rel, CATS, CAT, SITE_URL, TODAY = k["layout"], k["ad"], k["cta_band"], k["crumbs"], k["rel"], k["CATEGORIES"], k["CAT"], k["SITE_URL"], k["TODAY"]
    out = []
    r = rel(1)
    cards = "".join(f'<a class="card" href="{r}guides/{g["slug"]}/"><span class="badge brand">{CAT[g["cat"]][2] if g["cat"] in CAT else "All categories"}</span><h3>{g["title"]}</h3><p class="muted small">{g["summary"]}</p><div class="small">⏱ {g["minutes"]} min read · 💲 {g["cost"]}</div></a>' for g in GUIDES)
    idx = f"""{crumbs(r, [("", "Repair guides")])}<section class="section tight"><div class="container"><span class="eyebrow">Fix it yourself</span><h1>Repair guides &amp; decision tools</h1><p class="muted" style="max-width:720px">Practical, tested guides that tell you what's likely broken, whether you can fix it, what it costs either way, and when to stop and call a pro.</p>
<div class="grid grid-3 mt-3">{cards}</div>{ad("inArticle")}
<div class="card mt-3"><h3>Want a guide we haven't written?</h3><p class="muted small">Tell us the device and problem — popular requests get written first.</p><form class="form" data-form="Guide request" data-success="Thanks — request logged!"><input type="text" name="_honey" class="honeypot" tabindex="-1"><div class="row"><input name="request" placeholder="e.g. Bosch dishwasher E24 error" required><input type="email" name="email" placeholder="Email (optional, to notify you)"></div><button class="btn btn-primary">Request guide</button><div class="form-status"></div></form></div>
</div></section>{band(r)}"""
    out.append(dict(path="guides/index.html", html=L("guides/index.html", "Repair Guides — Fix It Yourself or Know When to Call a Pro", "Step-by-step repair guides and decision tools for phones, computers, TVs, appliances, cars and home systems, with DIY vs pro cost comparisons.", idx, 1)))

    for g in GUIDES:
        r = rel(2)
        catname = CAT[g["cat"]][2] if g["cat"] in CAT else "All categories"
        catlink = f'categories/{g["cat"]}/' if g["cat"] in CAT else "guides/"
        related = "".join(f'<a class="card" href="{r}guides/{o["slug"]}/"><h3 style="font-size:1rem">{o["title"]}</h3></a>' for o in GUIDES if o is not g and (o["cat"] == g["cat"] or g["cat"] == "all"))[:3000]
        ld = json.dumps({"@context": "https://schema.org", "@type": "HowTo", "name": g["title"], "description": g["summary"], "estimatedCost": {"@type": "MonetaryAmount", "currency": "USD", "value": g["cost"]}, "totalTime": f"PT{g['minutes']}M"})
        body = f"""
{crumbs(r, [("guides/", "Guides"), (catlink, catname), ("", g["title"][:40] + "…")])}
<section class="section tight"><div class="container"><div class="layout-side"><article class="article">
  <span class="badge brand">{catname}</span><h1 class="mt-1">{g["title"]}</h1>
  <p class="muted small">⏱ {g["minutes"]} min read · 💲 {g["cost"]} · Updated {TODAY} · <button class="btn btn-outline btn-sm" data-share>Share</button></p>
  <p class="lead" style="font-size:1.12rem">{g["summary"]}</p>
  {ad("inArticle")}
  {g["body"]}
  {ad("inArticle")}
  <div class="callout blue"><b>Affiliate disclosure:</b> product links on this page may earn us a commission at no cost to you. It funds free guides.</div>
  <h2>Related guides</h2><div class="grid grid-2">{related}</div>
</article><aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Skip the DIY?</h3><p class="muted small">Get 3 free quotes from vetted centers.</p><a class="btn btn-accent btn-sm" href="{r}get-quote/?cat={g['cat'] if g['cat'] in CAT else ''}">Get quotes →</a></div></aside></div></div></section>
"""
        out.append(dict(path=f"guides/{g['slug']}/index.html", html=L(f"guides/{g['slug']}/index.html", g["title"], g["summary"], body, 2, extra_head=f'<script type="application/ld+json">{ld}</script>', article=True)))

    # ---------------- VIDEOS ----------------
    r = rel(1)
    sections = "".join(f"""<h2 class="mt-4">{i} {n}</h2><div data-yt="{s}" class="grid grid-2"><div class="card"><p class="muted small">Add a playlist id or video ids for <code>{s}</code> in <code>assets/js/config.js → youtube.byCategory</code> to embed videos here. Until then: <a href="https://www.youtube.com/results?search_query={n.replace(' ', '+').replace('&', '%26')}+repair" target="_blank" rel="noopener">search YouTube for {n.lower()} repair videos →</a></p></div></div>""" for s, i, n, d in CATS)
    vid = f"""{crumbs(r, [("", "Videos")])}<section class="section tight"><div class="container"><div class="layout-side"><div>
<span class="eyebrow">Watch &amp; fix</span><h1>Repair video library</h1><p class="muted" style="max-width:700px">Curated, embedded repair walkthroughs by category — plus our own channel. Videos are embedded with privacy-enhanced mode.</p>
<h2 class="mt-3">Featured</h2><div data-yt="featured" class="grid grid-2"><div class="card"><h3>Our channel is launching</h3><p class="muted small">Connect the channel in <code>config.js</code> (<code>youtube.channelId</code>) and the latest uploads appear here automatically. <a data-social="youtube" href="#">Subscribe on YouTube</a>.</p></div></div>
{ad("inArticle")}
{sections}
<div class="card mt-4"><h3>Submit a video</h3><p class="muted small">Are you a repair creator? Get featured and linked from cost guides.</p><form class="form" data-form="Video submission" data-success="Thanks — we'll review it!"><input type="text" name="_honey" class="honeypot" tabindex="-1"><div class="row"><input name="video_url" placeholder="YouTube URL" required><input name="channel" placeholder="Channel name"></div><input type="email" name="email" placeholder="Contact email" required><button class="btn btn-primary">Submit video</button><div class="form-status"></div></form></div>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>{band(r)}"""
    out.append(dict(path="videos/index.html", html=L("videos/index.html", "Repair Video Library", "Curated repair walkthrough videos for phones, computers, TVs, appliances, cars and home systems.", vid, 1)))
    return out
