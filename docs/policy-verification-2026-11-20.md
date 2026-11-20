# Policy and copy verification memo — 2026-11-20

Session `arena/ba8e7240-prod3` · Tracking ID as supplied: `shopnow047c-20` (assignment **not** verified — see Q-A below)

This memo is the review desk for one round of work: what was checked against a primary source today, what
was found wrong in the site's own copy, what the site should look like next, and what information is still
missing before a decision can be made on the strength of evidence rather than instinct. Nothing here is
implemented by being written down.

## 1. Executive summary

1. **The site was citing real Amazon rules to the wrong section numbers.** The clauses on customer star
   ratings, URL obscuring and link shorteners exist on the live Program Policies page — they are
   Participation Requirements **§6(t), §6(v) and §6(w)**. They are *not* in §2. The site had them as
   §2(t)/§2(v), and after a 2026-11-20 pass that searched Section 2 only, three published rows said the
   wording "was not located". The rules were always there; the pointer was wrong. Corrected in this round
   wherever the file was not owned by another session, and logged as a cross-scope request for the rest.
2. **Four more clauses turn out to bind exactly the automation the project brief asks for.** §6(y) bans
   price-tracking and price-alert functionality without Amazon's agreement. §6(s) bans artificially
   generating clicks or impressions "by way of a robot or software program or otherwise". §6(g) bans
   offering anything of value to get people to use Special Links. §1 requires original content and a
   publicly available site. Each is now a row in the machine-readable policy register, so the publishing
   workflow can fail closed instead of trusting a prompt.
3. **Two compliance decisions the site already made are confirmed correct by today's read** — showing no
   prices (§2(b) is the right citation) and showing no star ratings (§6(t), now that it is located). The
   site's restraint was right even where its footnote was wrong.
4. **The most "generated-looking" defects found by reading the live pages are cheap to fix and were found
   by eye, not by a gate.** On the front page, four of five product cards print the same figures twice in
   two adjacent chip rows (e.g. `75–500°F` and `1700W` appear in both rows of the same card), the two
   thermometer cards carry no chips at all while the three air-fryer cards do, four inline hex colours
   bypass the palette, and every card repeats the price sentence twice (a "Current price on Amazon" line
   plus a "Check price on Amazon" button). The shop pages are owned by an active parallel session, so
   these are filed as a request with exact line references, not edited under someone else's claim.
5. **Nothing in the compliance picture can be closed from outside the account.** Intended ASINs, the
   Associates ID on live links, and the Special Link test are still owner-only (FLG-001, FLG-006, FLG-010).
   Today's read adds one reason not to improvise: the "tag as a parameter in the URL" wording is a direct
   quote from §2(b), so an untagged link is a tracking failure before it is a policy question.
6. **The link picture got worse and better in the same hour.** This session re-tested two of the five supplied
   short links and both landed on the correct product page (§7a) — where two earlier records from today read a
   homepage landing, and where 18 of the site's 25 buy buttons still route readers through that same
   inconsistency. Nobody's record is overwritten; the practical conclusion is the same one SG-13 already
   reaches, and it is now the only blocker worth an hour of the owner's time before anything else ships.

## 2. What was read today, and where to check it

Every row below was fetched and read on 2026-11-20 by this session. "Located" means the exact text was
found in the served page; the quote is copied from it.

