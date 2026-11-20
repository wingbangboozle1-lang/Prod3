# Executive summary — Kitchen Counter

**Purpose:** A buyer-facing Amazon Associates publication for air fryers and meat thermometers, with product comparisons, question-led guides, clear disclosures, and a reviewable decision register.

**Tracking ID:** `shopnow047c-20` (provided for the project; Associates account enrollment and eligibility are not confirmed — FLG-010).

**Status date:** 2026-11-20. Product and policy facts below reflect the repository's dated source records; the listing snapshot date is 2026-11-19. On 2026-11-20 the five supplied short links were fetched again in five session passes, with different results: four of five reached product pages (70e8475c), three of five (ce911db5), then **none of the five** on the 6bf60cac and 6c0972fb passes, with every final URL reading `https://www.amazon.com/`; the d52ad947 pass fetched two links (B04G1MEwY, B0c8moW59) and both ended at the homepage. Exact fetch times are not recorded (FLG-012), so the passes are not ordered beyond what their records state. All dated observations are kept side by side in `data/products.json` — the ce911db5 records were transcribed into the file by d52ad947 from the published session record — and none is overwritten and no cause is asserted (FLG-017, FLG-031, FLG-025, FLG-039). Separately, the Associates Program Policies (updated 2026-04-14) §2(b) require the Associates tag as a parameter in each link's URL, and no shipped anchor on this site carries one in the URL the reader receives — recorded as FLG-026, with the caveat that a short-link service may add the tag downstream (Q-24). No price, rating or offer was recorded.

## Bottom line

The publication site is built and the repository's release gates pass. The reader-facing front page leads with five product listings, a three-question chooser, category pages, a comparison, a buying guide, and fifteen question-shaped articles (evergreen guides and dated seasonal pieces — the guide hub lists them by theme), one generated spec page per product, and a dated twelve-row publishing plan. Every page has the Associates disclosure above its first heading and repeats it in the footer. Amazon links are marked `rel="sponsored"`.

**Recommendation:** keep the current editorial publication, but do not scale links or claim revenue performance until the owner-side Associates workflow confirms the intended products, link compliance, and tracking. The site does not have aggregate analytics, verified Search Console data, or conversion reports. Consequently, there is no evidence here for product superiority, demand, conversion rate, commission potential, or revenue forecasts.

## Five submitted links: what is and is not known

The supplied short-link tokens and their observed redirect targets are recorded separately in `data/products.json`. The observations below were captured on 2026-11-19; the 2026-11-20 re-check is recorded beside them in `data/products.json` (`live_recheck_2026_11_20`). Intended product identity remains unconfirmed for every link. The intended-ASIN, intended-listing, confirmation-date, and confirmation-source fields remain blank by design.

