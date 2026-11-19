#!/usr/bin/env python3
"""Rewrite sitemap.xml from the checked-in tree (or verify it with --check)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://wingbangboozle1-lang.github.io/Prod3"
DATE = "2026-11-19"

def pages():
    files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "articles").glob("*.html"))
    files = [f for f in files if f.name != "404.html"]  # error page: never in the sitemap
    return [f.relative_to(ROOT).as_posix() for f in files]

def render():
    urls = "\n".join(
        f"  <url><loc>{BASE}/{p}</loc><lastmod>{DATE}</lastmod></url>" for p in pages()
    )
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
