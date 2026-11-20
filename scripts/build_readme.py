#!/usr/bin/env python3
"""Generate the README register table from the data registers.

Why this exists
---------------
The README carried two register tables whose ID ranges contradicted each other,
then one table with hard-coded ranges. Both went stale the moment another session
added rows, and the counts a reader saw disagreed with the pages they linked to.

A gate rule caught the drift -- and then blocked main's deploy, because the fix it
demanded was a hand edit to a file no builder owned. The rule was right about the
defect and wrong about the remedy. The table is now generated from `data/*.json`,
so it cannot go stale, and the gate only has to prove the block matches its data.

Usage:
  python3 scripts/build_readme.py           # rewrite the block
  python3 scripts/build_readme.py --check   # exit 1 when the README is stale
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START = "<!-- build-registers-table:start -->"
END = "<!-- build-registers-table:end -->"


def load(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def nums(rows):
    return sorted(int(r["id"].split("-")[1]) for r in rows)


def build_table():
    sg = load("suggestions.json")["suggestions"]
    q = load("open-questions.json")["questions"]
    dt = load("decisions.json")["decisions"]
    flags = load("flagged.json")["items"]
    plan = load("editorial-plan.json")
    cites = load("citations.json")["citations"]

    sg_n, q_n, dt_n = nums(sg), nums(q), nums(dt)
    flag_n = nums([f for f in flags if f["id"].startswith("FLG")])
    plan_rows = plan.get("proposals", []) or plan.get("rows", [])

    def gaps(ns):
        return sorted(set(range(1, max(ns) + 1)) - set(ns))

    sg_note = ""
    if "SG-21" in [r["id"] for r in sg if r.get("status") == "retired"]:
        sg_note = " (SG-21 retired in place)"
    miss = gaps(sg_n)
    if miss:
        sg_note += "; unoccupied: " + ", ".join("SG-%02d" % n for n in miss) + " (see FLG-029)"

    rows = [
        ("Suggestions", "`suggestions.html`", "`data/suggestions.json`",
         "SG-01..SG-%02d%s" % (max(sg_n), sg_note), "%d rows" % len(sg)),
        ("Open questions", "`questions.html`", "`data/open-questions.json`",
         "Q-01..Q-%02d" % max(q_n), str(len(q))),
        ("Decisions to make", "`decisions.html`", "`data/decisions.json`",
         "DT-01..DT-%02d" % max(dt_n), str(len(dt))),
        ("Decisions taken", "`direction.html`", "`DIRECTION.md`", "dated rows", "-"),
        ("Publishing plan", "`publishing-plan.html`", "`data/editorial-plan.json`",
         "dated proposals", str(len(plan_rows))),
        ("Flagged findings", "`flagged.html`", "`data/flagged.json` + callouts",
         "FLG-%03d..FLG-%03d, F-01..F-21" % (min(flag_n), max(flag_n)),
         "%d in the data file" % len(flags)),
        ("Citation log", "`citations.html`", "`data/citations.json`",
         "claim-to-source rows", str(len(cites))),
    ]

    lines = ["| Register | Page | Data | IDs | Count |", "|---|---|---|---|---|"]
    lines += ["| %s | %s | %s | %s | %s |" % r for r in rows]
    return "\n".join(lines)


def render(doc):
    i = doc.index(START) + len(START)
    j = doc.index(END)
    return doc[:i] + "\n" + build_table() + "\n" + doc[j:]


def main():
    doc = README.read_text(encoding="utf-8")
    if "--check" in sys.argv:
        if render(doc) != doc:
            print("FAIL: README register table is out of date. Run python3 scripts/build_readme.py")
            return 1
        print("OK: README register table matches data/*.json")
        return 0
    README.write_text(render(doc), encoding="utf-8")
    print("wrote README register table")
    return 0


if __name__ == "__main__":
    sys.exit(main())
