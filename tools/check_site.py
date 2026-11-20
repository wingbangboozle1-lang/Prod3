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

import hashlib
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
         + sorted((ROOT / "tools").glob("*.html"))
         + sorted((ROOT / "products").glob("*.html")))
docs = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in pages}

titles, descs = {}, {}


def _link_names(html):
    """link text -> [outbound hrefs]. Used by the P14b uniqueness rule."""
    out = {}
    for m in re.finditer(r'<a\b[^>]*href="(https?://[^"]*)"[^>]*>(.*?)</a>', html, re.S):
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        href = m.group(1)
        if not text or "amazon" not in href:
            continue
        out.setdefault(text, []).append(href)
    return out

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

    # ---- one link name must not point at several products ----------------
    # A table that ends five rows with a bare "Listing" link gives a screen
    # reader, and anyone scanning the links panel, five identically-named
    # destinations. The visible table position carries the meaning; the link
    # name does not. Evidence links are named by ASIN instead.
    for label, hrefs in _link_names(html).items():
        if len(set(hrefs)) > 1:
            check("P14b-unique-link-name", False,
                  f"{name}: link text {label!r} points at {len(set(hrefs))} different destinations")

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

# ---- flag cross-references must resolve -----------------------------------
# Found during the FLG-id collision repair (T-52, session aa7b8dd8): a page can
# send a reader to a flag id that no longer exists after a renumber (the
# collision left FLG-022/FLG-023 refs pointing at nothing). Every FLG-xxx or
# F-xx id referenced on a published page must exist either as a callout heading
# on flagged.html or as an id in data/flagged.json. Historical mentions of
# retired ids are reworded, so every bare id must resolve.
_flag_json_ids = {i["id"] for i in
                  json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))["items"]}
_flag_headings = set(re.findall(
    r"<strong>(FLG-\d{3}|F-\d{2})\s+[—\u2014-]", (ROOT / "flagged.html").read_text(encoding="utf-8")))
_flag_known = _flag_json_ids | _flag_headings
for _name, _html in sorted(docs.items()):
    # expand compressed forms (FLG-017/031, FLG-001..017) before scanning
    _norm = re.sub(r"\bFLG-(\d{3})\s*(?:/|\.\.)\s*(\d{3})\b", r"FLG-\1 FLG-\2", _html)
    _refs = set(re.findall(r"\bFLG-\d{3}\b|\bF-\d{2}\b", _norm))
    _bad = sorted(r for r in _refs if r not in _flag_known)
    check("D06b-flag-refs", not _bad, f"{_name}: references undefined flag id(s) {_bad}")


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

# ---- the reader brief on ideas.html must match the registers ---------------
_rb = _sp.run([sys.executable, str(ROOT / "scripts" / "build_ideas.py"), "--check"],
              capture_output=True, text=True)
check("D18b-ideas-fresh", _rb.returncode == 0, f"ideas brief stale: {_rb.stdout.strip()[:200]}")

# ---- one identifier must mean one thing ----------------------------------
# This rule used to end in `or True`, so it could never fail. It was written for
# SG ids but the defect that actually shipped was in the FLG register: on
# 2026-11-20 flagged.html carried two different cards numbered FLG-020 and two
# numbered FLG-021, so a reader following "FLG-020" from citations.html (the
# Program Policies citation gap) landed on a card about DIRECTION.md question
# ids instead. Each id is now counted where it is DEFINED (a card or heading),
# not where it is merely referenced, and a repeat fails the release.
for _page, _prefix in (("suggestions.html", "SG"), ("flagged.html", "FLG")):
    _html = docs.get(_page, "")
    _defined = re.findall(rf"\b{_prefix}-\d{{2,3}}\s*(?:—|</strong>|<)", _html)
    _dupes = sorted({i for i in _defined if _defined.count(i) > 1})
    check(f"D19-{_prefix.lower()}-one-meaning", not _dupes,
          f"{_page}: identifier(s) defined more than once: {', '.join(_dupes)}")


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

