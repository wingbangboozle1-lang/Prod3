#!/usr/bin/env python3
"""Rewrite sitemap.xml from the checked-in tree (or verify it with --check)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def is_verification_file(path):
    """True only for a Search Console HTML verification file (see content/measurement.md §2).

    Narrow by design: the name must be google<token>.html AND the entire body must be the
    single line "google-site-verification: <token>". Any other root HTML file, including
    one that merely starts with that line, is a page and is held to the page rules.
    """
    if not re.fullmatch(r"google[A-Za-z0-9]+\.html", path.name):
        return False
    body = path.read_text(encoding="utf-8", errors="replace").strip()
    return re.fullmatch(r"google-site-verification: [A-Za-z0-9_.\-]+", body) is not None

BASE = "https://wingbangboozle1-lang.github.io/Prod3"
DATE = "2026-11-19"

def pages():
    files = [f for f in sorted(ROOT.glob("*.html")) if not is_verification_file(f)] + sorted((ROOT / "articles").glob("*.html"))
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
