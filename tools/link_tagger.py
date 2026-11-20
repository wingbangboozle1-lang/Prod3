#!/usr/bin/env python3
"""Outbound-link tagger and checker for Kitchen Counter.

Why this exists
---------------
Amazon's Associates Program Policies (Associates Program Participation
Requirements, section 2 "Links on Your Site" -> 2(b) "General Requirements
Applicable to All Special Links") state:

    "you must include your Associates ID or \u202ctag\u201d (appearing as XXXXX-##,
     or such other format as we may designate) as a parameter in the URL of
     each link you place on your Site to an Amazon Site."

and section 2(a) states that "Special Links must use the Associates ID we have
assigned to you". The Commission Income Statement (1(a)) makes a click through a
Special Link the condition of a Qualifying Purchase, so an untagged link is both
a policy gap and an unmonetised one. The same requirement is restated in the
Operating Agreement, section 1: "The links must properly use the special
\u202ctagged\u201d link formats we provide".

Source: https://affiliate-program.amazon.com/help/operating/policies and
https://affiliate-program.amazon.com/help/operating/agreement
(both read line by line on 2026-11-20; policies updated 2026-04-14,
agreement updated 2025-10-15).

What it does
------------
* Every `<a href="https://www.amazon.com/dp/<10-char ASIN>">` in the published
  HTML must carry `?tag=<tracking id>`.
* Every `<a href="https://link.amazon/<token>">` is replaced by the tagged listing
  URL recorded in `data/products.json` as that token's *observed* destination.
  Plain-text mentions of a supplied link -- in the registers, the docs and the
  flag rows -- are records of what the owner submitted, so they are never touched.
* A link to a 9-character token path (`/dp/B04G1MEwY`) is left alone: it is
  published as evidence of an observation, it is not a Product link, and a
  Special Link must link to a Product.

Usage
  python3 tools/link_tagger.py            # rewrite in place, print a diff summary
  python3 tools/link_tagger.py --check    # exit 1 if any product link is untagged
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY_URL = "https://affiliate-program.amazon.com/help/operating/policies"
ANCHOR = re.compile(
    r'(<a\b[^>]*?href=")(https://(?:www\.amazon\.com/dp/([A-Z0-9]{10})|link\.amazon/([A-Za-z0-9]+)))(")([^>]*>)'
)


def load() -> tuple[str, dict[str, str]]:
    doc = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))
    track = doc["tracking_id"]
    tokens = {}
    for p in doc["products"]:
        if p.get("observed_asin"):
            tokens[p["submitted_token"]] = p["observed_asin"]
    return track, tokens


def pages():
    return (sorted(ROOT.glob("*.html"))
            + sorted((ROOT / "articles").glob("*.html"))
            + sorted((ROOT / "products").glob("*.html"))
            + sorted((ROOT / "tools").glob("*.html")))


def shape_problems(html: str) -> list[str]:
    """Structural guard, used on the rewrite output and in --check mode.

    A replacement that drops an anchor's closing ">" turns the link's own text
    into tag soup and the browser renders no link at all. That is what the first
    run of this tool did, so the guard ships with it: no attribute value may be
    followed immediately by a non-space, and every opening anchor needs a match.
    """
    problems: list[str] = []
    for m in re.finditer(r"<a\b[^>]*>", html):
        tag = m.group(0)
        if re.search(r'="[^"]*"[^\s>]', tag):
            problems.append(f"malformed anchor tag: {tag[:100]}")
    opens = html.count("<a ") + html.count("<a>")
    if opens != html.count("</a>"):
        problems.append(f"{opens} opening anchor(s) vs {html.count('</a>')} closing")
    return problems


def scan(html: str, track: str, tokens: dict[str, str]) -> tuple[str, list[str], list[str], int]:
    """Return (rewritten html, rewrites made, violations, anchors changed)."""
    rewrites: list[str] = []
    violations: list[str] = []
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        # Groups: 1 "<a ... href="  2 the old URL  3 a /dp/ ASIN  4 a short-link token
        #         5 the closing quote  6 everything from there to ">" inclusive.
        # Group 6 MUST be re-emitted: on links written as <a href="…" rel="…"> the
        # qualifiers live after the href, and dropping them silently turns the
        # anchor's own text into part of the tag. (This happened on the first run
        # of this tool; the SHAPE guard below is what makes it unreproducible.)
        dp_asin, token, tail = m.group(3), m.group(4), m.group(6)
        if dp_asin:
            if f"tag={track}" in tail:
                return m.group(0)
            new = f"https://www.amazon.com/dp/{dp_asin}?tag={track}"
            rewrites.append(f"untagged /dp/{dp_asin} -> tagged")
        else:
            asin = tokens.get(token)
            if asin is None:
                violations.append(f"link.amazon/{token} has no observed ASIN in data/products.json")
                return m.group(0)
            new = f"https://www.amazon.com/dp/{asin}?tag={track}"
            rewrites.append(f"link.amazon/{token} -> {new}")
        changed += 1
        return f"{m.group(1)}{new}{m.group(5)}{tail}"

    # A product link written any other way (no query string at all) is caught by
    # the sweep below, which looks at every dp/<10-char> href rather than only
    # the ones the rewrite pattern recognised.
    for m in re.finditer(r'<a\b[^>]*href="https://www\.amazon\.com/dp/([A-Z0-9]{10})(\?[^"]*)?"[^>]*>', html):
        if f"tag={track}" not in (m.group(2) or ""):
            violations.append(f"/dp/{m.group(1)} appears without the tag parameter")
    out = ANCHOR.sub(repl, html)
    return out, sorted(set(rewrites)), violations, changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; exit 1 when a product link is untagged")
    args = ap.parse_args()

    track, tokens = load()
    bad = 0
    for f in pages():
        before = f.read_text(encoding="utf-8")
        after, rewrites, violations, changed = scan(before, track, tokens)
        if args.check:
            for p in shape_problems(before):
                print(f"FAIL {f.relative_to(ROOT)}: {p}")
                bad += 1
            if violations:
                bad += len(violations)
                print(f"FAIL {f.relative_to(ROOT)}")
                for v in violations:
                    print("   -", v)
        elif rewrites:
            broken = shape_problems(after)
            if broken:
                print(f"ABORT {f.relative_to(ROOT)}: the rewrite would produce malformed HTML; nothing written")
                for p in broken:
                    print("   -", p)
                return 2
            f.write_text(after, encoding="utf-8")
            print(f"{f.relative_to(ROOT)}: {changed} anchor(s) updated")
    if args.check:
        if bad:
            print(f"\n{bad} outbound Amazon product link(s) do not carry tag={track}")
            print("Rule source:", POLICY_URL, "(Participation Requirements 2(b)), read 2026-11-20")
            return 1
        print(f"OK every amazon.com/dp product link carries tag={track}")
        return 0
    print("\nDone. Re-run the release gates, then review the diff before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
