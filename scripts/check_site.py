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
html_files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "articles").glob("*.html"))
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
    # sponsored check: every link.amazon <a> tag must carry rel="sponsored"
    for tag in re.findall(r"<a\b[^>]*>", html):
        m = re.search(r'href="(https://link\.amazon/[^"]*)"', tag)
        if m and "sponsored" not in tag:
            errors.append(f"{rel}: link.amazon link without rel=sponsored: {m.group(1)}")
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
    if rel not in sitemap:
        errors.append(f"sitemap.xml: missing {rel}")
print("OK sitemap coverage checked")

if errors:
    print("\nFAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("\nAll checks passed.")
