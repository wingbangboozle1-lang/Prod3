#!/usr/bin/env python3
"""Resolve the recurring T-27 integration conflicts generically."""
import json
import subprocess
from pathlib import Path


def show(ref, path):
    return subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout


def resolve_keep_both(path):
    p = Path(path)
    lines = p.read_text().splitlines(keepends=True)
    out, prev = [], 0
    changed = False
    while True:
        try:
            l = next(i for i, x in enumerate(lines[prev:], prev) if x.startswith("<<<<<<< "))
        except StopIteration:
            break
        e = next(i for i, x in enumerate(lines[l:], l) if x.strip() == "=======")
        g = next(i for i, x in enumerate(lines[e:], e) if x.startswith(">>>>>>> "))
        out.extend(lines[prev:l])
        out.extend(lines[l + 1 : e])
        out.extend(lines[e + 1 : g])
        prev = g + 1
        changed = True
    out.extend(lines[prev:])
    if changed:
        p.write_text("".join(out))
    return changed


def main():
    unmerged = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=U"], capture_output=True, text=True
    ).stdout.split()
    for f in unmerged:
        if f in ("COORDINATION.md", "DIRECTION.md", "docs/verification.md", "README.md"):
            resolve_keep_both(f)
        elif f == "direction.html":
            p = Path("direction.html")
            lines = p.read_text().splitlines(keepends=True)
            out, prev = [], 0
            while True:
                try:
                    l = next(i for i, x in enumerate(lines[prev:], prev) if x.startswith("<<<<<<< "))
                except StopIteration:
                    break
                e = next(i for i, x in enumerate(lines[l:], l) if x.strip() == "=======")
                g = next(i for i, x in enumerate(lines[e:], e) if x.startswith(">>>>>>> "))
                a, b = lines[l + 1 : e], lines[e + 1 : g]
                keep = a if any("58 registered suggestions" in x or "SG-01..SG-58" in x for x in a) else b
                out.extend(lines[prev:l]); out.extend(keep); prev = g + 1
            out.extend(lines[prev:])
            p.write_text("".join(out))
        elif f == "data/suggestions.json":
            theirs = show("origin/main", "data/suggestions.json")
            d = json.loads(theirs)
            d["premise"] = d["premise"].replace(
                "was cited by DIRECTION.md — FLG-021 — until",
                "was cited by DIRECTION.md — FLG-029 — until",
            ).replace("which resolves FLG-021's gap note", "which resolves FLG-029's gap note")
            if "retired in place" in d.get("integrity_note", ""):
                d["integrity_note"] = (
                    "2026-11-20: SG-21 was found byte-identical to SG-20 (a merge replay during PR #17 "
                    "clobbered SG-20's content). The interim retirement was withdrawn the same day when "
                    "SG-20's original content was recovered from PR #17 commit 7fbef67; SG-20 and SG-21 "
                    "are live and distinct again. The register keeps retired rows so an ID is never reused."
                )
            s26 = next(x for x in d["suggestions"] if x["id"] == "SG-26")
            if "FLG-029" not in s26["evidence"]:
                s26["evidence"] += " (This row fills the SG-26 slot that FLG-029 documented as a gap.)"
            s26["evidence"] = s26["evidence"].replace("FLG-021", "FLG-029")
            Path("data/suggestions.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
        else:
            # generated pages and anything else: keep our side, builders regenerate
            p = Path(f)
            lines = p.read_text().splitlines(keepends=True)
            out, prev = [], 0
            while True:
                try:
                    l = next(i for i, x in enumerate(lines[prev:], prev) if x.startswith("<<<<<<< "))
                except StopIteration:
                    break
                e = next(i for i, x in enumerate(lines[l:], l) if x.strip() == "=======")
                g = next(i for i, x in enumerate(lines[e:], e) if x.startswith(">>>>>>> "))
                out.extend(lines[prev:l]); out.extend(lines[l + 1 : e]); prev = g + 1
            out.extend(lines[prev:])
            p.write_text("".join(out))
        subprocess.run(["git", "add", f], check=True)
    print("resolved:", unmerged or "nothing")


if __name__ == "__main__":
    main()
