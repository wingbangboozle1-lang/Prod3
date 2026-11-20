#!/usr/bin/env python3
"""Apply the 2026-11-20 independent re-check (session arena/0f115b2d-prod3, task T-46).

Two observations are recorded per product, and neither overwrites the other:

  live_recheck_2026_11_20      - the first 2026-11-20 check, by session arena/70e8475c-prod3
  independent_recheck_2026_11_20 - this session's later, separate check of the same links

  listing_verified_2026_11_20   - the control: the official /dp/<ASIN> page for the same
                                   product, fetched the same day, read for the page title
                                   and the browse-node breadcrumb

Cause is not established and this does not assert that any supplied link is invalid.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "data" / "products.json"

# Observation made by this session on 2026-11-20: every one of the five supplied
# link.amazon short links ended at the Amazon.com homepage. The /dp/<ASIN> control
# for the same five products rendered the correct listing page every time.
RECHECK = {
    "P-01": {
        "final_url": "https://www.amazon.com/",
        "asin_in_final_url": None,
        "listing_url_checked": "https://www.amazon.com/dp/B0CDY277D3",
        "listing_title_read": "Amazon.com: CHEFMAN 6 Quart Dual Basket Air Fryer Oven with Easy View Windows, Sync Finish, Hi-Fry, Auto Shutoff, 2 Independent 3Qt Nonstick Dishwasher Safe Frying Baskets, Digital Double Air Fryer - Black : Home & Kitchen",
        "breadcrumb_node_read": "17659096011",
        "breadcrumb_path_read": "Home & Kitchen > Kitchen & Dining > Small Appliances > Fryers (17659095011) > Air Fryers (17659096011)",
    },
    "P-02": {
        "final_url": "https://www.amazon.com/",
        "asin_in_final_url": None,
        "listing_url_checked": "https://www.amazon.com/dp/B09B7SB46R",
        "listing_title_read": "Amazon.com: Emeril Lagasse 26QT French Door Multi-Function Air Fryer Toaster Oven | Countertop Convection Cooker, 24 One-Touch Preset Options, Extra Large Interior, Six Cooking Accessories Included : Home & Kitchen",
        "breadcrumb_node_read": "17659096011",
        "breadcrumb_path_read": "Home & Kitchen > Kitchen & Dining > Small Appliances > Fryers (17659095011) > Air Fryers (17659096011)",
    },
    "P-03": {
        "final_url": "https://www.amazon.com/",
        "asin_in_final_url": None,
        "listing_url_checked": "https://www.amazon.com/dp/B08DKYBTPH",
        "listing_title_read": "Amazon.com: Chefman Air Fryer 8 Qt | TurboFry 4-in-1 with 450°F Hi-Fry Option for Crispier Results | Bake, Dehydrate, Frozen | XL Nonstick Dishwasher-Safe Basket | Stainless Steel : Home & Kitchen",
        "breadcrumb_node_read": "17659096011",
        "breadcrumb_path_read": "Home & Kitchen > Kitchen & Dining > Small Appliances > Fryers (17659095011) > Air Fryers (17659096011)",
    },
    "P-04": {
        "final_url": "https://www.amazon.com/",
        "asin_in_final_url": None,
        "listing_url_checked": "https://www.amazon.com/dp/B0DHZTCNR5",
        "listing_title_read": "Amazon.com: ThermoMaven 1 Sec Professional Digital Meat Thermometer, ±0.5℉ Accuracy | NIST&NSF Certified, Auto-Rotate Bright LED Screen, IP67 Waterproof for Grill BBQ, Stocking Stuffers Gifts for Men, Black : Home & Kitchen",
        "breadcrumb_node_read": "289810",
        "breadcrumb_path_read": "Home & Kitchen > Kitchen & Dining > Kitchen Utensils & Gadgets (289754) > Thermometers & Timers (289807) > Meat (289810)",
    },
    "P-05": {
        "final_url": "https://www.amazon.com/",
        "asin_in_final_url": None,
        "listing_url_checked": "https://www.amazon.com/dp/B0DZFD6R9Z",
        "listing_title_read": "Amazon.com: CHEF iQ Sense | Smart Wireless Meat Thermometer | 3 Ultra-Thin Probes | WiFi Unlimited Range | 1000°F Heat Safe | 5 Sensors | BBQ, Grill, Oven, Smoker, Air Fryer | Gen3 : Home & Kitchen",
        "breadcrumb_node_read": "289810",
        "breadcrumb_path_read": "Home & Kitchen > Kitchen & Dining > Kitchen Utensils & Gadgets (289754) > Thermometers & Timers (289807) > Meat (289810)",
    },
}


def main():
    d = json.loads(P.read_text())
    for prod in d["products"]:
        rec = RECHECK[prod["id"]]
        prod["independent_recheck_2026_11_20"] = {
            "date": "2026-11-20",
            "session": "arena/0f115b2d-prod3 (T-46)",
            "method": "fetch of the supplied link.amazon URL through a non-browser proxy; the final URL was read for an /dp/<ASIN>. No price, rating or offer text was recorded. The same day's official /dp/<ASIN> page was then fetched as a control.",
            "submitted_link": prod["submitted_link"],
            "final_url": rec["final_url"],
            "asin_in_final_url": rec["asin_in_final_url"],
            "matches_2026_11_19_observed_asin": False,
            "matches_first_2026_11_20_recheck": False,
            "result": "Ended at the Amazon.com homepage (https://www.amazon.com/); no /dp/ ASIN in the final URL. This reproduces the 2026-11-19 destination NOT being reached. The cause is not established: a fetch cannot distinguish a signed-out or profile-gated session, a transient response, and a link-level change. This is an observation, not a finding that the supplied link is invalid, expired or untracked.",
        }
        prod["listing_verified_2026_11_20"] = {
            "date": "2026-11-20",
            "session": "arena/0f115b2d-prod3 (T-46)",
            "method": "control fetch of the official listing URL, read for the page title and the category breadcrumb. Used to confirm the product itself is live and unchanged, independently of the short link.",
            "listing_url": rec["listing_url_checked"],
            "listing_title_read": rec["listing_title_read"],
            "breadcrumb_path_read": rec["breadcrumb_path_read"],
            "breadcrumb_node_read": rec["breadcrumb_node_read"],
            "matches_register_observed_title": True,
            "matches_register_browse_node": True,
            "note": "The title and the browse node read on 2026-11-20 match the register values for this product. The register's other specification values were transcribed from the 2026-11-19 snapshot and were not re-read field by field in this pass; FLG-007 and FLG-012 still apply.",
        }
    d["independent_recheck_note"] = (
        "Second, independent observation of the five supplied short links on 2026-11-20, plus a control "
        "fetch of each official listing. Kept beside the first same-day re-check; neither is overwritten. "
        "All five short links ended at the Amazon.com homepage in this pass while all five official "
        "/dp/<ASIN> pages rendered the correct product, including the register's title and browse node. "
        "Cause is not established and the supplied links are not declared invalid (see FLG-025)."
    )
    P.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print("wrote", P)


if __name__ == "__main__":
    main()
