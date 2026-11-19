/* Kitchen Counter — privacy-preserving measurement.
   No cookies, no fingerprinting, no PII. Events are counted locally in
   localStorage and (optionally) beaconed to a self-hosted endpoint the
   owner configures. Five defined events: page_view, outbound_click,
   article_read, chooser_complete, reader_signup. */
(function () {
  'use strict';
  var LS_KEY = 'kc-events-v1';
  // Owner: set to your self-hosted analytics endpoint to enable server-side
  // collection, e.g. 'https://analytics.example.com/collect'. Empty = local only.
  var ENDPOINT = '';

  function load() {
    try { return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); }
    catch (e) { return {}; }
  }
  function save(events) {
    try { localStorage.setItem(LS_KEY, JSON.stringify(events)); } catch (e) { /* private mode */ }
  }
  function track(event, data) {
    var events = load();
    events[event] = (events[event] || 0) + 1;
    save(events);
    if (ENDPOINT && navigator.sendBeacon) {
      var payload = JSON.stringify({ event: event, page: location.pathname, ts: new Date().toISOString(), data: data || {} });
      navigator.sendBeacon(ENDPOINT, new Blob([payload], { type: 'application/json' }));
    }
  }

  // page_view
  track('page_view', { path: location.pathname });

  // outbound_click — every sponsored Amazon link
  document.querySelectorAll('a[data-event="outbound_click"]').forEach(function (a) {
    a.addEventListener('click', function () {
      track('outbound_click', { asin: a.getAttribute('data-asin') || '', href: a.href });
    });
  });

  // article_read — 50% scroll on article pages
  if (document.body.classList.contains('is-article')) {
    var fired = false;
    window.addEventListener('scroll', function () {
      if (fired) return;
      var h = document.documentElement;
      var pct = (h.scrollTop + h.clientHeight) / Math.max(h.scrollHeight, 1);
      if (pct >= 0.5) { fired = true; track('article_read', { path: location.pathname }); }
    }, { passive: true });
  }

  // chooser_complete — fires when the 3-question chooser produces a result
  window.addEventListener('kc:chooser-complete', function () { track('chooser_complete', {}); });

  // reader_signup — newsletter form (stores nothing; owner wires the endpoint)
  var form = document.getElementById('reader-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      track('reader_signup', {});
      var msg = document.getElementById('reader-msg');
      if (msg) msg.textContent = 'Thanks — you are on the list. (Demo form: wire your email provider to finish setup.)';
      form.reset();
    });
  }

  // Dashboard counter in the footer (local counts only)
  var el = document.getElementById('local-counts');
  if (el) {
    var e = load();
    el.textContent = 'Local counts on this device: ' +
      Object.keys(e).map(function (k) { return k + ' × ' + e[k]; }).join(' · ') || 'Local counts on this device: none yet.';
  }
})();