| # | Source read (live, 2026-11-20) | What it settles |
|---|---|---|
| 1 | [Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies) — page header reads "Updated: April 14, 2026" | Participation Requirements §2 has subsections **(a) and (b) only**. There is no §2(t) or §2(v). |
| 2 | Same page, §2(a) "Special Links" | "Special Links must use the Associates ID we have assigned to you." |
| 3 | Same page, §2(b) "General Requirements Applicable to All Special Links" | Tag-as-parameter rule, price/availability rule, comparison-format rule, misleading-claims rule, sub-tag rule, product-list original-content rule, limited-time promotion removal duty, no-bookmark rule, direct-access rule — all in §2(b), quoted in §3 below. |
| 4 | Same page, §6 "Content on your Site", subsections (a)–(z) | **§6(t)** reviews/star ratings, **§6(v)** URL obscuring, **§6(w)** link shortening, **§6(y)** price tracking and alerting, **§6(s)** artificial clicks and impressions, **§6(g)** incentives for using Special Links, **§6(n)** framing, **§6(p)** Special Links inside Amazon customer-generated content. |
| 5 | Same page, Participation Requirements §1 "Enrollment and Eligibility" | Original content and public availability are eligibility conditions, not style advice. |
| 6 | Same page, Commission Income Statement §1(b), §5 | The 24-hour Session, 89-day cart window and 180-day shipment condition; and the dual-attribution prohibition that can withhold commissions. |
| 7 | [Associates Program Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) | **§5 "Identifying Yourself as an Associate"** carries the exact disclosure sentence. **§6** — not §5 — is what deems a §5 violation a material breach. |
| 8 | [USDA FSIS — Leftovers and Food Safety](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/leftovers-and-food-safety) — footer reads "Last Updated: Jul 31, 2020" | Reheat leftovers to 165°F; sauces, soups and gravies to a rolling boil; cover to reheat; 3–4 days refrigerated, 3–4 months frozen; the danger zone is 40–140°F; hot food held at 140°F or warmer; 2 hours out (1 hour above 90°F) and it goes. The page names a saucepan, a microwave or an oven for reheating from frozen — it does not name an air fryer. |

Sources 1–6 are the same document the register already carries as **S02**; source 7 is **S01**; source 8 is
a USDA page the register does not yet list (the register has the FSIS temperature chart as S17 and the probe-placement
release as S18). Adding a source ID belongs to the session holding `data/sources.json` — requested in §6.

## 3. The exact wording, so nobody has to take my word for it

Quoted from the served pages on 2026-11-20. Reproduced here because they are the ground for several
proposals below and for two flags.

**Participation Requirements §6(t) — ratings.**
> You will not display or otherwise use any of our customer reviews or star ratings, in part or in whole, on
> your Site unless you have obtained a link to that customer review or star rating through Creators API or PA
> API and you comply with the requirements for Creators API and PA API described in the License.

Note the shape of the permission: the API supplies **a link** to the review or rating. That is narrower than
"we may print the star count", which is how the old footnote read on this site.

**Participation Requirements §6(w) — shorteners.**
> You will not use a link shortening service, button, hyperlink or other ad placement in a manner that makes
> it unclear that you are linking to an Amazon Site.

The test is clarity to the reader, not the existence of a short domain. A bare code with no visible
destination and no Amazon label is the failure mode; a clearly labelled button is not automatically one.
This does **not** certify the supplied links — they still have to pass §2(a)/§2(b) on the tag, which is the
open owner-only question (FLG-006).

**Participation Requirements §6(v) — obscuring.**
> You will not cloak, hide, spoof, or otherwise obscure the URL of your Site containing Special Links
> (including by use of Redirecting Links) or the user agent of the application in which Program Content is
> displayed or used such that we cannot reasonably determine the site or application from which a customer
> clicks through such Special Link to an Amazon Site.

**Participation Requirements §2(b) — the tag.**
> For example, you must include your Associates ID or "tag" (appearing as XXXXX-##, or such other format as
> we may designate) as a parameter in the URL of each link you place on your Site to an Amazon Site.

**Participation Requirements §2(b) — prices.**
> Because prices for and availability of Products that you have listed on your Site may change, your Site may
> only show prices and availability if: (a) we serve the link in which that price and availability data are
> displayed, or (b) you obtain Product pricing and availability data via Creators API or PA API and you comply
> with the requirements regarding use of Creators API or PA API in the License.

