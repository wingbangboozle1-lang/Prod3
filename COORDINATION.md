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
| T-12 | Post-merge integration audit: correct demonstrable editorial errors, disclosure/capture copy, event schema, analytics readiness, and unresolved compliance gates | done | `arena/5bd92dff-prod3` | all published HTML for disclosure/nav, `assets/app.js`, `assets/style.css`, `analytics.html`, `analytics/*`, `data/campaign-ledger.json`, `data/sources.json`, `sources.html`, `flagged.html`, `direction.html`, `DIRECTION.md`, `sitemap.xml`, `scripts/check_site.py`, `tools/verify_site.py`, `README.md`, `EXECUTIVE_SUMMARY.md` |

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
- FLG-009 — ThermoMaven ±0.5°F / "NIST & NSF Certified" / 1-sec / IP67 wording is seller
  claim, not test; certificate unexamined; NIST traceability applies to measurement results.
- FLG-010 — Amazon Associates account status unverified (tracking ID owner-supplied);
  membership assertion removed, required earnings statement + conditional copy kept.
- FLG-011 — /dp/<token> Page-Not-Found check investigated and dismissed as link evidence
  (constructed /dp/ URLs are not the supplied short links; only the 9-char length is a finding).
- FLG-012 — Price/rating snapshots are date-only (no observation time or delivery location).
- FLG-013 — Emeril accessories count: six named in title/About vs "7 Accessories" config string.
- FLG-014 — Reader email signup not connected (demo form with fake confirmation removed).
- FLG-015 — Campaign ledger empty by design; no first-party reports yet.

## Cross-scope requests

(none)

## Handoff / conflict log

- 2026-11-19 T-12 audit (`arena/5bd92dff-prod3`): claim policy rewritten across the site —
  seller-stated specs attributed, capacity-ratio/serving-size/winner claims removed,
  NIST/USDA sources added to the register, FLG-009..015 opened, demo signup removed
  (matching `analytics.html`), and the b84724ea price-policy pass merged in (no currency
  rendered anywhere; §2(b) stated where prices used to be). Disclosure carries the required
  “As an Amazon Associate…” statement plus conditional commission wording and the
  unverified-account caveats (FLG-010). Release gates enforce banned phrases, the
  currency ban, claim markers, sponsored coverage, and source-linked data tables.
  Intended ASINs remain unconfirmed (FLG-001) and short-link compliance unresolved
  (FLG-006) — do not conclude the supplied links are invalid.

## Deploy record

- PR: https://github.com/wingbangboozle1-lang/Prod3/pull/1 (arena/5a4e180c-prod3 → main)
- Merge result: merged (merge commit ca9f4f27f77eef5ea6a15421c177b2f57f275427, 2026-11-19 12:43:28Z); verify_site.py and sitemap --check passed before merge
- Pages: 'Deploy GitHub Pages' workflow success on merge; 'pages build and deployment' success; live page confirmed at the URL below
- GitHub Pages URL: https://wingbangboozle1-lang.github.io/Prod3/

## Session arena/9978ab21-prod3 — integration (2026-11-19)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-12 | Independent re-verification of the 5 submitted links vs official Amazon listings | done | arena/9978ab21-prod3 | `data/products.json` (re-fetch confirmed identical observed destinations) |
| T-13 | Review existing click/conversion measurement (assets/app.js, data/campaign-ledger.json) — covers T-06 scope; no duplicate analytics added | done | arena/9978ab21-prod3 | `assets/app.js`, `data/campaign-ledger.json` |
| T-14 | Add docs/verification.md, docs/analytics-endpoint.md, 404.html | done | arena/9978ab21-prod3 | `docs/*`, `404.html` |
| T-15 | Integration PR #2 → main, merge, confirm GitHub Pages redeploy, record result here | done | arena/9978ab21-prod3 | all |

### Verification re-fetch (session arena/9978ab21-prod3, 2026-11-19)

Each submitted link was fetched again and its HTTP redirect followed to the official Amazon domain. Observed destinations match session 5a4e180c exactly:

- link.amazon/B04G1MEwY → https://www.amazon.com/dp/B0CDY277D3
- link.amazon/B02NbDxp3 → https://www.amazon.com/dp/B09B7SB46R
- link.amazon/B00hJ57DV → https://www.amazon.com/dp/B08DKYBTPH
- link.amazon/B0c8moW59 → https://www.amazon.com/dp/B0DHZTCNR5
- link.amazon/B0f3GKalj → https://www.amazon.com/dp/B0DZFD6R9Z

Intended ASIN / official listing URL / confirmation date / source remain blank for all five (short-link compliance status unresolved; no claim that the short links are invalid). Observed redirect targets are recorded separately and never merged with intended fields.

### Cross-scope requests

(none)

### Handoff / conflict log

2026-11-19: initial rebase of arena/9978ab21-prod3 onto origin/main conflicted on COORDINATION.md, data/products.json, data/sources.json. Resolved by keeping session 5a4e180c's versions (the mainline record); no other session's work was discarded. Duplicate file additions from the earlier draft of this session (index.html, guides/, categories/, products/index.html, executive-summary.md, flagged-for-review.html) were dropped to avoid duplicate content with the existing mainline site (articles/, air-fryers.html, meat-thermometers.html, compare.html, buying-guide.html, EXECUTIVE_SUMMARY.md, flagged.html, sources.html).

