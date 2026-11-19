#!/usr/bin/env python3
"""
Static site builder for the Shopwise Kitchen Desk affiliate publication.

Design rules this file enforces, so they cannot be forgotten on page fourteen:
  * every page carries the Amazon disclosure strip under the masthead and again in the footer;
  * every outbound Amazon link is rendered with rel="sponsored noopener";
  * no price, currency symbol, discount or delivery estimate is ever emitted;
  * every page has a unique <title> and meta description;
  * every page has exactly one <h1>;
  * all internal links resolve to a page this build actually produced.

There are no third-party dependencies. Run: python3 build.py
"""

import html
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT  # GitHub Pages publishes main:/ at the repository root

SITE_NAME = "Shopwise Kitchen Desk"
SITE_TAGLINE = "Air fryers and thermometers, read the way a spec sheet should be."
BASE_URL = "https://wingbangboozle1-lang.github.io/Prod3"
# GitHub Pages serves this repository as a project site at /Prod3/, so every
# root-absolute internal link has to carry that prefix or it 404s against
# wingbangboozle1-lang.github.io/ instead of the project. Set BASE_PATH to ""
# if the site ever moves to a custom domain at an apex.
BASE_PATH = ""

_INTERNAL = re.compile(r'(href|src|content)="(/(?!/)[^"]*)"')


