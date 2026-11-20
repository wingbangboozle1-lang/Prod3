# Self-hosted analytics collector

Status: **code shipped, not deployed.** `assets/app.js` sends nothing anywhere
until `ENDPOINT` is filled in, and gate `D43` in `tools/check_site.py` refuses a
site where `ENDPOINT` names a URL that `analytics.html` does not. No analytics
endpoint, host, or privacy notice has been selected by the owner yet.

## The two halves

| Half | File | State |
|---|---|---|
| Client | `assets/app.js` | Shipped. Counts five events in `localStorage` only. `ENDPOINT` is `''`. |
| Server | `analytics/collector/worker.js` | Shipped as deployable code. Not deployed anywhere. |

The payload contract is fixed by the client and enforced by the server:

```json
{ "event": "outbound_click", "page": "/Prod3/air-fryers.html", "asin": "B0CDY277D3" }
```

Only `event`, `page`, and (for `outbound_click` only) a 10-character `asin` are
read. The server answers `204` and drops anything else uncounted.

## What the collector stores — and what it never stores

Stores: a running count per `(day, event, page)`, and per-ASIN counts for
`outbound_click`. Nothing else.

Never stores or logs: IP addresses, user agents, cookies, referrers, client
timestamps, query strings, emails, or any personal data. The origin allowlist
is enforced server-side; a request from any other origin is dropped.

## Deploying (owner action)

1. Deploy `worker.js` to any `fetch()`-handler host (Cloudflare Workers, Deno
   Deploy, a small Node service). Keep the payload contract.
2. Set `ALLOWED_ORIGIN` to the live site origin
   (`https://wingbangboozle1-lang.github.io`) and choose durable storage for
   the `counts` map if the host offers one.
3. Decide and publish a retention period and an updated privacy notice on
   `analytics.html` and `disclosure.html`.
4. Only then set `ENDPOINT` in `assets/app.js` to the collector's **https**
   URL, and update `analytics.html` to name that URL — gate `D43` checks both
   halves and fails the build otherwise.

Until all four steps are done, `ENDPOINT` stays blank and the site measures
nothing beyond the reader's own browser.

## Consistency gates

- `D43-endpoint-consistency`: `ENDPOINT` is blank, or it is an https URL named
  on `analytics.html`.
- `D43-event-contract`: the five event names in `assets/app.js`,
  `analytics/collector/worker.js` and `data/campaign-ledger.json`
  (`events_defined`) are identical.
- The campaign ledger stays empty until authorized first-party reports exist
  (`D05-ledger-empty`). No conversion score or revenue forecast is derived
  from any of this.
