#!/usr/bin/env python3
"""Render the decision registers from their JSON files.

  data/suggestions.json  -> suggestions.html   (SG-01..SG-nn)
  data/open-questions.json -> questions.html   (Q-01..Q-nn)
  data/citations.json    -> citations.html     (product + policy rows)
  data/flagged.json      -> flagged.html       (F-01..F-nn table)

The JSON is the single source of truth. `--check` exits 1 when the published
page no longer matches the data, so a stale register cannot ship.

Session a25ccde6 added this builder after finding that direction.html carried
its own SG-01..SG-08 with different meanings from data/suggestions.json: the
same identifier named two different proposals on one site.

Session arena/0a1638a1-prod3 added the F-register splice after the audit found
that F-01..F-21 lived only in data/flagged.json while five public pages
referred to F-numbers a reader could not follow to anything.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangboozle1-lang.github.io/Prod3"
TRACKING = "shopnow047c-20"

DISCLOSURE = ('<div class="disclosure" role="note"><div class="wrap"><strong>Affiliate disclosure:</strong> '
              'As an Amazon Associate I earn from qualifying purchases. If a qualifying purchase is credited, '
              'Kitchen Counter may earn a commission at no extra cost to you. Tracking ID: '
              f'<strong>{TRACKING}</strong>. Prices change — confirm on Amazon. '
              '<a href="flagged.html">Flagged for Review</a> · <a href="disclosure.html">Full disclosure</a>.</div></div>')

def head(title, desc, slug):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="{BASE}/{slug}">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{BASE}/{slug}">
<meta property="og:image" content="{BASE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kitchen Counter — air fryers and meat thermometers compared by the numbers on their listings">
<meta property="og:site_name" content="Kitchen Counter">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<link rel="alternate" type="application/rss+xml" title="Kitchen Counter" href="feed.xml">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead"><div class="wrap">
  <a class="brand" href="index.html">Kitchen Counter<small>Listed specs, plainly told</small></a>
  <nav class="nav" aria-label="Primary">
    <a href="index.html">Front page</a><a href="air-fryers.html">Air fryers</a><a href="meat-thermometers.html">Thermometers</a><a href="compare.html">Compare</a><a href="buying-guide.html">Buying guide</a><a href="direction.html" aria-current="page">Direction</a>
  </nav>
</div></header>
{DISCLOSURE}
'''

FOOTER = f'''<footer><div class="wrap">
  <div class="cols">
    <div><h4>Kitchen Counter</h4><p>Listed specs, plainly told. Seller-stated details cite the official listing; contradictions stay visible.</p>
      <p id="local-counts" class="small">Local counts: loading…</p>
      <p class="small">Follow new guides with the <a href="feed.xml">RSS feed</a>.</p></div>
    <div><h4>Shop</h4><ul><li><a href="air-fryers.html">Air fryers</a></li><li><a href="meat-thermometers.html">Meat thermometers</a></li><li><a href="compare.html">Compare all five</a></li><li><a href="buying-guide.html">Buying guide</a></li></ul></div>
    <div><h4>Guides</h4><ul><li><a href="articles/basket-or-oven-air-fryer.html">Basket or oven?</a></li><li><a href="articles/air-fryer-capacity-checklist.html">Capacity checklist</a></li><li><a href="articles/cleanup-counter-space.html">Cleanup &amp; space</a></li><li><a href="articles/questions-before-multi-function.html">Before you buy</a></li></ul></div>
    <div><h4>Trust</h4><ul><li><a href="disclosure.html">Disclosure</a></li><li><a href="sources.html">Source register</a></li><li><a href="citations.html">Citation log</a></li><li><a href="flagged.html">Flagged for review</a></li><li><a href="suggestions.html">Suggestions</a></li><li><a href="questions.html">Open questions</a></li><li><a href="direction.html">Decision log</a></li><li><a href="analytics.html">Analytics &amp; privacy</a></li><li><a href="executive-summary.html">Executive summary</a></li><li><a href="about.html">About</a></li></ul></div>
  </div>
<p class="foot-disclosure"><strong>Affiliate disclosure:</strong> As an Amazon Associate I earn from qualifying purchases. Tracking ID: {TRACKING}. If a qualifying purchase is credited, Kitchen Counter may earn a commission at no extra cost to you. Account status and short-link compliance remain unverified (FLG-006/010) — details in Flagged for Review. Amazon and the Amazon logo are trademarks of Amazon.com, Inc. or its affiliates.</p></div></footer>
<script src="assets/app.js" defer></script>
</body></html>
'''

def pill(text, kind="grey"):
    return f'<span class="badge {kind}">{html.escape(text)}</span>'


_F_REF = re.compile(r"(?<![A-Za-z0-9])F-\d{2}(?![0-9])")


def link_findings(text):
    """Turn F-nn references into links to the published row on flagged.html.

    Every F-number in a register must be followable. The row it points at is
    generated from data/flagged.json, so the link is correct by construction.
    """
    return _F_REF.sub(lambda m: f'<a href="flagged.html#{m.group(0)}">{m.group(0)}</a>', text)

STATUS_KIND = {"implemented": "green", "proposed": "grey", "rejected": "grey", "in progress": "grey",
               "partly implemented": "grey"}
EFFORT = {"S": "Short session", "M": "Focused day", "L": "Project"}


def render_suggestions():
    data = json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))
    items = data["suggestions"]
    shipped = [s for s in items if s["status"] == "implemented"]
    open_items = [s for s in items if s["status"] != "implemented"]

    def card(s):
        opts = "".join(f"<li>{html.escape(o)}</li>" for o in s.get("options", []))
        kind = STATUS_KIND.get(s["status"], "grey")
        return f'''<article class="card">
      <div class="meta">{html.escape(s["id"])} · {html.escape(s.get("decision_owner", "owner"))} decides</div>
      <h3>{html.escape(s["title"])}</h3>
      <p><strong>Problem.</strong> {link_findings(html.escape(s.get("problem", "")))}</p>
      <p><strong>Evidence.</strong> {link_findings(html.escape(s.get("evidence", "")))}</p>
      <p><strong>Options.</strong></p><ul>{opts}</ul>
      <p><strong>Recommendation.</strong> {link_findings(html.escape(s.get("recommendation", "")))}</p>
      <p>{pill(s["status"], kind)} {pill("Effort " + s.get("effort", "?"), "grey")} {pill("Confidence " + s.get("confidence", "?"), "grey")}</p>
      <p class="small muted">Blocks: {link_findings(html.escape(s.get("blocks", "nothing")))}</p>
    </article>'''

    body = f'''<main id="main"><div class="article" style="max-width:1000px">
<p class="kicker">Direction · Suggestions register</p>
<h1>Suggestions, and the decision each one waits on</h1>
<p class="byline">Kitchen Counter · Register updated 2026-11-19 · Nothing here is implemented by being listed</p>

<p>This is the review desk. Every proposal carries its problem, the evidence behind it, the options considered, a recommendation, and the person who decides. Machine-readable copy: <code>data/suggestions.json</code>. The questions that block these proposals live on <a href="questions.html">Open questions</a>; what was actually decided is on the <a href="direction.html">decision log</a>.</p>

<div class="callout"><strong>How to read the status.</strong> <em>Implemented</em> means the change is live on the site today. <em>Partly implemented</em> means part of the change is live and the remainder is tracked as an open question or flag — the row says which. <em>Proposed</em> means it is waiting for a decision and has no effect yet. Nothing in the proposed column has been quietly half-built.</div>

<h2>Waiting on a decision ({len(open_items)})</h2>
<div class="grid mt">{''.join(card(s) for s in open_items)}</div>

<h2 class="mt">Already shipped ({len(shipped)})</h2>
<p>Listed so the register stays complete, not to take credit. Each one can be reverted if a decision goes the other way.</p>
<div class="grid mt">{''.join(card(s) for s in shipped)}</div>

<h2 class="mt">How a suggestion becomes a change</h2>
<ol>
  <li>It appears here with an ID, a problem, and a recommendation.</li>
  <li>An owner decision is recorded in <a href="direction.html">the decision log</a> with a date and a source.</li>
  <li>The change is made, and the status here moves to <em>implemented</em> on the same day.</li>
  <li>If the decision was to do nothing, it is recorded as rejected with the reason. Silence is not a decision.</li>
</ol>

<p class="mt"><a href="questions.html">Open questions →</a> · <a href="direction.html">Decision log and path chooser →</a></p>
</div></main>

'''
    return (head("Suggestions Register — What to Change and What It Waits On | Kitchen Counter",
                 "Every proposed change to Kitchen Counter with its problem, evidence, options, recommendation and decision owner, plus what has already shipped.",
                 "suggestions.html") + body + FOOTER)


def render_questions():
    data = json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))
    qs = data["questions"]
    groups = {}
    for q in qs:
        groups.setdefault(q["group"], []).append(q)

    def row(q):
        return f'''<tr>
  <td><strong>{html.escape(q["id"])}</strong></td>
  <td><strong>{html.escape(q["question"])}</strong><br><span class="small muted">Blocks: {link_findings(html.escape(q.get("blocks", "—")))}</span></td>
  <td><span class="small">{link_findings(html.escape(q.get("known", "—")))}</span></td>
  <td><span class="small">{link_findings(html.escape(q.get("unknown", "—")))}</span></td>
  <td><span class="small">{link_findings(html.escape(q.get("how_to_find_out", "—")))}</span></td>
  <td><span class="small">{html.escape(q.get("who", "—"))} · {html.escape(q.get("cost", "—"))}</span><br><span class="badge grey">{html.escape(q.get("status", "—"))}</span></td>
</tr>'''

    sections = []
    for g, items in groups.items():
        rows = "\n".join(row(q) for q in items)
        sections.append(f'''<h2>{html.escape(g)} ({len(items)})</h2>
<div class="table-wrap"><table>
<thead><tr><th>ID</th><th>Question</th><th>What we know</th><th>What we do not know</th><th>How to find out</th><th>Who · cost</th></tr></thead>
<tbody>
{rows}
</tbody></table></div>''')

    body = f'''<main id="main"><div class="article" style="max-width:1100px">
<p class="kicker">Direction · Open questions</p>
<h1>The questions that have to be answered before the next decision</h1>
<p class="byline">Kitchen Counter · Register updated 2026-11-19 · {len(qs)} open questions, grouped by what they block</p>

<p>A decision made on missing information is a guess with better manners. Each row states what is known, what is not, why it matters, and the cheapest concrete action that would settle it. Machine-readable copy: <code>data/open-questions.json</code>.</p>

<div class="callout"><strong>Read this first.</strong> Several rows can only be answered from inside the Associates account — they are marked <em>owner-only</em>. They are not blockers for publishing; they are blockers for claiming that the site earns anything. Nothing on this site presents a conversion rate, revenue figure, or ranking, because the data behind those figures does not exist yet.</div>

{''.join(sections)}

<h2>What would change if these were answered</h2>
<div class="table-wrap"><table>
<thead><tr><th>If this is answered</th><th>This changes</th></tr></thead>
<tbody>
<tr><td>Q-02 tag present on the supplied links</td><td>The site can drive traffic without losing attribution. If absent, every outbound link is regenerated before any promotion.</td></tr>
<tr><td>Q-04 short-link format acceptable in the enrolled workflow</td><td>Whether product buttons keep the supplied <code>link.amazon</code> destinations or move to direct <code>amazon.com/dp/</code> URLs with the tag.</td></tr>
<tr><td>Q-05 named author and experience</td><td>Whether first-hand testing becomes a real claim. Until then no experience claim is made anywhere.</td></tr>
<tr><td>Q-07 analytics that can be installed</td><td>Whether the next article is chosen from measured queries or from a hypothesis.</td></tr>
<tr><td>Q-14 cadence and who writes</td><td>Whether the publication keeps a schedule, and whether it can promise one.</td></tr>
</tbody></table></div>

<p class="mt"><a href="suggestions.html">← Suggestions register</a> · <a href="direction.html">Decision log and path chooser →</a></p>
</div></main>

'''
    return (head("Open Questions — What Blocks the Next Decision | Kitchen Counter",
                 "Every open question behind Kitchen Counter: what is known, what is unknown, how to find out, and which decision it blocks.",
                 "questions.html") + body + FOOTER)




# --------------------------------------------------------------------------
# citations.html — every rendered figure and where it came from
# --------------------------------------------------------------------------
def render_citations():
    cites = json.loads((ROOT / "data/citations.json").read_text(encoding="utf-8"))
    srcs = {s["id"]: s for s in json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]}
    prod = [c for c in cites["citations"] if c["product"] != "site"]
    policy = [c for c in cites["citations"] if c["product"] == "site"]

    def src_cell(c):
        s = srcs.get(c["source"])
        if not s:
            return "missing source"
        return f'<a href="{html.escape(s["url"])}" rel="sponsored noopener">{html.escape(c["source"])}</a>'

    prod_rows = "\n".join(
        f'<tr><td><strong>{html.escape(c["product"])}</strong><br><span class="small muted">{html.escape(c["asin"])}</span></td>'
        f'<td>{html.escape(c["brand"])}</td><td>{html.escape(c["observed"])}</td>'
        f'<td>{src_cell(c)}</td><td>{html.escape(c["observed_on"])}</td>'
        f'<td><span class="small">{html.escape(c["claim_status"])}</span></td></tr>' for c in prod)

    pol_rows = "\n".join(
        f'<tr><td>{src_cell(c)}</td><td><span class="small">{html.escape(c["observed"])}</span></td>'
        f'<td><span class="small muted">{html.escape(c["claim_status"])}</span></td></tr>' for c in policy)

    body = f'''<main id="main"><div class="article" style="max-width:1050px">
<p class="kicker">Trust · Citation log</p>
<h1>Every figure on this site, and the observation behind it</h1>
<p class="byline">Kitchen Counter · Log generated 2026-11-19 · Machine-readable copy in <code>data/citations.json</code></p>

<p>The <a href="sources.html">source register</a> lists the pages we read. This log is the other half: one row per figure the site renders, naming the observation, its date, and the official page it came from. If a figure has no row here, it does not belong on the site.</p>

<div class="callout"><strong>The rule, stated plainly.</strong> A value is published only if it traces to (a) a dated fetch of the official listing, (b) a dated fetch of an official policy page, or (c) arithmetic over (a) that shows its inputs. Everything else is left blank and published on <a href="flagged.html">Flagged for Review</a>. No price or availability value is rendered, so none appears here.</div>

<h2>Product figures</h2>
<div class="table-wrap"><table>
<thead><tr><th>Product</th><th>Brand</th><th>Observation (2026-11-19)</th><th>Source</th><th>Date</th><th>Claim status</th></tr></thead>
<tbody>
{prod_rows}
</tbody></table></div>
<p class="small muted mt">A seller statement is what the listing says. It is not a measurement performed by this site. Where a listing contradicts itself, both readings stay on the page and the conflict is recorded on <a href="flagged.html">Flagged for Review</a>.</p>

<h2>Policy and guidance rows</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>What it is cited for</th><th>How it is used</th></tr></thead>
<tbody>
{pol_rows}
</tbody></table></div>

<h2>What is deliberately not here</h2>
<ul>
<li><strong>Prices and availability.</strong> Program Policies §2(b) permits them only when Amazon serves the data or they arrive through Creators/PA API. Neither applies, so no price is rendered and none is logged as a published figure.</li>
<li><strong>Customer star ratings.</strong> Program Policies Participation Requirements §2(t) permits customer reviews and star ratings only when obtained through Creators API or PA API. They were removed from this site on 2026-11-19.</li>
<li><strong>Revenue, conversion rates, traffic.</strong> No first-party report exists. The ledger is empty by design.</li>
<li><strong>Product photography.</strong> No licensed photography is used; the cards are typographic art built from listed specs.</li>
</ul>

<p class="mt"><a href="sources.html">← Source register</a> · <a href="flagged.html">Flagged for Review →</a></p>
</div></main>

'''
    return (head("Citation Log — Every Figure and Its Source | Kitchen Counter",
                 "One row per figure Kitchen Counter publishes: the observation, its date, the official page it came from, and whether it is a seller statement or tested result.",
                 "citations.html") + body + FOOTER)


# --------------------------------------------------------------------------
# flagged.html — the F-register (F-01..F-nn)
#
# The FLG-series above the marker is hand-written prose about decisions and
# compliance state. The F-series is the source-and-status register: one row per
# finding, with the official sources behind it. The two series stay separate —
# F-numbers are findings with sources, FLG-numbers are decisions and open
# compliance questions. Every public F-nn reference on the site points at a row
# here, so a reader can follow the number to the evidence.
# --------------------------------------------------------------------------
F_START = "<!-- F-REGISTER:START -->"
F_END = "<!-- F-REGISTER:END -->"
SEVERITY_KIND = {"high": "warn", "medium": "", "low": "grey"}


def render_f_register():
    data = json.loads((ROOT / "data/flagged.json").read_text(encoding="utf-8"))
    srcs = {s["id"]: s for s in
            json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]}
    items = data["items"]

    def src_cell(it):
        cells = []
        for sid in it.get("sources", []):
            s = srcs.get(sid)
            if s is None:
                cells.append(f'<span class="muted small">{html.escape(sid)}</span>')
                continue
            rel = "sponsored noopener" if "amazon.com" in s["url"] else "noopener"
            cells.append(f'<a href="{html.escape(s["url"])}" rel="{rel}">{html.escape(sid)}</a>')
        return " · ".join(cells) or '<span class="muted small">none recorded</span>'

    rows = []
    for it in items:
        sev = it.get("severity", "low")
        kind = SEVERITY_KIND.get(sev, "grey")
        badge = f'<span class="badge {kind}">{html.escape(sev)}</span>' if kind else \
                f'<span class="badge">{html.escape(sev)}</span>'
        why = it.get("why_it_matters", "")
        action = it.get("action", "")
        rows.append(
            f'<tr id="{html.escape(it["id"])}">'
            f'<td><strong>{html.escape(it["id"])}</strong></td>'
            f'<td>{badge}</td>'
            f'<td><span class="small">{html.escape(it.get("area", ""))}</span></td>'
            f'<td><span class="small">{html.escape(it.get("product", ""))}</span></td>'
            f'<td><span class="small">{html.escape(it.get("detail", ""))}</span>'
            + (f'<br><span class="small muted">Why it matters: {html.escape(why)}</span>' if why else "")
            + (f'<br><span class="small muted">Action: {html.escape(action)}</span>' if action else "")
            + '</td>'
            f'<td><span class="small">{html.escape(it.get("status", ""))}</span></td>'
            f'<td><span class="small">{src_cell(it)}</span></td>'
            '</tr>')

    return (
        '<h2>Source-and-status register (F-01 … F-%02d)</h2>\n' % len(items)
        + '<p class="small muted">Every finding below carries the official pages it rests on, so a reader can follow a number '
          'to the evidence rather than taking the site\'s word for it. These are the <strong>F-series</strong>; the '
          '<strong>FLG-series</strong> above is the decision and compliance state that sits on top of them. The two series '
          'are kept apart on purpose: an FLG entry says what the site decided to do about something, an F entry says what was '
          'found and what it rests on. Machine-readable copy: <code>data/flagged.json</code>.'
          '</p>\n'
        + '<div class="table-wrap"><table data-source-required="source-register">\n'
          '<thead><tr><th>ID</th><th>Severity</th><th>Area</th><th>Product</th><th>What was found</th>'
          '<th>Status</th><th>Sources</th></tr></thead>\n<tbody>\n'
        + "\n".join(rows)
        + '\n</tbody></table></div>\n')


def splice_flagged():
    """Return flagged.html with the F-register replaced, or None if unchanged."""
    path = ROOT / "flagged.html"
    if not path.exists():
        return None
    current = path.read_text(encoding="utf-8")
    if F_START not in current or F_END not in current:
        raise SystemExit("flagged.html is missing the F-REGISTER markers")
    start = current.index(F_START)
    end = current.index(F_END)
    block = F_START + "\n" + render_f_register() + F_END
    updated = current[:start] + block + current[end + len(F_END):]
    return None if updated == current else updated


# --------------------------------------------------------------------------
# direction.html — the SG and Q snapshots
#
# The Direction page carries a compact snapshot of the two decision registers.
# It used to be hand-written, which is how SG-19's title drifted away from
# data/suggestions.json and how SG-20 onwards went missing. Both snapshots are
# now spliced from the same JSON the full registers are generated from, so an
# identifier cannot mean two different things on two pages.
# --------------------------------------------------------------------------
SG_SNAP_START = "<!-- SG-SNAPSHOT:START -->"
SG_SNAP_END = "<!-- SG-SNAPSHOT:END -->"
Q_SNAP_START = "<!-- Q-SNAPSHOT:START -->"
Q_SNAP_END = "<!-- Q-SNAPSHOT:END -->"


def render_sg_snapshot():
    items = json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))["suggestions"]
    rows = []
    for s in items:
        kind = STATUS_KIND.get(s["status"], "grey")
        rows.append(
            f'<tr><td><strong>{html.escape(s["id"])}</strong></td>'
            f'<td>{html.escape(s["title"])}<br>'
            f'<span class="muted small">{html.escape(s.get("problem", ""))}</span></td>'
            f'<td><span class="badge {kind}">{html.escape(s["status"])}</span></td>'
            f'<td>{html.escape(s.get("effort", "?"))}</td>'
            f'<td>{html.escape(s.get("confidence", "?"))}</td>'
            f'<td>{html.escape(s.get("decision_owner", "owner"))}</td></tr>')
    return ('<div class="table-wrap"><table>\n'
            '<thead><tr><th>#</th><th>Suggestion</th><th>Status</th><th>Effort</th><th>Confidence</th>'
            '<th>Decided by</th></tr></thead>\n<tbody>\n'
            + "\n".join(rows) + '\n</tbody></table></div>\n')


def render_q_snapshot():
    qs = json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))["questions"]
    rows = []
    for q in qs:
        rows.append(
            f'<tr><td><strong>{html.escape(q["id"])}</strong></td>'
            f'<td>{html.escape(q["question"])}</td>'
            f'<td><span class="pill">{html.escape(q.get("who", "owner"))}</span></td>'
            f'<td>{html.escape(q.get("status", "—"))}</td>'
            f'<td>{link_findings(html.escape(q.get("how_to_find_out", "—")))}</td></tr>')
    return ('<div class="table-wrap"><table>\n'
            '<thead><tr><th>#</th><th>Question</th><th>Who can answer</th><th>Status</th>'
            '<th>How to find out</th></tr></thead>\n<tbody>\n'
            + "\n".join(rows) + '\n</tbody></table></div>\n')


def splice_direction():
    """Return direction.html with both snapshots replaced, or None if unchanged."""
    path = ROOT / "direction.html"
    if not path.exists():
        return None
    current = path.read_text(encoding="utf-8")
    blocks = [(SG_SNAP_START, SG_SNAP_END, render_sg_snapshot()),
              (Q_SNAP_START, Q_SNAP_END, render_q_snapshot())]
    updated = current
    for start_marker, end_marker, body in blocks:
        if start_marker not in updated or end_marker not in updated:
            raise SystemExit(f"direction.html is missing the {start_marker} markers")
        start = updated.index(start_marker)
        end = updated.index(end_marker)
        block = start_marker + "\n" + body + end_marker
        updated = updated[:start] + block + updated[end + len(end_marker):]
    return None if updated == current else updated


def main():
    outputs = {
        "suggestions.html": render_suggestions(),
        "questions.html": render_questions(),
        "citations.html": render_citations(),
    }
    flagged_new = splice_flagged()
    direction_new = splice_direction()
    if "--check" in sys.argv:
        stale = [n for n, t in outputs.items()
                 if not (ROOT / n).exists() or (ROOT / n).read_text(encoding="utf-8") != t]
        if flagged_new is not None:
            stale.append("flagged.html (F-register)")
        if direction_new is not None:
            stale.append("direction.html (SG/Q snapshots)")
        if stale:
            print("FAIL: register pages out of date: " + ", ".join(stale))
            print("Run: python3 scripts/build_registers.py")
            sys.exit(1)
        print("OK: register pages match data/*.json")
        return
    for name, txt in outputs.items():
        (ROOT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}")
    if flagged_new is not None:
        (ROOT / "flagged.html").write_text(flagged_new, encoding="utf-8")
        print("wrote flagged.html (F-register)")
    if direction_new is not None:
        (ROOT / "direction.html").write_text(direction_new, encoding="utf-8")
        print("wrote direction.html (SG/Q snapshots)")


if __name__ == "__main__":
    main()