**Participation Requirements §6(y) — price alerts.**
> Unless otherwise agreed by Amazon, your Site must not have price tracking and/or price alerting functionality.

**Participation Requirements §6(s) — synthetic traffic.**
> You will not artificially generate clicks or impressions on your Site or create Sessions on an Amazon Site,
> whether by way of a robot or software program or otherwise.

**Participation Requirements §6(g) — incentives.**
> You will not offer any person or entity any consideration, reward, or incentive (including any money,
> rebate, discount, points, donation to charity or other organization, or other benefit) for using Special Links.

**Participation Requirements §4 — email and messaging.**
> You may include Special Links in emails, SMS and direct messaging from your social media Sites; provided,
> that such communications are solicited (i.e., opted into by the receiving customer) and are otherwise in
> compliance with the Agreement, the Trademark Guidelines, and the Amazon Brand Usage Guidelines.

**Participation Requirements §1 — eligibility.**
> Your Site(s) must contain original content and be publicly available via the website address provided in
> the application. Original content utilizing third-party materials must contain significant commentary,
> analysis, or transformation to any materials you include.

**Operating Agreement §5 — the disclosure, verbatim.**
> You must clearly and prominently state the following, or any substantially similar statement previously
> allowed under this Agreement, on your Site or any other location where Amazon may authorize your display
> or other use of Program Content: "As an Amazon Associate I earn from qualifying purchases."

**Operating Agreement §6 — the consequence.**
> For the avoidance of doubt and without limitation for purposes of the foregoing subsection (a) any
> violation of Section 5 and as specified in the Program Policies will be deemed a material breach of this Agreement.

**Operating Agreement §5, second half — a reading this site should not resolve alone.**
> Except for this disclosure, and other than as required by applicable law, you will not make any public
> communication with respect to this Agreement or your participation in the Associates Program without our
> advance written permission.

The site's `disclosure.html` and `flagged.html` pages describe policy obligations in public. This is not
asserted to be a breach — the ordinary reading of that sentence targets promotional claims *about* the
relationship, and "other than as required by applicable law" covers FTC-style disclosure — but the clause
exists, it is quoted above, and it is a question for the owner's legal review rather than for an agent
(session question Q-E below).

## 4. What changed in this round, and what was deliberately not touched

| Surface | Change | Why this session could make it |
|---|---|---|
| `data/policy-checks.json` | C-04 restated with the located §6(w) text; C-01 corrected to "§5 names the sentence, §6 makes it a material breach"; C-05, C-06, C-11, C-13 given the located subsection text; six new rows **C-15..C-20** for §6(t), §6(y), §6(s), §6(g)+§4, §6(n)+§6(p), §1 + CIS §5 | Not claimed by another session |
| `compare.html` | The Ratings footnote no longer cites §2(t); it cites §6(t) and drops the claim that the API returns a rating to print | Not claimed |
| `ideas.html` | Rejected-idea rows corrected to §6(t), and a new rejected row for **price-drop alerts** on the §6(y) ground; a new block of paste-ready design inputs for the next polish pass | Not claimed |
| `DIRECTION.md` | Dated rows: the citation correction, the new policy-register rows, and the design-brief publication. The digest's suggestion index was rebuilt from the final register — it had drifted at SG-32 while upstream filled SG-32..SG-42 — and the open-questions count corrected | Not claimed |

### 4a. Register nits found while working, listed rather than fixed

- `suggestions.html`, `questions.html` and `citations.html` all render the byline "Register updated
  2026-11-19" from a literal in `scripts/build_registers.py`, while the data files carry a `generated` field
  that this round moved to 2026-11-20. One-line fix in a file owned by T-46: read the field instead of the
  literal. A register that dates itself wrongly is the kind of detail that makes a reader distrust the numbers
  next to it.
- `tools/verify_site.py` asserts the feed has exactly nine items. The article count changed once already this
  week and will change again; the assertion should be derived from the `articles/` directory (requested in §6).
