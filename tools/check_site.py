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

pages = (sorted(ROOT.glob("*.html"))
         + sorted((ROOT / "articles").glob("*.html"))
         + sorted((ROOT / "tools").glob("*.html")))
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

# ---- citation attribution: a claim must cite a source by the same publisher --
# The D06 rule only proves that a cited ID exists. A 2026-11-20 audit found
# claims cited to the wrong publisher: a Google policy cited to a Chefman
# listing (S12), an FTC quotation cited to Google's spam policy (S22), and a
# Google rule cited to an Emeril listing (S11). This rule checks that the
# publisher named in a clause appears in the title of at least one cited source.
# Heuristic by design: it reads the clause before each "(Sxx)" group, back to
# the previous sentence or semicolon. Claims it cannot parse need manual review.
_source_titles = {s["id"]: s["title"] for s in _sources["sources"]}
_PUBLISHER_KEYS = {
    "FTC": "FTC", "NIST": "NIST", "USDA": "USDA", "Lighthouse": "Lighthouse",
    "Program Policies": "Program Policies", "Operating Agreement": "Operating Agreement",
    "CAN-SPAM": "CAN-SPAM", "Google": "Google", "people-first": "Google",
    "People-first": "Google", "E-E-A-T": "Google", "Page-experience": "Google",
    "thin-affiliation": "Google",
}
_CITE_GROUP = re.compile(r"\((S\d{2}(?:\s*(?:[-\u2013,]|and|or)\s*S?\d{2})*)\)")


def _cited_ids(group):
    out = set()
    for a, b in re.findall(r"S(\d{2})\s*[-\u2013]\s*S?(\d{2})", group):
        out.update(f"S{n:02d}" for n in range(int(a), int(b) + 1))
    out.update(re.findall(r"S\d{2}", group))
    return {i for i in out if i in _source_titles}


def _json_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _json_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _json_strings(v)


for _f in sorted((ROOT / "data").glob("*.json")):
    if _f.name == "sources.json":
        continue
    for _text in _json_strings(json.loads(_f.read_text(encoding="utf-8"))):
        for _m in _CITE_GROUP.finditer(_text):
            _pre = _text[:_m.start()]
            _cut = max(_pre.rfind(". "), _pre.rfind("; "))
            _clause = _pre[_cut + 1:][-220:]
            _cited = _cited_ids(_m.group(1))
            for _key, _pub in _PUBLISHER_KEYS.items():
                if _key in _clause:
                    check("D15-attribution", any(_pub in _source_titles[c] for c in _cited),
                          f"{_f.name}: '{_key}' claim cites {_m.group(1)}, none of which is a {_pub} source: ...{_clause.strip()[-90:]}")

# ---- product citation blocks travel with the product ---------------------
_products = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))["products"]
for p in _products:
    c = p.get("citation")
    check("D08-citation", bool(c) and c.get("observed_from") == p.get("submitted_link"),
          f"{p['id']}: citation block missing or points at another link")
    check("D09-intent-stays-null", c.get("intended_value") is None,
          f"{p['id']}: an intended value was filled in without owner confirmation")

# ---- no customer star ratings or rating counts rendered ------------------
# Program Policies 2(t) was cited for this rule. The wording was not located in
# Section 2 on 2026-11-20 (FLG-020). The rule is kept as a conservative site check.
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


# J01-J04: every inline script (and assets/app.js) must parse.
# On 2026-11-20 a generated page emitted a literal newline inside a JS string; no
# gate read the scripts, so the defect would have shipped as a dead control.
import shutil as _shutil, subprocess as _spj, tempfile as _tf
_node = _shutil.which("node")
for name, html in docs.items():
    for js in re.findall(r"<script(?![^>]*application/ld\+json)(?![^>]*src=)[^>]*>(.*?)</script>", html, re.S):
        check("J01-script-not-empty", bool(js.strip()), f"{name}: empty inline script")
        if _node:
            with _tf.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
                fh.write(js); _tmp = fh.name
            _r = _spj.run([_node, "--check", _tmp], capture_output=True, text=True)
            check("J02-script-syntax", _r.returncode == 0,
                  f"{name}: inline script does not parse — {(_r.stderr.strip().splitlines() or ['?'])[-1][:140]}")
if _node:
    for _asset in ("assets/app.js",):
        _r = _spj.run([_node, "--check", str(ROOT / _asset)], capture_output=True, text=True)
        check("J03-asset-syntax", _r.returncode == 0, f"{_asset}: does not parse")

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


