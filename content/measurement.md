# Measurement

Status: **local measurement implemented; first-party reporting not configured** (owner decision required — see F-10, F-17 and `docs/analytics-endpoint.md`).
Last reconciled with code: 2026-11-20, session arena/0a1638a1-prod3.

This file is the place the two measurement gaps point at. It exists because
`data/flagged.json` (F-17) and `data/policy-checks.json` (C-13) both refer to a
measurement document; until this file was written, those two references pointed
at nothing.

## 1. What the site measures today

The page script in `assets/app.js` counts five events in the browser's
`localStorage` under the key `kc-events-v1`. It sets no cookies and reads no
user ID, email, referrer or link URL.

| Event | Emitted by the shipped script | Trigger |
| --- | --- | --- |
| `page_view` | Yes | Every page load |
| `outbound_click` | Yes | Click on any `a[data-event="outbound_click"]` (sponsored Amazon links); the ASIN is sent only if it matches `^[A-Z0-9]{10}$` |
| `article_read` | Yes | Article pages (`body.is-article`) reach 50% scroll depth |
| `chooser_complete` | Yes | Window event `kc:chooser-complete` fired by the three-question chooser |
| `reader_signup` | **No, by design** | Only after an email provider dispatches `kc:reader-signup-confirmed`. No provider is connected, so it never fires. |

The footer counter shows these local counts only. It is a single-device
counter, not a visitor total. The full payload contract for a future server
endpoint is in `docs/analytics-endpoint.md`; `ENDPOINT` in `assets/app.js` is
intentionally empty, so nothing leaves the browser.

## 2. Search Console verification — the file slot

Search Console verification is an owner action. It needs either a DNS TXT
record on the domain, or a verification file served from the root of the
property. The property for this site is
`https://wingbangboozle1-lang.github.io/Prod3/`, so the file has to be served
from the root of the repository, not from a subdirectory.

**The slot.** Drop the file Google gives you at the root of the repository,
keeping its exact name:

```
google1a2b3c4d5e6f7a8b9.html
```

Its contents are a single line:

```
google-site-verification: 1a2b3c4d5e6f7a8b9
```

The site is published straight from the repository root, so the file is served
at `https://wingbangboozle1-lang.github.io/Prod3/google1a2b3c4d5e6f7a8b9.html`
with no build step in between.

**The gate exemption.** `scripts/check_site.py` treats every root-level
`*.html` file as a published page and requires it to carry a title, a meta
description, the disclosure strip, the footer disclosure, the tracking ID, and
an entry in `sitemap.xml`. A verification file is a bare token with none of
those, so the release gates recognise it by shape and exempt it. The same rule
is implemented in `scripts/check_site.py`, `tools/check_site.py` and
`scripts/build_sitemap.py`, and it is narrow: a root file is exempt only when
its name is `google<token>.html` **and** its entire body is the single line
`google-site-verification: <token>` (the token may contain dots, as Google's
own files do). Anything else, including a page that merely starts with that
line, is held to the page rules. The exempt file is deliberately left out of
`sitemap.xml`, and `tools/check_site.py` fails if it ever appears there.

**DNS instead.** A DNS TXT record on the host is equivalent and needs no
repository file at all. It is an owner decision (Q-18); this document only
records that the file route exists if DNS is inconvenient.

**After verification.** The owner adds the property, verifies it, submits
`https://wingbangboozle1-lang.github.io/Prod3/sitemap.xml`, and then Search
Console reports queries, impressions and clicks for the property. Until that
happens the site has no query data, and no guide may be chosen from one (SG-07,
SG-18, Q-07, Q-17, Q-18).

## 3. The analytics stub

There is no server endpoint, and GitHub Pages — static hosting — cannot
receive a POST. The stub is therefore the empty `ENDPOINT` constant in
`assets/app.js`: when it is empty the script never calls
`navigator.sendBeacon`. If the owner later enables one, the rules are:

1. No cookies, no per-user identifier, no IP address stored.
2. Payload limited to event name, page path and (for `outbound_click`) the
   ASIN. No link URL, no referrer, no client timestamp, no user ID.
3. Retention period and access controls written down before the first write,
   and reflected in `analytics.html` and `disclosure.html`.
4. The rows that land in `data/campaign-ledger.json` come from authorized
   first-party reports only, with a dated provenance trail. The ledger ships
   empty by design (SG-14, FLG-015).

## 4. What may not be claimed

Until a first-party report exists, the site publishes no traffic figure, no
conversion rate, no revenue figure and no commission figure. The ledger stays
empty, the counter in the footer is labelled as a local device count, and the
campaign ledger has no rows. This is recorded as F-10 and as FLG-015.
