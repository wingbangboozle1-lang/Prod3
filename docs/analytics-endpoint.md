# Analytics endpoint contract

Status: contract defined; handler not implemented on static GitHub Pages (flagged, does not block publication).

## Frontend (implemented)
`assets/js/analytics.js` records two event types into browser localStorage (`shopnow_events_v1`) and beacon-sends them to `POST /analytics/collect`:

- `pageview` — on every page load (payload: `{ page, referrer }`)
- `outbound_click` — on click of any `rel="sponsored"` link (payload: `{ link, targetHost, text }`)

Privacy: no cookies, no IP addresses, no personal data. If the endpoint is unavailable, the beacon fails silently and nothing breaks.

## Endpoint contract (to be implemented)
```
POST /analytics/collect
Content-Type: application/json

{
  "id": "string (uid)",
  "type": "string ('pageview' | 'outbound_click')",
  "ts": "ISO 8601 timestamp",
  "page": "string (pathname + search)",
  "referrer": "string | null",
  "payload": { "link": "string", "targetHost": "string", "text": "string" }
}
```

On success: respond 200/204 and append the event to `data/events.json` with a dated provenance trail.

## Campaign ledger (empty by design)
`data/campaign-ledger.json` fields (timestamp, source, channel, eligible sessions, clicks, reported orders) are added only when obtained from authorized first-party reports. No conversion score or revenue forecast is presented.

## Decision needed
Choose the handler (GitHub Actions `repository_dispatch` workflow writing to `data/events.json`, or a small backend). Log the decision in COORDINATION.md.
