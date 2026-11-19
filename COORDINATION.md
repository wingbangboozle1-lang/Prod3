# COORDINATION.md — Shared Task Board

**Repo:** wingbangboozle1-lang/Prod3
**Session ID:** `5a4e180c` (branch `arena/5a4e180c-prod3`)
**Tracking ID:** `shopnow047c-20` (Amazon Associates, as supplied)
**Last updated:** 2026-11-19

## How this board works

- Each task lists: status (`unclaimed` / `in progress` / `done` / `needs review`),
  owning session ID, and file scope.
- `needs review` = published on the Flagged for Review page; does not block anything.
- Claim a task by writing your session ID + file scope here, then commit + push immediately.
- Never edit a file owned by another session. Log cross-scope requests below instead.
- Run `git pull --rebase` before every push. Small, frequent commits.
- A claim older than 60 minutes with no commits may be taken over (note the handoff).

## Task board

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-01 | Verify 5 submitted links line-by-line vs official Amazon listings | done | 5a4e180c | `data/products.json`, `data/sources.json` |
| T-02 | Build product-intent confirmation record (intent vs observed, separate fields) | done | 5a4e180c | `data/products.json` |
| T-03 | Build publication-style site (front page, categories, compare, guides) | done | 5a4e180c | `index.html`, `air-fryers.html`, `meat-thermometers.html`, `compare.html`, `buying-guide.html`, `assets/*` |
| T-04 | Publish 8 question-shaped articles + RSS feed + sitemap | done | 5a4e180c | `articles/*`, `feed.xml`, `sitemap.xml` |
| T-05 | Disclosure strip above the fold on every page; `rel="sponsored"` on all outbound links | done | 5a4e180c | all `*.html` |
| T-06 | Click/conversion measurement (privacy-preserving, 5 defined events) | done | 5a4e180c | `assets/app.js`, `data/campaign-ledger.json` |
| T-07 | Flagged for Review page + source register with official links | done | 5a4e180c | `flagged.html`, `sources.html` |
| T-08 | Direction section: suggestions, open questions, path chooser | done | 5a4e180c | `direction.html`, `DIRECTION.md` |
| T-09 | Executive summary | done | 5a4e180c | `executive-summary.html`, `EXECUTIVE_SUMMARY.md` |
| T-10 | Gates: `scripts/check_site.py`, `tools/verify_site.py`, link check | done | 5a4e180c | `scripts/*`, `tools/*` |
| T-11 | GitHub Pages deploy + PR to main + merge | done | 5a4e180c | `.github/workflows/pages.yml` |

## Verification log (2026-11-19, session 5a4e180c)

All five submitted `link.amazon` tokens were checked against official Amazon pages
via direct fetch. Findings (full detail in `data/products.json`):

| Submitted link | Token length | `amazon.com/dp/<token>` | Observed destination (ASIN) | Category (browse node) |
|---|---|---|---|---|
| link.amazon/B04G1MEwY | 9 chars | Page Not Found | B0CDY277D3 | Air Fryers (17659096011) |
| link.amazon/B02NbDxp3 | 9 chars | Page Not Found | B09B7SB46R | Air Fryers (17659096011) |
| link.amazon/B00hJ57DV | 9 chars | Page Not Found | B08DKYBTPH | Air Fryers (17659096011) |
| link.amazon/B0c8moW59 | 9 chars | Page Not Found | B0DHZTCNR5 | Meat Thermometers (289810) |
| link.amazon/B0f3GKalj | 9 chars | Page Not Found | B0DZFD6R9Z | Meat Thermometers (289810) |

- An ASIN is a 10-character code (Amazon Associates / Creators API definition).
  A 9-character token cannot be an ASIN. The tokens are short-link codes.
- Intended ASIN / official listing URL / confirmation date / source are **blank**
  for all five (nothing public binds a short code to a product intent).
  Observed redirect targets are recorded separately and never merged.
- Official sources re-read live 2026-11-19: Operating Agreement (updated
  2025-10-15), Program Policies (updated 2026-04-14), FTC Disclosures 101,
  Google `rel="sponsored"` guidance, GitHub Pages docs. See `data/sources.json`.

## Flagged irregularities (published on `flagged.html`, do not block)

- FLG-001 — Intended product for each short link is unconfirmed (owner confirmation needed).
- FLG-002 — Emeril preset count: 24 (title) vs 25 (About this item) on the same listing.
- FLG-003 — CHEF iQ battery life: 50 h (About) vs 70 h (Product Description); warranty 2 yr vs 3 yr.
- FLG-004 — Chefman 8 QT (B08DKYBTPH) has a newer model B0CNY1YVDD listed on its page.
- FLG-005 — ThermoMaven (B0DHZTCNR5) has a newer model B0GL7Z4KP4 listed on its page.
- FLG-006 — Short-link compliance status unresolved; test one Special Link per product
  in the enrolled Associates workflow before scaling. Do **not** claim the short links are invalid.
- FLG-007 — Prices observed 2026-11-19 will drift; always verify on Amazon before purchase.
- FLG-008 — No product photography used (Operating Agreement §1: Program Content
  includes images; only Amazon-provided images may be used). Site uses CSS/SVG art.

## Cross-scope requests

(none)

## Handoff / conflict log

(none)

## Deploy record

- PR: https://github.com/wingbangboozle1-lang/Prod3/pull/1 (arena/5a4e180c-prod3 → main)
- Merge result: merged (merge commit ca9f4f27f77eef5ea6a15421c177b2f57f275427, 2026-11-19 12:43:28Z); verify_site.py and sitemap --check passed before merge
- Pages: 'Deploy GitHub Pages' workflow success on merge; 'pages build and deployment' success; live page confirmed at the URL below
- GitHub Pages URL: https://wingbangboozle1-lang.github.io/Prod3/
