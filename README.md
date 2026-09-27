# Service.Center

**Find · Compare · Fix.** An independent, cross-category platform for finding trusted repair & service centers, estimating fair repair prices, getting free quotes (lead generation) and fixing things yourself — for phones, computers, electronics, appliances, vehicles and homes.

Static site · GitHub Pages (free plan) · no backend · fully monetizable (AdSense, leads, sponsorships, affiliate, YouTube, donations).

## Quick start

```bash
python3 build.py            # regenerates every HTML page from src/pages_*.py
python3 -m http.server 8000 # preview at http://localhost:8000
```

Push to `main` → the workflow in `.github/workflows/pages.yml` rebuilds and deploys to GitHub Pages automatically (it enables Pages on the first run).

## Structure

```
build.py              layout (banner, header, footer, disclosure), sitemap, robots
src/pages_core.py     home, find (directory), categories, get-quote (lead wizard), costs, brands, faq
src/pages_content.py  guides (8 articles) and videos
src/pages_biz.py      partners, advertise, support (donations), careers, contests, about, contact, legal, 404
assets/js/config.js   ALL switches: contact key, form relay, AdSense, YouTube, donations, affiliate, analytics
assets/js/main.js     runtime: forms, wizard, directory, estimator, embeds, ads
assets/css/style.css  design system (light + dark)
data/centers.json     directory listings (seeded with clearly labeled demo entries — replace with real partners)
data/costs.json       30 repair cost benchmarks
docs/BUILD-PROMPT.md  phase-wise build prompt & roadmap
docs/RESEARCH.md      38-site competitive research
```

## Go-live checklist

1. **Forms** — submit any form once; the relay (FormSubmit) sends an activation email. Then paste your private hashed endpoint into `config.js → formEndpoint`.
2. **AdSense** — set `adsenseClient` + `adSlots` in `config.js`, and your publisher id in `ads.txt`.
3. **Donations** — fill `support.*` links (Buy Me a Coffee, Ko-fi, PayPal, Patreon, GitHub Sponsors, Stripe).
4. **YouTube** — `youtube.channelId` and per-category playlist ids.
5. **Analytics** — `ga4` or `plausibleDomain`.
6. **Custom domain** — add a `CNAME` file containing `service.center`; point DNS A records at GitHub Pages (185.199.108.153 / .109 / .110 / .111) and `www` CNAME at `webworksa1.github.io`; enable Enforce HTTPS in repo Settings → Pages.
7. **Replace demo listings** in `data/centers.json` with verified partners.

## Contact address policy

One address handles every inquiry. It is stored **only** base64-encoded in `config.js` (`contactKey`) and is decoded in the browser at click/submit time. It must never appear as plain text anywhere in this repository or on any page. Verify before each deploy:

```bash
grep -ri "<the address>" . --exclude-dir=.git   # must return nothing
```

## Trademark / copyright

"Service center" is used in its generic descriptive sense only. The site is not affiliated with any manufacturer, franchise or repair network; brand names are referenced under nominative fair use. Full disclosure in the footer of every page and at `/disclaimer/`.

Interested in this website, domain, sponsorship, advertising or partnership? **https://web.works/contact**
