# Verification record

Sessions: `arena/5a4e180c-prod3` (build, merged via PR #1) and `arena/9978ab21-prod3` (integration, in progress) · Date: 2026-11-19

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

The intended ASIN (short-link path code) and confirmed/observed ASIN (redirect destination) are stored in separate fields and never merged. Intended fields stay null until the owner confirms in the Associates workflow. Short-link compliance status is unresolved; no claim is made that the supplied short links are invalid (see ++FLG-003++ context).

## Flagged irregularities

See `data/sources.json` (flaggedIrregularities) and `/flagged.html`. None block the merge.

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
page where the disclosure marker does not occur before the first `<h1>`, so on all 21 pages the strip
precedes every heading and product button in reading order, and it is a normal full-width block (not
positioned after the hero), so it is not reordered on a narrow screen. The S-20 pass keeps the strip
compact at `<=600px` (`.disclosure` 0.8rem) so it cannot grow past the fold. A physical pixel measurement
in a real browser at 320px with an enlarged system font was **not** run from this sandbox (see the
matching note on Q-15 in `data/open-questions.json`); that remains a one-time owner/browser check.
