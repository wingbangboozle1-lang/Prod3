#!/usr/bin/env python3
"""Rewrite sitemap.xml from the checked-in tree (or verify it with --check)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangboozle1-lang.github.io/Prod3"
DATE = "2026-11-20"

def pages():
    files = (sorted(ROOT.glob("*.html"))
             + sorted((ROOT / "articles").glob("*.html"))
             + sorted((ROOT / "tools").glob("*.html"))
             + sorted((ROOT / "products").glob("*.html")))
    files = [f for f in files if f.name != "404.html"]  # error page: never in the sitemap
    return [f.relative_to(ROOT).as_posix() for f in files]

# Editorial weight, not a search-engine lever: sitemaps.org defines <priority> and
# Google's documentation says it is ignored for ranking. It is kept because it makes
# the file readable to a human deciding what to re-check, and nothing more.
PRIORITY = {
    "index.html": "1.0",
    "air-fryers.html": "0.9",
    "meat-thermometers.html": "0.9",
    "compare.html": "0.9",
    "decisions.html": "0.8",
    "buying-guide.html": "0.8",
    "products/chefman-6qt-dual-basket.html": "0.9",
    "products/emeril-lagasse-26qt-french-door.html": "0.9",
    "products/chefman-8qt-turbofry.html": "0.9",
    "products/thermomaven-1-sec.html": "0.9",
    "products/chefiq-sense-gen3.html": "0.9",
}


def render():
    def row(p):
        pri = PRIORITY.get(p)
        extra = f"<priority>{pri}</priority>" if pri else ""
        return f"  <url><loc>{BASE}/{p}</loc><lastmod>{DATE}</lastmod>{extra}</url>"
    urls = "\n".join(row(p) for p in pages())
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'

if __name__ == "__main__":
    if "--check" in sys.argv:
        current = (ROOT / "sitemap.xml").read_text()
        if render() != current:
            print("FAIL: sitemap.xml is out of date. Run: python3 scripts/build_sitemap.py")
            sys.exit(1)
        print("OK: sitemap.xml is up to date")
    else:
        (ROOT / "sitemap.xml").write_text(render())
        print(f"Wrote sitemap.xml with {len(pages())} pages")
