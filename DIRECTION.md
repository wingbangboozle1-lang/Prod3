# DIRECTION.md — Suggestions, open questions, and the path chooser

**Site:** Kitchen Counter · **Tracking ID:** shopnow047c-20 · **Date:** 2026-11-19
**HTML mirror:** `direction.html` (same content, reader-facing)

Nothing in this file is implemented until a path is chosen in the Path chooser
at the bottom. Suggestions are proposals; open questions are unknowns.

## Suggestions (proposals, not yet implemented)

| # | Suggestion | Why it might help | Effort |
|---|-----------|-------------------|--------|
| SG-01 | Weekly price re-check: re-fetch the five listings, update dated prices | Fresh prices convert better than stale ones | Low (script exists) |
| SG-02 | One new question-shaped guide per week, added to sitemap + RSS | Steady organic surface area | Medium |
| SG-03 | Amazon-provided product images (Program Content) on product cards | Visual trust without copyright risk | Low |
| SG-04 | Self-hosted analytics endpoint (wire `ENDPOINT` in `assets/app.js`) | Real click/conversion data for topic choices | Medium |
| SG-05 | Search Console verification + sitemap submission | Measure whether search traffic arrives | Low |
| SG-06 | Email reader capture (wire the form to a provider) | Return visits independent of search | Medium |
| SG-07 | Seasonal clusters: holiday, grilling season, back-to-school dorm | Match content to buying moments | Medium |
| SG-08 | Replace the two "newer model" picks (FLG-004/005) after review | Promote current models, not superseded ones | Low |

## Open questions (information we do not have)

| # | Question | How to discover the answer |
|---|----------|----------------------------|
| Q-01 | What product did the owner intend for each short link? | Owner confirms intended ASIN per link in the Associates workflow (FLG-001) |
| Q-02 | Are the supplied short links compliant Special Links? | Test one per product; check destination + tracking report (FLG-006) |
| Q-03 | What are current commission rates for these categories? | Associates Central → Commission Income Statement (first-party report only) |
| Q-04 | Which queries bring real search traffic? | Search Console after 30 days of indexing (SG-05) |
| Q-05 | Which product converts best? | Associates reports + outbound-click counts (SG-04); never forecast |
| Q-06 | Which listing conflict is correct (FLG-002/003)? | Seller clarification or manufacturer spec sheet |
| Q-07 | Should the site cover more categories? | Measure the two current pillars first; expand only on evidence |

## Path chooser

Choose one path. Record the choice here (date + path) and on `direction.html`.
Unchosen suggestions stay proposals.

- [ ] **Path A — Steady publication:** one guide per week, weekly price re-checks, sitemap + RSS updated each time.
- [ ] **Path B — Conversion focus:** Amazon-provided images, self-hosted analytics, and email capture before new content.
- [ ] **Path C — Hold:** resolve FLG-001 (intended ASINs) and FLG-006 (Special Link test) first, then choose A or B.

**Chosen path:** _(none yet — 2026-11-19)_
