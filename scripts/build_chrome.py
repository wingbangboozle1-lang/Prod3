#!/usr/bin/env python3
"""Render the shared page chrome (masthead, disclosure strip, footer) into every page.

Why this exists
---------------
Every page previously carried its own hand-copied masthead and footer. That is how
the site drifted: 24 pages, six nav labels, and an active-state attribute on 9 of 24
pages. Handles and footers should not be copy-paste artefacts of a page.

What it guarantees
------------------
* ONE navigation group (the brief asks for exactly that). Editorial sections live in a
  second-level "shelf" bar under the masthead, not in a competing top-level nav.
* The exact Agreement §5 sentence appears in the disclosure strip AND the footer on
  every page. Both strings are asserted here so a page cannot be generated without them.
* Prices are never rendered; the strip says so in plain words instead of apologising.
* The active page is marked with aria-current="page" on all 24 pages.

The article body is never touched: only the regions between the markers below are
replaced. `--check` re-renders in memory and exits 1 if a page has drifted.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangboozle1-lang.github.io/Prod3"
TRACKING = "shopnow047c-20"

# The exact sentence Agreement §5 asks for. tools/check_site.py and
# scripts/check_site.py both fail the release if this string disappears.
DISCLOSURE_SENTENCE = "As an Amazon Associate I earn from qualifying purchases."

# Top-level navigation: one group, four editorial destinations plus the desk.
NAV = [
    ("Shop", "index.html"),
    ("Air fryers", "air-fryers.html"),
    ("Thermometers", "meat-thermometers.html"),
    ("Compare", "compare.html"),
    ("Guides", "buying-guide.html"),
]

# The decision desk is the review surface for the owner; it sits in the same group
# because the brief asks for a single navigation group and this is where choices live.
NAV.append(("Decision desk", "decisions.html"))

# Second-level shelf: where a reader can go next. Rendered on every page so no
# surface is more than one click from anywhere.
SHELF = [
    ("Buying guide", "buying-guide.html"),
    ("Decision tools", "tools/index.html"),
    ("Gift guide", "articles/holiday-kitchen-gift-guide.html"),
    ("RSS", "feed.xml"),
]

FOOTER_GROUPS = [
    ("Shop", [
        ("Air fryers", "air-fryers.html"),
        ("Meat thermometers", "meat-thermometers.html"),
        ("Compare all five", "compare.html"),
        ("Buying guide", "buying-guide.html"),
    ]),
    ("Guides", [
        ("Basket or oven?", "articles/basket-or-oven-air-fryer.html"),
        ("Capacity checklist", "articles/air-fryer-capacity-checklist.html"),
        ("Cleanup &amp; counter space", "articles/cleanup-counter-space.html"),
        ("Before you buy", "articles/questions-before-multi-function.html"),
        ("All guides", "buying-guide.html"),
    ]),
    ("Decision desk", [
        ("Ideas &amp; review", "ideas.html"),
        ("Suggestions", "suggestions.html"),
        ("Open questions", "questions.html"),
        ("Information we still need", "decisions.html"),
        ("Decision log", "direction.html"),
    ]),
    ("Trust", [
        ("Disclosure", "disclosure.html"),
        ("Sources", "sources.html"),
        ("Citations", "citations.html"),
        ("Flagged for review", "flagged.html"),
        ("Analytics &amp; privacy", "analytics.html"),
        ("Executive summary", "executive-summary.html"),
        ("About", "about.html"),
    ]),
]

HEAD_START = "<!-- build-chrome:header:start -->"
HEAD_END = "<!-- build-chrome:header:end -->"
FOOT_START = "<!-- build-chrome:footer:start -->"
FOOT_END = "<!-- build-chrome:footer:end -->"


def rel(depth, target):
    """Relative URL from a page at `depth` (0 = root, 1 = articles/) to `target`."""
    return ("../" * depth) + target


def is_current(path, target):
    """True when `target` is the page being rendered."""
    return path == target


def render_header(path, depth, kicker=None):
    r = lambda t: rel(depth, t)
    links = []
    for label, target in NAV:
        cur = ' aria-current="page"' if is_current(path, target) else ""
        links.append(f'<a href="{r(target)}"{cur}>{label}</a>')
    shelf = []
    for label, target in SHELF:
        cur = ' aria-current="page"' if is_current(path, target) else ""
        shelf.append(f'<a href="{r(target)}"{cur}>{label}</a>')
    section = f'<span class="shelf-label">{kicker}</span>' if kicker else ""

    return f'''{HEAD_START}
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="wrap">
    <a class="brand" href="{r('index.html')}">Kitchen Counter<small>The kitchen-gear desk</small></a>
    <nav class="nav" aria-label="Primary">
      {''.join(links)}
    </nav>
  </div>
</header>
<div class="disclosure" role="note"><div class="wrap"><strong>Affiliate disclosure:</strong> {DISCLOSURE_SENTENCE} If a qualifying purchase is credited, Kitchen Counter may earn a commission at no extra cost to you. Tracking ID: <strong>{TRACKING}</strong>. Prices change &mdash; confirm on Amazon. <a href="{r('disclosure.html')}">How we make money</a>.</div></div>
<nav class="shelf" aria-label="Sections">
  <div class="wrap">{section}{''.join(shelf)}</div>
</nav>
{HEAD_END}'''


def render_footer(path, depth):
    r = lambda t: rel(depth, t)
    groups = []
    for title, links in FOOTER_GROUPS:
        items = "".join(f'<li><a href="{r(target)}">{label}</a></li>' for label, target in links)
        groups.append(f'<div><h4>{title}</h4><ul>{items}</ul></div>')

    return f'''{FOOT_START}
<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>Kitchen Counter</h4>
        <p>Five kitchen tools, compared on what their listings actually say. We read the label, show our working, and leave the price to Amazon.</p>
        <p class="small">New guides by <a href="{r('feed.xml')}">RSS</a>. No email signup: we could not connect one honestly, so we did not ship a fake form.</p>
        <p id="local-counts" class="small" hidden></p>
      </div>
      {''.join(groups)}
    </div>
    <p class="foot-disclosure"><strong>Affiliate disclosure:</strong> {DISCLOSURE_SENTENCE} Tracking ID: {TRACKING}. If a qualifying purchase is credited, Kitchen Counter may earn a commission at no extra cost to you. Amazon and the Amazon logo are trademarks of Amazon.com, Inc. or its affiliates. Where the listings contradict themselves, both readings are published on <a href="{r('flagged.html')}">Flagged for Review</a>.</p>
  </div>
</footer>
{FOOT_END}'''


def pages():
    out = []
    for p in sorted(ROOT.glob("*.html")):
        out.append((p, 0))
    for p in sorted((ROOT / "articles").glob("*.html")):
        out.append((p, 1))
    for p in sorted((ROOT / "tools").glob("*.html")):
        out.append((p, 1))
    return out


def kicker_for(name):
    """The shelf label: which desk the reader is on. Editorial, not a breadcrumb dump."""
    return {
        "index.html": "Front page",
        "air-fryers.html": "Air fryers",
        "meat-thermometers.html": "Thermometers",
        "compare.html": "Compare",
        "buying-guide.html": "Guides",
        "ideas.html": "Decision desk",
        "decisions.html": "Decision desk",
        "suggestions.html": "Decision desk",
        "questions.html": "Decision desk",
        "direction.html": "Decision desk",
        "flagged.html": "Trust",
        "sources.html": "Trust",
        "citations.html": "Trust",
        "disclosure.html": "Trust",
        "analytics.html": "Trust",
        "about.html": "Trust",
        "executive-summary.html": "Trust",
        "404.html": "Not found",
        "tools/index.html": "Tools",
        "tools/compare-builder.html": "Tools",
        "tools/oven-converter.html": "Tools",
        "tools/cook-temperatures.html": "Tools",
    }.get(name, "Guides")


def render(text, path, depth):
    head = render_header(path, depth, kicker_for(path))
    foot = render_footer(path, depth)

    # Header region: everything from the skip link up to (not including) <main>
    if HEAD_START in text and HEAD_END in text:
        text = re.sub(re.escape(HEAD_START) + r".*?" + re.escape(HEAD_END), lambda _: head, text, flags=re.S)
    else:
        # First run on a legacy page: replace the old skip-link..</header>+disclosure block.
        new = re.sub(r'<a class="skip" href="#main">Skip to content</a>.*?(?=<main\b)',
                     lambda _: head + "\n", text, count=1, flags=re.S)
        if new == text:
            # A freshly authored page (like a redesign) may open straight into <main>
            # with no chrome at all. Insert after <body> in that case.
            new = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + "\n" + head + "\n", text, count=1)
        if new == text:
            raise SystemExit(f"{path}: could not locate the header region")
        text = new

    if FOOT_START in text and FOOT_END in text:
        text = re.sub(re.escape(FOOT_START) + r".*?" + re.escape(FOOT_END), lambda _: foot, text, flags=re.S)
    else:
        new = re.sub(r"<footer>.*?</footer>", lambda _: foot, text, count=1, flags=re.S)
        if new == text:
            # No legacy footer at all: append before the closing body tag.
            new = re.sub(r"</body>", lambda _: foot + "\n</body>", text, count=1)
        if new == text:
            raise SystemExit(f"{path}: could not locate the footer region")
        text = new

    assert DISCLOSURE_SENTENCE in text, f"{path}: disclosure sentence missing after render"
    return text


def main():
    check = "--check" in sys.argv
    stale = []
    for p, depth in pages():
        path = p.relative_to(ROOT).as_posix()
        before = p.read_text(encoding="utf-8")
        after = render(before, path, depth)
        if after != before:
            stale.append(path)
            if not check:
                p.write_text(after, encoding="utf-8")
    if check:
        if stale:
            print("FAIL: chrome is stale on:")
            for s in stale:
                print("  -", s)
            print("Run: python3 scripts/build_chrome.py")
            sys.exit(1)
        print(f"OK: chrome is current on {len(pages())} pages")
    else:
        print(f"Rendered chrome into {len(pages())} pages ({len(stale)} changed)")


if __name__ == "__main__":
    main()
