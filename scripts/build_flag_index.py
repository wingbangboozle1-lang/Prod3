#!/usr/bin/env python3
"""Publish the F register (data findings) inside flagged.html, from data/flagged.json.

Why this exists: flagged.html carried FLG-001..FLG-038 plus three F rows by hand,
while data/flagged.json held 21 F rows. A register row with no published definition
is how an id ends up meaning two things — which is what FLG-040 and FLG-027 were
about. The F half of the page is therefore generated from the same file the product
pages read, so a new row cannot be published in one place and missed in the other.

Usage:
  python3 scripts/build_flag_index.py            # rewrite the block
  python3 scripts/build_flag_index.py --check     # fail if the page drifted

The block lives between the build-flags markers and is the only part this script
owns; the FLG callouts above it stay hand-written.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START = "<!-- build-flag-index:start -->"
END = "<!-- build-flag-index:end -->"
PAGE = ROOT / "flagged.html"
CURRENCY = re.compile(r"[$£€]\s?\d")
AMZ_PRODUCT = re.compile(r"^https://www\.amazon\.com/dp/[A-Z0-9]{10}$")
UNVERIFIED_MARKER = '<span class="unverified">No official source</span>'


def rows():
    data = json.loads((ROOT / "data" / "flagged.json").read_text(encoding="utf-8"))
    return [i for i in data["items"] if not i["id"].startswith("FLG")]


def cell(text):
    t = str(text or "")
    # The site publishes no prices; a quoted finding must not smuggle one in.
    t = CURRENCY.sub("a price figure (not published here)", t)
    return html.escape(t, quote=False)


def sources_for(row):
    """One link per declared source id, or the marker that says there is none.

    scripts/check_site.py rule 4 requires every row of a `data-source-required`
    table to carry a source link or the unverified marker, so a finding can never
    sit in a table with no stated origin. Links to a Product page carry the
    Associates tag, per Participation Requirements 2(b) (read 2026-11-20) — the
    same rule tools/link_tagger.py enforces across the site.
    """
    ids = row.get("sources") or []
    if not ids:
        return UNVERIFIED_MARKER + '<br><span class="small muted">recorded from the listing transcription ' \
               "in <code>data/products.json</code>; no policy page covers it</span>"
    out = []
    for sid in ids:
        src = SOURCES.get(sid)
        if not src:
            out.append(f'<span class="unverified">{html.escape(sid)} — not in the source register</span>')
            continue
        url = href_for(src["url"])
        rel = 'sponsored noopener' if ".amazon." in url else 'noopener'
        out.append(f'<a href="{html.escape(url, quote=True)}" rel="{rel}">{html.escape(sid)}</a>')
    return " · ".join(out)


TRACKING = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))["tracking_id"]
SOURCES = {s["id"]: s for s in json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))["sources"]}


def href_for(url):
    return f"{url}?tag={TRACKING}" if AMZ_PRODUCT.match(url) else url


def render():
    rs = sorted(rows(), key=lambda i: i["id"])
    out = [START]
    out.append('<div class="section-head mt"><h2>The data findings, in full</h2>'
               '<a href="data/flagged.json">data/flagged.json</a></div>')
    out.append('<p class="section-sub">These are the findings about the five listings themselves — what a '
               'listing states, what it contradicts, and what it leaves out. They are kept separate from the '
               'FLG register above, which is about the program relationship and this site. The table is '
               'generated from <code>data/flagged.json</code> by <code>scripts/build_flag_index.py</code>, '
               'so a row cannot exist in the data and be missing here.</p>')
    out.append('<div class="table-wrap"><table data-source-required="flag-register">'
               f'<caption>{len(rs)} data findings, F-01 to F-{rs[-1]["id"][-2:] if rs else "00"}. '
               'Every row is an irregularity in what was read, not a defect in a product.</caption>'
               '<thead><tr><th>ID</th><th>Severity</th><th>Subject</th><th>What was read</th>'
               '<th>Why it matters here</th><th>Handling</th><th>Source</th></tr></thead><tbody>')
    for i in rs:
        out.append("<tr>"
                   f'<td><strong>{cell(i["id"])}</strong></td>'
                   f'<td><span class="badge{chr(32)+"grey" if i.get("severity") in ("low", None) else ""}">'
                   f'{cell(i.get("severity") or "—")}</span></td>'
                   f'<td class="small">{cell(i.get("area", "—"))}<br><span class="muted">'
                   f'{cell(i.get("product", "—"))}</span></td>'
                   f'<td class="small">{cell(i.get("detail", ""))}</td>'
                   f'<td class="small">{cell(i.get("why_it_matters", ""))}</td>'
                   f'<td class="small">{cell(i.get("status", ""))}</td>'
                   f'<td class="small">{sources_for(i)}</td>'
                   "</tr>")
    out.append("</tbody></table></div>")
    srcs = sorted({s for i in rs for s in (i.get("sources") or [])})
    out.append('<p class="small muted">Source ids follow the '
               '<a href="sources.html">source register</a>'
               + (f"; the rows above cite {', '.join(cell(s) for s in srcs)}." if srcs else ".")
               + ' Quotation dates are per row in the data file.</p>')
    out.append(END)
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    page = PAGE.read_text(encoding="utf-8")
    block = render()
    if START in page and END in page:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, page, flags=re.S)
    else:
        anchor = '<p class="mt"><a href="sources.html">← Back to the source register</a>'
        if anchor not in page:
            print("FAIL: no insertion anchor in flagged.html", file=sys.stderr)
            return 2
        new = page.replace(anchor, block + "\n\n" + anchor, 1)
    if check:
        if new != page:
            print("FAIL: flagged.html is not in step with data/flagged.json — "
                  "run: python3 scripts/build_flag_index.py", file=sys.stderr)
            return 1
        print(f"OK flagged.html carries the {len(rows())}-row F register")
        return 0
    PAGE.write_text(new)
    print(f"flagged.html: F register block rebuilt ({len(rows())} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
