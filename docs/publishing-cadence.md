# Publishing cadence and per-guide checklist

Status: **set 2026-11-20** (decision DT-10 in `data/decisions.json`, recorded in `DIRECTION.md`).
Set on the owner's instruction in the 2026-11-20 brief ("Set a publishing cadence"), recorded by session `arena/2cd3bab9-prod3` (task T-48).

## The cadence

- **One guide per calendar month.** Each guide is question-shaped. Monthly is the commitment; the site does not promise more.
- **Approver:** the site owner. The owner approves each guide before it is merged. The named-author question is still open (Q-05), so guides are published under the site's name, not a person's.
- **Next guide due:** 2026-12-31 (the December 2026 slot). If a slot is missed, record the miss in the next board entry; do not back-date a guide.
- **Documented exception, 2026-11-20:** three guides were published on one day — `how-to-read-a-product-listing`, `check-your-thermometer-at-home` and `thanksgiving-leftovers-air-fryer`. Two exist because the calendar forced them (a Thanksgiving reheating guide is worthless a week late, and the probe check is the companion a reader needs before Thursday); the third explains the site's own method to its readers, which is worth doing while the pre-holiday window is open. The monthly default resumes at the December slot. The batch is recorded here rather than hidden, and each guide carries its true publication date of 2026-11-20.
- **Overlap with `data/editorial-plan.json`:** the plan's 2026-11-23 slot is served by the published Thanksgiving temperature plan, and the 2027-02-15 slot ("wireless probe or instant-read: which fails first in a cold snap") should be re-scoped before writing, because the ice-water guide now answers the part of it that can be answered from official sources.

This is a publishing rhythm, not a forecast. It makes no claim about traffic, search ranking, clicks, conversions or revenue. No such figure is published anywhere on the site.

## How the next topic is chosen

1. Until Search Console is verified by the owner (DT-03, Q-18), topics come from the open-questions register (`questions.html`) and the buyer questions the existing guides leave unanswered. The four working titles in the brief are already published as guides.
2. After Search Console is verified, topics come from measured queries (SG-18). The campaign ledger stays empty until authorized first-party reports exist (`data/campaign-ledger.json`).
3. A topic must be answerable from dated official sources and the dated listing snapshots already in `data/products.json`. If it cannot be, it goes on the questions register, not into a guide.

## Per-guide checklist

Each new guide needs all of these before it is merged. The release gate (`tools/verify_site.py`) checks items 3 to 5 and fails the build if any is missing.

1. Write `articles/<slug>.html` with the shared chrome (`python3 scripts/build_chrome.py`), a unique `<title>` and meta description, a canonical link, and JSON-LD with `datePublished` and `dateModified`.
2. Mark every outbound product link `rel="sponsored"`. Official reference links (NIST, USDA, FTC, Google, Amazon policy pages) are not affiliate links and stay unmarked.
3. Add the guide to `sitemap.xml`: `python3 scripts/build_sitemap.py`, then `--check`.
4. Add a feed item to `feed.xml`. Its `<title>` must equal the guide's H1; the gate fails otherwise. Its description is a short editorial summary.
5. Link the guide from the guides hub, `buying-guide.html`, in the cluster that fits it.
6. Run the gates listed in `README.md` (freshness checks, `scripts/check_site.py`, `tools/verify_site.py`, `tools/check_site.py`, `tools/crawl_links.py`).
7. Open a pull request into `main`, record the change on `COORDINATION.md`, and confirm the `Deploy GitHub Pages` run and the live URL.

## Limits

- No prices, customer ratings or review counts appear in a guide (`docs/verification.md`).
- Every figure traces to a dated official listing snapshot or an official policy page. A value that cannot be traced is left out and flagged on `flagged.html`.
- The site's disclosure strip stays above the masthead on every page, including new guides (`disclosure.html`).