# D38: one flag id must label one finding.
# On 2026-11-20 flagged.html carried FLG-020, FLG-021, FLG-022 and FLG-023 twice each,
# labelling four pairs of unrelated findings (T-46 logged it and left it for the owner).
# A duplicated id makes an earlier citation ambiguous, which is the whole point of an id,
# so this is now a release failure. The second finding in each pair was renumbered;
# no finding was deleted. Count is taken from the callout labels, not from the whole page,
# because ids are also cited in prose.
_flag_ids = re.findall(r"<strong>((?:FLG|F)-\d{3}) \u2014", docs.get("flagged.html", ""))
_flag_dupes = sorted({i for i in _flag_ids if _flag_ids.count(i) > 1})
check("D38-flag-id-unique", not _flag_dupes,
      f"flagged.html: id(s) labelling more than one finding: {_flag_dupes}")
check("D38-flag-count", len(_flag_ids) >= 26,
      f"flagged.html: only {len(_flag_ids)} labelled findings found (expected at least 26)")

# D39: no dangling flag citation.
# On 2026-11-20 flagged.html stopped defining FLG-022 and FLG-023 while air-fryers.html
# still cited both, so a reader who followed the reference landed on nothing. A flag whose
# id is not on the page is a broken promise in the site's most trust-bearing surface.
# This rule reads every FLG-/F- id cited anywhere in the published HTML and requires it to
# be defined by a callout label on flagged.html. It is what would have caught the deletion.
_flag_page = docs.get("flagged.html", "")
_defined_flags = set(re.findall(r"<strong>((?:FLG|F)-\d{3}) \u2014", _flag_page))
# A finding declared inside another finding's note is still declared: FLG-028 and
# FLG-029 were renumbered "in place" and are announced inside FLG-027.
_defined_flags |= set(re.findall(r"<strong>((?:FLG|F)-\d{3})</strong>", _flag_page))
_dangling = {}
for _name, _html in docs.items():
    if _name == "flagged.html":
        continue
    for _fid in set(re.findall(r"\b((?:FLG|F)-\d{3})\b", _html)):
        if _fid not in _defined_flags:
            _dangling.setdefault(_fid, []).append(_name)
check("D39-flag-citation", not _dangling,
      "cited but not defined on flagged.html: " +
      "; ".join(f"{k} ({', '.join(sorted(v)[:3])})" for k, v in sorted(_dangling.items())))

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
# D30: the seasonal block must surface the guide that matches the month. It used to
# assert the Thanksgiving plan literally; the guide set now has a December entry, so the
# rule checks that a seasonal guide is surfaced and that the December one ships while it
# is available. Both guides stay linked year-round; only the lead changes.
_front = docs.get("index.html", "")
check("D30-seasonal-surfaced",
      "thanksgiving-temperature-plan.html" in _front and "kitchen-gifts-that-get-used.html" in _front,
      "a seasonal guide is not linked from the front page")
check("D30-seasonal-lead",
      _front.find("kitchen-gifts-that-get-used.html") < _front.find("thanksgiving-temperature-plan.html"),
      "the December guide should lead the seasonal block while the site says it is December")


