#!/usr/bin/env python3
"""Render the two decision registers from their JSON files.

  data/suggestions.json  -> suggestions.html   (SG-01..SG-nn)
  data/open-questions.json -> questions.html   (Q-01..Q-nn)

The JSON is the single source of truth. `--check` exits 1 when the published
page no longer matches the data, so a stale register cannot ship.

Session a25ccde6 added this builder after finding that direction.html carried
its own SG-01..SG-08 with different meanings from data/suggestions.json: the
same identifier named two different proposals on one site.
"""
import html
import json
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

DECIDE_SCRIPT = '''<script>
(function(){
  var KEY='kc-decisions-v1', LABEL={do:'Do this',maybe:'Maybe',no:'No'};
  var store={}; try{ store=JSON.parse(localStorage.getItem(KEY)||'{}'); }catch(e){ store={}; }
  function save(){ try{ localStorage.setItem(KEY, JSON.stringify(store)); }catch(e){} }
  var out=document.getElementById('decide-out');
  function render(){
    if(!out) return;
    var ids=Object.keys(store);
    if(!ids.length){ out.textContent='No marks yet. Choose Do this / Maybe / No on a card above.'; return; }
    var head='Decisions ('+new Date().toISOString().slice(0,10)+'):';
    out.textContent=[head].concat(ids.map(function(id){ return id+' = '+LABEL[store[id]]; })).join(String.fromCharCode(10));
  }
  Array.prototype.forEach.call(document.querySelectorAll('[data-decide]'), function(group){
    var id=group.getAttribute('data-decide');
    Array.prototype.forEach.call(group.querySelectorAll('button'), function(btn){
      var v=btn.getAttribute('data-v');
      if(store[id]===v) btn.setAttribute('aria-pressed','true');
      btn.addEventListener('click', function(){
        if(store[id]===v){ delete store[id]; } else { store[id]=v; }
        Array.prototype.forEach.call(group.querySelectorAll('button'), function(b){
          b.setAttribute('aria-pressed', store[id]===b.getAttribute('data-v') ? 'true':'false');
        });
        save(); render();
      });
    });
  });
  var cp=document.getElementById('decide-copy');
  if(cp) cp.addEventListener('click', function(){
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(out.textContent);
      cp.textContent='Copied'; setTimeout(function(){ cp.textContent='Copy this block'; },1500);
    }
  });
  var cl=document.getElementById('decide-clear');
  if(cl) cl.addEventListener('click', function(){
    store={}; save();
    Array.prototype.forEach.call(document.querySelectorAll('[data-decide] button'), function(b){ b.setAttribute('aria-pressed','false'); });
    render();
  });
  render();
})();
</script>
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

STATUS_KIND = {"implemented": "green", "proposed": "grey", "rejected": "grey", "retired": "grey",
               "in progress": "grey", "partly implemented": "grey"}
EFFORT = {"S": "Short session", "M": "Focused day", "L": "Project"}


def render_suggestions():
    data = json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))
    items = data["suggestions"]
    shipped = [s for s in items if s["status"] == "implemented"]
    open_items = [s for s in items if s["status"] != "implemented"]

    def card(s):
        opts = "".join(f"<li>{html.escape(o)}</li>" for o in s.get("options", []))
        kind = STATUS_KIND.get(s["status"], "grey")
        dec = s.get("decision") or {}
        money = ""
        if dec:
            money = (f'<p class="small"><strong>Why it matters for the money:</strong> {html.escape(dec.get("benefit",""))}</p>'
                     f'<p class="small"><strong>What could go wrong:</strong> {html.escape(dec.get("risk",""))}</p>'
                     f'<p class="small"><strong>Reversible:</strong> {html.escape(str(dec.get("reversible","unknown")))}'
                     f' · <strong>What would prove it wrong:</strong> {html.escape(dec.get("falsifier","not stated"))}</p>')
        choices = "".join(f'<button type="button" data-v="{k}" aria-pressed="false">{v}</button>'
                          for k, v in (("do", "Do this"), ("maybe", "Maybe"), ("no", "No")))
        return f'''<article class="card decision-card" id="{html.escape(s["id"])}">
      <div class="meta">{html.escape(s["id"])} · {html.escape(s.get("decision_owner", "owner"))} decides</div>
      <h3>{html.escape(s["title"])}</h3>
      <p><strong>The situation.</strong> {html.escape(s.get("problem", ""))}</p>
      <p><strong>The evidence.</strong> {html.escape(s.get("evidence", ""))}</p>
      <p>{pill(s["status"], kind)} {pill("Effort " + s.get("effort", "?"), "grey")} {pill("Confidence " + s.get("confidence", "?"), "grey")}</p>
      <details><summary>The options and the recommendation</summary><ul>{opts}</ul>
        <p><strong>Recommendation.</strong> {html.escape(s.get("recommendation", ""))}</p></details>
      <div class="decide-box">{money}
        <div class="opts" data-decide="{html.escape(s["id"])}">{choices}</div>
      </div>
      <p class="small muted">Unblocks: {html.escape(s.get("blocks", "nothing"))}</p>
    </article>'''

    body = f'''<main id="main"><div class="article" style="max-width:1000px">
