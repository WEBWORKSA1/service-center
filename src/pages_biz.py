"""Business + legal pages."""

def pages(k):
    L, ad, band, crumbs, rel, CATS, SITE, OWNER_URL, TODAY = k["layout"], k["ad"], k["cta_band"], k["crumbs"], k["rel"], k["CATEGORIES"], k["SITE"], k["OWNER_URL"], k["TODAY"]
    out = []
    r = rel(1)
    HP = '<input type="text" name="_honey" class="honeypot" tabindex="-1" autocomplete="off">'
    cat_opts = "".join(f'<option value="{s}">{n}</option>' for s, i, n, d in CATS)

    # ---------------- PARTNERS (business lead-gen) ----------------
    partners = f"""
<section class="hero" style="padding:48px 0"><div class="container"><span class="chip">For service centers, garages, technicians &amp; franchises</span><h1 class="mt-2">Get qualified local repair leads. <span>Pay only for results.</span></h1><p class="lead">Every day people describe a repair, tell us their location and ask for quotes. Join the network and those requests land in your inbox.</p>
<div class="hero-stats"><div><b>Free</b>basic listing</div><div><b>Max 3</b>centers per lead</div><div><b>0</b>long-term contracts</div></div></div></section>
<section class="section"><div class="container"><div class="layout-side"><div>
  <h2>Plans</h2>
  <div class="grid grid-3">
    <div class="card tier"><h3>Basic listing</h3><div class="price">$0<small>/mo</small></div><ul><li>Directory profile</li><li>Reviews &amp; badges</li><li>Manual lead matching</li></ul><a class="btn btn-outline btn-block" href="#join">Claim free listing</a></div>
    <div class="card tier featured"><span class="tag-pop">Most popular</span><h3>Pay-per-lead</h3><div class="price">$12–$65<small>/lead</small></div><ul><li>Priced by category &amp; job value</li><li>Only exclusive-to-3 leads</li><li>Refund on bad-contact leads</li><li>Lead dashboard by email</li></ul><a class="btn btn-primary btn-block" href="#join">Start receiving leads</a></div>
    <div class="card tier"><h3>Featured partner</h3><div class="price">$149<small>/mo per city</small></div><ul><li>Top of directory results</li><li>"Featured" badge</li><li>10 leads included</li><li>Homepage &amp; category placement</li></ul><a class="btn btn-accent btn-block" href="#join">Get featured</a></div>
  </div>
  <p class="small muted mt-2">Indicative lead pricing: phones/computers $12–$25 · electronics $15–$30 · appliances $25–$45 · auto $20–$50 · HVAC/plumbing/electrical $35–$65. Final pricing confirmed at onboarding.</p>
  {ad("inArticle")}
  <h2 class="mt-4">How partnering works</h2>
  <div class="grid grid-3 steps"><div class="step"><h3>Apply</h3><p class="muted small">Submit the form. We verify registration, reviews and coverage area within 2 business days.</p></div><div class="step"><h3>Receive leads</h3><p class="muted small">Matched requests arrive by email/SMS with full details. Respond within 2 hours for best conversion.</p></div><div class="step"><h3>Win jobs</h3><p class="muted small">Quote, book, and collect reviews that boost your ranking.</p></div></div>
  <h2 class="mt-4" id="join">Apply to join the network</h2>
  <form class="form card" data-form="Partner application" data-success="Application received. We'll verify and respond within 2 business days.">{HP}
    <div class="row"><div><label>Business name</label><input name="business" required></div><div><label>Website</label><input name="website" placeholder="https://"></div></div>
    <div class="row"><div><label>Primary category</label><select name="category" required>{cat_opts}</select></div><div><label>Years in business</label><select name="years"><option>&lt; 1</option><option>1–3</option><option>3–10</option><option>10+</option></select></div></div>
    <div class="row"><div><label>City / service area</label><input name="location" required></div><div><label>Authorized / certified for</label><input name="authorized" placeholder="e.g. Samsung, Apple IRP, ASE"></div></div>
    <div><label>Services offered</label><textarea name="services" required></textarea></div>
    <div class="row"><div><label>Contact name</label><input name="name" required></div><div><label>Phone</label><input name="phone" type="tel" required></div></div>
    <div class="row"><div><label>Email</label><input name="email" type="email" required></div><div><label>Interested plan</label><select name="plan"><option>Basic (free)</option><option>Pay-per-lead</option><option>Featured partner</option><option>Not sure yet</option></select></div></div>
    <div><label>Claiming an existing listing? Name it</label><input name="claim" id="claim-field"></div>
    <label class="consent"><input type="checkbox" required name="consent"> I confirm the business is legitimately registered and agree to the <a href="{r}terms/">partner terms</a>.</label>
    <button class="btn btn-accent btn-lg">Submit application</button><div class="form-status"></div>
  </form>
  <script>try{{var c=new URLSearchParams(location.search).get('claim');if(c)document.getElementById('claim-field').value=c;}}catch(e){{}}</script>
</div><aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Prefer to talk?</h3><p class="muted small">Send us a note and we'll call you.</p><a class="btn btn-outline btn-sm" href="{r}contact/">Contact us →</a></div></aside></div></div></section>
"""
    out.append(dict(path="partners/index.html", html=L("partners/index.html", "List Your Service Center & Get Repair Leads", "Join the Service.Center network: free directory listing, pay-per-lead pricing and featured placement for repair shops, garages and technicians.", partners, 1)))

    # ---------------- ADVERTISE ----------------
    advertise = f"""
{crumbs(r, [("", "Advertise & sponsor")])}
<section class="section tight"><div class="container"><div class="layout-side"><div>
  <span class="eyebrow">Advertise · Sponsor · Partner</span><h1>Reach people at the exact moment they decide who fixes it</h1>
  <p class="muted" style="max-width:720px">Service.Center visitors arrive with a broken thing and a budget. That's the highest-intent audience in local services. Sponsor a category, a guide series, the cost estimator, a contest — or the whole site.</p>
  <div class="grid grid-2 mt-3">
    <div class="card"><div class="icon">📌</div><h3>Category sponsorship</h3><p class="muted small">Exclusive banner + "Presented by" on one category hub and its guides. From <b>$499/mo</b>.</p></div>
    <div class="card"><div class="icon">🧮</div><h3>Cost-estimator sponsor</h3><p class="muted small">Your brand on every price result across the site. From <b>$899/mo</b>.</p></div>
    <div class="card"><div class="icon">📰</div><h3>Sponsored guide / review</h3><p class="muted small">Clearly labeled sponsored content written to our editorial standard. From <b>$350</b> per piece.</p></div>
    <div class="card"><div class="icon">🏆</div><h3>Contest sponsor</h3><p class="muted small">Supply the prize, own the entry page and email blast. From <b>$250</b> + prize.</p></div>
    <div class="card"><div class="icon">🖥</div><h3>Display advertising</h3><p class="muted small">Programmatic via Google AdSense / Ad Manager, or direct-sold fixed placements at <b>$8–$15 CPM</b>.</p></div>
    <div class="card"><div class="icon">🤝</div><h3>Site-wide or domain partnership</h3><p class="muted small">Interested in the domain, an equity partnership or an exclusive network deal? <a href="{OWNER_URL}" rel="noopener">web.works/contact</a></p></div>
  </div>
  {ad("inArticle")}
  <h2 class="mt-4">Request the media kit</h2>
  <form class="form card" data-form="Advertising inquiry" data-success="Thanks — the media kit and current availability are on their way.">{HP}
    <div class="row"><div><label>Company</label><input name="company" required></div><div><label>Website</label><input name="website"></div></div>
    <div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input name="email" type="email" required></div></div>
    <div class="row"><div><label>Interested in</label><select name="interest"><option>Category sponsorship</option><option>Cost-estimator sponsor</option><option>Sponsored content</option><option>Contest sponsor</option><option>Display ads</option><option>Site-wide partnership</option><option>Domain inquiry</option></select></div><div><label>Monthly budget</label><select name="budget"><option>&lt; $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div></div>
    <div><label>Message</label><textarea name="message"></textarea></div>
    <button class="btn btn-accent btn-lg">Send inquiry</button><div class="form-status"></div>
  </form>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>
"""
    out.append(dict(path="advertise/index.html", html=L("advertise/index.html", "Advertise, Sponsor or Partner with Service.Center", "Sponsorship packages, display advertising and partnership opportunities to reach high-intent repair and service buyers.", advertise, 1)))

    # ---------------- SUPPORT / DONATE ----------------
    support = f"""
{crumbs(r, [("", "Support us")])}
<section class="section tight"><div class="container"><div class="layout-side"><div>
  <span class="eyebrow">Support independent repair info</span><h1>Keep the guides free and the ads light</h1>
  <p class="muted" style="max-width:720px">We buy the parts, break the things, test the fixes and publish the real prices — with no manufacturer on the payroll. Your support funds test equipment, writers, video production, contest prizes and the hosting bill.</p>
  <div class="grid grid-3 mt-3">
    <div class="card center"><div class="icon" style="margin:0 auto">☕</div><h3>One-time</h3><p class="muted small">Buy the team a coffee (or a multimeter).</p><a class="btn btn-primary btn-block" data-support="buyMeACoffee" href="#">Buy Me a Coffee</a><a class="btn btn-outline btn-block mt-1" data-support="paypal" href="#">PayPal</a></div>
    <div class="card center tier featured"><span class="tag-pop">Best value</span><div class="icon" style="margin:0 auto">💙</div><h3>Monthly supporter</h3><p class="muted small">Ad-free reading, early guides, supporter badge.</p><a class="btn btn-accent btn-block" data-support="patreon" href="#">Patreon</a><a class="btn btn-outline btn-block mt-1" data-support="kofi" href="#">Ko-fi</a></div>
    <div class="card center"><div class="icon" style="margin:0 auto">🐙</div><h3>Sponsor the project</h3><p class="muted small">Businesses and developers.</p><a class="btn btn-primary btn-block" data-support="githubSponsors" href="#">GitHub Sponsors</a><a class="btn btn-outline btn-block mt-1" data-support="stripeLink" href="#">Card (Stripe)</a></div>
  </div>
  <h2 class="mt-4">Where the money goes</h2>
  <table class="table"><tr><th>Use</th><th>Share</th></tr><tr><td>Test devices, parts and tools for guides</td><td>35%</td></tr><tr><td>Writers, technicians and video production</td><td>30%</td></tr><tr><td>Contest prizes and community</td><td>15%</td></tr><tr><td>Hosting, tools, marketing</td><td>20%</td></tr></table>
  {ad("inArticle")}
  <h2 class="mt-4">Other ways to help</h2>
  <div class="grid grid-2"><div class="card"><h3>Share a guide</h3><p class="muted small">Every share is a free ad.</p><button class="btn btn-outline btn-sm" data-share>Share this site</button></div><div class="card"><h3>Submit a price you paid</h3><p class="muted small">Real receipts make the estimator better for everyone.</p></div></div>
  <form class="form card mt-3" data-form="Price report" data-success="Thank you — logged for the next benchmark update.">{HP}<h3>Report a real repair price</h3><div class="row"><select name="category">{cat_opts}</select><input name="job" placeholder="Job (e.g. dryer heating element)" required></div><div class="row"><input name="price" placeholder="Total paid (USD)" required><input name="location" placeholder="City" required></div><input name="shop" placeholder="Shop name (optional)"><button class="btn btn-primary">Submit price</button><div class="form-status"></div></form>
</div><aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Corporate sponsor?</h3><a class="btn btn-outline btn-sm" href="{r}advertise/">Sponsorship options →</a></div></aside></div></div></section>
"""
    out.append(dict(path="support/index.html", html=L("support/index.html", "Support Service.Center — Donate", "Support independent repair guides and fair-price data with a one-time or monthly contribution.", support, 1)))

    # ---------------- CAREERS ----------------
    roles = [("Repair Technician Writers (remote, freelance)", "Write tested guides in your specialty. Paid per piece + revenue share."), ("Video Creators (remote)", "Produce short repair walkthroughs. Rev-share on ad income plus fixed fees."), ("Local Vetting Partners (city-based)", "Verify and onboard service centers in your metro. Commission per activated partner."), ("Sales / Partnerships (remote)", "Sell featured listings and sponsorships. High commission."), ("Front-end Developer (contract)", "Extend the static site, tooling and data pipelines.")]
    careers = f"""
{crumbs(r, [("", "Careers")])}
<section class="section tight"><div class="container"><div class="layout-side"><div>
  <span class="eyebrow">Hiring talent</span><h1>Work on the fair-repair platform</h1><p class="muted" style="max-width:700px">Remote-first, output-paid, no bureaucracy. If you can fix things, explain things or sell things, there's a role.</p>
  <div class="grid grid-2 mt-3">{''.join(f'<div class="card"><h3>{t}</h3><p class="muted small">{d}</p><a class="btn btn-outline btn-sm" href="#apply">Apply →</a></div>' for t, d in roles)}</div>
  {ad("inArticle")}
  <h2 class="mt-4" id="apply">Apply</h2>
  <form class="form card" data-form="Job application" data-success="Application received — we reply to every applicant within 7 days.">{HP}
    <div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input name="email" type="email" required></div></div>
    <div class="row"><div><label>Role</label><select name="role" required>{''.join(f'<option>{t}</option>' for t, d in roles)}<option>Other / propose a role</option></select></div><div><label>Location &amp; time zone</label><input name="location"></div></div>
    <div><label>Portfolio / LinkedIn / YouTube / GitHub</label><input name="links" placeholder="Paste links"></div>
    <div><label>Why you? (short)</label><textarea name="pitch" required></textarea></div>
    <div><label>Expected rate</label><input name="rate" placeholder="e.g. $120 per guide / $40 per hour"></div>
    <button class="btn btn-accent btn-lg">Send application</button><div class="form-status"></div>
  </form>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>
"""
    out.append(dict(path="careers/index.html", html=L("careers/index.html", "Careers — Writers, Technicians, Creators & Sales", "Remote, output-paid roles for repair technicians, writers, video creators, vetting partners and sales talent.", careers, 1)))

    # ---------------- CONTESTS ----------------
    contests = f"""
{crumbs(r, [("", "Contests & prizes")])}
<section class="hero" style="padding:44px 0"><div class="container"><span class="chip">🏆 Community contest</span><h1 class="mt-2">Best DIY Repair of the Month</h1><p class="lead">Show us a repair you did yourself — before/after photos and what it would have cost at a shop. Best entry wins a pro-grade repair toolkit and a feature on the homepage.</p>
<div class="countdown mt-2" data-countdown="{TODAY[:7]}-28T23:59:59"></div></div></section>
<section class="section"><div class="container"><div class="layout-side"><div>
  <div class="grid grid-3"><div class="card"><div class="icon">🥇</div><h3>1st prize</h3><p class="muted small">Pro repair toolkit (value $150) + homepage feature + supporter badge.</p></div><div class="card"><div class="icon">🥈</div><h3>2nd prize</h3><p class="muted small">$50 parts voucher + feature in the newsletter.</p></div><div class="card"><div class="icon">🥉</div><h3>3rd prize</h3><p class="muted small">Multimeter + feature in the guide library.</p></div></div>
  <h2 class="mt-4">Enter</h2>
  <form class="form card" data-form="Contest entry" data-success="Entry received! Winners are announced in the newsletter on the 1st.">{HP}
    <div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input name="email" type="email" required></div></div>
    <div class="row"><div><label>Category</label><select name="category">{cat_opts}</select></div><div><label>What you fixed</label><input name="item" required></div></div>
    <div><label>Photo / video links (before &amp; after)</label><input name="media" placeholder="Drive / Imgur / YouTube link" required></div>
    <div><label>Tell the story (what broke, what you did, what a shop quoted)</label><textarea name="story" required></textarea></div>
    <label class="consent"><input type="checkbox" name="consent" required> I own these photos and grant Service.Center permission to publish my entry with credit. I have read the <a href="#rules">rules</a>.</label>
    <button class="btn btn-accent btn-lg">Submit entry</button><div class="form-status"></div>
  </form>
  {ad("inArticle")}
  <h2 class="mt-4" id="rules">Rules (short version)</h2>
  <ul><li>Open worldwide to entrants 18+, except where prohibited. Void where prohibited. No purchase necessary.</li><li>One entry per person per month. Entries must be your own work.</li><li>Judged on difficulty, clarity, safety and money saved. Judges' decision final.</li><li>Prizes have no cash alternative unless stated; taxes are the winner's responsibility. Prize sponsors may be named on this page.</li><li>By entering you grant a non-exclusive licence to publish your entry with credit.</li></ul>
  <h2 class="mt-4">Sponsor a contest</h2><p>Provide the prize; own the entry page, the announcement email and the winner feature. <a href="{r}advertise/">Sponsorship options →</a></p>
</div><aside>{ad("sidebar", "sticky-side")}<div class="card mt-3"><h3>Past winners</h3><p class="muted small">First winners announced next month.</p></div></aside></div></div></section>
"""
    out.append(dict(path="contests/index.html", html=L("contests/index.html", "Contests & Prizes — Best DIY Repair of the Month", "Enter the monthly DIY repair contest to win tools, vouchers and a homepage feature.", contests, 1)))

    # ---------------- ABOUT ----------------
    about = f"""
{crumbs(r, [("", "About")])}
<section class="section tight"><div class="container"><div class="article">
  <span class="eyebrow">About</span><h1>Independent. Cross-category. Price-transparent.</h1>
  <p class="lead">Service.Center exists because finding someone trustworthy to fix a phone, a fridge or a furnace shouldn't require three hours of research and a leap of faith on price.</p>
  <h2>What we do</h2><p>We combine three things that other sites keep apart: a <b>directory</b> of authorized and independent service centers across six categories, a <b>fair-price estimator</b> built from real market data, and <b>DIY guides and videos</b> so you can decide for yourself whether to fix, book or replace. When you want quotes, our <a href="{r}get-quote/">free request</a> reaches up to three vetted local centers.</p>
  <h2>How we stay independent</h2><ul><li>No manufacturer or repair chain owns or funds us.</li><li>Sponsored content is always labeled.</li><li>Ranking in the directory is driven by reviews and response quality; featured placement is labeled "Featured".</li><li>Cost benchmarks are never influenced by partners.</li></ul>
  <h2>How we make money</h2><p>Service centers pay for leads and featured placement. We run display ads on informational pages, earn affiliate commissions on some product links, accept sponsorships, and gratefully take <a href="{r}support/">reader support</a>. Consumers never pay.</p>
  <h2>Editorial standards</h2><p>Guides are written or reviewed by working technicians. Every guide states DIY difficulty, safety stops, and the pro-repair cost so you can make an informed call.</p>
  <h2>Work with us</h2><p><a href="{r}partners/">List a business</a> · <a href="{r}advertise/">Advertise</a> · <a href="{r}careers/">Join the team</a> · <a href="{r}contact/">Contact</a> · Interested in the domain or a partnership? <a href="{OWNER_URL}" rel="noopener">web.works/contact</a></p>
</div></div></section>{band(r)}
"""
    out.append(dict(path="about/index.html", html=L("about/index.html", "About Service.Center", "An independent, cross-category platform for finding trusted service centers, fair repair prices and DIY guides.", about, 1)))

    # ---------------- CONTACT ----------------
    contact = f"""
{crumbs(r, [("", "Contact")])}
<section class="section tight"><div class="container"><div class="layout-side"><div>
  <span class="eyebrow">Contact</span><h1>Get in touch</h1>
  <p class="muted" style="max-width:640px">Questions, corrections, partnership ideas, press, data requests — use the form or the email link. We respond within 2 business days.</p>
  <div class="grid grid-2 mt-3">
    <div class="card"><h3>Email us</h3><p class="muted small">Opens your mail app. The address is not published on the page to prevent spam.</p><a class="btn btn-primary btn-sm" data-contact="Service.Center inquiry" href="#">✉ Send an email</a></div>
    <div class="card"><h3>Website, domain, sponsorship or partnership?</h3><p class="muted small">For inquiries about this website or domain name, sponsorship, advertising or partnership:</p><a class="btn btn-accent btn-sm" href="{OWNER_URL}" rel="noopener">web.works/contact →</a></div>
  </div>
  <form class="form card mt-3" data-form="Contact" data-success="Message sent. We'll reply within 2 business days.">{HP}
    <div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input name="email" type="email" required></div></div>
    <div><label>Topic</label><select name="topic"><option>General question</option><option>Quote request follow-up</option><option>Correction to a guide or price</option><option>Business listing</option><option>Advertising / sponsorship</option><option>Press</option><option>Privacy / data request</option><option>Report a problem with a listed center</option></select></div>
    <div><label>Message</label><textarea name="message" required></textarea></div>
    <button class="btn btn-primary btn-lg">Send message</button><div class="form-status"></div>
  </form>
</div><aside>{ad("sidebar", "sticky-side")}</aside></div></div></section>
"""
    out.append(dict(path="contact/index.html", html=L("contact/index.html", "Contact Service.Center", "Contact us about quotes, guides, listings, advertising, press or privacy requests.", contact, 1)))

    # ---------------- LEGAL ----------------
    privacy = f"""{crumbs(r, [("", "Privacy policy")])}<section class="section tight"><div class="container"><div class="article"><h1>Privacy policy</h1><p class="muted small">Effective {TODAY}</p>
<h2>What we collect</h2><p>Information you submit in forms (name, contact details, location, repair description, media links); usage data via analytics cookies (if enabled); and advertising identifiers via Google AdSense and its partners.</p>
<h2>How we use it</h2><p>Quote requests are shared with up to three matched service centers so they can contact you. Newsletter addresses are used only for the newsletter. Applications and inquiries are used to respond to you. We do not sell personal data to data brokers.</p>
<h2>Advertising &amp; cookies</h2><p>We use Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You may opt out of personalized advertising at <a href="https://www.google.com/settings/ads" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener">aboutads.info</a>. EEA/UK visitors are shown a consent message where required.</p>
<h2>Form processing</h2><p>Forms are delivered through a third-party form relay to our inbox; the relay processes submissions on our behalf under its own privacy terms. A copy may be stored in your browser's local storage for your convenience only.</p>
<h2>Embedded content</h2><p>YouTube videos are embedded in privacy-enhanced mode. Interacting with embeds is subject to the provider's policies.</p>
<h2>Your rights</h2><p>Request access, correction or deletion at any time via the <a href="{r}contact/">contact page</a>. We respond within 7 days. EEA/UK/California residents have additional rights under GDPR/CCPA, which we honour.</p>
<h2>Retention &amp; security</h2><p>Lead data is retained for 12 months then deleted. Transport is encrypted (HTTPS).</p>
<h2>Children</h2><p>The site is not directed at children under 16 and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We'll post updates here with a new effective date.</p></div></div></section>"""
    out.append(dict(path="privacy/index.html", html=L("privacy/index.html", "Privacy Policy", "How Service.Center collects, uses and protects your information.", privacy, 1)))

    terms = f"""{crumbs(r, [("", "Terms of use")])}<section class="section tight"><div class="container"><div class="article"><h1>Terms of use</h1><p class="muted small">Effective {TODAY}</p>
<h2>1. The service</h2><p>Service.Center is an information and referral platform. We do not perform repairs, employ technicians, or guarantee any listed business's work. Any contract for services is between you and the service center.</p>
<h2>2. Quotes and leads</h2><p>By submitting a request you consent to being contacted by up to three matched service centers. Quotes are provided by those businesses, not by us. Cost estimates on this site are informational benchmarks, not offers.</p>
<h2>3. Guides</h2><p>DIY guides are provided for general information. Repairs involve risk of injury and property damage. Follow all safety instructions, local codes and manufacturer guidance; stop and hire a professional if in doubt. You act at your own risk.</p>
<h2>4. Partner terms</h2><p>Businesses must be legitimately registered and insured where required, respond to leads promptly and honestly, and may be removed for complaints, misrepresentation or non-payment. Lead fees are non-refundable except for invalid-contact leads reported within 3 business days.</p>
<h2>5. Content and IP</h2><p>Site content is © Service.Center unless noted. Third-party trademarks belong to their owners. You may share links; you may not scrape or republish content without permission.</p>
<h2>6. Contests</h2><p>Contest-specific rules are posted on the contest page and form part of these terms.</p>
<h2>7. Disclaimer of warranties; limitation of liability</h2><p>The site is provided "as is". To the fullest extent permitted by law we disclaim all warranties and are not liable for indirect, incidental or consequential damages arising from use of the site or any service center.</p>
<h2>8. Governing law</h2><p>These terms are governed by the laws of the operator's jurisdiction, without regard to conflict-of-law rules.</p>
<h2>9. Contact</h2><p>Questions: <a href="{r}contact/">contact page</a>.</p></div></div></section>"""
    out.append(dict(path="terms/index.html", html=L("terms/index.html", "Terms of Use", "Terms governing use of Service.Center, quote requests, guides and partner listings.", terms, 1)))

    disclaimer = f"""{crumbs(r, [("", "Disclaimer & disclosures")])}<section class="section tight"><div class="container"><div class="article"><h1>Disclaimer, trademark &amp; copyright disclosures</h1><p class="muted small">Effective {TODAY}</p>
<h2>Trademark disclosure</h2><p>The phrase "service center" is a common, descriptive English term meaning a place where products or vehicles are serviced or repaired. Service.Center uses it solely in that generic, descriptive sense as its domain name and site title, and claims no exclusive rights in the words "service center" as such. Service.Center is an independent information and referral platform. It is <b>not affiliated with, endorsed by, sponsored by, or an authorized agent, dealer, franchisee or service provider of any manufacturer, brand, retailer, franchise network or repair chain</b>, including any company whose name includes the words "service center".</p>
<p>All product names, company names, logos and trademarks referenced on this site — including but not limited to Apple, iPhone, MacBook, Samsung, Google, Pixel, Dell, HP, Lenovo, ASUS, Acer, Microsoft, Sony, PlayStation, Xbox, Nintendo, LG, Whirlpool, GE, Bosch, Maytag, Dyson, Toyota, Honda, Ford, BMW, Tesla, Hyundai, Carrier, Trane, Rheem, Lennox and Kohler — are trademarks or registered trademarks of their respective owners. They are used only to identify the products and services with which a repair or service may be compatible (nominative fair use) and not to suggest affiliation or endorsement. Links to manufacturer websites are provided for convenience; those sites are governed by their own terms.</p>
<h2>Copyright</h2><p>Original text, data compilations, code and graphics on this site are © Service.Center. Third-party content (including embedded videos) remains the property of its owners and is displayed under the platform's embed terms. If you believe content on this site infringes your rights, contact us via the <a href="{r}contact/">contact page</a> with the URL and details and we will respond promptly.</p>
<h2>Listings</h2><p>Listings marked "Demo listing" are illustrative placeholders and do not represent real businesses. Real listings are provided by the businesses themselves or compiled from public sources; verify credentials before hiring. Featured placement is paid and labeled.</p>
<h2>Cost estimates</h2><p>Benchmarks are compiled from public price data and industry reporting and adjusted by region. They are estimates for orientation only, not quotes, and may not reflect your specific model, fault or market.</p>
<h2>DIY guidance</h2><p>Repairs can cause injury, fire, electrocution, gas leaks or property damage. Guides are general information, not professional advice. Follow manufacturer instructions and local codes and consult a licensed professional when in doubt.</p>
<h2>Advertising &amp; affiliate disclosure</h2><p>This site displays advertising (including Google AdSense) and contains affiliate links, meaning we may earn a commission if you purchase through them at no extra cost to you. Sponsored content is labeled. Service centers may pay for leads and featured placement; this never influences guide content or cost benchmarks.</p>
<h2>Website / domain inquiries</h2><p>For inquiries about this website or domain name, sponsorship, advertising or partnership: <a href="{OWNER_URL}" rel="noopener">web.works/contact</a>.</p></div></div></section>"""
    out.append(dict(path="disclaimer/index.html", html=L("disclaimer/index.html", "Disclaimer, Trademark & Copyright Disclosures", "Trademark, copyright, affiliate and DIY safety disclosures for Service.Center.", disclaimer, 1)))

    # ---------------- 404 ----------------
    r0 = rel(0)
    nf = f"""<section class="section center"><div class="container"><h1>404 — That page needs service</h1><p class="muted">The link may be broken or the page moved.</p><div class="flex" style="justify-content:center"><a class="btn btn-primary" href="{r0}">Home</a><a class="btn btn-outline" href="{r0}find/">Directory</a><a class="btn btn-accent" href="{r0}get-quote/">Get quotes</a></div></div></section>"""
    base_fix = "<script>(function(){var p=location.pathname.split('/');var b=(p[1]&&p[1].indexOf('.')<0&&location.hostname.indexOf('github.io')>-1)?'/'+p[1]+'/':'/';document.write('<base href=\"'+b+'\">');})();</script>"
    out.append(dict(path="404.html", html=L("404.html", "Page not found", "Page not found.", nf, 0, extra_head=base_fix), nosite=True))
    return out
