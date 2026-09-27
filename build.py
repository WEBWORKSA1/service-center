#!/usr/bin/env python3
"""
Service.Center static site generator.
  python3 build.py        -> writes every page into the repo root (GitHub Pages serves root of `main`)
Add a page: append to PAGES in src/pages_*.py. Layout lives here.
"""
import os, sys, datetime, importlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

SITE = "Service.Center"
SITE_URL = "https://service.center"
OWNER_URL = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()

CATEGORIES = [
    ("phones", "📱", "Phones & Tablets", "Screens, batteries, ports, water damage"),
    ("computers", "💻", "Computers & Laptops", "Screens, SSDs, data recovery, tune-ups"),
    ("electronics", "📺", "TVs, Consoles & Electronics", "TVs, game consoles, audio, cameras"),
    ("appliances", "🧺", "Home Appliances", "Fridges, washers, dryers, ovens, dishwashers"),
    ("auto", "🚗", "Auto & Vehicle", "Brakes, diagnostics, AC, batteries, tires"),
    ("home", "🏠", "HVAC, Plumbing & Electrical", "Heating, cooling, leaks, wiring, water heaters"),
]
CAT = {c[0]: c for c in CATEGORIES}

NAV = [
    ("find/", "Find a Center"),
    ("costs/", "Cost Estimator"),
    ("guides/", "Repair Guides"),
    ("videos/", "Videos"),
    ("partners/", "For Businesses"),
    ("support/", "Support Us"),
]

def rel(depth):
    return "./" if depth == 0 else "../" * depth