<p class="kicker">Direction · Suggestions register</p>
<h1>Suggestions, and the decision each one waits on</h1>
<p class="byline">Kitchen Counter · Register updated {data['generated']} · Nothing here is implemented by being listed</p>

<p>This is the review desk. Every proposal carries its problem, the evidence behind it, the options considered, a recommendation, and the person who decides. Machine-readable copy: <code>data/suggestions.json</code>. The questions that block these proposals live on <a href="questions.html">Open questions</a>; what was actually decided is on the <a href="direction.html">decision log</a>.</p>

<div class="callout"><strong>How to use this page.</strong> Read a card, then mark it. The block at the bottom collects your marks into text you can paste back into a session or a document. <strong>Implemented</strong> means it is live today; <strong>retired</strong> means it was decided against and the row keeps the reason; <strong>proposed</strong> means it has no effect until someone chooses.</div>
<div class="callout"><strong>How to read the status.</strong> <em>Implemented</em> means the change is live on the site today. <em>Partly implemented</em> means part of the change is live and the remainder is tracked as an open question or flag — the row says which. <em>Proposed</em> means it is waiting for a decision and has no effect yet. Nothing in the proposed column has been quietly half-built.</div>

<h2>Waiting on a decision ({len(open_items)})</h2>
<div class="grid mt">{''.join(card(s) for s in open_items)}</div>

<h2 class="mt">Already shipped ({len(shipped)})</h2>
<p>Listed so the register stays complete, not to take credit. Each one can be reverted if a decision goes the other way.</p>
<div class="grid mt">{''.join(card(s) for s in shipped)}</div>

<h2 class="mt" id="decide">Your decision block</h2>
<p>Mark a card <em>Do this</em>, <em>Maybe</em> or <em>No</em>. The marks stay in this browser and
appear here as one block of text you can copy back. A mark is a preference; nothing is implemented
by being marked.</p>
<div class="card"><pre id="decide-out" class="decide-out">No marks yet. Choose Do this / Maybe / No on a card above.</pre>
<p class="small"><button type="button" class="btn ghost" id="decide-copy">Copy this block</button> <button type="button" class="btn ghost" id="decide-clear">Clear my marks</button></p>
<p class="small muted">Stored only in this browser under <code>kc-decisions-v1</code>. No cookie, no identifier, no request to any server.</p></div>

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
                 "suggestions.html") + body + DECIDE_SCRIPT + FOOTER)


