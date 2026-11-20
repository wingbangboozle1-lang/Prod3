#!/usr/bin/env python3
"""Crawl the built tree: every internal href/src must resolve, every anchor must exist.

Why this is a separate gate
---------------------------
The existing checks resolve a relative target against the page on disk, but they do
not follow `#fragments` or prove that every page is reachable. Both failures are
invisible on disk and obvious in a browser. This crawler walks the tree the way a
reader does and exits 1 on a broken link, a dead in-page anchor, or an orphan page.

Run: python3 tools/crawl_links.py
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_PREFIX = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")


def pages():
    return (sorted(ROOT.glob("*.html"))
            + sorted((ROOT / "articles").glob("*.html"))
            + sorted((ROOT / "tools").glob("*.html"))
            + sorted((ROOT / "products").glob("*.html")))


def main():
    all_pages = pages()
    ids = {p: set(re.findall(r'id="([^"]+)"', p.read_text(encoding="utf-8"))) for p in all_pages}
    broken = []

    for p in all_pages:
        html = p.read_text(encoding="utf-8")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
            target = m.group(1)
            if target.startswith(SKIP_PREFIX):
                continue
            path_part, _, frag = target.partition("#")
            if not path_part:
                if frag and frag not in ids[p]:
                    broken.append(f"{p.relative_to(ROOT)}: dead in-page anchor #{frag}")
                continue
            resolved = (p.parent / path_part).resolve()
            if not resolved.exists():
                broken.append(f"{p.relative_to(ROOT)}: missing target {target}")
                continue
            if frag and resolved.suffix == ".html":
                if resolved in ids and frag not in ids[resolved]:
                    broken.append(f"{p.relative_to(ROOT)}: #{frag} not found in {resolved.name}")

    # Reachability: 404.html is intentionally unlinked from the tree.
    seen, queue = set(), [ROOT / "index.html"]
    while queue:
        cur = queue.pop()
        if cur in seen:
            continue
        seen.add(cur)
        for m in re.finditer(r'href="([^"#]+)', cur.read_text(encoding="utf-8")):
            t = m.group(1)
            if t.startswith(SKIP_PREFIX):
                continue
            f = (cur.parent / t).resolve()
            if f.exists() and f.suffix == ".html" and f not in seen:
                queue.append(f)

    orphans = [p.relative_to(ROOT).as_posix() for p in all_pages
               if p not in seen and p.name != "404.html"]

    print(f"{len(all_pages)} pages crawled · {len(seen)} reachable from index.html")
    if broken:
        print(f"\n{len(broken)} broken link(s):")
        for b in broken[:40]:
            print("  -", b)
    if orphans:
        print(f"\n{len(orphans)} orphan page(s) (no inbound internal link):")
        for o in orphans:
            print("  -", o)

    if broken or orphans:
        sys.exit(1)
    print("no broken links, no dead anchors, no orphans")


if __name__ == "__main__":
    main()
