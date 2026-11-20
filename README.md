# Prod3 — Kitchen Counter

**Kitchen Counter — Listed specs, plainly told.** A publication-style Amazon affiliate site covering air fryers and meat thermometers. The owner-supplied tracking ID is `shopnow047c-20`; its assignment and account eligibility have not been verified (FLG-010).

**Published site:** https://wingbangboozle1-lang.github.io/Prod3/ · GitHub Pages deploys from `main`.

Product details are attributed as seller/listing statements, not independent tests. Customer ratings and prices are not displayed. Product snapshots and source checks recorded in the data files are dated; verify the current listing before relying on time-sensitive details. The five observed redirect destinations do not establish the owner's intended ASINs or prove Special Link compliance. Those fields are kept separate in `data/products.json` and unresolved findings appear on [`flagged.html`](flagged.html).

## Current status

| Item | Status |
|---|---|
| Products | 5 submitted short-link tokens; 5 observed destinations; intended ASIN/listing confirmation remains blank for all 5 |
| Pages | 39 HTML (front page, start page, 2 pillars, compare, buying guide, publishing plan, decision desk, ideas & review hub, 5 per-product spec pages, 4 tool pages, 10 articles, 10 trust pages, 404 — not in sitemap) |
| Intended ASINs confirmed | 0 of 5 (blank until owner confirms — see FLG-001) |
| Links | Four dated observations of the five supplied short links; the 2026-11-20 pass ended all five at the Amazon homepage (FLG-025). No shipped anchor carries a visible `tag=` parameter although Program Policies §2(b) require one (FLG-026) |
| Analytics | Five event types defined; four can be counted locally, none is sent to a server; no endpoint, Search Console property, or email provider configured |
| Campaign ledger | Empty by design; add data only from authorized first-party reports |
| Gates | `scripts/check_site.py`, `tools/check_site.py`, `tools/verify_site.py`, `tools/crawl_links.py`, plus four `--check` freshness gates for generated surfaces |

## Working with it

```sh
python3 scripts/build_chrome.py              # masthead, disclosure strip, footer into all 39 pages
python3 scripts/build_products.py            # one spec page per product from data/products.json
python3 scripts/build_products.py --check    # fail when a product page has drifted from the register
python3 scripts/build_decisions.py           # decisions.html from data/decisions.json + registers
python3 tools/crawl_links.py                 # internal links, anchors, orphans (exit 1)
python3 tools/verify_site.py                 # release gate: sources, ledger, feed, robots, core checks
python3 tools/check_site.py                  # complementary site assertions
python3 scripts/check_site.py                # product/data/HTML checks
python3 scripts/build_registers.py           # rebuild suggestions, questions, citations
python3 scripts/build_registers.py --check   # fail when the registers are stale
python3 scripts/build_sitemap.py             # regenerate sitemap.xml
python3 scripts/build_sitemap.py --check     # fail when the sitemap is stale
python3 scripts/build_chrome.py --check      # fail when any page's chrome has drifted
python3 scripts/build_decisions.py --check   # fail when the decision desk is stale
python3 tools/amazon_intake.py --link 'https://link.amazon/B04G1MEwY' --validate-only
python3 tools/amazon_intake.py --asin B0CDY277D3 --offline
```

The tools use Python's standard library; no third-party Python dependencies are required.

## Site map

