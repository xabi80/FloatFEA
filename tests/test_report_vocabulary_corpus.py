"""The vocabulary guard, run against the reviewer's spellings (R271, R297).

CC1 took the word `closed` away from a step report, and the argument for it was
that this "removes the failure mode instead of detecting it". That is a claim
about a detector, and a detector has a reach. The reviewer wrote
`tests/corpus/report_status_vocabulary.txt` to measure it and the file sat there
for three rounds with **no runner**: twenty-two spellings, most of them getting
the word past the guard, and nothing in the suite said so.

WHAT THIS FILE DOES. For each corpus entry it appends the row to a COPY of the
newest revision's `Carried` text, points the shipped guard at that copy, and
runs the three vocabulary tests exactly as they ship:

    refused   at least one of the three reports the row
    allowed   all three pass

and compares the outcome with the entry's `expect=`.

WHY IT REBINDS A MODULE GLOBAL RATHER THAN BUILDING A TREE. The three tests read
one name, `CARRIED`, and everything else they use -- the verdict, the finding
set -- must stay real for the third test to have a domain at all. Copying the
repository per entry would take twenty-two clones to measure a string function.
The thing under test is the parser and the word list, and both are reached here.

DISAGREEMENTS ARE DECLARED, NOT SKIPPED. Where the shipped guard does not do
what an entry requires, `DISAGREEMENTS` states what it does instead and why,
and the test asserts THAT. A corpus entry is the reviewer's requirement, not a
proof that the requirement is right; but an entry silently unmet is exactly the
state this file exists to end, so the reason is written beside it and any drift
from the declared outcome is red.

THE CORPUS IS THE REVIEWER'S. The implementer writes the runner, never the
cases it is scored against.
"""

from __future__ import annotations

import contextlib
import re
from pathlib import Path

import pytest

import tests.test_report_carried as guard

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "tests" / "corpus" / "report_status_vocabulary.txt"

# The three tests the corpus header names. Run in this order; the first to
# report decides, and which one reported is part of the message.
CHECKS = (
    "test_a_report_does_not_say_CLOSED",
    "test_no_status_cell_carries_a_letter_that_is_not_ASCII",
    "test_the_Carried_section_is_markdown_rows_and_not_HTML",
    "test_every_carried_item_carries_one_of_the_report_words",
    "test_no_status_claims_more_than_the_verdict_allows",
)


class _Capsys:
    """`test_a_report_does_not_say_CLOSED` prints its census through capsys."""

    disabled = staticmethod(contextlib.nullcontext)


def _entries() -> list[tuple[str, str, str]]:
    """`(id, expect, row)` for every entry, in file order."""
    out: list[tuple[str, str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        m = re.match(r"id=(\S+)\s+expect=(\S+)\s+.*?\brow=(.*)$", line)
        if m:
            out.append((m.group(1), m.group(2), m.group(3)))
    return out


ENTRIES = _entries()

# What the shipped guard does where it does not do what the entry requires,
# with the reason it is the right answer. Each value is
# `(outcome, why)` and the outcome is asserted, so a repair that changes the
# behaviour makes this file red rather than quietly agreeing.
DISAGREEMENTS: dict[str, tuple[str, str]] = {}


def _carried_for(row: str) -> str:
    """The newest revision's Carried text with this entry's row in it.

    An entry whose `row=` is not a table row describes a mutation of the
    section itself rather than an addition to it; the one such entry renames
    the heading away, and the guard then parses no section at all.
    """
    if not row.lstrip().startswith("|"):
        return ""
    return guard.CARRIED.rstrip() + "\n" + row + "\n"


def _outcome(row: str) -> tuple[str, str]:
    """`('refused'|'allowed', which check reported)` for one row."""
    original = guard.CARRIED
    guard.CARRIED = _carried_for(row)
    try:
        for name in CHECKS:
            fn = getattr(guard, name)
            try:
                fn(_Capsys()) if name == CHECKS[0] else fn()
            except AssertionError:
                return "refused", name
        return "allowed", ""
    finally:
        guard.CARRIED = original


def test_the_corpus_was_parsed() -> None:
    """A runner that reads nothing agrees with everything."""
    assert len(ENTRIES) >= 20, (
        f"{len(ENTRIES)} entries parsed from {CORPUS.name}. The file carries "
        "twenty-two; a parse that loses them is a scan of nothing."
    )
    assert {e[1] for e in ENTRIES} >= {"refused", "allowed"}, (
        "the corpus parsed with no `allowed` entry. A vocabulary that refuses "
        "everything is not usable, and that is the worse failure."
    )


_NOTHING = ("(no entry parsed)", "allowed", "| R1 | open |")


@pytest.mark.parametrize(
    "name, expect, row",
    ENTRIES or [_NOTHING],
    ids=[e[0] for e in ENTRIES] or [_NOTHING[0]],
)
def test_the_guard_rules_on_the_spelling(name: str, expect: str, row: str) -> None:
    got, reporter = _outcome(row)
    if name in DISAGREEMENTS:
        declared, why = DISAGREEMENTS[name]
        assert got == declared, (
            f"{name}: the shipped guard is declared to answer `{declared}` here "
            f"and it answered `{got}`. Either the repair moved or the "
            f"declaration is stale.\n  declared because: {why}"
        )
        return
    assert got == expect, (
        f"{name}: the corpus requires `{expect}` and the shipped guard says "
        f"`{got}`" + (f", reported by {reporter}" if reporter else "") + f".\n  row: {row}\n"
        "Either the guard is repaired so the row is ruled on, or the "
        "disagreement is declared in DISAGREEMENTS with the reason."
    )