# D31: the publishing plan page must match data/editorial-plan.json, must be in the
# sitemap and linked from the decision desk. A plan row edited in one place only is
# a page that promises something the register does not contain.
_plan_path = ROOT / "data" / "editorial-plan.json"
check("D31-plan-data", _plan_path.exists(), "data/editorial-plan.json missing")
if _plan_path.exists():
    _plan = json.loads(_plan_path.read_text(encoding="utf-8"))
    _planpage = docs.get("publishing-plan.html", "")
    check("D31-plan-page", bool(_planpage), "publishing-plan.html missing from the tree")
    _rows = _plan.get("proposals", [])
    check("D31-plan-rows", len(_rows) == 12, f"expected 12 proposed rows, found {len(_rows)}")
    for _row in _rows:
        check("D31-plan-title", _row["title"].replace("&", "&amp;") in _planpage or _row["title"] in _planpage,
              f"proposed row not rendered: {_row['title'][:60]}")
        _d = _row["week"].split("-")
        _human = f"{int(_d[2])} {('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[int(_d[1])-1]} {_d[0]}"
        check("D31-plan-week", _human in _planpage,
              f"week {_human} for {_row['title'][:40]} not rendered")
        check("D31-plan-evidence", _row["evidence_status"] in ("available", "partly blocked", "blocked"),
              f"{_row['week']}: unknown evidence_status {_row['evidence_status']!r}")
    check("D31-plan-sitemap", "publishing-plan.html" in (ROOT / "sitemap.xml").read_text(encoding="utf-8"),
          "publishing-plan.html not in the sitemap")
    check("D31-plan-linked", "publishing-plan.html" in docs.get("ideas.html", "") and
          "publishing-plan.html" in docs.get("index.html", ""),
          "publishing-plan.html is not linked from ideas.html and the front page")
    # The plan may not smuggle in a traffic, volume or revenue claim.
    for _pat in (r"\bsearch volume\b(?! appears)", r"\b\d[\d,]* (?:searches|visitors|sales)\b",
                 r"\bconversion rate\b", r"\bestimated revenue\b"):
        _m = re.search(_pat, _planpage, re.I)
        check("D31-plan-no-forecast", not _m, f"publishing-plan.html carries a forecast claim: {_m.group(0) if _m else ''}")


# D32: one product page per registered product, each rendered from data/products.json,
# each in the sitemap and each reachable from its pillar. A page edited by hand instead
# of through the register fails here.
_r_pages = _sp2.run([sys.executable, str(ROOT / "scripts" / "build_products.py"), "--check"],
                          capture_output=True, text=True)
check("D32-product-pages-fresh", _r_pages.returncode == 0,
      f"product pages stale: {_r_pages.stdout.strip()[:160]}")
for _p in products:
    _slug = {"P-01": "chefman-6-qt-dual-basket", "P-02": "emeril-26qt-french-door",
             "P-03": "chefman-8-qt-turbofry", "P-04": "thermomaven-1-sec",
             "P-05": "chef-iq-sense-gen3"}[_p["id"]]
    _rel = f"products/{_slug}.html"
    check("D32-product-page-exists", _rel in docs, f"{_rel} missing")
    check("D32-product-page-sitemap", _rel in (ROOT / "sitemap.xml").read_text(encoding="utf-8"),
          f"{_rel} not in the sitemap")
    _pillar = "air-fryers.html" if _p["category"] == "Air Fryers" else "meat-thermometers.html"
    check("D32-product-page-linked", _rel in docs.get(_pillar, ""),
          f"{_rel} is not linked from {_pillar}")
    check("D32-product-page-observed", _p["observed_asin"] in docs.get(_rel, ""),
          f"{_rel} does not name the observed ASIN")
    check("D32-product-page-intent-blank", "No official source" in docs.get(_rel, ""),
          f"{_rel} does not show the blank intended-ASIN field")


# D33: a product page must list every flag that names its product, in either register.
# The first version of build_products.py matched only the "P-04" form and silently dropped
# every F row; this gate exists so that cannot happen again without failing the release.
_flags_all = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))["items"]
_SLUGS = {"P-01": "chefman-6-qt-dual-basket", "P-02": "emeril-26qt-french-door",
          "P-03": "chefman-8-qt-turbofry", "P-04": "thermomaven-1-sec",
          "P-05": "chef-iq-sense-gen3"}
for _p in products:
    _rel = f"products/{_SLUGS[_p['id']]}.html"
    _page = docs.get(_rel, "")
    _num = _p["id"].split("-")[-1].lstrip("0")
    _expected = [f["id"] for f in _flags_all
                 if "All five" in (f.get("product") or "")
                 or _p["observed_asin"] in (f.get("product") or "")
                 or any(t.lstrip("0") == _num for t in re.findall(r"P-?(\d+)", f.get("product") or ""))]
    check("D33-flags-present", len(_expected) > 0, f"{_rel}: no flag names this product at all")
    for _fid in _expected:
        check("D33-flag-listed", _fid in _page, f"{_rel}: flag {_fid} names this product but is not listed on its page")

