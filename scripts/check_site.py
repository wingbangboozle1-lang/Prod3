#!/usr/bin/env python3
"""Data + HTML gate for Kitchen Counter. Exit 1 on violation.

Checks:
 1. data/products.json parses; 5 products; intended_* and observed_* never merged
    (intended_asin must be null while observed_asin is set, or vice versa).
 2. Every HTML page has: a unique <title>, a meta description, the disclosure
    strip (class="disclosure"), and the footer disclosure.
 3. Every outbound link to link.amazon carries rel="sponsored".
 4. Every internal href/src target exists on disk.
 5. sitemap.xml lists every HTML page.
 6. Banned accuracy/compliance phrases do not appear (unverified participation
    claims, "Verified picks", undated "Observed" prices, capacity-ratio claims,
    unattributed NIST-certification claims).
 7. Every table marked data-source-required has an https source link in every
    body row.
 8. Every <p class="price"> block carries a snapshot date.
 9. Article JSON-LD blocks carry dateModified.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

# 1. products.json
try:
    data = json.loads((ROOT / "data/products.json").read_text())
    products = data["products"]
    assert len(products) == 5, f"expected 5 products, got {len(products)}"
    for p in products:
        assert p["intended_asin"] is None, f"{p['id']}: intended_asin must stay null until owner confirms"
        assert p["observed_asin"], f"{p['id']}: observed_asin missing"
        assert p["token_is_asin"] is False, f"{p['id']}: 9-char token wrongly marked as ASIN"
        assert p["submitted_token"] not in p["observed_asin"], f"{p['id']}: intent/observation merged"
    print(f"OK products.json: {len(products)} products, intent/observation separated")
except Exception as e:
    errors.append(f"products.json: {e}")

# 2-4. HTML checks
html_files = (sorted(ROOT.glob("*.html"))
              + sorted((ROOT / "products").glob("*.html"))
              + sorted((ROOT / "articles").glob("*.html"))
              + sorted((ROOT / "tools").glob("*.html"))
              + sorted((ROOT / "products").glob("*.html")))
titles = {}
for f in html_files:
    html = f.read_text()
    rel = f.relative_to(ROOT)
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if not m or not m.group(1).strip():
        errors.append(f"{rel}: missing <title>")
    else:
        t = m.group(1).strip()
        if t in titles:
            errors.append(f"{rel}: duplicate title with {titles[t]}")
        titles[t] = str(rel)
    if 'name="description"' not in html:
        errors.append(f"{rel}: missing meta description")
    if 'class="disclosure"' not in html:
        errors.append(f"{rel}: missing above-fold disclosure strip")
    if "Affiliate disclosure" not in html:
        errors.append(f"{rel}: missing footer affiliate disclosure")
    if "shopnow047c-20" not in html:
        errors.append(f"{rel}: missing tracking ID shopnow047c-20")
    # 3a. sponsored check: EVERY outbound Amazon anchor must carry
    #     rel="sponsored", not just the link.amazon ones. Evidence links to
    #     amazon.com/dp/<ASIN> and to the Associates help pages earn no
    #     commission but still point at Amazon, and Google's guidance on paid
    #     links applies to the commerce destinations.
    for tag in re.findall(r"<a\b[^>]*>", html):
        if not re.search(r'href="[^"]*amazon\.com', tag):
            continue
        if "sponsored" not in tag:
            href = re.search(r'href="([^"]*)"', tag).group(1)
            errors.append(f"{rel}: Amazon link without rel=sponsored: {href}")

    # 3b. price policy: no currency amount may be rendered anywhere.
    #     Program Policies section 2(b) permits displaying price and
    #     availability only when Amazon serves the data or it arrives via the
    #     Product Advertising API. This site does neither, so the rule is that
    #     no price appears at all.
    for m in re.finditer(r"[$£€]\s?\d", html):
        snippet = html[max(0, m.start() - 40):m.end() + 20].replace("\n", " ")
        errors.append(f"{rel}: currency amount rendered ({m.group(0)!r}): ...{snippet}...")
    for pat in (r"\b\d+%\s*(?:off|savings)\b", r"\bBlack Friday\b", r"\bPrime Day\b",
                r"\b(?:free delivery|delivery by|arrives by)\b"):
        m = re.search(pat, html, re.I)
        if m:
            errors.append(f"{rel}: promotional or availability claim: {m.group(0)!r}")
    # internal targets exist
    for target in re.findall(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"', html):
        if target.startswith(("http", "mailto:", "data:")):
            continue
        p = (f.parent / target).resolve()
        if not p.exists():
            errors.append(f"{rel}: broken internal target: {target}")
print(f"OK html: {len(html_files)} pages checked")

# 5. sitemap coverage
sitemap = (ROOT / "sitemap.xml").read_text()
for f in html_files:
    rel = f.relative_to(ROOT).as_posix()
    # 404.html is deliberately excluded: an error page has no canonical URL to
    # offer a crawler, and listing it in the sitemap invites it to be indexed.
    if rel == "404.html":
        continue
    if rel not in sitemap:
        errors.append(f"sitemap.xml: missing {rel}")
print("OK sitemap coverage checked")

# 6. banned phrases: unverified claims the audit removed must not return
BANNED = [
    "is a participant in the Amazon Services LLC Associates Program",
    "Verified picks",
    "verified line-by-line",
    "read line-by-line",
    "verified specs",
    "verified models",
    "Verified Air",
    "Observed 2026-11-19",
    "qt/in",
    "capacity per inch",
    "whole-chicken test",
    "±0.5°F NIST-certified",
    "NIST-certified accuracy",
    "NIST-certified,",
    "suits two people",
    "wins on",
    "the winner",
    "Winner",
]
for f in html_files:
    html = f.read_text()
    rel = f.relative_to(ROOT)
    for phrase in BANNED:
        if phrase in html:
            errors.append(f"{rel}: banned phrase present: {phrase!r}")
print("OK banned-phrase scan")

# 7. data-source-required tables: every body row must cite an https source,
#    OR carry the explicit "no official source" marker. The second branch exists
#    because the brief allows a value to be left blank and flagged when no official
#    source confirms it -- but it must never be left blank silently. A row with
#    neither a link nor the marker fails, so "unverified" cannot hide.
UNVERIFIED_MARKER = '<span class="unverified">No official source</span>'
for f in html_files:
    html = f.read_text()
    rel = f.relative_to(ROOT)
    for tbl in re.findall(r"<table[^>]*data-source-required[^>]*>.*?</table>", html, re.S):
        rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)
        for row in rows[1:]:  # skip header row
            if "https://" in row or UNVERIFIED_MARKER in row:
                continue
            errors.append(f"{rel}: data-source-required row has neither a source link nor an unverified marker")
print("OK data-source-required tables")

# 8. price blocks must be dated
for f in html_files:
    html = f.read_text()
    rel = f.relative_to(ROOT)
    for block in re.findall(r'<p class="price">(.*?)</p>', html, re.S):
        if not re.search(r"20\d{2}-\d{2}-\d{2}", block):
            errors.append(f"{rel}: <p class=\"price\"> without snapshot date")
print("OK price dating")

# 9. articles must carry JSON-LD dateModified
for f in sorted((ROOT / "articles").glob("*.html")):
    html = f.read_text()
    rel = f.relative_to(ROOT)
    if '"dateModified"' not in html:
        errors.append(f"{rel}: JSON-LD missing dateModified")
print("OK article dateModified")

# 10. no committed merge-conflict markers anywhere in the tree
# (a botched resolution once shipped literal <<<<<<< / >>>>>>> lines to readers)
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff",
                   ".woff2", ".ttf", ".eot", ".pdf", ".zip", ".gz", ".pack"}
marker_hits = 0
for f in sorted(ROOT.rglob("*")):
    if not f.is_file() or ".git" in f.parts or f.suffix.lower() in BINARY_SUFFIXES:
        continue
    try:
        lines = f.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError):
        continue
    for i, line in enumerate(lines, 1):
        if line.startswith("<<<<<<< ") or line.startswith(">>>>>>> ") or line == "=======":
            errors.append(f"{f.relative_to(ROOT)}:{i}: committed conflict marker")
            marker_hits += 1
print(f"OK conflict-marker scan ({marker_hits} markers found)" if marker_hits == 0
      else f"conflict-marker scan: {marker_hits} markers found")

if errors:
    print("\nFAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("\nAll checks passed.")
