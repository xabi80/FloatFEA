"""EY2: no name in `floatfea/tolerances.py` is assigned more than once.

**THE ONLY DR1 EXCEPTION, GRANTED BY EY2.** `CLAUDE.md` forbids new apparatus through F6 --
no new guards, scanners, meta-tests, detectors or report generators -- and this is a
meta-test. It exists because of one defect and the four-way blindness around it.

WHAT HAPPENED. Repairing R722 I replaced the span from the force channel's comment to the
next `# CLASS:` comment, and the decomposition entry had been inserted BETWEEN the force
ceiling and its counter. So the old counter survived below the new one and
`floatfea/tolerances.py` held:

    F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 3.0e-8      (the repair)
    ...
    F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 0.1         (the value being repaired)

Python takes the later binding, so the gate ran against `0.1` -- the number R722 was
raised about, 2.95e+06 times above a defect the same gate asserts it must fail.

WHAT SAW IT: nothing. `ruff check`, `black --check`, `mypy floatfea` ("Success: no issues
found in 36 source files" WITH the duplicate present -- **mypy does not flag a redefined
`Final`**), a green suite, and a green CI run at the commit's own sha. I found it by
printing the value back instead of trusting the edit. That is the same four-way blindness
EQ0 was written about, and it is the one failure mode of the seven findings in that round
that no guard could have caught.

WHY A META-TEST AND NOT A TEST. The subject is not a quantity the model computes; it is the
SHAPE of the file every quantity is declared in. There is nothing to measure and no
counter-case in the physical sense -- so the counter-case below plants a duplicate in a
copy of the file and requires the parser to find it, which is the only form the obligation
can take here (R430: a guard that cannot be shown to fail is the thing this repository
keeps rediscovering).

WHAT IT DOES NOT DO. It reads assignment TARGETS and nothing else: it says nothing about
values, classes, counters, plan rows or ordering. Those have their own guards in
`tests/verification/rung3/test_tolerance_counter_cases.py` and
`tests/test_plan_matches_tolerances.py`. A duplicate is the whole of its reach, stated so
that nobody reads it as a general check on this file.
"""

from __future__ import annotations

import ast
import collections
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TOLERANCES = ROOT / "floatfea" / "tolerances.py"


def assigned_names(source: str) -> list[str]:
    """Every module-level assignment target in `source`, in order, with repeats kept.

    A FUNCTION rather than a loop inside the test, so the counter-case below can run it on
    text that is not the shipped file.

    MODULE LEVEL ONLY, and `ast` rather than a regex. A regex over `^NAME` would also catch
    a name inside a docstring, a comment or a nested scope -- and this file is almost
    entirely prose, so a false positive would be the likely outcome rather than the rare
    one. Annotated assignments (`X: Final[float] = ...`) are the form every entry uses, so
    both `Assign` and `AnnAssign` are read.
    """
    out: list[str] = []

    def names_in(target: ast.expr) -> None:
        # TUPLE AND LIST TARGETS TOO. The first version of this read only `ast.Name`, so
        # `X, Y = 1.0, 2.0` bound nothing as far as it was concerned -- and the
        # parametrised row written to be adversarial about exactly that is what caught it.
        # No entry in `tolerances.py` is written that way today, which is the reason the
        # omission would have sat there unnoticed.
        if isinstance(target, ast.Name):
            out.append(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for element in target.elts:
                names_in(element)

    for node in ast.parse(source).body:
        if isinstance(node, ast.AnnAssign):
            names_in(node.target)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                names_in(target)
    return out


def duplicates(source: str) -> dict[str, int]:
    """`{name: count}` for every module-level name assigned more than once."""
    counted = collections.Counter(assigned_names(source))
    return {name: n for name, n in sorted(counted.items()) if n > 1}


def test_no_name_in_tolerances_is_assigned_twice() -> None:
    """EY2. A duplicate means the later binding wins and the earlier one is a comment."""
    found = duplicates(TOLERANCES.read_text(encoding="utf-8"))
    assert not found, (
        f"{TOLERANCES.name} assigns these names more than once: {found}. Python takes the "
        "LATER binding, so the earlier declaration -- and the entry above it explaining "
        "why that value is what it is -- is dead prose, and every gate reading the name "
        "runs against a value nobody chose. This is R722's repair shipping the number it "
        "repaired: `F4_G41_DYNAMIC_FORCE_COUNTER` was declared at both `3.0e-8` and `0.1`, "
        "and `ruff`, `black`, `mypy` and a green CI all passed."
    )


def test_the_parser_FINDS_a_planted_duplicate() -> None:
    """The counter-case. R430: a guard that cannot be shown to fail certifies nothing.

    The duplicate is planted in a COPY of the shipped file, so the check runs against the
    real thing it will face -- thousands of lines of prose, `Final` annotations, comments
    containing the same names -- and not against a toy three-line sample that would pass a
    regex this file's own history shows a regex cannot handle.
    """
    source = TOLERANCES.read_text(encoding="utf-8")
    assert not duplicates(source), "the shipped file must be clean for this to mean anything"

    name = next(n for n in assigned_names(source) if n.startswith("F4_"))
    planted = source + f"\n\n{name}: Final[float] = 1.0\n"
    found = duplicates(planted)
    assert found == {name: 2}, (
        f"a planted second binding of {name} was not found: {found}. The parser does not "
        "see the shape it exists for."
    )


@pytest.mark.parametrize(
    "snippet, expected",
    [
        # Each of these is a shape the regex this replaces would have got wrong.
        ('X: Final[float] = 1.0\n"""X: Final[float] = 2.0"""\n', {}),
        ("X: Final[float] = 1.0\n# X: Final[float] = 2.0\n", {}),
        ("def f():\n    X = 2.0\n\nX: Final[float] = 1.0\n", {}),
        ("X: Final[float] = 1.0\nX: Final[float] = 2.0\n", {"X": 2}),
        ("X = 1.0\nX: Final[float] = 2.0\n", {"X": 2}),
        ("X, Y = 1.0, 2.0\nX: Final[float] = 3.0\n", {"X": 2}),
    ],
)
def test_the_parser_separates_a_BINDING_from_a_MENTION(snippet: str, expected: dict) -> None:
    """A name in a docstring, a comment or a nested scope is not a second binding.

    This file is mostly prose and its entries quote their own constants' names in the
    paragraphs explaining them, so "a name appearing twice" and "a name BOUND twice" are
    very different counts here. `ast` is why the difference is reliable; these rows are why
    the claim is checkable.
    """
    assert duplicates(snippet) == expected
