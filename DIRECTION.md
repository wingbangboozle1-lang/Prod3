# DIRECTION.md — Suggestions, open questions, and the path chooser

**Site:** Kitchen Counter · **Tracking ID:** shopnow047c-20 · **Date:** 2026-11-20 (shop-first revision)
**Reader-facing mirror:** `direction.html` · **Decision desk:** `decisions.html` (generated from `data/decisions.json` + the three registers) · **Machine registries:** `data/suggestions.json`, `data/open-questions.json`, `data/decisions.json`

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
| SG-20 | Pick one product as the site's spine and let the other four support it | implemented 2026-11-20 (dual-basket air fryer is the front-page starting pick) | owner |
| SG-21 | — | **retired 2026-11-20**: byte-identical duplicate of SG-20, kept as a retired row so the change is auditable | — |
| SG-22 | Write the first-hand answer only after someone has actually used the appliance for a month | proposed | owner |
| SG-23 | Make one page the definitive answer to "how big is it really" | implemented | editorial |
| SG-24 | Give the site a named editor before giving it a voice | proposed | owner |
| SG-25 | Stop calling it a decision log until decisions are actually recorded there | implemented | engineering |
| — | *(gap)* The ID slot between SG-25 and SG-27 is unoccupied in `data/suggestions.json` — see the FLG-021 gap note below; the registered SG-27..SG-31 rows (this session re-mirrored them verbatim) are the canonical ones | — |
**Gap, 2026-11-20 (FLG-021):** this digest listed a "one generated chrome for all pages" row carrying an id that does not exist in `data/suggestions.json`, and the register skips from SG-25 to SG-27. Either a row was renumbered during a merge or one was never written. Neither is reconstructed here; the digest now names the ids that exist, and gate `D29` fails the build if it cites another phantom id.
| SG-27 | One name for the Direction page, in the nav and the footer | implemented | engineering |
| SG-28 | Ship the RSS feed and advertise it on every page | implemented | engineering |
| SG-29 | Connect Google Search Console once the owner has an account | proposed | owner |
| SG-30 | Decide how readers stay in touch: RSS only, or an email provider with consent | proposed | owner |
| SG-31 | Put the listing's own contradiction on the product card, not only the flag page | implemented 2026-11-20 | editorial |
| SG-43 | Give the seasonal block a retirement date and a successor, before Thanksgiving ends | proposed | editorial |
| SG-44 | Do not add FAQ markup expecting a Google FAQ rich result — that feature is gone | proposed | editorial |
| SG-45 | Fact-check any AI-assisted draft line by line before it ships, and say how the site is made | proposed | owner |
| SG-46 | Measure Core Web Vitals once, then gate new frontend effects on the result | proposed | editorial |
| SG-47 | Keep internal anchors descriptive — add a gate so the discipline cannot slip | proposed | engineering |
| SG-48 | Before any automated Amazon listing or price refresh, use the Product Advertising API or make the fetcher identify itself under the IP License Agent Terms | proposed | owner |

