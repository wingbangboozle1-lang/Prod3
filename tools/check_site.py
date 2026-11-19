#!/usr/bin/env python3
"""
Additional release gate for Kitchen Counter. Zero dependencies, runs from a
clean checkout and in CI.

This complements scripts/check_site.py and tools/verify_site.py rather than
replacing them. Those two cover structure, disclosure presence, sitemap
coverage and the release artefacts. This file covers the rules that were
missing, each of which a real defect slipped past recently:

  * currency amounts  — a price block was published in v1 while the site's own
    policy page said price display requires Amazon-served data. Now a failure.
  * sponsored coverage — the check used to look only at link.amazon links, so
    evidence links to amazon.com/dp/<ASIN> and to the Associates help pages
    sailed through unqualified. 42 anchors were affected; all are fixed, and
    this rule keeps them fixed.
  * duplicate descriptions, placeholder text, fake-experience phrasing,
    non-descriptive link text, and heading structure.

Run:  python3 tools/check_site.py     (exit 0 = pass, 1 = fail, 2 = no site)
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."

failures = []
checks_run = 0


def check(rule, condition, detail):
    global checks_run
    checks_run += 1
    if not condition:
        failures.append((rule, detail))


if not (ROOT / "index.html").exists():
    print("no site found — run this from the repository root after checkout")
    sys.exit(2)

pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "articles").glob("*.html"))
docs = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in pages}

titles, descs = {}, {}

for name, html in docs.items():

    # ---- disclosure: present, and above the first <h1>
    check("P01-disclosure", DISCLOSURE in html, f"{name}: disclosure sentence missing")
    if DISCLOSURE in html:
        first_disc = html.find(DISCLOSURE)
        first_h1 = html.find("<h1")
        check("P01-disclosure-position",
              0 <= first_disc < (first_h1 if first_h1 != -1 else len(html)),
              f"{name}: disclosure sits below the first h1")

    # ---- footer repeat
    check("P02-disclosure-footer", html.count(DISCLOSURE) >= 2,
          f"{name}: disclosure is not repeated in the footer")

    # ---- exactly one h1
    h1s = re.findall(r"<h1[\s>]", html)
    check("P03-single-h1", len(h1s) == 1, f"{name}: {len(h1s)} h1 elements")

    # ---- title and description, collected for the uniqueness pass
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    check("P04-title", bool(t) and len(t.group(1).strip()) > 12, f"{name}: missing or trivial title")
    check("P05-description", bool(d) and len(d.group(1).strip()) > 50,
          f"{name}: missing or thin meta description")
    if t:
        titles.setdefault(t.group(1).strip(), []).append(name)
    if d:
        descs.setdefault(d.group(1).strip(), []).append(name)

    # ---- canonical present and absolute
    check("P06-canonical", 'rel="canonical"' in html and "https://" in html.split('rel="canonical"')[1][:200],
          f"{name}: no absolute canonical URL")

    # ---- every Amazon anchor is sponsored AND opens a new tab
    for tag in re.findall(r"<a\b[^>]*>", html):
        if "amazon.com" not in tag:
            continue
        href = re.search(r'href="([^"]*)"', tag)
        check("P07-sponsored", "sponsored" in tag,
              f"{name}: Amazon link without rel=sponsored → {href.group(1) if href else '?'}")
        check("P08-noopener", "noopener" in tag,
              f"{name}: Amazon link without noopener → {href.group(1) if href else '?'}")
        if href:
            check("P09-no-shortener",
                  "link.amazon/" not in href.group(1) or "sponsored" in tag,
                  f"{name}: shortened link qualifier missing → {href.group(1)}")

    # ---- no currency amount, anywhere
    for m in re.finditer(r"[$£€]\s?\d", html):
        snippet = html[max(0, m.start() - 50):m.end() + 25].replace("\n", " ")
        check("P10-no-price", False, f"{name}: currency amount → …{snippet}…")

    # ---- no promotional or availability claim
    for pat in (r"\b\d+%\s*(?:off|savings)\b", r"\bBlack Friday\b", r"\bPrime Day\b",
                r"\b(?:free delivery|delivery by|arrives by|get it as soon as)\b",
                r"\b(?:coupon|voucher|promo code)\b"):
        m = re.search(pat, html, re.I)
        check("P11-no-promo", not m, f"{name}: {m.group(0) if m else ''}")

    # ---- no first-hand experience claim
    for pat in (r"\bwe tested\b", r"\bin our testing\b", r"\bwe found\b",
                r"\bwhen we used\b", r"\bour unit\b", r"\bafter \w+ months of use\b"):
        m = re.search(pat, html, re.I)
        check("P12-no-fake-experience", not m, f"{name}: {m.group(0) if m else ''}")

    # ---- no placeholders left behind
    for pat in (r"\bTODO\b", r"\bFIXME\b", r"lorem ipsum", r"\bXXX\b"):
        m = re.search(pat, html, re.I)
        check("P13-no-placeholders", not m, f"{name}: {m.group(0) if m else ''}")

    # ---- link text must describe its destination
    for m in re.finditer(r'<a\b[^>]*href="(https?://[^"]*)"[^>]*>(.*?)</a>', html, re.S):
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        check("P14-link-text", text.lower() not in ("click here", "here", "read more", "link"),
              f"{name}: non-descriptive link text {text!r} → {m.group(1)[:60]}")

    # ---- internal targets exist on disk
    for target in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', html):
        if target.startswith(("http", "mailto:", "data:", "//")):
            continue
        resolved = (ROOT / name).parent / target
        check("P15-internal-links", resolved.exists(),
              f"{name}: broken internal target → {target}")

# ---- cross-page uniqueness
for t, names in titles.items():
    check("P16-unique-titles", len(names) == 1, f"duplicate title {t!r} on {names}")
for d, names in descs.items():
    check("P17-unique-descriptions", len(names) == 1, f"duplicate description on {names}")

# ---- data integrity: intent and observation must stay apart
products = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))["products"]
check("D01-five-products", len(products) == 5, f"{len(products)} products in the register")
for p in products:
    check("D02-observed-present", bool(p.get("observed_asin")), f"{p['id']}: no observed ASIN")
    check("D03-token-not-an-asin", p.get("token_is_asin") is False,
          f"{p['id']}: a 9-character token was recorded as an ASIN")
    check("D04-not-merged", p.get("submitted_token") != p.get("observed_asin"),
          f"{p['id']}: intended token and observed ASIN were merged into one field")

# ---- the ledger must stay empty until a real report exists
ledger = json.loads((ROOT / "data" / "campaign-ledger.json").read_text(encoding="utf-8"))
rows = ledger.get("rows", [])
check("D05-ledger-empty", rows == [], f"ledger holds {len(rows)} rows with no first-party report behind them")

# ---- report
print(f"{len(docs)} pages checked, {checks_run} assertions run")
if failures:
    print(f"\n{len(failures)} FAILURES\n")
    for rule, detail in failures[:60]:
        print(f"  [{rule}] {detail}")
    sys.exit(1)

print("all additional rules passed")
sys.exit(0)
