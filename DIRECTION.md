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
| SG-20 | Pick one product as the site's spine and let the other four support it | proposed | owner |
| SG-21 | Pick one product as the site's spine and let the other four support it | duplicate | owner |
| SG-22 | Write the first-hand answer only after someone has actually used the appliance for a month | proposed | owner |
| SG-23 | Make one page the definitive answer to "how big is it really" | implemented | editorial |
| SG-24 | Give the site a named editor before giving it a voice | proposed | owner |
| SG-25 | Stop calling it a decision log until decisions are actually recorded there | implemented | engineering |
| SG-26 | _Unassigned — no proposal in the 2026-11-20 brief uses this number_ | — | — |
| SG-27 | Give the navigation one group and one name for the review desk | proposed | editorial |
| SG-28 | Make the shipped RSS feed discoverable from every page | proposed | engineering |
| SG-29 | Choose the Search Console property type and verification method (extends SG-07) | proposed | owner |
| SG-30 | Reader capture: RSS first, email only after a provider and a CAN-SPAM check | proposed | owner |

Retired 2026-11-19: the earlier `direction.html` row “Weekly price re-check: re-fetch the five
listings and update dated prices” contradicted Program Policies 2(b) and the site’s own no-prices
policy (SG-03). It is replaced by SG-17. The old reader-table rows SG-02…SG-08 map to the canonical
ledger above; the mobile-first row that session 65474d4f added as “SG-09” is registered here as
SG-19. The ledger is the single source of truth.

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

## Decision log (dated, with the source each decision rests on)

| Date | Decision | Source | Effect |
|---|---|---|---|
| 2026-11-19 | Publish both readings when a listing contradicts itself | S02 | Preset count, battery life, warranty and accessory count shown as conflicts |
| 2026-11-19 | Display no price while neither Amazon-served nor PA-API data is used | S02 §2(b) | Price slots read "Current price on Amazon"; the gate fails on a currency amount |
| 2026-11-19 | Remove customer star ratings and rating counts from every page | S02 §2(t) | Ratings replaced with a policy note in the comparison table |
| 2026-11-19 | Mark every outbound Amazon link `rel="sponsored"` and open in a new tab | S04 | The gate walks every anchor |
| 2026-11-19 | Keep intended ASIN and observed redirect in separate fields | S01 | `intended_*` stays null until an owner confirms |
| 2026-11-19 | Split suggestions, questions and decisions into three registers | audit I-01 | SG-01 no longer names two different proposals |
| 2026-11-20 | Register SG-27..SG-30 as proposals: one navigation label for the review desk, RSS discoverability, Search Console property choice (extends SG-07), reader capture | S26–S30; S02 §4 | Four proposals await a choice. None is implemented. |
| 2026-11-20 | Mark SG-21 as a duplicate of SG-20 (identical text); keep the ID so later IDs do not shift | `data/suggestions.json` | Owner may delete or replace SG-21 |
| 2026-11-20 | Correct 16 source IDs that named the wrong publisher (e.g., a Google rule cited to a product listing; an FTC quotation cited to Google) and add gate rule `D15-attribution` | S03, S04, S21, S22, S24, S25 | Fixed in the data; the gate fails on future publisher mismatches |
| 2026-11-20 | Flag the Program Policies §2(t), §2(v) and shortener citations as UNVERIFIED (FLG-018); compliance copy otherwise unchanged | S02 (section 2 text read 2026-11-20) | Owner or editorial review needed; no claim removed without a source |

## Audit findings, session a25ccde6 (2026-11-19)

| ID | Finding | Severity | Status |
|---|---|---|---|
| I-01 | `direction.html` carried SG-01..SG-08 with meanings different from `data/suggestions.json` | high | fixed — three generated registers, ID prefixes are exclusive |
| I-02 | Customer star ratings and rating counts rendered on four pages | high | fixed — removed; gate rule `D10-no-ratings` |
| I-03 | Data registers cited S07 and S08, which `sources.json` never defined | medium | fixed — S07/S08/S09/S19-S21 now defined; gate rule `D06-source-refs` |
| I-04 | `feed.xml` described the gift guide as "five verified kitchen gifts, $16.99-$149.99" and the capacity guide as using a "whole-chicken test" the site never ran | high | fixed — descriptions rewritten; gate rules `D11`, `D12` |
| I-05 | `og:image` was a relative SVG URL, which most social crawlers will not render | medium | fixed — absolute 1200x630 PNG on every page; gate rule `D14-og-absolute` |
| I-06 | `sources.json` S06 duplicated S02's URL without saying so | low | annotated, kept for citation continuity |
| I-07 | No structured data on the front page, the pillars or the buying guide | medium | fixed — WebSite/Organization/CollectionPage, BreadcrumbList, FAQPage |
| I-08 | `404.html` still used the pre-rebrand header and colours | low | rebuilt on the current design system |
| I-09 | Two copy claims still said a price is compared, after all prices were removed | low | fixed — "& price" now reads "& sourcing" |
| I-10 | No reader-facing suggestions or questions page existed, although the brief asks for one | high | fixed — `suggestions.html`, `questions.html`, `citations.html` |

## Audit findings recorded but **not** changed (published for review)

| ID | Finding | Why it was not changed |
|---|---|---|
| I-11 | `analysis.json` computes "quarts per square inch" from listed dimensions | The arithmetic is reproducible and `scripts/check_site.py` bans the phrase "capacity per inch" from reader pages, so it stays internal. Whether to publish it is proposal SG-18. |
| I-12 | `data/flagged.json` (F-series) is not linked from any page, while `flagged.html` tracks a separate FLG-series | The two registers overlap in scope. Merging them is a content decision, not a defect fix; logged here rather than half-done. |
| I-13 | The five `link.amazon` destinations still carry no visible `tag=` | Needs the owner's Associates account (FLG-006/010, Q-02). Not resolvable from outside. |
| I-14 | No build step regenerates article HTML from data | Articles are hand-written prose; a generator would be a project, not a fix. |