def layout(path, title, desc, body, depth, extra_head="", canonical=None, article=False):
    r = rel(depth)
    canonical = canonical or (SITE_URL + "/" + path.replace("index.html", ""))
    nav = "".join(f'<a href="{r}{h}">{t}</a>' for h, t in NAV)
    cats_footer = "".join(f'<li><a href="{r}categories/{s}/">{n}</a></li>' for s, _, n, _ in CATEGORIES)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {SITE}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:url" content="{canonical}"><meta property="og:site_name" content="{SITE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.webmanifest">
<meta name="theme-color" content="#0b1633">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script src="{r}assets/js/config.js"></script>
{extra_head}
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="owner-banner">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="{OWNER_URL}" rel="noopener">web.works/contact</a></div>
<header class="header"><div class="container nav">
  <a class="logo" href="{r}"><span class="mark">🛠</span>Service<span class="dot">.</span>Center</a>
  <button class="nav-toggle" aria-label="Menu">☰ Menu</button>
  <nav class="nav-links" aria-label="Main">{nav}
    <button class="theme-toggle" aria-label="Toggle dark mode" title="Dark / light">◐</button>
    <a class="btn btn-accent btn-sm nav-cta" href="{r}get-quote/">Get Free Quotes</a>
  </nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="footer"><div class="container">
  <div class="grid">
    <div>
      <a class="logo" href="{r}" style="color:#fff"><span class="mark">🛠</span>Service<span class="dot">.</span>Center</a>
      <p class="mt-2 small">Find, compare and book trusted repair &amp; service centers for phones, computers, electronics, appliances, vehicles and homes — plus honest cost guides and step-by-step fixes.</p>
      <div class="flex">
        <a class="btn btn-light btn-sm" href="{r}get-quote/">Get Free Quotes</a>
        <a class="btn btn-outline btn-sm" style="color:#fff;border-color:#3b4b7a" href="{r}support/">♥ Support Us</a>
      </div>
      <div class="flex mt-2 small">
        <a data-social="youtube" href="#">YouTube</a><a data-social="x" href="#">X</a><a data-social="instagram" href="#">Instagram</a><a data-social="facebook" href="#">Facebook</a><a data-social="linkedin" href="#">LinkedIn</a><a data-social="tiktok" href="#">TikTok</a>
      </div>
    </div>
    <div><h4>Categories</h4><ul>{cats_footer}</ul></div>
    <div><h4>Explore</h4><ul>
      <li><a href="{r}find/">Service center directory</a></li>
      <li><a href="{r}costs/">Repair cost estimator</a></li>
      <li><a href="{r}guides/">Repair guides</a></li>
      <li><a href="{r}videos/">Video library</a></li>
      <li><a href="{r}brands/">Official brand support links</a></li>
      <li><a href="{r}faq/">FAQ</a></li>
    </ul></div>
    <div><h4>Business</h4><ul>
      <li><a href="{r}partners/">List your business</a></li>
      <li><a href="{r}advertise/">Advertise &amp; sponsor</a></li>
      <li><a href="{r}careers/">Careers &amp; talent</a></li>
      <li><a href="{r}contests/">Contests &amp; prizes</a></li>
      <li><a href="{r}support/">Donate / support</a></li>
      <li><a href="{r}about/">About</a></li>
    </ul></div>
    <div><h4>Legal</h4><ul>
      <li><a href="{r}contact/">Contact</a></li>
      <li><a href="{r}privacy/">Privacy policy</a></li>
      <li><a href="{r}terms/">Terms of use</a></li>
      <li><a href="{r}disclaimer/">Disclaimer &amp; disclosures</a></li>
      <li><a href="{r}sitemap.xml">Sitemap</a></li>
    </ul></div>
  </div>
  <p class="disclosure"><b>Trademark &amp; copyright disclosure.</b> "Service Center" is used on this website solely in its ordinary, descriptive English sense — a place where products and vehicles are serviced or repaired. {SITE} is an independent information and referral platform. It is not affiliated with, endorsed by, sponsored by, or an authorized agent of any manufacturer, brand, franchise or repair network. All product names, brand names, logos and trademarks (including Apple, Samsung, Dell, HP, Lenovo, LG, Whirlpool, GE, Bosch, Toyota, Honda, Ford, Tesla and others) are the property of their respective owners and are referenced only for identification and compatibility purposes under nominative fair use. Listings marked "Demo" are illustrative placeholders, not real businesses. Some links may be affiliate or sponsored links; we may earn a commission at no extra cost to you. Cost figures are estimates, not quotes. Full details in our <a href="{r}disclaimer/">Disclaimer</a>.</p>
  <div class="footer-bottom"><span>© <span data-year>2026</span> {SITE}. All rights reserved.</span><span>Interested in this domain, sponsorship or partnership? <a href="{OWNER_URL}" rel="noopener">web.works/contact</a></span></div>
</div></footer>
<div class="sticky-cta"><a class="btn btn-accent" href="{r}get-quote/">⚡ Get Free Quotes</a><a class="btn btn-outline" href="{r}find/">Find a Center</a></div>
<script src="{r}assets/js/main.js" defer></script>
</body></html>"""

def ad(slot="inArticle", cls=""):
    return f'<div class="ad-slot {cls}" data-slot="{slot}"></div>'

def cta_band(r, h="Need it fixed fast?", p="Describe the problem once. Get up to 3 free quotes from vetted local service centers.", btn="Get Free Quotes", href="get-quote/"):
    return f'<section class="section tight"><div class="container"><div class="cta-band"><div><h2>{h}</h2><p>{p}</p></div><a class="btn btn-light btn-lg" href="{r}{href}">{btn} →</a></div></div></section>'

def crumbs(r, items):
    parts = [f'<a href="{r}">Home</a>'] + [f'<a href="{r}{h}">{t}</a>' if h else t for h, t in items]
    return '<div class="container"><div class="crumbs">' + " › ".join(parts) + "</div></div>"

def write(path, html):
    full = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    pages = []
    for mod in ("pages_core", "pages_content", "pages_biz"):
        m = importlib.import_module(mod)
        pages += m.pages(dict(layout=layout, ad=ad, cta_band=cta_band, crumbs=crumbs, rel=rel,
                              CATEGORIES=CATEGORIES, CAT=CAT, SITE=SITE, SITE_URL=SITE_URL, OWNER_URL=OWNER_URL, TODAY=TODAY))
    urls = []
    for p in pages:
        write(p["path"], p["html"])
        if not p.get("nosite"):
            urls.append(SITE_URL + "/" + p["path"].replace("index.html", ""))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /src/\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"Built {len(pages)} pages, {len(urls)} in sitemap.")

if __name__ == "__main__":
    main()
