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
