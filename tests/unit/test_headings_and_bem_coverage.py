"""FL2(c): headings as a declared list, and the BEM coverage refusal.

FL(c) asks for three things and this file carries two of them:

* **headings: any list** -- declared, checked against the same `HEADING` bound a case's
  own heading uses, with a repeat refused;
* **`export` refuses a heading the BEM dataset does not cover, naming what is missing** --
  the naming half, complete and tested here.

**THE THIRD IS UNDERDETERMINED BY WHAT THIS REPOSITORY HOLDS, AND SAYING SO IS THE
POINT.** FL(c) also asks that "the governing envelope is taken over all headings and
cases, and the report shows the governing heading". A dynamic-inputs npz records ONE
heading for the whole file -- `exported_wave_basis` returns a single `heading_deg`, and
the EX3/R724 caveat on every artifact says the heading dependence is UNTESTED for exactly
that reason. So an envelope over several headings needs a multi-heading npz, and producing
one is the `export` path, which needs the pinned HSP worktree that FL1 scoped out of step
1. Building a multi-heading envelope against a single-heading file would mean inventing
the other headings' loads.

The same fact is why `refuse_uncovered_headings` TAKES the covered set rather than holding
one: which headings the BEM dataset carries is a property of the pinned HSP state, whose
datasets and reader (`readers/capytaine.py`) live in HSP and not here.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml

from floatfea.run.config import ConfigError, load_config
from floatfea.run.pipeline import (
    refuse_headings_this_run_cannot_cover,
    refuse_uncovered_headings,
    uncovered_headings,
)

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"

# A set a test supplies, NOT a claim about any real dataset.
COVERED = (0.0, 45.0, 90.0, 135.0, 180.0)


@pytest.fixture
def cfg_with(tmp_path: Path) -> Any:
    """The shipped example with `load_cases.headings` set, paths absolutised."""

    def make(headings: Any) -> Path:
        data = copy.deepcopy(yaml.safe_load(EXAMPLE.read_text(encoding="utf-8")))
        for block, key in (("floatsim", "deck"), ("load_cases", "npz"), ("outputs", "directory")):
            value = data.get(block, {}).get(key)
            if isinstance(value, str) and value.strip():
                data[block][key] = str((EXAMPLE.parent / value).resolve())
        if headings is not None:
            data["load_cases"]["headings"] = headings
        path = tmp_path / "config.yaml"
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        return path

    return make


# ---------------------------------------------------------------------------
# The declared list
# ---------------------------------------------------------------------------


def test_FL2c_headings_are_ANY_LIST(cfg_with: Any) -> None:
    """FL(c)'s own words. Four headings, in the order declared."""
    cfg = load_config(cfg_with([0.0, 45.0, 90.0, 180.0]))
    assert cfg.load_cases.headings == (0.0, 45.0, 90.0, 180.0)


def test_FL2c_an_ABSENT_headings_key_declares_none(cfg_with: Any) -> None:
    """The default, which is what the shipped example runs.

    An absent key means "whatever the dynamic-inputs file was exported at", which the
    wave-basis line states and the EX3/R724 caveat qualifies.
    """
    assert load_config(cfg_with(None)).load_cases.headings == ()


@pytest.mark.parametrize(
    ("label", "headings", "needle"),
    [
        ("an empty list", [], "the list is EMPTY"),
        ("a repeat", [0.0, 45.0, 0.0], "contains a repeat"),
        ("a scalar", 45.0, "expected a list"),
        ("a string in the list", [0.0, "45"], "deg"),
        ("below the declared range", [-1.0], "deg"),
        ("above the declared range", [360.1], "deg"),
        ("an unquoted bool", [True], "deg"),
    ],
)
def test_FL2c_the_schema_refuses(cfg_with: Any, label: str, headings: Any, needle: str) -> None:
    """One case per way a declared heading list can be wrong.

    The range cases go through `HEADING`, the same bound a case's own `heading` uses --
    one declared domain rather than a second copy of it.
    """
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_with(headings))
    assert needle in str(caught.value), (label, str(caught.value))


def test_FL2c_the_declared_bound_is_the_SAME_one_a_case_uses() -> None:
    """Not a second copy. `0` and `360` are both inside it, so neither end is excluded."""
    from floatfea.run.config import HEADING

    assert HEADING == ("deg", 0.0, 360.0)  # not-a-tolerance: the declared domain


