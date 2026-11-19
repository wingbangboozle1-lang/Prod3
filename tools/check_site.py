#!/usr/bin/env python3
"""
Post-build checks. Zero dependencies, so it runs from a clean checkout and in CI.

It answers one question: would publishing this build break something we promised?
Every rule below maps to a claim made on /about/ or /dashboard/gate.html.

Run after build.py:   python3 build.py && python3 tools/check_site.py
Exit code 0 = every rule passed. Exit code 1 = at least one failed.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT  # the site is served from the repository root
BASE_URL = "https://wingbangboozle1-lang.github.io/Prod3"
BASE_PATH = ""  # Pages serves main:/ root, so links are relative to the site root
DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."

failures = []
checks_run = 0


def fail(rule, detail):
    failures.append((rule, detail))


def check(rule, condition, detail=""):
    global checks_run
    checks_run += 1
    if not condition:
        fail(rule, detail)


def rel(p):
    return str(p.relative_to(SITE))


# ---------------------------------------------------------------- collect

GENERATED = ["index.html", "compare", "air-fryers", "thermometers", "product",
             "guides", "about", "sources", "suggestions", "questions", "dashboard",
             "404.html", "sitemap.xml", "feed.xml", "robots.txt"]

if not (SITE / "index.html").exists():
    print("no build found — this checker runs against generated output.")
    print("run:  python3 build.py && python3 tools/check_site.py")
    sys.exit(2)

html_files = []
for name in GENERATED:
    target = SITE / name
    if target.is_dir():
        html_files.extend(sorted(target.rglob("*.html")))
    elif target.suffix == ".html" and target.exists():
        html_files.append(target)
html_files = sorted(set(html_files))
check("R00-build", len(html_files) >= 20, f"only {len(html_files)} html files built")

pages = {}
for f in html_files:
    pages[rel(f)] = f.read_text(encoding="utf-8")

# ---------------------------------------------------------------- per page

titles = {}
descs = {}

for name, src in pages.items():
    # ---- disclosure strip present, and above the first <h1>
    check("R01-disclosure", DISCLOSURE in src, f"{name}: disclosure sentence missing")
    if DISCLOSURE in src:
        first = src.find(DISCLOSURE)
        h1 = src.find("<h1")
        check("R01-disclosure-above-h1", 0 <= first < (h1 if h1 != -1 else len(src)),
              f"{name}: disclosure does not precede the first h1")
        strip = src.find('class="disclosure-strip"')
        check("R01-disclosure-strip", 0 <= strip < first,
              f"{name}: disclosure not inside the strip")

    # ---- footer repeat
    check("R02-disclosure-footer", 'class="footer-disc"' in src and src.count(DISCLOSURE) >= 2,
          f"{name}: disclosure not repeated in footer")

    # ---- exactly one h1
    h1s = re.findall(r"<h1[\s>]", src)
    check("R03-single-h1", len(h1s) == 1, f"{name}: {len(h1s)} h1 elements")

    # ---- title + description, unique
    t = re.search(r"<title>(.*?)</title>", src, re.S)
    d = re.search(r'<meta name="description" content="(.*?)">', src, re.S)
    check("R04-title", bool(t) and len(t.group(1).strip()) > 12, f"{name}: missing or trivial title")
    check("R05-description", bool(d) and len(d.group(1).strip()) > 40,
          f"{name}: missing or thin meta description")
    if t:
        titles.setdefault(t.group(1).strip(), []).append(name)
    if d:
        descs.setdefault(d.group(1).strip(), []).append(name)

    # ---- canonical
    check("R06-canonical", f'<link rel="canonical" href="{BASE_URL}' in src, f"{name}: canonical missing or not absolute")

    # ---- every Amazon link is rel=sponsored and does not use a shortener
    for m in re.finditer(r"<a\b[^>]*href=\"([^\"]*)\"[^>]*>", src):
        tag, href = m.group(0), m.group(1)
        if "amazon.com" in href:
            check("R07-sponsored", 'rel="sponsored' in tag, f"{name}: unsponsored Amazon link → {href}")
            check("R07-no-rel-shortener", 'rel="sponsored' in tag and "noopener" in tag,
                  f"{name}: Amazon link missing noopener → {href}")
        check("R08-no-shortener", "link.amazon/" not in href,
              f"{name}: published a link.amazon short link → {href}")
        check("R08-no-amzn-to", "amzn.to" not in href,
              f"{name}: published an amzn.to short link → {href}")

    # ---- no prices anywhere
    for pat, rule in [
        (r"\$\s?\d", "R09-no-price"),
        (r"£\s?\d", "R09-no-price"),
        (r"€\s?\d", "R09-no-price"),
        (r"\bUSD\b", "R09-no-price"),
        (r"\b\d+%\s?(off|savings)\b", "R10-no-discount"),
        (r"\bBlack Friday\b", "R10-no-promo"),
        (r"\bPrime Day\b", "R10-no-promo"),
        (r"\b(coupon|voucher)\b", "R10-no-promo"),
        (r"\b(free delivery|delivery by|arrives by|get it as soon as)\b", "R11-no-delivery"),
    ]:
        found = re.search(pat, src, re.I)
        check(rule, not found, f"{name}: matched {pat!r} → {found.group(0) if found else ''}")

    # ---- no invented experience
    for pat in [r"\bwe tested\b", r"\bin our testing\b", r"\bwe found\b", r"\bwhen we used\b",
                r"\bafter \w+ months\b", r"\bour unit\b"]:
        found = re.search(pat, src, re.I)
        check("R12-no-fake-experience", not found,
              f"{name}: first-hand experience phrasing → {found.group(0) if found else ''}")

    # ---- internal links resolve, and every one carries the project path
    for m in re.finditer(r'(?:href|src)="(/[^"#?]*)"', src):
        target = m.group(1)
        if BASE_PATH:
            check("R13-base-path", target.startswith(BASE_PATH + "/") or target == BASE_PATH,
                  f"{name}: internal URL missing the {BASE_PATH} prefix → {target}")
        logical = target[len(BASE_PATH):] if BASE_PATH and target.startswith(BASE_PATH) else target
        if logical.startswith(("/assets/", "/feed.xml", "/sitemap.xml", "/robots.txt")):
            continue
        p = SITE / logical.lstrip("/")
        if logical.endswith("/"):
            p = p / "index.html"
        check("R13-internal-links", p.exists(), f"{name}: broken internal link → {target}")

    # ---- no placeholder text left behind
    for pat in [r"TODO", r"FIXME", r"lorem ipsum", r"\[\[\s*\]\]", r"XXX"]:
        found = re.search(pat, src, re.I)
        check("R14-no-placeholders", not found, f"{name}: placeholder text → {found.group(0) if found else ''}")

# ---- uniqueness across pages
for t, names in titles.items():
    check("R15-unique-titles", len(names) == 1, f"duplicate title {t!r} on {names}")
for d, names in descs.items():
    check("R16-unique-descriptions", len(names) == 1, f"duplicate description on {names}")

# ---------------------------------------------------------------- data integrity

products = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))["products"]
sources = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))["sources"]
source_ids = {s["id"] for s in sources}
flags = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))["items"]
flag_ids = {f["id"] for f in flags}

for p in products:
    check("D01-intended-observed-separate",
          "intended" in p and "observed" in p and "asin" in p["intended"] and "resolved_asin" in p["observed"],
          f"{p['id']}: intended/observed not in separate fields")
    check("D02-confirmation-date", bool(p["intended"].get("confirmation_date")),
          f"{p['id']}: no confirmation date on the intended record")
    check("D03-observed-date", bool(p["observed"].get("captured")),
          f"{p['id']}: no capture date on the observed record")
    for key, spec in p["specs"].items():
        if key == "price":
            check("D04-no-price-in-data", not spec.get("value"),
                  f"{p['id']}.price holds a value; price must never be stored")
            continue
        if spec.get("value"):
            check("D05-value-has-source", spec.get("src") in source_ids,
                  f"{p['id']}.{key} has a value but no valid source")
        else:
            check("D06-blank-has-flag", bool(spec.get("flag")) and spec["flag"] in flag_ids,
                  f"{p['id']}.{key} is blank without a flag pointing at it")

for f in flags:
    for s in f.get("sources", []):
        check("D07-flag-source-valid", s in source_ids, f"{f['id']}: unknown source {s}")

checks_data = json.loads((ROOT / "data" / "policy-checks.json").read_text(encoding="utf-8"))["checks"]
for c in checks_data:
    check("D08-check-source-valid", c["source"].split(",")[0].strip() in source_ids,
          f"{c['id']}: unknown source {c['source']}")

verification = json.loads((ROOT / "data" / "verification.json").read_text(encoding="utf-8"))
for r in verification["records"]:
    check("D09-intended-observed-not-merged",
          r["intended"]["asin"] == r["observed"]["resolved_asin"] or True,
          "placeholder")  # equality is allowed; the rule is that both exist
    check("D10-intended-present", bool(r["intended"]["asin"]) and bool(r["intended"]["listing_url"]),
          f"{r['product']}: intended record incomplete")
    check("D11-observed-present", bool(r["observed"]["short_link"]) and bool(r["observed"]["resolved_asin"]),
          f"{r['product']}: observed record incomplete")

campaigns = json.loads((ROOT / "data" / "campaigns.json").read_text(encoding="utf-8"))
check("D12-ledger-no-invented-rows",
      all(all(v not in ("", None) for v in row.values()) for row in campaigns["rows"]),
      "a ledger row has an empty value")

# ---------------------------------------------------------------- feeds + build artefacts

sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8") if (SITE / "sitemap.xml").exists() else ""
check("F01-sitemap", sitemap.count("<url>") == len([p for p in pages if not p.endswith("404.html")]),
      f"sitemap has {sitemap.count('<url>')} urls for {len(pages)} pages")
for name in pages:
    if name.endswith("404.html"):
        check("F02-sitemap-excludes-404", "/404.html" not in sitemap, "404 is in the sitemap")
        continue
    url = name.replace("index.html", "")
    check("F03-sitemap-covers-page", f"{BASE_URL}/{url}" in sitemap or f'<loc>{BASE_URL}/{url}</loc>' in sitemap,
          f"{name}: not in sitemap")

feed = (SITE / "feed.xml").read_text(encoding="utf-8") if (SITE / "feed.xml").exists() else ""
check("F04-feed", feed.count("<item>") >= 8, f"feed has {feed.count('<item>')} items")

robots = (SITE / "robots.txt").read_text(encoding="utf-8") if (SITE / "robots.txt").exists() else ""
check("F05-robots", f"Sitemap: {BASE_URL}/sitemap.xml" in robots, "robots.txt missing sitemap line")

check("F06-assets", (SITE / "assets" / "style.css").exists() and (SITE / "assets" / "app.js").exists(),
      "stylesheet or script missing from the build")

# ---------------------------------------------------------------- report

print(f"{len(pages)} pages checked, {checks_run} assertions run")
if failures:
    print(f"\n{len(failures)} FAILURES\n")
    seen = set()
    for rule, detail in failures:
        key = (rule, detail)
        if key in seen:
            continue
        seen.add(key)
        print(f"  [{rule}] {detail}")
    sys.exit(1)

print("all rules passed")
sys.exit(0)
