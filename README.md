# Prod3 — Kitchen Counter

**Kitchen Counter — Listed specs, plainly told.** A publication-style Amazon affiliate site covering air fryers and meat thermometers. The owner-supplied tracking ID is `shopnow047c-20`; its assignment and account eligibility have not been verified (FLG-010).

**Published site:** https://wingbangboozle1-lang.github.io/Prod3/ · GitHub Pages deploys from `main`.

Product details are attributed as seller/listing statements, not independent tests. Customer ratings and prices are not displayed. Product snapshots and source checks recorded in the data files are dated; verify the current listing before relying on time-sensitive details. The five observed redirect destinations do not establish the owner's intended ASINs or prove Special Link compliance. Those fields are kept separate in `data/products.json` and unresolved findings appear on [`flagged.html`](flagged.html).

## Current status

| Item | Status |
|---|---|
| Products | 5 submitted short-link tokens; 5 observed destinations; intended ASIN/listing confirmation remains blank for all 5 |
| Content | 24 HTML documents; eight question-shaped guides, plus comparison, buying guide, category pages, and trust/decision pages |
| Analytics | Five event types defined; four can be counted locally, none is sent to a server; no endpoint, Search Console property, or email provider configured |
| Campaign ledger | Empty by design; add data only from authorized first-party reports |
| Release checks | `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`, `scripts/build_sitemap.py --check`, `scripts/build_registers.py --check` |

## Working with it

```sh
python3 tools/verify_site.py                 # source cross-references, ledger, feed, robots, and core checks
python3 tools/check_site.py                  # complementary site assertions
python3 scripts/check_site.py                 # product/data/HTML checks
python3 scripts/build_registers.py           # rebuild suggestions, questions, and citations pages
python3 scripts/build_registers.py --check   # fail when generated pages are stale
python3 scripts/build_sitemap.py              # regenerate sitemap.xml
python3 scripts/build_sitemap.py --check     # fail when sitemap is stale
python3 tools/amazon_intake.py --link 'https://link.amazon/B04G1MEwY' --validate-only
python3 tools/amazon_intake.py --asin B0CDY277D3 --offline
```

The tools use Python's standard library; no third-party Python dependencies are required.

## Site map

- `index.html` — buyer-first front page with product cards, chooser, category links, guides, comparison data, and RSS link.
- `air-fryers.html`, `meat-thermometers.html` — category hubs.
- `compare.html`, `buying-guide.html` — comparison and decision framework.
- `articles/` — eight question-shaped guides, included in `feed.xml` and `sitemap.xml`.
- `suggestions.html`, `questions.html`, `direction.html` — proposals, missing-information questions, and decisions.
- `sources.html`, `citations.html`, `flagged.html`, `disclosure.html`, `analytics.html`, `executive-summary.html`, `about.html` — source, disclosure, analytics, and trust pages.
- `suggestions.html`, `questions.html`, and `citations.html` are generated from JSON by `scripts/build_registers.py`; do not hand-edit them.
- `data/products.json` keeps intended product/link confirmation separate from observed redirect information; `data/sources.json` and `data/citations.json` hold source and claim mappings; `data/campaign-ledger.json` is empty until authorized first-party reports exist.
- `assets/app.js` counts local browser events only; the self-hosted analytics endpoint is not configured. `assets/og-image.png` is the shipped 1200×630 social preview; external share-debugger rendering is not verified.
- `COORDINATION.md` is the task board; `DIRECTION.md` is the decision digest.

## Release workflow

`.github/workflows/pages.yml` runs `tools/verify_site.py`, `tools/check_site.py`, sitemap freshness, and generated-register freshness before deploying to GitHub Pages. On 2026-11-20 the same checks passed locally, including 24 HTML pages and 2,516 assertions. That is an internal repository check; it does not re-fetch Amazon listings or verify Associates account settings.

The checks enforce site structure, disclosures, sponsored-link marking, source references, price restrictions, data provenance, and generated-page consistency. Historical audit details and the supporting official policy links are on [`sources.html`](sources.html), [`citations.html`](citations.html), and [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md).

## Registers (current data as of 2026-11-19)

| Register | Page | Data | IDs |
|---|---|---|---|
| Suggestions | `suggestions.html` | `data/suggestions.json` | SG-01..SG-30 (SG-26 unassigned; SG-21 duplicates SG-20) |
| Open questions | `questions.html` | `data/open-questions.json` | Q-01..Q-21 |
| Decisions | `direction.html` | `DIRECTION.md` | dated rows |
| Flagged findings | `flagged.html` | `flagged.html` (FLG-001..FLG-019); `data/flagged.json` (F-01..F-21, not linked from any page) |
| Citation log | `citations.html` | `data/citations.json` | claim-to-source rows |

Each register has its own ID prefix so proposals, questions, decisions, and flagged findings are distinguishable.
