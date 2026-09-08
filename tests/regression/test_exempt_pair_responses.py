"""Exempt (entry, defect) pairs the gate detects today keep detecting (BS2).

A pair whose injected defect is below `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`
carries no red assertion **from the classification** -- three of the four defects
are in `UNCONDITIONALLY_RED` and are asserted red whatever their classification,
so the premise stated here at first ("carries no red assertion") was true only of
`dropped_shear_parameter` (R158). What every exempt pair does lack is a claim
that it MUST be caught, and that is what this file replaces with a record.

**And most of them are detected anyway** -- see `exempt_detected` in
`docs/milestones/F2_figures.md`, regenerated -- one of them by `2956x`.
Leaving that unrecorded means a pair the gate catches now could stop being
caught with the suite green.

WHY A GOLDEN FILE AND NOT AN ASSERTION ON THE OUTCOME. Asserting "red wherever
the response exceeds the ceiling, regardless of classification" asserts the
measurement against itself -- the predicate and the outcome are the same number,
and such a test passes whatever the code does. What these pairs need is not a
claim but a REGRESSION: the response is recorded, and a move in it fails the
build. The claim stays where it is honest, at the classification; the protection
extends to everything measured.

CHANGING THE GOLDEN FILE. `CLAUDE.md` § Testing: a golden-file change requires a
written explanation of why the numbers moved, in the milestone closure artifact.
Regenerating it to match new output without that explanation is the same error as
widening a tolerance. The file is produced by the classification and the corpus
together, so it moves when either does -- and a corpus round that adds entries is
a legitimate reason, stated per round.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))

from test_corpus_configurations import (  # noqa: E402
    INJECTED_DEFECTS, SOLVED, STATES, _oob_with_injected, classify,
)

from floatfea.testing import assert_close  # noqa: E402
from floatfea.tolerances import (EXEMPT_RESPONSE_DRIFT,  # noqa: E402
                                 EXEMPT_RESPONSE_DRIFT_COUNTER,
                                 PATCH_TEST_EXACTNESS)

GOLDEN = Path(__file__).with_name("g22_exempt_pair_responses.json")


def _recorded() -> dict[str, float]:
    return json.loads(GOLDEN.read_text(encoding="utf-8"))


def _measured() -> dict[str, float]:
    out: dict[str, float] = {}
    for entry in SOLVED:
        for kind in INJECTED_DEFECTS:
            if classify(entry, kind) != "below resolution":
                continue
            worst = max(_oob_with_injected(entry, st, kind) for st in STATES)
            if worst > PATCH_TEST_EXACTNESS:
                out[f"{entry['id']}|{kind}"] = worst
    return out


def test_the_golden_file_is_not_empty() -> None:
    """Meta-test: an empty file makes every comparison below vacuous."""
    recorded = _recorded()
    assert recorded, "the golden file records no pair; nothing below checks anything"
    assert len(recorded) >= 10, (
        f"only {len(recorded)} pairs recorded. The exempt set is larger than "
        "that, so the file has been trimmed rather than regenerated."
    )


def test_every_recorded_pair_is_still_detected() -> None:
    """The regression: a pair caught today does not stop being caught.

    Compared on the RATIO to the ceiling, which is `O(1)`, rather than on two
    numbers near `1e-14` -- R38's lesson. The band is `EXEMPT_RESPONSE_DRIFT`,
    which is this quantity's own entry: it was `SUBDIVISION_INVARIANCE` borrowed,
    and a tolerance declared for the deviation between meshes of one member is
    not the admissible drift of a recorded response (R160). One number answering
    to two measurements can be moved by either.
    """
    recorded, measured = _recorded(), _measured()
    missing = sorted(set(recorded) - set(measured))
    assert not missing, (
        f"{missing} were recorded as exempt-and-detected and are no longer "
        "both. Either the classification moved them, or the gate has stopped "
        "detecting them -- the second is the failure this file exists for."
    )
    for key, was in sorted(recorded.items()):
        now = measured[key]
        assert_close(
            now / PATCH_TEST_EXACTNESS, was / PATCH_TEST_EXACTNESS,
            EXEMPT_RESPONSE_DRIFT, floor=np.finfo(float).eps,
            what=(f"{key}: the response moved from {was:.6e} to {now:.6e}. This "
                  "pair carries no red assertion because its defect is below "
                  "the declared resolution, so nothing else would have noticed"),
        )


def test_the_recorded_set_is_the_measured_set() -> None:
    """A new exempt-and-detected pair is a golden-file change, not a silent add.

    Without this, a corpus round could introduce a pair the gate detects, and it
    would sit outside the regression with nothing recording it.
    """
    extra = sorted(set(_measured()) - set(_recorded()))
    assert not extra, (
        f"{extra} are exempt and detected but not in the golden file. Regenerate "
        "it and state in the closure artifact why the set grew -- a corpus round "
        "is a reason; a classification change is a different one."
    )


def test_a_MOVED_response_is_caught() -> None:
    """`EXEMPT_RESPONSE_DRIFT`'s counter, injected (BG1).

    Without this the comparison above inspects two numbers that are equal by
    construction on a clean tree, and would look identical to one that compares
    nothing. The injected move is `EXEMPT_RESPONSE_DRIFT_COUNTER`, five orders
    above the band.
    """
    recorded = _recorded()
    key = sorted(recorded)[0]
    was = recorded[key]
    moved = was * (1.0 + EXEMPT_RESPONSE_DRIFT_COUNTER)
    with pytest.raises(AssertionError):
        assert_close(moved / PATCH_TEST_EXACTNESS, was / PATCH_TEST_EXACTNESS,
                     EXEMPT_RESPONSE_DRIFT, floor=np.finfo(float).eps,
                     what=f"{key}: injected drift")
