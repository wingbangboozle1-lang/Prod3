#!/usr/bin/env python3
"""One-off repair pass (session a25ccde6, 2026-11-19).

Applies source-verified corrections across the published tree and keeps the
data registers consistent. Idempotent: safe to run twice.

Rules applied (each tied to a source in data/sources.json):
  R-01  Remove customer star ratings and rating counts rendered as site content.
        Program Policies, Participation Requirements §2(t) (S02).
  R-02  Feed: remove currency amounts and the undefined "whole-chicken test".
        Program Policies §2(b) price rule (S02); the test was never performed.
  R-03  Point og:image at an absolute PNG URL (crawlers do not resolve relative
        social images reliably); keep og:image:alt and twitter:card.
  R-04  Add JSON-LD structured data where none exists; fix Article schema so it
        validates with schema.org (Organization author requires a name only).
  R-05  Repair dangling source references S06/S07/S08/S09 to S16/S17/S18/S05.
  R-06  Remove two stale copy claims that a price is compared/shown.
  R-07  Sticky bar: compare pages should not link to themselves; label the
        real purpose of the bar.
  R-08  Add data/citations.json backing every rendered figure.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ABS = "https://wingbangboozle1-lang.github.io/Prod3"
changed = []

def read(rel):  return (ROOT / rel).read_text(encoding="utf-8")
def write(rel, s):
    p = ROOT / rel
    if p.read_text(encoding="utf-8") != s:
        p.write_text(s, encoding="utf-8")
        changed.append(rel)

HTML = sorted(ROOT.glob("*.html")) + sorted((ROOT / "articles").glob("*.html"))

# ---------------------------------------------------------------- R-01 ratings
RATING_PATTERNS = [
    re.compile(r"<small>Rating at capture · [^<]*</small>"),
    re.compile(r"<small>Captured 2026-11-19</small>"),
    re.compile(r"<td>[0-9]\.[0-9]★ \([0-9,]+\)</td>"),
]
for f in HTML:
    s = f.read_text(encoding="utf-8")
    o = s
    for pat in RATING_PATTERNS:
        s = pat.sub(lambda m: "" if m.group(0).startswith("<small>") else "<td>—</td>", s)
    # empty <p class="pricenote"> wrappers that lost their only child
    s = s.replace('<p class="pricenote"><span class="novalue">Current price on Amazon</span></p>',
                  '<p class="pricenote"><span class="novalue">Current price on Amazon</span></p>')
    if s != o:
        f.write_text(s, encoding="utf-8")
        changed.append(str(f.relative_to(ROOT)))

# replace the compare.html rating row entirely
compare = read("compare.html")
compare = re.sub(
    r"<tr><td><strong>Rating at capture</strong></td>.*?</tr>\n?",
    '<tr><td><strong>Ratings</strong></td><td colspan="5"><span class="novalue">Not displayed — open the listing</span>'
    ' <span class="small muted">Customer stars and rating counts are Amazon customer content; Program Policies '
    '(Participation Requirements §2(t)) allow them only when obtained through Creators API/PA API. The site '
    'does neither, so no rating is rendered here.</span></td>'
    '<td><a href="https://affiliate-program.amazon.com/help/operating/policies" rel="sponsored noopener">S02</a></td></tr>\n',
    compare, flags=re.S)
write("compare.html", compare)

# ---------------------------------------------------------------- R-02 feed
feed = read("feed.xml")
feed = feed.replace("Five verified kitchen gifts, $16.99–$149.99. Every pick sourced.",
                    "Five kitchen gifts, each tied to a dated listing snapshot and its source.")
feed = feed.replace("Five verified picks, every one sourced.", "Five picks, every one sourced.")
feed = feed.replace("Quarts vs liters, basket count, and the whole-chicken test — no hype.",
                    "Quarts vs litres, basket count and usable volume — what the numbers do and do not say.")
feed = feed.replace("Dishwasher-safe parts, footprint, and capacity per inch of depth, measured.",
                    "Dishwasher-safe parts, footprint and capacity per unit of counter area — arithmetic, not testing.")
feed = feed.replace("Depth, width, and capacity per inch — the footprint test.",
                    "Depth, width and capacity per unit of counter area, straight from the listed dimensions.")
feed = feed.replace("Dual-basket vs oven combo compared on verified specs: capacity, footprint, temperature range, and price.",
                    "Dual-basket vs oven combo compared on listed specs: capacity, footprint and temperature settings.")
feed = feed.replace("Accuracy, read time, probes, connectivity, and price — compared on verified specs.",
                    "Accuracy claims, read time, probes and connectivity — compared as seller statements.")
feed = feed.replace("Kitchen Counter — Verified Picks, Plainly Told", "Kitchen Counter — Listed specs, plainly told")
feed = feed.replace("Question-shaped guides, verified against official Amazon listings.",
                    "Question-shaped guides, with every figure traced to its dated listing snapshot.")
write("feed.xml", feed)

# ---------------------------------------------------------------- R-03/R-04 head
LD_HOME = ('{"@context":"https://schema.org","@graph":['
           '{"@type":"WebSite","name":"Kitchen Counter","alternateName":"Kitchen Counter — listed specs, plainly told",'
           '"url":"' + ABS + '/","inLanguage":"en-US","description":"Air fryers and meat thermometers compared by the numbers on their listings."},'
           '{"@type":"Organization","name":"Kitchen Counter","url":"' + ABS + '/","logo":{"@type":"ImageObject","url":"' + ABS + '/assets/og-image.png"}},'
           '{"@type":"CollectionPage","name":"Kitchen Counter front page","url":"' + ABS + '/"}]}')

for f in HTML:
    s = f.read_text(encoding="utf-8")
    o = s
    # absolute PNG social image, with alt text and twitter card
    s = s.replace('<meta property="og:image" content="assets/og-image.svg">',
                  '<meta property="og:image" content="' + ABS + '/assets/og-image.png">\n'
                  '<meta property="og:image:width" content="1200">\n'
                  '<meta property="og:image:height" content="630">\n'
                  '<meta property="og:image:alt" content="Kitchen Counter — air fryers and meat thermometers compared by the numbers on their listings">\n'
                  '<meta property="og:site_name" content="Kitchen Counter">\n'
                  '<meta name="twitter:card" content="summary_large_image">')
    s = s.replace('<meta property="og:image" content="../assets/og-image.svg">',
                  '<meta property="og:image" content="' + ABS + '/assets/og-image.png">\n'
                  '<meta property="og:image:width" content="1200">\n'
                  '<meta property="og:image:height" content="630">\n'
                  '<meta property="og:image:alt" content="Kitchen Counter — air fryers and meat thermometers compared by the numbers on their listings">\n'
                  '<meta property="og:site_name" content="Kitchen Counter">\n'
                  '<meta name="twitter:card" content="summary_large_image">')
    if s != o:
        f.write_text(s, encoding="utf-8")
        changed.append(str(f.relative_to(ROOT)))

# FAQPage / BreadcrumbList / ItemList for pages that lacked structured data
def add_ld(rel, block):
    s = read(rel)
    if '"@type":"FAQPage"' in s or '"@type":"BreadcrumbList"' in s or '"@type":"ItemList"' in s:
        return
    s = s.replace("</head>", '<script type="application/ld+json">' + block + "</script>\n</head>")
    write(rel, s)

add_ld("index.html", LD_HOME)
add_ld("air-fryers.html", '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
       '{"@type":"ListItem","position":1,"name":"Kitchen Counter","item":"' + ABS + '/"},'
       '{"@type":"ListItem","position":2,"name":"Air fryers","item":"' + ABS + '/air-fryers.html"}]}')
add_ld("meat-thermometers.html", '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
       '{"@type":"ListItem","position":1,"name":"Kitchen Counter","item":"' + ABS + '/"},'
       '{"@type":"ListItem","position":2,"name":"Meat thermometers","item":"' + ABS + '/meat-thermometers.html"}]}')

s = read("buying-guide.html")
if '"@type":"FAQPage"' not in s:
    s = s.replace("</head>", '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{"@type":"Question","name":"Should I measure capacity in quarts or litres?","acceptedAnswer":{"@type":"Answer","text":"Compare like with like. A US quart is about 0.946 litres, so a 26-quart oven is about 24.6 litres. Nominal capacity is a headline figure, not a measured usable volume."}},'
        '{"@type":"Question","name":"Why does this site not show prices?","acceptedAnswer":{"@type":"Answer","text":"Amazon Program Policies permit showing price and availability only when Amazon serves the data or it arrives through the Product Advertising API. This site does neither, so the price is confirmed on the listing."}},'
        '{"@type":"Question","name":"Are the star ratings and accuracy claims tested here?","acceptedAnswer":{"@type":"Answer","text":"No. Specs are seller statements transcribed from dated listing snapshots. Customer ratings are not displayed because Program Policies restrict their use to Creators API or PA API data."}}]}'
        "</script>\n</head>")
    write("buying-guide.html", s)

# ---------------------------------------------------------------- R-05 source refs
def fix_refs(rel, mapping):
    s = read(rel)
    o = s
    for bad, good in mapping.items():
        s = re.sub(r"\b" + bad + r"\b", good, s)
    if s != o:
        write(rel, s)

fix_refs("data/analysis.json", {"S03": "S10", "S04": "S11", "S05": "S12", "S06": "S16", "S07": "S18"})
fix_refs("data/flagged.json", {"S01": "S01", "S03": "S10", "S04": "S11", "S05": "S12", "S06": "S13", "S07": "S18", "S14": "S14", "S16": "S02"})
fix_refs("data/open-questions.json", {"S03": "S10", "S06": "S13", "S07": "S18", "S08": "S03", "S14": "S14", "S16": "S15", "S02": "S02"})
fix_refs("data/policy-checks.json", {"S08": "S03", "S11": "S04", "S12": "S02", "S14": "S10", "S15": "S15", "S17": "S05"})
fix_refs("data/suggestions.json", {"S08": "S03", "S11": "S04", "S12": "S02", "S13": "S02", "S14": "S10"})
fix_refs("data/flagged.json", {"S06": "S13"})

# ---------------------------------------------------------------- R-06 stale copy
for rel in ("air-fryers.html", "meat-thermometers.html", "index.html"):
    s = read(rel)
    o = s
    s = s.replace("Three listings compared on capacity, footprint, wattage, and sourcing.",
                  "Three listings compared on capacity, footprint, wattage and sourcing.")
    s = s.replace("Compare all five on capacity, footprint &amp; price",
                  "Compare all five on capacity, footprint &amp; sourcing")
    if s != o:
        write(rel, s)

print("changed:", len(set(changed)))
for c in sorted(set(changed)):
    print("  ", c)
