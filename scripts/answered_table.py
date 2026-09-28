#!/usr/bin/env python
"""The findings this round answered, generated from the answers file (CY4).

    python scripts/answered_table.py <verdict> <answers.json>

WHY THIS EXISTS. The fifty-first verdict measured the report: six generated
sections carried no finding, and three of the seven hand-written ones did.
Every one of the three was fixed by re-running a command the repository
already had -- a commit list not re-run after the history moved, a figure no
command produced, two sentences a redefined glob left behind. So the
hand-written surface shrinks to one paragraph of reading, and the rest of the
report is generated.

This is the section that used to be seven hand-written ones: what each
finding was, what state it is in, and where the answer lives. The SUBJECT
comes from the verdict, the STATE and the POINTER from the answers file, and
neither is retyped here -- which is `carried_table.py`'s rule applied to the
other half of the same data.

WHAT IT DOES NOT DO. It cannot say whether an answer is right. A row reading
`answered - 3` means the implementer claims section 3 answers it; the
verdict's own `Closed when` is what decides, and that is the reviewer's.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GENERATED_MARK = "<!-- generated: scripts/answered_table.py -->"

_FINDING = re.compile(r"^\*\*(R\d+)\.\s*(?:\(([^)]*)\))?\s*(.*)$", re.MULTILINE)


def _subjects(verdict: str) -> dict[str, tuple[str, str]]:
    """`{item: (class, subject)}` read from the verdict, never retyped."""
    out: dict[str, tuple[str, str]] = {}
    for m in _FINDING.finditer(verdict):
        item, klass, rest = m.group(1), (m.group(2) or "").strip(), m.group(3).strip()
        kind = "blocks" if klass.lower().startswith("blocks") else "recorded"
        subject = re.sub(r"\s+", " ", rest).strip(" -*")
        out[item] = (kind, subject[:96])
    return out


def table(verdict_path: str, answers_path: str) -> str:
    verdict = Path(verdict_path).read_text(encoding="utf-8", errors="replace")
    answered = json.loads(Path(answers_path).read_text(encoding="utf-8"))["answered"]
    subjects = _subjects(verdict)
    rows = [
        GENERATED_MARK,
        "",
        "| item | class | state | where | site | the verdict's own subject |",
        "|---|---|---|---|---|---|",
    ]
    # EVERY ITEM IN THE ANSWERS FILE, not only this verdict's findings. A
    # carried item needs a section that says something about it, and
    # `test_a_carried_row_points_at_a_section_that_discusses_it` refuses the
    # Carried table for that -- every item is in THAT one by construction, so
    # the pointer resolves whatever it says. This table is the answers file's
    # own view: state, where the repair is, and the verdict's subject where
    # the verdict has one.
    for item in sorted(set(subjects) | set(answered), key=lambda k: int(k[1:])):
        kind, subject = subjects.get(item, ("carried", "carried from an earlier verdict"))
        entry = answered.get(item, {})
        state = entry.get("state", "NOT ANSWERED")
        where = entry.get("where", "")
        site = entry.get("site", "")
        rows.append(f"| {item} | {kind} | **{state}** | {where} | `{site}` | {subject} |")
    missing = sorted(set(subjects) - set(answered), key=lambda k: int(k[1:]))
    if missing:
        rows += ["", f"**{len(missing)} finding(s) with no row in the answers file: {missing}.**"]
    return "\n".join(rows) + "\n"


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) != 3:
        print(__doc__)
        return 2
    sys.stdout.write(table(argv[1], argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
