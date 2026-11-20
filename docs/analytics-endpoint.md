# Analytics endpoint contract

Status: **local measurement implemented; server collection not configured** (owner decision required — see FLG-015 and `analytics.html`).
Last reconciled with code: 2026-11-20, session arena/71a41253-prod3. The five-event names and emission conditions were checked against `assets/app.js` in this repository; no server endpoint is configured.

## What ships today (`assets/app.js`)

The page script counts events in the browser's `localStorage` under the key `kc-events-v1`. It sets no cookies and reads no user ID, email, referrer or link URL.

The five events defined in `data/campaign-ledger.json` (`events_defined`):

| Event | Emitted by the shipped script | Trigger |
| --- | --- | --- |
| `page_view` | Yes | Every page load |
| `outbound_click` | Yes | Click on any `a[data-event="outbound_click"]` (sponsored Amazon links); the ASIN is sent only if it matches `^[A-Z0-9]{10}$` |
| `article_read` | Yes | Article pages (`body.is-article`) reach 50% scroll depth |
| `chooser_complete` | Yes | Window event `kc:chooser-complete` fired by the three-question chooser |
| `reader_signup` | **No, by design** | Only after an email provider dispatches `kc:reader-signup-confirmed`. No provider is connected, so it never fires. |

The footer counter shows these local counts only. It is a single-device counter, not a visitor total.

## Server endpoint (not implemented)

`ENDPOINT` in `assets/app.js` is intentionally `''`. When it is empty the script never calls `navigator.sendBeacon`, so nothing leaves the browser. GitHub Pages is static hosting and cannot receive POSTs.

If an endpoint is later chosen, the payload the script would send is:

```json
{ "event": "outbound_click", "page": "/Prod3/air-fryers.html", "asin": "B0CDY277D3" }
```

It omits the link URL, referrer, client timestamp and user ID by design. Before the value of `ENDPOINT` is set, the following must be decided and tested:

1. Handler: a hosted service (for example a small backend) or a GitHub Actions workflow. GitHub Actions cannot receive a browser POST directly; it would need an external relay.
2. Origin policy (CORS / allowed origin for `https://wingbangboozle1-lang.github.io`).
3. Retention period, access controls and an updated privacy notice (`disclosure.html`, `analytics.html`).
4. Where received events are written, with a dated provenance trail.

## Campaign ledger (empty by design)

`data/campaign-ledger.json` fields (timestamp, source, channel, eligible sessions, clicks, reported orders) are added only from authorized first-party reports (Amazon Associates reports or the site's own analytics once enabled). No conversion score or revenue forecast is presented.
