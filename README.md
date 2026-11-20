# Prod3 — Kitchen Counter

**Kitchen Counter — Listed specs, plainly told.** A publication-style Amazon
affiliate site covering air fryers and meat thermometers. Tracking ID:
`shopnow047c-20` (owner-supplied; account eligibility unverified — FLG-010).
Published to GitHub Pages on merge to `main` (project site: https://wingbangboozle1-lang.github.io/Prod3/)

The 2026-11-19 audits (T-12 and the b84724ea compliance pass) set the claim
policy: specs are **seller statements from dated listing snapshots**,
attributed as such; accuracy/NIST wording is quoted as claim, never as test
result; **no prices are displayed at all** (Program Policies §2(b): price and
availability may be shown only from Amazon-served or PA-API data); the demo
email signup was removed. A third audit (session a25ccde6) removed customer star
ratings entirely — Program Policies §2(t) allows them only from Creators/PA API
data — and added a citation log so every rendered figure has a dated source.
Release gates enforce these rules (banned phrases,
currency-amount ban, claim markers, sponsored coverage, canonicals, source-linked
data tables).

## Status at a glance

| | |
|---|---|
| Submitted tokens that are ASINs | 0 of 5 (they are 9-char short-link tokens; an ASIN is 10 chars) |
| Observed destinations | B0CDY277D3, B09B7SB46R, B08DKYBTPH, B0DHZTCNR5, B0DZFD6R9Z |
| Intended ASINs confirmed | 0 of 5 (blank until owner confirms — see FLG-001) |
| Pages | 30 HTML (front page, 2 pillars, compare, buying guide, decision desk, 4 tool pages, 9 articles, 10 trust pages, 404 — not in sitemap) |
| Gates | `tools/check_site.py`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/crawl_links.py`, plus four `--check` freshness gates for generated surfaces |

## Working with it

```
python3 scripts/build_chrome.py         # masthead, disclosure strip, footer into all 30 pages
python3 scripts/build_decisions.py      # decisions.html from data/decisions.json + registers
python3 tools/crawl_links.py            # internal links, anchors, orphans (exit 1)
python3 tools/verify_site.py            # whole-tree release gate (exit 3 on violation)
python3 scripts/build_registers.py      # rebuild suggestions.html, questions.html, citations.html
python3 scripts/build_registers.py --check  # exit 1 if a register is stale
python3 scripts/check_site.py           # data + HTML gate (exit 1 on violation)
python3 scripts/build_sitemap.py        # rewrite sitemap.xml from the tree
python3 scripts/build_sitemap.py --check # exit 1 if sitemap is stale
python3 tools/amazon_intake.py --link 'https://link.amazon/B04G1MEwY' --validate-only
python3 tools/amazon_intake.py --asin B0CDY277D3 --offline   # exit 0, queued for API
```

No third-party dependencies: the standard library only.

## Layout

- `index.html` — shop front: a named starting pick with a "look elsewhere if", the rest of the short list, the 3-question chooser, the seasonal block, all guides, the full data table
- `decisions.html` — **the decision desk.** Every open choice (DT-01..DT-10), every unanswered question (Q-01..Q-21) with what would settle it, the irregularities reproduced before repair, and a three-path chooser
- `tools/` — comparison builder, oven-to-air-fryer converter, USDA cook-to-temperature card
- `air-fryers.html`, `meat-thermometers.html` — category pillars
- `compare.html`, `buying-guide.html` — comparison + decision framework
- `articles/` — 8 question-shaped guides (also in `feed.xml` + `sitemap.xml`)
- `disclosure.html`, `sources.html`, `citations.html`, `flagged.html`, `suggestions.html`, `questions.html`, `direction.html`, `executive-summary.html`, `about.html`, `analytics.html` — trust surfaces
- `suggestions.html` / `questions.html` / `citations.html` are **generated** from `data/*.json` by `scripts/build_registers.py`; do not hand-edit them
- `assets/product-art/` — typographic listing cards rendered from each product's own numbers (no photography)
- `data/` — `products.json` (intent vs observed, never merged), `sources.json`, `campaign-ledger.json` (empty until first-party reports)
- `assets/` — `style.css`, `app.js` (privacy-preserving measurement), `og-image.svg`, `favicon.svg`
- `data/citations.json` — one row per rendered figure, with its observation date and source
- `scripts/build_chrome.py` — single source of truth for masthead, disclosure strip and footer; the article body is never touched
- `COORDINATION.md` — shared task board · `DIRECTION.md` — decision digest + pointers to the registers

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

## Registers (as of 2026-11-19, session a25ccde6)

| Register | Page | Data | IDs |
|---|---|---|---|
| Suggestions | `suggestions.html` | `data/suggestions.json` | SG-01..SG-20 |
| Open questions | `questions.html` | `data/open-questions.json` | Q-01..Q-17 |
| Decisions | `direction.html` | `DIRECTION.md` | dated rows |
| Flagged irregularities | `flagged.html` | `data/flagged.json` | FLG-001..FLG-015, F-01..F-20 |
| Citation log | `citations.html` | `data/citations.json` | one row per figure |

An ID prefix belongs to exactly one register. A proposal, a question and a decision
are never given the same identifier, so no reader has to guess which page is authoritative.


## What changed in the 2026-11-20 shop-first pass

The site was accurate but read like an audit. It now reads like a shop, without giving up a
single compliance rule. Concretely:

| Change | Before | After |
|---|---|---|
| Front page | six-paragraph method statement above the products | a named starting pick ("Start here if…"), a "look elsewhere if" that names the alternative, then the rest of the list |
| Navigation | six top-level labels, active state on 9 of 24 pages | one group of six, a second-level shelf, active state on all 30 pages, generated so it cannot drift |
| Decision surfaces | suggestions, questions and decisions in three separate registers | one decision desk that summarises all three, plus a path chooser and an explicit "no official source" marker |
| Seasonal | a static gift-guide tile | a dated seasonal block that leads with the guide the calendar makes urgent this week |
| Tools | none | comparison builder, oven converter, USDA card — the three questions buyers get stuck on |
| Duplicate proposal | `SG-20` and `SG-21` were byte-identical | SG-21 retired in place, gate rule `D20` prevents a recurrence |

Nothing was softened: no price is rendered, every Amazon anchor is still `rel="sponsored"`,
the exact §5 disclosure sentence still appears in the strip and the footer of every page, and
every new table row carries a source link or an explicit "no official source" marker.
