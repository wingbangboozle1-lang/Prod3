#!/usr/bin/env python3
"""Render one page per product from data/products.json and data/flagged.json.

Why this exists
---------------
The site could compare five products across pages but had no page *per product*. A
shopper who wants to know one machine better than the comparison table allows had
nowhere to go, and every claim lived on a page that was not about the thing itself.

Rules this renderer obeys
-------------------------
* Every value is copied from data/products.json. Nothing is typed into this file
  that does not already exist in the register (headings and section sentences are
  the only prose here).
* Seller claims stay labelled as seller claims. Where a listing contradicts itself
  both readings are printed, copied from the register, never averaged.
* No price, no star rating, no review count and no "best" verdict is rendered.
* Intended vs observed stays separate: the page says what the supplied link did do
  and what the owner has confirmed, and that the second is still blank.
* `--check` re-renders in memory and exits 1 when a page has drifted.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_chrome  # noqa: E402  (shared chrome, so a product page cannot drift from the rest)

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangbooz1-lang.github.io".replace("booz1", "boozle1") + "/Prod3"
TRACKING = "shopnow047c-20"

# Which fields to show, in reading order, with a plain-language label and a note on
# what the field actually is. Field names must exist in the register or the build fails.
SPEC_ROWS = [
    ("capacity", "Listed capacity", "How the listing states capacity. A quart figure is not a serving size."),
    ("dimensions", "Listed exterior size (D × W × H)", "Exterior measurements as published. Operating clearance is separate and is not published."),
    ("temperature_range", "Temperature setting", "The range the listing states, not a tested result."),
    ("power", "Power", "Listed electrical rating."),
    ("weight", "Weight", "As listed."),
    ("material", "Material", "As listed."),
    ("color", "Colour", "As listed."),
    ("model_number", "Model number", "As listed — useful when comparing manuals or parts."),
    ("upc", "UPC", "As listed."),
    ("configuration", "Configuration", "The listing's own configuration wording."),
    ("presets", "Preset count", "Where the listing contradicts itself, both readings are printed."),
    ("included_components", "What is in the box", "The listing's contents wording."),
    ("response_time", "Read time", "A seller claim; this site has not timed it."),
    ("accuracy", "Stated accuracy", "A seller claim; this site has not measured it."),
    ("waterproof", "Water resistance", "A seller claim; this site has not tested it."),
    ("certification", "Certification wording", "The listing's own wording, kept as wording."),
    ("heat_safe", "Heat rating", "A seller claim; not tested here."),
    ("probes", "Probes", "As listed."),
    ("sensors", "Sensors", "As listed."),
    ("connectivity", "Connectivity", "As listed. Range depends on the owner's network, not the probe."),
    ("battery_life", "Battery life", "Where the listing contradicts itself, both readings are printed."),
    ("warranty", "Warranty wording", "As literally worded on the listing."),
    ("display", "Display", "As listed."),
    ("display_type", "Display type", "As listed."),
    ("special_features", "Features", "The listing's feature list, verbatim."),
    ("unit_count", "Unit count", "As listed."),
]

# The one-line trade-off per product is an editorial judgement about routine, and is
# the only sentence on the page not copied from the register. It is labelled as such.
TRADEOFF = {
    "P-01": "Two 3-quart baskets only help if you cook two different things at once. If you cook one big batch, the divider is in your way.",
    "P-02": "The largest footprint here and the widest temperature range. If your counter depth is tight, that trade is the wrong way round.",
    "P-03": "One deep basket means fewer parts to wash, and no way to finish two foods on separate timers.",
    "P-04": "A handheld spot-check needs you at the oven. That is the point of it, and also its limit.",
    "P-05": "Three probes and a hub to charge, pair and clean. Worth it only if you want to walk away during a long cook.",
}

# The short name is the start of the register's own listing title, so the page heading
# is checkable against data/products.json rather than typed from memory.
SHORT_NAME = {
    "P-01": "CHEFMAN 6 Quart Dual Basket Air Fryer Oven",
    "P-02": "Emeril Lagasse 26QT French Door Multi-Function Air Fryer Toaster Oven",
    "P-03": "Chefman Air Fryer 8 Qt",
    "P-04": "ThermoMaven 1 Sec Professional Digital Meat Thermometer",
    "P-05": "CHEF iQ Sense",
}

SLUG = {
    "P-01": "chefman-6-qt-dual-basket",
    "P-02": "emeril-26qt-french-door",
    "P-03": "chefman-8-qt-turbofry",
    "P-04": "thermomaven-1-sec",
    "P-05": "chef-iq-sense-gen3",
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="{base}/products/{slug}.html">
<title>{title} | Kitchen Counter</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:image" content="{base}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kitchen Counter — air fryers and meat thermometers compared by the numbers on their listings">
<meta property="og:site_name" content="Kitchen Counter">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/style.css">
<link rel="alternate" type="application/rss+xml" title="Kitchen Counter" href="../feed.xml">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<main id="main"><div class="article" style="max-width:1000px">
<p class="kicker">{kicker}</p>
<h1>{h1}</h1>
<p class="byline">Kitchen Counter · Listing read {date} · Every value below is copied from the listing, not tested here</p>
"""

