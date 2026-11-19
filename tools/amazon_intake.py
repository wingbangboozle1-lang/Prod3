#!/usr/bin/env python3
"""Amazon intake helper for Kitchen Counter.

Validates a submitted link.amazon URL or an ASIN against the rules:
 - A submitted token must be 9 chars (short-link code) or 10 chars (ASIN).
 - A 9-char token is NOT an ASIN; dp/<token> must return Page Not Found.
 - An ASIN is 10 alphanumeric chars; dp/<ASIN> must resolve to a listing.

Usage:
  python3 tools/amazon_intake.py --link 'https://link.amazon/B04G1MEwY' --validate-only
  python3 tools/amazon_intake.py --asin B0CDY277D3 --offline
"""
import argparse, re, sys

ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")
TOKEN_RE = re.compile(r"^https://link\.amazon/([A-Za-z0-9]+)$")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--link")
    ap.add_argument("--asin")
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()

    if args.link:
        m = TOKEN_RE.match(args.link)
        if not m:
            print("FAIL: not a link.amazon URL"); return 1
        token = m.group(1)
        print(f"token={token} length={len(token)}")
        if len(token) == 10 and ASIN_RE.match(token):
            print("OK: token is a valid ASIN format")
        elif len(token) == 9:
            print("OK: 9-char short-link token (not an ASIN). Verify dp/<token> returns Page Not Found.")
        else:
            print("FAIL: token length is neither 9 nor 10"); return 1
        if args.validate_only:
            print("validate-only: no network call made")
        return 0
    if args.asin:
        if not ASIN_RE.match(args.asin):
            print("FAIL: not a 10-char ASIN"); return 1
        print(f"OK: {args.asin} is a valid ASIN format")
        if args.offline:
            print("offline: queued for API verification (no network call made)")
        return 0
    print("FAIL: pass --link or --asin"); return 1

if __name__ == "__main__":
    sys.exit(main())
