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
_ENTRY = re.compile(
    r"# CLASS:\s*(ACCURACY|STRUCTURAL)\b.*?^([A-Z][A-Z0-9_]*)\s*:\s*Final\[float\]",
    re.DOTALL | re.MULTILINE,
)


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


def test_every_float_tolerance_declares_a_class() -> None:
    """An unclassified entry escapes the rule by omission."""
    text = SOURCE.read_text(encoding="utf-8")
    body = text.split('"""', 2)[-1]
    declared = {
        m.group(1)
        for m in re.finditer(r"^([A-Z][A-Z0-9_]*)\s*:\s*Final\[float\]", body, re.M)
    }
    classified = {n for _, n in _classified()}
    # A _COUNTER or _MEASURED is documented by the entry it belongs to, not
    # separately -- both are satellites of a classified name.
    missing = {
        d for d in declared - classified
        if not d.endswith(("_COUNTER", "_MEASURED"))
    }
    assert not missing, f"tolerances without a CLASS declaration: {sorted(missing)}"


@pytest.mark.parametrize(
    "name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"]
)
def test_accuracy_tolerances_have_a_counter_case(name: str) -> None:
    assert name != "<none>", "no ACCURACY entries found"
    counter = f"{name}_COUNTER"
    assert hasattr(tolerances, counter), (
        f"{name} is an ACCURACY tolerance with no {counter}. The counter-case is "
        "the smallest defect the gate must still fail; without it the ceiling can "
        "be widened one order at a time and still look principled."
    )


@pytest.mark.parametrize(
    "name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"]
)
def test_the_ceiling_sits_below_its_counter_case(name: str) -> None:
    """Property 3: widening the ceiling toward the counter-case breaks this."""
    assert name != "<none>", "no ACCURACY entries found"
    ceiling = getattr(tolerances, name)
    counter = getattr(tolerances, f"{name}_COUNTER")
    assert ceiling < counter, (
        f"{name} = {ceiling:.3e} is not below its counter-case {counter:.3e}. The "
        "gate would pass a defect it is required to catch."
    )


@pytest.mark.parametrize(
    "name", [n for c, n in _classified() if c == "STRUCTURAL"] or ["<none>"]
)
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


@pytest.mark.parametrize(
    "name", [n for c, n in _classified() if c == "ACCURACY"] or ["<none>"]
)
def test_measured_below_ceiling_below_counter(name: str) -> None:
    """BD1: MEASURED < TOL < COUNTER, for every accuracy entry.

    The middle inequality is the counter-case rule. The left one is new: it
    records the worst value actually seen at the entry's sites, so an entry whose
    sites drift toward the ceiling fails rather than silently consuming headroom.

    It does NOT by itself catch a widening -- 1e-12 would satisfy it as happily
    as 1e-14 did. That is why BD0's rule exists: a commit message claiming "no
    value loosened" carries the check that says so.
    """
    assert name != "<none>", "no ACCURACY entries found"
    measured = getattr(tolerances, f"{name}_MEASURED", None)
    assert measured is not None, (
        f"{name} has no {name}_MEASURED. Every accuracy entry records the worst "
        "value actually measured at its sites."
    )
    ceiling = getattr(tolerances, name)
    counter = getattr(tolerances, f"{name}_COUNTER")
    assert measured < ceiling < counter, (
        f"{name}: measured {measured:.4e} < ceiling {ceiling:.4e} < counter "
        f"{counter:.4e} does not hold"
    )
