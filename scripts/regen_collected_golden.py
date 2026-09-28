#!/usr/bin/env python
"""The set of test FUNCTIONS this suite collects, as a golden file (CM1).

    python scripts/regen_collected_golden.py

WHY THIS EXISTS, and it should have existed from step 1. `CLAUDE.md` has said
since it was written that a test is never deleted to get a green build, and the
only thing enforcing it was a reviewer comparing collected counts by hand. At
the thirty-eighth verdict that is exactly what caught it: a rewrite spliced
from one function to the end of a file and took three green tests with it, and
the count moved from 88 to 85 with nothing else saying a word.

WHAT IS RECORDED. `module::function`, never the parametrised id. Parameter sets
are driven by the reviewer's corpora and by the report being written, so they
move every round by design; a function disappearing is the defect this file is
about, and it is stable.

THE RULE. `tests/goldens/collected_tests.txt` is a golden under `CLAUDE.md`
§ Testing:

  * a name that disappears is a FAILING BUILD, not a diff nobody reads;
  * removing a test means regenerating this file **in its own commit**, with
    the reason in the closure artifact -- the same discipline V6.1 applies to
    every other golden;
  * a rename is a removal plus an addition and gets the same treatment;
  * adding a test needs nothing: the check is one-directional, because a new
    test is not the failure mode.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLDEN = ROOT / "tests" / "goldens" / "collected_tests.txt"

# The collection roots, in the order the ladder runs them. A root that
# collects nothing is a finding rather than an empty section.
ROOTS = (
    "tests",
    "tests/unit",
    "tests/verification/rung1",
    "tests/verification/rung3",
    "tests/verification/rung4",
    "tests/regression",
)


def collected(root: str) -> set[str]:
    """`module::function` for every test collected under `root`."""
    out = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            root,
            "-q",
            "--collect-only",
            "--no-header",
            "-p",
            "no:randomly",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    names: set[str] = set()
    for line in out.stdout.splitlines():
        line = line.strip()
        if "::" not in line or line.startswith(("ERROR", "FAILED")):
            continue
        names.add(line.split("[", 1)[0].replace("\\", "/"))
    return names


def render() -> str:
    lines = [
        "# COLLECTED TEST FUNCTIONS -- GENERATED, do not edit (CM1).",
        "#",
        "# `python scripts/regen_collected_golden.py`. A name here that the suite",
        "# no longer collects is a FAILING BUILD: removing a test means",
        "# regenerating this file in its own commit with the reason in the",
        "# closure artifact, and a rename is a removal plus an addition.",
        "#",
        "# Parametrised ids are deliberately not recorded -- they move with the",
        "# reviewer's corpora and with the report being written. A FUNCTION",
        "# disappearing is what this file exists to catch.",
        "",
    ]
    for root in ROOTS:
        names = sorted(collected(root))
        lines.append(f"[{root}] {len(names)}")
        lines += names
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse(text: str) -> dict[str, set[str]]:
    """`{root: names}` from the golden's own format."""
    out: dict[str, set[str]] = {}
    root = ""
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("["):
            root = line[1 : line.index("]")]
            out[root] = set()
        elif root:
            out[root].add(line)
    return out


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    GOLDEN.parent.mkdir(parents=True, exist_ok=True)
    text = render()
    GOLDEN.write_text(text, encoding="utf-8")
    counts = {r: len(n) for r, n in parse(text).items()}
    print(f"wrote {GOLDEN.relative_to(ROOT)}")
    for root, n in counts.items():
        print(f"  {root:<28} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