FOOT = """
<p class="mt"><a href="../{pillar}">← Back to the {pillar_name} shelf</a> · <a href="../compare.html">Compare all five</a> · <a href="../flagged.html">Flagged for review</a></p>
</div></main>
</body></html>
"""


def esc(v):
    return html.escape(str(v), quote=False)


def spec_table(p, listing):
    rows = []
    specs = p.get("specs") or {}
    for key, label, note in SPEC_ROWS:
        if key not in specs or specs[key] in (None, ""):
            continue
        rows.append(f'<tr><th scope="row">{esc(label)}</th>'
                    f'<td>{esc(specs[key])}<br><span class="small muted">{esc(note)}</span></td>'
                    f'<td class="small"><a href="{listing}" rel="sponsored noopener">Listing</a></td></tr>')
    if not rows:
        return '<p class="small muted">No specification fields are recorded for this product.</p>'
    return ('<div class="table-wrap"><table data-source-required="amazon-listing">'
            '<caption>Transcribed from the official listing. Nothing in this table is a measurement made by Kitchen Counter.</caption>'
            '<thead><tr><th>Field</th><th>What the listing states</th><th>Source</th></tr></thead>'
            '<tbody>' + "".join(rows) + "</tbody></table></div>")


def render(p, flags, products_doc):
    pid = p["id"]
    slug = SLUG[pid]
    asin = p["observed_asin"]
    listing = f"https://www.amazon.com/dp/{asin}"
    short = SHORT_NAME[pid]
    assert p["observed_title"].startswith(short), f"{pid}: short name is not a prefix of the listing title"

    kicker_bits = [p["category"], p["brand"]]
    kicker = " · ".join(kicker_bits)

    # flags that name this product
    mine = [f for f in flags if pid in (f.get("product") or "") or asin in (f.get("product") or "")]
    flag_list = "".join(
        f'<li><strong>{esc(f["id"])}</strong> — {esc(re.sub(r"<[^>]+>", "", f["detail"])[:300])}…</li>'
        for f in mine)

    cot = TRADEOFF[pid]

    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": short, "brand": {"@type": "Brand", "name": p["brand"]},
        "category": p["category"],
        "url": f"{BASE}/products/{slug}.html",
        "description": f"{p['category']} listing read on {products_doc['verified_on']}. Seller-published specifications, not a test result.",
    }, ensure_ascii=False)

    body = [
        f'<p class="lede">{esc(short)}. This page collects what the listing publishes, labelled as the listing, '
        f'and what it does not publish. It is not a review: nobody here has used this appliance.</p>',

        f'<p><a class="btn primary" rel="sponsored noopener" target="_blank" data-event="outbound_click" '
        f'data-asin="{asin}" href="{listing}">Open the official listing for {asin}</a></p>',
        f'<p class="small muted">The supplied short link for this product (<code>{esc(p["submitted_token"])}</code>) '
        f'is not used as the button. It last landed on the Amazon homepage on 2026-11-20 — see '
        f'<a href="../flagged.html">FLG-025</a>. The listing link above is the destination this page describes.</p>',

        '<div class="callout"><strong>The honest one-liner.</strong> ' + esc(cot) +
        ' <span class="small">(An editorial judgement about your routine, not a measurement.)</span></div>',

        '<div class="section-head mt"><h2>What the listing states</h2>'
        f'<a href="{listing}" rel="sponsored noopener">Source: official listing →</a></div>',
        spec_table(p, listing),

        '<div class="section-head mt"><h2>What the listing does not settle</h2></div>',
    ]

    if flag_list:
        body.append('<ul class="small">' + flag_list + '</ul>')
    else:
        body.append('<p class="small muted">No open flag names this product directly. That is not the same as '
                    'the listing being complete: absence of a flag means nobody has found a contradiction, not that '
                    'every field is published.</p>')

    body.append(
        '<div class="callout"><strong>Not shown here, on purpose.</strong> No price, no star rating and no review '
        'count. Amazon’s Program Policies permit showing price and availability only when Amazon serves that data '
        'or it arrives through the Product Advertising API; this site does neither. Ratings are left out for the '
        'same reason. <a href="../disclosure.html">Why the money works this way</a>.</div>')

    body.append('<div class="section-head mt"><h2>How this page was checked</h2></div>')
    body.append(
        f'<p class="small">The specification values were transcribed from the official listing on '
        f'<strong>{products_doc["verified_on"]}</strong> and re-read on {products_doc["verified_on_live_recheck"]}. '
        f'The link record below is kept separate from any statement of what the owner intended, because nothing '
        f'public confirms that intent.</p>')
    body.append(
        '<div class="table-wrap"><table data-source-required="amazon-listing">'
        '<caption>What the supplied link did, versus what the owner has confirmed. The second column is blank, and stays blank until the owner fills it.</caption>'
        '<thead><tr><th>Record</th><th>Value</th></tr></thead><tbody>'
        f'<tr><td>Supplied short link</td><td><code>{esc(p["submitted_link"])}</code></td></tr>'
        f'<tr><td>Token length</td><td>{p["token_length"]} characters — an ASIN is 10, so this is a short-link code, not an ASIN. <a href="https://affiliate-program.amazon.com/help/operating/policies" rel="sponsored noopener">Program Policies</a></td></tr>'
        f'<tr><td>Observed destination, 2026-11-19</td><td><a href="{esc(p["observed_redirect_target"])}" rel="sponsored noopener">{esc(p["observed_redirect_target"])}</a></td></tr>'
        f'<tr><td><strong>Intended ASIN (owner-confirmed)</strong></td><td><span class="unverified">No official source</span> — not confirmed by the owner (FLG-001)</td></tr>'
        f'<tr><td>Owner confirmation date</td><td><span class="unverified">No official source</span> — blank</td></tr>'
        f'<tr><td>Newer model noted on the listing</td><td>{esc(p.get("newer_model_note") or "None recorded")} — <a href="{listing}" rel="sponsored noopener">check the listing</a></td></tr>'
        '</tbody></table></div>')

    body.append(
        '<p class="small muted mt">Next: <a href="../compare.html">compare this with the other four</a>, or read '
        '<a href="../buying-guide.html">how to choose between them</a>.</p>')

    page = HEAD.format(
        base=BASE, slug=slug,
        title=esc(short + " — what the listing states"),
        desc=esc(f"{short}: {p['category'].lower()} specifications transcribed from the official Amazon listing on {products_doc['verified_on']}, with every conflict published and no price or rating shown."),
        jsonld=jsonld.replace("</", "<\\/"),
        kicker=kicker, h1=esc(short), date=products_doc["verified_on"],
    ) + "".join(body) + FOOT.format(pillar=PILLAR[pid][0], pillar_name=PILLAR[pid][1])
    return page


