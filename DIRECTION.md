# DIRECTION.md — Suggestions, open questions, and the path chooser

**Site:** Kitchen Counter · **Tracking ID:** shopnow047c-20 · **Date:** 2026-11-19 (shop-polish revision)
**Reader-facing mirror:** `direction.html` · **Machine registries:** `data/suggestions.json`, `data/open-questions.json`

Nothing in this file is implemented until a path is chosen in the Path chooser
at the bottom. Suggestions are proposals; open questions are unknowns. The
ledger index below mirrors `data/suggestions.json` — full problem statements,
options, and recommendations live there.

## Suggestion ledger (index)

| # | Suggestion | Status | Decided by |
|---|-----------|--------|------------|
| SG-01 | One beat: cooking to a target temperature — both families in one sentence | implemented | owner |
| SG-02 | Publish the two spec conflicts instead of picking a winner | implemented | editorial |
| SG-03 | No prices anywhere, with the policy explained on its own page | implemented | editorial |
| SG-04 | Eight question-shaped guides instead of eight product reviews | implemented | editorial |
| SG-05 | Compliance gate inside the build, not a checklist promise | implemented | editorial |
| SG-06 | Buy one air fryer and one thermometer to earn original testing | proposed | owner |
| SG-07 | Search Console verification + sitemap submission before guide nine | proposed | owner |
| SG-08 | Privacy-preserving outbound-click counter, local counts only | implemented | editorial |
| SG-09 | Unique title + meta description on every page | implemented | editorial |
| SG-10 | Publication front page; dashboard surfaces one click away in the footer | implemented | editorial |
| SG-11 | Typographic hero art and labelled placeholders; never generated or copied photos | implemented | editorial |
| SG-12 | Three-question chooser above the comparison | implemented | editorial |
| SG-13 | Test one short link inside the enrolled Associates workflow before trusting the format | proposed | owner |
| SG-14 | Empty campaign ledger with defined columns, filled only from first-party reports | implemented | owner |
| SG-15 | Every shop page leads with products; verification record one click away | implemented 2026-11-19 | editorial |
| SG-16 | Raster (PNG) social preview card replacing the SVG; verify in a share debugger | proposed | editorial |
| SG-17 | Product Advertising API as the only path to displayed prices (retires the old price-re-check idea) | proposed | owner |
| SG-18 | Guide nine chosen from measured queries, not instinct | proposed | editorial |
| SG-19 | Mobile-first tap-target pass ≥44/48px, ≥8px spacing (S-20, session 65474d4f; Google Lighthouse guidance, source S19) | implemented 2026-11-19 | engineering |

Retired 2026-11-19: the earlier `direction.html` row “Weekly price re-check: re-fetch the five
listings and update dated prices” contradicted Program Policies 2(b) and the site’s own no-prices
policy (SG-03). It is replaced by SG-17. The old rows SG-02…SG-08 in that table map to the
canonical ledger above; the ledger is the single source of truth.

## Open questions — what must be answered before deciding

Twenty-one questions are registered in `data/open-questions.json`. Each carries
`known`, `unknown`, `how_to_find_out`, `who`, and a status
(`blocking` / `queued` / `watch` / `owner-only`).

Owner-only, cheapest first — these unblock the most:

| # | Question | Cost |
|---|----------|------|
| Q-08 | Is tracking ID `shopnow047c-20` on an enrolled, eligible Associates account? | 5 min in Associates Central |
| Q-19 | Is the account eligible for the Product Advertising API? | 5 min in Associates Central |
| Q-02 | Do the five Special Links carry `tag=shopnow047c-20`? | One signed-in click each |
| Q-04 | Is the `link.amazon` short-link format acceptable in this account’s enrollment? | Same session as Q-02 (FLG-006) |
| Q-18 | Will the owner verify the site in Search Console this month? | 10 min |
| Q-01 | What product did the owner intend for each short link? (FLG-001) | One confirmation per link |

Queued / watch (full text in the JSON and on `direction.html`): Q-03 (commission rates),
Q-05 (which query set converts — data required), Q-06 (test purchases), Q-07 (which analytics
endpoint and retention), Q-09 (90-day target), Q-10 (newer ASIN swap for P4), Q-11 (P1 litres),
Q-12 (brand/visual sign-off), Q-13 (endpoint storage schema), Q-14 (cadence owner), Q-15
(disclosure reach), Q-16 (custom domain), Q-17 (retire zero-impression guides), Q-20 (email
provider + consent), Q-21 (does the SVG preview render anywhere).

## Path chooser

Choose one path. Record the choice here (date + path) and on `direction.html`.
Unchosen suggestions stay proposals.

- [ ] **Path A — Steady publication:** one question-shaped guide per week, sitemap + RSS
      updated each time; from guide nine onward, topics chosen from Search Console queries
      (SG-18). No price re-checks — SG-03/SG-17 forbid it without the API.
- [ ] **Path B — Conversion focus:** raster preview image (SG-16), self-hosted analytics
      endpoint (SG-04), and email capture (SG-06) before any new content.
- [ ] **Path C — Hold:** resolve FLG-001 (intended ASINs) and FLG-006 (Special Link test)
      first, then choose A or B.

**Chosen path:** _(none yet — 2026-11-19)_
