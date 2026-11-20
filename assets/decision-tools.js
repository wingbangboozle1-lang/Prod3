/* Kitchen Counter — decision tools, no network, no storage.
   Three small calculators that do arithmetic on numbers the listings publish, plus
   the USDA safe-minimum table. None of them predicts performance, and each says so
   in the markup rather than only here. */
(function () {
  'use strict';

  /* ------------------------------------------------------------------
     1. Comparison builder
     Specs transcribed from data/products.json (observed 2026-11-20).
     Anything not on a listing is null and renders as "Not published".
     ------------------------------------------------------------------ */
  var PRODUCTS = [
    {
      name: 'Chefman 6 Qt Dual Basket', asin: 'B0CDY277D3', link: 'https://link.amazon/B04G1MEwY',
      listing: 'https://www.amazon.com/dp/B0CDY277D3',
      capacity_qt: 6, baskets: 2, layout: 'Dual basket',
      temp_min: 200, temp_max: 450, watts: 1700,
      depth: 13.38, width: 11.81, height: 10.63,
      presets: null, probes: null, connectivity: null
    },
    {
      name: 'Emeril Lagasse 26QT Oven', asin: 'B09B7SB46R', link: 'https://link.amazon/B02NbDxp3',
      listing: 'https://www.amazon.com/dp/B09B7SB46R',
      capacity_qt: 26, baskets: 1, layout: 'Oven cavity',
      temp_min: 75, temp_max: 500, watts: 1700,
      depth: 16.9, width: 15.8, height: 14.8,
      presets: null, probes: null, connectivity: null
    },
    {
      name: 'Chefman 8 Qt TurboFry', asin: 'B08DKYBTPH', link: 'https://link.amazon/B00hJ57DV',
      listing: 'https://www.amazon.com/dp/B08DKYBTPH',
      capacity_qt: 8, baskets: 1, layout: 'Single basket',
      temp_min: 200, temp_max: 400, watts: 1700,
      depth: 12.75, width: 13.5, height: 10,
      presets: null, probes: null, connectivity: null
    },
    {
      name: 'ThermoMaven 1 Sec', asin: 'B0DHZTCNR5', link: 'https://link.amazon/B0c8moW59',
      listing: 'https://www.amazon.com/dp/B0DHZTCNR5',
      capacity_qt: null, baskets: null, layout: 'Instant-read',
      temp_min: null, temp_max: null, watts: null,
      depth: null, width: null, height: null,
      presets: null, probes: 1, connectivity: 'None listed'
    },
    {
      name: 'CHEF iQ Sense Gen3', asin: 'B0DZFD6R9Z', link: 'https://link.amazon/B0f3GKalj',
      listing: 'https://www.amazon.com/dp/B0DZFD6R9Z',
      capacity_qt: null, baskets: null, layout: 'Wireless probes',
      temp_min: null, temp_max: null, watts: null,
      depth: null, width: null, height: null,
      presets: null, probes: 3, connectivity: 'WiFi + Bluetooth'
    }
  ];

  var SPECS = [
    { key: 'capacity_qt', label: 'Listed capacity (qt)', suffix: ' qt' },
    { key: 'layout', label: 'Layout' },
    { key: 'temp_min', label: 'Lowest listed setting (°F)' },
    { key: 'temp_max', label: 'Highest listed setting (°F)' },
    { key: 'watts', label: 'Listed power (W)' },
    { key: 'depth', label: 'Listed depth (in)', suffix: ' in' },
    { key: 'width', label: 'Listed width (in)', suffix: ' in' },
    { key: 'height', label: 'Listed height (in)', suffix: ' in' },
    { key: 'probes', label: 'Probes' },
    { key: 'connectivity', label: 'Connectivity listed' }
  ];

  function buildComparison() {
    var form = document.getElementById('compare-form');
    if (!form) return;
    var out = document.getElementById('compare-out');
    var checked = function (name) {
      return Array.prototype.slice.call(form.querySelectorAll('input[name="' + name + '"]:checked'))
        .map(function (i) { return i.value; });
    };
    function render() {
      var rows = checked('spec');
      var cols = checked('product');
      if (!rows.length || !cols.length) {
        out.innerHTML = '<p class="small muted">Pick at least one spec and one product.</p>';
        return;
      }
      var chosen = PRODUCTS.filter(function (p) { return cols.indexOf(p.asin) !== -1; });
      var head = '<tr><th>Spec</th>' + chosen.map(function (p) {
        return '<th>' + p.name + '<br><span class="muted" style="font-weight:500">' + p.asin + '</span></th>';
      }).join('') + '</tr>';
      var body = rows.map(function (key) {
        var spec = SPECS.filter(function (s) { return s.key === key; })[0];
        var cells = chosen.map(function (p) {
          var v = p[key];
          if (v === null || v === undefined || v === '') {
            return '<td><span class="novalue">Not published</span></td>';
          }
          return '<td>' + v + (spec.suffix || '') + '</td>';
        }).join('');
        return '<tr><td><strong>' + spec.label + '</strong></td>' + cells + '</tr>';
      }).join('');
      var links = '<tr><td><strong>Official listing</strong></td>' + chosen.map(function (p) {
        return '<td><a href="' + p.listing + '" rel="sponsored noopener" target="_blank">' + p.asin + '</a></td>';
      }).join('') + '</tr>';
      out.innerHTML = '<div class="table-wrap"><table data-source-required="product-listing">' +
        '<thead>' + head + '</thead><tbody>' + body + links + '</tbody></table></div>' +
        '<p class="attrib">Every cell is a seller statement from the official listing, read 2026-11-20. ' +
        '“Not published” means the listing does not state it — it is not zero.</p>';
    }
    form.addEventListener('change', render);
    render();
  }

  /* ------------------------------------------------------------------
     2. Oven-to-air-fryer starting temperature
     Arithmetic only: the widely repeated starting point is 25°F lower than the
     oven temperature, with time reduced. That rule is a convention, not a
     measurement, and it is labelled as one in the markup.
     ------------------------------------------------------------------ */
  function ovenConverter() {
    var input = document.getElementById('oven-temp');
    if (!input) return;
    var out = document.getElementById('convert-out');
    var range = document.getElementById('oven-range');
    function render() {
      var v = parseInt(input.value, 10);
      if (isNaN(v)) { out.innerHTML = ''; return; }
      var low = Math.round((v - 25) / 5) * 5;
      var min = Math.max(200, low - 10);
      var max = Math.min(450, low + 10);
      out.innerHTML =
        '<p style="font-size:1.15rem;margin:.3em 0"><strong>A starting point: ' + low + '°F</strong></p>' +
        '<p class="small" style="margin:.2em 0">Try the range <strong>' + min + '–' + max + '°F</strong>, ' +
        'and start checking earlier than the oven recipe says.</p>' +
        '<p class="attrib" style="margin-top:12px">This is the common 25°F-lower convention, applied as arithmetic and ' +
        'clamped to the 200–450°F range our air-fryer listings publish. It is <strong>not</strong> a tested conversion: ' +
        'basket size, food load and the model all change the result. Use it as a first attempt, then adjust.</p>';
      if (range) {
        range.textContent = 'Oven setting: ' + v + '°F → air-fryer starting point ' + low + '°F';
      }
    }
    input.addEventListener('input', render);
    render();
  }

  /* ------------------------------------------------------------------
     3. Cook-to-temperature lookup
     Values are the USDA FSIS safe minimum internal temperatures, verbatim
     from S17 (https://www.fsis.usda.gov/.../safe-temperature-chart).
     Rest times are part of the same table and are NOT optional.
     ------------------------------------------------------------------ */
  var USDA = [
    ['Beef, pork, veal and lamb — steaks, chops, roasts', '145°F (62.8°C)', 'Rest at least 3 minutes'],
    ['Ground meats (beef, pork, veal, lamb)', '160°F (71.1°C)', 'No rest time specified'],
    ['Ground poultry', '165°F (73.9°C)', 'No rest time specified'],
    ['Ham, fresh or smoked (uncooked)', '145°F (62.8°C)', 'Rest at least 3 minutes'],
    ['All poultry — breasts, whole bird, legs, thighs, wings, giblets, stuffing', '165°F (73.9°C)', 'No rest time specified'],
    ['Eggs', '160°F (71.1°C)', 'No rest time specified'],
    ['Fish and shellfish', '145°F (62.8°C)', 'No rest time specified'],
    ['Leftovers', '165°F (73.9°C)', 'No rest time specified'],
    ['Casseroles', '165°F (73.9°C)', 'No rest time specified']
  ];

  function cookTable() {
    var body = document.getElementById('usda-body');
    if (!body) return;
    var filter = document.getElementById('usda-filter');
    function render() {
      var q = (filter && filter.value || '').toLowerCase();
      body.innerHTML = USDA.filter(function (r) {
        return !q || r.join(' ').toLowerCase().indexOf(q) !== -1;
      }).map(function (r) {
        return '<tr><td><strong>' + r[0] + '</strong></td><td>' + r[1] + '</td><td>' + r[2] + '</td></tr>';
      }).join('') || '<tr><td colspan="3" class="small muted">No match.</td></tr>';
    }
    if (filter) filter.addEventListener('input', render);
    render();
  }

  /* ------------------------------------------------------------------
     4. Oven-style vs basket layout side-by-side helper (used on the compare page)
     Kept separate so a page without the tool does nothing.
     ------------------------------------------------------------------ */
  function footprintNote() {
    var el = document.getElementById('footprint-note');
    if (!el) return;
    var d = [13.38, 16.9, 12.75];
    var min = Math.min.apply(null, d), max = Math.max.apply(null, d);
    el.textContent = 'Listed depths in this set run from ' + min + ' in to ' + max + ' in — a spread of ' +
      (Math.round((max - min) * 100) / 100) + ' in. That difference is the number to check against your counter.';
  }

  buildComparison();
  ovenConverter();
  cookTable();
  footprintNote();
})();
