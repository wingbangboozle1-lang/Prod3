# Shopwise Kitchen Desk

An affiliate publication about air fryers and cooking thermometers, built as a static site and
published from this repository's `main` branch at
**https://wingbangboozle1-lang.github.io/Prod3/**.

It is not a "best air fryers 2026" list. It is five specific Amazon listings, read against their own
specification sheets on a stated date, with every gap and contradiction published rather than
papered over.

## The five products

| ID | Product | ASIN | Supplied link resolved |
| --- | --- | --- | --- |
| P1 | CHEFMAN 6 Quart Dual Basket Air Fryer Oven | `B0CDY277D3` | ✔ `link.amazon/B04G1MEwY` |
| P2 | Emeril Lagasse 26QT French Door Air Fryer Toaster Oven | `B09B7SB46R` | ✔ `link.amazon/B02NbDxp3` |
| P3 | Chefman Air Fryer 8 Qt TurboFry 4-in-1 | `B08DKYBTPH` | ✔ `link.amazon/B00hJ57DV` |
| P4 | ThermoMaven 1 Sec Professional Digital Meat Thermometer | `B0DHZTCNR5` | ✔ `link.amazon/B0c8moW59` |
| P5 | CHEF iQ Sense Smart Wireless Meat Thermometer (3 probes) | `B0DZFD6R9Z` | ✔ `link.amazon/B0f3GKalj` |

The site links to `https://www.amazon.com/dp/<ASIN>` directly, with `rel="sponsored noopener"`. It
never publishes a shortened link, because a reader should never have to guess where a click goes.

## What is here

```
index.html …              generated pages — do not hand-edit, they are build output
build.py                  the generator (no dependencies, Python 3.8+)
tools/check_site.py       the gate — 4,800+ assertions, exit 1 on any failure
assets/                   style.css, app.js — hand-written, no framework
data/                     the verified source of truth
  products.json             every published value, with its source and capture date
  sources.json              19 registered sources, primary vs supplied
  verification.json         intended ASIN vs observed redirect, kept separate
  policy-checks.json        14 compliance checks
  flagged.json              20 unresolved items
  suggestions.json          14 decisions with their alternatives
  open-questions.json       17 open questions with a way to answer each
  analysis.json             the counter-space arithmetic
  campaigns.json            the campaign ledger — empty on purpose
content/                  editorial content
  VOICE.md                  the style rules, written before the guides
  guides.json               8 question-shaped guides
  reviews.json              5 product pages, specification-led
  categories.json           2 category hubs
  measurement.json          the measurement policy page
.github/workflows/        runs the same gate in CI
COORDINATION.md           the shared task board for parallel sessions
```

## Build and verify

```bash
python3 build.py                     # regenerate every page, the sitemap, the feed
python3 tools/check_site.py          # run the gate; exits 1 on any failure
```

There is nothing to install. The build is deterministic: running it twice produces a byte-identical
tree, which is what CI asserts.

## What the gate refuses to ship

Each rule below maps to a promise made on `/about/` and `/dashboard/gate.html`.

- A page without the Amazon Associates disclosure sentence, or with it below the first `<h1>`.
- A page whose footer does not repeat the disclosure.
- An Amazon link without `rel="sponsored"`, or one pointing at a shortened URL.
- A currency amount, a price pattern, a promotional discount phrase, or a delivery estimate.
- First-person testing language (`we tested`, `in our testing`, `our unit`).
- A duplicate `<title>` or meta description.
- A page without exactly one `<h1>`.
- A broken internal link, or an internal URL that skips the project path.
- A specification value with no source in the register, or a blank with no flag explaining it.

## The three registers that matter

**Intended vs observed.** `data/products.json` stores `intended.asin` (a decision, with a
confirmation date and the source it came from) and `observed.resolved_asin` (an observation, with
the date it was fetched) in separate fields. They are never merged, and a disagreement becomes a
flagged item rather than an overwrite.

**Sources.** Every claim resolves to an entry in `data/sources.json`, tagged `primary` (the
authoritative body itself) or `supplied` (owner-provided, not independently corroborated).

**Flags.** Anything that could not be confirmed, or that conflicts, is published at
`/dashboard/flagged.html` with a severity, a source and an action. A flag is not a failure; it is the
difference between a site that says "I don't know" and one that quietly makes something up.

## What this site does not do

- It does not claim to have tested anything. No unit has been handled.
- It does not show prices or availability. Amazon's Program Policies permit that only when Amazon
  serves the data or it arrives via the Product Advertising API.
- It does not publish traffic, conversion or revenue figures. No first-party report has been read,
  so the ledger is empty and stays empty until one is.
- It does not call the supplied short links invalid. Their status in the enrolled Associates workflow
  is unresolved, and `Q-04` records how to settle it.

## Local preview

```bash
python3 -m http.server 8000
# → http://localhost:8000/
```

Because the site is served from the repository root with root-relative links, a plain static server
in the repository root is a faithful preview of the published site.

## Contributing

Read `COORDINATION.md` first. It is the shared task board: claim a task and a file scope before you
edit, keep scopes non-overlapping, and never mark anything verified without an official source link.
Generated pages are owned by the build; change `data/`, `content/`, `assets/` or `build.py` and
regenerate.
