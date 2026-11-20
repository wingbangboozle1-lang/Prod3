# Executive Summary — Kitchen Counter

**Site:** Kitchen Counter — Listed specs, plainly told
**Tracking ID:** shopnow047c-20 (owner-supplied; account eligibility unverified — FLG-010)
**Date:** 2026-11-19 (T-12 audit revision; shop-polish pass T-17/T-18 same day) · **HTML mirror:** `executive-summary.html`

## What it is

A publication-style Amazon affiliate site covering two kitchen categories —
air fryers (3 products) and meat thermometers (2 products). The front page
leads with products, not process; every dashboard surface is reachable from
the footer and one navigation group. Eight question-shaped guides, a
comparison table, a buying guide, and a 3-question chooser help visitors
decide.

## What is sourced — and what is not (audit 2026-11-19)

- Specs and ratings are transcribed from dated official listing snapshots and
  cited to them (`data/sources.json`). They are **seller statements**, not
  independent Kitchen Counter tests. Prices are not displayed anywhere
  (Program Policies §2(b) — Amazon-served or PA-API data only); any price
  observations live solely in internal data files with date-only metadata
  (FLG-007/012).
- The five supplied `link.amazon` links were recorded as supplied. During the
  audit they resolved to listings B0CDY277D3, B09B7SB46R, B08DKYBTPH (Air
  Fryers) and B0DHZTCNR5, B0DZFD6R9Z (Meat Thermometers); observed
  destinations are kept separate from blank intended-ASIN fields (FLG-001).
  The `/dp/<token>` Page-Not-Found check was investigated and dismissed as
  link evidence (FLG-011).
- Policy and guidance pages cited: Amazon Operating Agreement (2025-10-15),
  Program Policies (2026-04-14), FTC Disclosures 101, Google
  `rel="sponsored"`, GitHub Pages docs, NIST metrological-traceability FAQ,
  USDA FSIS temperature and thermometer-placement guidance.
- Disclosure strip above the fold on every page with the required “As an
  Amazon Associate I earn from qualifying purchases.” statement plus
  conditional commission wording; `rel="sponsored"` + `noopener` on every
  Amazon link; absolute canonical URLs on every page (FLG-010 documents that
  account status is unverified).
- The demo email signup (fake confirmation) was removed; measurement is
  local-count only with no endpoint configured (FLG-014, `analytics.html`).

## What changed on 2026-11-19 (session a25ccde6)

- **Customer star ratings removed from every page.** Program Policies Participation
  Requirements §2(t) permits customer reviews and star ratings only when obtained
  through Creators API or PA API; the site uses neither. The comparison table now
  states the rule in the row where ratings used to be.
- **Eight dangling source citations repaired.** Data registers cited S07 and S08,
  which were never defined, so a reader could follow a citation to nothing.
- **Three registers replaced one ambiguous page.** `direction.html` carried SG-01..SG-08
  with meanings different from `data/suggestions.json`. Suggestions, open questions and
  decisions are now separate, generated pages with non-overlapping ID prefixes.
- **A citation log now backs every displayed figure** (`citations.html`).
- **Front page rebuilt** around product cards with typographic listing art, and a
  raster 1200×630 social preview; structured data added where it was missing.

## What is flagged (does not block)

- FLG-001: intended ASIN per short link unconfirmed (owner confirmation needed).
- FLG-002/003/013: three listing-internal conflicts (preset count; battery
  life + warranty; accessories count).
- FLG-004/005: two listings cross-promote other models.
- FLG-006: short-link compliance unresolved — test one Special Link per
  product before scaling. FLG-011: the `/dp/<token>` Page-Not-Found check was
  investigated and dismissed as link evidence.
- FLG-007/012: prices drift; snapshot metadata is date-only.
- FLG-008: no product photography used (compliant path).
- FLG-009: ThermoMaven accuracy/NIST wording is seller claim, not test.
- FLG-010: Associates account status unverified.
- FLG-014: email signup not connected. FLG-015: campaign ledger empty by design.
- FLG-016: SVG social-preview image unverified in share previewers (F-21).