- `data/flagged.json` holds FLG-017 with `status: open` while `data/products.json` records a later same-day
  observation; §7a adds a third. Nothing here picks a winner — the flags exist so a human can.
| `data/suggestions.json` + regenerated `suggestions.html` | **SG-43..SG-48**, six design-brief rows in the register (they arrived as SG-36..SG-41 and were
renumbered on rebase when upstream filled those IDs with different proposals)'s own format, each with the defect, the evidence, the options and a recommendation | suggestions.json is free; the generator was run unmodified |

Left alone because an active parallel session (`arena/59a087a1-prod3`, T-46, claiming `data/citations.json`,
`data/flagged.json`, `flagged.html`, `README.md`, `index.html`, `air-fryers.html`, `meat-thermometers.html`,
`articles/*`, `tools/*`) holds those files: the FLG-020 "not located" text, the README's duplicated register
table, the `citations.html` footnote, and every card-level copy fix in §5. Requests with exact file and line
references are in §6 — that is the whole point of the board: the fix ships, just not twice.

## 5. The shop-polish list — read this as "make it look bought-for, not generated"

These are the concrete tells found by reading the served HTML today. They are small, and they are exactly
what separates a shop from an audit.

1. **Same card, two chip rows, same numbers twice.** Front page, Emeril card: row one says
   `75–500°F · 1700 W · 16.9 × 15.8 × 14.8 in`; row two says `26 qt oven · 75–500°F · 1700W`. The 8 Qt,
   ThermoMaven (`±0.5°F` twice, "IP67 claimed" vs "IP67 claim") and CHEF iQ (`WiFi + Bluetooth` twice) cards
   do the same. A shopper reads two rows of near-identical pills and concludes a template filled them.
   *Fix:* one row, three distinct figures — the number that constrains the choice, the one that surprises,
   and the footprint.
2. **One entity is spelled two ways on one card.** `75–500°F` (a literal degree sign) and `75–500&deg;F`
   (an entity) render identically but sit adjacent in the source; `1700 W` vs `1700W`. Normalise to one form
   per component so the CSS, not the markup, decides spacing.
3. **The two shelves have different anatomy.** Every air-fryer card has a chip row; neither thermometer card
   has one, and the thermometer shelf has no `spec-chips` at all. Same product type, same card, different
   information density reads as "half the template was written".
4. **Four inline hex styles on the front page** (`style="color:#fff"`, `#fdba74`, `#e6d9c8`,
   `background:linear-gradient(135deg,#292524,#57534e)`) are colours that appear nowhere in
   `assets/style.css`. Foreign pasted colours are the single most recognisable generated-page tell. Move them
   onto tokens in the stylesheet.
5. **The price sentence appears twice per card.** A `Current price on Amazon` line and a
   `Check price on Amazon` button say the same thing; the line looks like a field left empty by an import.
   Drop the line, keep the button. No policy change — the gate that forbids rendering currency stays green.
6. **The "look elsewhere if" copy is the best line on the page and it is buried.** On the feature card it is
   the third paragraph. A shop that earns trust puts the disqualifier next to the button, because that is
   where the decision happens. (This is also the honest answer to "make it read like a publication": the
   differentiator here is not prose polish, it is that the page tells you who the product is *not* for.)
7. **Seasonal block has an expiry the site does not mention.** Thanksgiving 2026 is Thursday 2026-11-26.
   The front-page block currently links two dated tiles. §2(b) obliges an associate to remove references to a
   limited-time promotion as soon as it ends; the practical version here is a scheduled sweep date on the
   block, and a replacement tile — the leftovers guide in §7 — rather than a front page that quietly goes
   stale on November 27.

## 6. Requests to other scopes (do not implement twice)

- **`data/citations.json` / `citations.html`** (T-46): the S02 row reads "2(t) and 2(v) wording not located in
  Section 2 on 2026-11-20". Replace with "§2 has (a) and (b) only; the reviews and obscuring clauses are
  §6(t) and §6(v); located 2026-11-20". Same sentence appears in the "Customer star ratings" bullet below the
  table.
