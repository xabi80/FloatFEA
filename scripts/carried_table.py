#!/usr/bin/env python
"""Build a step report's `Carried` table from the verdict's own headings.

    python scripts/carried_table.py docs/reviews/F2/step-5.md \\
                                    docs/reports/F2/step-5-answers.json

WHY THIS IS A COMMITTED SCRIPT AND NOT A HABIT. A revision wrote statuses for a
block of findings without reading what each one said: six rows attached that
step's work to numbers naming different items, and four of eight blocking items
were recorded at step 4a. The next revision said the table "is generated from
the verdict" -- and no generator existed, so the sentence was unverifiable and
turned out to be wrong again in four rows. The round after that, the generator
existed and was right about class, and three hand-written rows were shifted by
one: R288 carried R287's subject, R289 carried R288's, and R290 -- the item that
had then gone unanswered for three rounds -- fell off the end of the shift.

THREE THINGS ARE READ AND NEVER REMEMBERED.

1. THE ROW SET. Every `R<n>` the verdict declares as a finding, plus every one
   its own `Carried` section mentions, in numeric order. This is the same rule
   `tests/test_report_carried.py` uses to decide what the report must carry, so
   the generated table cannot be short of what the guard demands.

2. THE CLASS, from each finding's own heading:

       **R267. (BLOCKS -- head 3) ...        -> blocking
       **R276. (recordable, 4a) ...          -> 4a

   An unanswered item is filed by its class, so it cannot be quietly re-filed.

3. THE SUBJECT. Every answered row declares a `site` -- a path the verdict names
   INSIDE that finding's own block -- and the generator refuses to print a table
   whose row cites a site the finding does not name. That is the mechanical half
   of the shift: a status written under the wrong number is a status whose site
   belongs to a different block, and three of three would have been caught.

The answers file is committed beside the report, so the command above runs at
the commit that publishes the table. `tests/test_report_carried.py` then re-runs
it and compares the output with what was committed, so a table that stops
matching its generator is red.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^\*\*(R\d+)\.?\s*\(([^)]*)\)", re.MULTILINE)
FINDING = re.compile(r"^\*\*(R\d+)[.\s]", re.MULTILINE)
MENTION = re.compile(r"\bR\d+\b")
SITE = re.compile(r"((?:\.?[\w.-]+/)*[\w.-]+\.(?:py|md|sh|txt|json|yml))")


def classify(verdict_text: str) -> dict[str, str]:
    """`{finding: 'blocking' | '4a'}` from the verdict's own headings."""
    return {
        m.group(1): ("blocking" if "block" in m.group(2).lower() else "4a")
        for m in HEADING.finditer(verdict_text)
    }


def _carried_section(text: str) -> str:
    heads = list(re.finditer(r"^##+ .*Carried.*$", text, re.MULTILINE))
    if not heads:
        return ""
    start = heads[-1].end()
    nxt = re.search(r"^##+ ", text[start:], re.MULTILINE)
    return text[start : start + nxt.start()] if nxt else text[start:]


def required(verdict_text: str) -> list[str]:
    """Exactly the set `tests/test_report_carried.py` requires, in its order."""
    items = set(FINDING.findall(verdict_text)) | set(
        MENTION.findall(_carried_section(verdict_text))
    )
    return sorted(items, key=lambda r: int(r[1:]))


def blocks(verdict_text: str) -> dict[str, str]:
    """`{finding: the text of its own block}`, heading to next heading."""
    out: dict[str, str] = {}
    marks = list(HEADING.finditer(verdict_text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(verdict_text)
        out[m.group(1)] = verdict_text[m.start() : end]
    return out


def check_sites(answered: dict[str, dict], by_block: dict[str, str]) -> list[str]:
    """Rows whose declared site is not named by that finding (the shift)."""
    wrong = []
    for item, entry in answered.items():
        site = entry.get("site", "")
        if not site:
            wrong.append(f"{item}: no `site` declared")
            continue
        block = by_block.get(item)
        if block is None:
            continue  # carried from an earlier verdict; it has no block here
        if site not in set(SITE.findall(block)):
            named = sorted(set(SITE.findall(block)))
            wrong.append(f"{item}: declares `{site}`, which its block does not name. It names {named}")
    return wrong


def rows(order: list[str], classes: dict[str, str], answered: dict[str, dict]) -> list[str]:
    out = ["| item | status |", "|---|---|"]
    for item in order:
        if item in answered:
            status = answered[item]["status"]
        elif classes.get(item) == "4a":
            status = "**open** — recordable at 4a in the verdict's own classification"
        elif classes.get(item) == "blocking":
            status = "**open** — blocking, and not answered in this round"
        else:
            status = "**open** — carried from an earlier verdict"
        out.append(f"| {item} | {status} |")
    return out


def table(verdict_text: str, answers: dict) -> str:
    answered = answers.get("answered", answers)
    classes = classify(verdict_text)
    wrong = check_sites(answered, blocks(verdict_text))
    if wrong:
        raise SystemExit(
            "the answers file attaches a row to a finding that does not name "
            "its site:\n  " + "\n  ".join(wrong)
        )
    return "\n".join(rows(required(verdict_text), classes, answered))


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    verdict = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    answers = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    print(table(verdict, answers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
