/* Kitchen Counter — self-hosted, privacy-preserving event collector.
 *
 * NOT DEPLOYED. This file is the server half of the measurement pair; the
 * client half is assets/app.js, whose ENDPOINT stays blank until the owner
 * deploys this collector, sets ALLOWED_ORIGIN to the live site origin, and
 * publishes a privacy notice (docs/analytics-endpoint.md). Gate D43 keeps the
 * two halves consistent: the five event names must match between this file,
 * assets/app.js and data/campaign-ledger.json, and ENDPOINT may only be filled
 * in with an https URL that analytics.html names.
 *
 * What it stores: a running count per (event, day, page) — and, for
 * outbound_click only, a count per 10-character ASIN. What it never stores or
 * logs: IP addresses, user agents, cookies, referrers, client timestamps,
 * query strings, or any personal data. Requests that do not match the payload
 * contract are answered with 204 and dropped uncounted.
 *
 * Deployable as a Cloudflare Worker, a Deno Deploy function, or any fetch()
 * handler. Adapt only the storage binding, never the payload contract.
 */

// Configuration. The owner sets these at deploy time.
const ALLOWED_ORIGIN = ''; // e.g. 'https://wingbangboozle1-lang.github.io' — blank refuses all cross-origin posts
const EVENTS = ['page_view', 'outbound_click', 'article_read', 'chooser_complete', 'reader_signup'];
const ASIN_RE = /^[A-Z0-9]{10}$/;
const PAGE_RE = /^\/[A-Za-z0-9_\/\-.]{0,120}$/;

// In-memory aggregate. Replace with a durable counter (KV, D1, SQLite) if the
// host offers one; the shape is the same: counts keyed by day|event|page|asin.
const counts = Object.create(null);

function bump(key) {
  counts[key] = (counts[key] || 0) + 1;
}

function corsHeaders(origin) {
  const headers = {
    'access-control-allow-methods': 'POST, OPTIONS',
    'access-control-allow-headers': 'content-type',
    'cache-control': 'no-store',
  };
  if (origin && origin === ALLOWED_ORIGIN) {
    headers['access-control-allow-origin'] = ALLOWED_ORIGIN;
    headers['vary'] = 'Origin';
  }
  return headers;
}

async function handleCollect(request) {
  const origin = request.headers.get('origin') || '';
  if (!ALLOWED_ORIGIN || origin !== ALLOWED_ORIGIN) {
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }
  let payload = null;
  try {
    payload = await request.json();
  } catch (e) {
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }
  const event = payload && payload.event;
  const page = payload && payload.page;
  if (EVENTS.indexOf(event) === -1) return new Response(null, { status: 204, headers: corsHeaders(origin) });
  if (typeof page !== 'string' || !PAGE_RE.test(page)) return new Response(null, { status: 204, headers: corsHeaders(origin) });

  const day = new Date().toISOString().slice(0, 10); // server-side day, not a client timestamp
  bump(day + '|' + event + '|' + page);
  if (event === 'outbound_click' && typeof payload.asin === 'string' && ASIN_RE.test(payload.asin)) {
    bump(day + '|asin|' + payload.asin);
  }
  // Everything else in the payload is ignored on purpose.
  return new Response(null, { status: 204, headers: corsHeaders(origin) });
}

addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method === 'OPTIONS') {
    event.respondWith(new Response(null, { status: 204, headers: corsHeaders(event.request.headers.get('origin') || '') }));
    return;
  }
  if (event.request.method === 'POST' && url.pathname === '/collect') {
    event.respondWith(handleCollect(event.request));
    return;
  }
  event.respondWith(new Response('Not found', { status: 404 }));
});

// Exported for the gate's syntax/consistency check and for unit-style testing
// under Node (node --check validates syntax; the names below let the gate read
// the contract without executing the file).
if (typeof module !== 'undefined') {
  module.exports = { EVENTS, ASIN_RE };
}