- **`data/flagged.json` / `flagged.html`** (T-46): FLG-020 can close as *resolved with a correction*: the
  clauses were never missing, they were mis-numbered. Keep the lesson visible — a Section-2-only search was
  the method that produced the false negative.
- **`README.md`** (T-46): two register tables are published, one headed "as of 2026-11-19" and one "as of
  2026-11-20". The first is stale (it lists SG-01..SG-31 while SG-32..SG-41 exist). Requested by
  `arena/9f36f5ee-prod3` earlier and still open.
- **`index.html`, `air-fryers.html`, `meat-thermometers.html`, `assets/style.css`** (T-46): items 1–6 of §5,
  with the exact cards named there.
- **`data/sources.json`** (T-46): register the USDA FSIS *Leftovers and Food Safety* page (next free ID, S34
  as of writing) with `used_for` naming the 165°F reheat rule and the 3–4 day refrigeration window. Until it
  is registered, no data row may cite it — D06 fails dangling IDs by design.
- **`tools/verify_site.py`** (T-46): the feed assertion is a literal `len(items) == 9`. It should count the
  `articles/` directory instead; a hardcoded count is how a feed silently loses an item.
- **`.github/workflows/pages.yml` / repo settings** (owner, FLG-024): the Pages source is still `legacy`, so
  a redundant deploy run fires on every push to `main` and can show a failure behind a successful one.

## 7. One guide the site can publish without inventing anything

Topic: reheating leftovers, timed to the week it matters, and the reason a thermometer survives the
refrigerator. Verified facts, all from source 8 above:

- reheat leftovers to **165°F**, measured with a food thermometer; sauces, soups and gravies come to a
  **rolling boil**; cover the food;
- reheating from frozen is allowed in an oven or microwave and takes longer;
- **3–4 days** refrigerated, **3–4 months** frozen;
- the danger zone is **40–140°F**, hot food holds at **140°F or warmer**, and two hours out (one above 90°F)
  ends it;
- the guidance names a saucepan, a microwave, or a conventional oven for reheating — **not an air fryer**, so
  the article must say that plainly rather than imply endorsement of a method;
- the appliance-side fact the site can honestly add from its own dated listing snapshots: two of the three
  air fryers list a **200–450°F** and **200–400°F** range, so the low end of the range is above the USDA's
  140°F holding temperature and the third (75–500°F) reaches below it. That is a spec comparison, not a
  test result, and it answers a question nobody else on the internet answers for this product set.

Why it earns a slot: it is a real question with a real date, it has an official source with numbers, it
sells the thermometer honestly (the rule is a *measured* temperature), and it is not the sentence-shape
"best X for Y" filler that makes affiliate pages smell generated. Blocks: it needs the S34 registration
first (§6) so the source column can be filled rather than marked unverified.

## 7a. A fourth dated link observation, from this session, at 06:57–06:58Z

Read by following the URL and recording the final address the page was served from. No purchase, no
session-forging, no tag appended — a page read, not a click. Prices shown on those pages are deliberately not
recorded here or anywhere in the repository (Participation Requirements §2(b); policy check C-05).

| Supplied link | Final address read at | What it shows | vs. the other 2026-11-20 records |
|---|---|---|---|
| `link.amazon/B04G1MEwY` | `amazon.com/dp/B0CDY277D3` (P-01, Chefman 6 Qt Dual Basket) — product page, browse path `Home & Kitchen › … › Air Fryers` | 2026-11-20 06:57Z | **Disagrees** with the record that read the Amazon homepage for this token on 2026-11-20; **agrees** with the 2026-11-19 ASIN |
| `link.amazon/B0c8moW59` | `amazon.com/dp/B0DHZTCNR5` (P-04, ThermoMaven) — product page, browse path `… › Thermometers & Timers › Meat` | 2026-11-20 06:58Z | **Agrees** with one same-day record and with 2026-11-19; the other same-day record read the homepage (FLG-023) |