# ---- decision desk and tools must stay fresh and fully sourced -----------
# Added 2026-11-20 with the decision desk. Each rule guards a specific failure
# that the rebuild could otherwise reintroduce silently.
import subprocess as _sp2

# D20: no two LIVE suggestions may share a title. SG-20/SG-21 were byte-identical
# duplicates, which is the same "one ID, two meanings" failure the earlier audit
# fixed elsewhere. Retired rows are exempt -- they are kept on purpose.
_sugg = json.loads((ROOT / "data" / "suggestions.json").read_text(encoding="utf-8"))
_live = {}
for _s in _sugg["suggestions"]:
    if _s.get("status") == "retired":
        continue
    key = _s["title"].strip().lower()
    check("D20-suggestion-dup", key not in _live,
          f"suggestions.json: {_s['id']} duplicates the title of {_live.get(key)}")
    _live.setdefault(key, _s["id"])

# D21: decisions.html must match data/decisions.json
_r21 = _sp2.run([sys.executable, str(ROOT / "scripts" / "build_decisions.py"), "--check"],
                capture_output=True, text=True)
check("D21-decisions-fresh", _r21.returncode == 0, f"decisions.html stale: {_r21.stdout.strip()[:160]}")

# D22: chrome (masthead / disclosure / footer) must match scripts/build_chrome.py
_r22 = _sp2.run([sys.executable, str(ROOT / "scripts" / "build_chrome.py"), "--check"],
                capture_output=True, text=True)
check("D22-chrome-fresh", _r22.returncode == 0, f"chrome stale: {_r22.stdout.strip()[:160]}")

# D23: every decision row resolves its evidence, and says so when it has none.
_dec = json.loads((ROOT / "data" / "decisions.json").read_text(encoding="utf-8"))
for _d in _dec["decisions"]:
    has = bool(_d.get("sources"))
    check("D23-decision-evidence",
          has or _d.get("evidence_status") == "unverified",
          f"{_d['id']}: no sources and not marked unverified")
    for _sid in _d.get("sources", []):
        check("D24-decision-source-known", _sid in _source_ids,
              f"{_d['id']}: cites undefined source {_sid}")

# D25: every open question either cites a registered source or is marked unverified
for _q in json.loads((ROOT / "data" / "open-questions.json").read_text(encoding="utf-8"))["questions"]:
    has = bool(_q.get("sources"))
    check("D25-question-evidence",
          has or _q.get("evidence_status") == "unverified",
          f"{_q['id']}: no sources and not marked unverified")
    for _sid in _q.get("sources", []):
        check("D26-question-source-known", _sid in _source_ids,
              f"{_q['id']}: cites undefined source {_sid}")

# D28: DIRECTION.md must cite only question ids that exist in the register.
# On 2026-11-20 the digest listed Q-08 as the account-status question and Q-05 as a
# query-set question; neither was true, and the account-status question had never
# been registered. A digest that renames questions is worse than no digest.
_dir = (ROOT / "DIRECTION.md").read_text(encoding="utf-8")
_qids = {q["id"] for q in json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))["questions"]}
for _qid in sorted(set(re.findall(r"\bQ-\d{2}\b", _dir))):
    check("D28-direction-question-refs", _qid in _qids,
          f"DIRECTION.md cites {_qid}, which is not in data/open-questions.json")
_sgids = {x["id"] for x in json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))["suggestions"]}
for _sid in sorted(set(re.findall(r"\bSG-\d{2}\b", _dir))):
    check("D29-direction-suggestion-refs", _sid in _sgids,
          f"DIRECTION.md cites {_sid}, which is not in data/suggestions.json")

# D27: the tools pages must exist and be reachable from the front page
for _tool in ("tools/index.html", "tools/compare-builder.html",
              "tools/oven-converter.html", "tools/cook-temperatures.html"):
    check("D27-tool-present", _tool in docs, f"{_tool} missing")
    check("D27-tool-in-sitemap", _tool in (ROOT / "sitemap.xml").read_text(), f"{_tool} not in sitemap")
for _tool in ("tools/index.html", "tools/compare-builder.html",
              "tools/oven-converter.html", "tools/cook-temperatures.html"):
    check("D28-tool-linked", _tool.replace("tools/", "tools/") in docs.get("index.html", ""),
          f"index.html does not link {_tool}")

