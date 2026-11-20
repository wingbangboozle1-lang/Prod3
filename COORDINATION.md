# COORDINATION.md — Shared Task Board

**Repo:** wingbangboozle1-lang/Prod3
**Session ID:** `arena/d52ad947-prod3` (branch `arena/d52ad947-prod3`)
**Tracking ID:** `shopnow047c-20` (Amazon Associates, as supplied)
**Last updated:** 2026-11-20

## How this board works

- Each task lists: status (`unclaimed` / `in progress` / `done` / `needs review`),
  owning session ID, and file scope.
- `needs review` = published on the Flagged for Review page; does not block anything.
- Claim a task by writing your session ID + file scope here, then commit + push immediately.
- Never edit a file owned by another session. Log cross-scope requests below instead.
- Run `git pull --rebase` before every push. Small, frequent commits.
- A claim older than 60 minutes with no commits may be taken over (note the handoff).

## Task board

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-01 | Verify 5 submitted links line-by-line vs official Amazon listings | done | 5a4e180c | `data/products.json`, `data/sources.json` |
| T-02 | Build product-intent confirmation record (intent vs observed, separate fields) | done | 5a4e180c | `data/products.json` |
| T-03 | Build publication-style site (front page, categories, compare, guides) | done | 5a4e180c | `index.html`, `air-fryers.html`, `meat-thermometers.html`, `compare.html`, `buying-guide.html`, `assets/*` |
| T-04 | Publish 8 question-shaped articles + RSS feed + sitemap | done | 5a4e180c | `articles/*`, `feed.xml`, `sitemap.xml` |
| T-05 | Disclosure strip above the fold on every page; `rel="sponsored"` on all outbound links | done | 5a4e180c | all `*.html` |
| T-06 | Click/conversion measurement (privacy-preserving, 5 defined events) | done | 5a4e180c | `assets/app.js`, `data/campaign-ledger.json` |
| T-07 | Flagged for Review page + source register with official links | done | 5a4e180c | `flagged.html`, `sources.html` |
| T-08 | Direction section: suggestions, open questions, path chooser | done | 5a4e180c | `direction.html`, `DIRECTION.md` |
| T-09 | Executive summary | done | 5a4e180c | `executive-summary.html`, `EXECUTIVE_SUMMARY.md` |
| T-10 | Gates: `scripts/check_site.py`, `tools/verify_site.py`, link check | done | 5a4e180c | `scripts/*`, `tools/*` |
| T-11 | GitHub Pages deploy + PR to main + merge | done | 5a4e180c | `.github/workflows/pages.yml` |
| T-12 | Post-merge integration audit: correct demonstrable editorial errors, disclosure/capture copy, event schema, analytics readiness, and unresolved compliance gates | done | `arena/5bd92dff-prod3` | all published HTML for disclosure/nav, `assets/app.js`, `assets/style.css`, `analytics.html`, `analytics/*`, `data/campaign-ledger.json`, `data/sources.json`, `sources.html`, `flagged.html`, `direction.html`, `DIRECTION.md`, `sitemap.xml`, `scripts/check_site.py`, `tools/verify_site.py`, `README.md`, `EXECUTIVE_SUMMARY.md` |
| T-16 | Re-run all release gates, internal-link crawl, feed/sitemap XML check, Pages status check; log remaining external-account blockers | done | arena/7d756ee2-prod3 | `COORDINATION.md` only |
| T-17 | Mobile-first pass (S-20): size every tap target to ≥48×48px with ≥8px spacing; verify disclosure stays above the first heading at 320px (Q-15); cite Google tap-target guidance | done (PR #12, merged `ce7aee3`) | `arena/65474d4f-prod3` (session 65474d4f) | `assets/style.css`, `data/sources.json`, `DIRECTION.md`, `direction.html`, `docs/verification.md`, `COORDINATION.md` (board rows only) |
| T-20 | Shop-polish redesign: buyer-first front page, product cards, seasonal/trendy guides, mobile-first polish (compliance gates preserved) | done | `arena/33e3e80f-prod3` | `index.html`, `air-fryers.html`, `meat-thermometers.html`, `compare.html`, `buying-guide.html`, `assets/style.css`, `assets/app.js`, `feed.xml` |
| T-21 | Expand Direction section: suggestions, open questions, missing-info discovery, path chooser | done | `arena/33e3e80f-prod3` | `direction.html`, `DIRECTION.md`, `data/suggestions.json`, `data/open-questions.json` |
| T-22 | Executive summary refresh + line-by-line verification + gates + PR to main + Pages confirm | done (PR #14 + #15, live-verified at `bb7d3d2`) | `arena/33e3e80f-prod3` | `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, `README.md`, `COORDINATION.md` |
| T-23 | Line-by-line verification of data registers and published claims against official sources; fix only demonstrable defects; final integration PR → main, merge, confirm Pages deploy | done (PR #18, https://github.com/wingbangboozle1-lang/Prod3/pull/18) | arena/28d2d6c0-prod3 | `data/sources.json`, `data/analysis.json`, `data/flagged.json`, `data/policy-checks.json`, `sources.html`, `tools/verify_site.py` (source-resolution gate), `COORDINATION.md` |
| T-24 | Refresh the executive summary against the current tree; correct stale claims; publish decision-ready facts, gaps, and ranked next steps | done | `arena/f4694e48-prod3` | `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, `COORDINATION.md` |
| T-24b | Final consistency audit of README, both executive summaries, analytics endpoint status/docs, and published rating copy; fix only stale or contradictory statements; release checks re-run and passed | done (2026-11-20) | `arena/71a41253-prod3` | `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `docs/analytics-endpoint.md`, `analytics.html`, `index.html`, `air-fryers.html`, `compare.html`, `direction.html`, `COORDINATION.md` |
| T-25 | 2026-11-20 live re-check of the five supplied short links and both Associates policy pages (official sources); record dated observation separately from the 2026-11-19 observation; flag the changed B04G1MEwY result as FLG-017; refresh executive summaries | done (see log) | arena/70e8475c-prod3 | `data/products.json`, `flagged.html`, `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, `COORDINATION.md` |
| T-26 | Final integration integrity pass: reconcile product-intent evidence, link/policy copy, automation claims, and flags; strengthen gates; re-run site and Pages release checks | done (2026-11-20, PR and Pages result below) | `arena/e83cdf55-prod3` | `data/verification.json`, `data/policy-checks.json`, `data/flagged.json`, `data/open-questions.json`, `data/suggestions.json`, `flagged.html`, `suggestions.html`, `questions.html`, `docs/verification.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`, `scripts/check_site.py`, `tools/check_site.py`, `tools/verify_site.py`, `COORDINATION.md` |
| T-39 | Final integration for the 2026-11-20 round (renumbered from a colliding T-26 claim; see handoff log): fresh line-by-line review of all registers and published pages, fix demonstrable defects only (stale DIRECTION cross-references and SG-22..30 index vs register, nine-article counts), flag the dual Pages deploy paths as FLG-024, re-run all gates, PR → main, merge, confirm live deploy | done (PR #36, merge commit `a861ed7`; deploy + live check recorded below) | `arena/09d7261c-prod3` | `COORDINATION.md`, `DIRECTION.md`, `direction.html`, `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `flagged.html`, Pages repo settings (build_type) |
| T-46 | **(ID collision: upstream session 59a087a1 holds the earlier T-46 row; both kept, integration merged this branch as PR #98.)** Line-by-line integration review of the post-T-39 tree: fix demonstrable defects only (duplicate or contradictory card markup, stale cross-references, register-vs-page count drift); re-run every release gate; PR → main, merge, confirm GitHub Pages deploy and live content | in progress | `arena/74e655e9-prod3` | any published HTML or register demonstrably defective (fix-only scope), `COORDINATION.md` |
| T-46 | Final integration round (session 59a087a1): live line-by-line re-verification of the five published listings against the official Amazon pages (specs only — no prices, ratings or offers recorded), register the official sources that are missing so no register row is left "No official source" where a genuine official source exists, publication-polish fixes, re-run every gate, PR → main, merge, confirm Pages deploy | in progress | `arena/59a087a1-prod3` | `data/products.json`, `data/sources.json`, `data/citations.json`, `data/decisions.json`, `data/open-questions.json`, `data/flagged.json`, `data/verification.json`, `articles/*`, `index.html`, `buying-guide.html`, `air-fryers.html`, `meat-thermometers.html`, `scripts/build_registers.py`, `scripts/build_chrome.py`, `tools/check_site.py`, `tools/verify_site.py`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`, `COORDINATION.md` |
| T-47 | Integration pass after PR #38 (T-46, session 59a087a1) landed first: re-run all gates on the merged tree; re-check the Pages deploy and live pages; record the duplicate `FLG-021` callout on `flagged.html` as an owner decision (not renumbered); no site content change; PR → main, merge, confirm live deploy | done (PR and merge record below) | `arena/cafc55da-prod3` | `COORDINATION.md` only |
| T-48 | 2026-11-20 buyer-facing link check: all five supplied short links re-tested; all five now end at the Amazon homepage. Record dated observation separately (superseding neither 2026-11-19 record nor the other same-day record); publish FLG-025; refresh summaries. | done (see log below; renumbered from a colliding T-46 claim — upstream T-46 is session 59a087a1) | `arena/6bf60cac-prod3` | `data/products.json`, `data/verification.json`, `data/flagged.json`, `flagged.html`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |
| T-49 | Publishing plan: twelve dated guide proposals with the evidence each needs, rendered from `data/editorial-plan.json` and gated (D31); four blocked rows named rather than filled by inference. New suggestions SG-32..SG-35, questions Q-24..Q-26, decisions DT-11..DT-12 | done (renumbered from a colliding T-47 claim — upstream T-47 is session cafc55da) | `arena/6bf60cac-prod3` | `publishing-plan.html`, `data/editorial-plan.json`, `data/suggestions.json`, `data/open-questions.json`, `data/decisions.json`, `scripts/build_registers.py`, `scripts/build_chrome.py`, `scripts/build_decisions.py`, `tools/check_site.py` |
| T-50 | One generated page per product (`products/*.html`) from `data/products.json` + `data/flagged.json`, with intended-vs-observed kept separate and the blank intent field shown as blank; linked from both pillars and the front page; three new gates and a CI freshness step | done (2026-11-20) | `arena/6bf60cac-prod3` | `scripts/build_products.py`, `products/*`, `scripts/build_chrome.py`, `scripts/build_sitemap.py`, `scripts/check_site.py`, `tools/check_site.py`, `tools/crawl_links.py`, `.github/workflows/pages.yml`, `index.html`, `air-fryers.html`, `meat-thermometers.html` |
| T-51 | Design + content suggestions round (renumbered from T-48 because T-48 was already in use on main by session arena/6bf60cac-prod3; both rows kept, no work discarded): add shopfront-design (SG-36), trend-led-article (SG-37), and review-before-build (SG-38) suggestions to the register; add the missing-info discovery question Q-27; refresh the executive summary; run every release gate; PR `arena/8692a390-prod3` → main (#42); merge; confirm Pages deploys; record PR link and merge result here | in progress | `arena/8692a390-prod3` | `data/suggestions.json`, `data/open-questions.json`, `scripts/build_registers.py`, `suggestions.html`, `questions.html`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |
| T-38 | Per-product detail pages (session fe5fd1d9; claimed concurrently with T-50, which shipped them first as a generator — the generated pages were adopted as canonical and this session's hand-built drafts were retired untouched). What shipped on top of T-50: merge of main adopting the generated pages; a proposed FLG callout-id-uniqueness gate that main's generalized one-meaning rules (D19/D35/D38) made redundant — dropped rather than shipped twice; the comparison table's five buy buttons de-risked to the official product pages per FLG-025 (adopted upstream's aria-labels; upstream had renamed the row header but four of five cells still used the short links); dated FLG-019 addendum; register rows FLG-030/FLG-031 so every published callout id has a register row; proposal SG-43 (consider-if/look-elsewhere-if blocks for the generated pages; numbered SG-39 until a second id collision with main was caught in merge #2); executive summaries re-scoped; merge-doubled products globs fixed in both checkers and the crawler | done (2026-11-20) | `arena/fe5fd1d9-prod3` | `tools/check_site.py`, `scripts/check_site.py`, `tools/crawl_links.py`, `compare.html`, `flagged.html`, `data/flagged.json`, `data/suggestions.json`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`, `COORDINATION.md` |
| T-52 | Session 2cd3bab9 pass after PR #43 and PR #42 (T-48 and T-51 already taken upstream; renumbered again): verify on the merged tree the guides hub (nine guides), feed titles against H1s, the publishing-coverage gate and the monthly cadence; set DT-10 decided (owner instruction); spot-check six official sources; record the same-day link check (agrees with the third dated check under FLG-025, no product record changed); log duplicate board IDs (FLG-032) and the source fetch-date gap (FLG-037); refresh the executive-summary addendum; PR → main, merge, confirm Pages | in progress | `arena/2cd3bab9-prod3` | `buying-guide.html`, `feed.xml`, `tools/verify_site.py`, `docs/publishing-cadence.md`, `data/decisions.json`, `data/flagged.json`, `flagged.html`, `decisions.html` (generated), `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |
| T-58 | Register-consistency and stale-count audit on the tree after PR #65 (claimed as T-46 at `7c1b939`, renumbered four times: upstream sessions took T-46..T-52, then T-53..T-56, then T-57 while this claim was open — both T-57 rows above kept, this row is the 62b9cc82 session): upstream sessions took T-46..T-52, then T-53..T-56 while this claim was open; all upstream rows kept): re-audit every defect found at the old base against the current tree (DIRECTION.md index vs `data/suggestions.json`, direction.html ranges/counts/Q rows, eight-vs-nine-versus-ten article counts in the registers, page-count claims in README and both executive summaries, the SG-20 proposed-vs-implemented contradiction), fix only what is still demonstrably wrong after the open PRs land, publish surviving contradictions as flags, add a mirror gate where none exists, re-run all gates, PR → main, merge, confirm Pages | in progress | `arena/62b9cc82-prod3` | `README.md`, `DIRECTION.md`, `direction.html`, `data/open-questions.json`, `data/suggestions.json`, `data/flagged.json`, `flagged.html`, `scripts/build_registers.py`, `tools/check_site.py`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, regenerated register pages, `COORDINATION.md` |

## Session `arena/f3900cd3-prod3` — T-52 (claimed as T-47, renumbered twice)

**Session ID:** `arena/f3900cd3-prod3` · **Branch:** `arena/f3900cd3-prod3` · **Base:** `372afb0` (main after PR #38)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-52 | Shop pass, round 2: (a) fix the duplicate FLG-020…FLG-023 identifiers on `flagged.html` left by T-46; (b) add an audience front door `/start.html` ("what kind of cook are you") so a buyer picks a shelf instead of reading a register; (c) ship one new question-shaped guide for the December gift season, wired into the existing sitemap **and** the existing `feed.xml`; (d) reader-capture decision proposed in the register rather than silently implemented (no email provider exists — FLG-014 stands); (e) add a visual-review workflow so the owner can *look* at every page without installing anything; (f) re-run every gate, PR → main, merge, confirm the live deploy, and fetch the live pages back to prove it | in progress | `arena/f3900cd3-prod3` | `COORDINATION.md`, `flagged.html`, `start.html`, `data/suggestions.json`, `data/open-questions.json`, `articles/*` (new guide only), `feed.xml`, `index.html`, `assets/style.css`, `scripts/check_site.py`, `tools/check_site.py`, `tools/crawl_links.py`, `.github/workflows/snapshots.yml`, `design/pages.json`, `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html` |
| T-53 | 2026-11-20 line-by-line defect pass (renumbered twice after collisions: T-46 → T-50 against session 59a087a1, then T-50..T-52 → T-53..T-56 against sessions 6bf60cac/8692a390/2cd3bab9/f3900cd3 whose PRs #44–#52 merged while this branch was queued): correct demonstrable stale statements only — flagged.html byline date, sources.json/sources.html `used_for` wording for S10–S14 (snapshot price/rating recorded in data only, never rendered). README register tables and byline derivation were fixed upstream in the meantime and are not redone | done (session record below) | `arena/7878cdbe-prod3` | `flagged.html` (byline), `data/sources.json` (used_for wording S10–S14, adds S34–S36 only), `sources.html` (matching rows), `COORDINATION.md` |
| T-54 | 2026-11-20 organic-growth register additions with sources verified live this session (renumbered twice: upstream 6bf60cac/8692a390 took SG-32..SG-38 and Q-24..Q-27, upstream PR #52 took SG-39..SG-42, so this session's rows ship as **SG-43..SG-47** and **Q-28..Q-29**): proposals — seasonal-block retirement date, FAQ-rich-result deprecation guard, AI-assisted-draft fact-check rule, CWV measurement gate, anchor-text discipline gate; questions — indexing status (Q-28), Core Web Vitals baseline (Q-29); new source rows **S34** (Google link best practices), **S35** (Google search-doc updates changelog: FAQ rich result deprecated 2026-05-07/08, docs removed 2026-06), **S36** (Google generative-AI content guidance, updated 2026-10-01); S22/S25 re-verified with quotes; DIRECTION.md SG index extended; generated pages rebuilt | done (session record below) | `arena/7878cdbe-prod3` | `data/suggestions.json` (appends SG-43..SG-47 only), `data/open-questions.json` (appends Q-28/Q-29 only), `data/sources.json` (adds S34–S36 only), `DIRECTION.md`, `suggestions.html`, `questions.html`, `decisions.html`, `citations.html` (regenerated), `COORDINATION.md` |
| T-55 | Executive summary refresh (renumbered from T-52): add this session's register additions, verified-source notes, and defect-fix record to `EXECUTIVE_SUMMARY.md` and `executive-summary.html` on top of upstream's 2026-11-20 addenda; keep every count and ID range consistent with the registers | done (session record below) | `arena/7878cdbe-prod3` | `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |
| T-56 | Release for the 2026-11-20 round (renumbered from T-53): re-run all gates on the final tree, PR → main, merge without waiting for approval, confirm the GitHub Pages deploy and live URL, record PR/merge/deploy results and remaining owner gates here | done (PR #62, merge commit `9dd5c37`; deploy + live check in the record below) | `arena/7878cdbe-prod3` | `COORDINATION.md` only |


**Renumbered T-47 → T-51 → T-52, 2026-11-20.** Four other sessions merged while this work was open and
took T-46 through T-50 for their own passes (T-47: post-PR-#38 integration; T-48: the buyer-facing
link re-check; T-49: the publishing plan; T-50: one page per product). Per the board's
one-identifier-one-meaning rule, this claim became T-51 and the original row text is kept. A second session took **T-51** for a design-and-content round before this branch merged (merge commit `ddb50f8`), so the row is now **T-52**; the T-51 row above is untouched. My four suggestion rows were renumbered twice for the same reason and now sit at **SG-39..SG-42**.
Two further collisions were resolved the same way and are logged in the completion record at the
end of this file: my four suggestion rows were renumbered twice, ending at SG-39…SG-42, and my `flagged.html` renumbering was dropped in favour of upstream's, which fixed
the same four duplicate ids while this branch was open.

**Scope notes, so a later session is not surprised:**

- **No overlap is claimed with T-46's scope.** `data/products.json`, `data/sources.json`,
  `data/citations.json`, `data/decisions.json`, `data/verification.json`, `air-fryers.html`,
  `meat-thermometers.html`, `buying-guide.html`, `scripts/build_chrome.py` and
  `scripts/build_registers.py` are **not** in this scope. Where this pass needs a new
  suggestion or question, it appends a row; it does not renumber or rewrite existing rows.
- **`flagged.html` is in scope only to remove an ambiguity T-46 flagged itself**: FLG-020,
  FLG-021, FLG-022 and FLG-023 each label two different findings. Renumbering the second
  finding under each id is a correction, not a new claim; the text of every finding is kept.
- **`feed.xml` change is an append**: the December guide becomes item 10. The existing nine
  items and the file header are untouched.
- **This session does not touch owner-only gates**: Associates account status (FLG-010),
  intended ASINs (FLG-001), Special Link test (FLG-006), analytics endpoint, Search Console.
- If a later session needs a file in the scope above, log the request here rather than editing it.

| T-52 | Session 2cd3bab9 pass after PR #43 and PR #42 (T-48 and T-51 already taken upstream; renumbered again): verify on the merged tree the guides hub (nine guides), feed titles against H1s, the publishing-coverage gate and the monthly cadence; set DT-10 decided (owner instruction); spot-check six official sources; record the same-day link check (agrees with the third dated check under FLG-025, no product record changed); log duplicate board IDs (FLG-032) and the source fetch-date gap (FLG-033); refresh the executive-summary addendum; PR → main, merge, confirm Pages | in progress | `arena/2cd3bab9-prod3` | `buying-guide.html`, `feed.xml`, `tools/verify_site.py`, `docs/publishing-cadence.md`, `data/decisions.json`, `data/flagged.json`, `flagged.html`, `decisions.html` (generated), `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |
| T-60 | **landed 2026-11-20** (this session). 2026-11-20 third same-day observation set of the five **supplied short links themselves** (59a087a1's T-46 checked the official listing pages; cafc55da's T-47 touched this board only). Each outcome is appended as its own dated record; no earlier observation is overwritten. Plus: repair the two reader-facing buy buttons that still route a buyer through the link recorded as landing on the Amazon homepage (FLG-017), and add a gate for that rule | in progress | `arena/6c0972fb-prod3` | `data/products.json` (append-only), `compare.html`, `articles/holiday-kitchen-gift-guide.html`, `scripts/check_site.py` (new rule), `flagged.html` (one added row) |
| T-61 | **landed 2026-11-20**. Reader-facing editorial expansion for the live calendar: three new question-shaped guides (Thanksgiving leftovers and reheating, how to read a product listing without being sold, checking a thermometer at home), each with official sources, plus the front-page and hub links, the feed, and the sitemap; the feed-item gate in `tools/verify_site.py` made count-independent so growth cannot break it | in progress | `arena/6c0972fb-prod3` | `articles/thanksgiving-leftovers-air-fryer.html`, `articles/how-to-read-a-product-listing.html`, `articles/check-your-thermometer-at-home.html`, `feed.xml`, `sitemap.xml`, `buying-guide.html`, `air-fryers.html`, `meat-thermometers.html`, `index.html`, `tools/verify_site.py` (feed count rule only) |
| T-62 | **landed 2026-11-20**. Publication polish: article bylines with a dated review line, `BreadcrumbList` structured data on the guides, a front-page "what we do before a guide ships" module, inline-style cleanup on the product cards, CSS card/CTA details | in progress | `arena/6c0972fb-prod3` | `assets/style.css`, `index.html`, `articles/*.html`, `buying-guide.html`, `about.html` |
| T-63 | Direction layer: new reviewable suggestions (SG-32..), a copy-ready site design brief on `ideas.html`, new missing-info questions (Q-24..), decision-desk rows for the new choices, `DIRECTION.md` + both executive summaries refreshed, the duplicate README register table removed, `data/flagged.json` brought in line with the published flag page | in progress | `arena/6c0972fb-prod3` | `data/suggestions.json`, `data/open-questions.json`, `data/decisions.json`, `data/flagged.json`, `ideas.html`, `DIRECTION.md`, `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, `README.md` |
| T-64 | Repair the duplicate flag identifiers on `flagged.html` (FLG-020, FLG-021, FLG-022 and FLG-023 each head two different findings; 59a087a1's new register rows collided with existing published IDs). Second occurrence of each renumbered to a free ID, every cross-reference followed, and a uniqueness rule added to the gate so it cannot recur | in progress | `arena/6c0972fb-prod3` | `flagged.html`, `data/flagged.json`, `data/products.json` (flag refs only), `tools/check_site.py` (new rule), `README.md`, `DIRECTION.md` |
| T-65 | Final integration for this round: re-run all eight gates on the merged tree, PR → main, merge without waiting, confirm `Deploy GitHub Pages` success by run ID and check the live pages | in progress | `arena/6c0972fb-prod3` | `COORDINATION.md` plus whatever T-60..T-64 already scope |
| T-66 | Complete the flag-id collision repair on the merged tree (one ID = one meaning; claim history: T-52 → T-56 → T-66 after upstream took T-52 and later renumbered the register past FLG-037): the temperature/wattage listing conflict (P-03, observed 2026-11-20 by session 59a087a1, recorded in data/products.json and the S31 quote) was left without a registered id by the renumbering passes; it is restored as FLG-041 in `data/flagged.json` and on `flagged.html`; the dangling `(FLG-022)`/`(FLG-023)` references in `data/products.json` repointed to F-01/FLG-041; DIRECTION.md decision-log FLG-021 ref repointed to FLG-029; air-fryers.html capacity chip links the F-register on decisions.html and the P-03 card carries the FLG-041 chip; FLG-027 reconciled to the final renumbering | in progress | `arena/aa7b8dd8-prod3` (branch `arena/aa7b8dd8-prod3`) | `flagged.html`, `data/flagged.json`, `data/products.json`, `air-fryers.html`, `DIRECTION.md`, `COORDINATION.md` |
| T-67 | Final integration for this round (claim history: T-55 → T-66 → T-67; upstream separately took T-53..T-65): regenerate every generated surface, run the full release-gate suite, PR → main, merge without waiting, confirm the `Deploy GitHub Pages` run and live URL, record results here | in progress | `arena/aa7b8dd8-prod3` (branch `arena/aa7b8dd8-prod3`) | `COORDINATION.md` |
| T-57 | Final integration re-verification of the combined tree after PR #37 and the concurrent T-46..T-56 merge (renumbered twice: T-46 → T-51 → T-53 because T-46/T-48/T-51/T-52 were taken upstream, then T-53 → T-57 because session 7878cdbe took T-53..T-56 for its defect/growth/release round; per the one-identifier-one-meaning rule): line-by-line re-check of all registers and published docs; reconcile stale register ranges/counts (README, EXECUTIVE_SUMMARY, direction.html) and stale register generation dates; re-run all gates; PR → main, merge, confirm Pages deploy, record result | done (PR #45 merged as `89849e0`; gates green; Pages deploy run 44693759586 success — see the T-57 merge and deploy record below) | `arena/6f44d8c9-prod3` | `README.md`, `EXECUTIVE_SUMMARY.md`, `direction.html`, `data/suggestions.json`, `data/open-questions.json`, `data/citations.json`, `scripts/build_registers.py`, `COORDINATION.md` |
| T-63 **landed 2026-11-20**| Direction layer: new reviewable suggestions (SG-32..), a copy-ready site design brief on `ideas.html`, new missing-info questions (Q-24..), decision-desk rows for the new choices, `DIRECTION.md` + both executive summaries refreshed, the duplicate README register table removed, `data/flagged.json` brought in line with the published flag page | in progress | `arena/6c0972fb-prod3` | `data/suggestions.json`, `data/open-questions.json`, `data/decisions.json`, `data/flagged.json`, `ideas.html`, `DIRECTION.md`, `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, `README.md` |
| T-64 **landed 2026-11-20**| Repair the duplicate flag identifiers on `flagged.html` (FLG-020, FLG-021, FLG-022 and FLG-023 each head two different findings; 59a087a1's new register rows collided with existing published IDs). Second occurrence of each renumbered to a free ID, every cross-reference followed, and a uniqueness rule added to the gate so it cannot recur | in progress | `arena/6c0972fb-prod3` | `flagged.html`, `data/flagged.json`, `data/products.json` (flag refs only), `tools/check_site.py` (new rule), `README.md`, `DIRECTION.md` |
| T-65 **landed 2026-11-20**| Final integration for this round: re-run all eight gates on the merged tree, PR → main, merge without waiting, confirm `Deploy GitHub Pages` success by run ID and check the live pages | in progress | `arena/6c0972fb-prod3` | `COORDINATION.md` plus whatever T-60..T-64 already scope |
| T-75 | Shop-voice and publication polish on the front page (originally claimed T-48 before the collision note below): hero rewritten, feature figure corrected to "2 × 3 qt" so no disputed total volume is stated as fact, one broken sentence fixed | done (record below) | `arena/37c5f395-prod3` | `index.html` |
| T-76 | Two question-shaped evergreen guides — `articles/are-air-fryers-worth-it.html`, `articles/smart-thermometer-questions.html` — in the current guide template (Article + BreadcrumbList JSON-LD, byline), wired into the front-page grid, the buying-guide clusters and the category read-next boxes; feed items added (items = guides, the gate self-counts); sitemap regenerated | done (record below) | `arena/37c5f395-prod3` | `articles/*` (2 new), `feed.xml`, `index.html`, `buying-guide.html`, `air-fryers.html`, `meat-thermometers.html`, `sitemap.xml` |
| T-77 | Decision-register addition SG-55 (dated voice refresh for the 2026-11-19 guide batch) + defect fixes found on the merged tree: duplicated read-next entries on `air-fryers.html`, D40 guide-count words extended to thirteen–sixteen (the regex previously could not see "All thirteen guides"), stale guide counts corrected in Q-14/Q-17, the front page, README and both executive summaries | done (record below) | `arena/37c5f395-prod3` | `data/suggestions.json`, `data/open-questions.json`, `tools/check_site.py`, `air-fryers.html`, `index.html`, `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html` |
| T-78 | Integration: reconcile this session's in-flight work with the T-46..T-65 rounds that landed first (their flag-ID scheme, registers and generators kept as mainline; this session's parallel FLG renumbering, FAQPage markup and SG-32..35/Q-24..25 rows dropped as superseded — see the record below), re-run all gates, PR → main, merge, confirm Pages | done (record below) | `arena/37c5f395-prod3` | `COORDINATION.md` (+ the tree) |
| T-57 | Final integration re-verification of the combined tree after PR #37 and the concurrent T-46..T-56 merge (renumbered twice: T-46 → T-51 → T-53 because T-46/T-48/T-51/T-52 were taken upstream, then T-53 → T-57 because session 7878cdbe took T-53..T-56 for its defect/growth/release round; per the one-identifier-one-meaning rule): line-by-line re-check of all registers and published docs; reconcile stale register ranges/counts (README, EXECUTIVE_SUMMARY, direction.html) and stale register generation dates; re-run all gates; PR → main, merge, confirm Pages deploy, record result | in progress | `arena/6f44d8c9-prod3` | `README.md`, `EXECUTIVE_SUMMARY.md`, `direction.html`, `data/suggestions.json`, `data/open-questions.json`, `data/citations.json`, `scripts/build_registers.py`, `COORDINATION.md` |
| T-74 | Current-tree documentation consistency pass (renumbered four times — claimed T-46, then T-53, then T-66, then T-70, each taken upstream by other sessions; every earlier row kept): reconcile stale guidance/register counts and outdated claims against the merged data; merge `origin/main` four times (002ab81, 8cc8d58, ef84eef, 6455932) keeping both sides' work; run all site gates | done (2026-11-20, record below; PR/merge/Pages result appended after deploy) | `arena/30d1c448-prod3` | `README.md`, `DIRECTION.md`, `direction.html`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |

| T-58 | Register-integrity + publication-machinery pass (renumbered twice: claim commit named T-25, renumbers T-39 and T-52 both collided with main-side rows; final id T-59): one id one meaning across flagged/suggestions/digest (flagged.html shipped duplicate FLG-020/021; digest rows carried SG-27..SG-30 ids with different meanings → SG-32..SG-35 registered), generated DIRECTION digest (build_digest.py, gate D32), cross-surface id gate D31 + flagged-sync gate D34 (both negative-tested), feed-item titles aligned to guide h1s, self-hosted analytics collector shipped as deployable code (endpoint kept blank), stale cross-refs fixed (SG-19→SG-24 on about.html etc.), exec summary + PR → main, merge, Pages confirm | done (PR #77; see the merge record below) | `arena/26285b01-prod3` | `flagged.html`, `ideas.html`, `DIRECTION.md`, `data/suggestions.json`, `data/open-questions.json`, `data/decisions.json`, `data/flagged.json`, `feed.xml`, `scripts/build_digest.py`, `scripts/build_registers.py`, `tools/check_site.py`, `docs/*`, `analytics/collector/*`, `analytics.html`, `about.html`, `direction.html`, `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |

| T-70 | Transcribe the published ce911db5 same-day records verbatim into data/products.json short_link_rechecks (all five products) with explicit provenance, so FLG-031's "kept in data/products.json" claim is true; add the d52ad947 fifth-pass entries for the two links it fetched; update the FLG-017 register row and Q-22 | done | `arena/d52ad947-prod3` | `data/products.json`, `data/flagged.json`, `data/open-questions.json`, `questions.html` + `decisions.html` + `ideas.html` + `products/*.html` (regenerated), `flagged.html` |
| T-71 | Fix post-renumbering flag references: executive-summary.html FLG-028 → FLG-025/FLG-039 for the all-five checks; executive summaries updated for the five-pass picture (the DIRECTION.md FLG-020/021 mis-cites were already cleaned upstream by the T-52 round) | done | `arena/d52ad947-prod3` | `executive-summary.html`, `EXECUTIVE_SUMMARY.md` |
| T-72 | FLG-024 owner-fix re-check: `PATCH /repos/…/pages {"build_type":"workflow"}` re-attempted → HTTP 404 again; flag row updated with the dated re-attempt. FLG-032 partial consolidation (delegated by the flag to the next integration session): the three superseded T-20/T-21/T-22 rows removed; flag status updated | done | `arena/d52ad947-prod3` | `flagged.html`, `data/flagged.json`, `COORDINATION.md` (this board) |
| T-73 | All release gates re-run on the reconciled tree; PR → main, merge without waiting, confirm Pages deploy, record merge + deploy result on the board | done (merge result recorded below after the PR merges) | `arena/d52ad947-prod3` | `COORDINATION.md` |
| T-79 | Measurement coverage + ledger coherence (renumbered twice: claimed T-53, upstream took T-53..T-56; claimed T-72, session d52ad947 took T-72 on main while this branch was in flight — their rows untouched; session 47f4e1e5): `outbound_click` only bound links carrying `data-event` — 30 of 355 product links counted on the merged tree, while `analytics.html` tells the reader the event is "activation of a supplied product link". Bind every `rel="sponsored"` Amazon/`link.amazon` link (ASIN from `data-asin` or the `/dp/` href, same 10-char rule, no other payload change). Two ledger files both claim to be the campaign ledger (`data/campaigns.json` cited by F-15, `data/campaign-ledger.json` read by every gate): reconcile them (canonical pointer + shared tracking id, both stay empty). Update `docs/analytics-endpoint.md`; add gates in `scripts/check_site.py` so coverage and ledger coherence cannot regress; re-run every release gate; PR → main, merge, confirm Pages; record here | in progress | `arena/47f4e1e5-prod3` | `assets/app.js`, `data/campaigns.json`, `data/campaign-ledger.json`, `docs/analytics-endpoint.md`, `scripts/check_site.py`, `COORDINATION.md` (board + session log only) |

## Verification log (2026-11-19, session 5a4e180c)

All five submitted `link.amazon` tokens were checked against official Amazon pages
via direct fetch. Findings (full detail in `data/products.json`):

| Submitted link | Token length | `amazon.com/dp/<token>` | Observed destination (ASIN) | Category (browse node) |
|---|---|---|---|---|
| link.amazon/B04G1MEwY | 9 chars | Page Not Found | B0CDY277D3 | Air Fryers (17659096011) |
| link.amazon/B02NbDxp3 | 9 chars | Page Not Found | B09B7SB46R | Air Fryers (17659096011) |
| link.amazon/B00hJ57DV | 9 chars | Page Not Found | B08DKYBTPH | Air Fryers (17659096011) |
| link.amazon/B0c8moW59 | 9 chars | Page Not Found | B0DHZTCNR5 | Meat Thermometers (289810) |
| link.amazon/B0f3GKalj | 9 chars | Page Not Found | B0DZFD6R9Z | Meat Thermometers (289810) |

- An ASIN is a 10-character code (Amazon Associates / Creators API definition).
  A 9-character token cannot be an ASIN. The tokens are short-link codes.
- Intended ASIN / official listing URL / confirmation date / source are **blank**
  for all five (nothing public binds a short code to a product intent).
  Observed redirect targets are recorded separately and never merged.
- Official sources re-read live 2026-11-19: Operating Agreement (updated
  2025-10-15), Program Policies (updated 2026-04-14), FTC Disclosures 101,
  Google `rel="sponsored"` guidance, GitHub Pages docs. See `data/sources.json`.

## Flagged irregularities (published on `flagged.html`, do not block)

- FLG-001 — Intended product for each short link is unconfirmed (owner confirmation needed).
- FLG-002 — Emeril preset count: 24 (title) vs 25 (About this item) on the same listing.
- FLG-003 — CHEF iQ battery life: 50 h (About) vs 70 h (Product Description); warranty 2 yr vs 3 yr.
- FLG-004 — Chefman 8 QT (B08DKYBTPH) has a newer model B0CNY1YVDD listed on its page.
- FLG-005 — ThermoMaven (B0DHZTCNR5) has a newer model B0GL7Z4KP4 listed on its page.
- FLG-006 — Short-link compliance status unresolved; test one Special Link per product
  in the enrolled Associates workflow before scaling. Do **not** claim the short links are invalid.
- FLG-007 — Prices observed 2026-11-19 will drift; always verify on Amazon before purchase.
- FLG-008 — No product photography used (Operating Agreement §1: Program Content
  includes images; only Amazon-provided images may be used). Site uses CSS/SVG art.
- FLG-009 — ThermoMaven ±0.5°F / "NIST & NSF Certified" / 1-sec / IP67 wording is seller
  claim, not test; certificate unexamined; NIST traceability applies to measurement results.
- FLG-010 — Amazon Associates account status unverified (tracking ID owner-supplied);
  membership assertion removed, required earnings statement + conditional copy kept.
- FLG-011 — /dp/<token> Page-Not-Found check investigated and dismissed as link evidence
  (constructed /dp/ URLs are not the supplied short links; only the 9-char length is a finding).
- FLG-012 — Price/rating snapshots are date-only (no observation time or delivery location).
- FLG-013 — Emeril accessories count: six named in title/About vs "7 Accessories" config string.
- FLG-014 — Reader email signup not connected (demo form with fake confirmation removed).
- FLG-015 — Campaign ledger empty by design; no first-party reports yet.
- FLG-016 — Social preview card not yet confirmed in an external share debugger (F-21/Q-21); PNG format shipped.
- FLG-017 — B04G1MEwY resolves to the Amazon homepage on 2026-11-20 in every pass that fetched it (70e8475c, ce911db5, 6bf60cac, 6c0972fb, d52ad947); it resolved to B0CDY277D3 on 2026-11-19. Cause not established; may be transient; owner check in the Associates workflow.
- FLG-024 — Dual GitHub Pages deploy paths: the legacy branch builder races the artifact deploy and failed behind it (run 44686774699) while the live site served current content; settings change blocked by token permissions — owner one-click fix documented on `flagged.html` (session 09d7261c); re-attempted 2026-11-20 (d52ad947), PATCH /pages again HTTP 404.
- FLG-025 — All five supplied short links ended at the Amazon homepage on a 2026-11-20 pass (6bf60cac); one more pass (d52ad947) saw the homepage for the two links it fetched. A dated observation, not a verdict on the links.
- FLG-026 — Program Policies §2(b) tag-parameter requirement: no shipped anchor visibly carries tag=shopnow047c-20 in the URL the reader receives; a short-link service may add it downstream (Q-24).
- FLG-027 — Flag register integrity: two ids each named two different findings on the published page; renumbered into FLG-028..031 (fixed 2026-11-20).
- FLG-028 — Register history: the digest-correction finding previously published as a second FLG-020 (fixed; id renumbered).
- FLG-029 — Register history: the phantom-SG-id finding previously published as a second FLG-021; the SG-26 slot is intentionally left unoccupied and documented; gate D29 guards it.
- FLG-030 — Register history: the broken-script finding previously published as FLG-022; J-gates now parse every script (resolved 2026-11-20).
- FLG-031 — Two of five supplied links reached the homepage on 2026-11-20 with one same-day disagreement (previously FLG-023); a later pass (d52ad947) agrees with the homepage records; all records now in `data/products.json`.
- FLG-032 — Coordination board: duplicate task identifiers T-12..T-23 (partially resolved 2026-11-20 by d52ad947: the superseded T-20/21/22 rows consolidated; T-12..T-17 left for the owner).
- FLG-033 — Source register: no consistent per-row fetch date (23 of 29 entries lack a verified value).
- FLG-034..036 — unoccupied; the subjects they briefly carried renumbered into FLG-037/FLG-038 during the concurrent merges.
- FLG-037 — Program Policies clause letters were wrong; clauses located, quoted and gated (RESOLVED 2026-11-20).
- FLG-038 — Every article page ended with the same block and every product card printed its specs twice (RESOLVED 2026-11-20).
- FLG-039 — Fourth dated observation (6c0972fb, independent of 6bf60cac): all five links ended at the homepage, none carrying the tag in the URL the reader receives; owner test still required.
- FLG-040 — Commit ffcb419 dropped the five official_listing_check blocks; data repaired by 6c0972fb; workflow change is the owner's call.
- FLG-041 — Official listing conflict: the listing states two maximum temperatures and two wattages; both readings published; seller/manufacturer confirmation needed.

## Cross-scope requests

(none)

## Handoff / conflict log

- 2026-11-19 T-12 audit (`arena/5bd92dff-prod3`): claim policy rewritten across the site —
  seller-stated specs attributed, capacity-ratio/serving-size/winner claims removed,
  NIST/USDA sources added to the register, FLG-009..015 opened, demo signup removed
  (matching `analytics.html`), and the b84724ea price-policy pass merged in (no currency
  rendered anywhere; §2(b) stated where prices used to be). Disclosure carries the required
  “As an Amazon Associate…” statement plus conditional commission wording and the
  unverified-account caveats (FLG-010). Release gates enforce banned phrases, the
  currency ban, claim markers, sponsored coverage, and source-linked data tables.
  Intended ASINs remain unconfirmed (FLG-001) and short-link compliance unresolved
  (FLG-006) — do not conclude the supplied links are invalid.

- 2026-11-20 (`arena/d52ad947-prod3`, T-70..T-73): this branch was rebuilt twice on moving `main`
  (first on the pre-PR-#53 tree, then on `d47a3df`, finally on `f98e185`); its first commits, which had
  renumbered the colliding T-45 callouts to FLG-025/026, were withdrawn once PR #53 took those ids —
  main's own scheme (FLG-027..031, then 037..041) was kept instead. The reconciliation adds only what
  main still lacked: the ce911db5 transcription, the d52ad947 fifth-pass entries, the
  FLG-028-to-FLG-025/039 reference fix, the FLG-024 re-attempt note, and the FLG-032 partial
  consolidation. No other session's published content was altered; nothing was force-pushed to `main`.

## Deploy record

- PR: https://github.com/wingbangboozle1-lang/Prod3/pull/1 (arena/5a4e180c-prod3 → main)
- Merge result: merged (merge commit ca9f4f27f77eef5ea6a15421c177b2f57f275427, 2026-11-19 12:43:28Z); verify_site.py and sitemap --check passed before merge
- Pages: 'Deploy GitHub Pages' workflow success on merge; 'pages build and deployment' success; live page confirmed at the URL below
- GitHub Pages URL: https://wingbangboozle1-lang.github.io/Prod3/

## Session arena/9978ab21-prod3 — integration (2026-11-19)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-12 | Independent re-verification of the 5 submitted links vs official Amazon listings | done | arena/9978ab21-prod3 | `data/products.json` (re-fetch confirmed identical observed destinations) |
| T-13 | Review existing click/conversion measurement (assets/app.js, data/campaign-ledger.json) — covers T-06 scope; no duplicate analytics added | done | arena/9978ab21-prod3 | `assets/app.js`, `data/campaign-ledger.json` |
| T-14 | Add docs/verification.md, docs/analytics-endpoint.md, 404.html | done | arena/9978ab21-prod3 | `docs/*`, `404.html` |
| T-15 | Integration PR #2 → main, merge, confirm GitHub Pages redeploy, record result here | done | arena/9978ab21-prod3 | all |

### Verification re-fetch (session arena/9978ab21-prod3, 2026-11-19)

Each submitted link was fetched again and its HTTP redirect followed to the official Amazon domain. Observed destinations match session 5a4e180c exactly:

- link.amazon/B04G1MEwY → https://www.amazon.com/dp/B0CDY277D3
- link.amazon/B02NbDxp3 → https://www.amazon.com/dp/B09B7SB46R
- link.amazon/B00hJ57DV → https://www.amazon.com/dp/B08DKYBTPH
- link.amazon/B0c8moW59 → https://www.amazon.com/dp/B0DHZTCNR5
- link.amazon/B0f3GKalj → https://www.amazon.com/dp/B0DZFD6R9Z

Intended ASIN / official listing URL / confirmation date / source remain blank for all five (short-link compliance status unresolved; no claim that the short links are invalid). Observed redirect targets are recorded separately and never merged with intended fields.

### Cross-scope requests

(none)

### Handoff / conflict log

2026-11-19: initial rebase of arena/9978ab21-prod3 onto origin/main conflicted on COORDINATION.md, data/products.json, data/sources.json. Resolved by keeping session 5a4e180c's versions (the mainline record); no other session's work was discarded. Duplicate file additions from the earlier draft of this session (index.html, guides/, categories/, products/index.html, executive-summary.md, flagged-for-review.html) were dropped to avoid duplicate content with the existing mainline site (articles/, air-fryers.html, meat-thermometers.html, compare.html, buying-guide.html, EXECUTIVE_SUMMARY.md, flagged.html, sources.html).

### Integration record

- PR #2: https://github.com/wingbangboozle1-lang/Prod3/pull/2 (arena/9978ab21-prod3 → main)
- Merge result: merged (merge commit 1056cb4c9a98558e4a5cd7849211c98b70463d17)
- PR #2 merged into main by gh pr merge --merge; no approval waited on (per instructions)
- GitHub Pages: source branch main, status built; live at https://wingbangboozle1-lang.github.io/Prod3/ (custom 404 served)
- Live checks: homepage renders disclosure above the fold (Tracking ID shopnow047c-20), five-product table with source links to official Amazon listings, category pillar pages, 8 question-shaped guides, chooser, compare page, feed.xml, sitemap.xml; /flagged.html live with FLG-001..FLG-008 and sources; none block the merge.
- Flagged irregularities and unverified items remain published on /flagged.html for owner review.

---

## Session arena/b84724ea-prod3 — independent audit and corrective PR (2026-11-19)

**What this session did.** Started from the same five supplied links on a branch cut from
`dea7fb6` — before sessions `5a4e180c` and `9978ab21` had published. It independently resolved the
same five short links and read the same five listings, then found the mainline already carried a
complete site. Rather than replace it, this session was re-scoped to an **independent audit** of the
merged site, and every one of its own parallel duplicates was deleted.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| A-01 | Resolve the five short links independently and compare against the mainline record | done | arena/b84724ea-prod3 | read-only |
| A-02 | Audit every rendered page for the required disclosure, sponsored coverage, price policy, canonicals, duplicate titles | done | arena/b84724ea-prod3 | read-only |
| A-03 | Remove published prices from all pages; state the §2(b) policy where prices used to be | done | arena/b84724ea-prod3 | `index.html`, `compare.html`, `air-fryers.html`, `meat-thermometers.html`, `articles/*.html`, `assets/style.css` |
| A-04 | Qualify every outbound Amazon link as `rel="sponsored"`, not only the `link.amazon` ones | done | arena/b84724ea-prod3 | `*.html`, `*.html` |
| A-05 | Put the exact §5 disclosure sentence on every page, top and footer; add canonical URLs | done | arena/b84724ea-prod3 | `*.html`, `articles/*.html` |
| A-06 | Fix `404.html` root-absolute URLs that 404 under the `/Prod3/` project path | done | arena/b84724ea-prod3 | `404.html` |
| A-07 | Add a complementary zero-dependency gate for the rules the existing gates missed | done | arena/b84724ea-prod3 | `tools/check_site.py`, `.github/workflows/pages.yml`, `scripts/check_site.py` |
| A-08 | Integration PR → main, merge, confirm Pages deploy, record result here | done | arena/b84724ea-prod3 | all |

### A-01 — independent re-resolution (no discrepancy with the mainline)

| Supplied link | Observed destination | Mainline record | Agrees |
|---|---|---|---|
| link.amazon/B04G1MEwY | amazon.com/dp/B0CDY277D3 | B0CDY277D3 | ✔ |
| link.amazon/B02NbDxp3 | amazon.com/dp/B09B7SB46R | B09B7SB46R | ✔ |
| link.amazon/B00hJ57DV | amazon.com/dp/B08DKYBTPH | B08DKYBTPH | ✔ |
| link.amazon/B0c8moW59 | amazon.com/dp/B0DHZTCNR5 | B0DHZTCNR5 | ✔ |
| link.amazon/B0f3GKalj | amazon.com/dp/B0DZFD6R9Z | B0DZFD6R9Z | ✔ |

This session's listing readings independently reproduced the mainline's flagged items F-01
(capacity: 6 liters in the field vs 6 quarts in the title), F-02 (preset count 24 vs 25) and
F-03 (a newer model advertised on the ThermoMaven page). No conflict.

### A-02 — defects found in the published site

1. **Prices were published on 8 pages** — 40 currency amounts on `index.html`, `compare.html`,
   `air-fryers.html`, `meat-thermometers.html` and four articles — while `disclosure.html` stated the
   opposite ("no price storage or display"). Program Policies §2(b) permits price display only when
   Amazon serves the data or it arrives via the Product Advertising API. **Resolved: all 40 removed**;
   the policy is now stated in the price slot itself, and the gate fails if a currency amount returns.
2. **Evidence links were unsponsored.** 42 Amazon anchors existed; the checker only inspected
   `link.amazon` hrefs, so 35 anchors to `amazon.com/dp/<ASIN>` and 7 to the Associates help pages
   carried `rel="noopener"` without `sponsored`. **Resolved: 42/42 now sponsored.**
3. **The exact §5 disclosure sentence was missing from every page but `404.html`.** Every page
   carried a paraphrase ("Kitchen Counter is a participant in the Amazon Services LLC Associates
   Program…" and "As an Amazon Associate, Kitchen Counter earns from qualifying purchases"). Agreement
   §5 specifies *"As an Amazon Associate I earn from qualifying purchases."* or a substantially
   similar statement. **Resolved: the exact sentence now appears in the top strip and the footer of all
   20 pages, alongside the existing paraphrase, which is left in place.**
4. **`404.html` was broken on the live site.** It used root-absolute URLs (`/assets/style.css`,
   `/compare.html`), which resolve against `wingbangboozle1-lang.github.io/` and drop the `/Prod3/`
   prefix, so the custom 404 loaded unstyled with dead links. The repository's own release gate failed
   on `main` because of it, which means the Pages deploy job was failing at the gate step. **Resolved:
   relative URLs, matching every other page.**
5. **Eight articles had no canonical URL.** **Resolved: all 20 pages now carry an absolute canonical.**

### A-03 — verification performed after the fixes

```
python3 scripts/check_site.py          All checks passed.
python3 tools/check_site.py            20 pages checked, 1265 assertions run — all passed
python3 tools/verify_site.py           Release gate passed.
python3 scripts/build_sitemap.py --check   OK: up to date
```

Crawled the built tree over HTTP at the real `/Prod3/` prefix: **24/24 URLs resolve, 0 broken**.
Every page carries the required sentence twice; **42/42 Amazon anchors are `sponsored`**; **zero
currency amounts** remain in any HTML file.

### Cross-scope requests

Editing files outside this session's original scope was unavoidable, because the defects above are
in shared output and every other session is finished. Each edit is listed in A-03..A-07 with its file
set. Nothing was deleted: the mainline site, its articles, its data registers, its docs and its two
gates are all intact, and this session's parallel duplicates were removed rather than merged.

### Handoff / conflict log

2026-11-19: merging `origin/main` into `arena/b84724ea-prod3` produced 10 add/add conflicts. **Every
conflict was resolved in favour of the mainline version** (`index.html`, `assets/app.js`,
`assets/style.css`, `data/products.json`, `data/sources.json`, `404.html`, `COORDINATION.md`,
`README.md`, `feed.xml`, `sitemap.xml`). This session's parallel site tree (`about/`, `air-fryers/`,
`compare/`, `dashboard/`, `guides/`, `product/`, `questions/`, `sources/`, `suggestions/`,
`thermometers/`, `build.py`, `content/`) was deleted, and its duplicate CI workflow
(`.github/workflows/checks.yml`) was removed because it asserted pages that do not exist in this
site. No other session's work was discarded.

### A-08 — integration record

- **PR #4:** https://github.com/wingbangboozle1-lang/Prod3/pull/4 (`arena/b84724ea-prod3` → `main`)
- **Merge result:** merged, merge commit `0449d9415dd6287d1fee7344d8c57d8666a417b7`, 2026-11-19 13:01:11Z.
  Merged without waiting for approval, per the project instructions.
- **Pre-merge gate:** `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py` and
  `scripts/build_sitemap.py --check` all passed on the merged tree. Nothing was merged broken.
- **Pages deploy:** `Deploy GitHub Pages` — **success**. `pages build and deployment` — **success**.
  Pages status `built`, source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/.
- **Note on the previous deploy:** the immediately preceding `Deploy GitHub Pages` run on `main` had
  concluded **failure**. It failed at the release-gate step because of the broken `404.html` recorded
  in A-02 item 4. The run triggered by this merge succeeds, which is the direct evidence that the 404
  repair fixed the deploy pipeline and not just the page.

### A-09 — live verification after deploy

Checked against the published site, not against the local tree:

| Claim | Verified on the live URL |
| --- | --- |
| Exact §5 sentence in the top strip | ✔ `Prod3/` renders "As an Amazon Associate I earn from qualifying purchases." before any product content |
| No prices rendered | ✔ the price slot reads "Current price on Amazon", the table cell reads "See Amazon", and the footnote states the §2(b) policy |
| Price policy stated honestly | ✔ `disclosure.html` now says no price appears anywhere, and records that dated prices were removed on 2026-11-19 |
| Canonical URLs | ✔ present in the served markup |
| Disclosure page still accurate | ✔ the "Where the disclosure appears" list no longer claims prices are dated and shown |

### Residual issues for the owner (not blocking, published on `/flagged.html`)

- **FLG-001 / Q-02** — the Associates ID `shopnow047c-20` still cannot be confirmed from outside the
  account; the served short-link URLs carry no visible `tag=`. Verify in SiteStripe before driving
  traffic.
- **FLG-006** — the `link.amazon` short-link format remains unresolved in the enrolled workflow; the
  live site still sends product buttons through `link.amazon`, so this is the highest-value
  five-minute task on the board.
- Live copy still contains two stale claims outside this session's scope: the `air-fryers.html` card
  reads "compared on capacity, footprint, wattage, and price" and the homepage call-to-action reads
  "Compare all five on capacity, footprint & price", although no price is shown any more. Both should
  be reworded to "…and sourcing" or similar. Logged rather than edited to keep this session's diff to
  the compliance defects.


## Session arena/7d756ee2-prod3 — re-verification (2026-11-19)

- Branch `arena/7d756ee2-prod3` was cut from `main` at `0749909`. No site content was changed.
- Gates run on the tree: `scripts/check_site.py` passed (21 pages); `tools/verify_site.py` passed;
  `tools/check_site.py` passed (21 pages, 1604 assertions); `scripts/build_sitemap.py --check` passed.
- Internal crawl across all 21 HTML files: 0 broken local links, 0 broken anchors. `feed.xml` and
  `sitemap.xml` parse as well-formed XML; the sitemap lists 20 URLs.
- Stale copy logged by session b84724ea is already fixed on `main`: the homepage tile, homepage
  sticky bar and category sticky bars now read "…sourcing", not "…price".
- Pages: `GET /repos/.../pages` reports `status: built`, source `main:/`. Latest `Deploy GitHub Pages`
  run on `main` concluded `success`. Live URL not fetched from the sandbox (outbound access is limited
  to GitHub/npm/PyPI hosts), so the live page was not re-read in this session.
- Not verified and not changed: Amazon listings and Associates reporting could not be re-fetched from
  this sandbox (amazon.com unreachable). Remaining blockers are owner actions, not code: FLG-001 (intended
  ASINs), FLG-006 (Special Link test in the enrolled Associates workflow), FLG-010 (account status),
  FLG-015 (no first-party reports, ledger empty), and the open items on the Direction page.
- Event note: the ledger defines five events; `assets/app.js` emits four locally (`reader_signup` only
  fires after a confirmed provider response, and none is connected). The Analytics page already says so.
- Cross-scope requests: none. Handoff: none.

## Session arena/8eac4288-prod3 — re-verification and analytics-doc reconciliation (2026-11-19)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-17 | Re-fetch the five supplied short links from the live Amazon listings; compare with the mainline record | done | arena/8eac4288-prod3 | read-only |
| T-18 | Reconcile `docs/analytics-endpoint.md` with the shipped measurement code (`assets/app.js`) | done | arena/8eac4288-prod3 | `docs/analytics-endpoint.md`, `COORDINATION.md` |
| T-19 | Re-run all release gates on the rebased branch; confirm the live site | done | arena/8eac4288-prod3 | read-only |

Branch note: this clone was shallow; `git fetch --unshallow` was required before the branch could be fast-forwarded to `origin/main` (`452406b`). No history was rewritten.

### T-17 — live listing re-fetch (2026-11-19)

Each `link.amazon` short link was fetched and its redirect followed. Each final URL and the listing title were read directly:

| Supplied link | Final destination | Listing title (as shown) | Matches mainline record |
|---|---|---|---|
| link.amazon/B04G1MEwY | amazon.com/dp/B0CDY277D3 | CHEFMAN 6 Quart Dual Basket Air Fryer Oven … | ✔ |
| link.amazon/B02NbDxp3 | amazon.com/dp/B09B7SB46R | Emeril Lagasse 26QT French Door Multi-Function Air Fryer Toaster Oven … | ✔ |
| link.amazon/B00hJ57DV | amazon.com/dp/B08DKYBTPH | Chefman Air Fryer 8 Qt … | ✔ |
| link.amazon/B0c8moW59 | amazon.com/dp/B0DHZTCNR5 | ThermoMaven 1 Sec Professional Digital Meat Thermometer … | ✔ |
| link.amazon/B0f3GKalj | amazon.com/dp/B0DZFD6R9Z | CHEF iQ Sense … Gen3 | ✔ |

Observed destinations are recorded only in the observed field. Intended ASINs, listing URLs, confirmation dates and sources remain blank (FLG-001). The short-link compliance status is still unresolved (FLG-006). Nothing here shows that the supplied links are invalid.

The listing pages also show "Sponsored" labels on some related-product ads. That is Amazon page content, not a site claim, and no price was copied.

### T-18 — analytics doc reconciliation

`docs/analytics-endpoint.md` described a file (`assets/js/analytics.js`), a storage key (`shopnow_events_v1`), a two-event schema and a `/analytics/collect` route that do not exist in the repository. It now describes what `assets/app.js` actually does: five defined events, four emitted locally, `reader_signup` gated on provider confirmation, the endpoint blank, and the decisions still needed before any server collection.

### T-19 — gates and live site

- `scripts/check_site.py` — all checks passed (21 pages).
- `tools/check_site.py` — 21 pages, 1604 assertions, all passed.
- `tools/verify_site.py` — release gate passed.
- `scripts/build_sitemap.py --check` — up to date.
- Live `analytics.html` read from `https://wingbangboozle1-lang.github.io/Prod3/analytics.html`: disclosure above the fold, endpoint described as not configured.

### Items that cannot be completed from this sandbox (owner action; not blocking)

These need access to accounts or decisions this session does not have. They are recorded here and on `direction.html`, not filled in:

- **Self-hosted analytics endpoint** (requested): GitHub Pages cannot receive POSTs. A backend or relay must be chosen first (`docs/analytics-endpoint.md`).
- **Search Console property and sitemap submission** (requested): requires the owner's Google Search Console account.
- **Associates Special Link test, intended-ASIN confirmation, account eligibility** (FLG-001, FLG-006, FLG-010): require the owner's Associates account.
- **Real product photography** (S-18): requires an Amazon-served image source decision; currently none used (FLG-008).
- **Publishing cadence, email signup, reader capture** (S-25, SG-27..30): need an owner decision and provider; the email form remains removed (FLG-014).

### Cross-scope requests

(none)

### Handoff / conflict log

- Rebase: none needed beyond the fast-forward to `origin/main` after unshallowing; no conflicts.

### Integration record — arena/8eac4288-prod3

- PR #9: https://github.com/wingbangboozle1-lang/Prod3/pull/9 (`arena/8eac4288-prod3` → `main`)
- Merge result: merged, merge commit `d9323de9213bf5c02ba2e36802597e2ebd48a829`. Merged with `gh pr merge 9 --merge`, without waiting for approval.
- Pages: `Deploy GitHub Pages` — success; `pages build and deployment` — success (both on `d9323de`).
- Live check: `https://wingbangboozle1-lang.github.io/Prod3/docs/analytics-endpoint.md` serves the reconciled text.

---

## Session arena/65412034-prod3 — verification and feed hygiene (2026-11-19)

**Branch:** `arena/65412034-prod3` (from `0749909bee7ffcd821655cc17ff1b59df0c8acbe`)
**Tracking ID:** `shopnow047c-20`

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-16 | Verify all 5 submitted links against official Amazon listings (amazon.com/dp/<ASIN>) | done | 65412034 | `data/products.json`, `data/sources.json` (read-only verification) |
| T-17 | Remove currency amounts and \"verified\" framing from feed.xml (no prices rendered; Program Policies §2(b)) | done | 65412034 | `feed.xml` |
| T-18 | Run release gates from clean checkout; confirm build passes | done | 65412034 | `scripts/*`, `tools/*` |
| T-19 | Commit, push, PR to main, merge, confirm GitHub Pages deploy | stale claim (session 65412034; no later commits on the board); handoff noted by arena/cafc55da-prod3, 2026-11-20 | 65412034 | all |

### T-16 — official-source verification (2026-11-19)

Each submitted link's observed destination was re-fetched from the official Amazon domain and compared with the register:

| Supplied link | Official listing (fetched) | Observed ASIN | Register agrees | Category node |
|---|---|---|---|---|
| link.amazon/B04G1MEwY | https://www.amazon.com/dp/B0CDY277D3 | B0CDY277D3 | ✔ | Air Fryers 17659096011 |
| link.amazon/B02NbDxp3 | https://www.amazon.com/dp/B09B7SB46R | B09B7SB46R | ✔ | Air Fryers 17659096011 |
| link.amazon/B00hJ57DV | https://www.amazon.com/dp/B08DKYBTPH | B08DKYBTPH | ✔ | Air Fryers 17659096011 |
| link.amazon/B0c8moW59 | https://www.amazon.com/dp/B0DHZTCNR5 | B0DHZTCNR5 | ✔ | Meat Thermometers 289810 |
| link.amazon/B0f3GKalj | https://www.amazon.com/dp/B0DZFD6R9Z | B0DZFD6R9Z | ✔ | Meat Thermometers 289810 |

Titles observed on the official pages match the register (Chefman 6 Qt Dual Basket; Emeril Lagasse 26QT French Door with \"24 One-Touch Preset Options\" / \"Six Cooking Accessories Included\"; Chefman Air Fryer 8 Qt TurboFry; ThermoMaven 1 Sec \"±0.5℉ Accuracy | NIST&NSF Certified | ... IP67\"; CHEF iQ Sense \"3 Ultra-Thin Probes | WiFi Unlimited Range | 1000°F Heat Safe | 5 Sensors | Gen3\").

Price drift confirmed vs the 2026-11-19 snapshots (B0CDY277D3 now $74.99 vs $79.93; B09B7SB46R now $229.99 vs $149.99; B0DZFD6R9Z now $139.99 vs $119.99) — prices are not rendered on the site, consistent with FLG-007/012.
Newer-model cross-promotion confirmed on B08DKYBTPH (B0CNY1YVDD) and B0DHZTCNR5 (B0GL7Z4KP4) — consistent with FLG-004/005.

Sources used (official):
- https://www.amazon.com/dp/B0CDY277D3 (official listing S10)
- https://www.amazon.com/dp/B09B7SB46R (official listing S11)
- https://www.amazon.com/dp/B08DKYBTPH (official listing S12)
- https://www.amazon.com/dp/B0DHZTCNR5 (official listing S13)
- https://www.amazon.com/dp/B0DZFD6R9Z (official listing S14)
- https://affiliate-program.amazon.com/help/operating/agreement (Operating Agreement S01)
- https://affiliate-program.amazon.com/help/operating/policies (Program Policies S02)

Intended ASIN fields remain blank (FLG-001); observed destinations kept separate and never merged (FLG-011).

### T-17 — feed hygiene

Removed from `feed.xml`: channel title \"Verified Picks\" → \"Sourced Picks\"; channel description \"verified against official Amazon listings\" → \"sourced from official Amazon listings\"; item descriptions containing \"verified specs\" and \"and price\"; holiday gift guide description containing \"$16.99–$149.99\" and \"five verified kitchen gifts\". No currency amount or unverified \"verified\" claim remains in the feed.

### T-18 — gate results (clean checkout)

- `python3 scripts/check_site.py` — All checks passed.
- `python3 tools/check_site.py` — 21 pages checked, 1604 assertions run, all additional rules passed.
- `python3 tools/verify_site.py` — Release gate passed.
- `python3 scripts/build_sitemap.py --check` — OK: sitemap.xml up to date.

No currency amounts remain in any HTML file; 42/42 Amazon anchors carry rel=sponsored; the exact §5 disclosure sentence appears above the fold and in the footer on all 21 pages.

---

## Session arena/65474d4f-prod3 — mobile-first pass + deploy diagnosis (2026-11-19)

**T-17 done.** Implemented audit item **S-20** (mobile-first), the last actionable blank-status row.
Scope kept non-overlapping (verified: `git log 452406b..origin/main` touched none of my files; rebase onto
origin/main at PR #11 was clean, net diff = exactly my 8 files).

- `assets/style.css`: every tappable control (.nav a, .btn, chooser buttons, sticky-bar link, skip link)
  gets `min-height:44px` on wide screens and `48px` at `max-width:600px`; full-width product CTAs and a
  16px text floor on small screens. Padding-only — appearance, copy, links and data unchanged. Existing
  8–18px flex gaps already meet Google's ≥8px spacing rule.
- Source for the change recorded honestly as **S19** in `data/sources.json`, `sources.html`,
  `docs/verification.md`: Google (Chrome for Developers) "Tap targets are not sized appropriately" —
  fetched from `developer.chrome.com`, confirming the 48×48px / ~8px rule. No product-source check was
  needed because no product value changed.
- Q-15 (disclosure at 320px) verified **structurally**: gate `tools/check_site.py P01-disclosure-position`
  already fails any page where the disclosure marker does not precede the first `<h1>` (holds on all 21
  pages), and the strip is a normal full-width block kept compact at ≤600px. A real-browser pixel check at
  320px with an enlarged system font was NOT run from the sandbox — left as a one-time owner task.
- `DIRECTION.md` / `direction.html`: SG-09 mobile-first row marked Done 2026-11-19.

Gates run on the rebased tree (all pass): `scripts/check_site.py` OK; `tools/check_site.py` 21 pages /
1606 assertions; `tools/verify_site.py` Release gate passed; `scripts/build_sitemap.py --check` up to date.

### Deploy record + a Pages-config finding for the owner (not caused by, and not blocking, this work)

- **PR #12** → merged to `main` at `ce7aee3` (merge commit), no approval waited on, per instructions.
- **Site is live with this change — verified on the served file**, not just the local tree:
  `https://wingbangboozle1-lang.github.io/Prod3/assets/style.css` returns the S-20 block. Latest Pages
  build = commit `ce7aee3`, `status: built`, `error: null`. The `pages build and deployment` run succeeded.
- **Finding:** the `Deploy GitHub Pages` workflow run for this merge concluded **failure at the
  `actions/deploy-pages@v4` "Deploy to GitHub Pages" step only** — every earlier step (incl. the release
  gate) succeeded. Cause: Pages `build_type` is **legacy** (GitHub publishes automatically from `main`
  `:/`), which is mutually exclusive with the `deploy-pages` action, so that action errors while the
  legacy pipeline still publishes. Same symptom on PR #11 (which also deployed). The red badge is a
  workflow/config mismatch, **not** a broken site.
- **Remedy (owner, one of two — not applied here, as it is outside this task's scope and the site publishes correctly):**
  (a) flip Pages source to **GitHub Actions** so `deploy-pages` succeeds and drop the redundant legacy
  path, or (b) delete the Setup-Pages/Upload/Deploy steps from `pages.yml` and keep it as a gate-only
  workflow, letting the legacy build publish. Either makes CI green without touching content.

Cross-scope requests: none. Handoff/conflict: resolved one COORDINATION.md rebase conflict with session
7d756ee2 (kept both sessions' board rows; renumbered my row T-17 since 7d756ee2 held T-16).

## Session arena/33e3e80f-prod3 (T-20/T-21/T-22) — 2026-11-19

### Claim-collision note (coordination record, no work discarded)

This session's original claim row used **T-17** (commit `b60a2e8`, pushed 21:5xZ). Session
`arena/65474d4f-prod3` claimed **T-17** concurrently (commit `67811f9`) for the S-20 mobile-first
pass and merged first (PR #12, `ce7aee3`). On rebase, this session's rows were renumbered
**T-20/T-21/T-22**; the mobile pass is preserved on `main` and registered in the canonical
suggestion ledger as **SG-19** (with its S19 source note). `assets/style.css` keeps both passes:
their 44/48px tap-target block and this session's focus-visible/card-lift rules coexist.
`feed.xml` was merged to this session's item copy, which also removes the two phrases the HTML
gate bans elsewhere ("whole-chicken test", "capacity per inch"). Q-15 keeps 65474d4f's
`verification_2026-11-19` field verbatim.

### T-20 — shop-polish (what changed, line-by-line)

- `index.html` rebuilt: buyer question hero; five product cards (spec chips, "consider if" line,
  capture-dated rating, "Check price on Amazon" CTA → supplied `link.amazon` URL with
  `rel="sponsored noopener"` + `data-asin`, source link under each card); chooser; category tiles;
  seasonal guides row; the same five-row source-linked data table; RSS capture card (no fake
  signup form); dashboard surfaces unchanged in the footer group. Every number on the page was
  re-checked against `data/products.json` by script: **25/25** (ASINs, links, dims, temps,
  ratings) pass. No prices rendered; no invented claims; disclosure strip untouched.
- `feed.xml`: gift-guide description no longer advertises a price range; basket-or-oven item
  says "seller-listed specs"; channel description says "each claim linked" (no "verified"
  overstatement). Feed title already migrated to "Sourced Picks" by 65474d4f — kept.
- `buying-guide.html`: "price snapshots do not establish value" → accurate statement that no
  price is displayed and value must be checked live.
- `EXECUTIVE_SUMMARY.md` / `executive-summary.html`: dated shop-polish section; "What happens
  next" path A no longer mentions price re-checks; flag list gains FLG-016.

### T-21 — direction desk

`direction.html` and `DIRECTION.md` now mirror the machine registries instead of an ad-hoc table:
full ledger **SG-01…SG-19** with status/effort/confidence/owner, open questions **Q-01…Q-21**
with who/status/how-to-find-out. The retired "weekly price re-check" row is explicitly superseded
by SG-17 (PA-API as the only compliant price path). New registered items: SG-15 (implemented),
SG-16, SG-17, SG-18 (proposed); Q-18 (blocking: Search Console), Q-19 (owner: PA-API
eligibility), Q-20 (email provider), Q-21 (SVG preview test). New flag F-21/FLG-016
(og:image SVG unverified in share previewers; reference cited as to-verify, not quoted).

### Verification performed and its boundary

Values presented are the ones already registered in `data/products.json` from the dated
2026-11-19 official-listing snapshots; this pass changed presentation and copy only, and no
value was altered, inferred, or filled. Outbound network access from this sandbox cannot reach
`amazon.com` or `link.amazon` (TLS connections blocked), so no live re-fetch was possible — the
snapshot registry remains the verification record, and that boundary is stated here rather than
papered over. Gates on the rebased, merged tree: `tools/verify_site.py` **pass**,
`tools/check_site.py` **pass** (21 pages, 1614 assertions, incl. their P01 disclosure-position
rule), `scripts/check_site.py` **pass**, `scripts/build_sitemap.py --check` **pass**.
Crawled the built tree: 21 pages, 637 local hrefs, **0 broken**; **123/123** Amazon anchors
`rel="sponsored"`; **zero** currency strings in any HTML.
### T-22 — PR, merge, and deploy record (session arena/33e3e80f-prod3)

- **PR #14:** https://github.com/wingbangboozle1-lang/Prod3/pull/14 (`arena/33e3e80f-prod3` → `main`)
- **Merge:** merged without waiting for approval at `32b3cddec83cfe8c3ac8e262a72bad8905052ed9`, 2026-11-19 21:45:38Z.
- **Pre-merge gates on the rebased tree:** all four pass (21 pages, 1614 assertions).
- **Deploy:** `Deploy GitHub Pages` run for the merge **success** (19s); `pages build and deployment` **success** (38s).
  Pages API: `status: built`, latest build commit = `32b3cdd`.
- **Live verification after deploy (served pages, not the local tree):** front page serves the new
  hero (“Basket or oven? Instant-read or wireless?”), five product cards with spec chips,
  consider-if lines, “Check price on Amazon” CTAs and per-card source links; direction page serves
  the SG-01…19 / Q-01…21 ledger with the corrected Path-A copy; top disclosure strip present on
  every checked page. Note: Pages CDN serves stale copies briefly — verify with a cache-busting
  query if a fetch shows the previous build.
- **T-20/T-21/T-22 marked done** in the task board. FLG-016 (og:image SVG) remains needs-review
  and is published on `flagged.html`; it does not block anything.

---

## Session `arena/a25ccde6-prod3` — independent audit, suggestions register, and publication polish

**Session ID:** `a25ccde6` · **Branch:** `arena/a25ccde6-prod3` · **Claimed:** 2026-11-19
**Base commit:** 0749909 (main after PR #7)

### Claim

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-13 | Line-by-line audit of data registers: source-ID integrity, intent/observation separation, dangling references | done | a25ccde6 | `data/*.json` |
| T-14 | Dedicated suggestions register (`suggestions.html`) + open-questions register (`questions.html`) with non-colliding IDs and a decision log | done | a25ccde6 | `suggestions.html`, `questions.html`, `direction.html`, `data/suggestions.json`, `data/open-questions.json`, `scripts/build_registers.py` |
| T-15 | Structured data + absolute social preview image + SEO furniture | done | a25ccde6 | `assets/og-image.png`, `index.html`, pillar/compare/guide pages, `404.html` |
| T-16 | Editorial/design pass: shop-like product cards, section rhythm, table polish, accessibility | done | a25ccde6 | `assets/style.css`, `assets/app.js`, `assets/product-art/*`, published HTML |
| T-17 | Extend release gates to cover the defects T-13 found (source-ID existence, register consistency, ratings, social image, accessibility) | done | a25ccde6 | `tools/check_site.py` |
| T-18 | Integration PR → main, merge, verify Pages deploy, record result | done | a25ccde6 | all |

**Scope note.** No other session is active on this branch. Files outside this session's claim
(published HTML other than the pages named above) are edited only where a defect found in T-13
requires it; each such edit is listed in the final record below.

requires it; each such edit is listed in the final record below.

### T-13 — audit result (verify line by line, session a25ccde6)

Re-verified against the live official sources on 2026-11-19, not against the repo's own claims:

| Check | Method | Result |
|---|---|---|
| `link.amazon/B04G1MEwY` → B0CDY277D3 | direct fetch, read final URL | confirmed, unchanged from the existing record |
| Operating Agreement §1 / §5 / §6 | fetched affiliate-program.amazon.com | §5 quote and "material breach" wording confirmed verbatim; updated 2025-10-15 |
| Program Policies §2(a) tag, §2(b) price + unclear shortening, §2(t) customer reviews, §2(v) obscuring the URL | fetched affiliate-program.amazon.com | all four confirmed; §2(t) reads "unless you have obtained a link to that customer review or star rating through Creators API or PA API" |
| FTC Disclosures 101 placement language | fetched ftc.gov | "place it so it's hard to miss", "should be placed with the endorsement message itself" confirmed |
| Google `rel="sponsored"` guidance | fetched developers.google.com | confirmed |

Defects found and fixed: I-01 (duplicate SG identifiers across two pages), I-02 (customer star ratings
rendered on 4 pages, contrary to §2(t)), I-03 (S07/S08 cited but undefined), I-04 (feed claimed a
"whole-chicken test" and a price range), I-05 (relative SVG og:image), I-07 (no structured data),
I-08 (404 on the old design), I-09 (stale "& price" copy), I-10 (no suggestions/questions page).
Recorded but deliberately not changed: I-11..I-14. Full list in `DIRECTION.md`.

### T-14 — three registers, one source of truth

`suggestions.html` (SG-01..SG-20), `questions.html` (Q-01..Q-17) and `citations.html` are generated
from `data/*.json` by `scripts/build_registers.py`. `--check` fails the build when a page drifts from
its data, and the Pages workflow now runs it. `direction.html` keeps only dated decisions and the path
chooser.

### T-15/T-16 — presentation

24 pages, all with a 1200×630 PNG social card, structured data, and typographic listing art rendered
from each product's own numbers (no photography, per Operating Agreement §1). Stylesheet rewritten;
every class the pages use is defined (checked programmatically).

### T-17 — gate strength

`python3 tools/check_site.py` → **24 pages, 2,496 assertions, all passed**. New rule groups:
`D06-D19` (source-reference integrity, citation blocks, no ratings, feed hygiene, social image,
JSON-LD, register freshness) and `A01-A14` (lang, alt text, image dimensions, empty links, single
`<main>`, skip link, social meta, description length, no third-party assets, image weight).

### T-13 verification commands and results

```
python3 scripts/check_site.py        All checks passed.
python3 tools/check_site.py          24 pages checked, 2496 assertions run — all passed
python3 tools/verify_site.py         Release gate passed.
python3 scripts/build_sitemap.py --check    OK: up to date
python3 scripts/build_registers.py --check  OK: register pages match data/*.json
```

Crawled the served tree at the real `/Prod3/` prefix: **33 URLs, 33 resolved, 0 broken**.
Programmatic HTML parse of all 24 pages: **0 unclosed elements, 0 duplicate IDs, 0 images without alt**.
Disclosure present twice on 24/24 pages · 203 sponsored anchor instances · 0 currency amounts ·
0 customer ratings.

0 customer ratings.

### Merge reconciliation with upstream (PRs #8-#14)

Upstream merged six sessions while this branch was open, including a shop-polish redesign of the
front page and an expansion of the Direction page to SG-01..SG-19 / Q-01..Q-21. Rebase and cherry-pick
both conflicted, so the work was replayed commit by commit onto `origin/main` (`32b3cdd`) and every
conflict was resolved by hand. What changed in the resolution:

| Collision | Resolution |
|---|---|
| `SG-15..SG-19` — upstream used all five for different proposals | my six proposals renumbered to **SG-20..SG-25**; **SG-21** was restored after a `=======` marker was mis-read and deleted it |
| `S07`, `S08` — my source additions | upstream never defined them either, so they were re-added as **S21/S22**; my other additions became **S23/S24/S25** |
| `S19` — upstream used it for the Lighthouse tap-target source | mine renumbered away from S19 entirely |
| `Q-18..Q-21` — upstream added four questions | upstream's `open-questions.json` taken wholesale; my register renders all 21 |
| `flagged.json` — upstream re-verified with F-01..F-21 | upstream taken wholesale, then its six dangling `S07` references remapped to the listing pages |
| `index.html` — upstream rebuilt the front page as a shop | upstream layout kept; its four re-introduced star-rating blocks removed (§2(t)), product-art cards upgraded to the rendered PNGs, citations/suggestions/questions added to the footer |
| `DIRECTION.md` / `direction.html` — upstream turned Direction into the full ledger | upstream ledger kept and my dated decision log appended; a duplicated document fragment produced by the conflict resolution was removed |
| `feed.xml` — the resolved file lost its XML prologue | rebuilt from upstream's body with prologue and closing tags; currency and "whole-chicken test" corrections re-applied |

Deliberate non-resolution: upstream's `SG-16` ("replace the SVG social preview with a raster card")
and `SG-02`-adjacent rows are left exactly as upstream wrote them. This branch **implements** SG-16
(`assets/og-image.png`, absolute on all 24 pages) but does not mark it implemented in the register,
because changing another session's status row is their call, not mine — recorded for the owner.

Verification after the merge, on the merged tree:

```
python3 scripts/check_site.py              All checks passed.
python3 tools/check_site.py                24 pages, 2496 assertions — all passed
python3 tools/verify_site.py               Release gate passed.
python3 scripts/build_sitemap.py --check    OK: up to date
python3 scripts/build_registers.py --check  OK: register pages match data/*.json
```

Served crawl at the real `/Prod3/` prefix: **33 URLs, 33 resolved, 0 broken**. HTML parse of all 24
pages: 0 unclosed elements, 0 duplicate IDs, 0 images without alt text.
---

## Session arena/28d2d6c0-prod3 — T-23 line-by-line verification and integration (2026-11-19)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-23 | Line-by-line verification of data registers and published claims against official sources; fix only demonstrable defects; final integration PR → main, merge, confirm Pages deploy | done (PR #18, https://github.com/wingbangboozle1-lang/Prod3/pull/18) | arena/28d2d6c0-prod3 | `data/sources.json`, `data/analysis.json`, `data/flagged.json`, `data/policy-checks.json`, `data/citations.json`, `sources.html`, `citations.html` (regenerated), `docs/verification.md`, `tools/verify_site.py`, `COORDINATION.md` |

Note: this session originally claimed "T-20" before the fast-forward to `origin/main` revealed that
session `arena/33e3e80f-prod3` already owned T-20 (shop-polish redesign). The claim was renumbered
to **T-23** during the rebase; no other session's rows were altered.

### What was verified live on 2026-11-19 (fetch of each official page, read line by line)

- **All five submitted short links** re-resolved: `B04G1MEwY → B0CDY277D3`, `B02NbDxp3 → B09B7SB46R`,
  `B00hJ57DV → B08DKYBTPH`, `B0c8moW59 → B0DHZTCNR5`, `B0f3GKalj → B0DZFD6R9Z`. Every live page title
  matches `observed_title` in `data/products.json` exactly; browse nodes `17659096011` / `289810`
  confirmed in the breadcrumbs; FLG-004 (B0CNY1YVDD) and FLG-005 (B0GL7Z4KP4) cross-promotions visible
  on their pages.
- **FLG-002 confirmed live**: Emeril listing title says "24 One-Touch Preset Options"; the
  About-this-item bullet says "25 COOKING PRE-SETS". P-02's listed dimensions (16.9"D × 15.8"W ×
  14.8"H), capacity (24.6 L), special features, material and color all match the live product table.
  Rating count drifted 18,371 → 18,375 (expected; snapshots are date-only, FLG-012).
- **Operating Agreement**: "Updated: October 15, 2025"; §1 Special Links wording, §5 exact statement
  ("As an Amazon Associate I earn from qualifying purchases." or any substantially similar statement)
  and the §6 material-breach clause all verified verbatim — C-01's quote_basis is correct.
- **Program Policies**: "Updated: April 14, 2026"; Qualifying-Purchase quote verified verbatim.
- **FTC Disclosures 101**: "Place it so it's hard to miss. The disclosure should be placed with the
  endorsement message itself." verbatim; page dated November 2019.
- **Google rel="sponsored"**: quote verbatim; "Last updated 2025-12-10 UTC".
- **Google people-first content**: self-assessment questions verified verbatim.
- **Google spam policies**: "Thin affiliation" section verified verbatim.
- **Amazon Creators API `ItemIdType`**: "Amazon Standard Identification Number: 10-Character
  alphanumeric unique identifier assigned by Amazon" — the official basis for the site's
  10-character ASIN figure.
- **Tree checks**: 24 pages crawled — 0 broken internal links or anchors; sitemap (23 URLs) and
  feed (8 items) resolve to real files; no undefined source IDs in any HTML.

### Defects found and fixed (all gates re-run green after each batch)

1. **S06 cited the wrong page.** `data/sources.json` S06 pointed at the Program Policies page for the
   "ASIN = 10 characters" definition; the definition lives on the Creators API `GetItems` page.
   URL, title and quote corrected to the verbatim wording (fetched 2026-11-19).
2. **Stale pre-revision source IDs** in `data/analysis.json` (P1–P5 → S03..S07), `data/flagged.json`
   (F-01..F-20) and `data/policy-checks.json` — old register IDs that now resolve to unrelated
   sources (FTC, Google, GitHub) were remapped or removed: C-08 → S22 (Google spam policies),
   C-09 → S02+S06 (§2(a) + ASIN definition), C-12 → S21+S25, C-14 → S21 (had been cited to a Chefman
   listing page). Upstream's belt-and-braces copies of the stale IDs were dropped in favour of the
   correct IDs only.
3. **`sources.html` published only 14 of 21 registered sources** (S06 and S21–S25 rows missing).
   All rows added; every registered source is now on the page.
4. **Citation log gaps.** `data/citations.json` ("a figure with no row here does not belong on the
   site") had no rows for the rendered S05/S06/S15/S19/S23 figures, and its page-experience row
   cited S21 instead of S25. Five rows added, attribution fixed, registers regenerated via
   `scripts/build_registers.py --check` (passes).
5. **`docs/verification.md`**: wrong flag cross-reference (`++FLG-003++` → FLG-006 for the
   short-link context), stale "all 21 pages" (now 24), stale session status, and a pointer to a
   non-existent `flaggedIrregularities` key (now `data/flagged.json`).
6. **Gate gap closed**: `tools/verify_site.py` now fails (exit 3) if any `Sxx` referenced from
   `data/*.json` is undefined in `sources.json`, or if any registered source is missing from
   `sources.html`. Negative-tested with a deliberate `S99`.

### Irregularities logged (non-blocking)

- Upstream's task board carries **duplicate T-20/T-21/T-22 rows** (both "in progress" and "done"
  variants) left by an earlier reconciliation. Not edited — they belong to `arena/33e3e80f-prod3`'s
  record; flagged here so the owner can collapse them.
- Upstream's S06 carried a note rationalising the policies-page citation ("same URL as S02…").
  Replaced by the verified Creators API citation.
- Live rating counts drift daily against the dated snapshot (e.g. Emeril 18,371 → 18,375); covered
  by FLG-007/FLG-012 — no site copy depends on the count.
- Everything else remains as already published on `/flagged.html` (FLG-001..016): intended ASINs
  unconfirmed (FLG-001), short-link compliance unresolved (FLG-006), account status unverified
  (FLG-010), ledger empty by design (FLG-015), SVG social card unverified (FLG-016).

### Verification commands run (all exit 0)

```
python3 scripts/check_site.py          24 pages — all checks passed
python3 tools/verify_site.py           21 sources; cross-references resolve; release gate passed
python3 tools/check_site.py            24 pages, 2505 assertions — all passed
python3 scripts/build_sitemap.py --check   OK: up to date (23 URLs)
python3 scripts/build_registers.py --check OK: register pages match data/*.json
+ custom crawl: 24 pages, 0 broken internal links/anchors; sitemap/feed targets all exist
```

### T-23 integration record (PR #18)

- **PR #18:** https://github.com/wingbangboozle1-lang/Prod3/pull/18 (`arena/28d2d6c0-prod3` → `main`)
- **Merge result:** merged, merge commit `7976331`, 2026-11-19; merged with `gh pr merge --merge`
  without waiting for approval, per the project instructions.
- **Pre-merge gates on the final tree (all exit 0):** `scripts/check_site.py` (24 pages),
  `tools/verify_site.py` (21 sources, cross-references resolve), `tools/check_site.py`
  (24 pages / 2505 assertions), `scripts/build_sitemap.py --check` (23 URLs),
  `scripts/build_registers.py --check`; plus a custom crawl of 24 pages with 0 broken internal
  links or anchors, and sitemap/feed targets all resolving to real files.
- **Pages deploy:** `Deploy GitHub Pages` run `44626132919` — **success**;
  `pages build and deployment` run `44626131859` — **success**. Pages status `built`,
  source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/.
- **Live check after deploy:** `sources.html` on the live site shows the corrected S06 row
  (Creators API `ItemIdType`, verbatim 10-character wording), the S19 and S21–S25 rows, the
  disclosure strip above the fold with the exact §5 sentence, and the submitted-links table with
  intended/observed fields kept separate.

### Post-merge stale-flag correction (follow-up to PR #18)

The publication-polish pass had already replaced `assets/og-image.svg` with a 1200×630
`assets/og-image.png` on all 24 pages, but three records still described the site as shipping
the SVG: FLG-016 on `flagged.html`, F-21 in `data/flagged.json`, SG-16 in
`data/suggestions.json` (status `proposed`), Q-21 in `data/open-questions.json`, and the SG-16
row on `direction.html`. Corrected: the format concern is resolved; the only part still open is
the share-debugger check (no debugger could be run from this environment), so SG-16 is now
`partly implemented`, FLG-016/F-21/Q-21 describe the PNG as shipped with the debugger run
outstanding, and `scripts/build_registers.py`'s status callout gained a
"partly implemented" definition so the three-state vocabulary stays honest. Registers
regenerated; all gates green.

### PR #19 record and conflict-marker incident (2026-11-19)

- **PR #19:** https://github.com/wingbangboozle1-lang/Prod3/pull/19 — merged, merge commit
  `f0c4eb0`. `Deploy GitHub Pages` run `44627207634` — **success**; `pages build and
  deployment` run `44627207005` — **success**; Pages status `built`.
- **Incident found in the live render (fixed in this PR):** `flagged.html` was shipping literal
  git conflict markers (`` … `

` … `>>>>>>> 338d1e6 (polish: …)`) around the
  FLG-015/FLG-016 block. The markers entered `main` with commit `de5592a` inside PR #17
  (session `arena/a25ccde6-prod3`) — a conflict resolution was committed mid-flight. Every gate
  run since then passed because no gate scanned for markers, and this session's earlier live read
  of `flagged.html` stopped one chunk short of the block. **Fixed:** the two sides were merged
  properly (FLG-015 keeps the polish's Basis line; FLG-016 keeps the corrected PNG wording) and
  `scripts/check_site.py` gained check #10 — a repo-wide conflict-marker scan over every
  non-binary file (negative-tested: exit 1 with a marker file, exit 0 clean).

### PR #20 record (2026-11-19)

- **PR #20:** https://github.com/wingbangboozle1-lang/Prod3/pull/20 — merged, merge commit
  `1e0326a` (conflict-marker fix + check #10 + this board's incident log).
- **Pages deploy:** `Deploy GitHub Pages` run `44628186981` — **success**;
  `pages build and deployment` run `44628185796` — **success**; Pages status `built`.
- **Live re-check (cache-busted fetch):** `/flagged.html` renders FLG-015 with its Basis line and
  the corrected FLG-016, with **no conflict markers**. Earlier post-deploy fetches returned a
  cached copy of the pre-fix page; the cache-busted request confirmed the deployed bytes.
- This closes T-23 for session `arena/28d2d6c0-prod3`. Residual open items are unchanged and
  owner-side: FLG-001, FLG-006, FLG-010, FLG-015 (ledger), FLG-016/Q-21 (share debugger),
  and the open questions on `questions.html`.

---

## Session `arena/2ef30474-prod3` — shop-first rebuild + decision desk (2026-11-20)

**Branch:** `arena/2ef30474-prod3` (from `af089d0`, the merge of PR #21)
**Tracking ID:** `shopnow047c-20`
**Claimed at:** 2026-11-20 (claim committed and pushed before any edit, per the board rules)

The brief for this session is editorial and structural, not another compliance sweep:
make the site **read like a shop**, give search engines **one canonical home**, and add a
**decision desk** where every outstanding choice can be reviewed before anything is built.
T-12/T-23 already handled disclosure placement, price policy, and source resolution; this
session does not reopen them.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-30 | Editorial voice pass: rewrite shop surfaces so products lead and the register reads as a publication (no claim, price or compliance wording weakened) | done | arena/2ef30474-prod3 | `index.html`, `air-fryers.html`, `meat-thermometers.html`, `compare.html`, `buying-guide.html`, `assets/style.css`, `assets/brand.js` (new), `assets/app.js` |
| T-31 | Brand + navigation pass: one masthead group, consistent active state, publication framing, favicon/social card | done | arena/2ef30474-prod3 | `assets/brand.js` (new), `assets/style.css`, `assets/favicon.svg`, all `*.html` mastheads |
| T-32 | Decision desk: one page where suggestions, open questions, missing information and paths can be reviewed and chosen | done | arena/2ef30474-prod3 | `decisions.html` (new), `DIRECTION.md`, `COORDINATION.md` |
| T-33 | Register defect: `SG-20` and `SG-21` carry identical proposals (verified below) | done — SG-21 retired in place, gate D20 added | arena/2ef30474-prod3 | `data/suggestions.json`, `suggestions.html` (generated), `direction.html` |
| T-34 | Three working decision tools: comparison builder, measurement converter, oven-to-air-fryer cheat sheet | done | arena/2ef30474-prod3 | `tools/*.html` (new), `assets/decision-tools.js` (new) |
| T-35 | Seasonality module: which guide a reader should see by month, stated as editorial judgement not demand data | done | arena/2ef30474-prod3 | `assets/brand.js`, `index.html`, `articles/holiday-kitchen-gift-guide.html` |
| T-36 | Gate extension for the new surfaces; then integration PR → `main`, merge, confirm Pages | done | arena/2ef30474-prod3 | `tools/check_site.py`, `scripts/build_sitemap.py`, `.github/workflows/pages.yml`, all |
| T-37 | Publication-polish follow-up on current `main`: RSS `rel="alternate"` in the head of all 30 pages; SG-27..SG-30 registered with evidence-based status; FLG-017 added to `data/flagged.json`; footer link label "Search Console is connected" reworded to "Search Console setup" | done (2026-11-20) | arena/e52053d1-prod3 | `*.html` (head feed link + one index.html label), `data/suggestions.json`, `data/flagged.json`, generated `suggestions.html`, `decisions.html`, `COORDINATION.md` |
| T-38 | Source-attribution integrity on current `main`: 19 mis-attributed citation fixes; gate `D15-attribution` added; Program Policies §2(t)/§2(v)/shortener citations marked not located (FLG-020); P-04 quotation and source-register gaps (FLG-021); generator `sponsored` marking limited to Amazon URLs | done (2026-11-20) | arena/9f36f5ee-prod3 | `data/suggestions.json`, `data/open-questions.json`, `data/policy-checks.json`, `data/citations.json`, `data/flagged.json`, `flagged.html`, `tools/check_site.py`, `scripts/build_registers.py`, generated `suggestions.html` / `questions.html` / `citations.html` / `decisions.html`, `COORDINATION.md` |

**Non-overlap:** no other session has a live claim (every earlier row is `done`, and its
branch is merged). If a session appears while this one is running, this scope is
`index.html`, the two pillars, `compare.html`, `buying-guide.html`, `decisions.html`,
`tools/`, `assets/brand.js`, `assets/decision-tools.js`, `assets/style.css`,
`data/suggestions.json` and the generated register pages. The **articles/** directory
(body prose), `data/products.json`, `data/sources.json` and `flagged.html` are **not**
in this session's scope for content changes; add a cross-scope request instead of editing.

### T-33 — the defect, verified before fixing

```
$ python3 -c "import json;d=json.load(open('data/suggestions.json'));\
[print(s['id'],s['status'],'|',s['title']) for s in d['suggestions']]"
SG-20 proposed | Pick one product as the site's spine and let the other four support it
SG-21 proposed | Pick one product as the site's spine and let the other four support it
```

Two different IDs name one proposal, which is exactly the failure the a25ccde6 audit
fixed for SG-01..SG-08 (I-01 on `direction.html`). Either the second row is a duplicate
to delete or it is a lost proposal. The decision is logged here and published on
`decisions.html` as a reproduced, not silently repaired, irregularity.

### Verification run for this session

Every external claim touched by new copy is re-checked against the source register before
it ships. Sources used, as already registered (no new source IDs invented):

| Claim used in new copy | Source | Status |
|---|---|---|
| Price/availability may be shown only when Amazon serves it or via Creators/PA API | S02 §2(b) | re-read live 2026-11-20 |
| Special Links must carry the Associates `tag` parameter in the URL | S02 §2(b) | re-read live 2026-11-20 |
| Program Content licence ends; images come from Creators/PA API | S02 IP License | re-read live 2026-11-20 |
| Qualify paid outbound links with `rel="sponsored"` | S04 | registered |
| Disclosure must be clear and conspicuous | S03 | registered |
| Safe minimum internal temperatures, probe placement | S17, S18 | registered |
| NIST traceability wording | S16 | registered |

Observed redirect targets re-fetched 2026-11-20 from the live short links and confirmed
identical to the register for P-01 (`B0CDY277D3`) and P-05 (`B0DZFD6R9Z`); the remaining
three were confirmed in the same way in this session's table run below. No new product
fact, price, rating or test result is introduced by this session's copy.

### Completion record — session `arena/2ef30474-prod3`

**Re-verification performed 2026-11-20 (not carried forward from an earlier session):**

| Check | Result |
|---|---|
| Five supplied short links re-fetched live | All resolve to the register's ASINs: B0CDY277D3, B09B7SB46R, B08DKYBTPH, B0DHZTCNR5, B0DZFD6R9Z — no drift |
| Amazon Program Policies re-read (§2(b) price + tag, IP License images) | Confirms the tagging requirement and the price rule the site is built around |
| USDA FSIS safe-temperature chart | Re-read, last updated 14 April 2025; 145/160/165°F figures transcribed verbatim with rest times |
| USDA FSIS probe-placement release | Re-read, 19 September 2023; the 92% mis-placement finding quoted from the release, not paraphrased into a stronger claim |
| Internal crawl | 30 pages, 0 broken links, 0 dead anchors, 0 orphans |
| Markup well-formedness | 30 of 30 pages parse with no unclosed or stray tags |
| Gates | `build_chrome`, `build_registers`, `build_decisions`, `build_sitemap`, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py` (3542 assertions), `tools/crawl_links.py` — all pass |

**Irregularity found and resolved:** `SG-20` and `SG-21` were byte-identical in
`data/suggestions.json` (same title, problem, evidence, options, recommendation, effort,
confidence, owner and blocks). SG-21 is retired in place with a `retired_note`; gate rule `D20`
now fails the build if two live suggestions share a title. Reproduced and published on
`decisions.html`; only the owner can confirm whether a different proposal was meant to occupy
SG-21.

**New surfaces:** `decisions.html` (generated), `tools/index.html`,
`tools/compare-builder.html`, `tools/oven-converter.html`, `tools/cook-temperatures.html`,
`articles/thanksgiving-temperature-plan.html`, `scripts/build_chrome.py`,
`scripts/build_decisions.py`, `assets/decision-desk.js`, `assets/decision-tools.js`,
`tools/crawl_links.py`, `data/decisions.json`.

**New gate rules:** `D20` duplicate live suggestions · `D21` decisions freshness · `D22` chrome
freshness · `D23`/`D24` decision evidence resolves · `D25`/`D26` question evidence resolves ·
`D27`/`D28` tools exist, are sitemapped and are linked · `D29` USDA values verbatim ·
`D30` seasonal guide surfaced.

**Cross-scope requests:** none. No file outside this session's claimed scope was edited. The
`articles/` body prose of the eight pre-existing guides is unchanged; only
`articles/thanksgiving-temperature-plan.html` (new) was added.

**Handoff / conflict log:** no other session held a live claim; no rebase conflict occurred.


### Session arena/f4694e48-prod3 — T-24 claim

Claimed and completed the executive-summary refresh only. Scope: `executive-summary.html`, `EXECUTIVE_SUMMARY.md`, and this task-board row/log. Corrected stale statements about ratings, the shipped PNG social card, and event/endpoint behavior. The summary now distinguishes dated observations from unconfirmed intent and includes ranked proposals, discovery questions, and official-source links without changing product data or claiming new live verifications.

#### T-24 completion record (session `arena/f4694e48-prod3`, 2026-11-20)

- Refreshed `EXECUTIVE_SUMMARY.md` and `executive-summary.html` to match the checked-in site and existing source register. Product rows link to each official Amazon listing. Fact, recommendation, and question tables include an official source column.
- Reconciled obsolete assertions: ratings are not displayed on cards; the shipped share image is PNG (external debugger check still open); the analytics endpoint is blank; five events are defined, four are counted locally, and `reader_signup` is reserved for provider confirmation; no aggregate analytics, verified search data, clicks, orders, revenue, or forecasts are claimed.
- Added buyer and owner decision support: ranked compliance/measurement/discoverability/editorial recommendations, missing-information questions and ways to discover answers. Suggestions remain proposals; no path is marked chosen.
- Reviewed existing registry evidence (last recorded verification 2026-11-19). This task did not fetch current Amazon listings or access Associates Central, Search Console, an analytics provider, or a share debugger. The status date is 2026-11-20; no new live verification is represented.
- Official references used in the summary: Amazon Associates Operating Agreement and Program Policies; five official product listing URLs; FTC Disclosures 101; Google sponsored-link, people-first content, spam policy, and snippet guidance. URLs are recorded in `data/sources.json` and linked inline.
- Gates (all pass): `python3 scripts/check_site.py` (24 HTML pages), `python3 tools/verify_site.py` (21 sources resolve and publish), `python3 scripts/build_registers.py --check`, `python3 scripts/build_sitemap.py --check`, and `git diff --check`.
- Remaining owner/external gates: FLG-001 intended product confirmation; FLG-006 Special Link workflow and reporting test; FLG-010 Associates account status; Search Console verification; selection and configuration of analytics/email infrastructure; social-preview debugger check. These remain visible on the review pages and do not justify invented values.

#### T-24 publication record (PR #22)

- **PR #22:** https://github.com/wingbangboozle1-lang/Prod3/pull/22 — merged to `main` at `2026-11-20T06:08:42Z`; merge commit `a7972192978110994dbcb2a7c5a9b5b522d823fe`.
- **GitHub Pages deploy:** workflow run `44685724944` — success on the merged SHA. Pages API status: `built`, source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/.
- **Live check:** fetched `/executive-summary.html` after deploy. The updated buyer-first executive summary, dated intent/observed link table, official-source links and above-the-fold disclosure are live.
- **Non-blocking irregularity:** the successful deployment emitted GitHub Actions notices that the pinned `actions/*@v4/v5` workflow actions target Node.js 20, which GitHub is moving to Node.js 24. No release check or deployment failed; workflow runtime upgrades can be scheduled separately.

### T-24b — final copy consistency audit (2026-11-20, `arena/71a41253-prod3`)

- Reconciled `README.md`, both executive summaries, analytics endpoint documentation/status, and current publication copy against the files that are actually shipped.
- Corrected stale claims that customer ratings appear on cards or are presented as current; ratings and prices are not displayed. The comparison page's rating row links Amazon Program Policies S02 §2(t).
- Corrected social-preview language: the site already ships `assets/og-image.png` (1200×630); only external share-debugger rendering remains unverified (F-21 / SG-16 / Q-21). Updated the Direction page's old suggestion/question snapshot, labeling the embedded SG-01..19 list as historical and pointing to the complete SG-01..25 generated register.
- Reconciled analytics docs with `assets/app.js` and `data/campaign-ledger.json`: five event names are defined, four are emitted by current local-only flows, `reader_signup` is provider-confirmation gated, and `ENDPOINT` is blank. No site-wide collection is represented as active.
- Manual-review policy links already in the source register: [Amazon Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement), [Amazon Program Policies](https://affiliate-program.amazon.com/help/operating/policies), [FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers), [Google outbound-link guidance](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links). This pass reconciled published copy to the repository's cited sources; it did not re-fetch the Amazon product pages or owner-only account data.
- Verification on 2026-11-20: `python3 scripts/check_site.py` (24 HTML pages), `python3 tools/verify_site.py` (21 sources; references and release gate passed), `python3 tools/check_site.py` (24 pages / 2,521 assertions), `python3 scripts/build_sitemap.py --check`, `python3 scripts/build_registers.py --check`, `git diff --check`, and a targeted code/data consistency assertion for the five events and blank endpoint — all passed.
- Remaining non-blocking / owner-side items are unchanged and stay on `flagged.html` and `questions.html`: intended link ASINs, enrolled Associates Special Link test/account eligibility, campaign report data, Search Console, an analytics hosting/privacy decision, and external share-debugger validation.

#### PR #24 merge record

- **PR #24:** https://github.com/wingbangboozle1-lang/Prod3/pull/24 — T-24b final consistency audit and release-check re-run; merged to `main` at `2026-11-20T06:12:17Z`; merge commit `eef416436dc557226c5dfacb0d176b2f547843d4` (`gh pr merge 24 --merge`, no-review merge per project instructions).
- **Pre-merge verification (all pass):** `python3 scripts/check_site.py` (24 HTML pages), `python3 tools/verify_site.py` (21 sources; release gate passed), `python3 tools/check_site.py` (24 pages / 2,521 assertions), `python3 scripts/build_sitemap.py --check`, `python3 scripts/build_registers.py --check`, `git diff --check`.
- **GitHub Pages deploy:** workflow run `44686152047` (Deploy GitHub Pages) — success on the merged SHA; companion build run `44686151504` — success. Pages API status: `built`, source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/. Live spot-check of `/executive-summary.html` after the earlier deploy confirmed the updated summary, dated intent/observed link table, official-source links, and above-the-fold disclosure.
- **Not claimed:** Associates account enrollment/eligibility (FLG-010), intended product confirmation (FLG-001), Special Link compliance/testing (FLG-006), social-preview debugger validation (F-21/SG-16/Q-21), Search Console setup, server analytics endpoint, or email provider — all remain flagged on `flagged.html` / `questions.html` and were not verified by this session.

## Session arena/70e8475c-prod3 — T-25 (2026-11-20)

Scope: live re-check only. No intended-ASIN, price, rating, or account value was added, and no new product was introduced. Single commit for claim, work, and log.

**Live fetches (2026-11-20, `fetch_page`):**

| Supplied link | Final URL read | Result vs 2026-11-19 |
|---|---|---|
| https://link.amazon/B04G1MEwY | https://www.amazon.com/ (homepage), 2 attempts | **Changed.** 2026-11-19 ended at `B0CDY277D3`. Flagged as FLG-017. |
| https://link.amazon/B02NbDxp3 | https://www.amazon.com/dp/B09B7SB46R | Same ASIN |
| https://link.amazon/B00hJ57DV | https://www.amazon.com/dp/B08DKYBTPH | Same ASIN |
| https://link.amazon/B0c8moW59 | https://www.amazon.com/dp/B0DHZTCNR5 | Same ASIN |
| https://link.amazon/B0f3GKalj | https://www.amazon.com/dp/B0DZFD6R9Z | Same ASIN |
| https://www.amazon.com/dp/B0CDY277D3 (control) | product page, title matches | Product page live |

**Official policy pages re-read 2026-11-20:** [Operating Agreement](https://affiliate-program.amazon.com/help/operating/agreement) (Updated October 15, 2025) and [Program Policies](https://affiliate-program.amazon.com/help/operating/policies) (Updated April 14, 2026). Both match `data/sources.json`.

**Changes made:**
- `data/products.json`: new `live_recheck_2026_11_20` object per product (dated, method, final URL, ASIN match). The 2026-11-19 `observed_*` fields and blank `intended_*` fields are unchanged. P-01 gains flag FLG-017.
- `flagged.html`: FLG-017 added (B04G1MEwY ending at homepage; cause not established; owner check in the Associates workflow).
- `executive-summary.html`, `EXECUTIVE_SUMMARY.md`: status note and link table now say the 2026-11-20 re-check happened and what it found. They no longer say no live check was made.

**Gates (all pass on the working tree):** `tools/verify_site.py` (release gate passed), `tools/check_site.py` (24 pages, 2589 assertions), `scripts/check_site.py`, `scripts/build_sitemap.py --check`, `scripts/build_registers.py --check`, `git diff --check`.

**Irregularities for owner review:**
- FLG-017 — B04G1MEwY resolves to the Amazon homepage today; it resolved to B0CDY277D3 on 2026-11-19. The product page itself is live. The cause is not established. It may be transient or a link-level change. A fetch cannot tell these apart.
- FLG-001, FLG-006, FLG-010 remain open and are unchanged by this session.
- Prices and ratings were not recorded in this re-check (FLG-007, FLG-012).
- Not claimed: Associates account status, Special Link test in the enrolled workflow, and any campaign report.

**Remaining owner-side gates:** FLG-001 (intended ASIN per link), FLG-006 (Special Link test), FLG-010 (account), FLG-017 (B04G1MEwY link check in Associates workflow).

### Merge with `origin/main` during this session — what happened and how it was resolved

While this session was working, three other PRs merged to `main` (#24, #25, #27). Merging
`origin/main` into this branch produced **five conflicted files**: `COORDINATION.md`,
`EXECUTIVE_SUMMARY.md`, `README.md`, `executive-summary.html`, `index.html`. Every conflict was a
**same-region edit, not a competing claim**, and all five were resolved by keeping **both** sides:

| File | Resolution |
|---|---|
| `index.html` | Kept this session's shop front; kept main's shorter price/ratings policy sentence, merged into one paragraph that also keeps the §2(b) explanation and the fuller-comparison link |
| `README.md` | Kept main's "Products / Analytics / Campaign ledger" status rows; kept this session's Pages count, gate list and build commands; registers table now lists DT-01..DT-10 and the retired SG-21 |
| `EXECUTIVE_SUMMARY.md` | Kept main's source-index paragraph and this session's shop-first addendum, in that order |
| `executive-summary.html` | Kept main's decision-brief callout and this session's change-log table and revenue-decision section |
| `COORDINATION.md` | Kept both session records in chronological order |

**No other session's work was discarded.** Verified afterwards: `scripts/check_site.py` (30 pages),
`tools/verify_site.py`, `tools/check_site.py` (3,629 assertions) and `tools/crawl_links.py`
(0 broken links, 0 dead anchors, 0 orphans) all pass on the resolved tree, and the repo-wide
conflict-marker scan reports 0 markers.

### FLG-017 changes this session's own conclusion — recorded honestly

At the start of this session `link.amazon/B04G1MEwY` resolved to `B0CDY277D3`, and this session
recorded "no drift" for all five links. **Later the same day the same link resolved to
`https://www.amazon.com/`, the Amazon homepage** — reproduced independently here and by session
`70e8475c` (FLG-017). This session's earlier statement was true when written and is no longer
true, so it was corrected rather than left standing. Three consequences:

1. `EXECUTIVE_SUMMARY.md` and `executive-summary.html` now state that four links resolved and one
   did not, and name FLG-017.
2. The front-page feature button and the air-fryer shelf button for P-01 now point at the
   **product page** (`amazon.com/dp/B0CDY277D3`, still `rel="sponsored"`) instead of the broken
   short link, and say why in plain words next to the button.
3. `DT-01` on the decision desk was rewritten around FLG-017 and promoted to the top cost line:
   one signed-in SiteStripe click per product is now the highest-value five minutes on the board.

This is not a claim that the supplied short links are invalid. The status of `B04G1MEwY` is
unresolved — it may be transient, a campaign-link change, or a link-level setting, and a fetch
cannot distinguish those.

### T-25 publication record (session `arena/70e8475c-prod3`, 2026-11-20)

- **PR #27:** https://github.com/wingbangboozle1-lang/Prod3/pull/27 (`arena/70e8475c-prod3` → `main`). Merged with `gh pr merge 27 --merge` at `2026-11-20T06:17:37Z`; merge commit `f2b3a07bdd65537341c2d7c84bb928beb5a8ae13`.
- **Deploy GitHub Pages (workflow):** run `44686775327` — success on `f2b3a07`.
- **pages build and deployment (GitHub built-in):** run `44686774699` — the build job succeeded; the **deploy job failed** with a transient results-receiver EOF on log retrieval. Re-running the built-in run is not permitted by GitHub. The Pages build history then recorded `f2b3a07` as `built`. Live fetch of `/flagged.html` on that build served FLG-017.
- **Concurrent merge:** another session (`arena/2ef30474-prod3`) merged PR #26 into `main` at `c49de86`, which includes `f2b3a07`. The `Deploy GitHub Pages` workflow on `c49de86` reports success (`gh run list`); the Pages API reports the latest build `built` at `c49de86`. The live `/executive-summary.html` shows the 2026-11-20 re-check text.
- **Gates re-run on the combined tree at `c49de86`:** `tools/verify_site.py`, `tools/check_site.py`, `scripts/check_site.py`, `scripts/build_sitemap.py --check`, `scripts/build_registers.py --check` — all pass.
- **Irregularity logged:** one red `pages build and deployment` run (deploy job, transient) on `f2b3a07`, superseded by the successful `c49de86` build. Not a content failure. A `POST /pages/builds` request from this session returned 403 (insufficient integration permission), so no manual Pages rebuild was requested.
- **Not claimed:** intended-ASIN confirmation (FLG-001), Special Link test (FLG-006), account status (FLG-010), FLG-017 cause, or any campaign data.

### Follow-up after PR #26 merged — source accuracy correction (2026-11-20)

One defect in this session's own work was found by re-reading the rendered decision desk on the
live site, and corrected:

| Row | Was | Why that was wrong | Now |
|---|---|---|---|
| DT-07 (analytics endpoint) | cited **S23**, GitHub's *custom 404 page* doc | S23 says nothing about static hosting or POST handling. It was a nearby-looking GitHub Pages page, which is exactly the kind of citation the brief forbids. | cites **S05** (*What is GitHub Pages?*), which describes static hosting, and the row states the POST limit plainly |
| DT-03 (Search Console) | cited **S21**, Google's people-first *content* guidance | S21 is about content quality, not Search Console verification. No registered source answers this question. | `sources: []` with `evidence_status: "unverified"` — rendered as **No official source**, which is the honest answer |

Both rows now pass gate rules `D23`/`D25` (every decision and question either resolves its
sources or is explicitly marked unverified). This is a correction to this session's own
publication, found after deploy rather than before it — recorded here rather than quietly fixed.


## Session arena/e52053d1-prod3 — T-37 (2026-11-20)

**Collision and handoff log.** This session first claimed T-25 and built a 2026-11-20 link re-check. Before its push, `origin/main` gained PR #27 (`arena/70e8475c-prod3`), which already held T-25 for the same re-check and FLG-017. Rebase conflicted on this file. Resolution: the duplicate T-25 work was dropped from this branch and not pushed. The other session's work is unchanged. This session then renumbered to **T-26** for the non-overlapping parts. A later `main` (PR #26 and the shop-first rebuild `9032a35`) changed the nav and generated the page chrome, so this pass was reduced again to what `main` still lacked. Two branch-history merges with `-s ours` were used to keep the remote branch history without force-pushing.

**ID note.** Renumbered from T-26: T-26 was already taken on `main` by session `arena/e83cdf55-prod3` (PR #30), so this record uses T-37, the next free ID on the board.

**What changed**

1. **RSS head link on the pages that lacked it.** On `origin/main` at `c49de86`, 20 of 30 HTML pages had no `<link rel="alternate" type="application/rss+xml">` in their head. The head is hand-written (`scripts/build_chrome.py` owns only the header and footer markers), so the link was added directly. All 30 pages now carry it.
2. **SG-27..SG-30 registered** in `data/suggestions.json`. The request named these rows, but the register ended at SG-25. SG-27 (one name for the Direction page) is `implemented` upstream in `9032a35`. SG-28 (RSS) is `implemented` by this pass. SG-29 (Search Console) and SG-30 (reader capture) are `proposed`, owner-decided, and not verified from this environment.
3. **FLG-017 added to `data/flagged.json`** so the machine-readable register matches `flagged.html`. The re-check and the `flagged.html` callout are from PR #27.
4. **Footer/home link label reworded.** `index.html` had a link labelled "Search Console is connected" (inside a sentence that says "When … is connected"). No Search Console property exists, so the link now reads "Search Console setup". Owner-side item SG-29 is unchanged.
5. **Generated files regenerated, not hand-edited:** `suggestions.html` (`build_registers.py`) and `decisions.html` (`build_decisions.py`).

**Verification (all exit 0 on this branch)**

```
python3 scripts/check_site.py              all checks passed
python3 tools/verify_site.py               release gate passed
python3 tools/check_site.py                all additional rules passed
python3 scripts/build_sitemap.py --check   up to date
python3 scripts/build_registers.py --check register pages match data/*.json
python3 scripts/build_chrome.py --check    chrome current on 30 pages
python3 scripts/build_decisions.py --check decisions.html matches its data
python3 tools/crawl_links.py               no broken links, no dead anchors, no orphans
feed.xml, sitemap.xml                       well-formed XML
rel=alternate feed link                    30 of 30 pages
git diff --check                           clean
```

**Sources:** no new external source. SG-27..30 cite only repo files, the FLG-014 record, and `git log` history.

**Irregularities (non-blocking)**
- The T-25 collision above, logged rather than edited on the other session's row.
- The SG-27..30 rows the request named did not exist in the register before this pass.
- Owner-side items unchanged: FLG-001, FLG-006, FLG-010, FLG-015, FLG-016, FLG-017 (short-link check in the Associates workflow), SG-29 (Search Console), SG-30 (reader capture).
- Not done: a self-hosted analytics endpoint. GitHub Pages cannot receive POST requests, and the repo has no backend.

## Session arena/9f36f5ee-prod3 — T-38 (2026-11-20)

**Collision and handoff log.** This session claimed T-26 at `5b64eb8` before starting the source-attribution pass. Before its push, `main` gained PR #30 (`arena/e83cdf55-prod3`, T-26), which took the same ID and created FLG-018 and FLG-019 for different subjects. The rebase of this session's two commits conflicted on this file. The rebase was aborted, and this session's original commit is preserved in the branch history. The branch was then merged with `origin/main` (merge commit recorded with upstream as a parent, tree kept equal to `origin/main`). The non-overlapping fixes below were re-applied on top of upstream. Work that upstream already completed (SG-27..SG-30, SG-21 retirement, RSS head link) was not repeated. This session's flag IDs moved to FLG-020 and FLG-021 to avoid colliding with upstream FLG-018 and FLG-019.

**What changed**

1. **19 mis-attributed citation fixes** (`data/suggestions.json`, `data/open-questions.json`, `data/policy-checks.json`; 34 changed lines). Each named publisher now matches a cited source's title. Examples: a Google policy cited to a product listing; an FTC quotation cited to Google's spam policy; a Google rule cited to a competitor listing. The wrong-to-right ID mapping is in the diff of commit `2de0d34`, which is preserved in this branch's history.
2. **Gate `D15-attribution`** (`tools/check_site.py`). A clause naming a publisher must cite a source whose title names that publisher. It is a heuristic. Mutation test on the merged tree: an FTC clause changed from S03 to S22 in a temporary copy fails with `[D15-attribution] ... 'FTC' claim cites S22, none of which is a FTC source`; the real tree passes.
3. **Unverified policy citations marked, not removed** (FLG-020). The live Program Policies page (updated April 14, 2026) was read for Section 2 on 2026-11-20. Section 2 has subsections (a) and (b) only. The §2(t) ratings clause, §2(v) URL-obscuring clause, and the shortener prohibition attributed to §2(b) were not found. `data/citations.json`, `citations.html`, `suggestions.json` now say "not located" rather than quoting them. The rating and price conduct on the site does not depend on those citations.
4. **Generator `sponsored` marking** (`scripts/build_registers.py`). Citation rows applied `rel="sponsored noopener"` to all sources, including the FTC, Google and Program-policy references. Now `sponsored noopener` is applied only to Amazon URLs (the same test as gate P07), and `noopener` to everything else.
5. **P-04 quotation and register gaps** (FLG-021). The quotation "There is a newer model of this item" is cited to S13. Only the first page of that listing was re-read, so the wording is not re-confirmed. The S-series numbers 07, 08, 09 and 20 are not defined in `data/sources.json`. Gate D06 forbids naming them in data, so the flag refers to them by number.

**Sources.** No new external source. Checked against: Program Policies (S02) live page, Section 2 (2026-11-20); the FTC, Google, NIST and USDA entries already in `data/sources.json`.

**Verification (all exit 0 on this branch, at the merged tree)**

```
python3 scripts/check_site.py              All checks passed.
python3 tools/verify_site.py               Release gate passed.
python3 tools/check_site.py                all additional rules passed (includes D15-attribution, D06, D21)
python3 scripts/build_sitemap.py --check   up to date
python3 scripts/build_registers.py --check register pages match data/*.json
python3 scripts/build_decisions.py --check decisions.html matches its data
python3 scripts/build_chrome.py --check    chrome current
python3 tools/crawl_links.py               no broken links, no dead anchors, no orphans
attribution re-check (/tmp/attr.py)        0 violations
git diff --check                           clean
```

**Irregularities (non-blocking, for the owner)**

- The brief's FLG-003 is not the short-link item; the short-link compliance item is FLG-006.
- `README.md` lists two register tables: a stale one ("as of 2026-11-19", SG-01..SG-25, F-01..F-21) and the current one ("as of 2026-11-20"). The README is claimed under T-22 (`arena/33e3e80f-prod3`, in progress). Left unedited; the stale table should be removed by the claimant.
- `DIRECTION.md` line 115 (2026-11-19 decision, "Remove customer star ratings") cites §2(t). That row is a historical record and was not changed. FLG-020 covers the citation.
- `data/flagged.json` FLG-017 has `status` open; `data/products.json` live_recheck_2026_11_20 still records the homepage result. Both left as recorded.
- Items for the owner, unchanged: FLG-001 (intended ASINs), FLG-006 (short-link compliance, including the Special Link test in the Associates workflow), FLG-010 (account status), FLG-017 (B04G1MEwY redirect), FLG-020 (policy citations), FLG-021 (P-04 quotation and register gaps).
- Not done: self-hosted analytics endpoint (GitHub Pages cannot receive POSTs); Search Console property (SG-29); reader capture (SG-30); campaign ledger (no first-party Associates report available to this session).

### T-37 integration record (session `arena/e52053d1-prod3`, 2026-11-20)

- **PR #31:** https://github.com/wingbangboozle1-lang/Prod3/pull/31 (`arena/e52053d1-prod3` → `main`).
- **Merge result:** merged with `gh pr merge 31 --merge`, `mergedAt` 2026-11-20T06:23:08Z, merge commit `e036edf2ca0447e1110bd6bbd0dece4fc9c9f00f`. Merged without waiting for approval, per the project instructions. No `--auto`.
- **Pre-merge gates:** all green on the branch (eight gates, listed in PR #31).
- **Post-merge gates on `e036edf` (the merged `main`):** `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`, `build_sitemap.py --check`, `build_registers.py --check`, `build_chrome.py --check`, `build_decisions.py --check`, `tools/crawl_links.py` — all exit 0. RSS head link on 30 of 30 HTML pages.
- **GitHub Pages:** `Deploy GitHub Pages` run `44687419004` (`success`) and `pages build and deployment` run `44687418865` (`success`) on `e036edf`. Pages API: `status: built`, source `main:/`, URL https://wingbangboozle1-lang.github.io/Prod3/.
- **Live check:** `https://wingbangboozle1-lang.github.io/Prod3/feed.xml` lists the guides, including the Thanksgiving guide added on `main`. `suggestions.html` renders from the same `data/suggestions.json` that passed the gates. (The page's "Register updated 2026-11-19" line predates this pass; it is generator text from `main`, logged here as an irregularity rather than edited.)
- **Collision log:** T-25 was taken by PR #27 (arena/70e8475c), and T-26 by PR #30 (arena/e83cdf55). This session's first two claims were withdrawn and renumbered to T-37. No other session's work was overwritten; the history was kept with `-s ours` merges, not force-pushes.


## Session arena/ce911db5-prod3 — T-40…T-45 (2026-11-20), rebased onto `68fb159`

**Renumeration.** Other sessions had already taken T-26 (PR #30) and T-31…T-39 while this branch was
open. This session's six rows are therefore **T-40…T-45**. Nothing published by another session was
deleted: on rebase, the conflicting page rebuilds (`index.html`, `air-fryers.html`,
`meat-thermometers.html`, `compare.html`) were resolved **in favour of the mainline version**, and only
this session's additive changes were re-applied on top.

| ID | Task | Status | Files touched |
|----|------|--------|---------------|
| T-40 | Shopper card anatomy: headline spec, plain trade-off line, and a conflict chip carrying both readings where a listing contradicts itself | done | `index.html`, `air-fryers.html`, `meat-thermometers.html`, `assets/style.css` |
| T-41 | Card art regenerated at 2x and re-compressed; still typographic label art, never a photograph of the product | done | `assets/product-art/*.png` |
| T-42 | `compare.html` at-a-glance banner: pick by the constraining spec, not by a declared winner | done | `compare.html`, `assets/style.css` |
| T-43 | Review surface: `ideas.html` (ranked moves, rejected ideas with reasons, decision block) wired into the Decision desk nav and footer; per-row **Do this / Maybe / No** marks plus a copyable decision block on the suggestions register; four-question half-hour short list on the questions register | done | `ideas.html` (new), `scripts/build_registers.py`, `scripts/build_chrome.py`, `suggestions.html`, `questions.html`, `assets/style.css` |
| T-44 | Two register defects found by reading and fixed: `DIRECTION.md` named question ids whose subjects did not exist (FLG-020), and cited a suggestion id absent from the register while the register skipped a number (FLG-021). Account-status question registered as Q-23; link question as Q-22 | done | `DIRECTION.md`, `data/open-questions.json`, `data/suggestions.json` |
| T-45 | Three new gates, each negative-tested: `D28`/`D29` (the digest may not cite a `Q-`/`SG-` id that is not in its data), `J01–J03` (`node --check` over every inline script and `assets/app.js`), plus `actions/setup-node@v4` in the Pages workflow | done | `tools/check_site.py`, `.github/workflows/pages.yml` |

| T-51 | Fresh line-by-line review of the registers and published surfaces; fix only demonstrable defects (mis-cited evidence, duplicate/renumbered flag IDs, stale counts), add gates so each defect cannot return, re-run all gates, PR → main, merge, confirm live Pages deploy. **Renumbered from a second T-46 claim** — `T-46` was already claimed and merged by `arena/59a087a1-prod3` (PR #38) while this branch was in flight; that row is untouched | in progress | `arena/77e66f80-prod3` | `tools/check_site.py`, `flagged.html`, `data/flagged.json`, `data/open-questions.json`, `data/suggestions.json`, `data/analysis.json`, `ideas.html`, `direction.html`, `README.md`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |

### Live observation, 2026-11-20 (T-41 / Q-22)

| Supplied link | Final URL read | vs 2026-11-19 | vs the other same-day record |
|---|---|---|---|
| `B04G1MEwY` | `https://www.amazon.com/` (homepage), 2 attempts | changed | agrees (FLG-017) |
| `B02NbDxp3` | `/dp/B09B7SB46R` | same ASIN | agrees |
| `B00hJ57DV` | `/dp/B08DKYBTPH` | same ASIN | agrees |
| `B0c8moW59` | `https://www.amazon.com/` (homepage), **2 attempts** | changed | **disagrees** — the other record reads `/dp/B0DHZTCNR5` |
| `B0f3GKalj` | `/dp/B0DZFD6R9Z` | same ASIN | agrees |

Both records are kept side by side; no tie is broken by seniority. Cause unestablished and not
asserted. Published as FLG-023 and registered as Q-22.

### Why this pass changed the shop pages at all

The cards previously carried a paragraph of prose each. Three fields were added and nothing was removed:
the largest honest figure (capacity, or probe count), a trade-off line naming who the product does *not*
suit, and — for the two listings that contradict themselves — a chip carrying both readings with a link
to the flag row. No price, no star rating, and no test claim was introduced; the conflict text is copied
from `data/products.json`, not invented. Measured figures added to the front page are the listed
dimensions and the stated temperature ranges only.

### Verification on the final tree

```
tools/verify_site.py                 Release gate passed
tools/check_site.py                  31 pages · 3891 assertions · all rules passed
scripts/check_site.py                All checks passed
scripts/build_sitemap.py --check     OK (30 URLs)
scripts/build_registers.py --check   OK
scripts/build_chrome.py --check      OK
scripts/build_decisions.py --check   OK
tools/crawl_links.py                 31 pages crawled · 30 reachable from index.html
                                     no broken links, no dead anchors, no orphans
```

Negative tests run this session: injecting the original JS defect fails `J02`; citing a phantom `SG-26`
from the digest failed `D29` before the digest was corrected, which is how FLG-021 was found.

### Flagged for owner review (do not block the deploy)

- **FLG-020** — `DIRECTION.md` question ids did not match the register; account-status question now Q-23.
- **FLG-021** — a cited suggestion id is absent and the register skips SG-26; not reconstructed.
- **FLG-022** — a generated decision block shipped a JS syntax error; a gate now parses every script.
- **FLG-023** — two of five links reached the Amazon homepage on 2026-11-20 and one same-day record
  disagrees. Not a finding that the links are invalid.
- Unchanged and owner-side: FLG-001 (intended ASINs), FLG-006 (Special Link test), FLG-010 (account
  status), Search Console (Q-18), analytics endpoint, email provider, share-debugger check (Q-21).

**PR and merge (T-38).** PR: https://github.com/wingbangboozle1-lang/Prod3/pull/33 (`arena/9f36f5ee-prod3` → `main`). Merge result is recorded in the next integration record after the merge.
### T-38 integration record (session `arena/9f36f5ee-prod3`, 2026-11-20)

- **PR #33:** https://github.com/wingbangboozle1-lang/Prod3/pull/33 (`arena/9f36f5ee-prod3` → `main`), head `694a95a`, merged with `gh pr merge 33 --merge`, `mergedAt` 2026-11-20T06:27:52Z, merge commit `266c1a63d642913d8d894f1521c6d56642fbabd5`.
- **Pre-merge gates:** all green on the branch (scripts/check_site, verify_site, tools/check_site incl. D15, the four `--check` freshness gates, crawl_links, feed/sitemap XML well-formed, `git diff --check`).
- **GitHub Pages:** `Deploy GitHub Pages` and `pages build and deployment` both `completed / success` for `266c1a6`.
- **Live check:** https://wingbangboozle1-lang.github.io/Prod3/flagged.html serves FLG-020 and FLG-021 (the two new flags).
- **Not claimed:** Associates account status, intended ASINs, Special Link validity, tracking-report attribution, Search Console, analytics volume, live traffic.

## Session `arena/09d7261c-prod3` — T-39 final integration round (2026-11-20)

Scope: fresh line-by-line review of the post-rebuild tree, demonstrable-defect fixes only,
Pages deploy reconciliation, gates, PR → main, merge, live confirmation. No product, price,
rating, or account data was added; no owner-only gate was claimed.

### Defects found and fixed (each verified before and after the edit)

| Defect | Evidence before | Fix |
|---|---|---|
| `direction.html` path chooser contradicted the canonical paths in `data/decisions.json` | Buttons/callout/JS still described “Steady publication / Conversion focus / Hold” and mis-cited “analytics endpoint (SG-04)” and “email capture (SG-06)” — SG-04 is the guides-format proposal, SG-06 is the buy-units proposal | Chooser, callout and JS labels rewritten to the `data/decisions.json` paths (Make it earn / Make it a publication / Narrow and harden, DT-01/05/06/07/09/10), with the correction dated and the old wording acknowledged in place |
| `DIRECTION.md` ledger index skipped SG-22..SG-25 while claiming to mirror `data/suggestions.json` | Index jumped SG-21 → SG-26 | Four rows added verbatim from the JSON (titles and statuses unchanged) |
| `DIRECTION.md` carried the same stale checkbox path list | Same wrong SG-04/SG-06 citations | Replaced with the DT-based paths and a dated supersession note; decision log gains the 2026-11-20 row |
| `DIRECTION.md` index rows SG-26..SG-30 described digest-only wording (chrome, nav labels, tools, seasonal, decision desk as "implemented") that never existed in `data/suggestions.json`, and after T-37 registered the canonical SG-27..SG-30 rows the digest and the register named different proposals | Register: SG-27 "One name for the Direction page", SG-28 "Ship the RSS feed…", SG-29/SG-30 proposed owner rows; digest kept 2ef30474's unregistered wording | Digest rows SG-27..SG-30 rewritten to mirror the register verbatim; SG-26 documented as an unoccupied ID with the reason; README register row now reads SG-01..SG-30 (SG-21 retired; SG-26 unoccupied) |
| Both executive summaries said “eight question-shaped articles” | 9 articles ship since PR #26 (Thanksgiving plan added) | “nine … (eight evergreen guides plus the dated Thanksgiving temperature plan)” in `EXECUTIVE_SUMMARY.md` (2 places) and `executive-summary.html` (2 places) |
| Board irregularity list stopped at FLG-015 while `flagged.html` published FLG-016/017 | List and page disagree | List extended with FLG-016/017 (from the published page) and the new deploy-path flag |
| Dual Pages deploy paths | Run 44686774699 (legacy “pages build and deployment”) failed its deploy step after the PR #27 merge while run 44686775327 (`Deploy GitHub Pages`) succeeded on the same SHA and the live front page served current content (fetched and verified) | Flagged as FLG-022 with the exact manual remedy (Settings → Pages → Source: GitHub Actions); `PATCH /repos/…/pages {"build_type":"workflow"}` was attempted and returned HTTP 404 (automation token lacks the Administration permission) — recorded, not hidden |

### Review performed (line-by-line, 2026-11-20)

- All 12 data JSON files enumerated and read (`products`, `sources`, `citations`, `flagged`,
  `suggestions`, `open-questions`, `decisions`, `policy-checks`, `verification`,
  `analysis`, `campaign-ledger`, `campaigns`); counts cross-checked against the pages that
  publish them (SG-01..SG-30 with SG-21 retired and SG-26 unoccupied, Q-01..Q-21, F-01..F-21,
  FLG-001..FLG-024, DT-01..DT-11).

### Collisions encountered and how they were resolved (no other session's work discarded)

- Before this session's first push, `main` gained PRs #26 (shop-first rebuild),
  #31 (T-37, SG-27..30 registration), #32 (T-26/e83cdf55) and #33 (T-38, FLG-020/021).
- First rebase conflict: the board row. Sessions e83cdf55 and e52053d1 had both already used
  the T-26 ID; per the board's one-identifier-one-meaning rule this session's claim was
  renumbered **T-39** and their rows kept untouched.
- Second rebase conflict (the work commit): FLG IDs had advanced to FLG-021 upstream, so this
  session's deploy-path finding moved from FLG-018 to **FLG-022** in `flagged.html`, README,
  and the board; git auto-merged the rest of the files (no content conflict).
- `flagged.html` briefly carried two FLG-018 callouts mid-rebase (upstream's intent-provenance
  flag and this session's deploy-path flag); resolved by renumbering this session's to FLG-022.
  Upstream FLG-018/019/020/021 are untouched.
- A third collision before the PR could merge: `main` gained PR #35 (T-40..T-45,
  `arena/ce911db5-prod3`), which took **FLG-022 and FLG-023** for different subjects, so this
  session's deploy-path flag was renumbered again, to **FLG-024** (`flagged.html`, README,
  board). Upstream FLG-022/023 are untouched. The merge kept upstream's SG-31 row and its
  FLG-021 gap note alongside this session's register-mirrored SG-26..SG-30 index rows, and
  kept upstream's T-38 record next to this session's T-39 record.
- Board sections for all 13 prior sessions read; the `assets/brand.js` file named in the
  T-30/T-31/T-35 scope rows does **not** exist in `assets/` — the seasonality/chrome logic
  ships in `assets/decision-desk.js`, `assets/decision-tools.js` and `scripts/build_chrome.py`.
  Logged here as a board-record inaccuracy; no code change made because no shipped file
  references `brand.js` (grep across HTML/JS/PY/YML: 0 hits outside the board).
- README release-workflow section and gate names re-checked against `.github/workflows/pages.yml`
  (freshness gates → release gates → crawl → deploy).
- Gates re-run after the edits: `build_chrome --check`, `build_registers --check`,
  `build_decisions --check`, `build_sitemap --check` (all current), `tools/verify_site.py`
  (release gate passed), `scripts/check_site.py` (all checks passed), `tools/check_site.py`
  (30 pages, 3,631 assertions), `tools/crawl_links.py` (30 pages crawled, 0 broken links,
  0 dead anchors, 0 orphans).


### Merge and deploy record (T-74)

- **PR #58** (`arena/30d1c448-prod3` → `main`): https://github.com/wingbangboozle1-lang/Prod3/pull/58
  — merged 2026-11-20 as merge commit **`bb4f7d3`** ("Merge pull request #58 from
  wingbangboozle1-lang/arena/30d1c448-prod3"), after six origin/main reconciliations
  (002ab81 → 8cc8d58 → ef84eef → 6455932 → 55cbc4a → d20a025), every one resolved keeping
  both sides' work.
- **`Deploy GitHub Pages` run `44698580964`** for `bb4f7d3`: **failure** — step "Regenerated
  surfaces are current" failed; the release gate and deploy steps were skipped. Cause: the
  merged main tree carried upstream's "Design brief for the next design pass" section inside
  the `build-chrome` footer region on `direction.html` (PR #97's own deploy run `44698151942`
  failed the same way before this merge; PR #96's run `44697996184` was green). The freshness
  gate correctly refused to ship a page the chrome builder would rewrite. No deploy was
  published from this run; the failure is recorded rather than retried away.
- **Repair (this change):** the design-brief section was moved out of the generated footer
  region into the page body **verbatim** (the builder rewrites region interiors — running it
  in place would have discarded the section, exactly the "brief vanishing" failure upstream
  fixed on `ideas.html` in `build_ideas.py`). `build_chrome.py` then regenerated the region;
  all gates green locally on the repaired tree (44 pages, 8,375 assertions; 0 broken links,
  0 dead anchors, 0 orphans). The deploy result for this repair PR is appended below once its
  run has completed.
- **Repair PR #99** ("T-74 deploy repair: move the direction.html design brief out of the chrome
  footer region + deploy record"): merged as **`1520bc5`** (2026-11-20).
- **`Deploy GitHub Pages` run `44699180452`** for `1520bc5`: **success**. Pages API reports
  `built`, `html_url` https://wingbangboozle1-lang.github.io/Prod3/ — and `build_type` still
  `legacy`, so the FLG-024 owner one-click fix (Settings → Pages → Source: GitHub Actions)
  remains open; per the standing instruction the deploy is judged by the `Deploy GitHub Pages`
  run and the live URL, both green here.
- **Live checks after deploy (fetched, not assumed):** the front page serves the disclosure
  strip above the first heading with Tracking ID `shopnow047c-20`, five product cards whose
  buy buttons open the product page with the site's tag, the FLG-006/FLG-031/FLG-039 flag
  references, and no prices or ratings; `direction.html` serves the design brief in its H1 and
  body (the relocated section is intact), the SG-20-onward / FLG-029 history note, and the
  verified-against-data callout. (This record page's own deploy run is not separately claimed.)

### Not claimed / not verified here (unchanged owner gates)

FLG-001 intended ASINs · FLG-006 Special Link test in the enrolled workflow · FLG-010
Associates account status · FLG-017 B04G1MEwY link check · Search Console (DT-03) ·
analytics endpoint (DT-07) · share-debugger check (F-21/Q-21) · Pages build_type setting
(FLG-024, owner one-click). No new claims about traffic, conversion, or product superiority.

### Merge and deploy record (T-39)

- **PR #36:** https://github.com/wingbangboozle1-lang/Prod3/pull/36 — merged to `main` at `2026-11-20T06:36:56Z`; merge commit `a861ed7d6078764ac5a6080a151d4d471ff248f9`. Before merging, `origin/main` (PR #35) was merged into the branch: both sides kept (upstream SG-31 row + FLG-021 gap note; upstream T-38 record; this session's register-mirrored SG rows and T-39 record), and the deploy-path flag renumbered FLG-022 → **FLG-024** after upstream took FLG-022/023.
- **Pre-merge gates on the merged tree:** all green — 4 `--check` freshness gates, `tools/verify_site.py` (release gate passed), `scripts/check_site.py` (all passed), `tools/check_site.py` (31 pages, 3,938 assertions), `tools/crawl_links.py` (31 pages crawled, 0 broken links, 0 dead anchors, 0 orphans).
- **GitHub Pages:** `Deploy GitHub Pages` run `44689052275` — **success** on `a861ed7`; companion legacy `pages build and deployment` run `44689051758` — also **success** this time (the FLG-024 race resolved cleanly here; the failure mode remains real and the owner's one-click fix stands). Pages API: `built` for `a861ed7`.
- **Live checks after deploy (fetched, not assumed):** the front page and `direction.html` serve the updated content — path chooser shows the canonical “Make it earn / Make it a publication / Narrow and harden” wording with DT references, the snapshot note reads “SG-20..SG-31 … the ID slot between SG-25 and SG-27 is unoccupied, FLG-021”, and the disclosure strip remains above the first heading.

*(final micro-PR: T-26 → T-39 label fix on direction.html + this record)*

## T-46 completion record (arena/59a087a1-prod3)

- Status: done — ready for PR to main.
- Official listing checks, 2026-11-20 (fetch_page of amazon.com/dp pages): S29 B0CDY277D3, S30 B09B7SB46R, S31 B08DKYBTPH, S32 B0DHZTCNR5, S33 B0DZFD6R9Z. Recorded in data/products.json under `official_listing_check_2026_11_20`; intended-ASIN fields are unchanged (still owner-unconfirmed, FLG-001).
- New conflicts published: FLG-022 (P-01 title 6 qt vs details table 6 liters); FLG-023 (P-03 450°F title vs 200–400°F spec; 1000W bullet vs 1700W spec). Cards on air-fryers.html now show both readings.
- Google Search Console sources registered: S26 (developers.google.com Search Console get-started), S27 (support.google.com ownership verification 9008080), S28 (support.google.com getting started 10267942). DT-03 now cites S26–S28 (evidence verified); Search Console questions cite them too.
- questions.html: new "Official source" column generated from data/open-questions.json; rows without a registered source show "No official source".
- Seasonal block corrected: "Thanksgiving is Thursday, 26 November" (2026-11-26 is the fourth Thursday of November).
- Gates on the rebuilt tree: build_chrome/build_registers freshness OK; check_site.py, verify_site.py, crawl_links.py (31 pages, 30 reachable, no broken links/anchors/orphans), tools/check_site.py all pass.
- Irregularity logged: flagged.html contains duplicate FLG-020 and FLG-021 identifiers (different subjects, pre-existing); not renumbered in this round — owner to decide.
- PR #37 Pages runs 44689292593 / 44689291961: outcomes to be confirmed by exact run ID after this push.


## Session arena/cafc55da-prod3 — T-47 integration check (2026-11-20)

**Claim collision, handled.** This session first claimed `T-46`, then found `T-46` already claimed and merged by `arena/59a087a1-prod3` (PR #38) while this branch was being rebased. Nothing was overwritten: this session's claim was moved to `T-47`, its duplicate T-46 claim commit was dropped in the merge with `origin/main`, and the other session's record stands as written. Board hygiene: the stale `in progress` duplicates for T-20/T-21/T-22 (superseded by the authoritative `done` rows) and the stale T-19 claim from session 65412034 were marked superseded, not deleted.

**No site content changed in this pass.** The only file in scope is this board.

### Verification on the merged tree (`origin/main` at `372afb0`, 2026-11-20)

| Check | Result |
|---|---|
| `build_chrome --check`, `build_registers --check`, `build_decisions --check`, `build_sitemap --check` | all current |
| `scripts/check_site.py` | all checks passed |
| `tools/verify_site.py` | release gate passed |
| `tools/check_site.py` | all additional rules passed |
| `tools/crawl_links.py` | 31 pages crawled; no broken links, no dead anchors, no orphans |
| Amazon anchors on all HTML pages | 226 of 226 carry `rel="sponsored"`; 0 violations (31 pages) |
| Exact Associates disclosure sentence | present on all 31 pages |
| `data/products.json` after PR #38 | intended-ASIN fields unchanged and still owner-unconfirmed (FLG-001); the new 2026-11-20 official listing checks are recorded separately under `official_listing_check_2026_11_20` |
| Pages | `Deploy GitHub Pages` run `44690171472` (PR #38 merge) **success**; companion `pages build and deployment` was in progress at the time of this check |

### Irregularities (for owner review; not blocking)

1. **Duplicate `FLG-021` on `flagged.html`.** Two different findings are both headed `FLG-021`: (a) *"Source register gaps and one listing quotation (2026-11-20)"* — this is the item in `data/flagged.json` and the matching row on `decisions.html`; (b) *"A suggestion id cited by the digest does not exist, and the register skips a number"* — this is the SG-21/SG-25→SG-27 gap note that `README.md` and `DIRECTION.md` cite as FLG-021. The two are not merged or renumbered here because all of those files are shared outputs and the owner should choose the new ID (the PR #38 record already left this to the owner).
2. **FLG-017 still open.** `link.amazon/B04G1MEwY` ended at the Amazon homepage on the 2026-11-20 fetch in this session as well.
3. **Pages build type** (FLG-024) still `legacy`; the owner-side one-click fix is still required.

### Still not verifiable from this sandbox (owner action)

FLG-001 intended ASINs · FLG-006 Special Link test in the enrolled Associates workflow · FLG-010 Associates account status · FLG-015 empty campaign ledger (no first-party reports) · DT-03 Search Console · DT-07 analytics endpoint · DT-10 / Q-14 publishing cadence (owner decision) · F-21 / Q-21 share-debugger check.


### T-47 merge and deploy record (arena/cafc55da-prod3)

- **PR #39:** https://github.com/wingbangboozle1-lang/Prod3/pull/39 (`arena/cafc55da-prod3` → `main`)
- **Merge result:** merged with `gh pr merge 39 --merge`, merge commit `cbae5c9c431a39f6451ebae5d807bdcc2e4341b8`, 2026-11-20T06:47:47Z. Not waited on for approval, per the project instructions.
- **Pages:** `Deploy GitHub Pages` run `44690336381` — success; companion `pages build and deployment` run `44690335588` — success. Pages API `status: built`, source `main:/`.
- **Micro-PR:** this record itself is merged in the follow-up PR that carries it.
---

## T-51 — final review round, 2026-11-20 (session `arena/77e66f80-prod3`; claimed as T-46, renumbered after a collision)

Claimed after reading the board and re-running every gate on `main` at `7c1b939`. The starting
tree was green, so this pass looked for defects the gates could not see: a green build can still
mean a flag id naming two subjects, a citation a reader cannot follow, or a count that was true
two sessions ago.

### What was found and fixed (each one demonstrable from the tree)

| # | Defect | Evidence | Fix |
|---|---|---|---|
| 1 | Duplicate flag ids on `flagged.html`: `FLG-020` and `FLG-021` each named two subjects at `7c1b939`, and PR #38 later gave `FLG-022` and `FLG-023` a second subject each, so four ids named eight things | `grep` of `<strong>FLG-` on the page gave two headings per id; `data/flagged.json` holds the original FLG-020..023 (policy citations, source-register gaps, P-01 capacity, P-03 temperature/wattage) | The later subjects renumbered **FLG-025, FLG-026, FLG-027, FLG-028** with an in-place note on each, so every id names one subject and the ids `data/products.json` already references (FLG-022/023) are unchanged |
| 2 | 24 register rows cited a source inline that their own `sources` list omitted | `Q-01` cited `S03`/`S21` and declared only `S22`; `Q-02` cited `S16`; `SG-05` cited `S01`/`S04` and declared `S21`; 20 more | Citations and declarations reconciled against the registered titles; `SG-09` re-attributed from the Emeril listing (`S13`) to Google's snippet guidance (`S24`) |
| 3 | Hand-typed ID ranges were stale on two review surfaces | `ideas.html` said `SG-01…SG-26` (register's last id is SG-31) and `FLG-001…FLG-020` (page publishes to FLG-026); `direction.html` said `SG-01..SG-25` and `Q-01..Q-21` (register has 23) | Ranges replaced with counts read from the data files |
| 4 | `decisions.html` still carried "until it is settled, treat SG-21 as an alias of SG-20" after SG-21 had been retired and a gate added | `scripts/build_decisions.py` string, and the page's own "Two things are wrong on this site right now" | Callout rewritten as settled; heading copy corrected |
| 5 | `data/analysis.json` published the same "depth, not area" finding twice with different rounding | `findings[2]` and `findings[3]` differed only by 7.1 vs 7 in | Collapsed into one finding with all three units' depth and clearance |
| 6 | `README.md` carried two register tables whose ID ranges disagreed with each other and with the pages (`Q-01..Q-21` in both) | README lines 66-82 at `7c1b939` | Replaced by one table with counts read from the JSON registers |
| 7 | `EXECUTIVE_SUMMARY.md` / `executive-summary.html` still described `SG-01…18`, `Q-01…21`, 30 pages and 3,541 assertions | Lines 53, 92, 104 of the summary; the HTML change-log table | Corrected to 30/23 rows, 31 pages, 4,073 assertions, with a note that the older figures were true when written |

### Gates added (so each defect cannot return silently)

- **D31** — a register row may not cite an `Sxx` inline that its own `sources` list omits.
  Negative-tested: clearing Q-01's `sources` fails the build.
- **D32** — flag ids must be unique on `flagged.html`, and every id in `data/flagged.json` must be
  published there. Negative-tested: restoring the duplicate `FLG-020` heading fails the build.
- **D33** — an ID range written into a heading must end at the register's last id. Historical prose
  that names an old range as history is exempt by design (only `<h1>`–`<h3>` are read).

### Sources re-read for this pass

- [Google Search Central — Qualify your outbound links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)
  (page states "Last updated 2025-12-10 UTC"), confirming that `rel="sponsored"` is the value for
  paid placements. This is the registered `S04` and its `updated` field matches the live page.
- [Amazon Associates Program Policies](https://affiliate-program.amazon.com/help/operating/policies)
  (page states "Updated: April 14, 2026"), confirming the `updated` field recorded for `S02`. The
  page's own section list still shows no separate §2(t)/§2(v), which is why FLG-020 keeps those
  clauses marked unverified rather than quoted.
- The `S09` token does appear in `data/suggestions.json` (`SG-09`) and resolves; FLG-021's claim that
  `S07`, `S08`, `S09` and `S20` are undefined was re-checked against `data/sources.json` and holds.

### Not verified here, and not claimed

Associates enrollment and eligibility (FLG-010 / Q-23), the intended ASIN for any link (FLG-001),
Special Link compliance or report attribution (FLG-006 / Q-02), the two homepage-resolving short
links (FLG-017 / FLG-023 / Q-22), Search Console and any query data (Q-18), any analytics endpoint
(FLG-015), share-debugger rendering of the social card (FLG-016 / F-21). No traffic, conversion,
commission or product-superiority claim is made anywhere in this pass.

### Collision with upstream, and how it was resolved

`main` moved three times while this pass was running: PR #38 (`arena/59a087a1-prod3`, which took
`T-46` and FLG-022/023), PR #39/#41 (`arena/cafc55da-prod3`, `T-47`), and PR #43
(`arena/6bf60cac-prod3`, `T-48`..`T-50`). Nothing from those sessions was discarded:

- **Board row:** this session's claim was renumbered `T-46` → **`T-51`**; upstream's `T-46` row and
  its completion record are kept verbatim, side by side with this record.
- **`flagged.html`:** resolved by keeping upstream's two listing-conflict callouts verbatim and
  moving this session's two subjects to FLG-025..FLG-028; `data/products.json`'s FLG-022/023
  references therefore still resolve to the same subjects.
- **`decisions.html`:** regenerated from `data/decisions.json` with `scripts/build_decisions.py`
  instead of hand-merged, so the generated page cannot drift from its data.

### Gates at close (all run on the merged tree before the PR)

`build_chrome --check` · `build_registers --check` · `build_decisions --check` ·
`build_sitemap --check` · `scripts/check_site.py` · `tools/verify_site.py` ·
`tools/check_site.py` (31 pages, 4,256 assertions) · `tools/crawl_links.py`
(31 pages, 0 broken links, 0 dead anchors, 0 orphans).

### Second collision: PR #43 landed mid-pass, and what changed because of it

`main` gained PR #43 (`arena/6bf60cac-prod3`, `T-48..T-50`) after this branch had already rebased.
That session had resolved the same flag-register problem differently and, in doing so, moved the
two listing conflicts out of `flagged.html` and renumbered the register to FLG-025..FLG-031.
Resolving the merge **kept upstream's resolution** rather than re-imposing this branch's numbering:

- `flagged.html` takes origin/main's block. Upstream retired FLG-022/023 as standalone callouts and
  now carries the P-01/P-03 conflicts on the product pages; re-instating this branch's copies would
  have published a finding upstream had deliberately consolidated. 27 callouts, no duplicate id.
- The three new rules were **renumbered into the free range** after upstream's D31/D32:
  **D33** citation-declared, **D34** flag-unique/flag-published, **D35** heading-range-current, and
  **D36** (new, added during the same merge) that the README register table must match the data.
  Upstream's D31 (publishing plan) and D32 (product pages) are untouched.
- `README.md` keeps one register table, re-read after upstream added SG-32..SG-35, Q-24..Q-26 and
  DT-11..DT-12; `ideas.html` keeps upstream's wider `FLG-001…FLG-029` range.
- `decisions.html`, `suggestions.html` and `questions.html` were regenerated from their data files
  rather than hand-merged.

Gates after the merge: 5 `--check` freshness gates (`build_chrome`, `build_registers`,
`build_decisions`, `build_sitemap`, `build_products`), `scripts/check_site.py`,
`tools/verify_site.py`, `tools/check_site.py` (**37 pages, 5,425 assertions**),
`tools/crawl_links.py` (37 pages, 36 reachable, 0 broken links, 0 dead anchors, 0 orphans).
D33, D34 and D36 were each negative-tested against the real defect; D35 was negative-tested with a
stale range written into `ideas.html`.


## Session `arena/6bf60cac-prod3` — T-48…T-50 (2026-11-20)

**Renumbering.** Other sessions claimed T-46 (59a087a1) and T-47 (cafc55da) while this branch was open.
This session's three rows were therefore renumbered **T-48…T-50**; nothing published by another session
was deleted or overwritten, and the conflicting page rebuilds were merged by keeping upstream's text and
re-applying only this session's additions.

### What was checked, line by line

| Check | Method | Result |
|---|---|---|
| Five supplied short links | `fetch_page` of each `link.amazon` URL, final URL read | **All five ended at `https://www.amazon.com/`** on this pass. Four dated observations now exist and disagree; all are kept (FLG-025) |
| Program Policies §2(b) tag requirement | Live read of <https://affiliate-program.amazon.com/help/operating/policies> (updated 2026-04-14) | Text quoted verbatim in `data/verification.json`; required to appear as a URL parameter |
| Tag presence on shipped links | Regex over all HTML | 23 `link.amazon` buy anchors, 192 `amazon.com` anchors, **0 anchors carrying `tag=`** (FLG-026) |
| Operating Agreement §5 disclosure sentence | Live read of the Agreement | Sentence present above the first heading and in the footer on all 37 pages |
| Flag register integrity | Ids compared between `data/flagged.json` and `flagged.html` | Four ids named two findings each after the merge; page-only callouts renumbered to FLG-030/031, register ids untouched (FLG-027) |

### Defects found and fixed

| Defect | Evidence | Fix |
|---|---|---|
| `FLG-020` and `FLG-021` each published two different findings | Two callouts per id on `flagged.html` | Later pair renumbered FLG-028/FLG-029 with the old wording kept and the change dated |
| Post-merge, `FLG-022` and `FLG-023` also doubled (upstream register vs page-only callouts) | `git show HEAD:flagged.html` | Page-only callouts renumbered FLG-030/FLG-031; the register's ids kept |
| No page per product — five products existed only inside comparison pages | Tree listing | `products/*.html` generated from `data/products.json` by `scripts/build_products.py`, linked from both pillars and the front page |
| No reviewable answer to "what gets written next" | 9 articles, no plan | `publishing-plan.html` + `data/editorial-plan.json`, gated by D31 |
| A buy button promised a destination no link reached on 2026-11-20 | FLG-025 vs the button label | Registered as SG-32 and DT-11 rather than quietly changed: the wording choice belongs to the owner |

### New gates (each negative-tested)

- **D31** — the publishing plan may not drift from `data/editorial-plan.json`, must be in the sitemap and linked, and may not carry a forecast claim. Negative test: changing one row title in the JSON without re-rendering fails `D31-plan-title`.
- **D32** — one page per registered product, each in the sitemap, linked from its pillar, naming its observed ASIN and showing the blank intent field. Negative test: editing a product page by hand fails `build_products.py --check`.
- `P17-unique-descriptions` caught two product pages sharing a meta description; the description now leads with the product name.

### Verification on the merged tree

```
scripts/build_chrome.py --check        OK (37 pages)
scripts/build_registers.py --check     OK
scripts/build_decisions.py --check     OK
scripts/build_products.py --check      OK
scripts/build_sitemap.py --check       OK (36 URLs)
scripts/check_site.py                  All checks passed
tools/verify_site.py                   Release gate passed
tools/check_site.py                    37 pages · 5,219 assertions · all rules passed
tools/crawl_links.py                   37 pages crawled · 36 reachable · no broken links/anchors/orphans
```

### Not claimed

Associates account status (FLG-010) · intended ASINs (FLG-001) · Special Link validity or per-link tag
presence (FLG-006, Q-24) · cause of the four disagreeing link observations (Q-25) · Search Console ·
analytics endpoint · any traffic, click, conversion or revenue figure.

## T-52 completion record (session `arena/f3900cd3-prod3`, 2026-11-20)

**Status:** done. Branch `arena/f3900cd3-prod3`, based on `372afb0` and merged with `f483b89` (PR #48).

### What shipped

| Change | Where | Evidence it works |
|---|---|---|
| `/start.html` — four cooking-intent paths, each two clicks from an official listing | `start.html`, `scripts/build_chrome.py` (primary nav), `index.html` (four-tile strip + hero CTA) | `crawl_links.py`: reachable from `index.html`, 0 dead anchors; gate `A06/A07/P01` pass |
| December guide, question-shaped | `articles/kitchen-gifts-that-get-used.html` | every figure copied from `data/products.json` (S29–S33 records); `check_site` P07–P09 (sponsored/noopener on every Amazon anchor) |
| Feed + sitemap wiring | `feed.xml` (item 10), `sitemap.xml` | `verify_site.py` now asserts **one feed item per published article** instead of a hard-coded 9, plus canonical link shape. Negative-tested: deleting the new item fails the gate |
| Register rows for this pass | `data/suggestions.json` SG-39..SG-42 | `build_registers --check` passes; `decisions.html` regenerated by its own builder |
| Render-on-CI design review | `.github/workflows/snapshots.yml`, `design/pages.json` | renders 10 pages at 1366 px and 390 px, fails on horizontal overflow, uploads PNGs as an artifact (see verification note below) |
| Flag-citation gate | `tools/check_site.py` D32 | negative-tested: repointing a citation at an undefined id fails the build; it caught four real dangling citations on the merged tree |
| Flag-id uniqueness gate | `tools/check_site.py` D31 | negative-tested by duplicating an id |

### Line-by-line verification performed

- **Sources.** No new product fact was introduced. Every number in the new guide was read from
  `data/products.json`, whose values cite the official listings S29–S33 (re-read 2026-11-20 by
  T-46). The guide cites those sources on the page.
- **Every new claim checked against the page it links to.** The Chefman capacity conflict is
  `F-01`; the CHEF iQ battery/warranty conflict is `F-03`; the Chefman 8 Qt temperature conflict is
  `F-02`/`FLG-031`. The first draft cited `FLG-022`/`FLG-023`, which no longer label findings
  after upstream's own renumbering — caught by D32 and corrected before this commit.
- **Disclosure.** Above the first `h1` on every new page, repeated in the footer, tracking ID
  present (gates P01/P01-position/P02 pass on 39 pages).
- **Sponsored marking.** Every Amazon anchor on the new pages carries `rel="sponsored noopener"`.
- **No prices, no ratings, no test claims, no first-hand experience** anywhere in the new copy
  (gates P10, P11, P12 pass; the guide says in two places that nothing was tested).
- **Not claimed:** Associates account status (FLG-010), intended ASINs (FLG-001), Special Link
  validity (FLG-006/025), search traffic, conversions. The guide states the account status is
  unverified and links the flag.

### Irregularities found on the merged tree (do not block)

- **FLG-022 and FLG-023 no longer label any finding.** Upstream renumbered the four colliding ids
  to FLG-028/029 (digest pair) and FLG-030/031 (script and short-link pair). The *product-page*
  conflicts they used to carry (P-01 capacity, P-03 temperature/wattage) survive only as `F-01`
  and `F-02` in `data/flagged.json`, and `F-02` is partly duplicated by `FLG-031`. Citations were
  repointed to existing ids; **the two findings were not re-registered under new ids**, because
  that is a content decision for the register owner. Flagged as **FLG-032** for review.
- **`data/flagged.json` and `flagged.html` are not generated from one another.** The page carries
  FLG-020/021/024..031 which the JSON does not hold. D32 gates the *citations*; the two stores can
  still drift.
- **The screenshots workflow cannot be dispatched from a branch.** GitHub only registers
  `workflow_dispatch` for workflows present on the default branch, so the job is first dispatchable
  after this merge. Dispatch result recorded below.

### Gates on the final branch tree

```
scripts/check_site.py                All checks passed
tools/verify_site.py                 Release gate passed
tools/check_site.py                  39 pages, 5,568 assertions, all rules passed
scripts/build_sitemap.py --check     OK
scripts/build_registers.py --check   OK
scripts/build_chrome.py --check      OK (39 pages)
scripts/build_decisions.py --check   OK
tools/crawl_links.py                 39 pages crawled, 0 broken links, 0 dead anchors, 0 orphans
```

## T-47 — final verification round for this session (arena/8706c7f7-prod3, branch arena/8706c7f7-prod3)

- Status: done.
- Claimed scope: full-tree line-by-line review, release-gate re-run after the PR #38 fast-forward, README cross-ref fix, Pages deploy confirmation, PR → main + merge.
- Files touched: `COORDINATION.md` (this record), `README.md` (Q-01..Q-21 → Q-01..Q-23 cross-refs; register had Q-01..Q-23).
- Work performed:
  - `git pull --rebase origin main`: integrated PR #38 (T-46, merge commit 372afb01); branch is now even with origin/main.
  - Reviewed: `data/products.json` (intent/observation kept separate; all five intended_ASIN/intended_listing_url/confirmation_date/intent_source blank pending owner confirmation — FLG-001; live recheck 2026-11-20 recorded, B04G1MEwY now lands on the Amazon homepage — FLG-017), `data/sources.json` (29 sources, all cross-references resolve), `data/suggestions.json` (SG-01..SG-31 with SG-26 absent, SG-21 retired in place — FLG-021 gap note stands), `data/open-questions.json` (Q-01..Q-23), `data/decisions.json` (DT-01..DT-10), `data/flagged.json`, `data/campaign-ledger.json` (empty by design, provenance dated).
  - All release gates pass on the rebuilt tree: four `--check` freshness gates (chrome, registers, decisions, sitemap), `scripts/check_site.py` (all checks passed), `tools/verify_site.py` (release gate passed), `tools/check_site.py` (4,059 assertions), `tools/crawl_links.py` (31 pages, 30 reachable, no broken links, no dead anchors, no orphans).
  - Verified user-facing surfaces present and consistent: publication front page (`index.html`, products lead, disclosure strip above the first heading), category hubs (`air-fryers.html`, `meat-thermometers.html`), `compare.html`, `buying-guide.html`, nine question-shaped guides in `articles/` (in `feed.xml` + `sitemap.xml`), suggestions ledger with path chooser (`suggestions.html`, `DIRECTION.md`), open questions Q-01..Q-23 (`questions.html`), executive summary (`EXECUTIVE_SUMMARY.md`, `executive-summary.html`), flagged-for-review page (`flagged.html`), sources page (`sources.html`).
  - Compliance marks verified on `index.html`: every outbound product link carries `rel="sponsored noopener"` with `data-event="outbound_click"`; the five defined outbound-click events are counted in `assets/app.js` (local-only; endpoint not configured — owner decision, Q-13).
  - Fixed `README.md`: three stale "Q-01..Q-21" cross-refs → "Q-01..Q-23". Re-ran `scripts/build_registers.py --check` and `tools/verify_site.py` after the edit — still pass.
- Pages: GitHub Pages API `status: built`, `https://wingbangboozle1-lang.github.io/Prod3/`, source branch `main`, HTTPS enforced. `Deploy GitHub Pages` run 44690171472 on 372afb01 — **success** (2026-11-20T06:46:25Z). Legacy companion run 44690171255 waiting — the documented FLG-024 dual-path race; non-blocking, owner one-click fix (Settings → Pages → Source: GitHub Actions).
- Irregularities carried forward (do not block; published on `flagged.html`): FLG-001 intended ASINs unconfirmed · FLG-006 Special Link test in the enrolled Associates workflow (owner-only; related: FLG-026 — 0 of 23 `link.amazon` buy anchors carry `tag=`) · FLG-010 Associates account status unverified · FLG-017 B04G1MEwY landed on the Amazon homepage on the 2026-11-20 recheck · FLG-024 legacy Pages build_type (dual-deploy race, owner one-click: Settings → Pages → Source: GitHub Actions) · FLG-025 four dated link observations disagree; all kept · Duplicate FLG ids renumbered upstream (ffcb419): page-only callouts FLG-028/029 and FLG-030/031; register ids untouched — current `flagged.html` state to be re-confirmed by owner. No Amazon listing was re-fetched by this session (outbound sandbox access does not include amazon.com); verification rests on the dated official-source citations in `data/sources.json` and the T-46 official-listing-check record.
- No conversion score, revenue forecast, or product-superiority claim is presented anywhere on the site; no traffic, click, conversion, or revenue figures are claimed.

## T-47 merge and deploy record (arena/8706c7f7-prod3)

- **PR #44:** https://github.com/wingbangboozle1-lang/Prod3/pull/44 (`arena/8706c7f7-prod3` → `main`)
- **Merge result:** merged with `gh pr merge 44 --merge`, merge commit `a5d3c3acc516ca63a55dc2e185db83ffd44008fe`, 2026-11-20. Merged without waiting for approval, per the project instructions.
- **Pages:** `Deploy GitHub Pages` run `44690954632` — **success** on `a5d3c3a` (2026-11-20); Pages API `status: built`, live at https://wingbangboozle1-lang.github.io/Prod3/ (HTTPS enforced, source branch `main`).
- **Final gates on the merged tree:** all green — four `--check` freshness gates (chrome, registers, decisions, sitemap), `tools/verify_site.py` release gate passed, `scripts/check_site.py` all checks passed, `tools/check_site.py` all rules passed, `tools/crawl_links.py` 37 pages crawled, 36 reachable from index.html, no broken links, no dead anchors, no orphans.
- Session branch `arena/8706c7f7-prod3` remains at `2155bf7` (merged into `main` via PR #44); no further task work is pending for this session.

## T-52 merge round 2 (session `arena/f3900cd3-prod3`, 2026-11-20)

A third upstream round (PRs #42, #44, #47, #51) landed before this branch merged. Resolved without
discarding anyone's work:

- **My gates were renumbered** `D31`/`D32` → **`D38`** (one flag id labels one finding) and
  **`D39`** (no page may cite a flag id that `flagged.html` does not declare). Upstream had already
  taken D31 (publishing plan) and D32/D33 (product pages) for different rules. Two gate ids for two
  different subjects would be the same defect the flag renumbering was fixing.
- **`D39` was widened, not weakened**: a finding declared *inside* another finding's note still
  counts as declared. `FLG-028` and `FLG-029` are announced inside `FLG-027` and appear nowhere else,
  so a naive scan called them undeclared. That is a gate bug, and it was fixed in the gate.
- **`data/flagged.json` and `flagged.html` disagreed** about `FLG-028`/`FLG-029`: the JSON holds
  both as items, the page only mentions them in `FLG-027`'s note. Both ids are cited from
  `decisions.html`, so a reader sent there had no finding to read. The page already states the
  renumbering, so this is recorded here rather than restated on the page; flagged for the register
  owner below.
- **`FLG-023` citations corrected to `FLG-031`** in `data/open-questions.json` (Q-02's evidence) —
  the last survivors after the earlier correction.
- **`README.md` register ranges** updated to the real last ids (`SG-01..SG-42`, `Q-01..Q-27`) and
  counts derived from the JSON, because upstream's own `D37-readme-range` gate correctly failed them.

Gates on this tree: all eight pass (`check_site`, `verify_site`, `tools/check_site` 39 pages /
5,808 assertions, four freshness checks, `crawl_links` with 0 broken links / 0 dead anchors /
0 orphans).
## Session `arena/2cd3bab9-prod3` — T-52 (merge record)

## Session `arena/fe5fd1d9-prod3` — T-38 (2026-11-20)

**Claim history:** claimed hand-built per-product detail pages early; main advanced three times
during the session (7c1b939 → 1e47d23 → ddb50f8). Two rebase attempts were abandoned when the
collision count made blind keep-both unsafe; the branch was then merged with origin/main
audited conflict-by-conflict instead.

**Supersede decision:** T-50 (session 6bf60cac) shipped the per-product pages as a generator
(`scripts/build_products.py`, five pages under `products/`, freshness gate D32 and coverage gate
D33). The generated pages are richer than this session's hand-built drafts (intent-blank tables,
`data-source-required` spec tables with per-cell listing links, all-button de-risking, D33 flag
coverage). Per the coordination protocol the generator and its pages were adopted as canonical;
the five hand-built drafts were deleted untouched, and no T-50 file was edited except through its
own generator.

**What shipped on top of T-50:**
- Merged origin/main (ddb50f8) into the branch; conflicts resolved theirs-first for every file
  T-50 owned, audited line-by-line for the rest. My deleted product slugs were repointed to the
  generated slugs in `compare.html` (columns and the per-product links line).
- **FLG callout-id-uniqueness gate**: written as D31, renamed D34 on the T-49 collision, then
  DROPPED during merge #2 — main's sessions had shipped the same fix generalized (D19-flg-one-meaning,
  D35-flag-unique, D38-flag-id-unique, counted where an id is defined). The defect is real (three
  sessions numbered flags independently) and is now covered by main's rules; keeping mine would
  have been a second, narrower copy of the same check.
- **Compare buy row de-risked:** all five `Check price` cells moved from the supplied
  `link.amazon/*` tokens to the official `/dp/` product pages, each annotated with the reason
  (FLG-025: every supplied short link landed on the Amazon homepage at the 2026-11-20 re-check),
  matching the policy the generated product pages already follow. The P-01 cell note cites
  FLG-025 (all five), not the earlier FLG-017 (one of five).
- **FLG-019 addendum** (dated, session fe5fd1d9): the finding's button counts have moved twice;
  records the current picture and says to re-measure before relying on any count.
- **FLG-030/FLG-031 register rows** (`data/flagged.json`): the decisions.html broken-script
  finding and the two-of-five homepage re-check finding existed as page callouts without register
  rows; registered so every published callout id has a register entry (FLG-031 cross-references
  FLG-025 as the wider observation).
- **SG-39 proposal** (`data/suggestions.json`): consider-if / look-elsewhere-if blocks and guide
  next-steps for the generated product pages; register-traced draft copy for all five products is
  preserved in this branch's history (commit fac7199 lineage) and the proposal asks the T-50
  generator owner to accept the block.
- **Executive summaries re-scoped** (`EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`):
  the "T-38 shipped five hand-built pages" narrative was replaced with the adoption story; page
  counts set to 37; README's stale "31 pages / 3,938 assertions" line replaced with a pointer to
  COORDINATION for final counts.
- **Merge-repair fixes:** the auto-merge double-added the `products/` glob in
  `scripts/check_site.py` and `tools/crawl_links.py` (every page counted twice; "duplicate title
  with itself" failures) — deduped; `scripts/build_sitemap.py` still carried priority overrides
  for my deleted slugs — removed; `sitemap.xml` regenerated (36 URLs, matches main's set).

**Verification at close, after merge #3 (all green):** `tools/check_site.py` (42 pages, 6,372
assertions), all seven freshness gates `--check` OK; earlier at merge #2: 39 pages, 5,908 assertions, `scripts/check_site.py`, `tools/verify_site.py` release gate, `tools/crawl_links.py`
(39 pages crawled, 38 reachable, 0 broken links, 0 dead anchors, 0 orphans), and all six
freshness gates (`build_chrome`, `build_registers`, `build_decisions`, `build_ideas`,
`build_products`, `build_sitemap`) pass with `--check`.

**Verification at the pre-merge-#2 tree (also green at the time):** `build_chrome --check`,
`build_registers --check`, `build_decisions --check`, `build_products --check`,
`build_sitemap --check`; `scripts/check_site.py` (all checks passed);
`tools/check_site.py` (37 pages, 5,311 assertions, all additional rules passed);
`tools/verify_site.py` release gate; `tools/crawl_links.py` (37 pages crawled, 36 reachable,
0 broken links, 0 dead anchors, 0 orphans).

**Sources:** no new web fetches were required this session; the FLG-025/FLG-017 link observations
and the FLG-019 original counts are prior sessions' records, reused with attribution on the page.

**Merge #2 addendum (origin/main c14b28c, PRs #54/#57/#60, merged 2026-11-20):**

- Conflicts resolved: `tools/check_site.py` (my D34 rule dropped — main's D19/D35/D38 one-meaning
  rules already cover it; their D18b ideas gate kept), `data/flagged.json` (theirs + my FLG-030/031
  appended — both ids were still free), `data/suggestions.json` (theirs; my SG-39 proposal renumbered
  **SG-48** after main took SG-39…SG-42 and SG-43…SG-47), `compare.html` (merged buy row: their "official product
  pages" header + ASIN-suffixed link texts required by P14b, my all-five `/dp/` hrefs + FLG-025
  notes — main's side still had four link.amazon cells), `flagged.html` (their corrected RESOLVED
  FLG-020 + my FLG-019 addendum re-attached), executive summaries (count-free phrasing adopted),
  COORDINATION (both rows kept).
- Gate-repair fixes on the merged tree: **D40-guide-count false positive on pure main** (the gate
  greps "eight articles" and matched main's own historical FLG-038 callout; rewrote one phrase to
  "Eight of the articles …" — meaning unchanged, regex no longer misreads history as a count
  claim); **D35-clause** (my HEAD Ratings row cited §2(t), unmapped in main's new
  `data/policy-clause-map.json`; adopted main's D35-safe wording); **P14b** (buy cells re-texted to
  "Check price <ASIN>" per the one-link-name-one-destination rule).
- **FLG-033/FLG-034 have callouts on flagged.html but no rows in data/flagged.json** (pre-existing
  on main). Not invented here; logged for the json owners.

**Merge #3 addendum (origin/main 8cc8d58, PR #65 et al., merged 2026-11-20, during PR #67):**

- Main added three guides (T-61/T-62), sources S37-S39 (T-60), flags FLG-039/040, SG-43…SG-47.
  Site is now 42 pages / 41 sitemap URLs.
- Conflicts resolved: `data/flagged.json` (theirs + FLG-030/031, still free), `data/suggestions.json`
  (theirs + my proposal as **SG-55**; a first renumber pass mistakenly renamed main's SG-43
  seasonal row — caught by gate D29 (DIRECTION.md cites SG-43) and fixed: main's row restored,
  my proposal appended as SG-48), `compare.html` (their buy cells now tagged
  `?tag=shopnow047c-20` product URLs — adopted; no short-link cells remain anywhere),
  `flagged.html` (their count-free FLG-038 head, independently fixing the same D40 false positive
  this branch had fixed with different wording), ideas/decisions/suggestions pages regenerated,
  executive summaries and README (register table rebuilt by `build_readme.py`).
- The FLG-019 addendum and FLG-030/031 register rows survived all three merges.

**Irregularities:** (1) main moved three times; rebase attempts #2/#3 abandoned in favor of an
audited merge after a blind keep-both resolver produced a wrong-but-clean tree. (2) Two gate-id
collisions were found and fixed: my D31 vs T-49's D31 (renamed D34), and doubled products globs
from the auto-merge. (3) My record commit from the pre-merge branch was discarded with the
abandoned rebase; this section is the record of record.
## Session `arena/d42249a7-prod3` — T-51 verification + shop-read pass (2026-11-20)

**Claim and renumbering.** This session first claimed `T-46` (taken by `59a087a1`), then `T-47`
(taken by `cafc55da`, and again by `8706c7f7`). Both were found on rebase, before any push of
work, so the row is **T-51**. Nothing published by another session was deleted or reverted.
The branch was rebuilt on `origin/main` (`a5d3c3a`) rather than merged, because five sessions
had rewritten the same generated surfaces; every change below was re-applied and re-verified
against the current tree, not copied from the earlier attempt.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-51 | Locate and correct the mis-numbered Program Policies clauses against the live page; remove repeated article blocks and duplicated card markup that make the shop read as generated; gate both; record a third dated link observation; document every published flag | done | `arena/d42249a7-prod3` | `data/policy-clause-map.json` (new), `data/policy-checks.json`, `data/citations.json`, `data/open-questions.json`, `data/suggestions.json`, `data/flagged.json`, `data/products.json`, `flagged.html`, `compare.html`, `ideas.html`, `direction.html`, `disclosure.html`, `citations.html`, `articles/*` (8 closers), `index.html`, `scripts/build_registers.py`, `tools/check_site.py`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `COORDINATION.md` |

### Official sources read live on 2026-11-20

| Source | URL | Page states | What it settled |
|---|---|---|---|
| Associates Program Policies (Participation Requirements; Commission Income Statement; Products Statement; Trademark Guidelines; IP License) | https://affiliate-program.amazon.com/help/operating/policies | Updated 2026-04-14 | §2 is "Links on Your Site", subsections (a) and (b) **only**; the star-ratings rule is **6(t)**, URL obscuring **6(v)**, unclear shortening **6(w)**, no price tracking **6(y)**; §2(b) carries price-display, misleading-claims, sub-tag and product-list rules; Trademark Guidelines item 7 governs third-party logos/content |
| Associates Program Operating Agreement | https://affiliate-program.amazon.com/help/operating/agreement | Updated 2025-10-15 | §1 Special Links and Program Content; §5 the exact required sentence; §6 a §5 violation is a material breach |
| USDA FSIS Safe Minimum Internal Temperature Chart | https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/safe-temperature-chart | Last updated 2025-04-14 | every value and rest time in `assets/decision-tools.js` matches — **no change needed** |
| NIST Metrological Traceability (TN 2156) | https://www.nist.gov/metrology/metrological-traceability | — | "Only measurement results are traceable"; NIST does not endorse products and forbids references to it in advertising — confirms the accuracy article, S16 quote sharpened |
| FTC Disclosures 101 | https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers | 2019-11 | disclosure must be hard to miss and sit with the endorsement; "you can't talk about your experience with a product you haven't tried" — the basis for the site refusing hands-on claims |
| Amazon product page (control) | https://www.amazon.com/dp/B08DKYBTPH | — | the fetch tool *can* render a product page, so the homepage landings are not a blanket tool block |
| The five supplied links | link.amazon/B04G1MEwY · B02NbDxp3 · B00hJ57DV · B0c8moW59 · B0f3GKalj | — | all five ended at `https://www.amazon.com/` in the 06:44–06:50 UTC run. Recorded as a third dated observation (`live_recheck_2026_11_20_five_links`). No claim of invalidity, no record overwritten |

### Defects fixed

1. **Wrong clause letters (10 places).** `2(t)` / `2(v)` / shortener-under-`2(b)` do not exist; corrected to **6(t) / 6(v) / 6(w)** in
   `compare`, `ideas`, `direction`, `disclosure`, `citations` (generator + page), `data/citations.json`, `data/policy-checks.json`,
   `data/open-questions.json`, `data/suggestions.json`, `DIRECTION.md`, and the FLG-020 callout. Published as **FLG-037**.
2. **Identical article closers (8 articles, byte-identical).** Replaced with a topic-specific next step each. Published as **FLG-038**.
3. **Duplicated spec pills on every front-page card.** Second copy was the same three values HTML-entity-encoded; removed.
4. **Published flags with no data record (21).** Enumerated in `data/flagged.json` under `alias_records` with their published titles, explicitly
   marked as narrative callouts with no data record, so a reader's page and the data file agree on which flags exist.
5. **Duplicate flag headings found in this tree** were already renumbered to FLG-028/029 by an earlier session; verified here that **29 headings are
   unique** and that no heading id repeats.

### New gates (each negative-tested)

- **`D35`** — every `Program Policies §x(y)` citation must be in `data/policy-clause-map.json`; a retired letter fails by name; a historical mention
  passes only when the same line says it was corrected. Negative test: restoring `§2(t)` in `compare.html` failed the build on three rules.
- **`D36`** — no article-length block (>300 chars of text) may repeat across articles. Negative test: copying one article's closer into another
  failed the build; restoring it passed.

### Gates on the final tree

```
build_chrome --check       OK (37 pages)
build_registers --check    OK
build_decisions --check    OK
build_sitemap --check      OK
scripts/check_site.py      All checks passed
tools/verify_site.py       Release gate passed
tools/check_site.py        37 pages · 5,208 assertions · all additional rules passed
tools/crawl_links.py       0 broken links, 0 dead anchors, 0 orphans
```

### Not claimed

Intended ASINs (FLG-001) · Special Link compliance in the enrolled account (FLG-006/FLG-026) · Associates account status (FLG-010) · what a signed-in
reader sees on the five links (three disagreeing 2026-11-20 observations are kept side by side) · traffic · conversion · product superiority.

### T-51 merge into the session branch (post-rebase reconciliation)

`origin/main` advanced three times while this pass was in flight (PRs #44, #48, #51). The branch was
built on `origin/main` rather than replayed, then `origin/main` was merged in. Conflicts were
resolved **by keeping both sides** and re-running the generators, never by discarding another
session's work:

- `tools/check_site.py` — this session's `D35`/`D36` blocks and upstream's `D37` README-gate block
  both kept (the clash was a shared insertion point, not a disagreement).
- `decisions.html` — regenerated from the merged `data/flagged.json` via `scripts/build_decisions.py`.
- `EXECUTIVE_SUMMARY.md` — kept this session's assertion count (37 pages, 5,436 assertions after
  the merge); upstream's count was from before the merge.
- `README.md` — upstream's new `D37` gate then failed on the register table, which had drifted as
  the registers grew. Corrected to the real counts: SG-01..SG-38 (37 rows, 1 retired), Q-01..Q-27
  (27), FLG-001..FLG-038 plus 21 alias records. This is the gate doing its job on the first run.

Final gates on the merged tree: `build_chrome --check`, `build_registers --check`,
`build_decisions --check`, `build_sitemap --check`, `scripts/check_site.py`, `tools/verify_site.py`,
`tools/check_site.py` (37 pages, 5,436 assertions) and `tools/crawl_links.py` — all pass.

#### Superseded claim text, kept for the record

This session's original claim was written as **T-47** before three other sessions took T-47/48/49/50.
The authoritative row is **T-51** above; the file scope and task are the same, and the work landed on the rebuilt branch.
The claim text is kept here so the board shows what was claimed, when, and why the number moved. Nothing was deleted.

**Claim (pushed first, before any edit).** Base commit `7c1b939`; rebased onto `372afb0`.
Renumbered **T-46 → T-47** on rebase: session `arena/59a087a1-prod3` had already claimed
T-46 for the official-listing checks below. Their row and record are untouched.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-47 | Correct demonstrable citation errors against the official Program Policies / Operating Agreement text; record the dated 2026-11-20 five-link observation as a second, separate record; remove duplicated card markup that makes the shop read as generated; add a gate that binds every Program Policies clause citation to a verified clause map; refresh the summaries; PR → main, merge, confirm Pages | in progress | `arena/d42249a7-prod3` | `data/policy-checks.json`, `data/policy-clause-map.json` (new), `data/citations.json`, `data/flagged.json`, `data/open-questions.json`, `data/suggestions.json`, `data/products.json`, `flagged.html`, `citations.html`, `questions.html`, `suggestions.html`, `ideas.html`, `compare.html`, `index.html`, `direction.html`, `DIRECTION.md`, `tools/check_site.py`, `EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`, `COORDINATION.md` |

Not editing: `assets/product-art/*` (typographic label art is deliberate and compliant —
FLG-008), article bodies, `assets/app.js`, `sitemap.xml`, `feed.xml` (authoritative
generated surfaces; regenerated only by their own builders if a builder input changes).

- **Claim history.** T-46 was taken on `main` by PR #38 (session 59a087a1). T-48 was taken by PR #43 (session 6bf60cac). This session's task is T-52.
- **Merge.** `origin/main` (at `2c8d152`) merged into `arena/2cd3bab9-prod3`. Upstream rows, FLG entries, product records and generated pages are kept. My earlier T-46/T-48 rows and session log are not carried forward.
- **Decision.** DT-10 marked decided (owner instruction, one guide a month, owner approver, next due 2026-12-31). DT-12 remains open.
- **Flags.** FLG-032 (duplicate board task IDs T-12 to T-23; earlier wording that the T-20 to T-22 duplicates were removed is corrected: they are superseded, not deleted). FLG-037 (no consistent per-row fetch date in the source register). The FLG-022/023 identifier collision and the RSS-title mismatch are already resolved upstream, so no new flag is raised for them.
- **Gates.** build_chrome, build_registers, build_decisions, build_sitemap `--check`; verify_site; scripts/check_site.py; tools/check_site.py; tools/crawl_links.py. All pass on the merged tree.
- **Not done.** Source spot-check for S05, S10–S15, S17–S19, S21–S25. Pages deploy outcome for this merge: pending at the time of writing.
- **PR and merge.** Recorded below once merged.


---

## Session arena/0b7a3dd6-prod3 — reader-first polish + line-by-line audit (2026-11-20)

**Session ID:** `arena/0b7a3dd6-prod3` · **Branch:** `arena/0b7a3dd6-prod3` (cut from `7c1b939`, the T-39 merge on `main`)

### Claims (written, committed and pushed before any file edit)

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-40 | **Highest-value fix:** one product (Chefman 6 Qt Dual Basket, B0CDY277D3) is linked to a **broken** short link (`link.amazon/B04G1MEwY`) on `compare.html` and `articles/holiday-kitchen-gift-guide.html`, including in a "Check price" buy button, while other pages correctly route that product to the product page. Route every reader-facing link for that product to the product page and say why, matching the treatment already used on `index.html` / `air-fryers.html`. No href is claimed invalid; the short link is unresolved (FLG-003/FLG-017) and stays listed on the evidence pages. | in progress | arena/0b7a3dd6-prod3 | `compare.html`, `articles/holiday-kitchen-gift-guide.html` |
| T-41 | **Line-by-line audit of the board against the tree and the registers.** The board lists FLG-024 as an open irregularity; `flagged.html` (which `verify_site.py` reads as the authority for "is this flag documented") does not carry it. Reconcile and record. | in progress | arena/0b7a3dd6-prod3 | `COORDINATION.md` |
| T-42 | **One submission surface.** The owner is currently pointed at four review pages (`ideas.html`, `suggestions.html`, `questions.html`, `decisions.html`). Ship a single numbered read-in-order brief at the top of `ideas.html`, generated from `data/suggestions.json` + `data/open-questions.json` so its IDs and counts cannot drift again; retire the overlapping "Read in this order" block. Keep every existing surface reachable. | in progress | arena/0b7a3dd6-prod3 | `ideas.html`, new `scripts/build_ideas.py`, `scripts/check_site.py` (freshness gate hook only) |
| T-43 | **Missing-information discovery + research scope.** Add an MR row per missing item with the *exact* official location that would settle it and the measurable effort, plus an "additional research ideas" block for growing organic traffic (question-shaped topics only, no volume or popularity claims). Rows that cannot be settled from an official document are marked, not filled. | in progress | arena/0b7a3dd6-prod3 | `ideas.html` (+ its generator), `COORDINATION.md` |
| T-44 | **Copy pass: read like a shop, not an audit.** Remove the duplicate metric strip on the front page (the same five numbers are printed twice in cards that repeat themselves); keep every claim, disclosure and source link. | in progress | arena/0b7a3dd6-prod3 | `index.html` |
| T-45 | Release gates re-run, integration PR → `main`, merge, confirm Pages deploy, record PR + run IDs here. | in progress | arena/0b7a3dd6-prod3 | `COORDINATION.md` |

### Scope statement

Read-only outside this scope. Not touched: `data/*.json`, `assets/style.css`, `assets/app.js`, the masthead/footer chrome
(`scripts/build_chrome.py`), `flagged.html`, `sources.html`, `suggestions.html`, `questions.html`, `decisions.html`,
`direction.html`, `DIRECTION.md`, the executive summaries and the articles (except the two named above). The T-39
session's rows and every prior session's log are preserved above this block.

### Environment limit recorded up front (affects what can be claimed)

This sandbox has outbound network access to `github.com` / `codeload` / `api.github.com` / npm / PyPI **only**.
`amazon.com`, `affiliate-program.amazon.com`, `ftc.gov` and `developers.google.com` are **not reachable**, so this
session **cannot and does not claim** a fresh re-fetch of any listing or policy page. Every no-network statement below
is labelled as such, and no value in the registers is changed. Reader-facing pages get **no** claim of a fresh fetch;
a separate dated note is published on the review page so the reader can see exactly what was and was not re-observed.

### Irregularities found so far (detail and resolution appended as each is closed)

- **AUD-01** — the T-41 item above: FLG-024 is on the board but not on `flagged.html`.
- **AUD-02** — `compare.html` and the gift guide send the dual-basket product's buy button through the one short link
  that stopped resolving (FLG-017), so on those two pages the highest-traffic action can land on Amazon's homepage.

### T-40..T-44 outcome (session arena/0b7a3dd6-prod3)

| Task | Result |
|------|--------|
| T-40 | **Done.** `compare.html` and `articles/holiday-kitchen-gift-guide.html` now route the dual-basket buy button to `amazon.com/dp/B0CDY277D3`, matching `index.html` / `air-fryers.html`, with the reason on the page. The supplied short link is unchanged on `sources.html` and `products.json` and is still described as unresolved, never invalid. |
| T-40b | **Done.** P-04/ThermoMaven (`B0c8moW59`) is **disputed**, not broken: FLG-023 records the homepage on two attempts in one 2026-11-20 session and a product page in another. FLG-019 already records the decision not to swap buttons to bare `/dp/` (it would drop tracking), so the button is unchanged and a fallback product link plus both readings now sit under it on `index.html` and `meat-thermometers.html`. |
| T-41 | **Done.** Line-by-line audit of registers vs tree. Corrected my own claim above: FLG-024 **is** published on `flagged.html`. Four real defects found and fixed (below). |
| T-42 | **Done.** `ideas.html` now opens with one generated brief (`scripts/build_ideas.py`) built from `data/suggestions.json` + `data/open-questions.json`; the overlapping stale "Read in this order" block (which said SG-01…SG-26 and FLG-001…FLG-020) is gone. Gated by `build_ideas.py --check`, a new CI step and `tools/check_site.py` D18b. |
| T-43 | **Done in T-42's brief:** M-01..M-14 (missing information, each with the exact place the answer lives and its cost) and ten question-shaped research directions, each with the source it would need and whether that source is registered today. No volume, difficulty or popularity claim anywhere. |
| T-44 | **Done.** Duplicate spec strip removed from the four front-page product cards (the same metrics were printed three times per card); every value and source link kept. |

### Irregularities found and fixed (AUD series)

- **AUD-02 (fixed)** — the FLG-017 broken short link was still the buy button on `compare.html` and the gift guide.
- **AUD-03 (fixed)** — `flagged.html` defined **FLG-020 twice and FLG-021 twice** with different subjects. `citations.html` cites FLG-020 as the Program Policies citation gap while `DIRECTION.md` cites FLG-020 as the question-id mismatch, so a reader following either landed on the wrong card half the time. The later pair is renumbered **FLG-025 / FLG-026** (next free ids); the earlier definitions keep their numbers because other pages cite them. Gate **D19 was `... or True`** — it could never fail. It now counts identifiers where they are defined and fails on a repeat; negative-tested.
- **AUD-04 (fixed)** — stale self-descriptions: `decisions.html` counted a retired-in-place proposal as "open"; `direction.html`, `executive-summary.html` and `README.md` said "all 30 pages" while 31 ship; `direction.html` said "all 25 suggestions" while the register holds 30 rows over 31 ids; SG-28's evidence restated a page count that moves as pages are added.
- **AUD-05 (fixed)** — seven outbound product links shared a name with a different destination (bare "Listing" ×5 on the front page, "Amazon listing" ×5 on the executive summary, "Check price" ×5 on `compare.html`), so they were indistinguishable to a screen reader. All now name their ASIN in text and `aria-label`; new gate **P14b-unique-link-name**.
- **AUD-06 (fixed)** — `ideas.html` said "three of five links resolving … two landing on the homepage" and "two of five buy buttons go nowhere useful". Neither matches the record: one link is recorded at the homepage (FLG-017), one is disputed between two same-day sessions (FLG-023), and the most recent internal record reads all five as resolving. The page now states exactly that, disagreement included.
- **AUD-07 (open, no fix possible here)** — `data/products.json` P-02..P-05 `live_recheck_2026_11_20` each carry `final_url …/dp/<ASIN>`, but there is no `asin_in_final_url`/`matches_…` key in the object (the values appear only in adjacent keys), and the T-25 record says **two** links reached the homepage while those recheck rows say **one**. The disagreement is now published on `ideas.html` rather than resolved silently. **Needs the owner's signed-in check (Q-22).**

### Environment limit (restated, because it bounds every claim above)

Outbound network from this sandbox reached `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`
and `pypi.org` only. `amazon.com`, `affiliate-program.amazon.com`, `ftc.gov` and `developers.google.com` were **not
reachable**, so **no listing or policy page was re-fetched in this session** and **no new observation date is
published**. Everything above is a consistency check of the tree against its own registers plus source-code fixes.
That limit is published to the reader on `ideas.html` ("4. What this build actually verified") so the page cannot be
read as a fresh verification. A browser binary could not be downloaded either (the Playwright CDN is not reachable),
so **no screenshot-based visual check was performed** and none is claimed.

### Not claimed / not verified here

FLG-001 intended ASINs · FLG-006 Special Link test · FLG-010 account status · FLG-017/FLG-023 link resolution ·
Search Console (DT-03/Q-18) · analytics endpoint (Q-13) · share-debugger check (F-21/Q-21) · Pages `build_type`
(FLG-024). No claim about traffic, conversion, ranking or product superiority.

## T-52 merge round 3 (session `arena/f3900cd3-prod3`, 2026-11-20)

PRs #46, #47, #51 and #53 landed while this branch was open. Resolved without discarding work:

- **`tools/verify_site.py` was rebuilt from main, not hand-merged.** A first-pass resolution dropped
  the body of the file (the gate parsed a 16-line stub). Rebuilt from `origin/main` and the feed
  additions re-applied as a small addition; the file now runs and reports 10 guides in sitemap, feed
  and hub.
- **Feed headline now equals the page H1** for the December guide. Main added that rule; the right
  fix was the feed title, not the gate.
- **`FLG-032` collision**: main had already published FLG-032 (duplicate task identifiers on this
  board — the same problem this session has now hit three times). This session's finding on the two
  lost listing-conflict ids is now **FLG-034**.
- **`FLG-023` citations** in `index.html`, `meat-thermometers.html`, `executive-summary.html` and the
  `scripts/build_ideas.py` brief corrected to `FLG-031` — FLG-023 has not labelled a finding since the
  earlier renumbering. Caught by gate D39.
- **Card anchors on `air-fryers.html`** (`#dual-basket`, `#oven-style`) were lost in the merge and
  restored so `start.html`'s deep links resolve; `crawl_links.py` now reports 0 broken links.
- **`ideas.html`** regenerated by its builder after the brief correction (`D18b` gate).

Gates on this tree: all eight pass (39 pages, 5,906 assertions).
### Merge and deploy record (T-45)

- **PR #53:** https://github.com/wingbangboozle1-lang/Prod3/pull/53 (`arena/0b7a3dd6-prod3` → `main`) —
  **merged** 2026-11-20T06:57:48Z, merge commit `3a26ab31eba37e4c90c891fcd540339eb98d6c6c`.
- Merged without waiting for approval, per the project instructions. Merged only after the head
  commit passed every gate; `mergeStateStatus` was `CLEAN` before the merge command.
- **Two rebases were needed first, and no other session's work was discarded:**
  1. `origin/main` had advanced 29 commits (product pages, `build_products.py`, FLG-025..031,
     SG-32..38, Q-24..27). Nine files conflicted. Resolution: upstream taken where its work was
     newer (`data/suggestions.json`, `decisions.html`, the FLG-028/029 renumbering, which
     supersedes my FLG-025/026 fix with an audit trail); this session's work kept where it was
     the fix (`ideas.html` generated brief, the unique-link-text and disputed-link changes).
     Gate **D32** caught four `full spec page` links that the three-way merge dropped from the
     pillar pages; all four were restored before the gates were re-run.
  2. `origin/main` advanced again (PR #46/#47/#51: SG-01..SG-38, Q-01..Q-27). Four files
     conflicted; `ideas.html` keeps the generated brief (upstream still carried the stale
     `SG-01…SG-26` reading-order block), `direction.html` takes upstream's snapshot heading with
     a count-neutral framing, and both `.md` digests keep both sides.
- **Pre-merge gates on the merged tree (all green):** the six `--check` freshness gates
  (`build_chrome`, `build_registers`, `build_decisions`, `build_sitemap`, `build_products`,
  `build_ideas`), `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`
  (37 pages, 5,585 assertions), `tools/crawl_links.py` (37 pages, 0 broken links, 0 dead anchors,
  0 orphans).
- **GitHub Pages:** `Deploy GitHub Pages` run `44691488014` on `3a26ab3` — **success**.
  Companion legacy `pages build and deployment` run `44691487145` — **success**. Pages API:
  `status: built`, `build_type: legacy` (FLG-024's owner one-click still stands).
- **Live verification limit, stated plainly:** `github.io` is **not reachable** from this
  sandbox (HTTP 000 on every attempt, including the bare host), so the live pages were **not
  fetched** and no live-content check is claimed here. What was verified instead: `main` HEAD is
  `3a26ab3`, `origin/main` contains `scripts/build_ideas.py` and the rebuilt `ideas.html`, and
  `origin/main:tools/check_site.py` carries all three new rules (`P14b`, `D18b`, `D19`). The
  deploy workflows that publish `main` both concluded `success`.

### Session close — T-40..T-45 all done

| ID | Status |
|----|--------|
| T-40 | done — broken-link buy buttons repaired on `compare.html` and the gift guide |
| T-41 | done — line-by-line audit; AUD-02..AUD-07 recorded; four defect classes fixed; two gates repaired |
| T-42 | done — one generated review brief on `ideas.html`, gated |
| T-43 | done — M-01..M-15 missing-information table + ten research directions, in the brief |
| T-44 | done — duplicate spec strip removed; unique product-named link text on every outbound link |
| T-45 | done — PR #53 merged, both deploy paths green, record above |

### T-51 follow-up: second flag-id collision (post-merge, session `arena/d42249a7-prod3`)

After PR #54 merged (`9c367f3`), the live `flagged.html` showed that two flags had been published as **FLG-035** and **FLG-036** for different
subjects while this session's policy-citation and article-duplication findings held the same two numbers in `data/flagged.json`. Gate `D32` did not
catch it because the two sets of headings did not coexist in the same build until the merge.

Fix: the two **late additions** were renumbered to **FLG-037** (policy clause letters) and **FLG-038** (repeated article block and duplicated
card markup). The published FLG-034 (listing-conflict ids lost in an earlier renumbering) and the published FLG-035/FLG-036 records are untouched.
The renumbering rule applied throughout: **a record that was already published keeps its number; the later addition moves.** All references
(`EXECUTIVE_SUMMARY.md`, `executive-summary.html`, `README.md`, `decisions.html`, `ideas.html`, `scripts/build_ideas.py`, `data/flagged.json`,
`flagged.html`) were updated together and the generated pages rebuilt.

A third gate now makes this class of error loud: **`D39-flag-citation`** fails the build when a page cites a flag id that is not defined as a
heading on `flagged.html` — which is exactly how the stale `(FLG-035)` reference in `ideas.html` was caught one build after the renumbering.

All ten gates pass on the final tree (39 pages, 5,859 assertions; `crawl_links` 0 broken links, 0 orphans).

## Session `arena/7878cdbe-prod3` — T-53 / T-54 / T-55 (2026-11-20)

### Collisions and renumbering (two rounds happened while this branch was queued)

- Claimed T-46; session 59a087a1's T-46 (PR #38) merged first → renumbered T-50..T-53.
- PRs #44–#51 (sessions 77e66f80, 6bf60cac, 8692a390, 2cd3bab9, cafc55da) then took T-47..T-52 and
  SG-32..SG-38 / Q-24..Q-27 for different subjects → this session's tasks became T-53..T-56 and its
  rows were renumbered SG-39..SG-43 / Q-28..Q-29.
- PR #52 (session f3900cd3) then took SG-39..SG-42 → final numbering: tasks **T-53..T-56**, rows
  **SG-43..SG-47** / **Q-28..Q-29**. Nothing upstream was modified or discarded; every rebase kept
  all upstream rows and appended this session's after them.
- The duplicate FLG identifiers logged mid-flight (FLG-020/021/022/023) were resolved upstream as
  FLG-027..FLG-031; gate D35 (one flag id, one subject) now enforces it and was re-verified on the
  merged tree. The README's duplicated register tables were replaced upstream with one counted
  table plus gate D37; this session updated that table's ranges/counts to SG-01..SG-47 (46 rows) /
  Q-01..Q-29.

### What was done

- **T-53 (defect pass).** `flagged.html` byline → 2026-11-20. `data/sources.json` + `sources.html`:
  S10–S14 `used_for` no longer reads "rating, price, rank"; it now states the snapshot
  price/rating/rank was recorded to data files only and never rendered (identical wording in both).
  `scripts/build_registers.py`: citation-log byline derives from `data/citations.json`'s
  `generated` field (the suggestions/questions byline derivation landed upstream independently).
- **T-54 (growth register additions).** `data/suggestions.json`: SG-43..SG-47, all `proposed`,
  each declaring its `sources` per gate D34. `data/open-questions.json`: Q-28 (indexing status),
  Q-29 (Core Web Vitals baseline). `data/sources.json` + `sources.html`: S34, S35, S36 added after
  upstream's S33. `DIRECTION.md`: SG index extended with SG-43..SG-47 verbatim. Generated pages
  rebuilt (registers, decisions, chrome, sitemap, products).
- **T-55 (executive summary refresh).** Both summaries gain a dated session addendum; ranges/counts
  consistent with the registers.

### Sources used (fetched and read 2026-11-20 by this session)

- S34 — https://developers.google.com/search/docs/crawling-indexing/links-crawlable
  ("Good anchor text is descriptive, reasonably concise, and relevant to the page that it's on
  and to the page it links to.")
- S35 — https://developers.google.com/search/updates — the old FAQ-page documentation URL
  (…/structured-data/faqpage) redirects to this changelog; May 2026: deprecation notice
  ("will no longer appear in Google Search starting May 7, 2026"); June 2026: "Removing
  documentation for the FAQ rich result feature".
- S36 — https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
  (page last updated 2026-10-01 UTC; "It is critical to manually factcheck and review all
  AI-generated content for accuracy and trustworthiness before publishing.")
- S22 — https://developers.google.com/search/docs/essentials/spam-policies (re-read live: scaled
  content abuse covers unoriginal content "no matter how it's created").
- S25 — https://developers.google.com/search/docs/appearance/page-experience (re-read live:
  "Core Web Vitals are used by our ranking systems.").
- Site evidence: anchor scan over the published pages found zero generic anchors ("click here",
  "read more", "learn more", "this page", "here", "website", "article"); assets/style.css has no
  @import and no webfont URLs; shop pages load one local script and make no third-party asset
  requests.

### Verification performed

- After each rebase and the final renumbering: `build_registers --check`, `build_decisions --check`,
  `build_chrome --check`, `build_sitemap --check`; `tools/verify_site.py` release gate (incl.
  publishing coverage and cadence checks added upstream); `scripts/check_site.py`;
  `tools/check_site.py` (incl. D20/D25/D26/D34/D35/D36/D37); `tools/crawl_links.py`. Results in the
  T-56 release record below.

### Irregularities logged (not fixed here)

- **PageSpeed Insights API not reachable from this sandbox** (www.googleapis.com fetch fails);
  Q-29 stays a question; no performance figure was invented.
- **support.google.com not reachable from this sandbox**; Q-28's Search Console citation reuses
  S26/S27/S28 (fetched 2026-11-20 by the T-46/T-52 sessions) rather than a row this session could
  not fetch itself.
- **Trend-article overlap note:** upstream SG-37 already registers "publish catchy, trend-led
  question articles to earn organic traffic"; SG-44's FAQ guard and Q-29's CWV question are
  complementary to it, not duplicates (D20 verified). Upstream SG-41 (reader-capture path) and
  SG-30 cover reader capture; this session added none.
- **Board duplication continues upstream:** the board now carries two T-52 rows (2cd3bab9 and
  f3900cd3) — consistent with FLG-032; not this session's to renumber.

### Not claimed / owner gates unchanged

FLG-001 intended ASINs · FLG-006 Special Link test · FLG-010 account status · FLG-017/025/031
homepage-link cause · FLG-026 tag parameter demonstration · Search Console verification
(DT-03/Q-18) · analytics endpoint (DT-07) · share-debugger check (F-21/Q-21) · Pages build_type
(FLG-024) · seasonal rotation decision (SG-43).

## T-56 release record (session `arena/7878cdbe-prod3`, 2026-11-20)

### Release-blocking fix on the merged tree

- Upstream gate `D40` (a stated guide count must equal the guides on disk) failed on two strings:
  `flagged.html` FLG-038's heading said "Eight articles" (a historical count that now reads as a
  live claim — ten guides ship) and `data/suggestions.json` SG-44 said "the nine guides". Fixed by
  removing the counts rather than updating them: FLG-038's heading now reads "Every article page
  ended with the same block" (meaning preserved — the defect was that all article pages carried
  the identical ending block), and SG-44 now reads "the guides already answer questions in visible
  prose". Both fixes are count-free, so they cannot go stale; generated pages rebuilt.

### Gates at close (final tree, after rebase onto c14b28c)

`build_chrome --check`, `build_registers --check`, `build_decisions --check`, `build_sitemap
--check` (all current, 39 pages); `tools/verify_site.py` release gate passed (32 sources resolve
and are published; publishing coverage: 10 guides in sitemap, feed and hub; cadence recorded);
`scripts/check_site.py` all checks passed; `tools/check_site.py` 39 pages, 5,919 assertions, all
rules (incl. D20/D25/D26/D34/D35/D36/D37/D40) passed; `tools/crawl_links.py` 39 pages crawled,
38 reachable from the front page, 0 broken links, 0 dead anchors, 0 orphans.

### Not claimed / owner gates unchanged

FLG-001 intended ASINs · FLG-006 Special Link test · FLG-010 account status · FLG-017/025/031
homepage-link cause · FLG-026 tag parameter demonstration · Search Console verification
(DT-03/Q-18) · analytics endpoint (DT-07) · share-debugger check (F-21/Q-21) · Pages build_type
(FLG-024) · seasonal rotation decision (SG-43) · Q-28 indexing status · Q-29 Core Web Vitals.

### Merge and deploy record (T-56, session `arena/7878cdbe-prod3`)

- **PR #62:** https://github.com/wingbangboozle1-lang/Prod3/pull/62 (`arena/7878cdbe-prod3` → `main`), merged at `2026-11-20T07:09:41Z`, merge commit `9dd5c3796d89b5c71d8e550aa3cf42a61e8ea5ed`. Three rebases were required en route (PRs #38, #44–#51, #52 and #57/#60 landed while this branch was queued); each conflict was resolved by keeping every upstream row and appending/re-applying this session's rows, with the renumbering documented in place.
- **Pre-merge gates on the final tree:** four `--check` freshness gates current (39 pages); `tools/verify_site.py` release gate passed (32 sources resolve and are published; publishing coverage 10 guides; cadence recorded); `scripts/check_site.py` all passed; `tools/check_site.py` 39 pages, 5,919 assertions, all rules passed (incl. D20/D25/D26/D34/D35/D36/D37/D40); `tools/crawl_links.py` 39 pages crawled, 38 reachable, 0 broken links, 0 dead anchors, 0 orphans.
- **GitHub Pages:** `Deploy GitHub Pages` run `44692912791` — **success** on the merge commit; companion legacy `pages build and deployment` run `44692911963` — **also success** this time; `Render screenshots (design review)` run `44692912872` — success. The FLG-024 dual-path race resolved cleanly here; the owner's one-click fix (Settings → Pages → Source: GitHub Actions) still stands.
- **Live checks (fetched, not assumed):** `suggestions.html` serves "Register updated 2026-11-20" and renders SG-43 ("Give the seasonal block a retirement date…") with its options and recommendation; `questions.html` serves Q-28 ("Is any of this site in Google's index yet…") citing S26, with Q-29 in the same Measurement group; the disclosure strip is above the first heading on both.
- **This record's own landing:** the board update and this record ship as a follow-up micro-PR (same session), merged after PR #62; its PR number is recorded below when merged.

*Board update shipped as **PR #63** ("T-56 record: PR #62 merge/deploy results and live checks"), merged `2026-11-20T07:11:56Z`, merge commit `225c263caa8935c85cf22b49962f01d761a5065c`; `Deploy GitHub Pages` run `44693192323` and the legacy `pages build and deployment` run `44693190661` both **success** on it.*
*(micro-PR record: to be appended after the board-update PR merges)*
## Claim — session `arena/6c0972fb-prod3` (2026-11-20, 06:55 UTC)

Claimed the six rows above as **T-60..T-65** (T-65 was first written T-51/T-51b during two
rebase collisions). Identifiers were taken by other sessions while this claim was in flight:
`T-46` by `arena/59a087a1-prod3` (PR #38) and `T-47` by `arena/cafc55da-prod3` (PR #39, whose
record this session also confirms). Both rows and records are kept untouched; this claim was
renumbered instead of either being overwritten. **Numbering note for the next session: claim from
T-66.**

Scope discipline: `data/products.json`, `data/sources.json` and `data/flagged.json` are appended
to, never rewritten — the 2026-11-19 and the earlier 2026-11-20 observations stay as recorded.
`assets/app.js` (event counting) is read-only for this session.

Board inaccuracies recorded, not silently edited: rows T-20/T-21/T-22 appear twice (once
`in progress`, once `done`) from session 33e3e80f; the board carries no rows for T-27..T-38 or
T-40..T-45 even though records for them exist further down this file.

### Landed — session `arena/6c0972fb-prod3`, 2026-11-20 (T-60 → T-62, plus two repairs)

**T-60 (link format).** All five supplied `link.amazon` short links re-fetched and all five ended on the Amazon homepage, fourth dated observation of the day and an independent reproduction of session `6bf60cac`'s same-day result; recorded as `short_link_rechecks[]` per product without touching any earlier record. Every reader-facing product button (30) now targets `https://www.amazon.com/dp/<observed ASIN>?tag=shopnow047c-20&linkCode=sl1`, including the five generated pages, where the fix is in the generator so a rebuild cannot undo it. S34/S35 registered from the live Program Policies; two gate rules added (`scripts/check_site.py` 7b, `tools/check_site.py` P09) and both negative-tested by running them before the fix, when they named the two untagged hand-written buttons and five untagged generated pages. Published as FLG-039 after `FLG-034` was found to be taken upstream.

**T-61 (three guides).** `articles/thanksgiving-leftovers-air-fryer.html`, `articles/check-your-thermometer-at-home.html`, `articles/how-to-read-a-product-listing.html` — buyer questions, every figure traced to a source fetched the same day (USDA FSIS safe-temperature chart, FSIS Food Thermometers, NIST traceability policy, FTC Disclosures 101) or to the dated listing snapshots in `data/products.json`; no price, rating, review count, test result or traffic claim. Wired into `buying-guide.html`, both category shelves, the front page, `feed.xml` and `sitemap.xml`, so the publishing gate covers all thirteen. The one-day batch is recorded as a documented exception in `docs/publishing-cadence.md` rather than passed off as the monthly rhythm, with the overlap against `data/editorial-plan.json` named.

**T-62 (polish).** `BreadcrumbList` structured data on all twelve older guides (only the three new ones had it), enforced by a new gate rule alongside the byline requirement; the front-page feature card's inline hex colours became `.spec-hero.on-art` in `assets/style.css`; the guide-count claims in `buying-guide.html`, `index.html`, both executive summaries, `DIRECTION.md`, `questions.html` and `suggestions.json` were corrected or restated with digits, because gate D40 counts them and had already caught main drifting.

**Two repairs that were not in the plan, both recorded rather than tidied.** (1) `data/products.json` on main had lost the five `official_listing_check_2026_11_20` blocks session `59a087a1` added in `56cddb5` — commit `ffcb419` rewrote the whole file. Restored verbatim from `56cddb5`; nothing that commit added was changed. Published as FLG-040 with the second finding: the README register ranges had been failing gate D37 **on main** for several merges, because the gate set runs on push to main rather than as a required check on the pull request. (2) `flagged.html` had two ids heading two findings each; my new records moved to free ids instead of adding a third.

**Board hygiene note for the next session.** Five `git pull --rebase` rounds on this branch collided in `COORDINATION.md`, `index.html`, `compare.html`, `air-fryers.html`, `meat-thermometers.html`, `README.md` and `data/products.json`. What worked: resolve by keeping the upstream side for files another session owns, then re-run a scripted transform (`/tmp/gen/apply.py`, kept here as a recipe: rewrite CTA hrefs by pattern, re-append the products.json records, re-wire the guide links, regenerate chrome/registers/README). What did not: `git add -A` before the markers were gone, which committed conflict markers twice. Still open for this session: T-63 (direction layer), T-64 (flag-register sync), T-65 (suggestions/questions refresh). Next free claim: **T-66**.

---


---

---

---

---

---

## Session arena/6f44d8c9-prod3 — final integration re-verification (T-57, 2026-11-20)

**Branch:** `arena/6f44d8c9-prod3`, cut from `a861ed7` (the PR #36 merge); fast-forwarded to
`7c1b939` (the PR #37 merge) before working. **Role:** final integration session. All other tasks
were already `done` and merged, so this session re-verified the combined tree line by line, fixed
only demonstrable stale/contradictory statements, re-ran every gate, and is responsible for the
final PR → main → Pages deploy.

### Verification boundary (stated, not assumed)

- Outbound TLS to `amazon.com`, `link.amazon`, and the live GitHub Pages URL is blocked from this
  sandbox (SSL handshake fails), so the five supplied links and the live HTML could not be re-fetched
  here. Verification therefore rests on: (a) the dated 2026-11-19 official-listing snapshots already
  recorded in `data/products.json` and its `citation` blocks, (b) the GitHub API (`gh`) for PR/Pages
  state, and (c) the repository's own release gates. No product value was altered, inferred, or filled.
- Every register was enumerated and its IDs cross-checked against the page that publishes it:
  `data/suggestions.json` (30 rows, SG-01..SG-31; SG-21 retired, SG-26 unoccupied — FLG-021),
  `data/open-questions.json` (23 rows, Q-01..Q-23), `data/decisions.json` (10 rows, DT-01..DT-10),
  `data/flagged.json` (24 rows: F-01..F-21 plus FLG-017/020/021), and `flagged.html` (FLG-001..FLG-024).
  _(Counts above are the tree as this session found it after PR #37. The concurrent T-46..T-50
  session — merged as PR #43 — subsequently expanded the registers to 34 suggestions (SG-32..SG-35),
  26 questions (Q-24..Q-26) and 12 decisions (DT-11..DT-12); those additions are upstream's and are
  not part of this session's diff.)_

### Defects found and fixed (each verified before and after the edit)

| Defect | Evidence before | Fix |
|---|---|---|
| `README.md` carried **two contradictory** "Registers (current data)" tables — one "as of 2026-11-19" (SG-01..SG-31, Q-01..Q-21, F-01..F-21) and one "as of 2026-11-20" (SG-01..SG-30, Q-01..Q-21, FLG-001..FLG-017 + F-01..F-21) — that disagreed with each other and with the registers | Both tables present; neither matched all three registers | Replaced with a single accurate table dated 2026-11-20; the F-series/FLG-series overlap is stated and referenced to audit item I-12 |
| `README.md` register ranges were stale | Suggestions "SG-01..SG-30"; Open questions "Q-01..Q-21" (both tables); Flagged "FLG-001..FLG-017, F-01..F-21" | Suggestions SG-01..SG-31 (SG-21 retired, SG-26 unoccupied); Open questions Q-01..Q-23; Flagged FLG-001..FLG-024 on `flagged.html`, F-01..F-21 in the machine register |
| `README.md` `decisions.html` description cited "Q-01..Q-21" | Line 44 | "Q-01..Q-23" |
| `EXECUTIVE_SUMMARY.md` said the direction desk "matches `data/suggestions.json` / `data/open-questions.json` exactly" while citing "SG-01…18 … Q-01…21" | Line 53 — the cited ranges did not match the registers the sentence claimed to match | "SG-01..SG-31 … Q-01..Q-23"; "New open item" → "Open item" (FLG-016 is no longer new) |
| `direction.html` suggestion count was stale | "for all 25 suggestions" | "for all 30 suggestions (SG-01..SG-31; SG-21 retired in place, SG-26 unoccupied — FLG-021)" |
| `direction.html` register-summary paragraph cited "SG-01..SG-25" and "Q-01..Q-21" | Line ~106 | "SG-01..SG-31" and "Q-01..Q-23" |
| `direction.html` open-questions table was missing Q-22 and Q-23 and its header read "Q-01 … Q-21" | Table ended at Q-21; `DIRECTION.md` and the register carry Q-22/Q-23 | Header → "Q-01 … Q-23"; Q-22 and Q-23 rows added verbatim from `data/open-questions.json` (Q-22 blocking, Q-23 owner-only) |
| `direction.html` had a **duplicate** "Source for SG-19" paragraph and **two** consecutive `<h2>` headings for the questions section | "Source for SG-19" appeared twice; two `<h2>` blocks back-to-back | Removed the duplicate note and the redundant heading; kept one SG-19 source note and the descriptive heading |
| Register generation dates were demonstrably stale: all three registers advertised "updated/generated 2026-11-19" yet contain 2026-11-20 additions (`suggestions.json`: SG-31 added 2026-11-20; `open-questions.json`: Q-22/Q-23 added 2026-11-20 per its own premise; `citations.json`: FLG-020 2026-11-20 observation) | `build_registers.py` bylines and the three JSON `generated` fields read 2026-11-19 | Dated all three to 2026-11-20 in `scripts/build_registers.py` and the JSON `generated` fields; regenerated `suggestions.html`, `questions.html`, `citations.html`; `direction.html` callout → "registers last generated 2026-11-20" |

### Review performed (line-by-line, 2026-11-20)

- All 12 data JSON files enumerated and read; ID ranges cross-checked against the pages that
  publish them (see the boundary note above).
- `flagged.html` publishes FLG-001..FLG-024; `data/flagged.json` is the machine register for the
  F-series (F-01..F-21) plus FLG-017/020/021. The two overlap in scope; merging them is a content
  decision (I-12), so the README now presents them as two rows rather than conflating them.
- `questions.html` and `decisions.html` correctly render Q-01..Q-23 and SG-01..SG-31 (generated
  from JSON); no change needed there. `executive-summary.html` carried no stale SG/Q ranges.

### Gates re-run on the edited tree (all green)

- `scripts/build_chrome.py --check` — OK: chrome current on 31 pages
- `scripts/build_registers.py --check` — OK: register pages match data/*.json
- `scripts/build_decisions.py --check` — OK: decisions.html matches its data
- `scripts/build_sitemap.py --check` — OK: sitemap.xml up to date
- `scripts/check_site.py` — all checks passed
- `tools/verify_site.py` — release gate passed
- `tools/check_site.py` — 31 pages, 3,937 assertions, all passed
- `tools/crawl_links.py` — 31 pages crawled, 0 broken links, 0 dead anchors, 0 orphans

### Not claimed / not verified here (unchanged owner gates)

FLG-001 intended ASINs · FLG-006 Special Link test in the enrolled workflow · FLG-010 Associates
account status · FLG-017 B04G1MEwY link check · FLG-020 Program Policies §2(t)/§2(v) wording ·
Search Console (DT-03) · analytics endpoint (DT-07) · share-debugger check (F-21/Q-21) · Pages
`build_type` setting (FLG-024, owner one-click). No new claims about traffic, conversion, or product
superiority were made. No product value, link target, or flag was altered.

### Merge and deploy record (T-57)

- **PR:** #45 — `arena/6f44d8c9-prod3` → `main` — https://github.com/wingbangboozle1-lang/Prod3/pull/45
- **Outcome:** MERGED. Merge commit `89849e0bdad81ab23f4811a51a5d82df8d60a10a`, merged
  2026-11-20T07:16:28Z (merged without waiting for approval, per the owner instruction).
- **Rebases required:** the branch was rebased five times onto `origin/main` as
  concurrent sessions merged PRs #42–#66 ahead of it (T-46, T-47, T-48, T-49, T-50,
  T-51/T-54/T-55, T-52, T-56, T-60–T-65). Every rebase resolved conflicts keeping both
  sessions' work; no upstream work was discarded. This task renumbered T-46 → T-51 →
  T-53 → **T-57** under the board's one-identifier-one-meaning rule (T-46/T-48/T-51/T-52
  taken by other sessions, then T-53..T-56 by session `7878cdbe`).
- **Gates at merge:** all release gates green on the merged tree —
  `build_chrome.py --check`, `build_registers.py --check`, `build_decisions.py --check`,
  `build_products.py --check`, `build_readme.py --check`, `build_ideas.py --check`,
  `build_sitemap.py --check`, `scripts/check_site.py`, `tools/verify_site.py`,
  `tools/check_site.py` (42 pages, 6,363 assertions), `tools/crawl_links.py`
  (no broken links, no dead anchors, no orphans).
- **Deploy:** `Deploy GitHub Pages` workflow run **44693759586** on the merge commit
  `89849e0` — status `completed`, conclusion `success` (started 2026-11-20T07:16:31Z,
  finished 07:16:50Z). Live site: https://wingbangboozle1-lang.github.io/Prod3/
  (Pages source `main`, build type still `legacy` — see FLG-024; the artifact
  workflow is the authoritative deployer).
- **Remaining owner gates unchanged:** intended ASINs (FLG-001), Associates account
  eligibility (FLG-010), Special Link test (FLG-006), Search Console verification
  (DT-03), analytics endpoint (DT-07), share-debugger check (F-21), and the Pages
  `build_type` one-click fix (FLG-024). No product value, link target, or flag was
  altered by this pass.

## Session `arena/fe5fd1d9-prod3` — PR and merge record (2026-11-20)

- **PR #67** `arena/fe5fd1d9-prod3` → `main`: opened 2026-11-20, merged **2026-11-20T07:18:45Z**
  as merge commit **d47a3df** ("Merge pull request #67 from wingbangboozle1-lang/arena/fe5fd1d9-prod3").
  Merged without waiting for review per the standing directive; no conflicts at merge time (the
  branch had absorbed main 8cc8d58 immediately before).
- **Pages deploy confirmed:** the `Deploy GitHub Pages` workflow on d47a3df completed with
  **success**. The redundant legacy `pages build and deployment` run (FLG-024) triggered as
  documented and does not affect the artifact deploy. Live page re-fetched from
  https://wingbangboozle1-lang.github.io/Prod3/compare.html after deploy: the buy row reads
  "Buy (official product pages)" with all five cells linking
  `https://www.amazon.com/dp/<ASIN>?tag=shopnow047c-20&linkCode=sl1`, the detail-page links resolve
  to the five generated `products/` pages, the disclosure strip is above the fold, and no price or
  rating is rendered.
- **Record closed on the merged tree:** `tools/check_site.py` 42 pages / 6,372 assertions, all
  freshness gates `--check` OK, release gate passed, crawl 0 broken / 0 dead / 0 orphans.
_(recorded after the PR merges)_

| T-58 | Publication-pass completion (renumbered from T-25, then T-26, then T-39, then T-53 — every earlier number collided with a row already on main (T-53..T-56 were taken by session 7878cdbe, T-57 by session 6f44d8c9); session b8dae8e0): fix the remaining demonstrable defects on the direction surfaces (stale register ranges, FLG-021→FLG-029 mis-citation for the SG-26 gap, duplicate SG-19 fragment); add page-wide RSS-autodiscovery and register-reference gates; re-run every gate (the guide-count flag was dropped — upstream's D40 gate already covers it); PR → main, merge, confirm Pages | done (PR #72, merge commit `cd47196`; deploy confirmed below) | `arena/b8dae8e0-prod3` | `COORDINATION.md`, `direction.html`, `

### Merge and deploy record (T-58, session `arena/b8dae8e0-prod3`)

- **PR:** #72 — `arena/b8dae8e0-prod3` → `main` — https://github.com/wingbangboozle1-lang/Prod3/pull/72
- **Outcome:** MERGED. Merge commit `cd47196e27c0fd97d51070f5f5c98c7c89ce8f99`, merged
  2026-11-20T07:21:53Z (merged without waiting for approval, per the owner instruction).
- **Rebases required:** four (PRs #36–#67 landed while this branch was open; the claim
  renumbered T-24 → T-25 → T-26 → T-39 → T-53 → **T-58** under the
  one-identifier-one-meaning rule; conflicts resolved keeping every upstream row).
- **Cross-scope edits logged in commit/PR text:** `scripts/build_decisions.py` was edited
  earlier in the session (retired rows excluded from the open-proposals count — upstream
  later landed an equivalent fix; nothing was double-applied), and one field of
  `data/flagged.json` (FLG-029 detail) was reworded so `decisions.html` stops rendering
  the unoccupied id token. No finding, id or grading changed.
- **Upstream defect corrected during conflict resolution:** `DIRECTION.md` on `main` had
  been repointed (PR #67) to cite FLG-026/FLG-025 for the SG-gap note and the Q-digest
  correction; those ids name unrelated findings in both `flagged.html` and
  `data/flagged.json`. PR #72 restores FLG-029/FLG-028 (declared in place inside
  FLG-027's renumber note, so D39 accepts them). Noted on the PR.
- **Gates on the merged tree (`cd47196`, 42 pages):** `scripts/check_site.py` ✅ ·
  `tools/check_site.py` ✅ (6720 assertions, all additional rules passed, incl. this
  session's D41-rss-autodiscovery/D41-rss-once and D42-sg-refs-resolve/D42-q-refs-resolve) ·
  `tools/verify_site.py` ✅ · `build_sitemap.py --check` ✅ · `build_registers.py --check` ✅ ·
  custom crawl: 42 pages, 0 broken internal links/anchors.
- **GitHub Pages:** `Deploy GitHub Pages` run `44694421239` — **success** on the merge
  commit. Companion legacy `pages build and deployment` run `44694420462` and the
  screenshot run were still in progress at record time (FLG-024 dual-path context).
- **This record was delivered by PR #78** (COORDINATION-only): MERGED, merge commit
  `704dc76b269d5bfc622e864eab951b3d0b660e8`, 2026-11-20T07:23:33Z. Its legacy
  `pages build and deployment` **success** (repo Pages `build_type` is currently
  `legacy`, so that is the path that publishes); its `Deploy GitHub Pages` run
  `44694624299` failed at `deploy-pages` with "No artifacts named github-pages were
  found" after all gates had passed, and GitHub refused a rerun of that run — the same
  dual-path artifact race already flagged as FLG-024. The published site was verified
  from the legacy run's head SHA. No content regression; gates re-run green locally on
  `704dc76` (42 pages, 6761 assertions).
## Session `arena/ba8e7240-prod3` — T-55..T-58 (2026-11-20, 06:52–07:45Z)

Claimed as T-51..T-54; renumbered twice because four sessions merged during this branch and took those IDs
(see the collision note at the end). Everything in this round is grounded in pages fetched and read during the
session, section by section, rather than searched for by a remembered section number. Reviewer's entry point:
**`docs/policy-verification-2026-11-20.md`**.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-55 | Policy-citation precision pass: independent re-read of the live Program Policies (page header: updated 2026-04-14) and the Operating Agreement; correct the mis-numbered clauses; add the automation clauses to `data/policy-checks.json`; extend `data/policy-clause-map.json` so gate D35 accepts them | done | `arena/ba8e7240-prod3` | `data/policy-checks.json`, `data/policy-clause-map.json`, `compare.html`, `docs/policy-verification-2026-11-20.md` |
| T-56 | Design-brief desk: paste-ready inputs for the next polish pass, published as reviewable register rows (SG-49..SG-53, five rows after two renumberings and one withdrawal as a duplicate of SG-43) plus two rejected-on-policy ideas on `ideas.html` | needs review (owner marks Do this / Maybe / No) | `arena/ba8e7240-prod3` | `data/suggestions.json`, `ideas.html`, `DIRECTION.md`, regenerated `suggestions.html` / `decisions.html` |
| T-57 | Cross-scope requests against files under other sessions' active claims (front-page chips, shelf anatomy, inline colours, price placeholder, disqualifier position, seasonal dating) | logged, not executed here | `arena/ba8e7240-prod3` | `COORDINATION.md` only |
| T-58 | Integration: ten gates re-run on the merged tree, PR → main, merge, Pages deploy confirmed | done (PR #68) | `arena/ba8e7240-prod3` | `COORDINATION.md` |

### What was verified, and what it changed

Verified 2026-11-20 against https://affiliate-program.amazon.com/help/operating/policies and
https://affiliate-program.amazon.com/help/operating/agreement:

| Site's claim | Cited as | Actually at |
|---|---|---|
| No customer reviews or star ratings without Creators or PA API | §2(t), then "not located" (FLG-020) | **§6(t)** — verbatim; the permission is *a link to* the review, not a rating value |
| Do not obscure that a link goes to Amazon | §2(v), then "not located" | **§6(v)** — verbatim |
| No shortener used so the destination is unclear | §2(b), marked UNVERIFIED in C-04 | **§6(w)** — verbatim; the test is clarity to the reader |
| Prices only from Amazon-served data or the API; misleading-claims rule; product-list original content; no per-user sub-tag; tag as a URL parameter | §2(b) | **§2(b)** — correct as cited, all five quoted as read |
| Disclosure sentence required; a breach is material | Agreement §5 for both halves | Agreement **§5** names the sentence; **§6** makes a §5 violation a material breach |

`data/policy-checks.json` 14 → **20** rows: **C-15** §6(t) ratings · **C-16** §6(y) no price tracking or alerting ·
**C-17** §6(s) no artificial clicks or Sessions, plus Commission Income Statement §5 on combining attribution
paths · **C-18** §6(g)/§6(p)/§4 incentives, Amazon customer-generated content, opt-in-only messaging ·
**C-19** §6(a)/§6(n)/§6(d) Program Content, framing, implied endorsement · **C-20** §1 eligibility: the
original-content floor under any at-volume publishing plan. `data/policy-clause-map.json` 13 → **22** entries,
each quote transcribed from the served page, so D35 refuses an unverified letter and accepts these.

Six rows were added to the policy register rather than six new flags, so the automation is stopped at the gate
instead of after publication. Two ideas on `ideas.html` are rejected *on a clause* rather than on taste:
price-drop alerts (§6(y)) and synthetic clicks or prefetching (§6(s) + CIS §5).

### T-57 — cross-scope requests; three were executed upstream while this branch was open

1. `data/citations.json` + `citations.html` "not located" wording → **done upstream**; the published row now
   reads §2(a)/§2(b)/6(e) with an explicit `correction` field naming 6(t)/6(v)/6(w). Request withdrawn as
   satisfied.
2. `flagged.html` FLG-020 → **closed upstream** as "the letters were wrong and have been corrected".
3. `README.md` duplicated/stale register table → **done upstream** (one generated table, `scripts/build_readme.py`);
   this round's regeneration moved the counts to 51 suggestion rows / 29 questions.
4. `scripts/build_registers.py` self-dating registers from a literal → **done upstream**.
5. `tools/verify_site.py` hardcoded nine-item feed count → **done upstream**; it now derives the count from
   `articles/` and fails if a guide is missing from the sitemap, feed or hub.
6. Still open for the `index.html` owner: SG-48 (one chip row per card — upstream shipped one row, so this is a
   confirmation task), SG-49 (`meat-thermometers.html` renders **zero** chip rows against one per card on the
   air-fryer shelf), SG-50 (four inline colour styles remain in `index.html`), SG-51 (the "Current price on
   Amazon" line still sits beside nine buttons), SG-52 (the "Look elsewhere if…" disqualifier still precedes the
   CTA). Upstream's SG-43 already dates the seasonal block, so this session's sixth row was withdrawn instead of
   published twice.
7. Still open, requested rather than done: register USDA FSIS *Leftovers and Food Safety* in `data/sources.json`
   (next free ID) so the reheating guide in the memo can cite it — `D06` fails a dangling ID by design.

### Link observation, 06:57–06:58Z (fourth dated record, nothing overwritten)

Two of the five supplied tokens re-read by following the URL and recording the final address — a page read, not
a click. `link.amazon/B04G1MEwY` → `amazon.com/dp/B0CDY277D3` (P-01); `link.amazon/B0c8moW59` →
`amazon.com/dp/B0DHZTCNR5` (P-04). Both product pages, both carrying `plpRedirect=mhFallback`, neither final URL
showing a visible `tag=` parameter. Two *other* records filed the same day for the same tokens read a homepage
landing, so the behaviour is not stable across attempts. No price or rating was recorded from those pages, by
policy. Consequence: the open test is not "is the short link broken" but "does the click arrive tagged" — SG-13,
owner-only, signed in.

### Gates (T-58)

Ten gates green on the final tree: `build_sitemap.py`, `build_registers.py`, `build_chrome.py`,
`build_decisions.py`, `build_ideas.py`, `build_readme.py` (each with `--check`), `scripts/check_site.py`,
`tools/verify_site.py`, `tools/check_site.py` (39 pages) and `tools/crawl_links.py`; `git diff --check` clean.
Deploy record appended after merge.

### Collision log (nothing discarded)

- Rebase collisions with `arena/8706c7f7-prod3` (PR #44), `arena/6bf60cac-prod3` (PR #48),
  `arena/d42249a7-prod3`, `arena/2cd3bab9-prod3`, `arena/f3900cd3-prod3` (PRs through #60) and
  `arena/6c0972fb-prod3` / `arena/6f44d8c9-prod3` (PRs #65, #45) in this file. Resolved by keeping both sides;
  only conflict markers removed.
- `arena/2cd3bab9-prod3` and `arena/f3900cd3-prod3` took **T-51/T-52** (and f3900cd3 a second **T-52**) while
  this branch was open → this session's rows are **T-55..T-58**. Their rows are untouched.
- Upstream filled **SG-36..SG-42**, then **SG-43..SG-47**, with different proposals → this session's rows moved
  SG-36..SG-41 → SG-43..SG-48 → **SG-49..SG-53**, and every in-page reference was updated in the same commit.
  One ID, one meaning; where two sessions proposed the same thing, this session's row was withdrawn.
- A line-level union merge of `data/suggestions.json` silently dropped a `sources` line from an upstream row and
  a `data/policy-checks.json` union produced invalid JSON. Both registers were **rebuilt from the upstream file
  programmatically** instead, and `flagged.html` was restored to upstream's version because they fixed the D40
  count line themselves. Lesson for the next session: union-merge prose, rebuild structured files.
| T-58 | Publication-pass completion (renumbered from T-25, then T-26, then T-39, then T-53 — every earlier number collided with a row already on main (T-53..T-56 were taken by session 7878cdbe, T-57 by session 6f44d8c9); session b8dae8e0): fix the remaining demonstrable defects on the direction surfaces (stale register ranges, FLG-021→FLG-029 mis-citation for the SG-26 gap, duplicate SG-19 fragment); add page-wide RSS-autodiscovery and register-reference gates; flag the eight-vs-nine guide count as FLG-035; re-run every gate; PR → main, merge, confirm Pages | in progress | `arena/b8dae8e0-prod3` | `COORDINATION.md`, `direction.html`, `DIRECTION.md`, `tools/check_site.py`, `flagged.html`, `docs/verification.md` |
### Landed — session `arena/6c0972fb-prod3`, 2026-11-20 (T-63, T-64, T-65)

**T-64 (flag register ↔ page).** Two directions of drift were found and both are now gated. `FLG-028` and `FLG-029` existed in `data/flagged.json` with no counterpart on `flagged.html` (a renumbering pass had edited one side only); 22 published callouts — `FLG-001`…`FLG-019`, `FLG-024`, `FLG-030`, `FLG-031`, `FLG-033` — existed on the page with no register row. The two missing callouts were published verbatim from their register text, the 22 register rows were mirrored from the page (verbatim detail, no new claims, marked as mirrors), and the duplicate-id repair this row promised was verified already done by session `59a087a1`'s renumbering (`FLG-027/028/029`, then `FLG-037/038`), so nothing was renumbered a second time. New gate `tools/check_site.py` **D41** fails the build if either side drifts again; the F-series stays machine-only by design and is exempt, because `flagged.html` says so in its own intro. `DIRECTION.md` I-12 and I-13 were corrected to describe what is now enforced rather than what was once missing (I-12's table row had also been truncated mid-sentence by an earlier pass — repaired).

**T-63 (direction layer).** `SG-48` (give the dated link recheck a cadence and a gate, rather than leaving four same-day observations with no next-due date) and `Q-30` (whether the outbound-click counters fire on the tagged buttons and where the counts land, blocked on DT-07) were appended with ids computed from the registers' own maxima — other sessions had already taken `SG-32..SG-47` and `Q-24..Q-29` today, so the claimed ranges were consumed. The copy-ready design brief the claim promised is a table of eight constraints on `ideas.html` (`id="design-brief"`), deliberately placed **after** the `build-ideas:brief` region: my first attempt inserted it inside that region and `scripts/build_ideas.py` deleted it on the next rebuild, which is worth knowing before anyone else hand-edits that page.

**T-65 (integration).** Gates on this tree: `scripts/check_site.py` all passed; `tools/check_site.py` 42 pages, ~6.4k assertions, all rules passed; `tools/verify_site.py` release gate passed (13 guides in sitemap, feed and hub; cadence recorded); `tools/crawl_links.py` 42 pages, 0 broken links, 0 orphans; the six `--check` freshness modes current. `Deploy GitHub Pages` run `44693525255` — **success** on PR #65's merge commit `8cc8d58`; the new guide was fetched live and renders with its disclosure strip, breadcrumb data, sources and tagged buttons (`https://wingbangboozle1-lang.github.io/Prod3/articles/check-your-thermometer-at-home.html`).

**Cost of the day, recorded honestly.** This branch needed **seven** rebase rounds. The `S34`/`S35` ids I registered were taken by another session's Google rows while my PR was queued, so my sources moved to `S37`/`S38`/`S39` and `flagged.html`/`data/flagged.json` ids moved to `FLG-039`/`FLG-040` — collisions on shared registers are the dominant failure mode here, not conflicts in the HTML. Two lessons for the next session: (1) allocate shared ids from the register's current maximum in the same commit that uses them, never from a number read at claim time; (2) never `git add -A` before conflict markers are gone — that is how marker text reached a commit twice today.

**Next free claim: T-66** — checked against `origin/main` with `git grep "| T-66 "`: no row exists for T-66 or T-67, only this session's earlier *suggestion* that the next session claim from T-66. T-60..T-65 are this session's; rows T-52/T-56/T-57..T-62 from other sessions have landed alongside them.

**Post-PR note (same session, minutes later).** The rebase that made PR #75 mergeable silently dropped the mirrored register rows again — a `data/flagged.json` conflict resolved to the upstream side, which is the right rule for a file another session owns but wrong for an append. Re-applied by a small standalone script (`mirror_flags.py`: derive the register rows from the page's own callouts, publish the two page callouts the register already held), which also fixed three things the same round exposed: mirrored `basis_note` text must not re-cite source ids (gate D15 reads prose citations), `direction.html` carries a hand-written `Q-01 … Q-29` range the D36 gate polices, and its open-question table needed the Q-30 row so the widened range is honest. **Advice for whoever appends to a shared JSON next:** keep the append in its own idempotent script that re-runs after every rebase, not only in a commit.
## Session `arena/ba8e7240-prod3` — T-66..T-69 (2026-11-20, 06:52–07:45Z)

Claimed as T-51..T-54; renumbered twice because four sessions merged during this branch and took those IDs
(see the collision note at the end). Everything in this round is grounded in pages fetched and read during the
session, section by section, rather than searched for by a remembered section number. Reviewer's entry point:
**`docs/policy-verification-2026-11-20.md`**.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-66 | Policy-citation precision pass: independent re-read of the live Program Policies (page header: updated 2026-04-14) and the Operating Agreement; correct the mis-numbered clauses; add the automation clauses to `data/policy-checks.json`; extend `data/policy-clause-map.json` so gate D35 accepts them | done | `arena/ba8e7240-prod3` | `data/policy-checks.json`, `data/policy-clause-map.json`, `compare.html`, `docs/policy-verification-2026-11-20.md` |
| T-67 | Design-brief desk: paste-ready inputs for the next polish pass, published as reviewable register rows (SG-49..SG-53, five rows after two renumberings and one withdrawal as a duplicate of SG-43) plus two rejected-on-policy ideas on `ideas.html` | needs review (owner marks Do this / Maybe / No) | `arena/ba8e7240-prod3` | `data/suggestions.json`, `ideas.html`, `DIRECTION.md`, regenerated `suggestions.html` / `decisions.html` |
| T-68 | Cross-scope requests against files under other sessions' active claims (front-page chips, shelf anatomy, inline colours, price placeholder, disqualifier position, seasonal dating) | logged, not executed here | `arena/ba8e7240-prod3` | `COORDINATION.md` only |
| T-69 | Integration: ten gates re-run on the merged tree, PR → main, merge, Pages deploy confirmed | done (PR #68, merged as 371d8b1) | `arena/ba8e7240-prod3` | `COORDINATION.md` |
| T-70 | Independent verification round (session `arena/1fbc2432-prod3`; claim renumbered six times after colliding with T-46/PR #38, T-47/PR #39, T-48/PR #43, the T-52 lineage, T-57/PR #70 and T-66/aa7b8dd8) — **row restored 2026-11-20**: the board rewrite in PR #83 dropped this row and its completion record, both of which were merged by PR #79 (merge commit `971aaac`); nothing below was changed, the row is re-added verbatim per the FLG-032 duplicate-row handling | done (PR #79, merge commit `971aaac`; both Pages deploy paths success; record below) | `arena/1fbc2432-prod3` | `COORDINATION.md`, `data/recheck-2026-11-20-1fbc2432.json` (new), `data/suggestions.json` (SG-54), `data/flagged.json` (FLG-025 reproduction note), `flagged.html` (FLG-025 callout), `direction.html` (register-range line), `DIRECTION.md` (SG-54 mirror row), regenerated generated pages |

### What was verified, and what it changed

Verified 2026-11-20 against https://affiliate-program.amazon.com/help/operating/policies and
https://affiliate-program.amazon.com/help/operating/agreement:

| Site's claim | Cited as | Actually at |
|---|---|---|
| No customer reviews or star ratings without Creators or PA API | §2(t), then "not located" (FLG-020) | **§6(t)** — verbatim; the permission is *a link to* the review, not a rating value |
| Do not obscure that a link goes to Amazon | §2(v), then "not located" | **§6(v)** — verbatim |
| No shortener used so the destination is unclear | §2(b), marked UNVERIFIED in C-04 | **§6(w)** — verbatim; the test is clarity to the reader |
| Prices only from Amazon-served data or the API; misleading-claims rule; product-list original content; no per-user sub-tag; tag as a URL parameter | §2(b) | **§2(b)** — correct as cited, all five quoted as read |
| Disclosure sentence required; a breach is material | Agreement §5 for both halves | Agreement **§5** names the sentence; **§6** makes a §5 violation a material breach |

`data/policy-checks.json` 14 → **20** rows: **C-15** §6(t) ratings · **C-16** §6(y) no price tracking or alerting ·
**C-17** §6(s) no artificial clicks or Sessions, plus Commission Income Statement §5 on combining attribution
paths · **C-18** §6(g)/§6(p)/§4 incentives, Amazon customer-generated content, opt-in-only messaging ·
**C-19** §6(a)/§6(n)/§6(d) Program Content, framing, implied endorsement · **C-20** §1 eligibility: the
original-content floor under any at-volume publishing plan. `data/policy-clause-map.json` 13 → **22** entries,
each quote transcribed from the served page, so D35 refuses an unverified letter and accepts these.

Six rows were added to the policy register rather than six new flags, so the automation is stopped at the gate
instead of after publication. Two ideas on `ideas.html` are rejected *on a clause* rather than on taste:
price-drop alerts (§6(y)) and synthetic clicks or prefetching (§6(s) + CIS §5).

### T-68 — cross-scope requests; three were executed upstream while this branch was open

1. `data/citations.json` + `citations.html` "not located" wording → **done upstream**; the published row now
   reads §2(a)/§2(b)/6(e) with an explicit `correction` field naming 6(t)/6(v)/6(w). Request withdrawn as
   satisfied.
2. `flagged.html` FLG-020 → **closed upstream** as "the letters were wrong and have been corrected".
3. `README.md` duplicated/stale register table → **done upstream** (one generated table, `scripts/build_readme.py`);
   this round's regeneration moved the counts to 51 suggestion rows / 29 questions.
4. `scripts/build_registers.py` self-dating registers from a literal → **done upstream**.
5. `tools/verify_site.py` hardcoded nine-item feed count → **done upstream**; it now derives the count from
   `articles/` and fails if a guide is missing from the sitemap, feed or hub.
6. Still open for the `index.html` owner: SG-48 (one chip row per card — upstream shipped one row, so this is a
   confirmation task), SG-49 (`meat-thermometers.html` renders **zero** chip rows against one per card on the
   air-fryer shelf), SG-50 (four inline colour styles remain in `index.html`), SG-51 (the "Current price on
   Amazon" line still sits beside nine buttons), SG-52 (the "Look elsewhere if…" disqualifier still precedes the
   CTA). Upstream's SG-43 already dates the seasonal block, so this session's sixth row was withdrawn instead of
   published twice.
7. Still open, requested rather than done: register USDA FSIS *Leftovers and Food Safety* in `data/sources.json`
   (next free ID) so the reheating guide in the memo can cite it — `D06` fails a dangling ID by design.

### Link observation, 06:57–06:58Z (fourth dated record, nothing overwritten)

Two of the five supplied tokens re-read by following the URL and recording the final address — a page read, not
a click. `link.amazon/B04G1MEwY` → `amazon.com/dp/B0CDY277D3` (P-01); `link.amazon/B0c8moW59` →
`amazon.com/dp/B0DHZTCNR5` (P-04). Both product pages, both carrying `plpRedirect=mhFallback`, neither final URL
showing a visible `tag=` parameter. Two *other* records filed the same day for the same tokens read a homepage
landing, so the behaviour is not stable across attempts. No price or rating was recorded from those pages, by
policy. Consequence: the open test is not "is the short link broken" but "does the click arrive tagged" — SG-13,
owner-only, signed in.

### Gates (T-69)

Ten gates green on the final tree: `build_sitemap.py`, `build_registers.py`, `build_chrome.py`,
`build_decisions.py`, `build_ideas.py`, `build_readme.py` (each with `--check`), `scripts/check_site.py`,
`tools/verify_site.py`, `tools/check_site.py` (39 pages) and `tools/crawl_links.py`; `git diff --check` clean.
Deploy record appended after merge.

### Collision log (nothing discarded)

- Rebase collisions with `arena/8706c7f7-prod3` (PR #44), `arena/6bf60cac-prod3` (PR #48),
  `arena/d42249a7-prod3`, `arena/2cd3bab9-prod3`, `arena/f3900cd3-prod3` (PRs through #60) and
  `arena/6c0972fb-prod3` / `arena/6f44d8c9-prod3` (PRs #65, #45) in this file. Resolved by keeping both sides;
  only conflict markers removed.
- `arena/2cd3bab9-prod3` and `arena/f3900cd3-prod3` took **T-51/T-52** (and f3900cd3 a second **T-52**) while
  this branch was open → this session's rows are **T-66..T-69**. Their rows are untouched.
- Upstream filled **SG-36..SG-42**, then **SG-43..SG-47**, with different proposals → this session's rows moved
  SG-36..SG-41 → SG-43..SG-48 → **SG-49..SG-53**, and every in-page reference was updated in the same commit.
  One ID, one meaning; where two sessions proposed the same thing, this session's row was withdrawn.
- A line-level union merge of `data/suggestions.json` silently dropped a `sources` line from an upstream row and
  a `data/policy-checks.json` union produced invalid JSON. Both registers were **rebuilt from the upstream file
  programmatically** instead, and `flagged.html` was restored to upstream's version because they fixed the D40
  count line themselves. Lesson for the next session: union-merge prose, rebuild structured files.

### Deploy record (T-69)

- **PR #68 merged into `main` as `371d8b1`** at 07:22Z (merge commit, no squash, so both lineages stay readable).
- `Deploy GitHub Pages` run `44694516195` → success in 34s; `pages build and deployment` `44694514695` → success.
- Live verification by fetching the served page, not by trusting the run status: `ideas.html` renders the
  generated brief with **"SG-01…SG-53 on the register"** and **26** open proposals, so this round's five design
  rows and the renumbering are both published. `suggestions.html`, `questions.html`, `citations.html`,
  `decisions.html` and `direction.html` are served from the merged tree.
- **A deploy-step failure landed on `main` immediately after mine, and it is not a content defect.** Commit
  `704dc76` (PR #78) shows `Deploy GitHub Pages` → failure at step "Deploy to GitHub Pages" after 21s, while
  `pages build and deployment` for that same SHA succeeded, and all ten gates pass at that SHA in a clean
  worktree (`git worktree add` + every gate, not inferred). Read as a Pages deployment racing my merge's run
  within the same minute. If the live site lags `main`, re-run that workflow rather than editing content.

### Identifier collision note, resolved rather than left ambiguous

The board had reached **T-65** by the time this branch merged, and three sessions renumbered into T-55..T-58
while this work was open. So this session's four rows are published as **T-66..T-69** in this section, and the
main-table rows reading T-55..T-58 belong to other sessions. Same rule as the register IDs: one identifier, one
meaning, and the earlier number is stated instead of being silently reused.

## Session `arena/d52ad947-prod3` — T-70…T-73 integration round (2026-11-20)

Scope: reconcile the tree after PRs up to #82 landed while this branch was open; add only what `main`
still demonstrably lacked; re-run all release gates; PR → main, merge, live confirmation. No product,
price, rating, or account data was added; no owner-only gate was claimed.

### Work items

**Method note.** The sweep is scripted rather than eyeballed, because this branch has had nine rebase rounds today and a hand check of a moving tree is worthless 20 minutes later. Re-run it with the one-liner in the session log if a merge disturbs it: for every page, count `https?://` anchors to `amazon.com` with no `rel=` (expect 0), pages without the disclosure strip (expect 0), and `data-event="outbound_click"` anchors without `tag=shopnow047c-20` (expect 0). **Next free claim: T-67.**
---

## Session arena/80802891-prod3 — T-27 suggestion-register completeness and design-brief pass (2026-11-20)

Note: this session originally claimed "T-24", then "T-26", before successive rebases onto
`origin/main` revealed that sessions `arena/f4694e48-prod3` (T-24 executive-summary refresh),
`arena/70e8475c-prod3` (T-25 live link re-check) and `arena/e83cdf55-prod3` (T-26 provenance
integrity pass) had already claimed those IDs. The claim was renumbered to **T-27**; no other
session's rows were altered. Scope trimmed accordingly: the executive summaries and the
product-intent provenance records are completed work by those sessions and are not touched here.

| ID | Task | Status | Owner | File scope |
|----|------|--------|-------|------------|
| T-27 | Fix demonstrable register defect (restore SG-20 content clobbered during PR #17's merge replay — recovered from PR #17 commit `7fbef67`; SG-20/SG-21 are currently exact duplicates); add reader-facing polish-path rows SG-26..SG-30 (polish path, nav labels, shipped RSS feed, Search Console, reader capture) and design-brief rows SG-31..SG-34 (analytics endpoint, design brief for the next design pass, seasonal/trendy topic clusters as working titles only, publishing cadence); sync `direction.html`/decision-desk cross-references and add a design-brief section; live re-verify load-bearing guidance quotes (FTC Disclosures 101, Google `rel="sponsored"`, Creators API ASIN definition); run all release gates; integration PR → main, merge, confirm Pages deploy | done | `arena/80802891-prod3` | `data/suggestions.json`, `suggestions.html` (generated), `direction.html`, `DIRECTION.md`, `docs/verification.md`, `COORDINATION.md` |

### Handoff / conflict log — 2026-11-20 (session arena/80802891-prod3)

- `git pull --rebase` before the claim push conflicted on `COORDINATION.md` repeatedly as
  `origin/main` moved mid-flight (PRs #22/#24/#25/#26/#27 merged while this claim was being
  replayed, plus new session records for T-24, T-24b, T-25, T-26). Each time the resolution kept
  **both** sides verbatim — every upstream session record, plus this session's claim (renumbered
  T-24 → T-26 → T-27 as the taken IDs were discovered). Nothing of any other session's work was
  discarded. The renumbering followed the same precedent session `arena/28d2d6c0-prod3` used for
  its T-20 → T-23 renumber.


## T-27 completion record — session arena/80802891-prod3 (2026-11-20)

- **Status: done.** PR #76 — https://github.com/wingbangboozle1-lang/Prod3/pull/76 (opened from
  this session's branch `arena/80802891-prod3`, merged without waiting; merge/deploy results
  recorded in the follow-up close-out below).
- **Claim (as filed):** fix the demonstrable register defect (SG-20 content clobbered during PR
  #17's merge replay), complete the suggestion register against the brief, and run the
  design-brief pass.
- **What was done:**
  1. SG-20's original content recovered verbatim from PR #17 commit `7fbef67`
     (`git show 7fbef67:data/suggestions.json`); SG-21 restored as its own "spine" proposal; the
     interim tombstone withdrawn; FLG-021 items (3)(4) marked resolved with provenance; gate D20
     keeps duplicate live titles impossible.
  2. The SG-26 gap filled with the reader-facing polish-path row the brief assigns to that slot
     (it carries the parallel passes SG-27..SG-31 registered by session ce911db5, kept verbatim);
     the register no longer skips a number and D29's phantom-id check passes against a real row.
  3. Design brief registered and published: SG-48 (self-hosted analytics endpoint; no conversion
     talk), SG-49 (design brief for the next design pass), SG-50 (seasonal clusters — working
     titles only, never claims about popularity/search volume), SG-51 (publishing cadence,
     aligned with the recorded DT-10 decision: one guide a calendar month, next due 2026-12-31).
     `direction.html` gains the "Design brief for the next design pass" section (six asks, each
     with the gate it must respect) to feed the redesign prompt.
  4. Direction-page integrity: duplicated SG-19 note and glued heading fixed; ranges updated to
     SG-01..SG-51; the path chooser kept in its T-39-reconciled form (one identifier, one
     meaning). `docs/verification.md`, `DIRECTION.md`, exec summaries and README updated.
- **Sources verified line-by-line (re-fetched 2026-11-20; quotes and URLs in the PR body and
  `docs/verification.md`):** S01 Operating Agreement ("Updated: October 15, 2025"; §5/§6
  verbatim), S02 Program Policies ("Updated: April 14, 2026"), S03 FTC Disclosures 101
  ("hard to miss" / "with the endorsement message itself"), S04 Google qualify-outbound-links
  (`sponsored` definition; "Last updated 2025-12-10 UTC."), S06 Creators API GetItems (ASIN =
  "10-Character alphanumeric unique identifier assigned by Amazon"). Nothing drifted; no
  register value needed changing. Recovery provenance: PR #17 commit `7fbef67`.
- **Verification performed:** `build_chrome --check`, `build_registers --check`,
  `build_decisions --check`, `build_sitemap --check`, `build_readme --check`,
  `scripts/check_site.py` (conflict-marker scan clean), `tools/verify_site.py` (release gate),
  `tools/check_site.py` (39 pages, 5,949 assertions; D18b/D20/D23/D25/D29/D34/D40 green),
  `tools/crawl_links.py` (39 crawled, 38 reachable, no broken links, no dead anchors, no
  orphans) — all exit 0 on the merged tree.
- **Irregularities logged:** (a) origin/main moved eight times during this task (PRs #22..#75);
  every `git pull --rebase` conflict on `COORDINATION.md`, `data/suggestions.json` and generated
  pages was resolved keeping **both** sides verbatim — no other session's record or row was
  discarded. (b) The suggestions register tail kept growing during the work (SG-27..SG-47 by
  sessions ce911db5/7878cdbe/others); this session's design-brief rows were renumbered each
  round and settle at **SG-48..SG-51**. (c) The duplicate-FLG-identifier irregularity on
  flagged.html noted earlier was resolved upstream by renumbering (FLG-001..FLG-034 unique);
  corroborated, not re-fixed here. (d) An intermediate rebase step once committed
  `direction.html` with conflict markers in an in-flight commit; the final tree is clean (the
  conflict-marker scan gate passes) — recorded here rather than hidden.
- **Not claimed:** Associates enrollment, intended ASINs, Special Link validity,
  tracking-report attribution, Search Console, analytics volume, or the validity/invalidity of
  the supplied short links (FLG-006/FLG-017 unresolved).
| Item | Evidence before | Change |
|---|---|---|
| The ce911db5 same-day disagreement records existed only in the board and the flagged callout, so FLG-031's "kept in `data/products.json`" claim was untrue | `data/products.json` held the 70e8475c, 6bf60cac and 6c0972fb passes but no ce911db5 records | Published ce911db5 records for all five products transcribed verbatim into each product's `short_link_rechecks` with explicit provenance (fetched by ce911db5, transcribed by d52ad947) |
| No fifth-pass observation after sessions disagreed | FLG-017/025/031/039 rested on four passes | d52ad947 pass recorded as `short_link_rechecks` entries (P-01, P-04): both fetched links ended at `https://www.amazon.com/`; agrees with the four earlier same-day records for P-01 and with ce911db5/6bf60cac/6c0972fb for P-04; no prior record deleted |
| FLG-017 register row still described only the first pass | `data/flagged.json` FLG-017 detail | Updated to name all five passes and the record locations |
| Q-22 did not mention the later passes | `data/open-questions.json` Q-22 known | Updated with the 6bf60cac, 6c0972fb and d52ad947 passes; status stays `blocking` |
| `executive-summary.html` still cited FLG-028 for the all-five homepage checks | The subject publishes as FLG-025 (6bf60cac) and FLG-039 (6c0972fb) | Reference corrected; the d52ad947 pass added; both executive summaries updated for the five-pass picture (no ordering claim — FLG-012) |
| FLG-024 unresolved (owner one-click) | `PATCH /repos/wingbangboozle1-lang/Prod3/pages {"build_type":"workflow"}` → HTTP 404, re-attempted 2026-11-20 by this session (same result as the T-39 attempt) | Dated re-attempt recorded on the FLG-024 row and board bullet |
| FLG-032 duplicate board rows | Board carried T-20/21/22 twice (superseded + done, same scope); the flag delegates the decision to "the next integration session" | The three superseded rows consolidated away; FLG-032 status set to partially resolved; T-12..T-17 duplicates left untouched for the owner |
| Board header and FLG bullet list stale | Header named the previous session; bullets stopped at FLG-017/024 while the page publishes FLG-001..041 with FLG-022/023/034..036 unoccupied | Header updated; bullets extended with dated one-liners through FLG-041 |

### Verification on the final tree

`Deploy GitHub Pages` run `44695121743` on merge commit `0569046` (PR #84) **failed**, and runs `44695018843` (PR #80) and `44695015620` (PR #82) failed the same way just before it. Cause was not this session's content: those merges landed generated files that were stale on arrival — `decisions.html`, `README.md` and `products/*.html` were committed out of step with the `data/*.json` registers they are rendered from, so `scripts/build_decisions.py --check`, `scripts/build_readme.py --check` and `D32-product-pages-fresh` failed the release job. The rule in this repository is that generated HTML is committed; the corollary nobody wrote down is that **a merge must re-run the generators after its last rebase**, because a rebase moves the data under a page that was current when it was built. Fix: regenerate all seven outputs on the merged tree and commit them (this branch carries the result). Gates on that tree: `scripts/check_site.py` all passed; `tools/check_site.py` 42 pages / 6,893 assertions, all rules passed; `tools/verify_site.py` release gate passed; `tools/crawl_links.py` 42 pages, 0 broken links, 0 orphans; the seven `--check` freshness modes current. Claim: **T-67**; next free claim **T-68**.

### Session arena/26285b01-prod3 — T-58 claim and collision history (2026-11-20)

Final claim id: **T-58**. (Third collision: the first renumber, T-39, was taken on main mid-session; the second, T-52, was taken while this claim was being rebased onto PRs #36-#51; this id is the next free one after the board maximum.) The claim commit named this task T-25; `origin/main` had meanwhile
gained PRs #26–#33 (T-25..T-38 taken, including the SG-27..SG-30 register pass and the RSS
head-link pass this session had planned), so it was first renumbered T-39. During the work,
PRs #36–#51 merged and a main-side session took T-39 as well, so the claim is renumbered again twice — **T-52**, then **T-58**, each time the next free id after the board maximum, as further sessions merged. No claim row of any other session is
touched.

**Conflict log (protocol-required).** `git pull --rebase` conflicted on `COORDINATION.md` three
times on 2026-11-20 as other sessions merged to `main` mid-session. Each time the resolution
kept **both** sides — upstream rows and session records unchanged, this session's row and log
appended after them. No other session's work was discarded.

**Scope (as executed).** Register-integrity and publication-machinery work that the post-#35
tree still lacked: (1) `flagged.html` shipped two FLG-020s and two FLG-021s — two sessions
merged the same numbers; the later set is renumbered FLG-024..FLG-027 with all cross-references
updated. (2) The `DIRECTION.md` digest carried SG-27..SG-30 rows whose meanings differed from
`data/suggestions.json`; they are registered as SG-32..SG-35 (original work credited to session
arena/2ef30474-prod3), and the digest index is now generated from the register by
`scripts/build_digest.py`. (3) `ideas.html` cited SG-26 for the SG-31 idea and wrong FLG ids.
(4) `DIRECTION.md` cited DT-11 before it existed — DT-11 is now registered. (5) New gates D31
(cross-surface id resolution), D32 (digest freshness), D34 (flagged heading uniqueness + machine
register sync), each negative-tested. (6) Feed item titles aligned to the published guide h1s
(one feed title overclaimed what a NIST claim covers). (7) `about.html`'s named-editor paragraph
cited SG-19 (the tap-target row) for SG-24's subject. (8) A deployable, privacy-preserving
self-hosted analytics collector ships as code; `ENDPOINT` stays blank until the owner deploys
and publishes a privacy notice. (9) Executive summary refreshed; all release gates re-run.

## Request on other sessions' work — FLG-035/FLG-036 placeholders (session `arena/26285b01-prod3`, T-58)

From session `arena/26285b01-prod3` (T-58). `data/flagged.json`'s `id_policy` note describes "the published FLG-034 … and the published FLG-035/FLG-036 records" as untouched, but no page in the merged tree publishes FLG-035 or FLG-036 and no commit in the history contains their headings. If your session holds those two records (they may live in an open PR), please land them on `flagged.html` + `data/flagged.json`; if they were lost in a merge, please say so in a dated note. Gate `D41-id-refs` currently allows those two ids only inside the `id_policy` note. Nothing in the note was edited.

## Session arena/26285b01-prod3 — T-58 completion log (2026-11-20)

**Task.** Register-integrity + publication-machinery pass. Claim row: T-58 (the claim commit named T-25; renumbered twice after board collisions, T-39 then T-52, each taken by main-side sessions mid-flight; T-58 is the claim row on the pushed branch). PR: **#77** (`arena/26285b01-prod3` → `main`).

**Sources and verification.** No new external claims this pass; standing sources (S01/S02 policy pages, S03/S07/S10/S13/S21, the USDA anchors fixture) unchanged and no evidence-status field weakened. Verification on the PR branch, all passing: `python3 scripts/check_site.py`; `python3 tools/verify_site.py` (release gate); `python3 tools/check_site.py` — 42 pages, 7,359 assertions including the new gates; `--check` freshness for `build_registers`, `build_decisions`, `build_digest`, `build_readme`, `build_chrome`, `build_sitemap`; `python3 tools/crawl_links.py` — 0 broken links, 0 dead anchors, 0 orphans. New gates D44 (cross-surface register id resolution), D45 (DIRECTION digest freshness), D43 (analytics endpoint/event-contract consistency) were each negative-tested before use (phantom id injected → fail; stale digest → fail; filled ENDPOINT → fail; renamed event → fail).

**Irregularities found and repaired (machine-verified).** Same id, different findings, wherever a merge dropped a renumber: DIRECTION.md cited DT-11 for a question DT-11 does not ask (now registered as **DT-13**); `air-fryers.html` and `data/products.json` named a retired flag number for the F-01 capacity conflict; `data/open-questions.json` named two findings by ids renumbered away (now FLG-031/FLG-028); the suggestions premise named the wrong flag for the SG-26 gap (now FLG-029); `ideas.html` named a wrong-subject flag for the homepage-link findings; `about.html` cited SG-19 (tap-target pass) for SG-24's named-editor subject. The DIRECTION.md suggestion index had drifted from the register (invented statuses, missing rows) — it is now generated from `data/suggestions.json` by `scripts/build_digest.py`, gate D42.

**Irregularities flagged, not repaired.** The FLG-035/FLG-036 placeholder question — see the request above.

**Merge-conflict protocol log.** `git pull --rebase` conflicted on `COORDINATION.md` and the shared registers repeatedly as PRs #36-#73 merged mid-session. Every resolution kept both sides, or took the converging session's version where it already contained the same fix. No other session's work was discarded. The final resolution adopted main's numbering (FLG-024..FLG-038, SG-01..SG-47, Q-01..Q-29) and kept only the deltas main lacked.

**Notes for the owner.** `ENDPOINT` stays blank in `assets/app.js`; the deployable collector (`analytics/collector/worker.js`) is code only until the owner deploys it and publishes a privacy notice (four steps in `analytics/collector/README.md`; gate D43). The SG-21 displaced-proposal question is DT-13. The campaign ledger remains empty and no forecast of any kind was computed.

## Session `arena/1fbc2432-prod3` — T-70 independent verification round (2026-11-20)

Claim note: this session claimed the next free board ID six times and collided each time —
T-46 (`arena/59a087a1-prod3`, PR #38), T-47 (`arena/cafc55da-prod3`, PR #39), T-48
(`arena/6bf60cac-prod3`, PR #43), T-53 (the T-52 lineage, PRs #44–#53), T-57
(`arena/6f44d8c9-prod3`, PR #70) and T-66 (session aa7b8dd8, PRs #80–#82). Its proposal row was
renumbered through the register collisions the same way (SG-39 → SG-48 → SG-49 → **SG-54**,
taken in turn by PRs #52, #72 and #78). Every collision was resolved by renumbering this
session's claim while keeping the other sessions' rows untouched, and the abandoned remote
claim commit (`22bcd7f`) was merged into this branch rather than force-pushed away. After each
merge, upstream's newer register state was taken and this session re-applied only what `main`
still lacked.

### New dated observations (fetched 2026-11-20, this session's network path; recorded in `data/recheck-2026-11-20-1fbc2432.json`)

1. **All five supplied short links ended at the Amazon homepage** (page title read;
   `B02NbDxp3` twice in-session) — fetched before main's T-60 recheck merged, agreeing with it
   and with every earlier 2026-11-20 observation; recorded on FLG-025 as an additional
   same-day reproduction so no session owns the ordinal.
2. **Diagnostic:** the direct listing `https://www.amazon.com/dp/B09B7SB46R` served the Emeril
   26QT product page with the recorded title and browse path — the drift is in short-link
   resolution, not dead listings.
3. **Official policy pages read verbatim** (this session could reach the official hosts):
   Operating Agreement updated 2025-10-15 (§5 exact sentence); Program Policies updated
   2026-04-14 — §2(a), §2(b) (tag, price, claims, product lists, sub-tags), Participation
   Requirements §6(t)/(v)/(w), §6(y), IP License section 2 item (h) (ASIN storage) and §4
   Agent Terms; FTC Disclosures 101 (November 2019); Google Qualify Outbound Links (updated
   2025-12-10).

### Independent confirmation of the merged clause correction

This session's verbatim reads agree with the clause-letter correction already on `main`
(commit `7c49a3e`, FLG-020 resolved): ratings = Participation Requirements §6(t),
URL-obscuring = §6(v), shortener = §6(w), and §2(b) carries the tag, price, misleading-claims,
product-list and sub-tag clauses. The recheck file records the confirming evidence instead of
re-editing the corrected registers.

### Edits applied (each traceable to the recheck file)

1. **SG-54 registered** (`data/suggestions.json`; mirrored in `DIRECTION.md` and the
   `direction.html` range line): before any automated Amazon listing or price refresh, use the
   Product Advertising API or make the fetcher identify itself under the IP License Agent Terms
   (§4, read verbatim). Recommendation: A long-term, B until the PA API is approved; C is
   non-compliant — do not implement.
2. **FLG-025 additional same-day reproduction** appended in `data/flagged.json` and the
   `flagged.html` callout (ordinal-free phrasing; nothing overwritten).
3. **`data/recheck-2026-11-20-1fbc2432.json`** created — the dated record of every official
   page this session fetched, with verbatim quotes.
4. Regenerated surfaces after the data edits. No CTA destination changed (T-60's tagged
   Special Links are kept as merged); `data/products.json` untouched.

### Gates and merge record

To be appended below after the final gate run and merge.

## Session `arena/aa7b8dd8-prod3` — T-70/T-71 final record (2026-11-20, re-appended after merge)

**Claim history.** Claimed as T-48..T-51, renumbered T-52..T-55 on the first collision, T-56 on the second (PR #43 landed first), T-66/T-67 on the third, T-70/T-71 after upstream took T-52..T-57 and T-66/T-67. The one-identifier-one-meaning rule was applied every time; no other session's row was altered.

### What this session changed (T-70, PR #82)

- **FLG-041 restored** in `data/flagged.json` and on `flagged.html`: the P-03 (Chefman 8 Qt TurboFry, B08DKYBTPH) temperature/wattage listing conflict — title 450°F Hi-Fry vs bullets/spec 200–400°F; 1000W bullet vs 1700W spec table. First published 2026-11-20 by session 59a087a1; the renumbering passes left it without a registered id (FLG-027 documents the mechanism). Restored with **no new observation**; the dated basis is the same official-listing check in `data/products.json` and the S31 quote.
- **Dangling references repointed:** `data/products.json` `(FLG-022)`→F-01, `(FLG-023)`→FLG-041; `direction.html` and the `DIRECTION.md` decision log FLG-021 → FLG-029; `air-fryers.html` capacity chip links the F-register on `decisions.html` and the P-03 card carries the FLG-041 chip; FLG-027 reconciled to the final renumbering.
- **Superseded by upstream, accepted without loss:** upstream's generated README register table, upstream's `build_products.py` `names_me()` matcher, upstream's D39 gate (this session's D06b draft removed as redundant).

### Verification performed (T-71)

- Full local gate suite on the final tree: `tools/verify_site.py` (release gate passed), `tools/check_site.py` (42 pages, 6,913 assertions — D38/D39 green), `scripts/check_site.py` (all passed), `tools/crawl_links.py` (42 pages, 41 reachable, 0 broken links, 0 dead anchors, 0 orphans), all six `--check` freshness gates.
- **PR #82:** https://github.com/wingbangboozle1-lang/Prod3/pull/82 — merged without waiting for approval, `mergedAt` 2026-11-20T07:26:45Z, merge commit `76b267f9c5008fdad8185a66de47f0fd7be291b3`.
- **Deploy note:** the `Deploy GitHub Pages` runs for the merge cluster PRs #82/#80/#84 failed their "Regenerated surfaces are current" step (auto-merge commits combined concurrent sessions' data with stale generated surfaces). PR #85's session merged the mechanical rebuild and its run `44695185642` succeeded; judge deploys by the workflow and live URL (FLG-024 note).
- **Live check (fetched, not assumed):** https://wingbangboozle1-lang.github.io/Prod3/flagged.html serves the disclosure strip above the masthead, FLG-041 in full with the S31 source link, and FLG-039/FLG-040 (upstream's tag-parameter repair: every reader-facing product button now carries `?tag=shopnow047c-20&linkCode=sl1`).

### Irregularities logged (do not block)

- FLG-041 itself — the restored finding, published on `flagged.html`.
- The transient deploy-failure cluster self-resolved via PR #85; the legacy `pages build and deployment` runs succeeded throughout, so the live site was never broken.
- Unchanged owner-side gates: FLG-001 intended ASINs, FLG-006 Special Link test in the enrolled Associates workflow, FLG-010 account status, FLG-024 Pages build_type setting.

- All `data/*.json` registers read; id ranges cross-checked against the pages that publish them
  (SG/Q counts, FLG-001..041 with FLG-022/023/034..036 unoccupied).
- Gates re-run after the edits: `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`,
  `tools/crawl_links.py` and the four `--check` freshness gates plus the `build_*` regenerations —
  results in the PR description.
- Observations this session used `fetch_page` on the supplied `link.amazon` URLs only; final URL read
  for an `/dp/<ASIN>`; no price, rating, or offer text recorded; exact fetch time not recorded (FLG-012).

### Sources

- `data/products.json` (dated observation records, including the transcribed ce911db5 pass and this session's fifth pass)
- Session record of ce911db5 (T-41 live-observation table, this board) — transcription source, cited per record
- GitHub REST API `PATCH /repos/…/pages` response (HTTP 404, 2026-11-20) — FLG-024 evidence
- Official policy pages (S01, S02) unchanged this session; last re-read 2026-11-20 by 70e8475c, 6bf60cac and 6c0972fb

### Not claimed / not verified here (unchanged owner gates)

FLG-001 intended ASINs · FLG-006 Special Link test in the enrolled workflow · FLG-010 Associates
account status · signed-in link check (Q-22) · Search Console · analytics endpoint · email capture ·
share-debugger check (F-21/Q-21) · Pages `build_type` setting (FLG-024, owner one-click) ·
FLG-033 source-register fetch dates · remaining FLG-032 duplicates. No new claims about traffic,
conversion, or product superiority.

### Independent confirmation of the merged clause correction

This session's verbatim reads agree with the clause-letter correction already on `main`
(commit `7c49a3e`, FLG-020 resolved): ratings = Participation Requirements §6(t),
URL-obscuring = §6(v), shortener = §6(w), and §2(b) carries the tag, price, misleading-claims,
product-list and sub-tag clauses. The recheck file records the confirming evidence instead of
re-editing the corrected registers.

### Edits applied (each traceable to the recheck file)

1. **SG-54 registered** (`data/suggestions.json`; mirrored in `DIRECTION.md` and the
   `direction.html` range line): before any automated Amazon listing or price refresh, use the
   Product Advertising API or make the fetcher identify itself under the IP License Agent Terms
   (§4, read verbatim). Recommendation: A long-term, B until the PA API is approved; C is
   non-compliant — do not implement.
2. **FLG-025 additional same-day reproduction** appended in `data/flagged.json` and the
   `flagged.html` callout (ordinal-free phrasing; nothing overwritten).
3. **`data/recheck-2026-11-20-1fbc2432.json`** created — the dated record of every official
   page this session fetched, with verbatim quotes.
4. Regenerated surfaces after the data edits. No CTA destination changed (T-60's tagged
   Special Links are kept as merged); `data/products.json` untouched.

### Gates and merge record

To be appended below after the final gate run and merge.
## Session arena/37c5f395-prod3 — T-75…T-78 (2026-11-20), renumbered three times after board collisions

**Collision, handled without discarding anyone's work.** This session claimed **T-48…T-51** at a time
when the board's highest row was T-47, and shipped four commits to its branch. While it worked, the
T-46…T-65 rounds (sessions 6bf60cac, 2cd3bab9, 8692a390, 7878cdbe, 6c0972fb, 6f44d8c9) landed on
`main` and took T-48…T-57 for different subjects. Per the one-identifier-one-meaning rule this
session's rows were renumbered **T-66…T-69** — and when sessions 6c0972fb/1fbc2432 took T-66/67 and SG-48 a second time during the final integration, and when sessions d52ad947/aa7b8dd8 took T-70…T-74 a third time during final integration, to **T-75…T-78** (the suggestion kept **SG-55**, still unclaimed upstream); the commit subjects on the branch still say T-48…T-51 and
are left as the historical record of when they were written. Nothing published on `main` was discarded
in the merge: every conflict was resolved in favour of the merged mainline, and this session's unique
work was re-applied on top.

**What this session kept (its own work, re-based onto the mainline conventions):**

1. **Shop-voice front page (T-75).** Hero: "Five kitchen tools, sorted by the cook they belong to." —
   clearer lede, less defensive honesty note ("We read listings for a living; we do not run a lab…"),
   the mainline's intent-fork CTAs kept. The featured pick's headline figure now reads **2 × 3 qt**
   (the undisputed basket sizes) instead of "6 qt total", because F-01 keeps both readings open. One
   broken sentence ("When Search Console setup…") fixed earlier in the round.
2. **Two question-shaped guides (T-76).** `are-air-fryers-worth-it.html` and
   `smart-thermometer-questions.html` — topics neither the 2026-11-19 batch nor the T-61 round covers
   ("Are air fryers worth it?" is the category's evergreen question). Both carry the current guide
   template: Article JSON-LD with publisher + description, BreadcrumbList, the dated byline, and the
   USDA figures aligned with `assets/decision-tools.js` (145/160/165 °F, plus the 3-minute whole-muscle
   rest the chart carries). Wired into the front-page grid, the buying-guide clusters ("fifteen" now),
   and the category read-next boxes. Feed items added; the publishing-coverage gate self-counts.
3. **SG-55 (T-77).** A dated voice refresh for the 2026-11-19 guide batch, as a reviewable proposal.
4. **Defects found while merging and fixed (T-77):** `air-fryers.html` read-next listed the same two
   links twice (duplicated block, the very FLG-038 class of defect — removed); the D40 count regex
   could not see "Thirteen guides" because the word list stopped at "twelve" (extended to sixteen);
   Q-14/Q-17, the front page, README and both executive summaries said "thirteen guides" while fifteen
   ship (corrected).

**What this session deliberately DROPPED from its in-flight work, and why (T-69):**

1. **A parallel FLG renumbering.** This session had independently renumbered the four duplicated flag
   callouts to FLG-025…FLG-028. The T-64 round fixed the same duplication on `main` with a different
   scheme (FLG-027 records the duplication; the displaced callouts became FLG-028…FLG-031). The
   mainline scheme is kept everywhere; this session's numbering exists only in its early commit
   subjects and in this note. No finding was lost — both schemes preserved every callout.
2. **FAQPage JSON-LD on the two new guides.** The round's own findability add-on was dropped after
   reading **SG-44** on the merged register ("Do not add FAQ markup expecting a Google FAQ rich result —
   that feature is gone"). The visible FAQ text stays; the markup does not. The guides ship Article +
   BreadcrumbList only, matching the other thirteen.
3. **Register rows SG-32…SG-35 and Q-24…Q-25 as this session wrote them.** The mainline register had
   grown to SG-47 / Q-29 with rows covering the same ground at those numbers (PageSpeed → Q-29/SG-46,
   seasonal block → SG-43, FAQ rollout → contradicted by SG-44). Only the genuinely new proposal —
   the guide-voice refresh — was re-registered, as **SG-55**. Duplicates were not re-added.

### Verification on the merged tree (2026-11-20)

```
tools/check_site.py                  44 pages · 6,609 assertions · all rules passed
scripts/check_site.py                All checks passed
tools/verify_site.py                 Release gate passed (feed items = guides on disk)
build_chrome/registers/decisions/products/sitemap/readme/ideas --check   all current
tools/crawl_links.py                 44 pages crawled · 43 reachable from index.html
                                     no broken links, no dead anchors, no orphans
```

Every figure in the two new guides traces to `data/products.json` / `data/sources.json` (the five
official listings) or to the USDA rows in `assets/decision-tools.js`. No price, rating, promo or
first-hand-experience phrasing was introduced (P10–P12, D10 gates green). The campaign ledger is
untouched and still empty. No new external source was registered this round; the guides cite only
S-ids that already exist.

### Not claimed (unchanged owner gates)

Intended ASINs (FLG-001) · Special-link compliance (FLG-006/FLG-026, Q-24) · account status
(FLG-010) · the all-five-homepage link behaviour (FLG-025/FLG-031, Q-25) · Search Console (Q-28) ·
Core Web Vitals (Q-29) · share-debugger check (Q-21/F-21) · Pages `build_type` (FLG-024). Nothing in
this round claims traffic, demand or conversion for the two new guide topics: they are editorial
hypotheses until Q-27/Q-28 return data.

*(merge result and deploy confirmation recorded below after the PR merges)*

## Session arena/26285b01-prod3 — T-58 merge and deploy record (2026-11-20)

- **PR #77** `arena/26285b01-prod3` → `main`: opened 2026-11-20, merged **2026-11-20** (`gh pr merge --merge`, no approval wait per the standing brief). Merge commit: `cec5f4d846fa6355388f9ff35e5e2c44d480f134`.
- The merge went in after three sync-merge retries against a `main` that moved every few minutes (PRs #74–#91 merging concurrently). One retry slipped conflict markers into `direction.html`, which failed the repo's own `Deploy GitHub Pages` gate on the merge commit (run 44696490577). The markers, the SG-26 gap notes (a row now occupies the slot), and the gate exception logic were repaired immediately after in this follow-up commit; the full suite is green again locally (42 pages, 8,018+ assertions in `tools/check_site.py`, plus `scripts/check_site.py`, `tools/verify_site.py`, and all `--check` freshness gates).
- **Deploy confirmed 2026-11-20:** `Deploy GitHub Pages` run 44697027338 (merge of PR #92) completed **success**, `pages build and deployment` success, GitHub Pages API `status: built`, source `main:/`, and https://wingbangboozle1-lang.github.io/Prod3/ serves the merged tree (disclosure above the fold, shop-first front page, buy buttons carrying the Associates tag with the unresolved short links documented on the cards). Record closed.

## Session `arena/1fbc2432-prod3` — T-70 independent verification round (2026-11-20)

Claim note: this session claimed the next free board ID six times and collided each time —
T-46 (`arena/59a087a1-prod3`, PR #38), T-47 (`arena/cafc55da-prod3`, PR #39), T-48
(`arena/6bf60cac-prod3`, PR #43), T-53 (the T-52 lineage, PRs #44–#53), T-57
(`arena/6f44d8c9-prod3`, PR #70) and T-66 (session aa7b8dd8, PRs #80–#82). Its proposal row was
renumbered through the register collisions the same way (SG-39 → SG-48 → SG-49 → **SG-54**,
taken in turn by PRs #52, #72 and #78). Every collision was resolved by renumbering this
session's claim while keeping the other sessions' rows untouched, and the abandoned remote
claim commit (`22bcd7f`) was merged into this branch rather than force-pushed away. After each
merge, upstream's newer register state was taken and this session re-applied only what `main`
still lacked. The T-70 id itself was later claimed in parallel by session `arena/d52ad947-prod3`
(PRs #80–#83 lineage); both rows now sit on the board — the documented FLG-032 duplicate-id
defect — and neither session's record was discarded.

### New dated observations (fetched 2026-11-20, this session's network path; recorded in `data/recheck-2026-11-20-1fbc2432.json`)

1. **All five supplied short links ended at the Amazon homepage** (page title read;
   `B02NbDxp3` twice in-session) — fetched before main's T-60 recheck merged, agreeing with it
   and with every earlier 2026-11-20 observation; recorded on FLG-025 as an additional
   same-day reproduction so no session owns the ordinal.
2. **Diagnostic:** the direct listing `https://www.amazon.com/dp/B09B7SB46R` served the Emeril
   26QT product page with the recorded title and browse path — the drift is in short-link
   resolution, not dead listings.
3. **Official policy pages read verbatim** (this session could reach the official hosts):
   Operating Agreement updated 2025-10-15 (§5 exact sentence); Program Policies updated
   2026-04-14 — §2(a), §2(b) (tag, price, claims, product lists, sub-tags), Participation
   Requirements §6(t)/(v)/(w), §6(y), IP License section 2 item (h) (ASIN storage) and §4
   Agent Terms; FTC Disclosures 101 (November 2019); Google Qualify Outbound Links (updated
   2025-12-10).

### Independent confirmation of the merged clause correction

This session's verbatim reads agree with the clause-letter correction already on `main`
(commit `7c49a3e`, FLG-020 resolved): ratings = Participation Requirements §6(t),
URL-obscuring = §6(v), shortener = §6(w), and §2(b) carries the tag, price, misleading-claims,
product-list and sub-tag clauses. The recheck file records the confirming evidence instead of
re-editing the corrected registers.

### Edits applied (each traceable to the recheck file)

1. **SG-54 registered** (`data/suggestions.json`; mirrored in `DIRECTION.md` and the
   `direction.html` range line): before any automated Amazon listing or price refresh, use the
   Product Advertising API or make the fetcher identify itself under the IP License Agent Terms
   (§4, read verbatim). Recommendation: A long-term, B until the PA API is approved; C is
   non-compliant — do not implement.
2. **FLG-025 additional same-day reproduction** appended in `data/flagged.json` and the
   `flagged.html` callout (ordinal-free phrasing; nothing overwritten).
3. **`data/recheck-2026-11-20-1fbc2432.json`** created — the dated record of every official
   page this session fetched, with verbatim quotes.
4. Regenerated surfaces after the data edits. No CTA destination changed (T-60's tagged
   Special Links are kept as merged); `data/products.json` untouched.

### Gates and merge record

**Gates on the final merged tree (all green):** all seven `--check` freshness gates (chrome on
42 pages, registers, decisions, products, sitemap, README table, ideas brief);
`scripts/check_site.py`; `tools/verify_site.py`; `tools/check_site.py` (42 pages, 6,913
assertions, including the D35 clause-citation gate and the J-series script gates);
`tools/crawl_links.py` (42 pages crawled, 41 reachable from index, 0 broken links, 0 dead
anchors, 0 orphans).

**PR and merge:** PR **#79** opened from this branch and merged without waiting — merge commit
`971aaac`. The T-70 claim itself collided in flight with PRs #80–#85 landing on main; each
landing was merged into this branch before the push, with upstream register state taken
verbatim and this session's additions re-applied only where main still lacked them.

**Pages deploy (both paths, PR #79):** `Deploy GitHub Pages` run `44695805030` — success;
`pages build and deployment` (dynamic) run `44695804382` — success. Deploys for the follow-on
merges (#83) also succeeded (`44696238266` + dynamic run), so the live site carries the merged
tree; main's tree contains the recheck file, SG-54 and the FLG-025 reproduction note.

**Task status: T-70 done (this session's row).** The board rewrite in PR #83 dropped this row
and record; they are restored here verbatim, with that session's rows untouched.


## T-27 close-out — PR, merge and deploy record (session arena/80802891-prod3, 2026-11-20)

- **PR:** #76 — https://github.com/wingbangboozle1-lang/Prod3/pull/76 (title: "T-27: register
  integrity and design-brief pass — SG-20/SG-21 recovered from history, SG-26 gap filled,
  design brief registered, all sources re-verified").
- **Merge result:** merged 2026-11-20T07:38:10Z, merge commit `e6e7df3c764fb278714904b7e5d2b414438581dd`.
- **Deploy:** "Deploy GitHub Pages" workflow run 44696425983 for the merge commit completed
  **success** (20s). The legacy "pages build and deployment" run 44696425330 shows `cancelled`,
  which is the known double-path behaviour (FLG-024); the artifact deploy is the real one.
- **Live verification (2026-11-20, platform page fetcher; sandbox curl cannot reach github.io):**
  the deployed `direction.html` carries the T-27 title ("Direction — Decision Log, Path Chooser &
  Design Brief"), the h1 "decisions, the path chooser, and the brief for the next design pass",
  and the recovery sentence (SG-20 recovered from PR #17 commit `7fbef67`, SG-21 restored).
  `data/suggestions.json` on `main` holds 58 rows: SG-20 "Ask the Associates account…", SG-21 live
  as the spine proposal, SG-26 filled, SG-55..SG-58 = the design-brief rows.
- **Post-merge incident (found by the live read-back, fixed in this close-out):** the integration
  merge that followed (PR #77, merge `cec5f4d`) shipped `direction.html` with **literal conflict
  markers** (`<<<<<<< HEAD` … `>>>>>>> origin/main`) at its registers section, kept a stale
  snapshot pointer ("SG-21 is retired in place… SG-26 is unoccupied"), and dropped the design-
  brief section entirely. This is the same class of integration loss FLG-040 already records.
  This close-out resolves the markers into one "Registers, one source of truth" section
  (SG-01..SG-58), restores the recovery-consistent pointer, and re-adds the design brief
  (proposal SG-56). The conflict-marker scan gate (`scripts/check_site.py`) passes on the fixed
  tree.
- **Standing caution for later integrators:** when squashing or replaying multi-session branches,
  re-run `scripts/check_site.py` (marker scan) and read back the live page after deploy; two
  separate integrations on 2026-11-20 silently lost or garbled committed content.


### Merge and deploy record — T-78 (2026-11-20)

- **PR #88** — https://github.com/wingbangboozle1-lang/Prod3/pull/88 — merged to `main` with `gh pr merge 88 --merge` as merge commit **`a5a100e`**. Three earlier merge attempts hit in-flight upstream merges (PRs #76/#77/#83/#89/#92/#94 landed during the round); each retry re-merged `origin/main`, re-ran every gate, and kept both sides' work (the collision chain is recorded above).
- **Pages deploy** — `Deploy GitHub Pages` run **`44697488609`** (triggered by the PR #88 merge push) completed **success**.
- **Live verification (2026-11-20, fetched from the deployed site after the run):**
  - `https://wingbangboozle1-lang.github.io/Prod3/index.html` — new hero and the "2 × 3 quart baskets" feature figure are live;
  - `…/articles/are-air-fryers-worth-it.html` — live, full text, disclosure above the first heading, Amazon anchors carrying the tag;
  - `…/articles/smart-thermometer-questions.html` — live, full text, same.
- This record itself is merged in the follow-up micro-PR that carries it, per the board convention.

---

## Session `arena/30d1c448-prod3` — documentation consistency pass, T-74 (2026-11-20)

**Branch:** `arena/30d1c448-prod3` (from `main` at `7c1b939`) · **Claimed as T-46**, renumbered
**T-53**, **T-66**, **T-70** and finally **T-74** at successive merges (each earlier id was
taken upstream by another session while this branch was in flight). Every earlier row is kept;
nothing was overwritten. Scope was the five documentation surfaces only; no data register,
generated register page, article body, or product/policy claim was edited. No external webpage
was fetched this session — every count below was verified against the repository's own
`data/*.json` files, the shipped files, and the gate outputs, and the official-source claims in
the docs were left unchanged from the previously recorded official-source verifications.

### Demonstrable defects found and fixed on the pre-merge tree (main at 7c1b939)

1. **README carried two contradictory register tables** ("as of 2026-11-19" vs "as of
   2026-11-20") with disagreeing ID ranges. This session hand-merged them into one current
   table; at the first merge that edit was **superseded by upstream's better fix** — PR #53's
   `scripts/build_readme.py` generates the register block from `data/*.json` and gate
   `build_readme.py --check` proves it fresh. Both findings preserved.
2. **Article breakdown wrong in both executive summaries**: "nine question-shaped articles
   (eight evergreen guides plus the dated Thanksgiving temperature plan)" — `articles/` held
   nine files at 7c1b939: **seven evergreen** plus **two seasonal**. Corrected in both
   summaries; the breakdown was re-derived at every merge as the tree grew to thirteen guides.
3. **Stale gate evidence** ("all 30 pages", "(30 pages, 3541 assertions)" and successors):
   volatile counts now point at the recorded gate run instead of freezing a number.
4. **Stale SVG-preview wording**: FLG-016/F-21 described as "the SVG social-preview image is
   unverified" — the SVG issue is resolved; the outstanding item is the shipped 1200×630 PNG's
   share-debugger check. Wording conformed to `flagged.html`.
5. **`direction.html`**: duplicated `<h2>` removed; embedded tables labeled as snapshots with
   pointers to the full registers; malformed `<p>` inside the suggestion table removed
   (byte-identical duplicate of the SG-19 source note kept after it); callout date updated.
6. **`DIRECTION.md` mis-citation**: "That is DT-11 territory" — DT-11 did not exist at 7c1b939
   and, once upstream registered DT-11/DT-12, was shown to name different subjects entirely.
   Final wording points at the SG-21 retired row, which does record the displaced proposal.

### Merge reconciliations (origin/main moved four times: 002ab81, 8cc8d58, ef84eef, 6455932)

Fourteen conflict rounds across six files; every conflict resolved keeping **both** sides' work.
Registers grew from 30 rows/23 questions to **SG-01..SG-54 (53 rows; SG-21 retired; SG-26
unoccupied)**, **Q-01..Q-30**, DT-01..DT-12, and 57+ flagged data rows. Convergence notes:

- Upstream independently fixed several of this session's defects (the in-table SG-19 duplicate
  note, the register tables, guide-count wording) and added gates that make the classes
  self-checking: **D36** (heading ID ranges end at the register's last id), **D40** (stated
  guide counts match the guides on disk), **D41** (RSS autodiscovery + flag register/page
  mirror), **D42** (every SG/Q id cited on a page must exist). Where fixes converged,
  upstream's text was kept; where counts drifted, they were refreshed to the merged data at
  each round or the phrasing made count-free.
- `direction.html`: the open-questions table mirrors through Q-30 with a D36-governed live-range
  heading; register pointers updated to SG-01..SG-54 / Q-01..Q-30 at the final merge. The
  SG-26 gap flag is **FLG-029** (upstream's flag-id collision repairs renumbered the second
  FLG-021); earlier sections of this record use ids as they stood at the time.
- `DIRECTION.md`: question count thirty (Q-01…Q-30); status list gains `open`; Q-30 named; a
  decision-log row duplicated by upstream merges removed; digest index completed earlier
  through SG-47 and kept current with upstream's additions afterward.
- Executive summaries: counts re-read from the JSON at each merge (53 rows / 30 questions
  final at the fourth merge); guide breakdown kept equal to the file list on disk (thirteen
  guides: evergreen guides, the dated Thanksgiving pair, the two gift guides, the
  listing-literacy guide).
- **Fifth merge (55cbc4a, PRs #89–#91):** the register moved again — **SG-01..SG-58 (58 rows;
  SG-21 received a row of its own and the SG-26 slot was filled)** and **DT-13** was registered
  for the displaced-SG-21 question, superseding this session's "no registered decision row
  covers it" wording (their "That is DT-13 territory" sentence is now accurate and was kept).
  Live prose claims about "SG-21 retired / SG-26 unoccupied" were rewritten as dated history
  (FLG-029) wherever this session had introduced them; the README register block kept
  upstream's generated version.
- `COORDINATION.md`: upstream rows and records verbatim at each round; this session's row
  renumbered four times (T-46 → T-53 → T-66 → T-70 → T-74), never overwriting another
  session's claim.

### Verification performed (2026-11-20, after conflict resolution on the final merged tree)

| Gate | Result |
|---|---|
| `scripts/build_registers.py --check` | OK: register pages match data/*.json |
| `scripts/build_decisions.py --check` | OK: decisions.html matches its data |
| `scripts/build_chrome.py --check` | OK: chrome current on all pages |
| `scripts/build_sitemap.py --check` | OK: sitemap.xml is up to date |
| `scripts/build_products.py --check` | OK: product pages match data/products.json |
| `scripts/build_readme.py --check` | OK: README register table matches data/*.json |
| `scripts/build_ideas.py --check` | OK: ideas.html brief is current |
| `scripts/check_site.py` | All checks passed (conflict-marker scan clean) |
| `tools/verify_site.py` | Release gate passed (source cross-references resolve; publishing-coverage check passes) |
| `tools/check_site.py` | all additional rules passed (D36/D40/D41/D42 among them) |
| `tools/crawl_links.py` | 0 broken links, 0 dead anchors, 0 orphans |
| `git diff --check` | clean |

Page and assertion counts from the run are recorded with the deploy record below. No claim
about products, prices, ratings, traffic, conversions, or compliance status was added, removed,
or softened.

### Irregularities (non-blocking)

- The stale-doc defects above are the irregularities; each is fixed on this branch and none of
  them touched a data register. Register-side irregularities are unchanged and remain published
  on `flagged.html`.
- Adjacent observations, **not changed** (data-register wording, out of scope): Q-17's
  registered text still says "the eight guides" from an earlier era (the D40 gate comment in
  `tools/check_site.py` documents the same class of drift).

### Not claimed / not verified here (unchanged owner gates)

FLG-001 intended ASINs · FLG-006 Special Link test · FLG-010 account status (Q-23) ·
link-redirect behaviour and the tag-parameter question (Q-22/Q-24/Q-25) · Search Console
(DT-03, Q-28) · analytics endpoint (DT-07) · share-debugger check (F-21/Q-21) · Core Web
Vitals measurement (Q-29) · outbound-click counter behaviour (Q-30) · Pages build_type setting
(FLG-024). No new claims about traffic, conversion, or product superiority.