Three things this settles, and one it does not:

- **The behaviour is not stable across attempts.** Three dated records on 2026-11-20 alone disagree with each
  other about the same token. A shopper's single click should not depend on that. It is the strongest
  argument yet for SG-13 (regenerate the product links inside the enrolled workflow), which is already the
  register's open proposal — this round adds evidence to it rather than a competing proposal.
- **`plpRedirect=mhFallback` appears in both resolved URLs.** Read literally, the parameter names a
  homepage-fallback path in the redirect chain. That is an observation about a query string, *not* a
  proven cause of the homepage landings other sessions recorded, and no cause is asserted here.
- **Neither resolved URL carries a visible `tag=` parameter.** §2(b) requires the Associates ID to appear as a
  parameter in the URL of each link to an Amazon Site. Absence in the final URL is not proof of absence in the
  attribution chain — which is exactly why Q-B has to be answered signed in, from the report, and not by an
  agent reading a URL bar.
- **Not settled:** the other three tokens were not re-tested in this round (the fetch budget went to the two
  whose records disagree). The site-wide count, from the built HTML at commit time, is **25 product buttons on
  10 pages, 18 of them routed through `link.amazon/…` and 7 through direct `/dp/` addresses**; 435 Amazon-domain
  anchors across 37 pages, all carrying `rel="sponsored noopener"`; the disclosure strip present on all 37.

## 8. The decision gate: what has to be answered, by whom, and what it unblocks

Each row states the question, what a good answer looks like, who can produce it, and what stays frozen until
they do. This is the list that separates "we can build it" from "we can ship it".

| ID | Question | What a complete answer looks like | Who | Blocked until answered |
|---|---|---|---|---|
| Q-A | Is `shopnow047c-20` a tracking ID on an enrolled, eligible, in-good-standing account, and is this site listed as a Site in the account? | A dated screenshot-or-note: ID present, status, the registered site URL | owner, minutes | Whether the disclosure describes a live relationship; whether any link can earn; whether the site is even eligible (§1 requires the site be identified in the application and publicly available) |
| Q-B | Do the five supplied `link.amazon/…` links carry the tag when a reader arrives, and do they land on a Product? | The final URL of each of the five, read while signed in, showing `tag=shopnow047c-20` or not, plus the landing page's ASIN | owner, minutes | Whether the five product buttons stay on the short links or move to freshly generated Special Links; FLG-001, FLG-006, FLG-026 |
| Q-C | Which ASIN did the owner mean for each of the five tokens? | Five intended ASINs + listing URLs + a confirmation date + the source of the confirmation, kept in the intent fields and never merged with observed redirects | owner | The product-intent record stays blank by design; nothing about "this page is about product X" can be asserted |
| Q-D | Is the site's public description of its obligations inside §5's permission, or does it need rewording? | A yes/no from whoever owns the legal reading, or a reword to "we follow Amazon's published program policies and the FTC's endorsement rules" without quoting the Agreement's section numbers | owner / legal | Whether `disclosure.html`, `flagged.html` and `citations.html` keep naming Agreement sections in public copy |
| Q-E | Does the owner want prices at all? If yes, on which pipe? | Either "no" (status quo, and the comparison table stays spec-only) or a Creators/PA API credential path, plus the §2(b) comparison-format consequence: showing a price in a comparison alongside non-Amazon prices obliges showing the lowest new (and, where provided, lowest used) Amazon price | owner | DT-02 stays open; a weekly "price refresh" automation stays out of scope permanently under §6(y) if it becomes alerts |
| Q-F | Which events does the owner want counted, and where do they land? | A named store and schema — or a written "no endpoint": GitHub Pages cannot receive POSTs, so self-hosting means a second service | owner + editorial | The five event types stay local-only; the campaign ledger stays empty; no conversion or revenue claim can be made |
| Q-G | Is there a Search Console property, verified, with the sitemap submitted? | A verified property, a submitted `sitemap.xml`, and 28 days of query data | owner | Choosing guides from measured queries instead of hypotheses (SG-07, SG-18) |
| Q-H | Who is the author, and what have they actually done? | A name, a real bio, and a statement of what they have used versus only read | owner + editorial | Every byline stays organisational; no experience claim can appear; "not a lab" stays in the hero |
| Q-I | What is the review-and-merge authority for flagged rows? | A rule: which flags an agent may close unilaterally (a wrong section number) and which need a human (anything touching account status, links, money) | owner | FLG-020-style closures; whether this memo's §6 requests get applied by the next session or by a human |
| Q-J | What does "polished" mean to the owner, measurably? | A pick among the SG-43..SG-48 rows, plus one reference site the owner would call good, and one they would call slop | owner | Whether the shop-page fixes ship as a set or a subset; a design brief with no reference point produces more of what is already there |

