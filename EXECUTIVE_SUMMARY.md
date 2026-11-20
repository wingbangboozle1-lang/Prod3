# Executive summary — Kitchen Counter

**Purpose:** A buyer-facing Amazon Associates publication for air fryers and meat thermometers, with product comparisons, question-led guides, clear disclosures, and a reviewable decision register.

**Tracking ID:** `shopnow047c-20` (provided for the project; Associates account enrollment and eligibility are not confirmed — FLG-010).

**Status date:** 2026-11-20. Product and policy facts below reflect the repository's dated source records; the listing snapshot date is 2026-11-19. On 2026-11-20 the five supplied short links were fetched three separate times by three sessions, with different results each time: four of five reached product pages, then three of five, then — on the most recent pass (session 6bf60cac, ~07:0x UTC) — **none of the five**, with every final URL reading `https://www.amazon.com/`. All four dated observations are kept side by side in `data/products.json`; none is overwritten and no cause is asserted (FLG-017, FLG-023, FLG-025). Separately, the Associates Program Policies (updated 2026-04-14) §2(b) require the Associates tag as a parameter in each link's URL, and no shipped anchor on this site carries one in the URL the reader receives — recorded as FLG-026, with the caveat that a short-link service may add the tag downstream (Q-24). No price, rating or offer was recorded.

## Bottom line

The publication site is built and the repository's release gates pass. The reader-facing front page leads with five product listings, a three-question chooser, category pages, a comparison, a buying guide, and nine question-shaped articles (eight evergreen guides plus the dated Thanksgiving temperature plan), one generated spec page per product, and a dated twelve-row publishing plan. Every page has the Associates disclosure above its first heading and repeats it in the footer. Amazon links are marked `rel="sponsored"`.

**Recommendation:** keep the current editorial publication, but do not scale links or claim revenue performance until the owner-side Associates workflow confirms the intended products, link compliance, and tracking. The site does not have aggregate analytics, verified Search Console data, or conversion reports. Consequently, there is no evidence here for product superiority, demand, conversion rate, commission potential, or revenue forecasts.

## Five submitted links: what is and is not known

The supplied short-link tokens and their observed redirect targets are recorded separately in `data/products.json`. The observations below were captured on 2026-11-19; the 2026-11-20 re-check is recorded beside them in `data/products.json` (`live_recheck_2026_11_20`). Intended product identity remains unconfirmed for every link. The intended-ASIN, intended-listing, confirmation-date, and confirmation-source fields remain blank by design.