# ---------------------------------------------------------------------------
# The BEM coverage refusal
# ---------------------------------------------------------------------------


def test_FL2c_a_COVERED_set_is_accepted() -> None:
    """The control, so the refusals below are not refusing everything."""
    refuse_uncovered_headings((0.0, 45.0, 180.0), COVERED)
    assert uncovered_headings((0.0, 45.0, 180.0), COVERED) == ()


def test_FL2c_EVERY_missing_heading_is_named_not_just_the_first() -> None:
    """A reader fixing a configuration needs the whole list.

    Half of an item is not the item -- the same argument CLAUDE.md makes about a closing
    condition that names sites.
    """
    with pytest.raises(ConfigError) as caught:
        refuse_uncovered_headings((0.0, 30.0, 45.0, 200.0), COVERED)
    message = str(caught.value)
    assert "30.0" in message and "200.0" in message, message
    assert "[30.0, 200.0]" in message, message
    # and it says what IS carried, so the fix is visible without opening the dataset
    assert "45.0" in message, message


def test_FL2c_the_missing_list_is_in_DECLARATION_order() -> None:
    """Not sorted. The order a reader wrote is the order they read the refusal in."""
    assert uncovered_headings((200.0, 30.0), COVERED) == (200.0, 30.0)


def test_FL2c_a_NEAR_MISS_is_refused_because_a_heading_is_a_DECLARED_INPUT() -> None:
    """`44.9` against a covered `45.0` is refused, and there is no tolerance here.

    A run that asked for 45 deg and silently got 44.9 would publish an envelope for a sea
    state nobody declared. The comparison is exact because the quantity is an input and
    not a measurement, so "near enough" is the wrong question rather than a value to pick.
    """
    assert uncovered_headings((44.9,), COVERED) == (44.9,)
    with pytest.raises(ConfigError):
        refuse_uncovered_headings((44.9,), COVERED)


def test_FL2c_an_EMPTY_declared_set_asks_for_nothing_and_is_accepted() -> None:
    """Nothing declared cannot be uncovered. The schema already refuses an empty LIST;
    this is the tuple that results from the key being absent."""
    refuse_uncovered_headings((), COVERED)
    assert uncovered_headings((), ()) == ()


def test_FL2c_an_EMPTY_covered_set_refuses_everything_declared() -> None:
    """EH4's weakening direction: a dataset carrying nothing covers nothing.

    The opposite reading -- "no coverage list means do not check" -- would turn a missing
    dataset into a silent pass, which is the shape this whole refusal exists to prevent.
    """
    assert uncovered_headings((0.0,), ()) == (0.0,)
    with pytest.raises(ConfigError):
        refuse_uncovered_headings((0.0,), ())


# ---------------------------------------------------------------------------
# R866: a declared heading this run cannot cover is refused BEFORE any output
# ---------------------------------------------------------------------------
#
# **THE DEFECT WAS MINE AND IT WAS THE SHAPE R809 ALREADY REFUSES.** `headings` was
# parsed, range-checked and repeat-checked, and read by nothing. Measured through the
# real CLI on the shipped example with `headings: [0.0, 45.0, 90.0]`:
#
#     EXIT=0  wrote member_forces.csv (1248 rows) / utilisation.csv (32) / report.md
#     governing U = 1.71167 at platform:hub4_arm ROOT
#
# so two artifacts shipped as the output of a configuration declaring three headings,
# with `U` presented as THE governing utilisation while being the envelope over heading
# 0 alone. The fact needed to catch it is LOCAL: the npz records its own heading.


def test_R866_a_declared_heading_the_RUN_cannot_cover_is_REFUSED() -> None:
    """The envelope would be published as THE envelope over a set that never ran."""
    with pytest.raises(ConfigError) as caught:
        refuse_headings_this_run_cannot_cover((0.0, 45.0, 90.0), {"heading_deg": 0.0})
    message = str(caught.value)
    assert "45.0" in message and "90.0" in message, message
    assert "0.0 deg" in message, "the refusal does not say what the run DOES cover"
    assert "before any output is written" in message, message


def test_R866_the_declared_set_matching_the_run_is_ACCEPTED() -> None:
    """The control. Declaring exactly what the file carries is not an error."""
    refuse_headings_this_run_cannot_cover((0.0,), {"heading_deg": 0.0})


