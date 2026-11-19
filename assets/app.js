/* Kitchen Counter — privacy-preserving measurement.
   No cookies, no fingerprinting, no email or user ID. Four events are
   counted locally in localStorage. reader_signup is reserved for a confirmed
   email-provider response and is not emitted unless an integration dispatches
   kc:reader-signup-confirmed. The self-hosted endpoint is intentionally blank. */
(function () {
  'use strict';
  var LS_KEY = 'kc-events-v1';
  // No server-side analytics endpoint is configured. Do not fill this in until
  // a self-hosted service, origin policy, retention, and privacy notice are ready.
  var ENDPOINT = '';

  function load() {
    try { return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); }
    catch (e) { return {}; }
  }
  function save(events) {
    try { localStorage.setItem(LS_KEY, JSON.stringify(events)); } catch (e) { /* private mode */ }
  }
  function track(event, data) {
    var allowed = ['page_view', 'outbound_click', 'article_read', 'chooser_complete', 'reader_signup'];
    if (allowed.indexOf(event) === -1) return;
    var events = load();
    events[event] = (events[event] || 0) + 1;
    save(events);
    if (ENDPOINT && navigator.sendBeacon) {
      var payload = { event: event, page: location.pathname };
      if (event === 'outbound_click' && data && /^[A-Z0-9]{10}$/.test(data.asin || '')) {
        payload.asin = data.asin;
      }
      // Deliberately omit email, link URL, referrer, client timestamp, and user ID.
      navigator.sendBeacon(ENDPOINT, new Blob([JSON.stringify(payload)], { type: 'text/plain;charset=UTF-8' }));
    }
  }

  // page_view
  track('page_view', { path: location.pathname });

  // outbound_click — every sponsored Amazon link
  document.querySelectorAll('a[data-event="outbound_click"]').forEach(function (a) {
    a.addEventListener('click', function () {
      track('outbound_click', { asin: a.getAttribute('data-asin') || '' });
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

  // reader_signup — an email integration may dispatch this only after the
  // provider confirms enrollment. The static publication has no such provider.
  window.addEventListener('kc:reader-signup-confirmed', function () {
    track('reader_signup', {});
  });

  // Dashboard counter in the footer (local counts only)
  var el = document.getElementById('local-counts');
  if (el) {
    var e = load();
    var summary = Object.keys(e).map(function (k) { return k + ' × ' + e[k]; }).join(' · ');
    el.textContent = summary ? 'Local counts on this device: ' + summary : 'Local counts on this device: none yet.';
  }
})();
