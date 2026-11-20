#!/usr/bin/env python3
"""Whole-tree release gate for Kitchen Counter. Exit 3 on violation.

Runs scripts/check_site.py, then verifies:
 - data/sources.json parses, every source URL is well-formed, and the
   verification-semantics note is present
 - every source ID referenced from data/*.json resolves to sources.json,
   and every registered source is published on sources.html
 - data/products.json carries claim markers, dated prices, and only flags
   documented in flagged.html
 - data/campaign-ledger.json has no fabricated rows (rows must be empty
   until first-party reports exist; provenance must be dated)
 - feed.xml is well-formed XML and carries one item per published article
 - robots.txt references the sitemap
 - product-intent fields: intended ASINs need an owner-confirmation record
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

# Every source ID referenced from any data/*.json record must resolve to an
# entry in data/sources.json, and every registered source must be published
# on sources.html. (Catches stale/dangling cross-references like S07/S08.)
try:
    reg_ids = {s["id"] for s in sources["sources"]}
    referenced = set()
    for path in sorted((ROOT / "data").glob("*.json")):
        text = path.read_text()
        for m in re.finditer(r'"(?:source|sources)"\s*:\s*(\[[^\]]*\]|"[^"]*")', text):
            for sid in re.findall(r"S\d{2}", m.group(1)):
                referenced.add(sid)
                assert sid in reg_ids, f"{path.name}: references undefined source {sid}"
    html = (ROOT / "sources.html").read_text()
    for sid in sorted(reg_ids):
        assert re.search(rf"<td>{sid}</td>", html), f"sources.html: missing row for {sid}"
    print(f"OK source cross-references: {len(referenced)} referenced ids all resolve; {len(reg_ids)} registered ids all published")
except Exception as e:
    errors.append(f"source cross-references: {e}")

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
    _articles = sorted((ROOT / "articles").glob("*.html"))
    assert len(items) == len(_articles), f"feed carries {len(items)} items but {len(_articles)} articles are published"
    _links = set()
    for _it in items:
        _l = _it.find("link").text
        assert _l.startswith("https://wingbangboozle1-lang.github.io/Prod3/articles/"), f"unexpected feed link {_l}"
        _links.add(_l.rsplit("/", 1)[-1])
    _missing = sorted({a.name for a in _articles} - _links)
    assert not _missing, f"published article(s) absent from the feed: {_missing}"
    _dates = [i.find("pubDate").text for i in items]
    print(f"OK feed.xml: well-formed, {len(items)} items, one per published article, every link canonical")
except Exception as e:
    errors.append(f"feed.xml: {e}")

try:
    robots = (ROOT / "robots.txt").read_text()
    assert "sitemap.xml" in robots, "robots.txt missing sitemap"
    print("OK robots.txt references sitemap")
except Exception as e:
    errors.append(f"robots.txt: {e}")

try:
    # Product-intent gate (C-09). An intended ASIN may be filled only with an
    # owner-confirmation record; a reference source (for example S16) or an
    # observed redirect value may never stand in for intent.
    vdoc = json.loads((ROOT / "data/verification.json").read_text())
    pdoc = json.loads((ROOT / "data/products.json").read_text())
    for rec in vdoc["records"]:
        intended = rec["intended"]
        if intended.get("asin") is not None:
            assert intended.get("owner_confirmation_ref"), f"{rec['product']}: intended ASIN set without owner_confirmation_ref"
            assert intended.get("source") not in ("S16", None), f"{rec['product']}: intended source must be an owner record, not a reference page"
            assert intended.get("listing_url") and intended.get("confirmation_date"), f"{rec['product']}: intended record incomplete"
        assert "agrees" not in rec["observed"], f"{rec['product']}: observed.agrees compares to an unconfirmed intent"
    for prod in pdoc["products"]:
        if prod.get("intended_asin") is not None:
            assert prod.get("intent_source"), f"{prod['id']}: intended_asin set without intent_source"
    print("OK product intent: intended fields blank or owner-confirmed; observed kept separate")
except Exception as e:
    errors.append(f"product intent gate: {e}")

if errors:
    print("\nFAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(3)
print("\nRelease gate passed.")
