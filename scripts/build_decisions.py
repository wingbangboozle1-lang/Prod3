#!/usr/bin/env python3
"""Render decisions.html from the three data registers plus data/decisions.json.

Why a generated page
--------------------
The brief asks for one place where every outstanding choice can be reviewed and a path
chosen before anything is built. That page must not drift from the registers it
summarises, so it is generated from them:

  data/suggestions.json     -> SG-*  proposals (status, effort, owner)
  data/open-questions.json  -> Q-*   unknowns, with who can answer and the cost
  data/flagged.json         -> F-*   irregularities found during capture
  data/decisions.json       -> DT-*  the choices this page asks the owner to make,
                                     each with the information that would settle it

`--check` exits 1 when the published page no longer matches the data.

Evidence rule for this page
---------------------------
Every DT row carries `sources` (IDs registered in data/sources.json) OR
`sources: []` plus `evidence_status: "unverified"`, in which case the row is rendered
with an explicit "no official source" marker instead of an invented citation. The
release gate enforces both halves; see tools/check_site.py rule P25.
"""
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangboozle1-lang.github.io/Prod3"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://wingbangboozle1-lang.github.io/Prod3/decisions.html">
<title>Decision Desk — What to Choose, and What We Still Don't Know | Kitchen Counter</title>
<meta name="description" content="Every open choice on this site in one place: what we suggest, what it would cost, what is still unknown, and which questions only the account owner can answer.">
<meta property="og:title" content="Decision Desk — What to Choose, and What We Still Don't Know">
<meta property="og:description" content="Suggestions, open questions, missing information and a path chooser, on one page.">
<meta property="og:type" content="article">
<meta property="og:image" content="https://wingbangboozle1-lang.github.io/Prod3/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kitchen Counter decision desk">
<meta property="og:site_name" content="Kitchen Counter">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<link rel="alternate" type="application/rss+xml" title="Kitchen Counter" href="feed.xml">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"Decision Desk","description":"Open choices, unknowns and missing information for Kitchen Counter, published so each can be reviewed before anything is built."}</script>
</head>
<body>
<main id="main"><div class="article" style="max-width:1060px">
"""

TAIL = """</div></main>
<script src="assets/app.js" defer></script>
<script src="assets/decision-desk.js" defer></script>
</body></html>
"""


def esc(v):
    return html.escape(str(v))


def badge(text, kind="grey"):
    return f'<span class="badge {kind}">{esc(text)}</span>'


STATUS_KIND = {"implemented": "green", "proposed": "grey", "partly implemented": "grey",
               "rejected": "grey", "blocking": "grey", "queued": "grey",
               "watch": "grey", "owner-only": "grey"}


def source_links(ids, sources_by_id):
    """Render a source cell from registered IDs. Never invents a link."""
    if not ids:
        return '<span class="unverified">No official source</span>'
    out = []
    for sid in ids:
        s = sources_by_id.get(sid)
        if not s:
            raise SystemExit(f"decisions.html: cites unregistered source {sid}")
        label = f"{sid} — {esc(s['title'][:70])}"
        # Any Amazon property must carry rel="sponsored" on this site, including
        # policy documents that earn no commission. scripts/check_site.py enforces it.
        rel_attr = "sponsored noopener" if "amazon.com" in s["url"] else "noopener"
        out.append(f'<a href="{esc(s["url"])}" rel="{rel_attr}">{label}</a>')
    return "<br>".join(out)


def render():
    suggestions = json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))
    questions = json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))
    flagged = json.loads((ROOT / "data/flagged.json").read_text(encoding="utf-8"))
    decisions = json.loads((ROOT / "data/decisions.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in sources["sources"]}

    # "Open" means proposed: a row that is retired in place is neither open nor
    # shipped, and counting it as open (the earlier behaviour) overstated the
    # work waiting on the owner. "Shipped" includes partly implemented, because
    # part of it is live.
    sg_open = [s for s in suggestions["suggestions"] if s["status"] == "proposed"]
    sg_done = [s for s in suggestions["suggestions"] if s["status"] in ("implemented", "partly implemented")]
    sg_retired = [s for s in suggestions["suggestions"] if s["status"] == "retired"]
    q_all = questions["questions"]
    q_owner = [q for q in q_all if q.get("who") == "owner"]
    q_block = [q for q in q_all if q.get("status") == "blocking"]
    dup = [s for s in suggestions["suggestions"] if s["id"] == "SG-20"]

    parts = []
    parts.append('<p class="kicker">Decision desk</p>')
    parts.append("<h1>What to choose, what it costs, and what nobody has told us yet</h1>")
    parts.append('<p class="byline">Kitchen Counter · Desk updated 2026-11-20 · Nothing on this page is live until it is chosen and built</p>')
    parts.append(
        "<p>This is the review surface. Every open choice on the site is listed once, with the "
        "evidence behind it, the effort it needs, who can decide, and — where the answer does not "
        "exist yet — what would have to be found out first. Pick a row and it becomes work; leave it "
        "and it stays a proposal. Nothing here is quietly half-built.</p>")

    parts.append(f'''<div class="grid cols-4 mt">
  <div class="card"><p class="kicker" style="margin:0">Decisions to make</p><p style="font-size:2rem;font-weight:800;margin:.2em 0 0">{len(decisions["decisions"])}</p><p class="small muted">DT rows below</p></div>
  <div class="card"><p class="kicker" style="margin:0">Proposals open</p><p style="font-size:2rem;font-weight:800;margin:.2em 0 0">{len(sg_open)}</p><p class="small muted">{len(sg_done)} already shipped &middot; {len(sg_retired)} retired in place</p></div>
  <div class="card"><p class="kicker" style="margin:0">Questions unanswered</p><p style="font-size:2rem;font-weight:800;margin:.2em 0 0">{len(q_all)}</p><p class="small muted">{len(q_owner)} need the owner&rsquo;s accounts</p></div>
  <div class="card"><p class="kicker" style="margin:0">Blocking today</p><p style="font-size:2rem;font-weight:800;margin:.2em 0 0">{len(q_block)}</p><p class="small muted">A choice is on hold until answered</p></div>
</div>''')

    # ---- Section 1: the decisions this page asks for
    parts.append('<h2 class="mt">1. The decisions, in order</h2>')
    parts.append('<p>Each row is one choice. The &ldquo;settled by&rdquo; column names the single piece of evidence that would close it — or says plainly that no official source exists and the answer has to come from the account.</p>')
    parts.append('<div class="table-wrap mt"><table data-source-required="decision-evidence">')
    parts.append('<caption>DT-01 onward. Source links point to the registered official document; rows without one are marked, not filled in.</caption>')
    parts.append('<thead><tr><th style="min-width:110px">ID</th><th>Decision</th><th>Recommendation</th><th>Cost / owner</th><th>What settles it (source)</th></tr></thead><tbody>')
    for d in decisions["decisions"]:
        kind = "green" if d["status"] == "shipped" else "grey"
        rec = esc(d["recommendation"])
        parts.append(
            f'<tr><td><strong>{esc(d["id"])}</strong><br>{badge(d["status"], kind)}</td>'
            f'<td><strong>{esc(d["title"])}</strong><br><span class="small muted">{esc(d["why"])}</span></td>'
            f'<td>{rec}<br><span class="small muted">Blocks: {esc(d.get("blocks", "nothing"))}</span></td>'
            f'<td><span class="small">{esc(d.get("effort", "?"))}</span><br><span class="small muted">{esc(d.get("who", "owner"))}</span></td>'
            f'<td class="small">{source_links(d.get("sources", []), by_id)}</td></tr>')
    parts.append('</tbody></table></div>')

    # ---- Section 2: missing information
    parts.append('<h2 class="mt">2. Information we do not have</h2>')
    parts.append('<p>These are gaps, not opinions. For each one: what we know, what we do not, and the cheapest way to find out. An owner answer is worth more than another week of writing, because most of these take minutes inside the Associates or Search Console accounts.</p>')
    parts.append('<div class="table-wrap mt"><table data-source-required="question-register">')
    parts.append('<caption>Q-01 onward, generated from <code>data/open-questions.json</code>. Status meanings are defined in the register. A row marked <em>No official source</em> has nothing in the public record that settles it; it is not a citation we skipped.</caption>')
    parts.append('<thead><tr><th style="min-width:96px">ID</th><th>Question</th><th>Known</th><th>Unknown</th><th>How to find out</th><th>Cost / who</th><th>Source</th></tr></thead><tbody>')
    for q in q_all:
        parts.append(
            f'<tr><td><strong>{esc(q["id"])}</strong><br>{badge(q.get("status", ""), "grey")}</td>'
            f'<td>{esc(q["question"])}</td>'
            f'<td class="small">{esc(q.get("known", "—"))}</td>'
            f'<td class="small">{esc(q.get("unknown", "—"))}</td>'
            f'<td class="small">{esc(q.get("how_to_find_out", "—"))}</td>'
            f'<td class="small">{esc(q.get("cost", "?"))}<br><span class="muted">{esc(q.get("who", "owner"))}</span></td>'
            f'<td class="small">{source_links(q.get("sources", []), by_id)}</td></tr>')
    parts.append('</tbody></table></div>')

    # ---- Section 3: reproduce first, then fix
    parts.append('<h2 class="mt">3. Irregularities, reproduced before they are repaired</h2>')
    parts.append('<p>Both defects below were reproduced here before they were repaired, because a fix nobody can check is just a different story. One is settled; the other still needs a check only the owner can run.</p>')

    parts.append(f'''<div class="callout"><strong>Register defect: reproduced, then resolved the same day.</strong>
Two different identifiers named one proposal: <code>SG-20</code> and <code>SG-21</code> both read
&ldquo;{esc(dup[0]["title"]) if dup else ""}&rdquo;. The same failure — one ID, two meanings — was fixed for the
first eight proposals in an earlier audit, so this was a recurrence, not a one-off. <strong>Settled:</strong> do not
treat SG-21 as an open choice; action SG-20 only.
<strong>What was done:</strong> SG-21 was retired in place rather than deleted, marked as a duplicate of SG-20, and
kept in <a href="suggestions.html">the suggestions register</a> so the change is auditable. A new gate rule
(<code>D20</code>) now fails the build if two live proposals ever share a title again. What the owner may still want
to confirm: that no proposal was <em>displaced</em> by the duplicate — only the owner knows whether a second,
different idea was ever meant to occupy SG-21.</div>''')

    f21 = next((f for f in flagged["items"] if f["id"] == "F-21"), None)
    if f21:
        parts.append(f'''<div class="callout warn"><strong>Unverified preview image.</strong>
{f21["detail"]} We have not confirmed how the social card renders in any previewer, and we are not going to claim it does.
Settled by: running a public share debugger against the live URL and screenshotting the result ({esc(f21["id"])},
<a href="flagged.html">Flagged for Review</a>). Until then the card is a best effort, not a verified asset.</div>''')

    parts.append('<h3 class="mt">What we could not confirm at all</h3>')
    parts.append('<div class="table-wrap"><table><caption>The F-register, from <code>data/flagged.json</code>. Severity is the capture author&rsquo;s judgement, not a computed score.</caption>')
    parts.append('<thead><tr><th style="min-width:80px">ID</th><th>Area</th><th>What happened</th><th>Why it matters</th><th>Source</th></tr></thead><tbody>')
    for f in flagged["items"]:
        parts.append(
            f'<tr><td><strong>{esc(f["id"])}</strong><br><span class="small muted">{esc(f.get("severity",""))}</span></td>'
            f'<td class="small">{esc(f.get("area",""))}</td>'
            f'<td class="small">{esc(f.get("detail",""))}</td>'
            f'<td class="small">{esc(f.get("why_it_matters",""))}</td>'
            f'<td class="small">{source_links(f.get("sources", []), by_id)}</td></tr>')
    parts.append('</tbody></table></div>')

    # ---- Section 4: path chooser
    parts.append('<h2 class="mt">4. Choose a path</h2>')
    parts.append('<p>Three coherent routes. Each one is costed, each one says what it delays, and none of them requires a decision you cannot reverse. Naming a path does not change the site by itself — it goes into the decision log first.</p>')
    parts.append('<div class="grid cols-3 mt">')
    for path in decisions["paths"]:
        feats = "".join(f"<li>{esc(x)}</li>" for x in path["includes"])
        delays = "".join(f"<li>{esc(x)}</li>" for x in path["delays"])
        parts.append(f'''<article class="card path-card" data-path="{esc(path["id"])}">
  <span class="badge">{esc(path["id"])}</span>
  <h3>{esc(path["name"])}</h3>
  <p>{esc(path["summary"])}</p>
  <p class="small"><strong>Includes</strong></p><ul class="small">{feats}</ul>
  <p class="small"><strong>Delays</strong></p><ul class="small">{delays}</ul>
  <p class="small muted"><strong>Cost:</strong> {esc(path["cost"])}</p>
  <p class="small muted"><strong>Best if:</strong> {esc(path["best_if"])}</p>
  <p><button type="button" class="btn ghost" data-choose-path="{esc(path["id"])}">Record {esc(path["id"])} as the chosen path</button></p>
</article>''')
    parts.append('</div>')
    parts.append('''<div class="callout mt" id="path-status" role="status" aria-live="polite">
<strong>No path recorded yet.</strong> This button writes your choice to this browser only, so the page can show
what you picked while you read. It is not a server record and it is not a commitment: the real record is the
decision log, which is edited by hand and dated. Nothing on this site is transmitted anywhere.</div>''')

    # ---- Section 5: what is already decided
    parts.append('<h2 class="mt">5. Already shipped, so you can see the pattern</h2>')
    parts.append('<p>These are not proposals. They are the calls already made and built, listed so the register is complete and any of them can be reversed on purpose.</p>')
    parts.append('<div class="grid cols-2 mt">')
    for s in sg_done:
        parts.append(f'<article class="card"><div class="meta">{esc(s["id"])} · {esc(s.get("decision_owner","editorial"))}</div>'
                     f'<h3 style="font-size:1rem">{esc(s["title"])}</h3>'
                     f'<p class="small muted" style="margin:0">{esc(s.get("recommendation",""))[:240]}</p></article>')
    parts.append('</div>')

    parts.append('''<div class="read-next">
  <h3>Where the detail lives</h3>
  <ul>
    <li><a href="suggestions.html">The suggestions register</a> — every SG row with options and evidence</li>
    <li><a href="questions.html">The open-questions register</a> — the same Q rows, one per page</li>
    <li><a href="direction.html">The decision log</a> — dated rows and the source each rests on</li>
    <li><a href="flagged.html">Flagged for Review</a> — the FLG register for readers</li>
  </ul>
</div>''')

    return HEAD + "\n".join(parts) + "\n" + TAIL


if __name__ == "__main__":
    # Apply the shared chrome so this builder's output is identical to what the
    # chrome pass would produce. Without this the two builders fight over the same
    # bytes and each one's --check fails after the other runs.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_chrome

    html_out = build_chrome.render(render(), "decisions.html", 0)
    target = ROOT / "decisions.html"
    if "--check" in sys.argv:
        cur = target.read_text(encoding="utf-8") if target.exists() else ""
        if cur != html_out:
            print("FAIL: decisions.html is stale. Run: python3 scripts/build_decisions.py")
            sys.exit(1)
        print("OK: decisions.html matches its data")
    else:
        target.write_text(html_out, encoding="utf-8")
        print(f"Wrote decisions.html ({len(html_out.splitlines())} lines)")
