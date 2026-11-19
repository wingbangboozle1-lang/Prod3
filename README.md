# Prod3 — Kitchen Counter

**Kitchen Counter — Listed specs, plainly told.** A publication-style Amazon
affiliate site covering air fryers and meat thermometers. Tracking ID:
`shopnow047c-20` (owner-supplied; account eligibility unverified — FLG-010).
Published to GitHub Pages on merge to `main` (project site: https://wingbangboozle1-lang.github.io/Prod3/)

The 2026-11-19 audits (T-12 and the b84724ea compliance pass) set the claim
policy: specs and ratings are **seller statements from dated listing snapshots**,
attributed as such; accuracy/NIST wording is quoted as claim, never as test
result; **no prices are displayed at all** (Program Policies §2(b): price and
availability may be shown only from Amazon-served or PA-API data); the demo
email signup was removed. Release gates enforce these rules (banned phrases,
currency-amount ban, claim markers, sponsored coverage, canonicals, source-linked
data tables).

## Status at a glance

| | |
|---|---|
| Submitted tokens that are ASINs | 0 of 5 (they are 9-char short-link tokens; an ASIN is 10 chars) |
| Observed destinations | B0CDY277D3, B09B7SB46R, B08DKYBTPH, B0DHZTCNR5, B0DZFD6R9Z |
| Intended ASINs confirmed | 0 of 5 (blank until owner confirms — see FLG-001) |
| Pages | 21 HTML (front page, 2 pillars, compare, guide, 8 articles, 7 trust pages incl. analytics, 404 page — not in sitemap) |
| Gates | `tools/check_site.py`, `scripts/check_site.py`, `tools/verify_site.py` (non-zero exit on violation) |

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

- `index.html` — publication front page, buyer-first (question hero, five product cards with CTAs and source links, 3-question chooser, category tiles, seasonal guides, data table, RSS capture)
- `air-fryers.html`, `meat-thermometers.html` — category pillars
- `compare.html`, `buying-guide.html` — comparison + decision framework
- `articles/` — 8 question-shaped guides (also in `feed.xml` + `sitemap.xml`)
- `disclosure.html`, `sources.html`, `flagged.html`, `direction.html`, `executive-summary.html`, `about.html`, `analytics.html` — trust surfaces
- `data/` — `products.json` (intent vs observed, never merged), `sources.json`, `campaign-ledger.json` (empty until first-party reports)
- `assets/` — `style.css`, `app.js` (privacy-preserving measurement), `og-image.svg`, `favicon.svg`
- `COORDINATION.md` — shared task board · `DIRECTION.md` — suggestions + open questions + path chooser

## Release gates

Three checks run in `.github/workflows/pages.yml` before anything is deployed:

```bash
python3 scripts/check_site.py          # structure, disclosure presence, sitemap coverage
python3 tools/verify_site.py           # runs the above + feed, robots, ledger provenance
python3 tools/check_site.py            # complementary rules (see below)
python3 scripts/build_sitemap.py --check
```

`tools/check_site.py` exists because three defects reached the published site in its first
version and the earlier gates did not catch them:

| Rule | Defect it caught |
| --- | --- |
| `P10-no-price` | 40 currency amounts rendered on 8 pages while `disclosure.html` claimed the site stores no prices. Program Policies §2(b) permits price display only when Amazon serves the data. |
| `P07-sponsored` | The old check inspected only `link.amazon` hrefs, so 35 evidence links to `amazon.com/dp/<ASIN>` and 7 to the Associates help pages were unqualified. |
| `P01-disclosure` / `P02-disclosure-footer` | The exact Agreement §5 sentence was missing from all 20 pages; only paraphrases were present. |

It also enforces one `<h1>`, unique titles and descriptions, absolute canonicals, no first-hand
experience claims, no placeholders, descriptive link text, and that the campaign ledger stays empty
until a real first-party report exists.
