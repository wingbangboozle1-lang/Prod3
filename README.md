# Prod3 — Kitchen Counter

**Kitchen Counter — Verified picks, plainly told.** A publication-style Amazon
affiliate site covering air fryers and meat thermometers. Tracking ID:
`shopnow047c-20`. Published to GitHub Pages on merge to `main` (project site: https://wingbangboozle1-lang.github.io/Prod3/)

## Status at a glance

| | |
|---|---|
| Submitted tokens that are ASINs | 0 of 5 (they are 9-char short-link tokens; an ASIN is 10 chars) |
| Observed destinations | B0CDY277D3, B09B7SB46R, B08DKYBTPH, B0DHZTCNR5, B0DZFD6R9Z |
| Intended ASINs confirmed | 0 of 5 (blank until owner confirms — see FLG-001) |
| Pages | 19 HTML (front page, 2 pillars, compare, guide, 8 articles, 6 trust pages) |
| Gates | `tools/verify_site.py` (exit 3 on violation) |

## Working with it

```
python3 tools/verify_site.py            # whole-tree release gate (exit 3 on violation)
python3 scripts/check_site.py           # data + HTML gate (exit 1 on violation)
python3 scripts/build_sitemap.py        # rewrite sitemap.xml from the tree
python3 scripts/build_sitemap.py --check # exit 1 if sitemap is stale
python3 tools/amazon_intake.py --link 'https://link.amazon/B04G1MEwY' --validate-only
python3 tools/amazon_intake.py --asin B0CDY277D3 --offline   # exit 0, queued for API
```

No third-party dependencies: the standard library only.

## Layout

- `index.html` — publication front page (hero, picks, chooser, categories, guides, data table)
- `air-fryers.html`, `meat-thermometers.html` — category pillars
- `compare.html`, `buying-guide.html` — comparison + decision framework
- `articles/` — 8 question-shaped guides (also in `feed.xml` + `sitemap.xml`)
- `disclosure.html`, `sources.html`, `flagged.html`, `direction.html`, `executive-summary.html`, `about.html` — trust surfaces
- `data/` — `products.json` (intent vs observed, never merged), `sources.json`, `campaign-ledger.json` (empty until first-party reports)
- `assets/` — `style.css`, `app.js` (privacy-preserving measurement), `og-image.svg`, `favicon.svg`
- `COORDINATION.md` — shared task board · `DIRECTION.md` — suggestions + open questions + path chooser
