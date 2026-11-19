/* Shopwise Kitchen Desk
 *
 * Two behaviours, both optional and both degrading to nothing:
 *
 *  1. The "which one is for you" chooser on /compare/.
 *  2. An outbound-click tally held entirely in this browser's localStorage.
 *
 * On the tally, deliberately: it stores one integer per product and a page
 * path is NOT stored, no timestamp, no session id, no cookie, and nothing is
 * ever sent anywhere. Clearing site data removes it permanently. That design
 * is a compliance requirement, not a preference — Amazon's Program Policies
 * forbid associating any tracking id with an individual user, so the counter
 * cannot create one. See /dashboard/measurement.html.
 */
(function () {
  "use strict";

  var STORE_KEY = "swkd.clicks.v1";

  /* ------------------------------------------------------------ chooser */

  var PATHS = {
    air: {
      q: "2. How much counter depth do you have, and who are you cooking for?",
      opts: [
        {
          label: "Under 15 inches, or one or two people",
          out: {
            title: "A basket fryer. Start with the Chefman TurboFry 8 Qt.",
            why: "12.75 in deep, the shallowest of the three, single 8 qt basket with a 450 F high-heat mode. Simple, and it fits.",
            href: "/product/chefman-turbofry-8-quart-air-fryer.html",
            label: "Read the Chefman TurboFry page"
          }
        },
        {
          label: "Two components most nights, two or three people",
          out: {
            title: "The Chefman dual-basket machine.",
            why: "Two independent 3 qt drawers with Sync Finish, 13.38 in deep. It exists for cooking two things that need to land together.",
            href: "/product/chefman-6-quart-dual-basket-air-fryer.html",
            label: "Read the dual-basket page"
          }
        },
        {
          label: "I have 17 inches and cook for four to six",
          out: {
            title: "The Emeril Lagasse 26QT oven.",
            why: "26 qt, French doors, fits a 12 in pizza or a 6 lb chicken. It is really a second oven that also air fries.",
            href: "/product/emeril-lagasse-26qt-french-door-air-fryer-oven.html",
            label: "Read the Emeril page"
          }
        }
      ]
    },
    thermo: {
      q: "2. What do you want from a thermometer?",
      opts: [
        {
          label: "A reading, right now, then I am done",
          out: {
            title: "An instant-read. The ThermoMaven 1 Sec.",
            why: "One second claimed, IP67, and it ships with a calibration certificate you can check yourself in an ice bath.",
            href: "/product/thermomaven-1-sec-instant-read-thermometer.html",
            label: "Read the ThermoMaven page"
          }
        },
        {
          label: "Leave the food and be told when it is done",
          out: {
            title: "A wireless probe. The CHEF iQ Sense.",
            why: "Three probes, five sensors including an ambient one, readings over Wi-Fi. It needs a phone, which is the trade.",
            href: "/product/chef-iq-sense-wireless-thermometer.html",
            label: "Read the CHEF iQ page"
          }
        }
      ]
    }
  };

  function initChooser() {
    var root = document.querySelector("[data-chooser]");
    if (!root) return;

    var step2 = root.querySelector('[data-step="2"]');
    var out = root.querySelector("[data-out]");
    var qEl = root.querySelector("[data-q]");
    var optsEl = root.querySelector("[data-opts]");
    var step1 = root.querySelector('[data-step="1"]');

    root.querySelectorAll("[data-step='1'] .choice").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var path = PATHS[btn.getAttribute("data-v")];
        if (!path) return;
        step1.hidden = true;
        step2.hidden = false;
        out.hidden = true;
        qEl.textContent = path.q;
        optsEl.innerHTML = "";
        path.opts.forEach(function (opt) {
          var b = document.createElement("button");
          b.className = "choice";
          b.type = "button";
          b.textContent = opt.label;
          b.addEventListener("click", function () {
            step2.hidden = true;
            out.hidden = false;
            out.innerHTML = "";
            var h = document.createElement("h3");
            h.textContent = opt.out.title;
            var p = document.createElement("p");
            p.textContent = opt.out.why;
            var a = document.createElement("a");
            a.className = "btn btn-solid";
            a.href = opt.out.href;
            a.textContent = opt.out.label;
            var again = document.createElement("button");
            again.className = "chooser-again";
            again.type = "button";
            again.textContent = "Start again";
            again.addEventListener("click", reset);
            out.appendChild(h);
            out.appendChild(p);
            out.appendChild(a);
            out.appendChild(document.createElement("br"));
            out.appendChild(again);
          });
          optsEl.appendChild(b);
        });
      });
    });

    function reset() {
      step1.hidden = false;
      step2.hidden = true;
      out.hidden = true;
    }
  }

  /* ------------------------------------------------------------ counter */

  function readStore() {
    try {
      var raw = window.localStorage.getItem(STORE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function bump(productId) {
    var data = readStore();
    data[productId] = (data[productId] || 0) + 1;
    try {
      window.localStorage.setItem(STORE_KEY, JSON.stringify(data));
    } catch (e) {
      /* private mode, full quota, or storage disabled: nothing happens, by design */
    }
  }

  function initCounter() {
    document.addEventListener("click", function (ev) {
      var el = ev.target;
      while (el && el !== document.body) {
        if (el.hasAttribute && el.hasAttribute("data-product")) {
          bump(el.getAttribute("data-product"));
          return;
        }
        el = el.parentNode;
      }
    }, { passive: true });
  }

  function boot() {
    initChooser();
    initCounter();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
