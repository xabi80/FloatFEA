"""A test that disappears fails the build (CM1, R333).

`CLAUDE.md` has said since it was written that a test is never deleted to get a
green build. Nothing enforced it. What enforced it in practice was a reviewer
comparing collected counts between rounds by hand, and at the thirty-eighth
verdict that is what caught the failure this file exists to prevent: a rewrite
spliced from one function to the end of a module and took three green tests
with it. The rung went from 88 collected to 85, every remaining test passed,
and the same module still cited one of the deleted tests as the justification
for a change made in the same commit.

**This is the eighth guard aimed at the suite's own extent** -- the others ask
whether CI runs what exists, whether a corpus has a runner, whether a rung
collects anything. None of them could see a test that simply stopped existing,
because every one of them measures what IS there.

WHAT IT CHECKS. `tests/goldens/collected_tests.txt` lists `module::function`
per collection root. Every name in it must still be collected. It is
ONE-DIRECTIONAL on purpose: a new test is not the failure mode, so additions
need no ceremony and the golden is regenerated whenever convenient.

REMOVING A TEST is a golden change under `CLAUDE.md` § Testing: regenerate in
its own commit, with the reason in the closure artifact. A rename is a removal
plus an addition and takes the same route -- which is the point, because a
rename is indistinguishable from a deletion to everything else in this
repository.

WHAT IT DOES NOT CHECK, so it is not trusted past its reach: whether a test
that still exists still asserts anything. A body emptied to `pass` collects
under the same name and this file says nothing about it. That is the reviewer's,
and the corpora are what measure it.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
GOLDEN = ROOT / "tests" / "goldens" / "collected_tests.txt"


def _generator():
    spec = importlib.util.spec_from_file_location(
        "regen_collected_golden", ROOT / "scripts" / "regen_collected_golden.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


GEN = _generator()
RECORDED = GEN.parse(GOLDEN.read_text(encoding="utf-8")) if GOLDEN.is_file() else {}


def test_the_golden_exists_and_records_something() -> None:
    """A missing or empty golden would make every check below vacuous."""
    assert GOLDEN.is_file(), (
        f"{GOLDEN.relative_to(ROOT)} is missing. Generate it with "
        "`python scripts/regen_collected_golden.py`; without it nothing "
        "notices a deleted test."
    )
    assert RECORDED, "the golden parsed to no roots at all"
    total = sum(len(v) for v in RECORDED.values())
    assert total > 300, (
        f"the golden records {total} test functions. This suite is larger "
        "than that, so the file was generated against something else."
    )


@pytest.mark.parametrize("root", sorted(RECORDED) or ["(none)"])
def test_every_recorded_test_is_still_collected(root: str) -> None:
    if root == "(none)":
        pytest.fail("reported by test_the_golden_exists_and_records_something")
    now = GEN.collected(root)
    assert now, (
        f"`pytest {root} --collect-only` collects nothing. Either the root "
        "moved or collection is erroring, and both are worse than a deletion."
    )
    gone = sorted(RECORDED[root] - now)
    assert not gone, (
        f"{len(gone)} test(s) recorded under `{root}` are no longer "
        f"collected:\n  " + "\n  ".join(gone[:8]) + "\n"
        "A test is never deleted to get a green build (`CLAUDE.md`). If the "
        "removal is intended, regenerate this golden IN ITS OWN COMMIT with "
        "the reason in the closure artifact -- a rename is a removal plus an "
        "addition and takes the same route."
    )


def test_the_golden_would_notice_the_deletion_that_caused_it() -> None:
    """The ablation, on the three tests that were actually lost.

    Not a synthetic name: these three were deleted at `be534a8`, restored at
    CM0, and they are what this file was written for. If any of them stops
    being recorded, the golden was regenerated over a deletion rather than
    beside one.
    """
    rung4 = RECORDED.get("tests/verification/rung4", set())
    for name in (
        "test_channels_are_not_interchangeable",
        "test_a_validation_error_SURVIVES_propagation",
        "test_mu_is_present_and_not_all_zero",
    ):
        assert any(n.endswith(f"::{name}") for n in rung4), (
            f"{name} is not in the golden. It was deleted once already, by a "
            "commit that meant to rewrite the function above it."
        )


def test_a_missing_name_is_reported_rather_than_crashed_on() -> None:
    """The guard's own failure mode: a name that never existed.

    A golden listing a test that is not there must produce a NAMED failure,
    not an error during collection of this file -- which is R234's lesson
    applied to the newest guard rather than re-learned on it.
    """
    root = "tests/regression"
    now = GEN.collected(root)
    planted = {*RECORDED.get(root, set()), "tests/regression/test_nothing.py::test_planted"}
    gone = sorted(planted - now)
    assert gone == ["tests/regression/test_nothing.py::test_planted"], (
        "the comparison did not single out the planted name, so what the "
        f"message would print is not what is missing: {gone}"
    )


def test_the_generator_and_the_golden_agree_on_shape() -> None:
    """A golden whose format the generator no longer writes is unreadable.

    The parse is one function used by both sides, so this asserts the roots
    the generator declares are the roots the file carries -- a root added to
    the script and not regenerated into the file is silently unchecked.
    """
    assert set(RECORDED) == set(GEN.ROOTS), (
        f"the golden records {sorted(RECORDED)} and the generator declares "
        f"{sorted(GEN.ROOTS)}. Regenerate it."
    )


def test_parametrised_ids_are_NOT_recorded() -> None:
    """The decision that keeps this golden stable, asserted.

    Parameter sets move with the reviewer's corpora and with the report being
    written. Recording them would make this file churn every round and the
    signal would be lost in it.
    """
    with_params = [n for names in RECORDED.values() for n in names if "[" in n]
    assert not with_params, f"{with_params[:3]} carry parameter ids. The golden records functions."
