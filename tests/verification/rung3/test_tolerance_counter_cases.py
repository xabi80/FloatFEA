"""Every ACCURACY tolerance carries a paired counter-case value (AO1/AO2).

The rule
--------
An accuracy tolerance is a ceiling on something supposed to be small, and it is
what "the test fails, widen the tolerance" reaches for. Each one carries

    X          the ceiling the check asserts
    X_COUNTER  the smallest defect that must still fail

Three properties, and the third is the one that matters:

1. **Existence is mechanically checkable** — asserted here.
2. **It cannot be satisfied by prose**, because `X_COUNTER` is a number an
   executable test consumes. A comment-parsing rule would be satisfied by writing
   the right-shaped sentence, which certifies that prose exists.
3. **Widening `X` toward `X_COUNTER` eventually breaks a test** — asserted here as
   `X < X_COUNTER`, and separately in each gate's own counter-test, which measures
   that a real defect of that magnitude exceeds the ceiling.

Binds on ACCURACY only. A STRUCTURAL tolerance is a threshold on a condition and
fires by design — `MEMBER_ORIENTATION_DEGENERACY` fires on the platform's vertical
spars on purpose. Demanding a counter-case there would force an artificial number,
and a rule applied where it does not fit gets weakened to accommodate.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from floatfea import tolerances

SOURCE = Path(tolerances.__file__)
_DECL = r"^[A-Z][A-Z0-9_]*\s*:\s*Final\["
# THE MATCH TERMINATES AT THE NEXT DECLARATION OF ANY TYPE (R1108). It used to be
# `# CLASS:...(ACCURACY|STRUCTURAL).*?^NAME: Final[float]` with DOTALL, and a lazy
# `.*?` crosses anything -- so a recognised class on a NON-float constant did not
# terminate at that constant. The match ran on and attached the label to the next
# `Final[float]` entry, whatever that entry's own comment said.
#
# Measured, with `# CLASS: STRUCTURAL` restored above `NODE_COINCIDENCE_DECIMALS`
# (a `Final[int]`): the old form reported `RECORDED_HEIGHT_PAIR_RELATIVE` as
# STRUCTURAL where its own nearest CLASS line says ACCURACY, and STRUCTURAL
# FORBIDS a counter while that entry has one -- so the obligation failed on the
# wrong entry, silently. On the clean tree both forms classify the same 55
# entries with identical labels, so this is a repair and not a change of rule.
#
# The tempered `(?:(?!_DECL).)*?` is what forbids the crossing: at every position
# the lookahead refuses to step over the start of any `NAME: Final[...]` line.
_ENTRY = re.compile(
    r"# CLASS:\s*(ACCURACY|STRUCTURAL)\b"
    r"(?:(?!" + _DECL + r").)*?"
    r"^([A-Z][A-Z0-9_]*)\s*:\s*Final\[float\]",
    re.DOTALL | re.MULTILINE,
)
_CLASS_LINE = re.compile(r"^# CLASS:\s*(?:ACCURACY|STRUCTURAL)\b", re.MULTILINE)


def _classified() -> list[tuple[str, str]]:
    """(class, name) for every entry declaring a CLASS, nearest-comment-first."""
    text = SOURCE.read_text(encoding="utf-8")
    # Cut the module docstring: it discusses CLASS without declaring entries.
    body = text.split('"""', 2)[-1]
    return [(m.group(1), m.group(2)) for m in _ENTRY.finditer(body)]


def test_there_are_classified_entries_to_check() -> None:
    """Meta-test: an empty match set makes every assertion below vacuous."""
    found = _classified()
    assert found, "no CLASS-tagged entries parsed -- the regex or the file changed"
    assert any(c == "ACCURACY" for c, _ in found), "no ACCURACY entries to check"
    assert any(c == "STRUCTURAL" for c, _ in found), "no STRUCTURAL entries"


def test_R1108_every_CLASS_line_CLASSIFIES_an_entry_so_none_is_ORPHANED() -> None:
    """A `# CLASS:` line that classifies nothing is the silent half of R1108.

    The regex repair above stops a label TRANSFERRING to an entry that did not
    declare it. It cannot say that the label went nowhere, and a class nobody
    reads is an obligation nobody checks -- a `# CLASS: ACCURACY` whose entry the
    regex never reaches carries no counter requirement at all.

    This is the cell that is RED under the armed state R1108 was found with.
    Measured both ways, one variable moved -- `# CLASS: STRUCTURAL` restored
    above `NODE_COINCIDENCE_DECIMALS`, a `Final[int]`:

        clean:  CLASS lines 55, classified 55, orphaned 0
        armed:  CLASS lines 56, classified 55, orphaned 1

    So it fires on exactly the edit that reintroduces the defect, and the clean
    tree gives it nothing to report. Keyed on the COUNT rather than on a name,
    because the next orphan will be above some other constant.
    """
    body = SOURCE.read_text(encoding="utf-8").split('"""', 2)[-1]
    declared = len(_CLASS_LINE.findall(body))
    classified = len(_classified())
    assert declared == classified, (
        f"{declared - classified} `# CLASS:` line(s) classify no entry. A class "
        f"label that reaches no `Final[float]` declaration is an obligation that "
        f"is never checked, and before R1108 the label was instead TRANSFERRED to "
        f"the next float entry. Put the class on the entry it describes, or state "
        f"the reason in prose and remove the CLASS line."
    )