def test_R866_declaring_NOTHING_is_accepted() -> None:
    """An absent key means "whatever the export used", which the artifacts state."""
    refuse_headings_this_run_cannot_cover((), {"heading_deg": 0.0})
    refuse_headings_this_run_cannot_cover((), {})


def test_R866_a_SIDECAR_LESS_npz_refuses_a_declared_set_rather_than_assuming_zero() -> None:
    """FL1(a) admits an npz whose export recorded no heading.

    Assuming 0 would make the commonest declared value pass by coincidence, which is the
    weakening direction: the run cannot SHOW it covered anything, so it refuses.
    """
    with pytest.raises(ConfigError) as caught:
        refuse_headings_this_run_cannot_cover((0.0,), {})
    assert "records NO heading" in str(caught.value), str(caught.value)


def test_R866_the_check_REUSES_the_coverage_function() -> None:
    """One comparison, not two.

    `uncovered_headings` is exact for the reason stated at its own definition, and this
    check inherits it rather than re-deciding whether 44.9 is 45.
    """
    with pytest.raises(ConfigError):
        refuse_headings_this_run_cannot_cover((44.9,), {"heading_deg": 45.0})


# ---------------------------------------------------------------------------
# R872, R873, R874: the RECORDED side -- the side the R866 repair created
# ---------------------------------------------------------------------------
#
# All three were found on the half my own four-row table said nothing about. The table
# measured the DECLARED side; the repair introduced a comparison against a value read
# out of a sidecar, and that value was unvalidated.


@pytest.mark.parametrize(
    ("declared", "recorded"),
    [(360.0, 0.0), (0.0, 360.0), (360.0, 360.0)],
    ids=["360 vs 0", "0 vs 360", "360 vs 360"],
)
def test_R872_360_and_0_are_ONE_direction(declared: float, recorded: float) -> None:
    """`heading_deg` is a direction of travel from +X, so 360 names what 0 names.

    `HEADING`'s domain is inclusive at both ends, so `headings: [360.0]` is a legal
    declaration -- and against an export at 0 it was refused, through the real CLI, with
    `EXIT=2` and no directory created.

    ARITHMETIC, NOT SLACK: the question is whether two names denote one direction, not
    whether two directions are close enough. There is no tolerance here to choose.
    """
    refuse_headings_this_run_cannot_cover((declared,), {"heading_deg": recorded})
    assert uncovered_headings((declared,), (recorded,)) == ()


def test_R872_a_NEAR_MISS_is_still_refused_after_the_modulo() -> None:
    """The exactness `refuse_uncovered_headings` documents survives R872's repair.

    `44.9 % 360.0` is `44.9`, so normalising a direction does not round one.
    """
    assert uncovered_headings((44.9,), (45.0,)) == (44.9,)
    with pytest.raises(ConfigError):
        refuse_headings_this_run_cannot_cover((44.9,), {"heading_deg": 45.0})


@pytest.mark.parametrize(
    ("label", "recorded"),
    [
        ("a LIST, which is a multi-heading export", [0.0, 45.0]),
        ("a bool, which is what YAML makes of `yes`", True),
        ("a string", "0"),
    ],
)
def test_R873_R874_a_NON_SCALAR_recorded_heading_is_REFUSED_BY_NAME(
    label: str, recorded: Any
) -> None:
    """The declared side refuses a bool in eleven places; the recorded side coerced one.

    `{"heading_deg": True}` against a declared `[1.0]` was ACCEPTED, because `float(True)`
    is `1.0`, and the run published `heading True deg` with the comparison agreeing. A
    LIST raised `TypeError` inside `float()`, so the one check that exists to compare
    declared against covered ABSTAINED instead of refusing.
    """
    declared = (1.0,) if recorded is True else (0.0,)
    with pytest.raises(ConfigError) as caught:
        refuse_headings_this_run_cannot_cover(declared, {"heading_deg": recorded})
    message = str(caught.value)
    assert "recorded `heading_deg`" in message, (label, message)
    assert "not a single heading" in message, (label, message)


def test_R873_a_VALID_recorded_heading_still_passes() -> None:
    """The control, so the refusals above are not refusing every sidecar."""
    refuse_headings_this_run_cannot_cover((0.0,), {"heading_deg": 0.0})
    refuse_headings_this_run_cannot_cover((90.0,), {"heading_deg": 90})