## What happens next

Choose a path in `DIRECTION.md` / `direction.html`: steady publication
(weekly question-shaped guides, next topic chosen from measured Search Console
queries — SG-18), conversion focus (raster preview image, a real analytics
endpoint, a real email provider — SG-16/SG-04/SG-06), or hold until
FLG-001/006/010 are resolved. The retired “weekly price re-check” idea now
appears only as SG-17, which makes the Product Advertising API the single
compliant path to displayed prices. Measurement is privacy-preserving (four
events counted locally; `reader_signup` reserved for a confirmed provider
response; no endpoint configured) and the campaign ledger stays empty — rows
are added only from authorized first-party reports. No conversion score or
revenue forecast is presented.

## Shop-polish pass (T-17/T-18, 2026-11-19)

The reader-facing surface now leads with the shop, not the audit. The front
page opens on a buyer question (“Basket or oven? Instant-read or wireless?”),
followed by five product cards — seller-listed spec chips, an honest
“consider if” line, ratings dated at capture, a “Check price on Amazon” CTA,
and a source link under every card — then the chooser, seasonal guide row,
and the data table. Stylesheet: 44 px tap targets, visible focus states, card
lift on hover (mobile-first pass S-20 in effect). The RSS feed no longer
advertises a price range in the gift-guide description, and its channel title
drops the overstated channel title the audit flagged. The
Direction desk was rebuilt as a full ledger (SG-01…18 with statuses, Q-01…21
with discovery paths) and now matches `data/suggestions.json` /
`data/open-questions.json` exactly. New open item: FLG-016 / F-21 — the SVG
social-preview image is unverified in share previewers. All four release gates
pass on the rebuilt tree.


---

# Addendum — 2026-11-20, shop-first pass

**What this session did, in one paragraph.** The site was accurate and read like an audit.
It now reads like a shop without giving up a single compliance rule: a named starting pick on
the front page with a "look elsewhere if" that names the alternative; one navigation group plus
a second-level shelf, generated so it cannot drift; three working decision tools; a dated
seasonal guide; and a decision desk where every open choice, every unknown and three costed
paths sit on one page.

**Verified, not asserted.** The five supplied short links were re-fetched on 2026-11-20 and
resolved to the same five ASINs the register has recorded since 2026-11-19 — no drift. The
Amazon Program Policies were re-read the same day for the two clauses this pass leans on:
§2(b) on price display and Special Link tagging, and the IP License on product images. The
USDA FSIS safe-temperature chart (last updated 14 April 2025) and its probe-placement release
(19 September 2023) were fetched and the figures transcribed exactly, including the 92%
mis-placement finding in the FSIS test-kitchen study.

**A real defect, found and fixed.** `SG-20` and `SG-21` in `data/suggestions.json` were
byte-identical — the same "one identifier, two meanings" failure an earlier audit fixed
elsewhere. SG-21 was retired in place rather than deleted, so the change can be audited, and
gate rule `D20` now fails the build if any two live suggestions share a title.

**Nothing was softened.** No price is rendered anywhere. Every Amazon anchor is
`rel="sponsored"`. The exact §5 disclosure sentence appears in the strip and the footer of all
30 pages. Every new table row carries a source link or an explicit "No official source" marker,
and the gate fails a row that has neither — so "unverified" can never hide.

**Still true, still not this session's to fix.** The five short links carry no visible
`tag=shopnow047c-20`; the enrolled-account test has not been run (DT-01, FLG-006). There is no
analytics endpoint and no Search Console property (DT-03, DT-07). Every figure remains a seller
statement, because nothing has been purchased or tested (DT-05). These are owner actions with
minutes-scale costs, and they are published on `decisions.html` rather than buried here.

**Gates at close:** `build_chrome --check`, `build_registers --check`, `build_decisions --check`,
`build_sitemap --check`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`
(30 pages, 3541 assertions) and `tools/crawl_links.py` (30 pages, 0 broken links, 0 dead
anchors, 0 orphans) all pass on the merged tree.