def test_every_float_tolerance_declares_a_class() -> None:
    """An unclassified entry escapes the rule by omission."""
    text = SOURCE.read_text(encoding="utf-8")
    body = text.split('"""', 2)[-1]
    declared = {
        m.group(1) for m in re.finditer(r"^([A-Z][A-Z0-9_]*)\s*:\s*Final\[float\]", body, re.M)
    }
    classified = {n for _, n in _classified()}
    # A _COUNTER or _COUNTER_DEFECT is documented by the entry it belongs to.
    missing = {d for d in declared - classified if not d.endswith(("_COUNTER", "_COUNTER_DEFECT"))}
    assert not missing, f"tolerances without a CLASS declaration: {sorted(missing)}"


@pytest.mark.parametrize("name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"])
def test_accuracy_tolerances_have_a_counter_case(name: str) -> None:
    assert name != "<none>", "no ACCURACY entries found"
    if hasattr(tolerances, f"{name}_COUNTER_DEFECT"):
        return  # the defect-size kind; its obligations are the two tests below
    counter = f"{name}_COUNTER"
    assert hasattr(tolerances, counter), (
        f"{name} is an ACCURACY tolerance with no {counter}. The counter-case is "
        "the smallest defect the gate must still fail; without it the ceiling can "
        "be widened one order at a time and still look principled."
    )


@pytest.mark.parametrize("name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"])
def test_the_ceiling_sits_below_its_counter_case(name: str) -> None:
    """Property 3: widening the ceiling toward the counter-case breaks this."""
    assert name != "<none>", "no ACCURACY entries found"
    if hasattr(tolerances, f"{name}_COUNTER_DEFECT"):
        # A defect SIZE is not in the ceiling's quantity, so no ordering between
        # them exists to assert. Applying the rule here anyway would force an
        # artificial number, which is how a rule gets weakened to accommodate the
        # cases it was never for (AO2).
        return
    ceiling = getattr(tolerances, name)
    counter = getattr(tolerances, f"{name}_COUNTER")
    assert ceiling < counter, (
        f"{name} = {ceiling:.3e} is not below its counter-case {counter:.3e}. The "
        "gate would pass a defect it is required to catch."
    )


@pytest.mark.parametrize("name", [n for c, n in _classified() if c == "STRUCTURAL"] or ["<none>"])
def test_structural_tolerances_do_NOT_carry_a_counter_case(name: str) -> None:
    """The rule must not spread to where it does not fit (AO2).

    A structural threshold fires by design; an invented counter-case for one would
    be an artificial number, and it is how a rule gets weakened to accommodate the
    cases it was never for.
    """
    assert name != "<none>", "no STRUCTURAL entries found"
    assert not hasattr(tolerances, f"{name}_COUNTER"), (
        f"{name} is STRUCTURAL but carries a counter-case. Either it is really an "
        "ACCURACY tolerance and the CLASS is wrong, or the counter-case is invented."
    )


def test_no_entry_carries_a_hand_written_MEASURED_value() -> None:
    """BE2: a measured value does not live in the file that declares the ceiling.

    `X_MEASURED` was added in BD1 and removed here. The assertion it powered --
    ``MEASURED < TOL < COUNTER`` -- compared three literals from one file, so it
    was satisfied by whatever the author typed: four of nine were wrong when
    written, two of those measured on a solve path deleted one commit later, and
    the suite stayed green throughout.

    The worst measured value is reported by the run that measures it, in
    `docs/reports/F<n>/step-<k>.md`. This test keeps the shape from coming back.
    """
    reintroduced = [n for n in dir(tolerances) if n.endswith("_MEASURED")]
    assert not reintroduced, (
        f"{sorted(reintroduced)} declare a measurement in the file that declares "
        "the ceiling. A check cannot take its own subject from its own source; "
        "put the number in the step report, where a run produces it."
    )


@pytest.mark.parametrize("name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"])
def test_every_accuracy_entry_has_a_counter_that_something_INJECTS(name: str) -> None:
    """BG1: a counter that nothing injects is a number, not a check.

    `RESULTANT_EXACTNESS` shipped with `ceiling < counter` as its only guard --
    a comparison between two literals in `tolerances.py` -- and could be widened
    from 1e-9 to 1e-7 with the whole suite still green. The obligation is that
    some test under `tests/` NAMES the counter, which is the cheapest mechanical
    proxy for "injects it": a counter no test mentions cannot be being injected.

    It does not prove the naming test perturbs anything. That is the limitation,
    and it is why the per-entry mutation tests exist beside it rather than this
    standing in for them.
    """
    assert name != "<none>", "no ACCURACY entries found"
    counters = [c for c in (f"{name}_COUNTER", f"{name}_COUNTER_DEFECT") if hasattr(tolerances, c)]
    assert counters, f"{name} has neither a _COUNTER nor a _COUNTER_DEFECT"

    root = Path(__file__).resolve().parents[3]
    users: list[str] = []
    for f in sorted(root.glob("tests/**/*.py")):
        if f.name == Path(__file__).name:
            continue
        text = f.read_text(encoding="utf-8")
        if any(c in text for c in counters):
            users.append(str(f.relative_to(root)))
    assert users, (
        f"{name}'s counter ({', '.join(counters)}) is named by no test under "
        "tests/. It is a literal sitting beside another literal, and the ceiling "
        "above it can be widened until something else notices."
    )
