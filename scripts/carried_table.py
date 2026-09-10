#!/usr/bin/env python
"""Build a step report's `Carried` table from the verdict's own headings.

WHY THIS IS A COMMITTED SCRIPT AND NOT A HABIT. A revision wrote statuses for a
block of findings without reading what each one said: six rows attached that
step's work to numbers naming different items, and four of eight blocking items
were recorded at step 4a. The next revision said the table "is generated from
the verdict" -- and no generator existed in the repository, so the sentence was
unverifiable and turned out to be wrong again in four rows.

The classification is READ, never remembered. Each finding heading carries its
own class:

    **R267. (BLOCKS -- head 3) ...        -> blocking
    **R276. (recordable, 4a) ...          -> 4a

`answered.json` supplies the text for items this round actually acted on; every
other row is generated from the class, so an item cannot be silently re-filed.

    python scripts/carried_table.py docs/reviews/F2/step-5.md answered.json

Prints the table on standard output. `tests/test_report_carried.py` then checks
what was committed: a blocking item may not carry a 4a status, every row must
use the report's vocabulary, and no row may use the verdict's.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^\*\*(R\d+)\.?\s*\(([^)]*)\)", re.MULTILINE)


def classify(verdict_text: str) -> dict[str, str]:
    """`{finding: 'blocking' | '4a'}` from the verdict's own headings."""
    return {
        m.group(1): ("blocking" if "block" in m.group(2).lower() else "4a")
        for m in HEADING.finditer(verdict_text)
    }


def rows(order: list[str], classes: dict[str, str], answered: dict[str, str]) -> list[str]:
    out = ["| item | status |", "|---|---|"]
    for item in order:
        if item in answered:
            status = answered[item]
        elif classes.get(item) == "4a":
            status = "**open** — recordable at 4a in the verdict's own classification"
        elif classes.get(item) == "blocking":
            status = "**open** — blocking, and not answered in this round"
        else:
            status = "**open** — carried from an earlier verdict"
        out.append(f"| {item} | {status} |")
    return out


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    verdict = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    answered = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    classes = classify(verdict)

    order = sorted(classes, key=lambda r: int(r[1:]))
    if len(argv) > 3:  # an explicit order, as the carry guard computes it
        order = Path(argv[3]).read_text(encoding="utf-8").split()

    print("\n".join(rows(order, classes, answered)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
