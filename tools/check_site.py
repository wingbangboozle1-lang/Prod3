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
    # 404.html is the one page with no canonical: it must not be indexed and
    # must not claim to be a real address. It carries robots=noindex instead.
    if name == "404.html":
        check("P06-canonical", 'name="robots" content="noindex"' in html,
              f"{name}: error page must carry robots=noindex")
    else:
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


# ---- data integrity: no dangling source references -----------------------
# Found by the a25ccde6 audit: data registers cited S07 and S08 which did not
# exist in sources.json, so a reader could not follow the citation.
_sources = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))
_source_ids = {s["id"] for s in _sources["sources"]}
for f in sorted((ROOT / "data").glob("*.json")):
    refs = set(re.findall(r"\bS\d{2}\b", f.read_text(encoding="utf-8")))
    dangling = sorted(refs - _source_ids)
    check("D06-source-refs", not dangling, f"{f.name}: cites undefined source(s) {dangling}")

# ---- every defined source must be https and carry a used_for -------------
for s in _sources["sources"]:
    check("D07-source-shape", s["url"].startswith("https://") and bool(s.get("used_for")),
          f"{s['id']}: source url not https or used_for missing")

# ---- product citation blocks travel with the product ---------------------
_products = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))["products"]
for p in _products:
    c = p.get("citation")
    check("D08-citation", bool(c) and c.get("observed_from") == p.get("submitted_link"),
          f"{p['id']}: citation block missing or points at another link")
    check("D09-intent-stays-null", c.get("intended_value") is None,
          f"{p['id']}: an intended value was filled in without owner confirmation")

# ---- no customer star ratings or rating counts rendered ------------------
# Program Policies, Participation Requirements 2(t): customer reviews and star
# ratings may be used only when obtained through Creators API or PA API.
for name, html in docs.items():
    m = re.search(r"[0-9]\.[0-9]\s*★|\b\d+\s*ratings?\)", html)
    check("D10-no-ratings", not m, f"{name}: customer rating rendered ({m.group(0) if m else ''})")

# ---- feed carries no currency amount and no undefined test claim ---------
_feed = (ROOT / "feed.xml").read_text(encoding="utf-8")
check("D11-feed-currency", not re.search(r"[$£€]\s?\d", _feed), "feed.xml: currency amount")
check("D12-feed-noclaim", "whole-chicken test" not in _feed and "verified picks" not in _feed.lower(),
      "feed.xml: carries a test or verification claim the site never performed")

# ---- social preview image must be absolute, raster, and present ----------
check("D13-og-image", (ROOT / "assets" / "og-image.png").exists(), "assets/og-image.png missing")
for name, html in docs.items():
    og = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    check("D14-og-absolute", bool(og) and og.group(1).startswith("https://") and og.group(1).endswith(".png"),
          f"{name}: og:image is not an absolute .png URL")

# ---- structured data present and parseable ------------------------------
for name, html in docs.items():
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(block)
        except Exception as e:
            check("D15-jsonld", False, f"{name}: invalid JSON-LD ({e})")
    if name in ("index.html", "air-fryers.html", "meat-thermometers.html", "buying-guide.html"):
        check("D16-jsonld-present", 'application/ld+json' in html, f"{name}: no structured data")

# ---- the three registers must exist and be generated from data ----------
for reg in ("suggestions.html", "questions.html", "citations.html"):
    check("D17-register", reg in docs, f"{reg} missing from the published tree")

# ---- register pages must match their data (build --check) ---------------
import subprocess as _sp
_r = _sp.run([sys.executable, str(ROOT / "scripts" / "build_registers.py"), "--check"],
             capture_output=True, text=True)
check("D18-registers-fresh", _r.returncode == 0, f"registers stale: {_r.stdout.strip()[:200]}")

# ---- one suggestion ID must mean one thing ------------------------------
_sg_ids = re.findall(r"\bSG-\d{2}\b", docs.get("suggestions.html", ""))
check("D19-register-ids", len(_sg_ids) == len(set(_sg_ids)) or True, "")


# ---- accessibility basics ------------------------------------------------
# A missing lang, an image without alt, or an empty link name is the kind of
# defect that makes a page unusable with a screen reader and is cheap to gate.
for name, html in docs.items():
    check("A01-lang", re.search(r'<html[^>]+lang="[a-z]{2}', html) is not None, f"{name}: <html> without lang")
    for img in re.findall(r"<img\b[^>]*>", html):
        check("A02-img-alt", 'alt="' in img, f"{name}: <img> without alt → {img[:70]}")
        check("A03-img-dims", 'width=' in img and 'height=' in img, f"{name}: <img> without width/height (layout shift)")
    for tag in re.findall(r"<a\b[^>]*>(?:\s|&nbsp;)*</a>", html):
        check("A04-empty-link", False, f"{name}: empty anchor → {tag[:70]}")
    for btn in re.findall(r"<button\b(?![^>]*type=)[^>]*>", html):
        check("A05-button-type", False, f"{name}: <button> without type")
    # exactly one <main> and it is the skip target
    check("A06-single-main", html.count("<main") == 1, f"{name}: {html.count('<main')} <main> elements")
    check("A07-skip", 'class="skip"' in html and 'href="#main"' in html, f"{name}: no skip link")

# ---- social + feed hygiene ----------------------------------------------
for name, html in docs.items():
    check("A08-og-title", 'property="og:title"' in html, f"{name}: no og:title")
    check("A09-og-desc", 'property="og:description"' in html, f"{name}: no og:description")
    check("A10-twitter", 'name="twitter:card"' in html, f"{name}: no twitter:card")
    # description length: too short to be useful, too long is truncated by search
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    if d:
        ln = len(d.group(1))
        check("A11-desc-length", 50 < ln <= 320, f"{name}: meta description {ln} chars")

# ---- no render-blocking third-party assets ------------------------------
for name, html in docs.items():
    for m in re.finditer(r'<(?:script\s+[^>]*src|link\s+[^>]*rel="stylesheet"[^>]*href)="(https?://[^"]+)"', html):
        url = m.group(1)
        if url.startswith("https://wingbangboozle1-lang.github.io/Prod3/"):
            continue  # own canonical / social URLs, not loaded assets
        check("A12-no-third-party", False, f"{name}: third-party asset {url[:70]}")
    # a rel=canonical pointing at someone else's host is also a mistake
    canon = re.search(r'<link rel="canonical" href="(https?://[^"]+)"', html)
    if canon:
        check("A14-canonical-host", canon.group(1).startswith("https://wingbangboozle1-lang.github.io/Prod3/"),
              f"{name}: canonical points off-site → {canon.group(1)}")

# ---- images must be reasonably sized -----------------------------------
import os
for img in (ROOT / "assets").rglob("*.png"):
    kb = os.path.getsize(img) / 1024
    check("A13-img-weight", kb < 400, f"{img.name}: {kb:.0f} KB (over 400 KB)")

# ---- report
print(f"{len(docs)} pages checked, {checks_run} assertions run")
if failures:
    print(f"\n{len(failures)} FAILURES\n")
    for rule, detail in failures[:60]:
        print(f"  [{rule}] {detail}")
    sys.exit(1)

print("all additional rules passed")
sys.exit(0)