# ---------------------------------------------------------------------------
# D35: every Program Policies clause citation must match the verified clause map.
# Found 2026-11-20: ten places cited the Section 2 letter for the star-ratings,
# URL-obscuring and shortener rules. All three rules exist, but in Section 6
# ("Content on your Site") as (t), (v) and (w). Section 2 ("Links on Your Site")
# has only (a) and (b). A wrong letter is a citation a reader cannot follow, so the
# letters actually on the live page are recorded in data/policy-clause-map.json and
# this rule refuses any other. A historical mention passes only when the same line
# says it was corrected - that is what keeps the fix auditable.
# ---------------------------------------------------------------------------
_clause_map = json.loads((ROOT / "data" / "policy-clause-map.json").read_text(encoding="utf-8"))
_verified = {c["section"] for c in _clause_map["clauses"]}
_verified |= {c["section"].split(" ")[0] for c in _clause_map["clauses"]}
CORRECTION_MARKERS = ("until corrected", "not Section 2", "cited as the section 2 letter", "as it read at the time",
                      "before the correction", "retired", "wrong section", "renumbered")
_scan_files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "articles").glob("*.html")) \
    + sorted((ROOT / "tools").glob("*.html")) + sorted((ROOT / "data").glob("*.json")) \
    + [ROOT / "DIRECTION.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "README.md"]
for _f in _scan_files:
    if _f.name == "policy-clause-map.json":
        continue  # the map quotes retired letters on purpose, as supersedes_citation
    _t = _f.read_text(encoding="utf-8")
    for _line in _t.splitlines():
        if ("\u00a72(t)" in _line or "\u00a72(v)" in _line or "§2(t)" in _line or "§2(v)" in _line):
            if not any(mk in _line for mk in CORRECTION_MARKERS):
                check("D35-clause-retired", False, f"{_f.name}: live citation of a retired clause — {_line.strip()[:110]}")
    for _m in re.finditer(r"(?:Program Policies|Participation Requirements|S02)\s*§?\s*(\d\([a-z]\))", _t):
        check("D35-clause-known", _m.group(1) in _verified,
              f"{_f.name}: cites Program Policies §{_m.group(1)}, which is not in data/policy-clause-map.json")
    for _m in re.finditer(r"§2\(([c-z])\)", _t):
        _ctx = _t[max(0, _m.start() - 160):_m.end() + 160]
        if not any(mk in _ctx for mk in CORRECTION_MARKERS):
            check("D35-clause-2x", False, f"{_f.name}: cites §2({_m.group(1)}); Section 2 stops at (b)")

# ---------------------------------------------------------------------------
# D36: no paragraph-length block of article body may repeat across articles.
# Found 2026-11-20: all eight evergreen articles closed with the same five-product
# block, byte for byte. Nothing in it was false; it is what makes a publication read
# as a template. Article chrome may repeat - the argument may not.
# ---------------------------------------------------------------------------
_art_blocks = {}
for _n, _h in docs.items():
    if not _n.startswith("articles/"):
        continue
    _body = _h.split("build-chrome:header:end")[-1].split("build-chrome:footer:start")[0]
    _body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", _body, flags=re.S)
    for _blk in re.findall(r'<div class="card[^"]*"[^>]*>(.*?)</div>', _body, re.S):
        _txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", _blk)).strip()
        if len(_txt) > 300:
            _art_blocks.setdefault(hashlib.md5(_txt.encode()).hexdigest(), []).append((_n, _txt[:100]))
for _key, _where in _art_blocks.items():
    check("D36-article-unique", len(_where) == 1,
          f"identical {len(_where)}x article block across {[w[0] for w in _where]}: {_where[0][1]}...")

# D37: the README register table must agree with the data files. It carried two
# contradicting tables and then stale ranges (Q-01..Q-21 while the register held
# Q-23) that nothing checked, so a reader could not tell which count was current.
_readme = (ROOT / "README.md").read_text(encoding="utf-8")
for _pre, _fn, _key, _page in (
        ("SG", "suggestions.json", "suggestions", "suggestions.html"),
        ("Q", "open-questions.json", "questions", "questions.html"),
        ("DT", "decisions.json", "decisions", "decisions.html")):
    _ids = json.loads((ROOT / "data" / _fn).read_text(encoding="utf-8"))[_key]
    _last = f"{_pre}-{max(int(i['id'].split('-')[1]) for i in _ids):02d}"
    check("D37-readme-range", f"{_pre}-01..{_last}" in _readme,
          f"README.md register table does not show {_pre}-01..{_last} for {_page}")

# D37: the README register table must match the data registers. It carried two
# contradicting tables and then hard-coded ranges that went stale the moment
# another session added rows. The table is now generated by scripts/build_readme.py,
# so this rule only has to prove the block matches the data -- it no longer asks
# anyone to hand-edit a number, which is what made it block a deploy on 2026-11-20.
_r37 = _sp2.run([sys.executable, str(ROOT / "scripts" / "build_readme.py"), "--check"],
                capture_output=True, text=True)
check("D37-readme-range", _r37.returncode == 0,
      f"README.md register table stale: {(_r37.stdout or _r37.stderr).strip()[:160]}")

# D34: a register row may not cite a source inline and omit it from its own
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
        check("D34-citation-declared", not _undeclared,
              f"{_fn}: {_row['id']} cites {_undeclared} inline but does not list them in sources")

# D35: one flag id, one subject. flagged.html published two different FLG-020
# callouts and two different FLG-021 callouts after a merge renumbered one pair,
# so the same id named both a policy-citation gap and a digest defect. Also
# checks the reverse: every id in data/flagged.json must be published.
_fh = docs.get("flagged.html", "")
_fids = re.findall(r"<strong>(FLG-\d{3}) —", _fh)
_fdupes = sorted({i for i in _fids if _fids.count(i) > 1})
check("D35-flag-unique", not _fdupes, f"flagged.html: duplicate flag id(s) {_fdupes}")
_fdata = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))
_fmissing = [i["id"] for i in _fdata["items"] if i["id"] not in _fh]
check("D35-flag-published", not not _fmissing,
      f"flagged.html: data/flagged.json id(s) not published {_fmissing}")

