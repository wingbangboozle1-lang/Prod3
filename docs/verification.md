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

## T-53 direction-surface reconciliation and page-wide gates (session `arena/b8dae8e0-prod3`, 2026-11-20)

- **Context:** this session began against `main` @ `0be7124` (PR #34) and re-based three
  times as PRs #36–#62 landed; every earlier claim number (T-24, T-25, T-26, T-39) had
  been taken upstream before the claim committed, so the claim ships as **T-53**. Work
  already landed by parallel sessions was discarded rather than re-implemented (chrome
  SG-26 reconstruction was explicitly declined upstream and is now FLG-029; the
  guide-count copy is gated by D40; `build_decisions.py` counts only `proposed`; the
  README table is generated). Nothing was re-added that main already had.
- **Defects fixed (all demonstrable on the merged tree):**
  - `direction.html` cited the unoccupied suggestion slot as "SG-26" in two places and
    attributed it to FLG-021; FLG-021 is the source-register finding, and the gap was
    renumbered FLG-029 in place. Citations now point at FLG-029 and describe the slot
    between SG-25 and SG-27 (the register-jump id is not cited as a reference — the
    convention DIRECTION.md already follows so D29 can pass).
  - Register ranges were stale: pages said SG-01..SG-31 / Q-01..Q-21 while the
    registers hold SG-01..SG-47 (SG-26 unoccupied) and Q-01..Q-29. Corrected in
    `direction.html` (two places) and `DIRECTION.md` (index note + "twenty-nine
    questions" count), plus the two remaining FLG-021→FLG-029 pointers and the
    Q-digest correction's FLG-020→FLG-028 pointer (FLG-028 is the renumbered
    duplicate that describes that correction).
  - `direction.html` still shipped a duplicate "Source for SG-19" paragraph, one copy
    inside `<tbody>`; the in-tbody copy was removed (the table cell text is unchanged).
- **Gates added (`tools/check_site.py`, free ids D41/D42 after upstream's D40):**
  - `D41-rss-autodiscovery` + `D41-rss-once` — every page carries exactly one
    `application/rss+xml` link, `feed.xml` at the root and `../feed.xml` one level
    down (articles/, tools/, products/). Negative-tested: removing the link fails
    `rss-once`, duplicating it fails `rss-once`, and both were restored to green.
  - `D42-sg-refs-resolve` + `D42-q-refs-resolve` — every `SG-nn`/`Q-nn` token on any
    page must exist in its register (D28/D29 covered only `DIRECTION.md`). Its first
    run caught the two direction-surface citations above. Negative-tested with a dangling unregistered suggestion id, restored to green.
- **One cross-scope edit, logged per the board rule:** `data/flagged.json`, FLG-029's
  `detail` field said "the register itself skips the SG-26 slot" — the same token the
  new gate rightly rejects, and `decisions.html` renders the field verbatim. Reworded
  to "skips the slot between SG-25 and SG-27"; no finding, id or grading changed, and
  `data/flagged.json` was the only field touched. Flag file otherwise untouched
  (guide-count was already handled upstream via D40/FLG-038-era rewording).
- **Verification on the final tree (all exit 0):** `scripts/check_site.py` (39 pages),
  `tools/check_site.py` (39 pages, 6245 assertions, all additional rules passed),
  `tools/verify_site.py`, `scripts/build_sitemap.py --check`,
  `scripts/build_registers.py --check`; plus a custom crawl of 39 pages / 1998 internal
  hrefs with 0 broken links or anchors, and sitemap + feed link targets all resolving.
## Live source re-verification (T-27, session arena/80802891-prod3, 2026-11-20)

Each load-bearing quote was re-fetched from its official domain on 2026-11-20 and read against
`data/sources.json`. All matched; no register value needed changing. Links below are for manual
review.

| Source | What was checked | Result | URL for manual review |
|---|---|---|---|
| S01 Operating Agreement | Update stamp; §5 disclosure sentence; §6 material-breach clause | "Updated: October 15, 2025"; §5 requires "As an Amazon Associate I earn from qualifying purchases." or a substantially similar statement, verbatim as recorded; §6 makes any §5 violation a material breach | https://affiliate-program.amazon.com/help/operating/agreement |
| S02 Program Policies | Update stamp; Qualifying Purchases definition | "Updated: April 14, 2026"; Qualifying Purchases require a customer click through a Special Link on your Site, as recorded | https://affiliate-program.amazon.com/help/operating/policies |
| S03 FTC Disclosures 101 | Placement language; page date | "Place it so it's hard to miss." and "The disclosure should be placed with the endorsement message itself." both verbatim; page dated November 2019 | https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers |
| S04 Google — Qualify outbound links | `rel="sponsored"` definition; last-updated stamp | "Mark links that are advertisements or paid placements (commonly called paid links) with the sponsored value." verbatim; "Last updated 2025-12-10 UTC." | https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links |
| S06 Creators API — GetItems | ItemIdType definition of ASIN | "Amazon Standard Identification Number: 10-Character alphanumeric unique identifier assigned by Amazon." verbatim | https://affiliate-program.amazon.com/creatorsapi/docs/en-us/api-reference/operations/get-items |

Product pages were not re-fetched by this session: session `arena/70e8475c-prod3` (T-25) re-checked
all five short links and both policy pages on the same day, 2026-11-20; the only drift found there
is FLG-017 (B04G1MEwY resolving to the Amazon homepage). T-27 changed no product claim.

## Register recovery (T-27, 2026-11-20)

`data/suggestions.json` SG-20 and SG-21 had carried byte-identical content since PR #17's merge
replay (the board's own handoff log recorded "SG-21 was restored after a `=======` marker was
mis-read"). The original content was recovered from PR #17's own commit history: commit
`7fbef67` (`git show 7fbef67:data/suggestions.json`) carries SG-20 "Ask the Associates account one
question and let the answer price the whole site" and SG-21 "Pick one product as the site's spine
and let the other four support it" as two distinct rows. SG-20 was restored verbatim from that
commit (with one dated sentence appended for the 2026-11-20 link re-check), SG-21 now carries the
spine proposal, and the interim SG-21 tombstone is withdrawn. Gate rule D20 continues to fail the
build if two live proposals ever share a title again. Manual review: the Commits tab of
https://github.com/wingbangboozle1-lang/Prod3/pull/17, or `git show 7fbef67:data/suggestions.json`
in any checkout of the repository.