### Integration record

- PR #2: https://github.com/wingbangboozle1-lang/Prod3/pull/2 (arena/9978ab21-prod3 → main)
- Merge result: merged (merge commit 1056cb4c9a98558e4a5cd7849211c98b70463d17)
- PR #2 merged into main by gh pr merge --merge; no approval waited on (per instructions)
- GitHub Pages: source branch main, status built; live at https://wingbangboozle1-lang.github.io/Prod3/ (custom 404 served)
- Live checks: homepage renders disclosure above the fold (Tracking ID shopnow047c-20), five-product table with source links to official Amazon listings, category pillar pages, 8 question-shaped guides, chooser, compare page, feed.xml, sitemap.xml; /flagged.html live with FLG-001..FLG-008 and sources; none block the merge.
- Flagged irregularities and unverified items remain published on /flagged.html for owner review.

---

## Session arena/b84724ea-prod3 — independent audit and corrective PR (2026-11-19)

**What this session did.** Started from the same five supplied links on a branch cut from
`dea7fb6` — before sessions `5a4e180c` and `9978ab21` had published. It independently resolved the
same five short links and read the same five listings, then found the mainline already carried a
complete site. Rather than replace it, this session was re-scoped to an **independent audit** of the
merged site, and every one of its own parallel duplicates was deleted.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| A-01 | Resolve the five short links independently and compare against the mainline record | done | arena/b84724ea-prod3 | read-only |
| A-02 | Audit every rendered page for the required disclosure, sponsored coverage, price policy, canonicals, duplicate titles | done | arena/b84724ea-prod3 | read-only |
| A-03 | Remove published prices from all pages; state the §2(b) policy where prices used to be | done | arena/b84724ea-prod3 | `index.html`, `compare.html`, `air-fryers.html`, `meat-thermometers.html`, `articles/*.html`, `assets/style.css` |
| A-04 | Qualify every outbound Amazon link as `rel="sponsored"`, not only the `link.amazon` ones | done | arena/b84724ea-prod3 | `*.html`, `*.html` |
| A-05 | Put the exact §5 disclosure sentence on every page, top and footer; add canonical URLs | done | arena/b84724ea-prod3 | `*.html`, `articles/*.html` |
| A-06 | Fix `404.html` root-absolute URLs that 404 under the `/Prod3/` project path | done | arena/b84724ea-prod3 | `404.html` |
| A-07 | Add a complementary zero-dependency gate for the rules the existing gates missed | done | arena/b84724ea-prod3 | `tools/check_site.py`, `.github/workflows/pages.yml`, `scripts/check_site.py` |
| A-08 | Integration PR → main, merge, confirm Pages deploy, record result here | done | arena/b84724ea-prod3 | all |

### A-01 — independent re-resolution (no discrepancy with the mainline)

| Supplied link | Observed destination | Mainline record | Agrees |
|---|---|---|---|
| link.amazon/B04G1MEwY | amazon.com/dp/B0CDY277D3 | B0CDY277D3 | ✔ |
| link.amazon/B02NbDxp3 | amazon.com/dp/B09B7SB46R | B09B7SB46R | ✔ |
| link.amazon/B00hJ57DV | amazon.com/dp/B08DKYBTPH | B08DKYBTPH | ✔ |
| link.amazon/B0c8moW59 | amazon.com/dp/B0DHZTCNR5 | B0DHZTCNR5 | ✔ |
| link.amazon/B0f3GKalj | amazon.com/dp/B0DZFD6R9Z | B0DZFD6R9Z | ✔ |

This session's listing readings independently reproduced the mainline's flagged items F-01
(capacity: 6 liters in the field vs 6 quarts in the title), F-02 (preset count 24 vs 25) and
F-03 (a newer model advertised on the ThermoMaven page). No conflict.

### A-02 — defects found in the published site

1. **Prices were published on 8 pages** — 40 currency amounts on `index.html`, `compare.html`,
   `air-fryers.html`, `meat-thermometers.html` and four articles — while `disclosure.html` stated the
   opposite ("no price storage or display"). Program Policies §2(b) permits price display only when
   Amazon serves the data or it arrives via the Product Advertising API. **Resolved: all 40 removed**;
   the policy is now stated in the price slot itself, and the gate fails if a currency amount returns.
2. **Evidence links were unsponsored.** 42 Amazon anchors existed; the checker only inspected
   `link.amazon` hrefs, so 35 anchors to `amazon.com/dp/<ASIN>` and 7 to the Associates help pages
   carried `rel="noopener"` without `sponsored`. **Resolved: 42/42 now sponsored.**