- `index.html` — shop front: a named starting pick with a "look elsewhere if", the rest of the short list, the chooser, the seasonal block, all guides, the full data table
- `decisions.html` — **the decision desk.** Every open choice (DT-01..DT-12), every unanswered question (Q-01..Q-29) with what would settle it, the irregularities reproduced before repair, and a three-path chooser
- `tools/` — comparison builder, oven-to-air-fryer converter, USDA cook-to-temperature card
- `air-fryers.html`, `meat-thermometers.html` — category hubs
- `compare.html`, `buying-guide.html` — comparison and decision framework
- `products/` — five per-product spec pages, generated from `data/products.json` by `scripts/build_products.py`; each prints the listing's own contradictions and shows the blank intended-ASIN field as blank
- `publishing-plan.html` — twelve dated guide proposals from `data/editorial-plan.json`, with the evidence each needs and whether it exists
- `articles/` — thirteen question-shaped guides, included in `feed.xml` and `sitemap.xml`
- `suggestions.html`, `questions.html`, `direction.html` — proposals, missing-information questions, and decisions
- `sources.html`, `citations.html`, `flagged.html`, `disclosure.html`, `analytics.html`, `executive-summary.html`, `about.html` — source, disclosure, analytics, and trust pages
- `suggestions.html`, `questions.html`, and `citations.html` are generated from JSON by `scripts/build_registers.py`; `decisions.html` by `scripts/build_decisions.py`; the masthead/disclosure/footer of every page by `scripts/build_chrome.py`. Do not hand-edit any of them.
- `data/products.json` keeps intended product/link confirmation separate from observed redirect information; `data/sources.json` and `data/citations.json` hold source and claim mappings; `data/decisions.json` holds the decision desk rows; `data/campaign-ledger.json` is empty until authorized first-party reports exist.
- `assets/app.js` counts local browser events only; the self-hosted analytics endpoint is not configured. `assets/og-image.png` is the shipped 1200×630 social preview; external share-debugger rendering is not verified (F-21).
- `COORDINATION.md` is the task board; `DIRECTION.md` is the decision digest.

## Release workflow

`.github/workflows/pages.yml` runs the five `--check` freshness gates, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py` and `tools/crawl_links.py` before deploying to GitHub Pages. On 2026-11-20 the same checks passed locally, including 39 HTML pages and 5,879 assertions, with 0 broken links and 0 orphans. That is an internal repository check; it does not re-fetch Amazon listings or verify Associates account settings.

**Deploy path note (FLG-024):** this workflow is the only deployer the site has ever shipped through. The repo's Pages build type is still set to `legacy`, so a second, redundant "pages build and deployment" run also triggers on every push to `main` and can fail its deploy step behind the successful artifact deploy without affecting the live site. The automation token cannot change that setting (`PATCH /pages` → HTTP 404); the one-click owner fix is Settings → Pages → Build and deployment → Source: **GitHub Actions**. Judge deploys by the `Deploy GitHub Pages` workflow and the live URL.

The checks enforce site structure, disclosures, sponsored-link marking, source references, price restrictions, data provenance, and generated-page consistency. Historical audit details and the supporting official policy links are on [`sources.html`](sources.html), [`citations.html`](citations.html), and [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md).

## Registers (generated from the data files)

<!-- build-registers-table:start -->
| Register | Page | Data | IDs | Count |
|---|---|---|---|---|
| Suggestions | `suggestions.html` | `data/suggestions.json` | SG-01..SG-49 (SG-21 retired in place); unoccupied: SG-26 | 48 rows |
| Open questions | `questions.html` | `data/open-questions.json` | Q-01..Q-29 | 29 |
| Decisions to make | `decisions.html` | `data/decisions.json` | DT-01..DT-12 | 12 |
| Decisions taken | `direction.html` | `DIRECTION.md` | dated rows | - |
| Publishing plan | `publishing-plan.html` | `data/editorial-plan.json` | dated proposals | 12 |
| Flagged findings | `flagged.html` | `data/flagged.json` + callouts | FLG-017..FLG-040, F-01..F-21 | 36 in the data file |
| Citation log | `citations.html` | `data/citations.json` | claim-to-source rows | 21 |
<!-- build-registers-table:end -->

One table, not two. An earlier revision carried a 2026-11-19 table and a 2026-11-20 table side by
side whose ID ranges disagreed with each other and with the pages, and a later one hard-coded ranges
that went stale the moment another session added rows. The table above is now generated by
`scripts/build_readme.py` from the JSON registers, and the release gate fails if it drifts.

An ID prefix belongs to exactly one register. A proposal, a question and a decision
are never given the same identifier, so no reader has to guess which page is authoritative.