| Submitted token | Observed listing at snapshot | Category | Intent confirmed? | Source |
|---|---|---|---|---|
| `B04G1MEwY` | Chefman 6 Qt Dual Basket · `B0CDY277D3` (2026-11-19); 2026-11-20 re-check ended at the Amazon homepage — FLG-017 | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B0CDY277D3) |
| `B02NbDxp3` | Emeril Lagasse 26QT French Door · `B09B7SB46R` | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B09B7SB46R) |
| `B00hJ57DV` | Chefman 8 Qt TurboFry · `B08DKYBTPH` | Air fryer | No | [Official Amazon listing](https://www.amazon.com/dp/B08DKYBTPH) |
| `B0c8moW59` | ThermoMaven instant-read · `B0DHZTCNR5` | Meat thermometer | No | [Official Amazon listing](https://www.amazon.com/dp/B0DHZTCNR5) |
| `B0f3GKalj` | CHEF iQ Sense Gen3 · `B0DZFD6R9Z` | Meat thermometer | No | [Official Amazon listing](https://www.amazon.com/dp/B0DZFD6R9Z) |

**Important distinction:** the observed destination is evidence of where a supplied link resolved during that dated check; it does not prove that destination is the product the owner intended or that the link has been tested in the enrolled Associates account. FLG-001 and FLG-006 remain open. Do not describe the supplied short links as invalid: their exact compliance status is unresolved.

**Correction (2026-11-20, FLG-018/019):** earlier 2026-11-19 records had copied observed ASINs into the intended-ASIN fields and cited a NIST reference page as their source. Those intended fields are now blank, and a release gate blocks any intended ASIN without an owner-confirmation record. The policy record also said product buttons go straight to `/dp/` URLs; the buttons actually use the supplied short links, and the `/dp/` URLs are separate source links. Both corrections are recorded.

## Current capabilities and evidence limits

| Area | Current state | What is not established | Official source |
|---|---|---|---|
| Publication | Buyer-first front page; two category pillars; comparison and buying guide; nine articles (eight evergreen plus the dated Thanksgiving plan); five per-product spec pages; a twelve-row publishing plan; three decision tools; RSS feed and sitemap | Organic impressions, rankings, readership, or topic popularity | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
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
Direction desk was rebuilt as a full ledger (SG-01…18 with statuses, Q-01…21
with discovery paths) and now matches `data/suggestions.json` /
`data/open-questions.json` exactly. New open item: FLG-016 / F-21 — the SVG
social-preview image is unverified in share previewers. All four release gates
pass on the rebuilt tree.


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
elsewhere. SG-21 was retired in place rather than deleted, so the change can be audited, and
gate rule `D20` now fails the build if any two live suggestions share a title.

**Nothing was softened.** No price is rendered anywhere. Every Amazon anchor is
`rel="sponsored"`. The exact §5 disclosure sentence appears in the strip and the footer of all
30 pages. Every new table row carries a source link or an explicit "No official source" marker,
and the gate fails a row that has neither — so "unverified" can never hide.

**Still true, still not this session's to fix.** The five short links carry no visible
`tag=shopnow047c-20`; the enrolled-account test has not been run (DT-01, FLG-006), and one of
them no longer reaches its product at all (FLG-017). There is no
analytics endpoint and no Search Console property (DT-03, DT-07). Every figure remains a seller
statement, because nothing has been purchased or tested (DT-05). These are owner actions with
minutes-scale costs, and they are published on `decisions.html` rather than buried here.

**Gates at close:** `build_chrome --check`, `build_registers --check`, `build_decisions --check`,
`build_sitemap --check`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`
(30 pages, 3541 assertions) and `tools/crawl_links.py` (30 pages, 0 broken links, 0 dead
anchors, 0 orphans) all pass on the merged tree.

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

## Questions that must be answered before consequential decisions

| Question | Known from repository | Unknown / why it matters | How to discover it | Official source |
|---|---|---|---|---|
| What product was intended for each submitted link? | Five observed destinations are documented separately | Intended ASIN and listing remain blank; product matching cannot be assumed | Confirm each in the Associates account and record date, official listing URL, and source | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Is `shopnow047c-20` enrolled and eligible for the intended activity? | Tracking ID was supplied | Account state, eligibility, and API access are not visible to this repository | Check Associates Central; save only non-sensitive confirmation/status and date | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Do the Special Links work as intended and report under this ID? | Outbound links are marked sponsored in the site | Account-side link compliance and report attribution are untested | Test one product link in the enrolled workflow; confirm destination and report before scaling | [Amazon Associates Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) |
| Which topics attract qualified visitors? | Eight guides and the technical SEO files exist | No Search Console impressions, clicks, or query export | Verify Search Console and review dated query reports after sufficient data accrues | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Are visits turning into outbound clicks or orders? | Event definitions exist; browser-local counters are not aggregate | No endpoint or first-party click/order reports | Configure privacy-reviewed analytics; obtain authorized Associates reports; add provenance to the ledger | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| What commissions or revenue are realistic? | No qualifying order or commission evidence is recorded | Current rates, attribution, conversion, and order data are unavailable | Obtain current account reports and applicable program terms; do not forecast beforehand | [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) |
| What analytics and email data handling is acceptable? | No endpoint or email provider is connected | Hosting, retention, consent/notice, access, and data subject process are undecided | Select a provider and document the full data lifecycle before enabling collection | [FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) |
| Is original product testing feasible? | Current comparisons rely on seller listings | Product access, budget, staff, method, and timeline are unknown | Decide whether to obtain units and publish a repeatable test protocol before making performance claims | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| Who owns the cadence and brand decisions? | A proposal register and path chooser exist | No named editor, domain/brand approval, or confirmed publishing capacity | Assign an owner, cadence, and approval process in the decision register | [Google people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |

The proposal ledger, open-question register, and decision log are available on the [Direction page](direction.html). Each suggestion should remain a proposal until its evidence, owner, cost, and decision are recorded.

## Release and review status

The repository's current release checks pass on the reviewed tree: `python3 scripts/check_site.py`, `python3 tools/verify_site.py`, `python3 scripts/build_registers.py --check`, and `python3 scripts/build_sitemap.py --check`. The coordination history records a successful GitHub Pages deployment at the project URL. These checks validate repository structure and registered content; they do not verify the Associates account, live traffic, external search indexing, or link-report conversion.

- [Open the publication](https://wingbangboozle1-lang.github.io/Prod3/)
- [Suggestions and path chooser](direction.html)
- [Open questions](questions.html)
- [Flagged for Review](flagged.html)
- [Analytics and privacy status](analytics.html)
- [Sources](sources.html)