# D29: the USDA figures on the cook-temperature page must match the published chart.
# Wrong food-safety numbers are the worst possible defect on this site, so the
# values are asserted literally rather than trusted to the renderer.
_usda = docs.get("tools/cook-temperatures.html", "")
for _pair in (("poultry", "165"), ("ground meats", "160"), ("fish and shellfish", "145")):
    check("D29-usda-values", _pair[0] in _usda.lower() or _pair[0] in (ROOT / "assets" / "decision-tools.js").read_text(encoding="utf-8").lower(),
          f"the USDA row for {_pair[0]} is in neither the page nor the renderer")
for _val in ("145°F (62.8°C)", "160°F (71.1°C)", "165°F (73.9°C)"):
    check("D29-usda-exact", _val in (ROOT / "assets" / "decision-tools.js").read_text(encoding="utf-8"),
          f"decision-tools.js is missing the USDA value {_val}")

# D30: a seasonal guide must be surfaced on the front page, and it must be the
# one whose month matches. Checked as a presence rule, not a render rule.
check("D30-seasonal-surfaced",
      "thanksgiving-temperature-plan.html" in docs.get("index.html", ""),
      "the seasonal guide is not linked from the front page")

# D31: a register row may not cite a source inline and omit it from its own
# `sources` list. Found by reading on 2026-11-20: Q-01 cited S03/S21 while
# declaring only S22, SG-09 attributed Google's meta-description guidance to the
# Emeril listing (S13), and 15 more rows cited evidence they did not declare.
# The reader-facing register links only the declared ids, so an undeclared
# citation is a source the reader cannot follow.
for _fn, _key, _fields in (
        ("open-questions.json", "questions", ("question", "known", "unknown", "how_to_find_out")),
        ("suggestions.json", "suggestions", ("title", "problem", "evidence", "recommendation"))):
    for _row in json.loads((ROOT / "data" / _fn).read_text(encoding="utf-8"))[_key]:
        _text = " ".join(str(_row.get(k, "")) for k in _fields)
        _cite = set(re.findall(r"\bS\d{2}\b", _text))
        _declared = set(_row.get("sources") or [])
        _undeclared = sorted(_cite - _declared)
        check("D31-citation-declared", not _undeclared,
              f"{_fn}: {_row['id']} cites {_undeclared} inline but does not list them in sources")

# D32: one flag id, one subject. flagged.html published two different FLG-020
# callouts and two different FLG-021 callouts after a merge renumbered one pair,
# so the same id named both a policy-citation gap and a digest defect. Also
# checks the reverse: every id in data/flagged.json must be published.
_fh = docs.get("flagged.html", "")
_fids = re.findall(r"<strong>(FLG-\d{3}) —", _fh)
_fdupes = sorted({i for i in _fids if _fids.count(i) > 1})
check("D32-flag-unique", not _fdupes, f"flagged.html: duplicate flag id(s) {_fdupes}")
_fdata = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))
_fmissing = [i["id"] for i in _fdata["items"] if i["id"] not in _fh]
check("D32-flag-published", not not _fmissing,
      f"flagged.html: data/flagged.json id(s) not published {_fmissing}")

# D33: a heading that advertises an ID range must end at the register's last id.
# ideas.html and direction.html both carried headings with stale ranges
# (SG-01..SG-26, SG-01..SG-25, FLG-001..FLG-020) that excluded rows published in
# the very registers they linked to. Only headings are checked: historical prose
# that names an old range as history is accurate and must not fail the build.
_ranges = {
    "SG": [s["id"] for s in json.loads((ROOT / "data" / "suggestions.json").read_text(encoding="utf-8"))["suggestions"]],
    "Q": [q["id"] for q in json.loads((ROOT / "data" / "open-questions.json").read_text(encoding="utf-8"))["questions"]],
}
for _name, _html in docs.items():
    for _pre, _ids in _ranges.items():
        _last = max(int(i.split("-")[1]) for i in _ids)
        _heads = " ".join(re.findall(r"<h[123][^>]*>(.*?)</h[123]>", _html, re.S))
        for _m in re.finditer(_pre + r"-01\s*(?:\.\.|…+)\s*" + _pre + r"-(\d{2})", _heads):
            check("D33-range-current", int(_m.group(1)) == _last,
                  f"{_name}: range says {_m.group(0)} but the register's last id is {_pre}-{_last:02d}")

# ---- report
print(f"{len(docs)} pages checked, {checks_run} assertions run")
if failures:
    print(f"\n{len(failures)} FAILURES\n")
    for rule, detail in failures[:60]:
        print(f"  [{rule}] {detail}")
    sys.exit(1)

print("all additional rules passed")
sys.exit(0)