## 9. Missing information that no one has asked for yet

These are gaps the registers do not currently carry. They are the ones that hurt later, so they belong in
`data/open-questions.json` (T-46's file — requested here rather than written there):

1. **Category-node and browse-path confirmation for the five observed ASINs.** The site asserts categories
   from listing pages; it does not record what the Associates rate card pays for those categories. Without a
   dated commission-rate note from the account, "commission potential" in the project brief cannot be
   computed at all — it would be invented.
2. **What the site is allowed to do with listing copy at all.** §6(a) forbids adding to or altering Program
   Content; the site's cards quote spec fields and add editorial judgement. Whether "seller says X, we
   conclude Y" sits on the right side of that line is a judgement the owner should make explicitly, with the
   §6(d) endorsement clause in view, not implicitly in a prompt.
3. **Whether an agent may generate the text at all.** There is no clause in what was read today that bans
   AI-assisted drafting — the binding language is the original-content requirement in §1 and Google's
   quality policies. A project that intends "generates SEO-optimized product articles" at volume should record
   its own line: what a human verified before publish, per article, with a date. Otherwise the automation and
   the eligibility rule collide, and eligibility is the one that can lose the account.
4. **Any prior traffic, ranking or index history.** Not knowable from the sandbox. Until Search Console
   reports exist, the site has no baseline, so "did the new guide work?" has no answer — which is why the
   ledger stays empty rather than filling with estimates.
5. **The owner's stance on the two same-day link observations that disagree** (FLG-023: one record read a
   ThermoMaven destination, another read the homepage, same day, both kept). Whether to re-test on a schedule
   or accept the instability and route readers only through freshly generated Special Links is a decision, not
   a finding.
6. **What happens on November 27.** A post-Thanksgiving date is the first real test of whether this is a
   publication with a calendar or a repository with pages. The seasonal block, the two dated tiles, and the
   feed all need the same sweep decision, and §2(b)'s limited-time-promotion duty gives a policy reason to
   schedule it.

## 10. Suggested paths, with the risk named

- **Path A — earn the basics first (recommended).** Q-A, Q-B, Q-C and Q-G in one sitting; then regenerate every
  product link as a tagged Special Link; then apply the §5 shop-polish set; then publish the leftovers guide with
  S34 registered. Cost: a day, of which the owner's part is under an hour. Risk: near none. Everything else the
  brief asks for is downstream of knowing whether a click can be attributed.
- **Path B — polish first, account later.** Ship §5 now, keep links as-is. Risk: a prettier page whose
  outbound links may still earn nothing, and a front page that sends readers through a link whose behaviour
  changed twice this week.
- **Path C — scale the content.** More guides now, on today's evidence. Risk: this is the path that produces
  the slop the owner objects to. Guides are cheap to write and expensive to be believed; without Q-G there is
  no measurement to choose topics by, and §1 makes thin pages an eligibility problem, not just a taste one.

