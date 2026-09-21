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

3. THE SUBJECT, WRITTEN INTO EVERY ROW (CH4). Each row carries what the verdict
   says that item IS, read out of the verdict and keyed by the number the row is
   written under. **THE SUBJECT CANNOT BE ATTACHED TO THE WRONG NUMBER** -- and
   that is the whole of the claim. The previous sentence said a rotation was
   impossible to write, and the reviewer rotated the `state` and `where` fields
   of three findings and printed all fifty-nine rows: what CH4 removed is the
   PROSE, and a state and a section number are still rotatable here.

   What catches that is one level up, in `tests/test_report_carried.py`: the
   section a row points at must exist in the report and must discuss that item.
   A rotated pointer then names a section that never mentions the number.

   The `site` check stays as the second half and its reach is small: it
   discriminates only where the declared site is unique to that finding's
   block, which was ONE row in eight this round, because
   `docs/reports/F2/step-5.md` is named in nearly every block. It was published
   as though it caught the shift outright, and it would not have.

   THE ANSWERS FILE IS POINTERS ONLY. A `state` from a fixed list and a `where`
   short enough to be a section number. Prose beside a number is what shifted,
   and there is nowhere left to write it.

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
            # OPTIONAL SINCE CH4. The subject beside every row is read out of
            # the verdict now, so a row cannot be attached to the wrong number
            # without saying so on the page; a declared site is a second,
            # weaker check and it is worth running when it is offered.
            continue
        block = by_block.get(item)
        if block is None:
            continue  # carried from an earlier verdict; it has no block here
        if site not in set(SITE.findall(block)):
            named = sorted(set(SITE.findall(block)))
            wrong.append(
                f"{item}: declares `{site}`, which its block does not name. It names {named}"
            )
    return wrong


# One newline, named, so this module's own source carries no escape
# that a generator has to get right twice.
NL = chr(10)

SUBJECT_CHARS = 96


def subject(item: str, verdict_text: str, by_block: dict[str, str]) -> str:
    """What the VERDICT says this item is, in the verdict's own words (CH4).

    This is the half that makes a rotation impossible rather than merely
    detectable. Three rows were once shifted by one -- R288 carrying R287's
    subject, R289 carrying R288's -- and the site check that followed
    discriminated only where a declared site was unique to its block, which
    was one row in eight. Here the subject is not declared at all: it is read
    out of the verdict, keyed by the number the row is written under, so a
    status attached to the wrong number carries that number's subject and
    contradicts itself on the page.
    """
    block = by_block.get(item)
    if block:
        after = block.split(")", 1)[-1]
    else:
        line = next(
            (
                ln
                for ln in _carried_section(verdict_text).splitlines()
                if re.search(rf"\b{item}\b", ln)
            ),
            "",
        )
        after = re.sub(rf"^.*?\b{item}\b\s*(--|-|:)?\s*", "", line)
        # A carry line often lists several numbers before saying anything --
        # "R225-R228, R232, R233 -- carried". Drop the rest of the list so the
        # subject starts where the sentence does.
        after = re.sub(r"^(,?\s*R\d+(\s*-+\s*R\d+)?)+\s*(--|-|:)?\s*", "", after)
    if not block and len(after.strip(" ,-:")) < 8:
        # THE STRIP ATE THE SENTENCE. A carry line that is mostly a list
        # of numbers leaves nothing after the last of them, and a row
        # whose subject is a comma says less than no subject at all.
        # These lines put their one clause after the final dash.
        after = line.rsplit("--", 1)[-1] if "--" in line else line
    text = re.sub(r"[`*]", "", after).replace("\n", " ")
    text = " ".join(text.split())
    if not text:
        return "carried, and the verdict says nothing further about it here"
    if len(text) > SUBJECT_CHARS:
        text = text[:SUBJECT_CHARS].rsplit(" ", 1)[0] + "..."
    return text


def rows(
    order: list[str],
    classes: dict[str, str],
    answered: dict[str, dict],
    verdict_text: str,
    by_block: dict[str, str],
) -> list[str]:
    """One row per item: what this round DID, then what the verdict SAID.

    The first half is a pointer the answers file supplies -- a section of the
    report, at most. The second half is generated. Neither is prose typed
    beside a number.
    """
    out = ["| item | status | the verdict's own subject |", "|---|---|---|"]
    for item in order:
        if item in answered:
            where = answered[item].get("where", "")
            state = answered[item].get("state", "answered")
            status = f"**{state}** — {where}" if where else f"**{state}**"
        elif classes.get(item) == "4a":
            status = "**open** — recordable at 4a in the verdict's own classification"
        elif classes.get(item) == "blocking":
            status = "**open** — blocking, and not answered in this round"
        else:
            status = "**open** — carried from an earlier verdict"
        out.append(f"| {item} | {status} | {subject(item, verdict_text, by_block)} |")
    return out


STATES = ("answered", "open", "withdrawn", "carried", "later")


def check_states(answered: dict[str, dict]) -> list[str]:
    """A pointer file may not carry prose, and may not carry a verdict's word.

    The whole point of CH4 is that the sentence beside an item is generated. A
    `state` outside this list, or a `where` long enough to be an argument, puts
    the prose back and the rotation with it.
    """
    bad = []
    for item, entry in answered.items():
        state = entry.get("state", "answered")
        if state not in STATES:
            bad.append(f"{item}: state {state!r} is not one of {list(STATES)}")
        where = entry.get("where", "")
        if len(where) > 40:
            bad.append(
                f"{item}: `where` is {len(where)} characters. It is a pointer "
                "-- a section of the report -- and not a place to write the "
                "status that this script exists to generate."
            )
    return bad


def table(verdict_text: str, answers: dict) -> str:
    answered = answers.get("answered", answers)
    classes = classify(verdict_text)
    by_block = blocks(verdict_text)
    wrong = check_states(answered) + check_sites(answered, by_block)
    if wrong:
        raise SystemExit(
            "the answers file cannot be used as written:" + NL + "  " + (NL + "  ").join(wrong)
        )
    return NL.join(rows(required(verdict_text), classes, answered, verdict_text, by_block))


GENERATED_MARK = "<!-- generated: scripts/carried_table.py -->"


def _mark(text: str) -> str:
    """CY3: the generated/hand-written split keys on this line."""
    return GENERATED_MARK + "\n\n" + text


def main(argv: list[str]) -> int:
    # The table carries em dashes and section marks. On a console whose
    # encoding is not UTF-8 those are replaced on the way out, and the
    # published table then differs from the generated one by exactly the
    # characters nobody looks at.
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) != 3:
        print(__doc__)
        return 2
    verdict = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    answers = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
    print(_mark(table(verdict, answers)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
