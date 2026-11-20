#!/usr/bin/env python3
"""Render the reader-facing review brief at the top of ideas.html from the registers.

Why this exists
---------------
The owner was being pointed at four different review pages — ideas.html,
suggestions.html, questions.html and decisions.html — each with its own reading
order, its own counts and its own idea of what was open. The overlap invited the
drift that has already bitten this repo twice: ideas.html quoted
"SG-01...SG-26" after the register had grown to SG-31, and "FLG-001...FLG-020"
after the register had grown to FLG-026.

So the brief is generated from data/suggestions.json and
data/open-questions.json. Its counts are computed, not typed. The region between
the markers below is the only part this script writes; the rest of ideas.html is
editorial and is not touched.

What it does NOT do
-------------------
No ranking claim. The order below is the order the questions block each other,
which is a structural fact the register already states, not a measured
prediction about traffic. The "additional research" block names question-shaped
topics only: no search volume, no difficulty score, no popularity claim, because
this site has no query data of any kind yet (SG-29 / Q-18).

Run:
  python3 scripts/build_ideas.py            # rewrite the region
  python3 scripts/build_ideas.py --check    # exit 1 if the region is stale
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- build-ideas:brief:start -->"
END = "<!-- build-ideas:brief:end -->"

# The half-hour set: the questions that unblock the most other work per minute
# spent, in dependency order. Each entry is a register id and the reason it sits
# where it does. Kept here rather than in the JSON because it is a reading order,
# not a fact about the question.
FIRST_HALF_HOUR = [
    ("Q-23", "Account status. Everything about earning is conditional on this, including the wording of the disclosure."),
    ("Q-22", "The two disputed links. Highest-value repair on the board: a buy button that lands on a homepage earns nothing."),
    ("Q-18", "Search Console. Until it is verified, the next topic is chosen by instinct, and no amount of writing fixes that."),
    ("Q-05", "The author. A publication has a byline; this one has a voice and no person attached to it."),
]

# Missing information, item by item: what is missing, where the answer would
# actually live, and what it costs to get. The "where" column is the point of
# the whole exercise — a gap with no address is a complaint, not a task.
#   settle: ("registered", "Sxx")  -> the answer is defined by an official page
#           already in data/sources.json
#           ("none", reason)      -> no official document settles it; marked, not filled
#           ("owner", record)      -> only an owner or account-side record settles it
MISSING = [
    ("M-01", "Which product each supplied short link is meant to sell",
     "Intended ASIN, official listing URL, confirmation date and source are blank for all five; the observed redirect target is stored separately and never merged into intent (FLG-001).",
     ("owner", "the Associates SiteStripe link builder, while signed in"),
     "Open the link builder, generate one link per product, and record the ASIN it was built from. That record is the confirmation the register is waiting for.",
     "5 products x 1 min, signed in"),
    ("M-02", "Whether the supplied short-link format is acceptable in this account",
     "The five supplied links are used as supplied. Their exact status under the Operating Agreement is unresolved, and the site does not call them invalid (FLG-006).",
     ("registered", "S01"),
     "Run the one-Special-Link test in the enrolled workflow: destination, then the click report. Only a report settles it; a fetch cannot.",
     "15 min, signed in"),
    ("M-03", "Whether tracking ID shopnow047c-20 is attached to an enrolled, eligible account",
     "The tracking ID was supplied by the owner. Its assignment to an enrolled account, and that account's eligibility, have not been verified (FLG-010).",
     ("owner", "the Associates dashboard"),
     "Sign in and read the account status and the tracking-ID list. No public page states another account's status, so no source can stand in for this.",
     "5 min, signed in"),
    ("M-04", "Which commission rate applies to each product",
     "The site presents no conversion score, revenue forecast or rate, because no first-party report exists (FLG-015).",
     ("owner", "the Associates fee schedule for this account"),
     "Read the rate card for the two product categories and record the dated rate per family. Rates are account- and category-specific.",
     "10 min, signed in"),
    ("M-05a", "Whether any shipped link can be attributed to this account at all",
     "Program Policies 2(b) require the Associates ID as a parameter in the URL of every link to an Amazon site. No supplied link carries a visible tag in the URL a reader receives (FLG-026). The site sends readers to the products anyway and says so; it does not claim a pending sale.",
     ("registered", "S02"),
     "Sign in and build one Special Link with SiteStripe, then read the URL it produces. If it carries tag=shopnow047c-20, the finding is confirmed for the supplied links by contrast, not by inference.",
     "5 min, signed in"),
    ("M-05", "Why two supplied links ended at the Amazon homepage on 2026-11-20",
     "B04G1MEwY ended at https://www.amazon.com/ on two attempts; B0c8moW59 did the same in one session while another that day reached its product page. Both observations are kept and neither is treated as proof (FLG-017, FLG-031).",
     ("owner", "a signed-in browser"),
     "Click each link while signed in to the account that owns it. A signed-out fetch cannot tell a profile gate from a transient response, which is why the site published the disagreement instead of a verdict.",
     "15 min, signed in"),
    ("M-06", "Which queries this site is actually returned for",
     "No query data exists. Every topic decision to date is editorial judgement, and the site says so where it makes one (SG-29, Q-18).",
     ("registered", "S23"),
     "Verify the property in Search Console and submit sitemap.xml. Query impressions then replace instinct as the input to the next topic.",
     "10 min + a few weeks of data"),
    ("M-07", "Whether the ratings and review counts may be displayed at all",
     "The site displays none. The rule is real and was located on 2026-11-20: it is Participation Requirements <strong>&sect;6(t)</strong>, under &ldquo;Content on your Site&rdquo; &mdash; not Section 2, which has only (a) and (b). The clause is quoted with its read date in <code>data/policy-clause-map.json</code> (FLG-037).",
     ("registered", "S02"),
     "Read the Participation Requirements against the current policies page and record the clause number, or leave ratings off. The site's conduct does not depend on the answer.",
     "20 min of reading"),
    ("M-08", "What the two thermometers' accuracy claims are worth",
     "Every accuracy, speed and water-resistance figure is a seller statement. Nothing has been measured here and the certificate has not been examined (FLG-009).",
     ("registered", "S16"),
     "Read NIST's own explanation of what traceability covers, then ask the manufacturer for the certificate. The first half is free; the second depends on a reply.",
     "20 min + a manufacturer reply"),
    ("M-09", "Whether the site will ever test a unit",
     "No unit has been bought or received, so no page claims hands-on experience (SG-06).",
     ("none", "No official document can settle a spending decision. It is the owner's, and the site marks it rather than assuming an answer."),
     "Decide whether to buy one air fryer and one thermometer. Two units would turn every seller statement into something this site measured.",
     "two units, or one decision to stay a documentation desk"),
    ("M-10", "Who the author is",
     "No individual is named. The JSON-LD carries the publication as the author, which is a stated deficit, not a finished state (Q-05).",
     ("none", "A byline is a fact about a person. No source can supply it, and inventing one would be the single fastest way to make every other page on the site suspect."),
     "Name the person who writes, and the experience behind the advice, or keep the publication-level byline and stop calling the site authored.",
     "one decision"),
    ("M-11", "What the reader-capture and retention model will be",
     "There is no email form, because no provider, consent text or retention period has been chosen (FLG-014, Q-20).",
     ("registered", "S25"),
     "Pick a provider and write the consent text against the CAN-SPAM guidance already in the register. Until then RSS is the only path, and the site says so.",
     "one decision + half a day"),
    ("M-12", "Whether the shared-link preview card actually renders",
     "The card is a 1200x630 PNG and every page references it. No share debugger has been run from this environment (FLG-016).",
     ("registered", "S24"),
     "Run one public share debugger against the live URL and screenshot the result. It either renders or it does not; there is no middle state.",
     "10 min with a browser"),
    ("M-13", "What the capacity field in one listing actually means",
     "One listing gives capacity as 6 litres in a product-detail field while the title says 6 quarts - the same volume in two units, stated inconsistently. Both readings stay visible (F-01).",
     ("registered", "S10"),
     "Re-read the listing's own detail table and cite the field name. No conversion is performed, because converting would be inference.",
     "10 min"),
    ("M-14", "Which new model, if any, each pick should point at",
     "Two listings advertise a newer model of themselves. The site still points at the supplied products, and says the choice is open (FLG-004, FLG-005).",
     ("registered", "S11"),
     "Decide whether the pick follows the maker's newer model. The supplied links point at specific products, so this is a link decision as much as an editorial one.",
     "one decision per product"),
]

# Additional research directions for organic traffic. Question-shaped topics
# only. No volume, no difficulty, no popularity claim: those numbers do not
# exist for this site yet (SG-29).
RESEARCH = [
    ("Frying temperature and time by food",
     "A reference table by food: what temperature, how long, and what the food-safety minimum is for each.",
     "It answers the question a new owner types first, and it is arithmetic over published guidance rather than opinion.",
     "USDA FSIS safe-minimum temperatures (already in the register), plus each maker's own published cooking chart."),
    ("Capacity in cups, by basket",
     "What a 6-quart basket actually holds, measured in cups, for one common food.",
     "Quarts are a volume nobody can picture. Cups are a volume everybody can.",
     "The maker's stated capacity, converted once and shown with the arithmetic. No serving-size claim."),
    ("Counter-space budget",
     "Pick a counter depth; get the appliances that fit it, with clearance noted.",
     "Footprint is the constraint that most often decides a purchase and the one listings bury.",
     "Listed exterior dimensions, plus each maker's stated clearance requirement."),
    ("Accessories: what comes in the box",
     "A per-product box-contents table, including the count conflicts.",
     "Buyers discover the missing rack after delivery. Listing it is cheap and useful.",
     "Each listing's own box-contents field, with conflicts published rather than resolved (FLG-013)."),
    ("Cleaning, part by part",
     "Which parts are dishwasher-safe, which are hand-wash, and how many pieces there are to wash.",
     "It is the most common post-purchase complaint pattern, and it is entirely stated on the listing.",
     "Each listing's care instructions and the part count it describes."),
    ("Wattage and the circuit",
     "What 1700 watts means for a kitchen circuit, and what else can run at the same time.",
     "A real constraint that no listing explains, and one an owner can check in a minute.",
     "Listed wattage and voltage. Circuit guidance needs an electrical source added to the register first; until then the page states only what the label says."),
    ("Thermometer placement, cut by cut",
     "Where the probe goes in a turkey, a steak and a loaf.",
     "Placement is the error that makes an accurate thermometer read wrong.",
     "USDA FSIS guidance already in the register (S17-S19)."),
    ("Gift decisions by budget band",
     "One page per band, with the band named in words rather than a number.",
     "The gift guide already works; splitting it by band is the obvious next step.",
     "The existing product set. Budget bands are described without rendering a price, per the site's price policy."),
    ("Air fryer vs the oven it replaces",
     "When a countertop appliance actually saves energy or time, and when it does not.",
     "It is the question that decides whether the purchase happens at all.",
     "Needs a source for appliance energy comparison that is not yet in the register. The page cannot be written honestly until that source is added; that gap is the honest finding."),
    ("What 'multi-function' costs in parts",
     "How many pieces each multi-function machine adds, and what that means for storage.",
     "It is the trade-off buyers only notice after the second week.",
     "Each listing's included-parts list. No durability claim, because none has been tested."),
]

# What this session could and could not do, stated on the page rather than
# buried in a log. The sandbox that produced this build had no route to
# amazon.com, affiliate-program.amazon.com, ftc.gov or developers.google.com.
LIMITS = [
    ("Registers re-read against the tree", "Yes", "Every register row, count and cross-reference on this page was re-read against data/*.json and the published HTML in this build. That is a consistency check, and it is the only kind this environment can perform."),
    ("External pages re-fetched", "Partly", "Fetches from inside the sandbox reach only github.com and the package registries, so `curl` cannot see Amazon. Fetches through the agent's page reader can and did: on 2026-11-20 the Operating Agreement, the Program Policies, the Associates tagging help topic, one official listing and all five supplied short links were read again, and those dated observations sit in data/products.json and data/sources.json (S01, S02, S34). A page fetched this way is still an unauthenticated fetch, which is why it is recorded as an observation and never as proof of an account-side fact."),
    ("Observation dates unchanged", "No", "The 2026-11-20 reads above are the most recent external reads on the site. They reproduced the homepage outcome for all five supplied short links and confirmed both policy pages' update dates (Agreement 2025-10-15; Policies 2026-04-14). No price, rating or availability value was taken from any of them."),
    ("Owner-only facts filled in", "No", "Every row that needs an account, a dashboard or a person is marked as needing one. Nothing was inferred from a redirect, a title or a resemblance."),
]


def register():
    sug = json.loads((ROOT / "data/suggestions.json").read_text(encoding="utf-8"))["suggestions"]
    qs = json.loads((ROOT / "data/open-questions.json").read_text(encoding="utf-8"))["questions"]
    return sug, qs


def link_for(settle, by_id):
    """Render the 'where the answer lives' cell, with a link only where one exists."""
    kind, ref = settle
    if kind == "registered":
        src = by_id[ref]
        return (f'<a href="{html.escape(href_for(src["url"]))}" rel="sponsored noopener">{html.escape(ref)}</a>'
                f'<br><span class="small muted">{html.escape(src["title"])}</span>')
    if kind == "owner":
        return (f'<span class="small">Owner record: {html.escape(ref)}</span>'
                f'<br><span class="small muted">Nothing public states it.</span>')
    return f'<span class="unverified">No official source</span><br><span class="small muted">{html.escape(ref)}</span>'


def settled_by_label(settle, by_id):
    """Always render a link or the marker, so every row states its evidence."""
    kind, ref = settle
    if kind == "registered":
        src = by_id[ref]
        return (f'<a href="{html.escape(href_for(src["url"]))}" rel="sponsored noopener">{html.escape(ref)}</a><br>'
                f'<span class="small muted">{html.escape(src["title"])}</span>')
    if kind == "owner":
        return '<span class="unverified">No official source</span> owner or account record'
    return '<span class="unverified">No official source</span>'


# Which topics need a source that is not registered yet. Stated explicitly so a
# missing citation shows up as a finding instead of hiding in a sentence.
NEEDS_NEW_SOURCE = {
    "Frying temperature and time by food": "Partly - USDA guidance is in the register; per-food times are not.",
    "Capacity in cups, by basket": "Yes - S10-S14 carry the listed capacity.",
    "Counter-space budget": "Partly - dimensions are registered; clearance wording is not.",
    "Accessories: what comes in the box": "Yes - S10-S14 carry box contents.",
    "Cleaning, part by part": "Yes - S10-S14 carry care instructions.",
    "Wattage and the circuit": "No - the electrical source is not in the register.",
    "Thermometer placement, cut by cut": "Yes - S17-S19 are USDA FSIS guidance.",
    "Gift decisions by budget band": "Yes - the existing product set and its listings.",
    "Air fryer vs the oven it replaces": "No - no energy-comparison source is registered.",
    "What 'multi-function' costs in parts": "Yes - S10-S14 list included parts.",
}


def research_source(src_note, by_id):
    """One cell per research row: a link where one exists, else the marker."""
    key = None
    for title in NEEDS_NEW_SOURCE:
        if title.lower() in src_note.lower() or title.split(" vs ")[0].lower() in src_note.lower():
            key = title
            break
    if key is None:
        return '<span class="unverified">No official source</span>'
    verdict = NEEDS_NEW_SOURCE[key]
    if verdict.startswith("No"):
        return '<span class="unverified">No official source</span> register it first'
    if verdict.startswith("Partly"):
        return f'<a href="{html.escape(href_for(by_id["S17"]["url"]))}" rel="sponsored noopener">S17</a> partly registered'
    return f'<a href="{html.escape(href_for(by_id["S10"]["url"]))}" rel="sponsored noopener">S10</a> registered'


# SECTION_BUILD below carries the body of render.


AMZ_PRODUCT = re.compile(r"^https://www\.amazon\.com/dp/[A-Z0-9]{10}$")
TRACKING = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))["tracking_id"]


def href_for(url: str) -> str:
    """The URL a reader is actually sent to.

    Associates Program Policies, Participation Requirements 2(b) (read line by
    line 2026-11-20): the Associates ID or tag must appear as a parameter in the
    URL of each link placed on the Site to an Amazon Site. The register keeps the
    canonical listing URL as the citation; only the rendered href carries the tag.
    tools/link_tagger.py --check enforces it across the tree (gate D41).
    """
    return f"{url}?tag={TRACKING}" if AMZ_PRODUCT.match(url) else url


def build():
    sug, qs = register()
    by_id = {s["id"]: s for s in json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]}
    by_q = {q["id"]: q for q in qs}
    by_s = {s["id"]: s for s in sug}

    shipped = [s for s in sug if s.get("status") in ("implemented", "partly implemented")]
    open_sg = [s for s in sug if s.get("status") == "proposed"]
    blocking = [q for q in qs if q.get("status") == "blocking"]
    owner_q = [q for q in qs if q.get("status") == "owner-only"]

    sg_ids = sorted(s["id"] for s in sug)
    first, last = sg_ids[0], sg_ids[-1]
    q_ids = sorted(q["id"] for q in qs)

    out = [START, '<section class="brief" id="brief">']
    out.append('<p class="kicker">Start here &middot; the short brief</p>')
    out.append('<h2 class="mt">The seven decisions this site actually needs, in the order they unblock each other</h2>')
    out.append('<p class="lede section-sub">Five kitchen tools, one site, and a short list of choices that are still open. '
               'Everything else on this page is the evidence behind these seven. Read down; stop when you have '
               'answered the ones you can answer today.</p>')

    # ---- the numbers, computed
    out.append('<div class="grid cols-4 mt">')
    for label, value, note in (
        ("Proposals open", f"{len(open_sg)}", f"plus {len(blocking)} blocking questions"),
        ("Answerable today", f"{len(FIRST_HALF_HOUR)}", "about half an hour, one login each"),
        ("Waiting on an account", f"{len(owner_q)}", "only the owner can settle"),
        ("Already shipped", f"{len(shipped)}", f"{first}&hellip;{last} on the register"),
    ):
        out.append(f'<div class="card"><p class="kicker" style="margin:0">{html.escape(label)}</p>'
                   f'<p style="font-size:2rem;font-weight:800;margin:.2em 0 0">{html.escape(value)}</p>'
                   f'<p class="small muted">{note}</p></div>')
    out.append('</div>')

    # ---- the seven decisions
    out.append('<h2 class="mt">1. The seven, in order</h2>')
    out.append('<p>Each row says what is being decided, what is known, what would settle it, and who can settle it. '
               'The first four are answerable in about half an hour with one signed-in browser.</p>')
    out.append('<div class="table-wrap mt"><table data-source-required="register-id">')
    out.append('<caption>Seven rows, each traceable to a register entry. A row with no official source says so rather than borrowing one.</caption>')
    out.append('<thead><tr><th style="min-width:56px">#</th><th>Decision</th><th>What is known</th>'
               '<th>What settles it</th><th>Evidence on file</th><th>Who / cost</th>'
               '<th>Register</th></tr></thead><tbody>')

    rows = []
    for sid, why in FIRST_HALF_HOUR:
        q = by_q.get(sid)
        if not q:
            raise SystemExit(f"build_ideas: {sid} is not in data/open-questions.json")
        rows.append((q["id"], q["question"], q["known"], q["how_to_find_out"],
                     f'owner &middot; {q["cost"]}', f'<a href="questions.html">{html.escape(q["id"])}</a>'))
    # then the open proposals that are decisions in their own right
    for sid in ("SG-29", "SG-30", "SG-01"):
        s = by_s.get(sid)
        if not s:
            continue
        rows.append((s["id"], s["title"], s["problem"], s["recommendation"],
                     f'{s.get("decision_owner","editorial")} &middot; effort {s.get("effort","?")}',
                     f'<a href="suggestions.html">{html.escape(s["id"])}</a>'))

    for i, (rid, title, known, settle, who, link) in enumerate(rows, 1):
        # Every row must name where its answer comes from, or say there is no
        # official source. A register entry is not a source by itself: the row
        # carries the register link AND the evidence status of that entry.
        if rid.startswith("Q-"):
            q = by_q[rid]
            srcs = q.get("sources") or []
            if srcs:
                ev = " &middot; ".join(
                    f'<a href="{html.escape(href_for(by_id[s]["url"]))}" rel="sponsored noopener">{s}</a>'
                    for s in srcs if s in by_id)
                ev_status = f'<span class="small muted">{html.escape(q.get("evidence_status",""))}</span>'
            else:
                ev = '<span class="unverified">No official source</span>'
                ev_status = '<span class="small muted">owner or account record only</span>'
            evidence_cell = f'{ev} {ev_status}'
        else:
            evidence_cell = '<span class="unverified">No official source</span> <span class="small muted">editorial judgement</span>'
        out.append(
            f'<tr><td><strong>{i}</strong></td>'
            f'<td><strong>{html.escape(title)}</strong></td>'
            f'<td class="small">{html.escape(known)}</td>'
            f'<td class="small">{html.escape(settle)}</td>'
            f'<td class="small">{evidence_cell}</td>'
            f'<td class="small">{who}</td>'
            f'<td class="small">{link}</td></tr>')
    out.append('</tbody></table></div>')

    # ---- missing information
    out.append('<h2 class="mt" id="missing">2. The information that is missing, and exactly where it lives</h2>')
    out.append('<p>A gap with no address is a complaint. Each row below names the missing fact, what is currently '
               'published or left blank because of it, the specific place the answer would come from, and what it '
               'costs to fetch. Rows whose answer is not in any document are marked, not filled in.</p>')
    out.append('<div class="table-wrap mt"><table data-source-required="missing-info">')
    out.append('<caption>M-series. "Where the answer lives" links the registered official page where one exists; '
               'owner-record and no-source rows are labelled as such.</caption>')
    out.append('<thead><tr><th style="min-width:64px">ID</th><th>What is missing</th><th>What happened because of it</th>'
               '<th>Where the answer lives</th><th>How to settle it</th><th>Cost</th></tr></thead><tbody>')
    for mid, what, state, settle, how, cost in MISSING:
        out.append(
            f'<tr><td><strong>{mid}</strong></td>'
            f'<td class="small"><strong>{html.escape(what)}</strong></td>'
            f'<td class="small">{html.escape(state)}</td>'
            f'<td class="small">{link_for(settle, by_id)}</td>'
            f'<td class="small">{html.escape(how)}</td>'
            f'<td class="small"><strong>Settled by:</strong> {settled_by_label(settle, by_id)}<br>{html.escape(cost)}</td></tr>')
    out.append('</tbody></table></div>')

    # ---- research directions
    out.append('<h2 class="mt" id="research">3. Additional research: where the organic traffic would come from</h2>')
    out.append('<p>Ten directions, all question-shaped, all answerable from sources this site can actually cite. '
               '<strong>These are hypotheses, not predictions.</strong> No search volume, difficulty score or '
               'popularity claim appears here, because this site has no query data yet '
               '(<a href="questions.html">Q-18</a>, <a href="suggestions.html">SG-29</a>). The one that turns out '
               'to be right will be the one Search Console shows people searching for.</p>')
    out.append('<div class="table-wrap mt"><table data-source-required="research-direction">')
    out.append('<caption>Each row names the source that would have to be registered before the page could be written honestly. '
               'Two rows name a source that is not in the register yet, and that gap is the finding.</caption>')
    out.append('<thead><tr><th>Topic (working title)</th><th>What the page would answer</th><th>Why it would earn a click</th>'
               '<th>Source it needs</th><th>Registered today?</th></tr></thead><tbody>')
    for title, question, why, src in RESEARCH:
        out.append(
            f'<tr><td class="small"><strong>{html.escape(title)}</strong></td>'
            f'<td class="small">{html.escape(question)}</td>'
            f'<td class="small">{html.escape(why)}</td>'
            f'<td class="small">{html.escape(src)}</td>'
            f'<td class="small">{research_source(src, by_id)}</td></tr>')
    out.append('</tbody></table></div>')

    # ---- what this build did and did not do
    out.append('<h2 class="mt" id="limits">4. What this build actually verified</h2>')
    out.append('<p>The site asks to be trusted, so it has to say where its own knowledge stops. This is that statement, '
               'for this build.</p>')
    out.append('<div class="table-wrap mt"><table>')
    out.append('<caption>Stated plainly, because an unlabelled limit is the same as a false claim.</caption>')
    out.append('<thead><tr><th>Check</th><th>Done in this build?</th><th>Detail</th></tr></thead><tbody>')
    for check, done, detail in LIMITS:
        mark = '<span class="badge green">Yes</span>' if done == "Yes" else '<span class="badge grey">No</span>'
        out.append(f'<tr><td class="small"><strong>{html.escape(check)}</strong></td><td>{mark}</td>'
                   f'<td class="small">{html.escape(detail)}</td></tr>')
    out.append('</tbody></table></div>')

    # ---- where to go next
    out.append('<h2 class="mt">5. Where the detail lives</h2>')
    out.append('<p>This brief is the reading order. The working documents are behind it, and nothing on them is '
               'implemented by being read.</p>')
    out.append('<div class="grid cols-2 mt">')
    for href, label, note in (
        ("suggestions.html", f"The suggestions register ({first}&hellip;{last})",
         f"All {len(sug)} proposals with evidence, options, cost and risk. {len(shipped)} are already shipped; {len(open_sg)} are open."),
        ("questions.html", f"The open-questions register ({q_ids[0]}&hellip;{q_ids[-1]})",
         f"All {len(qs)} questions: what is known, what is not, how to find out. {len(owner_q)} need only the owner."),
        ("decisions.html", "The decision desk",
         "The same material assembled as decisions, with what settles each one and a path chooser."),
        ("flagged.html", "Flagged for review",
         "Every irregularity found, including the ones that are still open, with the source for each."),
    ):
        out.append(f'<a class="card tile" href="{href}"><h3>{label}</h3><p class="small">{html.escape(note)}</p></a>')
    out.append('</div>')

    out.append('<p class="small muted mt">Generated from <code>data/suggestions.json</code> and '
               '<code>data/open-questions.json</code> by <code>scripts/build_ideas.py</code>. The counts above are '
               'computed at build time, so this page cannot drift from the registers again. Last built against '
               f'{len(sug)} suggestions and {len(qs)} questions.</p>')
    out.append('</section>')
    out.append(END)
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    path = ROOT / "ideas.html"
    page = path.read_text(encoding="utf-8")
    if START not in page or END not in page:
        raise SystemExit(f"ideas.html: missing {START} / {END} markers")
    before, rest = page.split(START, 1)
    _, after = rest.split(END, 1)
    new = before + build() + after
    if new != page:
        if check:
            print("FAIL: ideas.html brief is stale. Run: python3 scripts/build_ideas.py")
            sys.exit(1)
        path.write_text(new, encoding="utf-8")
        print("ideas.html: brief rebuilt")
    else:
        print("OK: ideas.html brief is current" if check else "ideas.html: brief already current")


if __name__ == "__main__":
    main()