The register rows SG-43..SG-48 implement the polish part of A and B; they are marked *proposed*, and a mark on
`suggestions.html` is a preference, not a change.

## 11. What upstream changed while this branch was open (re-read at merge time, not assumed)

A parallel session merged several passes during this work. Each request in §6 was re-checked against the
merged tree rather than left standing:

| Request | State at merge |
|---|---|
| Front-page duplicate spec-chip rows (§5 item 1) | **Done upstream** — each of the four affected cards now carries one chip row. SG-43 is therefore a confirmation task, not a change request. |
| `suggestions.html` / `questions.html` / `citations.html` self-dating from a literal | **Done upstream** — the "Register updated 2026-11-19" string no longer appears on any register page. |
| `tools/verify_site.py` hardcoded feed count | **Done upstream** — it now derives the expected count from `articles/` and additionally fails if a guide is missing from the sitemap, the feed or the guides hub. The tree has 10 guides and 10 feed items. |
| `README.md` duplicated register table (§6 item 3) | **Done upstream** — one generated table remains, produced by `scripts/build_readme.py`; this round's regeneration moved its counts to 47 suggestion rows and 27 questions. |
| `citations.html` / `data/citations.json` still said §2(t)/§2(v) "was not located" | **Done upstream while this branch was open** — the published row now reads §2(a)/§2(b)/6(e), and the register carries an explicit `correction` field recording that the three rules are 6(t), 6(v), 6(w). The only remaining "not located" text in the tree is inside that correction sentence, where it belongs. |
| `flagged.html` FLG-020 "citations not located (UNVERIFIED)" | **Closed upstream** — retitled "the letters were wrong and have been corrected", which is the outcome requested here. |
| `tools/check_site.py` refused any §2(x) citation | **New upstream gate, and it passed on this round's edits** — `D35` reads `data/policy-clause-map.json` and rejects a clause letter absent from that map, plus `D36` (no repeated article-length block) and `D40` (a published count must equal the count on disk). This session's six rows cite only clauses in the map. |
| `flagged.html` said "Eight articles…" against 10 guides on disk | **Fixed in this round** — the sentence now scopes the count to the date it was true instead of asserting a number that goes stale. Main was red on this line at merge time; a count a gate can only satisfy by being rewritten every deploy is the wrong shape of assertion. |
| Thermometer cards have no chips; four inline hex colours remain on the front page | **Still open** — `meat-thermometers.html` renders zero chip rows against one per card on the air-fryer shelf, and `index.html` still carries `#fff`, `#fdba74`, `#e6d9c8` and the `#292524→#57534e` gradient inline. SG-44 and SG-45 cover exactly these. |

Alongside those, this round extended the upstream clause map from 13 to 22 entries with the automation-side
clauses the six new policy rows rest on — 6(a), 6(d), 6(g), 6(n), 6(p), 6(s), Participation Requirements section 1
and section 4, and Commission Income Statement section 5 — each transcribed from the page served today, so
gate `D35` now refuses a citation of any of them *and* accepts them when cited correctly.

The pattern is worth stating plainly for whoever reads this after the merge: on this repository a cross-scope
*request* is reliable, because the file owner is already editing it, and a cross-scope *edit* is how two
sessions end up publishing two meanings for one ID — which happened to these six rows and cost a renumbering.

## 12. Reviewer's checklist for this round

- [ ] Read §3 of this memo against the live pages before accepting any renumbering of a citation.
- [ ] Decide Q-A, Q-B, Q-C — the three that nothing else can proceed on.
- [ ] Mark SG-43..SG-48 on `suggestions.html` (Do this / Maybe / No) and copy the block back; that is the
      design brief's approval step, and no page changes without it.
- [ ] Close or keep FLG-020 once the citations row is corrected by its owner.
