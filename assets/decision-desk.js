/* Kitchen Counter — decision desk, local only.
   The path buttons record a choice in localStorage so the page can reflect what you
   picked while you read. Nothing is transmitted, there is no server, and the value is
   not a commitment: the real record is the dated decision log, edited by hand. */
(function () {
  'use strict';
  var KEY = 'kc-path-choice-v1';
  var status = document.getElementById('path-status');
  if (!status) return;

  var buttons = document.querySelectorAll('[data-choose-path]');

  function paint(choice) {
    Array.prototype.forEach.call(buttons, function (b) {
      var isChosen = b.getAttribute('data-choose-path') === choice;
      b.textContent = isChosen ? 'Recorded on this device ✓' : 'Record ' + b.getAttribute('data-choose-path') + ' as the chosen path';
      b.disabled = false;
      var card = b.closest('.path-card');
      if (card) card.setAttribute('data-selected', isChosen ? 'true' : 'false');
    });
    if (!choice) return;
    status.innerHTML = '<strong>' + choice + ' is recorded on this device.</strong> ' +
      'That is a note to yourself, not a change to the site. To make it real, the choice is added to the ' +
      'dated decision log by hand, and the rows it includes move from proposed to in progress. ' +
      'Clear it any time with the button below.';
    if (!document.getElementById('clear-path')) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.id = 'clear-path';
      btn.className = 'btn ghost';
      btn.style.marginTop = '12px';
      btn.textContent = 'Clear my local choice';
      btn.addEventListener('click', function () {
        try { localStorage.removeItem(KEY); } catch (e) {}
        btn.remove();
        paint('');
        status.innerHTML = '<strong>No path recorded yet.</strong> This button writes your choice to this browser only, ' +
          'so the page can show what you picked while you read. It is not a server record and it is not a commitment.';
      });
      status.appendChild(document.createElement('div')).appendChild(btn);
    }
  }

  Array.prototype.forEach.call(buttons, function (b) {
    b.addEventListener('click', function () {
      var choice = b.getAttribute('data-choose-path');
      try { localStorage.setItem(KEY, choice); } catch (e) { /* private mode: still show it */ }
      paint(choice);
      window.dispatchEvent(new Event('kc:chooser-complete'));
    });
  });

  var saved = '';
  try { saved = localStorage.getItem(KEY) || ''; } catch (e) {}
  paint(saved);
})();