SG-48 was added 2026-11-20 (session `arena/1fbc2432-prod3`, T-57) from the same-day official-source recheck (`data/recheck-2026-11-20-1fbc2432.json`); the row was drafted as SG-39 and renumbered twice with the register. SG-43..SG-47 were added 2026-11-20 (session `arena/7878cdbe-prod3`, T-54; renumbered twice while
this branch was queued — first from SG-32..SG-36 after upstream 6bf60cac/8692a390 registered
SG-32..SG-38, then from SG-39..SG-43 after upstream PR #52 registered SG-39..SG-42) with sources
verified that day:
S34 (Google link best practices), S35 (Google search-doc changelog: the FAQ rich result was
deprecated 2026-05-07/08 and its documentation removed June 2026), S36 (Google generative-AI
content guidance, page updated 2026-10-01). The rows above mirror `data/suggestions.json` verbatim.

Retired 2026-11-19: the earlier `direction.html` row “Weekly price re-check: re-fetch the five
listings and update dated prices” contradicted Program Policies 2(b) and the site’s own no-prices
policy (SG-03). It is replaced by SG-17. The old reader-table rows SG-02…SG-08 map to the canonical
ledger above; the mobile-first row that session 65474d4f added as “SG-09” is registered here as
SG-19. The ledger is the single source of truth.

## Open questions — what must be answered before deciding

Twenty-three questions are registered in `data/open-questions.json` (Q-01…Q-23). Each carries
`known`, `unknown`, `how_to_find_out`, `who`, `cost`, `sources` and a status
(`blocking` / `queued` / `watch` / `owner-only`).

**Correction, 2026-11-20 (FLG-020).** This digest used to list Q-08 as the account-status question
and Q-05 as "which query set converts". Neither matched the register: Q-08 is "what counts as a
session for the ledger" and Q-05 is "who is the named author". The account-status question had never
been registered at all, so it was added as **Q-23** rather than renumbered into a used id. Every id
below is the register's own subject; `tools/check_site.py` fails the build if this file cites an id
that does not exist.

Owner-only, cheapest first — these unblock the most:

| # | Question (as registered) | Cost |
|---|--------------------------|------|
| Q-23 | Is `shopnow047c-20` on an enrolled, eligible Associates account? | 5 min in Associates Central |
| Q-19 | Is the account eligible for the Product Advertising API? | 5 min in Associates Central |
| Q-02 | Do the five Special Links carry `tag=shopnow047c-20`? | One signed-in click each |
| Q-04 | Is the `link.amazon` short-link format acceptable in this account's enrollment? | Same session as Q-02 (FLG-006) |
| Q-22 | Why did two of the five links end at the Amazon homepage on 2026-11-20? | 15 min, signed in (FLG-017) |
| Q-18 | Will the owner verify the site in Search Console this month? | 10 min |
| Q-05 | Who is the named author, and what is their experience? | One decision |
| Q-09 | What is the 90-day target outcome? | One decision |

Queued / watch, in register order (full text in the JSON and on `decisions.html`): Q-01 (one beat or
two), Q-03 (commission rates), Q-06 (test purchases), Q-07 (which analytics can be installed),
Q-08 (what counts as a session), Q-10 (newer ASIN swap for P4), Q-11 (P1 capacity in litres),
Q-12 (brand and visual sign-off), Q-13 (endpoint storage schema), Q-14 (cadence and who writes),
Q-15 (disclosure reach when a reader never scrolls), Q-16 (custom domain), Q-17 (retire
zero-impression guides), Q-20 (email provider and consent), Q-21 (does the PNG preview render in
a share debugger).

## The SG-20 / SG-21 duplicate — reproduced and resolved

Verified 2026-11-20: `SG-20` and `SG-21` carried byte-identical `title`, `problem`,
`evidence`, `options`, `recommendation`, `effort`, `confidence`, `decision_owner` and
`blocks` fields. This is the same "one identifier, two meanings" failure the a25ccde6
audit fixed for SG-01..SG-08, so it was treated as a recurrence rather than a typo.

**Resolution:** SG-21 was retired in place — not deleted — with a `retired_note` recording
the byte-for-byte comparison. Deleted rows cannot be audited; retired rows can. Gate rule
`D20` now fails the build if any two live suggestions share a title.

**What is still open:** only the owner knows whether a second, different proposal was ever
meant to occupy SG-21. If so, the duplicate displaced it and it needs re-entering. That is
DT-11 territory and is recorded on `decisions.html`.

## Path chooser

Choose one path. Record the choice here (date + path) and on `decisions.html`.
Unchosen suggestions stay proposals. The three paths are defined in `data/decisions.json`
so the page and the data cannot disagree.

| Path | Name | What it fixes first | Cost |
|---|---|---|---|
| A | Make it earn | Special Link test (DT-01), analytics endpoint (DT-07), Search Console (DT-03) | One session + one focused day |
| B | Make it a publication | Buy two units (DT-05), publish real measurements, fix cadence (DT-10) | Purchase price + recurring writing |
| C | Narrow and harden | Cut to one family (DT-06), settle the URL (DT-09), clear owner-only questions | Time and one pruning decision |

- [ ] **Path A — Make it earn:** DT-01 one signed-in Special Link test per product, DT-07 the
      analytics endpoint, DT-03 Search Console verified and the sitemap submitted — then one
      guide, chosen from search data. Guide nine and any brand or domain change wait.
- [ ] **Path B — Make it a publication:** DT-05 buy one air fryer and one thermometer (SG-06),
      publish the measurements as method, name the author, fix the cadence at one guide a
      month (DT-10). Costs money before it earns any.
- [ ] **Path C — Narrow and harden:** DT-06 air fryers as the single beat, DT-09 settle the URL
      before promoting it, clear the owner-only question rows; no new content until the desk
      is empty.

Superseded 2026-11-20: the checkbox list that previously lived here described different paths
(“Steady publication / Conversion focus / Hold”) and mis-cited “analytics endpoint (SG-04)” and
“email capture (SG-06)” — SG-04 is the guides-format proposal and SG-06 is the buy-units
proposal. The table above, from `data/decisions.json`, is the only path definition now.

**Chosen path:** _(none yet — 2026-11-20. Recording a path on `decisions.html` writes to the reader's browser only; the real record is this table.)_

## Decision log (dated, with the source each decision rests on)

| Date | Decision | Source | Effect |
|---|---|---|---|
| 2026-11-19 | Publish both readings when a listing contradicts itself | S02 | Preset count, battery life, warranty and accessory count shown as conflicts |
| 2026-11-19 | Display no price while neither Amazon-served nor PA-API data is used | S02 §2(b) | Price slots read "Current price on Amazon"; the gate fails on a currency amount |
| 2026-11-19 | Remove customer star ratings and rating counts from every page | S02 §6(t) *(recorded as the Section 2 letter until corrected 2026-11-20)* | Ratings replaced with a policy note in the comparison table |
| 2026-11-19 | Mark every outbound Amazon link `rel="sponsored"` and open in a new tab | S04 | The gate walks every anchor |
| 2026-11-19 | Keep intended ASIN and observed redirect in separate fields | S01 | `intended_*` stays null until an owner confirms |
| 2026-11-19 | Split suggestions, questions and decisions into three registers | audit I-01 | SG-01 no longer names two different proposals |
| 2026-11-20 | Reconcile the path chooser on `direction.html` and in this file with the canonical paths in `data/decisions.json` (DT-01..DT-10); retire the stale “Steady publication / Conversion focus / Hold” wording and its wrong SG-04/SG-06 citations | session T-39 audit | The digest and the decision desk cannot disagree about what the three paths are |
| 2026-11-20 | Reconcile the digest's tail index rows with the registered SG-27..SG-31 rows (T-37/T-40..45); the unoccupied ID between SG-25 and SG-27 is documented under FLG-021, not re-numbered | session T-39 audit · `data/suggestions.json` | The digest index names the same proposals as the register for every live ID |
| 2026-11-20 | Publish one question-shaped guide a calendar month; approver: the site owner; next guide due 2026-12-31 (DT-10, owner instruction in the 2026-11-20 brief) | Owner instruction · `docs/publishing-cadence.md` · `data/decisions.json` DT-10 | The commitment is a rhythm, not a traffic or revenue forecast; `tools/verify_site.py` now fails a guide that is missing from the sitemap, the feed (headline = H1) or the guides hub |

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