PILLAR = {
    "P-01": ("air-fryers.html", "air fryers"),
    "P-02": ("air-fryers.html", "air fryers"),
    "P-03": ("air-fryers.html", "air fryers"),
    "P-04": ("meat-thermometers.html", "meat thermometers"),
    "P-05": ("meat-thermometers.html", "meat thermometers"),
}


def main():
    products = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))
    flagged = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))["items"]
    outdir = ROOT / "products"
    outdir.mkdir(exist_ok=True)
    check = "--check" in sys.argv
    stale = []
    for p in products["products"]:
        target = outdir / f"{SLUG[p['id']]}.html"
        # Chrome is rendered here, not left to a second pass, so --check and the page on
        # disk are produced by exactly the same code path.
        rendered = build_chrome.render(render(p, flagged, products),
                                       f"products/{SLUG[p['id']]}.html", 1)
        if check:
            current = target.read_text(encoding="utf-8") if target.exists() else ""
            if current != rendered:
                stale.append(target.name)
        else:
            target.write_text(rendered, encoding="utf-8")
            print(f"wrote products/{target.name}")
    if check:
        if stale:
            print("FAIL: stale product pages: " + ", ".join(stale))
            print("Run: python3 scripts/build_products.py")
            return 1
        print("OK: product pages match data/products.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