def render_questions():
    data = json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))
    qs = data["questions"]
    groups = {}
    for q in qs:
        groups.setdefault(q["group"], []).append(q)

    src_by_id = {s["id"]: s for s in json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]}

    def qsource(q):
        ids = q.get("sources", [])
        if not ids:
            return '<span class="unverified">No official source</span>'
        out = []
        for sid in ids:
            s = src_by_id.get(sid)
            if not s:
                raise SystemExit(f"questions.html: cites unregistered source {sid}")
            rel = "sponsored noopener" if "amazon.com" in s["url"] else "noopener"
            out.append(f'<a href="{html.escape(s["url"])}" rel="{rel}">{html.escape(sid)}</a>')
        return " · ".join(out)

    def row(q):
        return f'''<tr>
  <td><strong>{html.escape(q["id"])}</strong></td>
  <td><strong>{html.escape(q["question"])}</strong><br><span class="small muted">Blocks: {html.escape(q.get("blocks", "—"))}</span></td>
  <td><span class="small">{html.escape(q.get("known", "—"))}</span></td>
  <td><span class="small">{html.escape(q.get("unknown", "—"))}</span></td>
  <td><span class="small">{html.escape(q.get("how_to_find_out", "—"))}</span></td>
  <td><span class="small">{html.escape(q.get("who", "—"))} · {html.escape(q.get("cost", "—"))}</span><br><span class="badge grey">{html.escape(q.get("status", "—"))}</span></td>
  <td class="small">{qsource(q)}</td>
</tr>'''

    sections = []
    for g, items in groups.items():
        rows = "\n".join(row(q) for q in items)
        sections.append(f'''<h2>{html.escape(g)} ({len(items)})</h2>
<div class="table-wrap"><table>
<thead><tr><th>ID</th><th>Question</th><th>What we know</th><th>What we do not know</th><th>How to find out</th><th>Who · cost</th><th>Official source</th></tr></thead>
<tbody>
{rows}
</tbody></table></div>''')

    body = f'''<main id="main"><div class="article" style="max-width:1100px">
<p class="kicker">Direction · Open questions</p>
<h1>The questions that have to be answered before the next decision</h1>
<p class="byline">Kitchen Counter · Register updated {data['generated']} · {len(qs)} open questions, grouped by what they block</p>

<p>A decision made on missing information is a guess with better manners. Each row states what is known, what is not, why it matters, and the cheapest concrete action that would settle it. Machine-readable copy: <code>data/open-questions.json</code>.</p>

<div class="callout"><strong>Read this first.</strong> Several rows can only be answered from inside the Associates account — they are marked <em>owner-only</em>. They are not blockers for publishing; they are blockers for claiming that the site earns anything. Nothing on this site presents a conversion rate, revenue figure, or ranking, because the data behind those figures does not exist yet.</div>

{''.join(sections)}

<h2 id="cheapest">The shortest path: four questions, about half an hour, signed in once</h2>
<p>Most of this register cannot be answered from outside an account. These four can, and nearly every
proposal on the site depends on at least one of them. Do them in one sitting, record the date and what
the screen said, and the rest of the register becomes decidable.</p>
<div class="table-wrap"><table>
<thead><tr><th>#</th><th>Do this</th><th>You end up with</th><th>Then unblocks</th></tr></thead>
<tbody>
<tr><td><strong>Q-23</strong></td><td>Associates Central → Account Settings. Is <code>shopnow047c-20</code> listed, and is the account in good standing?</td><td>Yes or no, with the date</td><td>Whether the disclosure describes a live relationship, and whether any link can earn at all</td></tr>
<tr><td><strong>Q-02</strong> + <strong>Q-22</strong></td><td>Signed in, click each of the five links once. Read the final URL: does it carry <code>tag=shopnow047c-20</code>, and does it land on the product or the homepage?</td><td>Five final URLs and five yes/no answers</td><td>Whether the two homepage links get replaced with freshly generated Special Links (FLG-017 / FLG-023)</td></tr>
<tr><td><strong>Q-18</strong></td><td>Add the site as a Search Console property, verify it, submit <code>sitemap.xml</code>.</td><td>A verified property and a submitted sitemap</td><td>Choosing the next guide from measured queries instead of instinct</td></tr>
<tr><td><strong>Q-19</strong></td><td>Associates Central → Product Advertising API. Is the tab available?</td><td>Available, or not yet</td><td>Whether prices and ratings can ever be displayed compliantly</td></tr>
</tbody></table></div>
<div class="callout"><strong>What this register cannot do for you.</strong> It cannot read your Associates account, your Search Console, or a share debugger. Those answers come back as facts with a date, or they stay open. Nothing here is invented to fill the gap.</div>

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
        # Same test as tools/check_site.py P07: any amazon.com or link.amazon URL is an Amazon link.
        amazon = "amazon.com" in s["url"] or "link.amazon" in s["url"]
        rel = "sponsored noopener" if amazon else "noopener"
        return f'<a href="{html.escape(s["url"])}" rel="{rel}">{html.escape(c["source"])}</a>'

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
<li><strong>Customer star ratings.</strong> Participation Requirements §2(t) permits customer reviews and star ratings on a site only when they are obtained through Creators API or PA API (Program Policies, read 2026-11-20). This site uses neither, so no rating is rendered. Ratings were removed 2026-11-19; the clause was located on the live page 2026-11-20 (FLG-020, resolved).</li>
<li><strong>Revenue, conversion rates, traffic.</strong> No first-party report exists. The ledger is empty by design.</li>
<li><strong>Product photography.</strong> No licensed photography is used; the cards are typographic art built from listed specs.</li>
</ul>

<p class="mt"><a href="sources.html">← Source register</a> · <a href="flagged.html">Flagged for Review →</a></p>
</div></main>

'''
    return (head("Citation Log — Every Figure and Its Source | Kitchen Counter",
                 "One row per figure Kitchen Counter publishes: the observation, its date, the official page it came from, and whether it is a seller statement or tested result.",
                 "citations.html") + body + FOOTER)


def main():
    # Apply the shared chrome so the output here matches what scripts/build_chrome.py
    # produces. Otherwise the two builders overwrite each other and every --check
    # fails immediately after the other has run.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_chrome

    outputs = {
        "suggestions.html": build_chrome.render(render_suggestions(), "suggestions.html", 0),
        "questions.html": build_chrome.render(render_questions(), "questions.html", 0),
        "citations.html": build_chrome.render(render_citations(), "citations.html", 0),
    }
    if "--check" in sys.argv:
        stale = [n for n, t in outputs.items()
                 if not (ROOT / n).exists() or (ROOT / n).read_text(encoding="utf-8") != t]
        if stale:
            print("FAIL: register pages out of date: " + ", ".join(stale))
            print("Run: python3 scripts/build_registers.py")
            sys.exit(1)
        print("OK: register pages match data/*.json")
        return
    for name, txt in outputs.items():
        (ROOT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