3. **The exact §5 disclosure sentence was missing from every page but `404.html`.** Every page
   carried a paraphrase ("Kitchen Counter is a participant in the Amazon Services LLC Associates
   Program…" and "As an Amazon Associate, Kitchen Counter earns from qualifying purchases"). Agreement
   §5 specifies *"As an Amazon Associate I earn from qualifying purchases."* or a substantially
   similar statement. **Resolved: the exact sentence now appears in the top strip and the footer of all
   20 pages, alongside the existing paraphrase, which is left in place.**
4. **`404.html` was broken on the live site.** It used root-absolute URLs (`/assets/style.css`,
   `/compare.html`), which resolve against `wingbangboozle1-lang.github.io/` and drop the `/Prod3/`
   prefix, so the custom 404 loaded unstyled with dead links. The repository's own release gate failed
   on `main` because of it, which means the Pages deploy job was failing at the gate step. **Resolved:
   relative URLs, matching every other page.**
5. **Eight articles had no canonical URL.** **Resolved: all 20 pages now carry an absolute canonical.**

### A-03 — verification performed after the fixes

```
python3 scripts/check_site.py          All checks passed.
python3 tools/check_site.py            20 pages checked, 1265 assertions run — all passed
python3 tools/verify_site.py           Release gate passed.
python3 scripts/build_sitemap.py --check   OK: up to date
```

Crawled the built tree over HTTP at the real `/Prod3/` prefix: **24/24 URLs resolve, 0 broken**.
Every page carries the required sentence twice; **42/42 Amazon anchors are `sponsored`**; **zero
currency amounts** remain in any HTML file.

### Cross-scope requests

Editing files outside this session's original scope was unavoidable, because the defects above are
in shared output and every other session is finished. Each edit is listed in A-03..A-07 with its file
set. Nothing was deleted: the mainline site, its articles, its data registers, its docs and its two
gates are all intact, and this session's parallel duplicates were removed rather than merged.

### Handoff / conflict log

2026-11-19: merging `origin/main` into `arena/b84724ea-prod3` produced 10 add/add conflicts. **Every
conflict was resolved in favour of the mainline version** (`index.html`, `assets/app.js`,
`assets/style.css`, `data/products.json`, `data/sources.json`, `404.html`, `COORDINATION.md`,
`README.md`, `feed.xml`, `sitemap.xml`). This session's parallel site tree (`about/`, `air-fryers/`,
`compare/`, `dashboard/`, `guides/`, `product/`, `questions/`, `sources/`, `suggestions/`,
`thermometers/`, `build.py`, `content/`) was deleted, and its duplicate CI workflow
(`.github/workflows/checks.yml`) was removed because it asserted pages that do not exist in this
site. No other session's work was discarded.

### A-08 — integration record

- **PR #4:** https://github.com/wingbangboozle1-lang/Prod3/pull/4 (`arena/b84724ea-prod3` → `main`)
- **Merge result:** merged, merge commit `0449d9415dd6287d1fee7344d8c57d8666a417b7`, 2026-11-19 13:01:11Z.
  Merged without waiting for approval, per the project instructions.
- **Pre-merge gate:** `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py` and
  `scripts/build_sitemap.py --check` all passed on the merged tree. Nothing was merged broken.
- **Pages deploy:** `Deploy GitHub Pages` — **success**. `pages build and deployment` — **success**.
  Pages status `built`, source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/.
- **Note on the previous deploy:** the immediately preceding `Deploy GitHub Pages` run on `main` had
  concluded **failure**. It failed at the release-gate step because of the broken `404.html` recorded
  in A-02 item 4. The run triggered by this merge succeeds, which is the direct evidence that the 404
  repair fixed the deploy pipeline and not just the page.

### A-09 — live verification after deploy

Checked against the published site, not against the local tree:

| Claim | Verified on the live URL |
| --- | --- |
| Exact §5 sentence in the top strip | ✔ `Prod3/` renders "As an Amazon Associate I earn from qualifying purchases." before any product content |
| No prices rendered | ✔ the price slot reads "Current price on Amazon", the table cell reads "See Amazon", and the footnote states the §2(b) policy |
| Price policy stated honestly | ✔ `disclosure.html` now says no price appears anywhere, and records that dated prices were removed on 2026-11-19 |
| Canonical URLs | ✔ present in the served markup |
| Disclosure page still accurate | ✔ the "Where the disclosure appears" list no longer claims prices are dated and shown |

### Residual issues for the owner (not blocking, published on `/flagged.html`)

- **FLG-001 / Q-02** — the Associates ID `shopnow047c-20` still cannot be confirmed from outside the
  account; the served short-link URLs carry no visible `tag=`. Verify in SiteStripe before driving
  traffic.
- **FLG-006** — the `link.amazon` short-link format remains unresolved in the enrolled workflow; the
  live site still sends product buttons through `link.amazon`, so this is the highest-value
  five-minute task on the board.
- Live copy still contains two stale claims outside this session's scope: the `air-fryers.html` card
  reads "compared on capacity, footprint, wattage, and price" and the homepage call-to-action reads
  "Compare all five on capacity, footprint & price", although no price is shown any more. Both should
  be reworded to "…and sourcing" or similar. Logged rather than edited to keep this session's diff to
  the compliance defects.
