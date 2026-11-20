/* Kitchen Counter — privacy-preserving measurement.
   No cookies, no fingerprinting, no email or user ID. Five event types are
   counted locally in localStorage. reader_signup is reserved for a confirmed
   email-provider response and is not emitted unless an integration dispatches
   kc:reader-signup-confirmed. The self-hosted endpoint is intentionally blank:
   no server-side analytics service, origin policy, retention period or privacy
   notice has been selected, so nothing is transmitted. */
(function () {
  'use strict';
  var LS_KEY = 'kc-events-v1';
  // No server-side analytics endpoint is configured. Do not fill this in until
  // a self-hosted service, origin policy, retention, and privacy notice are ready.
  var ENDPOINT = '';
  var ALLOWED = ['page_view', 'outbound_click', 'article_read', 'chooser_complete', 'reader_signup'];

  function load() {
    try { return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); }
    catch (e) { return {}; }
  }
  function save(events) {
    try { localStorage.setItem(LS_KEY, JSON.stringify(events)); } catch (e) { /* private mode */ }
  }
  function track(event, data) {
    if (ALLOWED.indexOf(event) === -1) return;
    var events = load();
    events[event] = (events[event] || 0) + 1;
    save(events);
    renderCounts(events);
    if (ENDPOINT && typeof navigator.sendBeacon === 'function') {
      var payload = { event: event, page: location.pathname };
      // Only a 10-character ASIN may travel, and only for an outbound click.
      if (event === 'outbound_click' && data && /^[A-Z0-9]{10}$/.test(data.asin || '')) {
        payload.asin = data.asin;
      }
      // Deliberately omit email, link URL, referrer, client timestamp, and user ID.
      try {
        navigator.sendBeacon(ENDPOINT, new Blob([JSON.stringify(payload)], { type: 'text/plain;charset=UTF-8' }));
      } catch (e) { /* never break the page for a counter */ }
    }
  }

  // Footer local counter. Shows counts for this browser only.
  function renderCounts(events) {
    var el = document.getElementById('local-counts');
    if (!el) return;
    var keys = ALLOWED.filter(function (k) { return events[k]; });
    var summary = keys.map(function (k) { return k + ' × ' + events[k]; }).join(' · ');
    el.textContent = summary
      ? 'Local counts on this device only: ' + summary
      : 'Local counts on this device: none yet. Nothing is sent to a server.';
  }

  // page_view
  track('page_view', { path: location.pathname });

  // outbound_click — every supplied product link: rel="sponsored" plus an
  // Amazon product URL (www.amazon.com/dp/<10-char ASIN> or the supplied
  // link.amazon short link). Policy-page citations, the homepage evidence
  // link and non-Amazon links are not product links and are not counted.
  // The ASIN comes from data-asin when it is a real ASIN, otherwise from
  // the /dp/ path; track() only ever forwards a ^[A-Z0-9]{10}$ value.
  var PRODUCT_LINK = /^(https:\/\/www\.amazon\.com\/dp\/[A-Z0-9]{10}|https:\/\/link\.amazon\/)/;
  var outbound = document.querySelectorAll('a[rel~="sponsored"]');
  Array.prototype.forEach.call(outbound, function (a) {
    var href = a.getAttribute('href') || '';
    if (!PRODUCT_LINK.test(href)) return;
    a.addEventListener('click', function () {
      var asin = a.getAttribute('data-asin') || '';
      if (!/^[A-Z0-9]{10}$/.test(asin)) {
        var m = href.match(/\/dp\/([A-Z0-9]{10})/);
        asin = m ? m[1] : '';
      }
      track('outbound_click', { asin: asin });
    });
  });

  // article_read — 50% scroll on article pages, once per page load
  if (document.body.classList.contains('is-article')) {
    var fired = false;
    window.addEventListener('scroll', function () {
      if (fired) return;
      var h = document.documentElement;
      var pct = (h.scrollTop + h.clientHeight) / Math.max(h.scrollHeight, 1);
      if (pct >= 0.5) { fired = true; track('article_read', { path: location.pathname }); }
    }, { passive: true });
  }

  // chooser_complete — fires once per completed set of three answers
  window.addEventListener('kc:chooser-complete', function () { track('chooser_complete', {}); });

  // reader_signup — an email integration may dispatch this only after the
  // provider confirms enrollment. The static publication has no such provider.
  window.addEventListener('kc:reader-signup-confirmed', function () {
    track('reader_signup', {});
  });

  // Copy-link affordance: lets a reader share the official listing without
  // leaving the page. No network call, no tracking.
  Array.prototype.forEach.call(document.querySelectorAll('[data-copy-url]'), function (btn) {
    btn.addEventListener('click', function () {
      var url = btn.getAttribute('data-copy-url');
      var done = function () {
        var old = btn.textContent;
        btn.textContent = 'Link copied';
        setTimeout(function () { btn.textContent = old; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done, function () {});
      }
    });
  });
})();