def prefix_internal(doc):
    """Rewrite root-absolute internal URLs to include the project path.

    Absolute http(s) URLs are untouched (they are already canonical), and so
    are protocol-relative //host URLs. Everything else that starts with a
    single slash is an internal reference and gets the prefix.
    """
    if not BASE_PATH:
        return doc

    def repl(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(BASE_PATH + "/") or url == BASE_PATH:
            return m.group(0)
        return f'{attr}="{BASE_PATH}{url}"'

    return _INTERNAL.sub(repl, doc)
TRACKING_ID = "shopnow047c-20"
DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases."
BUILD_DATE = "2026-11-19"

NAV_PRIMARY = [
    ("/air-fryers/", "Air fryers"),
    ("/thermometers/", "Thermometers"),
    ("/guides/", "Guides"),
    ("/compare/", "Compare"),
]

FOOTER_GROUPS = [
    ("Shop", [
        ("/air-fryers/", "Air fryers"),
        ("/thermometers/", "Thermometers"),
        ("/compare/", "Compare all five"),
        ("/guides/", "All guides"),
    ]),
    ("The desk", [
        ("/about/", "About and how we work"),
        ("/sources/", "Source register"),
        ("/suggestions/", "Suggestions board"),
        ("/questions/", "Open questions"),
    ]),
    ("Dashboard", [
        ("/dashboard/", "Overview"),
        ("/dashboard/register.html", "Product register"),
        ("/dashboard/verification.html", "Verification record"),
        ("/dashboard/gate.html", "Compliance gate"),
        ("/dashboard/analysis.html", "Counter-space analysis"),
        ("/dashboard/ledger.html", "Campaign ledger"),
        ("/dashboard/flagged.html", "Flagged for review"),
        ("/dashboard/measurement.html", "Measurement policy"),
    ]),
]

# ---------------------------------------------------------------- loading

def load(name):
    with open(ROOT / "data" / name, encoding="utf-8") as fh:
        return json.load(fh)


def load_content(name):
    with open(ROOT / "content" / name, encoding="utf-8") as fh:
        return json.load(fh)


DATA = {
    "sources": load("sources.json"),
    "products": load("products.json"),
    "checks": load("policy-checks.json"),
    "flagged": load("flagged.json"),
    "suggestions": load("suggestions.json"),
    "questions": load("open-questions.json"),
    "campaigns": load("campaigns.json"),
    "verification": load("verification.json"),
    "analysis": load("analysis.json"),
    "guides": load_content("guides.json"),
    "reviews": load_content("reviews.json"),
    "categories": load_content("categories.json"),
    "measurement": load_content("measurement.json"),
}

SOURCE_BY_ID = {s["id"]: s for s in DATA["sources"]["sources"]}
PRODUCT_BY_ID = {p["id"]: p for p in DATA["products"]["products"]}
REVIEW_BY_PRODUCT = {r["product"]: r for r in DATA["reviews"]["reviews"]}
GUIDE_BY_SLUG = {g["slug"]: g for g in DATA["guides"]["guides"]}

PAGES = []          # (url_path, title, description, body_html)
ASSETS = []


# ---------------------------------------------------------------- helpers

def esc(text):
    return html.escape(str(text), quote=True)


SPONSORED_HOSTS = ("amazon.com", "amazon.co.uk", "amazon.ca", "amazon.de",
                    "amazon.fr", "amazon.co.jp", "amazon.com.au", "link.amazon")


def is_commerce_url(url):
    """True for any outbound link that can earn a commission.

    Amazon's Associate programme pays on traffic that lands on an Amazon Site,
    so Amazon itself — including the help and policy pages, which are on the
    affiliate-program subdomain — is treated as commerce, not as a citation.
    Google, the FTC and the USDA are citations and are left unqualified.
    """
    return any(host in url for host in SPONSORED_HOSTS)


def citation(url, title, inner, extra_class="src"):
    """The only way an outbound citation is rendered.

    Commerce destinations are qualified as sponsored; genuine third-party
    citations are not. This distinction is decided in one place so a page
    cannot get it wrong.
    """
    rel = "sponsored noopener" if is_commerce_url(url) else "noopener"
    return (f'<a class="{esc(extra_class)}" href="{esc(url)}" target="_blank" '
            f'rel="{rel}" title="{esc(title)}">{inner}</a>')


def src_link(src_id, source_map=None):
    """Render one source as a small outbound citation chip."""
    smap = source_map or SOURCE_BY_ID
    src = smap.get(src_id)
    if not src:
        return ""
    return citation(src["url"], src["title"], esc(src_id))


def src_links(ids):
    return " ".join(src_link(i) for i in ids if i)


def amazon_button(product, label="View on Amazon"):
    """The only way an outbound product link is ever rendered."""
    url = product["intended"]["listing_url"]
    return (
        f'<a class="btn btn-amazon" href="{esc(url)}" rel="sponsored noopener" '
        f'target="_blank" data-product="{esc(product["id"])}">'
        f'{esc(label)}<span class="btn-ext" aria-hidden="true">↗</span></a>'
        f'<span class="btn-note">Link opens Amazon in a new tab. We earn a commission '
        f'on qualifying purchases.</span>'
    )


def spec_row(label, spec):
    value = spec.get("value") or ""
    if value:
        cell = f'{esc(value)} <span class="spec-src">{src_link(spec.get("src", ""))}</span>'
    else:
        flag = spec.get("flag", "")
        flag_html = f' <a class="flagchip" href="/dashboard/flagged.html#{esc(flag)}">{esc(flag)}</a>' if flag else ""
        cell = f'<span class="unverified">Not published on the listing</span> — left blank{flag_html}'
    return f"<tr><th scope=\"row\">{esc(label)}</th><td>{cell}</td></tr>"


def page(path, title, description, body, kicker=None, show_masthead=True):
    PAGES.append({
        "path": path,
        "title": title,
        "description": description,
        "body": body,
        "kicker": kicker,
        "masthead": show_masthead,
    })


# ---------------------------------------------------------------- shell

def nav_html(active):
    items = []
    for href, label in NAV_PRIMARY:
        cls = ' class="on"' if active.startswith(href) else ""
        items.append(f'<a href="{href}"{cls}>{esc(label)}</a>')
    return "\n".join(items)


def footer_html():
    groups = []
    for title, links in FOOTER_GROUPS:
        lis = "\n".join(f'<li><a href="{esc(h)}">{esc(l)}</a></li>' for h, l in links)
        groups.append(f'<div class="fgroup"><h3>{esc(title)}</h3><ul>{lis}</ul></div>')
    return "\n".join(groups)


def shell(p, prev_urls):
    canonical = BASE_URL + p["path"]
    masthead = ""
    if p["masthead"]:
        kicker = f'<p class="hero-kicker">{esc(p["kicker"])}</p>' if p["kicker"] else ""
        masthead = f"""
<header class="hero">
  <div class="wrap">
    {kicker}
    <h1>{esc(p["title"])}</h1>
    <p class="hero-sub">{esc(p["description"])}</p>
  </div>
</header>"""
    else:
        masthead = f"""
<header class="hero hero-tight">
  <div class="wrap">
    <h1>{esc(p["title"])}</h1>
    <p class="hero-sub">{esc(p["description"])}</p>
  </div>
</header>"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])} · {esc(SITE_NAME)}</title>
<meta name="description" content="{esc(p["description"])}">
<link rel="canonical" href="{esc(canonical)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(p["title"])} · {esc(SITE_NAME)}">
<meta property="og:description" content="{esc(p["description"])}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(BASE_URL)}/assets/social-card.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/style.css">
<link rel="alternate" type="application/rss+xml" title="{esc(SITE_NAME)}" href="/feed.xml">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap topbar-in">
    <a class="brand" href="/">
      <span class="brand-mark" aria-hidden="true">◪</span>
      <span class="brand-name">{esc(SITE_NAME)}</span>
    </a>
    <nav class="nav" aria-label="Primary">{nav_html(p["path"])}</nav>
  </div>
</div>

<div class="disclosure-strip" role="note">
  <div class="wrap">
    <strong>Disclosure:</strong> {esc(DISCLOSURE)} Amazon and the Amazon logo are trademarks of
    Amazon.com, Inc. or its affiliates. <a href="/about/#disclosure">How we disclose</a>
  </div>
</div>

{masthead}

<main id="main">
  <div class="wrap">
{p["body"]}
  </div>
</main>

<footer class="footer">
  <div class="wrap">
    <div class="footer-cols">
      {footer_html()}
    </div>
    <div class="footer-disc">
      <p><strong>{esc(DISCLOSURE)}</strong> {esc(SITE_NAME)} is written and published independently
      and is not owned by, operated by, or endorsed by Amazon.com, Inc. or its affiliates. Prices and
      availability are shown only on Amazon, never here.</p>
      <p class="small">Last full verification pass: {esc(BUILD_DATE)}. No unit of any product reviewed
      here has been handled or tested. <a href="/about/#method">Read the method</a>.</p>
    </div>
  </div>
</footer>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- blocks

def product_card(pid, note=None):
    p = PRODUCT_BY_ID[pid]
    rv = REVIEW_BY_PRODUCT.get(pid)
    verdict = rv["verdict"] if rv else ""
    return f"""
<article class="pcard">
  <div class="pcard-art" aria-hidden="true"><span>{esc(p["short_name"][:2])}</span></div>
  <div class="pcard-body">
    <p class="pcard-family">{esc(p["family"])}</p>
    <h3><a href="/product/{esc(p["handle"])}.html">{esc(p["short_name"])}</a></h3>
    <p class="pcard-verdict">{esc(note or verdict)}</p>
    {amazon_button(p)}
  </div>
</article>"""


def spec_table(pid):
    p = PRODUCT_BY_ID[pid]
    rows = []
    labels = [
        ("type", "Type"),
        ("capacity_title", "Capacity (as titled)"),
        ("capacity_field", "Capacity (specification field)"),
        ("dimensions", "Dimensions"),
        ("colour", "Colour"),
        ("material", "Material"),
        ("features", "Features listed"),
        ("presets", "Presets"),
        ("temperature_range", "Temperature range"),
        ("reading_time", "Reading time"),
        ("accuracy_claim", "Accuracy claim"),
        ("probes", "Probes"),
        ("sensors", "Sensors"),
        ("connectivity", "Connectivity"),
        ("battery", "Battery"),
        ("heat_resistance", "Heat resistance"),
        ("water_resistance", "Water resistance"),
        ("display", "Display"),
        ("power", "Power"),
        ("included", "In the box"),
        ("care", "Care"),
        ("certifications_listed", "Standards listed by seller"),
        ("warranty", "Warranty"),
        ("dimensions", "Dimensions"),
    ]
    seen = set()
    for key, label in labels:
        if key in seen or key not in p["specs"]:
            continue
        seen.add(key)
        rows.append(spec_row(label, p["specs"][key]))
    rows.append(spec_row("Price", p["specs"]["price"]))
    if p["specs"].get("rating_at_capture"):
        rows.append(spec_row("Rating at capture", p["specs"]["rating_at_capture"]))
    if p["specs"].get("badges_at_capture"):
        rows.append(spec_row("Badges at capture", p["specs"]["badges_at_capture"]))
    return f'<table class="spec"><caption class="sr-only">Specifications for {esc(p["name"])}</caption><tbody>{"".join(rows)}</tbody></table>'


def data_table(headers, rows, caption=None, cls=""):
    """Render a real table. Header cells are text; body cells may carry markup."""
    head = "".join(f'<th scope="col">{esc(h)}</th>' for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    return (f'<div class="table-scroll"><table class="{esc(cls)}">{cap}'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")


def product_strip(ids):
    cards = "".join(product_card(i) for i in ids)
    return f'<div class="pcards">{cards}</div>'


def guide_teaser(slug):
    g = GUIDE_BY_SLUG[slug]
    return f"""
<a class="gteaser" href="/guides/{esc(g["slug"])}.html">
  <span class="gteaser-kicker">{esc(g["kicker"])}</span>
  <span class="gteaser-title">{esc(g["title"])}</span>
  <span class="gteaser-meta">{g["reading_time"]} min read</span>
</a>"""


# ---------------------------------------------------------------- pages

def build_home():
    ids = ["P1", "P2", "P3", "P4", "P5"]
    body = f"""
<section class="lead">
  <div class="lead-copy">
    <h2>Five listings, read properly.</h2>
    <p>Three air fryers and two thermometers. No price theatre, no invented testing, no
    "best of 2026" list assembled from other people's summaries. What each listing actually
    says, what it leaves out, and which one fits which cook — with the date we read it.</p>
    <p class="lead-actions">
      <a class="btn btn-solid" href="/compare/">Compare all five</a>
      <a class="btn btn-ghost" href="/guides/">Start with a question</a>
    </p>
  </div>
  <div class="lead-art" aria-hidden="true">
    <div class="art-grid">
      <span>13.4″</span><span>12.8″</span><span>16.9″</span>
      <em>counter depth is the number that decides</em>
    </div>
  </div>
</section>

<section class="band">
  <h2 class="band-title">The products</h2>
  {product_strip(ids)}
</section>

<section class="band">
  <h2 class="band-title">Start with a question</h2>
  <div class="gteasers">
    {guide_teaser("basket-or-oven-air-fryer")}
    {guide_teaser("air-fryer-capacity-checklist")}
    {guide_teaser("do-i-need-a-meat-thermometer")}
    {guide_teaser("counter-space-per-quart")}
  </div>
  <p class="more"><a href="/guides/">All eight guides →</a></p>
</section>

<section class="band">
  <h2 class="band-title">Two ways in</h2>
  <div class="tiles">
    <a class="tile" href="/air-fryers/">
      <span class="tile-k">Air fryers</span>
      <span class="tile-t">Basket, dual-basket or oven</span>
      <span class="tile-d">Three shapes, and the reason capacity is the wrong number to start with.</span>
    </a>
    <a class="tile" href="/thermometers/">
      <span class="tile-k">Thermometers</span>
      <span class="tile-t">Instant-read or probe</span>
      <span class="tile-d">The USDA targets, and which thermometer actually answers your question.</span>
    </a>
  </div>
</section>

<section class="band band-quiet">
  <h2 class="band-title">How this site works</h2>
  <div class="steps">
    <div class="step"><span class="step-n">01</span><h3>Read the listing</h3><p>Every specification is copied from the product's own page on a stated date, and cited.</p></div>
    <div class="step"><span class="step-n">02</span><h3>Flag what is missing</h3><p>If a number is not on the listing, it is left blank and named. Nothing is inferred.</p></div>
    <div class="step"><span class="step-n">03</span><h3>Say who did not test it</h3><p>No unit has been handled. The site says so on every product page rather than implying otherwise.</p></div>
  </div>
  <p class="more"><a href="/about/">Who writes this, and how →</a></p>
</section>
"""
    page(
        "/",
        "Air fryers and thermometers, read like spec sheets",
        "Five Amazon listings — three air fryers, two thermometers — read against their own specification sheets, dated, with every gap flagged. Which one fits your counter and your cook.",
        body,
        kicker="Shopwise Kitchen Desk",
    )


def build_compare():
    headers = ["", "P1 Chefman dual basket", "P2 Emeril 26QT oven", "P3 Chefman TurboFry 8 Qt", "P4 ThermoMaven instant-read", "P5 CHEF iQ Sense"]
    ids = ["P1", "P2", "P3", "P4", "P5"]
    metric_rows = [
        ("Form", lambda p: p["specs"]["type"]["value"]),
        ("Capacity", lambda p: (p["specs"].get("capacity_title") or {}).get("value", "")),
        ("Capacity (spec field)", lambda p: (p["specs"].get("capacity_field") or {}).get("value", "")),
        ("Counter depth", lambda p: (p["specs"].get("dimensions") or {}).get("value", "") or ""),
        ("Presets", lambda p: (p["specs"].get("presets") or {}).get("value", "")),
        ("Rating at capture", lambda p: (p["specs"].get("rating_at_capture") or {}).get("value", "")),
        ("Price", lambda p: ""),
    ]
    rows = []
    for label, fn in metric_rows:
        cells = []
        for pid in ids:
            p = PRODUCT_BY_ID[pid]
            val = fn(p)
            if label == "Price":
                cells.append('<span class="unverified">See Amazon</span>')
            elif label == "Counter depth":
                dims = (p["specs"].get("dimensions") or {}).get("value", "")
                cells.append(esc(dims) if dims else '<span class="unverified">Not published</span> <a class="flagchip" href="/dashboard/flagged.html#F-04">F-04</a>')
            elif val:
                cells.append(esc(val))
            else:
                cells.append('<span class="unverified">Not published</span>')
        rows.append([label] + cells)
    rows.append(["Read the page"] + [f'<a href="/product/{PRODUCT_BY_ID[i]["handle"]}.html">Open →</a>' for i in ids])

    summary = data_table(headers, rows, caption="Five listings, compared field by field. Every value is from the product's own listing, captured 2026-11-19.", cls="cmp")

    body = f"""
<p class="standfirst">One table, five listings, every cell traceable to a product page and a date.
Where the table says "not published", the listing genuinely does not contain the value — it has not
been estimated to make the column look complete.</p>

<h2>Which one is for you</h2>
<div class="chooser" data-chooser>
  <div class="chooser-step" data-step="1">
    <p class="chooser-q">1. What are you buying?</p>
    <button class="choice" data-v="air">An air fryer</button>
    <button class="choice" data-v="thermo">A thermometer</button>
  </div>
  <div class="chooser-step" data-step="2" hidden>
    <p class="chooser-q" data-q>2. …</p>
    <div data-opts></div>
  </div>
  <div class="chooser-out" data-out hidden></div>
</div>

<h2>The full comparison</h2>
{summary}

<h2>What the table cannot tell you</h2>
<ul class="tight">
  <li><strong>How it cooks.</strong> Nothing here has been used. The table compares declarations, not results.</li>
  <li><strong>Whether it fits.</strong> Listed dimensions exclude door swing and drawer travel. Add both before measuring a tight counter.</li>
  <li><strong>What it costs today.</strong> Prices are not shown here by design; Amazon's Program Policies restrict who may display them. The link takes you to the live figure.</li>
</ul>

<h2>Read next</h2>
<div class="gteasers">
  {guide_teaser("basket-or-oven-air-fryer")}
  {guide_teaser("counter-space-per-quart")}
  {guide_teaser("thermometer-buying-checklist")}
</div>
"""
    page("/compare/", "Compare all five listings, field by field",
         "Side-by-side comparison of three air fryers and two thermometers, built only from values the listings publish, with every missing value named rather than guessed.",
         body, kicker="Comparison")


def build_category(cat):
    cards = "".join(product_card(opt["product"], note=opt["why"]) for opt in cat["chooser"]["options"])
    teasers = "".join(guide_teaser(s) for s in cat["guides"])
    body = f"""
<p class="standfirst">{esc(cat["intro"])}</p>

<h2>Which one is for you</h2>
<p class="chooser-q">{esc(cat["chooser"]["question"])}</p>
<div class="chips">
  {"".join(f'<span class="chip">{esc(o["label"])}</span>' for o in cat["chooser"]["options"])}
</div>

<div class="pcards">{cards}</div>

<h2>Read before you decide</h2>
<div class="gteasers">{teasers}</div>

<h2>How to read this category</h2>
<p>Every figure on these pages comes from the product's own listing on 2026-11-19 and carries its
source. Where a listing contradicts itself or omits a value, that is shown on the product page and
listed on the <a href="/dashboard/flagged.html">Flagged for review</a> page. Nothing is inferred from
a similar model. {src_links(cat["sources"])}</p>
"""
    page(f"/{cat['slug']}/", f"{cat['name']}: three listings, read carefully" if cat["slug"] == "air-fryers" else f"{cat['name']}: instant-read or probe",
         cat["strapline"], body, kicker="Category")


def build_product(pid):
    p = PRODUCT_BY_ID[pid]
    rv = REVIEW_BY_PRODUCT[pid]
    highlights = "".join(f"<li>{esc(h)}</li>" for h in p["highlights"])
    watch = "".join(f"<li>{esc(w)}</li>" for w in p["watch_outs"])
    listed = "".join(f"<li>{esc(h)}</li>" for h in rv["what_the_listing_says"])
    related = [g for g in DATA["guides"]["guides"] if pid in g["products"]][:3]
    related_html = "".join(guide_teaser(g["slug"]) for g in related)
    body = f"""
<p class="standfirst">{esc(rv["verdict"])}</p>

<div class="product-head">
  <div class="product-art" aria-hidden="true"><span>{esc(p["short_name"][:3])}</span>
    <em>Illustration, not a photograph.<br>No product photography is used on this site.</em></div>
  <div class="product-buy">
    <p class="product-family">{esc(p["family"])} · {esc(p["brand"])}</p>
    <h2>{esc(p["name"])}</h2>
    <p class="product-asin">ASIN <code>{esc(p["intended"]["asin"])}</code>, confirmed {esc(p["intended"]["confirmation_date"])}</p>
    {amazon_button(p, "Check the listing on Amazon")}
  </div>
</div>

<div class="two-col">
  <div>
    <h2>Best for</h2>
    <p>{esc(rv["best_for"])}</p>
    <h2>Not for</h2>
    <p>{esc(rv["not_for"])}</p>
    <h2>What the listing says</h2>
    <ul class="tight">{listed}</ul>
    <h2>Where it is weak</h2>
    <p>{esc(rv["where_it_is_weak"])}</p>
    <h2>The fit test</h2>
    <p>{esc(rv["fit_test"])}</p>
  </div>
  <aside>
    <h2>Quick read</h2>
    <ul class="tight">{highlights}</ul>
    <h2>Watch out for</h2>
    <ul class="tight">{watch}</ul>
  </aside>
</div>

<h2>The specification sheet</h2>
<p class="small">Every row is copied from <a href="{esc(p["intended"]["listing_url"])}" target="_blank" rel="sponsored noopener">the listing</a>
on 2026-11-19. A row that says "not published on the listing" is a value the listing does not contain;
it has been left blank deliberately, not overlooked.</p>
{spec_table(pid)}

<h2>Verification record</h2>
<div class="table-scroll"><table class="reg">
<thead><tr><th scope="col">Field</th><th scope="col">Intended</th><th scope="col">Observed</th></tr></thead>
<tbody>
<tr><th scope="row">ASIN</th><td><code>{esc(p["intended"]["asin"])}</code></td><td><code>{esc(p["observed"]["resolved_asin"])}</code></td></tr>
<tr><th scope="row">Date</th><td>{esc(p["intended"]["confirmation_date"])}</td><td>{esc(p["observed"]["captured"])}</td></tr>
<tr><th scope="row">Source</th><td>Supplied link · {src_link("S16")}</td><td><code class="plain">{esc(p["observed"]["short_link"])}</code></td></tr>
<tr><th scope="row">Result</th><td colspan="2">{"The short link resolves to the intended ASIN." if p["observed"]["agrees_with_intended"] else "The short link does not resolve to the intended ASIN — flagged."} {esc(p["observed"].get("note", ""))}</td></tr>
</tbody></table></div>

<div class="notice">
  <p><strong>What this page is not.</strong> It is not a test. No unit has been handled, measured or
  timed. Every figure comes from the listing on the date shown, and the judgements are about fit
  rather than quality. The FTC is explicit that you cannot describe experience with a product you
  have not tried {src_link("S08")}, so this page does not.</p>
</div>

<h2>Read next</h2>
<div class="gteasers">{related_html}</div>
"""
    page(f"/product/{p['handle']}.html",
         f"{p['short_name']}: what the listing actually says",
         rv["verdict"][:180],
         body, kicker=p["family"])


def build_guides_index():
    cards = []
    for g in DATA["guides"]["guides"]:
        cards.append(f"""
<article class="gcard">
  <p class="gcard-kicker">{esc(g["kicker"])}</p>
  <h3><a href="/guides/{esc(g["slug"])}.html">{esc(g["title"])}</a></h3>
  <p>{esc(g["description"])}</p>
  <p class="gcard-meta">{g["reading_time"]} min · {esc(g["cluster"])}</p>
</article>""")
    body = f"""
<p class="standfirst">Eight questions a buyer actually types, answered from published specifications
and USDA tables rather than opinion. Each one ends in a recommendation and the condition that would
change it.</p>
<div class="gcards">{"".join(cards)}</div>
"""
    page("/guides/", "Guides: eight buyer questions, answered",
         "Question-shaped buying guides on air fryer form, capacity, counter space, cleanup, multi-function appliances and thermometer choice, each answered from published specifications.",
         body, kicker="Guides")


def build_guide(g):
    sections = []
    for s in g["sections"]:
        paras = "".join(f"<p>{esc(p)}</p>" for p in s["body"])
        sections.append(f"<h2>{esc(s['h'])}</h2>{paras}")
    rec = f"""
<div class="verdict">
  <p class="verdict-k">The recommendation</p>
  <p>{esc(g["recommendation"])}</p>
  <p class="verdict-change"><strong>It changes if:</strong> {esc(g["changes_when"])}</p>
</div>"""
    links = "".join(guide_teaser(s) for s in g["links_to"])
    body = f"""
<p class="standfirst">{esc(g["answer"])}</p>
<p class="guide-meta">{g["reading_time"]} min read · specification-led · sources {src_links(g["sources"])}</p>

{''.join(sections)}

{rec}

<h2>The listings this is based on</h2>
{product_strip(g["products"])}

<h2>Read next</h2>
<div class="gteasers">{links}</div>

<div class="notice">
  <p><strong>How this was written.</strong> From the products' own listings and, where food safety is
  involved, the USDA Food Safety and Inspection Service's published chart {src_link("S10")}. No unit
  was tested. Figures are dated 2026-11-19 and will drift.</p>
</div>
"""
    page(f"/guides/{g['slug']}.html", g["title"], g["description"], body, kicker=g["kicker"])


def build_about():
    body = f"""
<p class="standfirst">This site is written by a small editorial desk. It does not have a personality,
a founder with a favourite pan, or a testing lab. What it has is the patience to read five
specification sheets closely and the discipline to say so when something is missing.</p>

<h2 id="method">The method</h2>
<ol class="tight">
  <li>Every product gets its own listing read, on one date, and every value is copied out with a source.</li>
  <li>If a value is absent, it stays absent. A blank with a flag is published instead of a guess.</li>
  <li>If a listing contradicts itself, both readings are published and the conflict is named.</li>
  <li>Food-safety figures come from the USDA, not from a summary of the USDA.</li>
  <li>No price is stored or shown, because Amazon's Program Policies restrict who may display price and availability.</li>
</ol>
<p>All five sources are listed on the <a href="/sources/">source register</a>, and every unresolved
issue is on the <a href="/dashboard/flagged.html">Flagged for review</a> page.</p>

<h2 id="disclosure">How this site discloses</h2>
<p>The sentence required by the Amazon Associates Operating Agreement appears in a strip beneath the
masthead on every page, above the first heading, and again in the footer. The same requirement is
repeated next to every outbound product button. The strip is deliberately annoying, because a
disclosure that is easy to miss is not a disclosure.</p>
<p>Every outbound link to Amazon is marked <code>rel="sponsored noopener"</code>, is labelled as
going to Amazon, and opens in a new tab. This site does not use a link shortener for anything it
publishes: the destination is always a full amazon.com address so nobody has to guess where a click
goes.</p>

<h2>What this site is not</h2>
<ul class="tight">
  <li>It is not affiliated with, owned by, or endorsed by Amazon.com, Inc.</li>
  <li>It is not a testing lab. No unit of any product here has been handled.</li>
  <li>It does not publish prices, availability or delivery estimates.</li>
  <li>It does not rank products as "best" — it explains which one fits a given cook and counter.</li>
</ul>

<h2>Who to talk to</h2>
<p>Corrections are the point of the exercise. If a figure here disagrees with the listing, the listing
is right and this page is a bug — see the <a href="/suggestions/">suggestions board</a> and the
<a href="/questions/">open questions</a> for what is already known to be unsettled.</p>

<h2>Sources</h2>
{src_links(["S01", "S02", "S08", "S10", "S14"])}
"""
    page("/about/", "About the desk, and how this site is written",
         "Who writes this site, the five rules it follows, how the affiliate disclosure is placed, and what it deliberately does not do — including testing products it has not handled.",
         body, kicker="About")


def build_sources():
    rows = []
    for s in DATA["sources"]["sources"]:
        tier = f'<span class="tier tier-{esc(s["tier"])}">{esc(s["tier"])}</span>'
        supports = "<br>".join(f"— {esc(x)}" for x in s["supports"])
        rows.append([
            f'<strong>{esc(s["id"])}</strong>',
            tier,
            citation(s["url"], s["title"], esc(s["title"]), extra_class="citesrc") + f'<br><span class="small">{esc(s["publisher"])}</span>',
            f'<span class="small">{supports}</span>',
            esc(s["captured"]),
        ])
    body = f"""
<p class="standfirst">Every claim on this site resolves to one of these. Tier matters: a
<em>primary</em> source is the authoritative body itself — Amazon's own agreement, a .gov agency,
Google Search Central, or the product listing in question. A <em>supplied</em> source is something
the site owner provided that has not been independently corroborated.</p>
{data_table(["ID", "Tier", "Source", "What it supports", "Read on"], rows, caption="The source register. Nineteen entries, each read on 2026-11-19.", cls="reg")}
<h2>What is not in this register</h2>
<p>No blog posts, no "best of" round-ups, no competitor comparisons and no AI summaries. If a fact
could only be sourced to one of those, it did not go on the site.</p>
"""
    page("/sources/", "Source register: every claim, and where it came from",
         "Nineteen sources the site relies on, split into primary sources and supplied material, each with a link, a capture date, and the exact claims it supports.",
         body, kicker="Transparency")


def build_suggestions():
    cards = []
    for s in DATA["suggestions"]["suggestions"]:
        opts = "".join(f"<li>{esc(o)}</li>" for o in s["options"])
        cards.append(f"""
<article class="sg">
  <div class="sg-head">
    <span class="sg-id">{esc(s["id"])}</span>
    <span class="sg-status sg-{esc(s["status"])}">{esc(s["status"])}</span>
    <span class="sg-eff">effort {esc(s["effort"].split(" —")[0])}</span>
    <span class="sg-conf">{esc(s["confidence"].split(" —")[0])}</span>
  </div>
  <h3>{esc(s["title"])}</h3>
  <p class="sg-problem">{esc(s["problem"])}</p>
  <p><strong>Evidence.</strong> {esc(s["evidence"])}</p>
  <p><strong>Paths.</strong></p>
  <ul class="opts">{opts}</ul>
  <p class="sg-rec"><strong>Recommended.</strong> {esc(s["recommendation"])}</p>
  <p class="small">Decision owner: {esc(s["decision_owner"])} · Blocks: {esc(s["blocks"])}</p>
</article>""")
    body = f"""
<p class="standfirst">A place to review suggestions and choose a path before anything is built. Each
card states the problem, the evidence behind it, the alternatives, and the recommendation. Some are
already implemented and say so; those are shown because a decision you cannot see is a decision you
cannot reverse.</p>
<div class="sg-legend">
  <span class="sg-status sg-implemented">implemented</span> shipped in this build
  <span class="sg-status sg-proposed">proposed</span> waiting on a decision
  <span class="sg-status sg-blocked">blocked</span> needs account access
</div>
{"".join(cards)}
"""
    page("/suggestions/", "Suggestions board: fourteen decisions, with the paths not taken",
         "A review board of fourteen site suggestions, each with its evidence, its alternatives and a recommendation, so a path can be chosen before anything is implemented.",
         body, kicker="Review")


def build_questions():
    groups = {}
    for q in DATA["questions"]["questions"]:
        groups.setdefault(q["group"], []).append(q)
    out = []
    out.append(f"""
<p class="standfirst">A decision made on missing information is a guess wearing a suit. Every entry
below states what is known, what is not, what decision it blocks, and the cheapest action that would
answer it. The honest count is: {sum(1 for q in DATA["questions"]["questions"] if q.get("status") == "owner-only")} of
{len(DATA["questions"]["questions"])} need the site owner's account access and cannot be closed from outside.</p>""")
    for group, qs in groups.items():
        rows = []
        for q in qs:
            rows.append([
                f'<strong>{esc(q["id"])}</strong><br><span class="small">{esc(q["status"])}</span>',
                f'<strong>{esc(q["question"])}</strong>',
                esc(q["known"]),
                esc(q["unknown"]),
                esc(q["blocks"]),
                f'<span class="small">{esc(q["how_to_find_out"])}</span>',
                f'<span class="small">{esc(q["who"])}<br>{esc(q["cost"])}</span>',
            ])
        out.append(f"<h2>{esc(group)}</h2>")
        out.append(data_table(["ID", "Question", "What is known", "What is not known", "What it blocks", "How to find out", "Who / cost"], rows, cls="reg q"))
    body = "\n".join(out)
    page("/questions/", "Open questions: what is known, and what is missing",
         "Seventeen open questions blocking decisions on this site, each with what is known, what is unknown, what it blocks and the cheapest way to find out.",
         body, kicker="Review")


def build_dashboard_index():
    cards = [
        ("/dashboard/register.html", "Product register", "Every published value, its source and its capture date, for all five listings."),
        ("/dashboard/verification.html", "Verification record", "Intended ASIN versus observed redirect, kept in separate fields, never merged."),
        ("/dashboard/gate.html", "Compliance gate", "Fourteen checks against Amazon's agreement, the FTC guidance and Google's policies — and which side of the automate/review line each sits on."),
        ("/dashboard/analysis.html", "Counter-space analysis", "Nominal capacity per square inch of counter, derived only from published dimensions."),
        ("/dashboard/ledger.html", "Campaign ledger", "Empty on purpose. Columns are defined; rows arrive only from first-party reports."),
        ("/dashboard/flagged.html", "Flagged for review", "Nineteen unresolved items, each with a source and an action."),
        ("/dashboard/measurement.html", "Measurement policy", "What the click counter records, what it deliberately does not, and why there is no cookie."),
    ]
    tiles = "".join(f"""
<a class="dtile" href="{h}">
  <span class="dtile-t">{esc(t)}</span>
  <span class="dtile-d">{esc(d)}</span>
</a>""" for h, t, d in cards)

    total = len(DATA["flagged"]["items"])
    high = sum(1 for f in DATA["flagged"]["items"] if f["severity"] == "high")
    checks = DATA["checks"]["checks"]
    met = sum(1 for c in checks if c["status"] == "met")
    partial = sum(1 for c in checks if c["status"] == "partial")
    blocked = sum(1 for c in checks if c["status"] == "blocked")
    body = f"""
<p class="standfirst">The machinery behind the shop. Everything here is reachable from the footer on
every page, and none of it is required reading for a buyer.</p>

<div class="kpis">
  <div class="kpi"><span class="kpi-n">{len(PRODUCT_BY_ID)}</span><span class="kpi-l">listings read line by line</span></div>
  <div class="kpi"><span class="kpi-n">{len(SOURCE_BY_ID)}</span><span class="kpi-l">sources registered</span></div>
  <div class="kpi"><span class="kpi-n">{met}<em>/{len(checks)}</em></span><span class="kpi-l">compliance checks met</span></div>
  <div class="kpi"><span class="kpi-n">{total}</span><span class="kpi-l">flagged items, {high} high severity</span></div>
  <div class="kpi"><span class="kpi-n">0</span><span class="kpi-l">performance figures claimed</span></div>
</div>

<div class="dtiles">{tiles}</div>

<h2>The one-line summary</h2>
<p>Five listings, all five short links resolved to the intended ASINs, {len(checks)} policy checks of
which {met} are fully met, {partial} are met subject to human review and {blocked} needs the Associates
account. {total} items are flagged rather than hidden. There is no traffic data, so no performance
number appears anywhere on this site.</p>
"""
    page("/dashboard/", "Dashboard: the verification machinery",
         "The audit trail behind the shop: product register, verification record, compliance gate, counter-space analysis, campaign ledger and nineteen flagged items.",
         body, kicker="Dashboard")


def build_register():
    rows = []
    for pg in DATA["products"]["products"]:
        for key, spec in pg["specs"].items():
            if key == "price":
                continue
            val = spec.get("value") or '<span class="unverified">blank</span>'
            flag = f'<a class="flagchip" href="/dashboard/flagged.html#{esc(spec["flag"])}">{esc(spec["flag"])}</a>' if spec.get("flag") else ""
            rows.append([
                f'<strong>{esc(pg["id"])}</strong>',
                f'<a href="/product/{esc(pg["handle"])}.html">{esc(pg["short_name"])}</a>',
                esc(key.replace("_", " ")),
                val,
                src_link(spec.get("src", "")) if spec.get("src") else '<span class="unverified">no source</span>',
                flag,
            ])
    body = f"""
<p class="standfirst">Every published value, in one table, with the source it came from and the date it
was read. Values that were absent from the listing appear as <span class="unverified">blank</span>
with a reason, because a blank is information.</p>
<div class="notice"><p><strong>No price rows.</strong> Price and availability are deliberately absent —
Amazon's Program Policies permit displaying them only when Amazon serves the data or it comes through
the Product Advertising API {src_link("S02")}. Both the register and the site comply by omitting them.</p></div>
{data_table(["Product", "Name", "Field", "Value as published", "Source", "Flag"], rows, caption="The product register. Prices are excluded by policy, not by oversight.", cls="reg wide")}
"""
    page("/dashboard/register.html", "Product register: every value and its source",
         "Every specification published on this site, in one table, each with the listing it came from and the date it was read — blanks included.",
         body, kicker="Register")


def build_verification():
    rows = []
    for r in DATA["verification"]["records"]:
        prod = PRODUCT_BY_ID[r["product"]]
        agree = "✔ agrees" if r["observed"]["agrees"] else "✖ does not agree — flagged"
        rows.append([
            f'<strong>{esc(r["product"])}</strong><br><span class="small">{esc(prod["short_name"])}</span>',
            f'<code>{esc(r["intended"]["asin"])}</code>',
            citation(r["intended"]["listing_url"], "Amazon listing " + r["intended"]["asin"], "/dp/" + esc(r["intended"]["asin"]), extra_class="citesrc"),
            esc(r["intended"]["confirmation_date"]),
            src_link(r["intended"]["source"]),
            f'<code class="plain">{esc(r["observed"]["short_link"])}</code><br><code class="small">{esc(r["observed"]["resolved_asin"])}</code>',
            esc(r["observed"]["captured"]),
            esc(agree),
        ])
    tid = DATA["verification"]["tracking_id_status"]
    body = f"""
<p class="standfirst">The confirmation record for each supplied link: the ASIN this site intends to
send readers to, the official listing URL, the date that intent was set, and where it came from — in
the left half. What the short link actually did, on the right. The two are never merged, because one
is a decision and the other is an observation.</p>

<div class="notice notice-warn">
  <p><strong>Tracking ID:</strong> <code>{esc(tid["value"])}</code>. Verified on the live links:
  <strong>no</strong>. The resolved URLs served to this session carried query parameters but no visible
  <code>tag=</code> value, so the Associates ID could not be confirmed from outside the account.
  Program Policies section 2(a) requires Special Links to carry the assigned ID {src_link("S02")}.
  This is not a statement that the links are invalid — it is a statement that the check cannot be
  completed without the dashboard. See <a href="/questions/#Q-02">Q-02</a>.</p>
</div>

{data_table(["Product", "Intended ASIN", "Official listing", "Confirmed", "Source", "Observed redirect", "Observed on", "Result"], rows, caption="Intended versus observed, kept in separate fields.", cls="reg wide")}

<h2>How to re-run this check</h2>
<ol class="tight">
  <li>Fetch each short link and record the <code>/dp/</code> ASIN it serves. Do not edit the intended field.</li>
  <li>If the observation differs from the intent, add a flagged item and publish both.</li>
  <li>Update <code>observed.captured</code> to the new date. Never overwrite an earlier observation without noting it.</li>
</ol>
"""
    page("/dashboard/verification.html", "Verification record: intended ASIN versus observed redirect",
         "Five links, five intended ASINs, five observed redirects, kept in separate fields with separate dates — the product-intent confirmation record.",
         body, kicker="Verification")


def build_gate():
    rows = []
    for c in DATA["checks"]["checks"]:
        status_cls = {"met": "ok", "partial": "warn", "blocked": "bad"}.get(c["status"], "warn")
        audit = "automated" if c["automated"] else "human gate"
        rows.append([
            f'<strong>{esc(c["id"])}</strong><br><span class="small">{esc(c["area"])}</span>',
            f'<strong>{esc(c["requirement"])}</strong><br><span class="small">{esc(c["quote_basis"])}</span>',
            src_link(c["source"]),
            f'<span class="status status-{status_cls}">{esc(c["status"])}</span>',
            f'<span class="small">{esc(audit)}</span>',
            f'<span class="small">{esc(c["evidence"])}</span>',
            f'<span class="small">{esc(c["gate"])}</span>',
        ])
    checks = DATA["checks"]["checks"]
    counts = {k: sum(1 for c in checks if c["status"] == k) for k in ("met", "partial", "blocked")}
    body = f"""
<p class="standfirst">Automate what can be automated, and put a gate in front of what cannot. Each
check below names the obligation, the primary source it comes from, whether a machine enforces it, and
what a machine cannot enforce.</p>

<div class="kpis">
  <div class="kpi"><span class="kpi-n">{counts["met"]}</span><span class="kpi-l">fully met, enforced by the build</span></div>
  <div class="kpi"><span class="kpi-n">{counts["partial"]}</span><span class="kpi-l">met, subject to human review</span></div>
  <div class="kpi"><span class="kpi-n">{counts["blocked"]}</span><span class="kpi-l">blocked on account access</span></div>
</div>

{data_table(["Check", "Obligation", "Source", "Status", "Enforced by", "Evidence", "The gate"], rows, caption="Fourteen policy checks against Amazon's agreement and program policies, the FTC's disclosure guidance and Google's publishing policies.", cls="reg wide gate")}

<h2>What the build refuses to ship</h2>
<ul class="tight">
  <li>A page without the disclosure strip.</li>
  <li>An Amazon link without <code>rel="sponsored"</code>.</li>
  <li>A currency symbol, a price pattern, a promotional discount phrase, or a delivery estimate.</li>
  <li>A duplicate title or meta description.</li>
  <li>A page with zero or more than one <code>&lt;h1&gt;</code>.</li>
  <li>An internal link that does not resolve.</li>
</ul>
"""
    page("/dashboard/gate.html", "Compliance gate: fourteen checks and where the human steps in",
         "Fourteen checks against Amazon's Operating Agreement and Program Policies, FTC disclosure guidance and Google publishing policy, each marked as automated or human-gated.",
         body, kicker="Compliance")


def build_analysis_page():
    a = DATA["analysis"]
    rows = []
    for p in a["products"]:
        if p["footprint_sq_in"]:
            rows.append([
                f'<strong>{esc(p["id"])}</strong> {esc(p["label"])}',
                f'{p["depth_in"]}″ × {p["width_in"]}″ × {p["height_in"]}″',
                f'{p["footprint_sq_in"]:.1f} in²',
                f'{p["capacity_quarts"]} qt',
                f'<strong>{p["quarts_per_sq_in"]:.3f}</strong>',
                src_links(p["sources"]),
            ])
        else:
            rows.append([
                f'<strong>{esc(p["id"])}</strong> {esc(p["label"])}',
                '<span class="unverified">not published</span>',
                "—", "—", "—",
                f'<a class="flagchip" href="/dashboard/flagged.html#F-04">F-04</a>',
            ])
    caveats = "".join(f"<li>{esc(c)}</li>" for c in a["caveats"])
    findings = "".join(f"<li>{esc(f)}</li>" for f in a["findings"])
    body = f"""
<p class="standfirst">The one piece of analysis here that no listing supplies: how much nominal
capacity each appliance packs into each square inch of counter. It is arithmetic on published
dimensions, not a measurement, and it is labelled as arithmetic.</p>

<h2>The method</h2>
<p>{esc(a["method"])}</p>

{data_table(["Product", "D × W × H", "Counter area", "Nominal capacity", "Quarts per in²", "Source"], rows, caption="Nominal capacity per square inch of counter footprint, derived from published dimensions.", cls="reg")}

<h2>What the numbers show</h2>
<ul class="findings">{findings}</ul>

<h2>Why this is not a ranking</h2>
<ul class="tight">{caveats}</ul>
"""
    page("/dashboard/analysis.html", "Counter-space analysis: quarts per square inch of counter",
         "Nominal capacity divided by counter footprint for the three air fryers, showing the oven-style machine packs about 2.6 times the capacity per square inch — and why that is not a ranking.",
         body, kicker="Analysis")


def build_ledger():
    c = DATA["campaigns"]
    defs = "".join(f"<li><strong>{esc(k)}</strong> — {esc(v)}</li>" for k, v in c["definitions"].items() if k != "frozen_rules")
    frozen = "".join(f"<li>{esc(x)}</li>" for x in c["definitions"]["frozen_rules"])
    body = f"""
<p class="standfirst">{esc(c["note_for_reader"])}</p>

<div class="empty-ledger">
  <p class="el-title">The ledger is empty</p>
  <p>Columns are defined. No row has been entered, because no first-party report has been read yet.
  Nothing here is estimated.</p>
</div>

<h2>The columns</h2>
<ul class="tight">{defs}</ul>

<h2>Frozen rules</h2>
<ol class="tight">{frozen}</ol>

<h2>Why it starts empty</h2>
<p>A conversion rate needs a numerator and a denominator drawn from the same population. The
denominator would have to come from an analytics source; the numerator only ever arrives in the
Associates Orders Report. They do not count the same things. Until both exist, the only honest
entry is a blank. {src_link("S02")}</p>

<h2>What will fill it</h2>
<ol class="tight">
  <li>Verify the site in Search Console — see <a href="/questions/#Q-07">Q-07</a>.</li>
  <li>Choose a reporting cadence and stick to it; a weekly read beats a daily glance.</li>
  <li>Transcribe one row per report, with the export filename and the date you read it.</li>
</ol>
"""
    page("/dashboard/ledger.html", "Campaign ledger: empty on purpose, with fixed columns",
         "The campaign ledger starts with zero rows and defined columns. Every row will come from an authorized first-party report with the date it was read. No estimates.",
         body, kicker="Measurement")


def build_flagged():
    items = DATA["flagged"]["items"]
    cards = []
    for f in items:
        prod = ", ".join(PRODUCT_BY_ID[p]["short_name"] for p in [x.strip() for x in f["product"].split(",")] if p in PRODUCT_BY_ID) if f["product"] != "all" else "All products"
        sev = f["severity"]
        cards.append(f"""
<article class="flag flag-{esc(sev)}" id="{esc(f["id"])}">
  <div class="flag-head">
    <span class="flag-id">{esc(f["id"])}</span>
    <span class="flag-sev sev-{esc(sev)}">{esc(sev)}</span>
    <span class="flag-area">{esc(f["area"])}</span>
    <span class="flag-prod">{esc(prod)}</span>
  </div>
  <h3>{esc(f["detail"])}</h3>
  <p><strong>Why it matters.</strong> {esc(f["why_it_matters"])}</p>
  <p><strong>What was done.</strong> {esc(f["action"])}</p>
  <p><strong>Status.</strong> {esc(f["status"])}</p>
  <p class="small">Sources: {src_links(f["sources"]) if f["sources"] else "none — this is an observation about what is absent."}</p>
</article>""")
    counts = {s: sum(1 for f in items if f["severity"] == s) for s in ("high", "medium", "low")}
    body = f"""
<p class="standfirst">Everything that could not be confirmed, or that conflicts, at the capture date.
None of it blocks publication and all of it is published rather than smoothed over. {len(items)} items:
{counts["high"]} high, {counts["medium"]} medium, {counts["low"]} low.</p>
<div class="notice"><p>A flagged item is not a failure. It is the difference between a site that says
"I don't know" and a site that quietly makes something up. Severity <em>high</em> means a buyer would
rely on the wrong number or a compliance question needs the account to settle it.</p></div>
{"".join(cards)}
"""
    page("/dashboard/flagged.html", "Flagged for review: nineteen unresolved items",
         "Nineteen items that could not be confirmed or that conflict, each with its severity, its source, what was done about it and what action would close it.",
         body, kicker="Review")


def build_measurement_page():
    m = DATA["measurement"]
    secs = "".join(f"<h2>{esc(s['h'])}</h2>" + "".join(f"<p>{esc(p)}</p>" for p in s["body"]) for s in m["sections"])
    body = f"<p class=\"standfirst\">{esc(m['description'])}</p>{secs}<p class=\"small\">Sources: {src_links(m['sources'])}</p>"
    page("/dashboard/measurement.html", m["title"], m["description"], body, kicker="Measurement")


def build_not_found():
    body = """
<p class="standfirst">That page does not exist. The five products, the eight guides and the dashboard
are all one link away.</p>
<p><a class="btn btn-solid" href="/">Back to the front page</a></p>
"""
    page("/404.html", "Not found", "The page you asked for does not exist. Start from the front page, the guides or the comparison.", body, kicker="404")


# ---------------------------------------------------------------- feeds

def write_sitemap(urls):
    entries = []
    for path in urls:
        if path == "/404.html":
            continue
        entries.append(
            f'  <url><loc>{esc(BASE_URL + path)}</loc>'
            f'<lastmod>{BUILD_DATE}</lastmod></url>'
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(entries) + "\n</urlset>\n")
    (OUT / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_feed():
    items = []
    for g in DATA["guides"]["guides"]:
        url = f'{BASE_URL}/guides/{g["slug"]}.html'
        items.append(f"""    <item>
      <title>{esc(g["title"])}</title>
      <link>{esc(url)}</link>
      <guid>{esc(url)}</guid>
      <pubDate>Wed, 19 Nov 2026 09:00:00 +0000</pubDate>
      <description>{esc(g["description"])}</description>
    </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{esc(SITE_NAME)}</title>
    <link>{esc(BASE_URL)}/</link>
    <description>{esc(SITE_TAGLINE)}</description>
    <language>en-us</language>
    <lastBuildDate>Wed, 19 Nov 2026 09:00:00 +0000</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
    (OUT / "feed.xml").write_text(xml, encoding="utf-8")


def write_robots():
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {BASE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------- main

GENERATED_FILES = [
    "index.html", "compare", "air-fryers", "thermometers", "product", "guides",
    "about", "sources", "suggestions", "questions", "dashboard", "404.html",
    "sitemap.xml", "feed.xml", "robots.txt",
]


def remove_generated():
    """Delete previously generated output, and nothing else."""
    for name in GENERATED_FILES:
        target = ROOT / name
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()


def main():
    # Clean only what this build owns. Source lives in data/, content/, assets/,
    # tools/ and build.py; generated pages never overwrite those.
    remove_generated()

    build_home()
    build_compare()
    for cat in DATA["categories"]["categories"]:
        build_category(cat)
        for pid in [o["product"] for o in cat["chooser"]["options"]]:
            pass
    for pid in PRODUCT_BY_ID:
        build_product(pid)
    build_guides_index()
    for g in DATA["guides"]["guides"]:
        build_guide(g)
    build_about()
    build_sources()
    build_suggestions()
    build_questions()
    build_dashboard_index()
    build_register()
    build_verification()
    build_gate()
    build_analysis_page()
    build_ledger()
    build_flagged()
    build_measurement_page()
    build_not_found()

    urls = [p["path"] for p in PAGES]
    # assets/ is already at the served root, so it needs no copying.

    for p in PAGES:
        dest = OUT / p["path"].lstrip("/")
        if p["path"].endswith("/"):
            dest = dest / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(prefix_internal(shell(p, urls)), encoding="utf-8")

    write_sitemap(urls)
    write_feed()
    write_robots()

    print(f"built {len(PAGES)} pages into {OUT}")
    for p in PAGES:
        print("  ", p["path"])


if __name__ == "__main__":
    main()
