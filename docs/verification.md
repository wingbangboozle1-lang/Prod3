# Verification record

Sessions: `arena/5a4e180c-prod3` (build, merged via PR #1), `arena/9978ab21-prod3` (integration, merged via PR #2), and `arena/28d2d6c0-prod3` (T-23 line-by-line re-verification, 2026-11-19) · Date: 2026-11-19

## Method

Every source was fetched from its official domain and read line by line. No value was inferred, and nothing was filled in from assumption. Where a value cannot be confirmed from an official source, it is left blank/null and flagged. Product pages were reached by following the submitted short links; only the redirect target and page title were recorded.

## Official sources used

| Source | URL | Used for |
|---|---|---|
| Amazon Associates Program Operating Agreement | https://affiliate-program.amazon.com/help/operating/agreement | Special Links definition, Program Content scope, compliance requirements |
| Amazon Associates Program Policies | https://affiliate-program.amazon.com/help/operating/policies | Qualifying/disqualified purchases, commission statement |
| FTC Disclosures 101 for Social Media Influencers | https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers | Disclosure placement and plain language |
| FTC Endorsement Guides | https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews | Endorsement context |
| Google Search Central: Qualify outbound links | https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links | `rel="sponsored"` on affiliate links |
| Google Search Central: Meta descriptions | https://developers.google.com/search/docs/appearance/snippet | Unique title + description per page |
| Google Search Central: Helpful, people-first content | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | Editorial standard |
| GitHub Pages | https://docs.github.com/pages | Publishing |
| Google — Lighthouse tap targets (S19) | https://developer.chrome.com/docs/lighthouse/seo/tap-targets | Mobile-first pass (S-20): 48×48px tap targets, ~8px spacing |

## Product-intent confirmation records

See `data/products.json`. Each submitted short link was fetched and its redirect followed (independent re-fetch by session `arena/9978ab21-prod3`, 2026-11-19 — same observed destinations as session `5a4e180c`):

- https://link.amazon/B04G1MEwY → https://www.amazon.com/dp/B0CDY277D3
- https://link.amazon/B02NbDxp3 → https://www.amazon.com/dp/B09B7SB46R
- https://link.amazon/B00hJ57DV → https://www.amazon.com/dp/B08DKYBTPH
- https://link.amazon/B0c8moW59 → https://www.amazon.com/dp/B0DHZTCNR5
- https://link.amazon/B0f3GKalj → https://www.amazon.com/dp/B0DZFD6R9Z

The intended ASIN (short-link path code) and confirmed/observed ASIN (redirect destination) are stored in separate fields and never merged. Intended fields stay null until the owner confirms in the Associates workflow. Short-link compliance status is unresolved; no claim is made that the supplied short links are invalid (see FLG-006).

## Flagged irregularities

See `data/flagged.json` (F-series), `flagged.html` (FLG-series) and `/flagged.html`. None block the merge.

## Mobile-first tap-target pass (S-20, session 65474d4f, 2026-11-19)

Scope: `assets/style.css` only — hit-area sizing. No copy, link, or data value changed, so nothing here
needed a new product-source check; the one guidance source (Google tap targets, S19) was fetched from
`developer.chrome.com` and recorded in `data/sources.json` and `sources.html`.

What was done, against the Google rule ("Tap targets that are 48 px by 48 px never fail the audit",
~8px spacing):

- Every `.nav a`, `.btn`, chooser `.chooser button`, the sticky-bar link and the skip link get a
  `min-height` of 44px on wide screens and 48px at `max-width:600px`, using padding so appearance is
  unchanged (Google's own recommended fix).
- Existing flex `gap` values (8–18px) already meet the ≥8px spacing recommendation, so no spacing was
  added that would push controls further apart than the guideline suggests.
- At `max-width:600px` product CTAs become full-width (`width:100%`) thumb targets and body text floors
  at 16px (the size iOS Safari uses to decide whether to zoom on focus).

### Q-15 — disclosure above the fold at 320px

Verified **structurally**, not in a browser: `tools/check_site.py` `P01-disclosure-position` fails any
page where the disclosure marker does not occur before the first `<h1>`, so on all 24 pages the strip
precedes every heading and product button in reading order, and it is a normal full-width block (not
positioned after the hero), so it is not reordered on a narrow screen. The S-20 pass keeps the strip
compact at `<=600px` (`.disclosure` 0.8rem) so it cannot grow past the fold. A physical pixel measurement
in a real browser at 320px with an enlarged system font was **not** run from this sandbox (see the
matching note on Q-15 in `data/open-questions.json`); that remains a one-time owner/browser check.

## T-23 line-by-line re-verification (session `arena/28d2d6c0-prod3`, 2026-11-19)

Every official source in `data/sources.json` was re-fetched and read on 2026-11-19:

| Checked | Result |
|---|---|
| All five `link.amazon` short links | Resolve to B0CDY277D3, B09B7SB46R, B08DKYBTPH, B0DHZTCNR5, B0DZFD6R9Z; all five live page titles match `observed_title` in `data/products.json` exactly |
| Browse nodes | Air Fryers `17659096011` and Meat Thermometers `289810` confirmed in the live breadcrumbs |
| FLG-002 (Emeril presets) | Confirmed live: title reads "24 One-Touch Preset Options"; the About-this-item bullet reads "25 COOKING PRE-SETS" |
| FLG-004 / FLG-005 (newer models) | B0CNY1YVDD visible on the Chefman 8 Qt page; B0GL7Z4KP4 visible on the ThermoMaven page |
| P-02 listed specs | Dimensions 16.9"D x 15.8"W x 14.8"H, capacity 24.6 L, special features, material and color match the live product table |
| Operating Agreement | "Updated: October 15, 2025"; §1 Special Links quote, §5 exact statement ("As an Amazon Associate I earn from qualifying purchases." or any substantially similar statement) and §6 material-breach clause verified verbatim |
| Program Policies | "Updated: April 14, 2026"; Qualifying-Purchase quote verified verbatim |
| FTC Disclosures 101 | "Place it so it's hard to miss…" verified verbatim; page dated November 2019 |
| Google rel="sponsored" guidance | Quote verified verbatim; "Last updated 2025-12-10 UTC" |
| Google people-first content | Self-assessment questions verified verbatim |
| Google spam policies | "Thin affiliation" section verified verbatim (including the good-affiliate-pages sentence) |
| Amazon Creators API `ItemIdType` | "Amazon Standard Identification Number: 10-Character alphanumeric unique identifier assigned by Amazon" — the official basis for the 10-character ASIN figure |

Corrections made under T-23 (all gates re-run green afterwards):

- `data/sources.json` S06 now cites the Creators API `ItemIdType` table (the old citation pointed at
  the Program Policies page, which does not carry the definition); S21/S22 quotes corrected to
  verbatim page text.
- Stale pre-revision source IDs removed/remapped across `data/analysis.json`, `data/flagged.json`
  and `data/policy-checks.json` (including C-08 → S22, C-09 → S02+S06, C-12 → S21+S25,
  C-14 → S21, which had been cited to Amazon listing pages).
- `sources.html` now publishes every registered source (S06, S21–S25 rows added).
- `data/citations.json` gained rows for the rendered S05/S06/S15/S19/S23 figures; the
  page-experience row re-attributed from S21 to S25.
- New release gate in `tools/verify_site.py`: every source ID referenced from `data/*.json` must
  resolve to `data/sources.json`, and every registered source must appear on `sources.html`
  (negative-tested: exit 3 on an undefined ID).

## T-26 intent-provenance and policy-copy correction (session `arena/e83cdf55-prod3`, 2026-11-20)

- **Defect found:** `data/verification.json` (2026-11-19) copied each observed redirect ASIN into `intended.asin`, cited S16 (the NIST traceability FAQ) as the intent source, and set `agrees: true`. Intent cannot be inferred from a redirect, and S16 does not mention any ASIN.
- **Correction:** all five `intended` fields are now null. `observed.*` values are unchanged. `agrees` is replaced by `comparison_to_intent: "not performed"`. Recorded under `correction_2026_11_20` in that file (FLG-018).
- **Defect found:** policy check C-04 said product buttons go directly to `amazon.com/dp/<ASIN>`. The built HTML has 25 buttons to the supplied `link.amazon` URLs and 138 separate `/dp/` source links, all `rel="sponsored noopener"`. C-04 and C-09 are corrected to status `partial` with the actual evidence (FLG-019).
- **Gate added:** `tools/verify_site.py` fails when an intended ASIN is set without `owner_confirmation_ref`, when the intended source is S16, or when `observed.agrees` reappears. Positive and negative checks were run on the corrected tree.
- **Not changed:** the supplied short-link CTAs stay as they are. Their compliance status is unresolved (FLG-006). No link is described as invalid or compliant.
- **Still open (owner-side):** FLG-001 intended ASIN confirmation; FLG-006 one-link Special Link test; FLG-010 account status; FLG-017 (2026-11-20 homepage result for B04G1MEwY, recorded by T-25).

## T-46 line-by-line integration review (session `arena/74e655e9-prod3`, 2026-11-20)

- **Same-day link re-checks recorded:** all five supplied short links fetched again (signed-out, 2026-11-20) and appended to `data/products.json` as `live_recheck_2026_11_20_session_74e655e9` — P-01 reached its product page twice (no `tag=` in either final URL), P-02 and P-03 ended at the Amazon homepage, P-04 returned HTTP 500 once and then reached its product page, P-05 reached its product page. Existing same-day records were never overwritten; FLG-017, FLG-023 and Q-22 were amended to carry all three passes with no tie broken.
- **Defect found:** four front-page product cards carried two `.spec-chips` rows each (PR #36). Merged to one row per card; every unique fact kept.
- **Defect found:** the front page's "All the guides" grid listed 8 of 9 articles. Thanksgiving tile added.
- **Defect found:** `compare.html` and the gift guide still sent the Chefman dual-basket CTA through `B04G1MEwY` while `index.html`/`air-fryers.html` had moved it to the direct listing. CTAs are now consistent: 20 buttons — 16 via the supplied short links, 4 via `/dp/B0CDY277D3` — and C-04/FLG-019 carry dated recounts with explicit definitions.
- **Defect found (count drift):** the canonical count is nine guides (eight evergreen plus the dated Thanksgiving plan). Factual fields in `data/open-questions.json`, `data/decisions.json`, `data/suggestions.json`, `direction.html`, `DIRECTION.md`, `EXECUTIVE_SUMMARY.md` and `executive-summary.html` still said eight / "guide nine" / "stalls at eight articles"; corrected and registers regenerated.
- **Defect found (wrong sources):** Q-10 cited the Chefman listing (S12) for a ThermoMaven claim → S13 (with the FLG-021 first-page caveat). Q-08's `sources` field said S01 while its text cited S02; the Session definition was verified live in the Program Policies Commission Income Statement → sources set to S02. Q-18 borrowed S24 (meta-robots snippet control) for a Search Console access question → sources emptied and marked unverified, the precedent DT-03 already set for Search Console rows; the off-topic Q-04 reference was dropped from its blocks list.
- **Defect found (FLG-020 itself was wrong):** a first 2026-11-20 re-read looked only at Program Policies Section 2 and reported the §2(t) ratings clause, §2(v) URL-obscuring clause and a §2(b) shortener clause as not located. A second re-read the same day located all three in the Associates Program Participation Requirements, in the lettered list under the section headed "Content on your Site": **(t)** customer reviews and star ratings only via a link obtained through Creators API or PA API; **(v)** do not cloak, hide, spoof or otherwise obscure the URL of your Site containing Special Links; **(w)** do not use a link shortening service, button, hyperlink or other ad placement in a manner that makes it unclear that you are linking to an Amazon Site. Section 2's own (b) does carry the price-display and tag-parameter rules the site cites elsewhere. FLG-020 rewritten as corrected; every citation renumbered to §6(t)/§6(v)/§6(w) across `data/citations.json`, `data/policy-checks.json`, `data/open-questions.json`, `data/suggestions.json`, `data/flagged.json`, `compare.html`, `ideas.html`, `direction.html`, `DIRECTION.md`, `scripts/build_registers.py` and the `tools/check_site.py` comment; exact wording recorded in the citation log.
- **Defect found (stale provenance and counts):** FLG-023 and Q-22 claimed both P-04 homepage records were kept in `data/products.json` — the ce911db5 record lives on FLG-023, Q-22 and the coordination board; corrected in place. README's two duplicate register tables (stale ranges) replaced with one table dated 2026-11-20; "all 30 pages" claims updated to 31; `ideas.html` FLG-018 references corrected to FLG-023; `flagged.html` byline re-dated; the empty "What is flagged" heading in `executive-summary.html` filled; stale "two of five / one no longer reaches its product" link claims in `EXECUTIVE_SUMMARY.md`, `executive-summary.html` and `ideas.html` rewritten to the three-pass record; `direction.html` register ranges corrected to SG-01..SG-31 / Q-01..Q-23.
- **DT-01 recommendation scoped** to that product's buttons — the other four keep the supplied short links pending the same test (FLG-019).
- **Not changed:** SG-04's proposal title, the meat-thermometers/compare bylines dated 2026-11-19, and pricenote wording — reviewed and left as accurate. The supplied short links are never described as invalid or compliant; their status stays unresolved (FLG-003/FLG-006).
- **Gates after the fixes:** `build_chrome`/`build_registers`/`build_decisions`/`build_sitemap --check` all OK; `scripts/check_site.py` OK; `tools/verify_site.py` release gate passed; `tools/check_site.py` 31 pages, 3,948 assertions; `tools/crawl_links.py` 31 pages, 30 reachable, 0 broken links, 0 dead anchors, 0 orphans.