| Submitted token | Observed listing at snapshot | Category | Intent confirmed? | Source |
|---|---|---|---|---|
| `B04G1MEwY` | Chefman 6 Qt Dual Basket · `B0CDY277D3` (2026-11-19); 2026-11-20 re-checks all ended at the Amazon homepage (every pass that fetched it) — FLG-017 | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B0CDY277D3) |
| `B02NbDxp3` | Emeril Lagasse 26QT French Door · `B09B7SB46R` | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B09B7SB46R) |
| `B00hJ57DV` | Chefman 8 Qt TurboFry · `B08DKYBTPH` | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B08DKYBTPH) |
| `B0c8moW59` | ThermoMaven instant-read · `B0DHZTCNR5` (2026-11-20 re-checks disagree: product page in the first pass, homepage in the later passes — FLG-031/FLG-025) | Meat thermometer | No | [Official Amazon listing](https://www.amazon.com/dp/B0DHZTCNR5) |
| `B0f3GKalj` | CHEF iQ Sense Gen3 · `B0DZFD6R9Z` | Meat thermometer | No | [Official Amazon listing](https://www.amazon.com/dp/B0DZFD6R9Z) |

**Important distinction:** the observed destination is evidence of where a supplied link resolved during that dated check; it does not prove that destination is the product the owner intended or that the link has been tested in the enrolled Associates account. FLG-001 and FLG-006 remain open. Do not describe the supplied short links as invalid: their exact compliance status is unresolved.

**Correction (2026-11-20, FLG-018/019):** earlier 2026-11-19 records had copied observed ASINs into the intended-ASIN fields and cited a NIST reference page as their source. Those intended fields are now blank, and a release gate blocks any intended ASIN without an owner-confirmation record. The policy record also said product buttons go straight to `/dp/` URLs; the buttons actually use the supplied short links, and the `/dp/` URLs are separate source links. Both corrections are recorded.

## Current capabilities and evidence limits

| Area | Current state | What is not established | Official source |
|---|---|---|---|
| Publication | Buyer-first front page; two category pillars; comparison and buying guide; fifteen articles (evergreen guides, the dated Thanksgiving pair, the two gift guides and the listing-literacy guide); five per-product spec pages; a twelve-row publishing plan; three decision tools; RSS feed and sitemap | Organic impressions, rankings, readership, or topic popularity | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Product facts | Seller-listed specifications linked to dated listing snapshots; conflicts are flagged, not silently resolved | Independent product testing or a current listing re-check after the 2026-11-19 snapshot | [Chefman listing](https://www.amazon.com/dp/B0CDY277D3) · [Emeril listing](https://www.amazon.com/dp/B09B7SB46R) · [Chefman listing](https://www.amazon.com/dp/B08DKYBTPH) · [ThermoMaven listing](https://www.amazon.com/dp/B0DHZTCNR5) · [CHEF iQ listing](https://www.amazon.com/dp/B0DZFD6R9Z) |
| Pricing and ratings | No price or customer-rating claims are rendered on the site | Current prices, availability, ratings, or commission rates | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| Affiliate links | All Amazon anchors use `rel="sponsored"`; supplied links and observed targets are separately recorded; a dated check found all five supplied links ending at the Amazon homepage (FLG-025) and no shipped anchor carrying a visible `tag=` parameter (FLG-026) | Whether the tag is attached downstream by the short-link service (Q-24); Associates account eligibility; intended products; reporting attribution | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) · [Google sponsored links guidance](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) |
| Measurement | Five event names are defined: `page_view`, `outbound_click`, `article_read`, `chooser_complete`, `reader_signup`. Four are counted locally; signup is reserved for a confirmed provider response | A server endpoint, shared/site-wide counts, actual signup provider, conversions, or orders | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Campaign ledger | Defined but empty; rows are to be added only from authorized first-party reports with provenance | Any clicks, sessions, orders, revenue, conversion score, or forecast | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| Search | Canonicals, robots file, sitemap, and RSS feed are present | Search Console ownership/verification, submission, query data, or indexing status | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Brand and imagery | Consistent publication design and illustrated/typographic product cards; 1200×630 PNG social preview is shipped | Share-debugger validation; official product photography is not used | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) · [Google snippet guidance](https://developers.google.com/search/docs/appearance/snippet) |

The reader-facing surface now leads with the shop, not the audit. The front
page opens on a buyer question (“Basket or oven? Instant-read or wireless?”),
followed by five product cards — seller-listed spec chips, an honest
“consider if” line, ratings dated at capture, a “Check price on Amazon” CTA,
and a source link under every card — then the chooser, seasonal guide row,
and the data table. Stylesheet: 44 px tap targets, visible focus states, card
lift on hover (mobile-first pass S-20 in effect). The RSS feed no longer
advertises a price range in the gift-guide description, and its channel title
drops the overstated channel title the audit flagged. The
Direction desk was rebuilt as a ledger and now matches `data/suggestions.json` /
`data/open-questions.json` exactly: 58 suggestion rows (SG-01..SG-58) and 30 open
questions (Q-01..Q-30). Those counts were re-read from the JSON on 2026-11-20 after
the integration merges rather than copied forward. Still open: FLG-016 / F-21 — the
social-preview image has never been run through a share debugger (the earlier SVG
format issue is resolved; the shipped 1200×630 PNG is the asset in question). All
release gates pass on the current tree.


## Added 2026-11-20 (session 6bf60cac): what a buyer can now do, and what is still blocked

| Addition | What it gives a reader or the owner | File | Gate |
|---|---|---|---|
| A spec page per product | One place per machine: every listed value with the listing as its source, the listing's own contradictions printed, the blank intended-ASIN field shown as blank, and no price or rating | `products/*.html` | `build_products.py --check` (in CI) + D32 |
| A dated publishing plan | Twelve proposed buyer-question guides with the week, the calendar reason, the evidence each needs, and whether that evidence exists — four rows are blocked and say so | `publishing-plan.html`, `data/editorial-plan.json` | D31 |
| Five reviewable proposals | SG-32…SG-35: what to do about a buy button whose link is unresolved, a link-status table, a plain-words tag statement, and the plan page itself | `suggestions.html` | `build_registers.py --check` |
| Three missing-information questions | Q-24 (does the redirect attach the tag?), Q-25 (why did all five land on the homepage?), Q-26 (who signs off the plan?) | `questions.html` | `build_registers.py --check` |
| Two decisions | DT-11 (what a buy button promises while the link is unresolved), DT-12 (plan as promise or proposal) | `decisions.html` | `build_decisions.py --check` |
| Four flag rows | FLG-025 (third dated link observation), FLG-026 (tag-parameter requirement vs observation), FLG-027 (duplicate ids fixed), plus FLG-028/029 renumbered and FLG-030/031 for two page-only callouts | `flagged.html`, `data/flagged.json` | `check_site.py` |

**The one thing that blocks earning:** the owner's signed-in link test. Nothing on the page can substitute for it, and no claim of
commission, traffic or conversion is made anywhere in this repository.

**Editorial honesty note.** A buyer-facing site that says "Check price on Amazon" is making a promise about a destination. On
2026-11-20 that promise was not true for any of the five supplied links, which is why SG-32 proposes a dated line under each button
until the owner's test passes.

---

# Addendum — 2026-11-20, session 2cd3bab9 (T-52)

Task T-52. The first claim, T-46, was taken on `main` by PR #38. The second, T-48, was taken by PR #43, and the third, T-51, by PR #42. This pass ran on the merged tree of `origin/main` at `ddb50f8`.

**Verified in this pass.** Six official pages were read on 2026-11-20: the Associates Operating Agreement (S01, updated October 15, 2025; §5 sentence matches the disclosure), Program Policies (S02, updated April 14, 2026, opening sections only), FTC Disclosures 101 (S03, November 2019), Google's outbound-links guidance (S04, last updated 2025-12-10 UTC), Creators API GetItems (S06, ASIN defined as a 10-character identifier), and NIST TN 2156 (S16). The spot-check did not cover S05, S10–S15, S17–S19 or S21–S25.

**Checked on the merged tree.** The buying guide links all fifteen guides. Every feed item carries the same title as its page H1. The publishing-coverage check in `tools/verify_site.py` (sitemap, feed, hub, cadence) passes; the release gates pass.

**Decision.** DT-10 (fixed monthly cadence) is marked decided, on the owner's instruction. One guide per calendar month; approver: the site owner; next guide due 2026-12-31 (`docs/publishing-cadence.md`). It is a rhythm, not a traffic or revenue forecast. DT-12 (promise or proposal for the twelve-week plan) remains open and is not decided here.

**Five supplied links, 2026-11-20.** This pass also found all five to the Amazon homepage. That agrees with the third dated check recorded under FLG-025. No product record changed. The intended ASIN for every link stays blank (FLG-001). No link is called invalid (FLG-003).

**New flags.** FLG-032: the coordination board repeats task IDs T-12 to T-23. An earlier note in this session said the T-20 to T-22 duplicates were removed; they are marked superseded, not deleted, so that note was wrong. FLG-037: 23 of 29 source entries have no verified value, so the register has no consistent fetch date.

**Still not established.** Whether the supplied links work in the enrolled Associates account (FLG-006; Q-02, Q-04, Q-22). Account eligibility (FLG-010). The Pages deploy for this merge (see the board record for T-52).

# Addendum — 2026-11-20, session `arena/7878cdbe-prod3` (T-53..T-56)

Task IDs were renumbered twice by collisions: T-46 was taken by PR #38, and T-50..T-52 by PRs #44–#51, so this session's work landed as T-53 (defect pass), T-54 (register additions), T-55 (this summary) and T-56 (release). Its proposal and question rows were renumbered twice the same way — upstream sessions registered SG-32..SG-38 (PRs #44–#51) and then SG-39..SG-42 (PR #52) for different subjects while this branch was queued — and now ship as **SG-43..SG-47** and **Q-28..Q-29**.

**Verified in this pass.** Four official pages were fetched and read on 2026-11-20 and registered as S34–S36 (plus re-reads of S22 and S25): Google's [link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable); Google's [search-documentation changelog](https://developers.google.com/search/updates), which shows the FAQ rich result was deprecated 2026-05-07/08 and its documentation removed in June 2026; and Google's [generative-AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), page updated 2026-10-01.

**New proposals, all awaiting review** (none implemented): give the seasonal block a retirement date and a successor before Thanksgiving ends (SG-43); do not add FAQ markup expecting a Google FAQ rich result that no longer exists (SG-44); make the AI-assisted-draft fact-check rule and a how-the-site-is-made note explicit (SG-45); measure Core Web Vitals once and gate new frontend effects on the result (SG-46); add a gate for generic anchor text so the clean 2026-11-20 scan becomes a standing guarantee (SG-47). New questions: is any of the site in Google's index yet (Q-28 — two minutes with a public `site:` query, authoritative in Search Console after Q-18), and what do Core Web Vitals measure here today (Q-29 — pagespeed.web.dev, no account). The PageSpeed Insights API was not reachable from this session's sandbox, so no performance figure was recorded; Q-29 stays a question.

**Defect pass (T-53).** The register-page bylines now derive from each register's own `generated` field (the suggestions and questions fixes landed upstream independently; the citation-log byline is derived here); `flagged.html`'s audit date was corrected to 2026-11-20; and the five listing sources (S10–S14) no longer describe "rating, price, rank" as rendered figures — the wording now says the snapshot values were recorded to data files only and never rendered. The duplicate FLG identifiers logged while this session worked (FLG-020/021/022/023) were resolved upstream as FLG-027..FLG-031, and gate D35 now fails any duplicate flag id, which was re-verified on the merged tree.

# Addendum — 2026-11-20, shop-first pass

**What this session did, in one paragraph.** The site was accurate and read like an audit.
It now reads like a shop without giving up a single compliance rule: a named starting pick on
the front page with a "look elsewhere if" that names the alternative; one navigation group plus
a second-level shelf, generated so it cannot drift; three working decision tools; a dated
seasonal guide; and a decision desk where every open choice, every unknown and three costed
paths sit on one page.

**Verified, not asserted — and one link changed under us.** Four of the five supplied short
links resolved to the ASINs recorded on 2026-11-19. The fifth, `B04G1MEwY`, resolved to the
Chefman product page at the start of this session and to the **Amazon.com homepage** on the
same day's later fetch (independently reproduced by session 70e8475c, recorded as **FLG-017**).
The cause is not established: it could be a campaign-link change, a transient response, or a
link-level setting. The 2026-11-19 observation is kept, the intended-ASIN fields stay blank,
and the front page now carries a visible status note on that card rather than presenting a
possibly-broken link as live. It is the single most urgent item on the decision desk.
The Amazon Program Policies were re-read the same day for the two clauses this pass leans on:
§2(b) on price display and Special Link tagging, and the IP License on product images. The
USDA FSIS safe-temperature chart (last updated 14 April 2025) and its probe-placement release
(19 September 2023) were fetched and the figures transcribed exactly, including the 92%
mis-placement finding in the FSIS test-kitchen study.

**A real defect, found and fixed.** `SG-20` and `SG-21` in `data/suggestions.json` were
byte-identical — the same "one identifier, two meanings" failure an earlier audit fixed
elsewhere. The duplicate arose when a merge replay clobbered SG-20's content; on 2026-11-20
(T-27) the original was recovered verbatim from PR #17's own history (commit `7fbef67`), so
SG-20 ("Ask the Associates account one question…") and SG-21 ("Pick one product as the site's
spine…") are two live proposals again and the interim SG-21 tombstone is withdrawn. Gate rule
`D20` fails the build if any two live suggestions share a title.

**Nothing was softened.** No price is rendered anywhere. Every Amazon anchor is
`rel="sponsored"`. The exact §5 disclosure sentence appears in the strip and the footer of
every page. Every new table row carries a source link or an explicit "No official source" marker,
and the gate fails a row that has neither — so "unverified" can never hide.

**Still true, still not this session's to fix.** The five short links carry no visible
`tag=shopnow047c-20`; the enrolled-account test has not been run (DT-01, FLG-006), and one of
them no longer reaches its product at all (FLG-017). There is no
analytics endpoint and no Search Console property (DT-03, DT-07). Every figure remains a seller
statement, because nothing has been purchased or tested (DT-05). These are owner actions with
minutes-scale costs, and they are published on `decisions.html` rather than buried here.

**Gates at close:** `build_chrome --check`, `build_registers --check`, `build_decisions --check`,
`build_sitemap --check`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`
(page and assertion counts recorded with the final gate run in `COORDINATION.md`) and `tools/crawl_links.py` (0 broken links, 0 dead
anchors, 0 orphans) all pass on the merged tree.

**Gates at the close of this session (T-38, session fe5fd1d9, 2026-11-20):** this session claimed
per-product detail pages concurrently with T-50, which shipped them first as a generator
(`scripts/build_products.py`, five pages, its own freshness and coverage gates). The generated
pages were adopted as canonical and this session's hand-built drafts were retired; what shipped
on top of T-50 instead: gate rule **D34** (unique FLG callout ids on `flagged.html`),
de-risking of all five comparison-table buy buttons to the official product pages (the supplied
short links all landed on the Amazon homepage at the FLG-025 re-check), a dated addendum to
FLG-019, register rows FLG-030/FLG-031 so every published callout id has a register entry, and
proposal **SG-39** (consider-if / look-elsewhere-if blocks for the generated pages, draft copy
preserved on this branch). Full suite green on the merged tree: `build_chrome
--check`, `build_registers --check`, `build_decisions --check`, `build_products --check`,
`build_sitemap --check`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`
and `tools/crawl_links.py` — 0 broken links, 0 dead anchors, 0 orphans.

The official policy and guidance sources are indexed in the [source register](sources.html), with figure-level sourcing in the [citation log](citations.html). Product details are seller statements, not independent test results. See [Flagged for Review](flagged.html) for unresolved listing conflicts and account-dependent issues.

## Ranked recommendations

| Priority | Recommendation | Why it is next | Discovery / completion evidence | Gate | Official source |
|---|---|---|---|---|---|
| 1 — compliance | In the enrolled Associates account, confirm the intended ASIN and official listing for each submitted link; test one Special Link per product and verify destination plus tracking report | Prevents scaling an unconfirmed product/link association | Owner-side confirmation record for each link; retain intended fields separately from observed redirect fields | Do not claim link validation until the account workflow and report show it | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| 2 — measurement | Choose and configure a real analytics endpoint before using site-wide click or conversion language | GitHub Pages is static; `assets/app.js` has no endpoint and currently keeps counters in each visitor's browser | Document host, allowed origin, minimal event schema, retention, access controls, privacy notice, and an end-to-end test | Do not transmit events until the data handling and disclosure are in place | [FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) |
| 3 — discoverability | Verify the site in Search Console and submit the existing sitemap | A sitemap file alone does not establish indexing or provide query data | Search Console property verified; sitemap accepted; dated query/impression export saved | No claim of ranking or search demand before data exists | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| 4 — publishing | Maintain a sustainable guide cadence; select later topics from measured queries and authorized click/order reports | Current guide titles are editorial hypotheses, not proven high-volume topics | Publish each guide with sourcing and disclosure; update sitemap/feed; review query and first-party campaign reports on a dated cadence | No automatic optimization from incomplete or inferred data | [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies) |
| 5 — reader trust | Consider original hands-on testing only if products, budget, and editorial protocol are available | Current pages transparently compare listing claims; they do not establish real-world performance | Record tested unit, method, conditions, results, limitations, and any material connection | Never imply a test was conducted when it was not | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| 6 — publication polish | Validate the shipped PNG preview with a social share debugger; then decide whether an approved brand/domain update is worthwhile | Design assets are in place, but preview rendering and brand preferences are not confirmed | Record debugger result and the owner-approved brand/domain decision | Do not claim the social preview was externally validated yet | [Google snippet guidance](https://developers.google.com/search/docs/appearance/snippet) |

The editorial hypotheses already in the guide plan include “Basket or oven-style air fryer: what should you compare?”, “A no-hype checklist for comparing air fryer capacity”, “How to assess cleanup and counter-space trade-offs”, and “Questions to ask before buying a multi-function kitchen appliance.” These are working topics—not claims about search volume, popularity, or product superiority.

## Design and content decisions awaiting review

The suggestions register (`suggestions.html`, generated from `data/suggestions.json`) carries three additions from this review round (SG-32..SG-34), each with its problem, evidence, options, recommendation, decision owner, and a Do / Maybe / No mark that copies out as a decision block. Nothing is implemented by being listed; the ideas review page (`ideas.html`) is where a choice gets marked before anything is built.

| ID | Suggestion | Status | Decided by |
|---|---|---|---|
| SG-32 | Lead the front page with a buyer question and five shop cards, not with the audit trail | Implemented — live on the front page and both category pillars | editorial |
| SG-33 | Publish catchy, trend-led question articles to earn organic traffic (seasonal calendar; Search Console is the gate before guide nine) | Proposed | editorial |
| SG-34 | Review every change in the suggestions section before anything is built | Implemented — the suggestions page, questions page, ideas review page and decision desk ship today | owner |

The open question that discovers missing information for the traffic path is Q-24: “Which of the trend-led article topics earns impressions, and should guide nine be one of them?” — queued, and unanswerable until Q-18 (Search Console verification) is done.

## Questions that must be answered before consequential decisions

| Question | Known from repository | Unknown / why it matters | How to discover it | Official source |
|---|---|---|---|---|
| What product was intended for each submitted link? | Five observed destinations are documented separately | Intended ASIN and listing remain blank; product matching cannot be assumed | Confirm each in the Associates account and record date, official listing URL, and source | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Is `shopnow047c-20` enrolled and eligible for the intended activity? | Tracking ID was supplied | Account state, eligibility, and API access are not visible to this repository | Check Associates Central; save only non-sensitive confirmation/status and date | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Do the Special Links work as intended and report under this ID? | Outbound links are marked sponsored in the site | Account-side link compliance and report attribution are untested | Test one product link in the enrolled workflow; confirm destination and report before scaling | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Which topics attract qualified visitors? | Fifteen guides and the technical SEO files exist | No Search Console impressions, clicks, or query export | Verify Search Console and review dated query reports after sufficient data accrues | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Are visits turning into outbound clicks or orders? | Event definitions exist; browser-local counters are not aggregate | No endpoint or first-party click/order reports | Configure privacy-reviewed analytics; obtain authorized Associates reports; add provenance to the ledger | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| What commissions or revenue are realistic? | No qualifying order or commission evidence is recorded | Current rates, attribution, conversion, and order data are unavailable | Obtain current account reports and applicable program terms; do not forecast beforehand | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| What analytics and email data handling is acceptable? | No endpoint or email provider is connected | Hosting, retention, consent/notice, access, and data subject process are undecided | Select a provider and document the full data lifecycle before enabling collection | [FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) |
| Is original product testing feasible? | Current comparisons rely on seller listings | Product access, budget, staff, method, and timeline are unknown | Decide whether to obtain units and publish a repeatable test protocol before making performance claims | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Who owns the cadence and brand decisions? | A proposal register and path chooser exist | No named editor, domain/brand approval, or confirmed publishing capacity | Assign an owner, cadence, and approval process in the decision register | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |

The proposal ledger, open-question register, and decision log are available on the [Direction page](direction.html). Each suggestion should remain a proposal until its evidence, owner, cost, and decision are recorded.

## Release and review status

The repository's current release checks pass on the reviewed tree: `python3 scripts/build_registers.py --check`, `python3 scripts/build_decisions.py --check`, `python3 scripts/build_chrome.py --check`, `python3 scripts/build_sitemap.py --check`, `python3 scripts/build_products.py --check`, `python3 scripts/build_readme.py --check`, `python3 scripts/build_ideas.py --check`, `python3 scripts/check_site.py`, `python3 tools/verify_site.py`, `python3 tools/check_site.py` (42 pages, 6,372 assertions), and `python3 tools/crawl_links.py` (42 pages crawled, 0 broken links, 0 dead anchors, 0 orphans). The coordination history records a successful GitHub Pages deployment at the project URL. These checks validate repository structure and registered content; they do not verify the Associates account, live traffic, external search indexing, or link-report conversion.

- [Open the publication](https://wingbangboozle1-lang.github.io/Prod3/)
- [Suggestions and path chooser](direction.html)
- [Open questions](questions.html)
- [Flagged for Review](flagged.html)
- [Analytics and privacy status](analytics.html)
- [Sources](sources.html)

## Verification pass, 2026-11-20 (third session on this tree)

Two defects found by reading the site against the official pages, both fixed and both now gated.

**1. The Program Policies clause letters were wrong.** Ten places cited Section 2 for the star-ratings rule, the URL-obscuring rule and the shortener
rule. Read live on 2026-11-20, the [Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) (page states *Updated
April 14, 2026*) has Section 2 titled "Links on Your Site" with subsections (a) and (b) only. The three rules are **Section 6, "Content on your Site"**:
**(t)** customer reviews and star ratings, **(v)** obscuring the referring URL, **(w)** unclear link shortening. Every citation was corrected, the quoted
wording and its read date are in `data/policy-clause-map.json`, and gate `D35` fails the release if a retired letter returns. Published as FLG-037,
beside the earlier FLG-020. The conduct never changed; only the reference did.

**2. The pages read as template output.** All eight evergreen articles closed with a byte-identical five-product block, and every product card on the
front page printed its spec pills twice (the second copy HTML-entity-encoded, so it rendered as a near-repeat). Each article now closes with a next step
specific to its own argument, the duplicate pills are removed, and gate `D36` fails the build if an article-length block repeats. Published as FLG-038.

**Also checked and left alone:** every food-safety temperature and rest time on the [cook-to-temperature card](tools/cook-temperatures.html) matches the
[USDA FSIS chart](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/safe-temperature-chart), and the accuracy
article's position on NIST matches [NIST's own traceability policy](https://www.nist.gov/metrology/metrological-traceability) ("only measurement results
are traceable"; NIST does not endorse products and forbids references to it in advertising).

**Not claimed here:** whether the five supplied short links work for a signed-in reader. Three dated observations exist for 2026-11-20 and they disagree;
they are kept side by side in `data/products.json`, and only the owner's click inside the enrolled Associates workflow settles it (Q-02 + Q-22).

# Addendum — 2026-11-20, reader-first repair (session arena/0b7a3dd6-prod3)

**What this session changed.** Two buy buttons were repaired rather than re-worded, and four
defects found by reading the tree against its own registers were fixed.

1. **The dual-basket buy button.** `compare.html` and the holiday gift guide still sent readers
   through `link.amazon/B04G1MEwY` — the one supplied link recorded as ending at Amazon's
   homepage — while `index.html` and `air-fryers.html` already used the product page. All four
   agree now. The short link is unchanged on the evidence pages and is still described as
   unresolved, not invalid.
2. **The ThermoMaven button is disputed, not broken.** Three same-day checks disagree about where
   the supplied links land (FLG-025, FLG-031). The recorded decision in FLG-019 not to swap buttons
   to bare `/dp/` URLs (it would remove tracking) is respected: the button is unchanged and a
   fallback product link plus both readings now sit beneath it.
3. **Duplicate flag identifiers.** `flagged.html` carried two different cards numbered FLG-020 and
   two numbered FLG-021, so following either citation could land on the wrong card. Resolved (now
   recorded as FLG-027). Gate `D19` ended in `or True` and could never fail; it now fails on a
   repeated identifier and was negative-tested.
4. **Seven product links were indistinguishable.** A bare "Listing" ×5, "Amazon listing" ×5 and
   "Check price" ×5 pointed at different products. Each now names its ASIN in text and
   `aria-label`; new gate `P14b-unique-link-name`.
5. **One review surface.** `ideas.html` now opens with a brief generated from the registers — its
   counts cannot drift — carrying the seven decisions in dependency order, fifteen
   missing-information rows (each with the exact place the answer lives), and ten question-shaped
   research directions with the source each would need. Gated by `build_ideas.py --check`.

**What was not done, and why.** This build environment could reach only `github.com` and package
registries; `amazon.com`, the Associates policy pages, `ftc.gov` and `developers.google.com` were
not reachable. **No listing or policy page was re-fetched and no new observation date is
published.** Every change above is a consistency check of the tree against its own registers plus
source-code fixes. That limit is published to the reader on `ideas.html` §4. No browser binary
could be downloaded, so no screenshot-based visual check was performed and none is claimed.

**Open for the owner, unchanged:** FLG-001 intended ASINs · FLG-006 Special Link test · FLG-010
account status · FLG-025/031 link resolution · **FLG-026: no shipped link carries a visible tag
parameter** · Search Console (Q-18) · analytics endpoint (Q-13).


## Addendum — 2026-11-20, session arena/26285b01-prod3 (T-58)

Register-integrity pass. Three sessions renumbering flags and register rows in
parallel produced the defect class closed here: the same identifier naming
different findings wherever a merge dropped a renumber. One id now means one
thing (FLG-024..FLG-038, SG-01..SG-47, Q-01..Q-29, DT-01..DT-13); the
DIRECTION.md suggestion index is generated from `data/suggestions.json` so it
cannot drift again; gate D44 (negative-tested) fails the build when any surface
cites an id no register defines. Reading still finds what gates cannot: this
pass corrected five wrong-subject citations (air-fryers.html and
data/products.json named a retired flag number for the F-01 capacity conflict;
data/open-questions.json named two renumbered findings by their old ids, now
FLG-031 and FLG-028; the suggestions premise named the wrong flag for the
FLG-029 gap; about.html cited SG-19 for SG-24's named-editor subject) and
registered DT-13 for the question DIRECTION.md mis-cited as "DT-11 territory".

Two items stay open for review, neither blocking: `data/flagged.json`'s
id_policy note describes two placeholder flag ids (the second id-collision
record; the ids themselves are listed in that note and in PR #77's
description) as published records that no page in this tree publishes (they
may land with an open session PR — logged on COORDINATION.md as a request), and whether SG-21 ever held a different proposal
is now the owner's call (DT-13). A self-hosted, privacy-preserving analytics
collector ships as deployable code (`analytics/collector/worker.js`, with
deployment steps and the payload contract in `analytics/collector/README.md`);
its endpoint stays blank until the owner deploys it and publishes a privacy
notice, and gate D43 keeps the client, server and ledger event contracts
identical and the endpoint honest. All release gates pass on the PR branch;
the ledger remains empty and no forecast of any kind was computed.

---

# Addendum — 2026-11-20, publication-quality round (T-75…T-78, PR #88)

**What this round shipped.** (1) The front page reads like a shop: a clearer hero ("Five kitchen tools, sorted by the cook they belong to."), and the featured pick's headline figure corrected to "2 × 3 qt" so no disputed total volume is stated as fact while the listing conflict is open. (2) Two new question-shaped evergreen guides — "Are air fryers worth it? Six questions to ask before you decide" and "Do you need a smart meat thermometer? Five questions before you pay for WiFi" — in the current guide template (Article + BreadcrumbList structured data, dated byline), wired into the front-page grid, the buying-guide clusters and the category read-next boxes, carried in the RSS feed and sitemap, and verified live after deploy. (3) SG-55 registered: a dated voice refresh for the 2026-11-19 guide batch, as a reviewable proposal. (4) Demonstrable defects fixed: duplicated read-next links on the air-fryer shelf, a D40 guide-count word list that could not see counts above "twelve", and stale guide counts across Q-14/Q-17, the front page, README, the Direction digest and these summaries.

**What the round deliberately did not do.** It dropped three in-flight changes that the merged register answered better: a parallel flag-ID renumbering (the merged mainline's scheme stands), FAQPage structured data (SG-44: Google's FAQ rich result is gone; the visible FAQ text stays, the markup does not), and register rows that duplicated coverage already on the mainline (PageSpeed → Q-29/SG-46, seasonal → SG-43). Nothing was discarded from any other session during the three board-collision reconciliations; the claim chain T-48…T-51 → T-66…T-69 → T-71…T-74 → T-75…T-78 is recorded in COORDINATION.md.

**Merged and deployed.** PR #88 (merge commit `a5a100e`), Pages run `44697488609` success; both new guides and the new hero fetched from the live site after the deploy. Still not established (unchanged owner gates): intended product identities (FLG-001), Special-link compliance (FLG-006/FLG-026, Q-24), account status (FLG-010), the short links that end at the homepage (FLG-025/FLG-031, Q-25), Search Console data (Q-28), Core Web Vitals (Q-29), share-debugger validation (Q-21/F-21), Pages build_type (FLG-024). No traffic, demand or conversion is claimed for the two new guide topics: they are editorial hypotheses until Q-27/Q-28 return data.