# D36: a heading that advertises an ID range must end at the register's last id.
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
            check("D36-range-current", int(_m.group(1)) == _last,
                  f"{_name}: range says {_m.group(0)} but the register's last id is {_pre}-{_last:02d}")

# D40: a stated guide count must equal the number of guides on disk.
# The tree shipped ten articles while README, buying-guide.html, both executive
# summaries, Q-17, SG-18 and SG-37 all said "eight" or "nine" -- seven reader-facing
# places, on a site whose whole claim is that the numbers are checked. The word
# counts are compared, not the digits, because those are what the copy uses.
_NUMWORD = {6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen"}
_guides = len(list((ROOT / "articles").glob("*.html")))
check("D40-guide-count-known", _guides in _NUMWORD, f"{_guides} guides on disk; add the number word to D40")
for _name, _html in docs.items():
    for _m in re.finditer(r"\b(six|seven|eight|nine|ten|eleven|twelve)\s+(?:question-shaped\s+)?(?:guides|articles)\b", _html, re.I):
        _said = _m.group(1).lower()
        _want = _NUMWORD.get(_guides, "")
        check("D40-guide-count", _said == _want,
              f"{_name}: says {_m.group(0)!r} but {_guides} guides ship ({_want})")
for _f in ("README.md", "EXECUTIVE_SUMMARY.md"):
    _txt = (ROOT / _f).read_text(encoding="utf-8")
    for _m in re.finditer(r"\b(six|seven|eight|nine|ten|eleven|twelve)\s+(?:question-shaped\s+)?(?:guides|articles)\b", _txt, re.I):
        check("D40-guide-count", _m.group(1).lower() == _NUMWORD.get(_guides, ""),
              f"{_f}: says {_m.group(0)!r} but {_guides} guides ship")

# ---- report
print(f"{len(docs)} pages checked, {checks_run} assertions run")
if failures:
    print(f"\n{len(failures)} FAILURES\n")
    for rule, detail in failures[:60]:
        print(f"  [{rule}] {detail}")
    sys.exit(1)

print("all additional rules passed")
sys.exit(0)
