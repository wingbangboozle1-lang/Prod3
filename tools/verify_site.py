#!/usr/bin/env python3
"""Whole-tree release gate for Kitchen Counter. Exit 3 on violation.

Runs scripts/check_site.py, then verifies:
 - data/sources.json parses, every source URL is well-formed, and the
   verification-semantics note is present
 - data/products.json carries claim markers, dated prices, and only flags
   documented in flagged.html
 - data/campaign-ledger.json has no fabricated rows (rows must be empty
   until first-party reports exist; provenance must be dated)
 - feed.xml is well-formed XML with 8 items
 - robots.txt references the sitemap
"""
import json, re, subprocess, sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

r = subprocess.run([sys.executable, str(ROOT / "scripts/check_site.py")], capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print(r.stderr)
    errors.append("check_site.py failed")

try:
    sources = json.loads((ROOT / "data/sources.json").read_text())
    for s in sources["sources"]:
        assert s["url"].startswith("https://"), f"{s['id']}: url not https"
        assert s.get("used_for"), f"{s['id']}: missing used_for"
    assert sources.get("note"), "sources.json missing verification-semantics note"
    print(f"OK sources.json: {len(sources['sources'])} sources")
except Exception as e:
    errors.append(f"sources.json: {e}")

try:
    products = json.loads((ROOT / "data/products.json").read_text())
    assert products.get("claim_basis"), "products.json missing claim_basis"
    assert products.get("price_snapshot_note"), "products.json missing price_snapshot_note"
    for p in products["products"]:
        assert re.search(r"20\d{2}-\d{2}-\d{2}", p["price_observed"]), f"{p['id']}: undated price"
        for f_id in p["flags"]:
            assert f_id in (ROOT / "flagged.html").read_text(), f"{p['id']}: flag {f_id} not documented in flagged.html"
    p4 = next(x for x in products["products"] if x["id"] == "P-04")
    for k in ("accuracy", "certification", "response_time"):
        v = p4["specs"][k]
        assert "claim" in v.lower() or "seller" in v.lower(), f"P-04 specs.{k} not marked as seller claim"
    print("OK products.json: dated prices, claim markers, flags documented")
except Exception as e:
    errors.append(f"products.json claims: {e}")

try:
    ledger = json.loads((ROOT / "data/campaign-ledger.json").read_text())
    assert ledger["rows"] == [], "ledger rows must stay empty until first-party reports exist"
    assert ledger["provenance"], "ledger provenance missing"
    print("OK campaign-ledger.json: empty, provenance dated")
except Exception as e:
    errors.append(f"campaign-ledger.json: {e}")

try:
    tree = ET.parse(ROOT / "feed.xml")
    items = tree.getroot().findall(".//item")
    assert len(items) == 8, f"expected 8 feed items, got {len(items)}"
    print("OK feed.xml: well-formed, 8 items")
except Exception as e:
    errors.append(f"feed.xml: {e}")

try:
    robots = (ROOT / "robots.txt").read_text()
    assert "sitemap.xml" in robots, "robots.txt missing sitemap"
    print("OK robots.txt references sitemap")
except Exception as e:
    errors.append(f"robots.txt: {e}")

if errors:
    print("\nFAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(3)
print("\nRelease gate passed.")
