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
    _validated_wave_basis,
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


# ---------------------------------------------------------------------------
# R876: the MODULUS is held, not just its two endpoints
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("declared", "covered"),
    [(180.0, 0.0), (90.0, 0.0), (270.0, 90.0)],
    ids=["head vs following", "beam vs following", "beam vs beam"],
)
def test_R876_a_DIFFERENT_direction_is_not_covered(declared: float, covered: float) -> None:
    """The row that pins the modulus to 360 rather than to anything coarser.

    **NOTHING HELD THE MODULUS.** `% 180.0` and `% 90.0` both left the suite at `29
    passed`: the `44.9` case measures fineness WITHIN one turn and the `360`/`0` case
    measures that ONE turn is identified, and together they admit every modulus from 90
    to 360. A head sea is not covered by a following sea, and that is the assertion that
    separates them.
    """
    assert uncovered_headings((declared,), (covered,)) == (declared,)
    with pytest.raises(ConfigError):
        refuse_headings_this_run_cannot_cover((declared,), {"heading_deg": covered})


# ---------------------------------------------------------------------------
# R877 / R878 / R879: the wave basis is validated AT THE READER
# ---------------------------------------------------------------------------
#
# The first repair validated `heading_deg` inside the comparison, which returns early
# when no `load_cases.headings` is declared -- and the shipped example declares none, so
# the defect published on exactly the path the check could not reach. Measured through
# the CLI with `heading_deg = true`: no headings declared -> EXIT=0 and
# `* **heading** - True deg` in report.md; `headings: [1.0]` -> EXIT=2.

SIDECAR = Path("dynamic_inputs.provenance.json")
GOOD = {
    "heading_deg": 0.0,
    "wave_height_full_m": 24.2,
    "wave_height_model_m": 0.484,
    "lambda": 50.0,
    "window": "the last 5 whole periods",
}
"""The committed sidecar's own shape. `lambda` joined the basis as R903."""


def test_R877_an_EMPTY_basis_is_still_empty() -> None:
    """No sidecar, or no recorded run block, is NOT RECORDED and not an error."""
    assert _validated_wave_basis({}, SIDECAR) == {}


def test_R877_the_COMMITTED_shape_passes() -> None:
    """The control: all four fields, the types the real sidecar carries."""
    assert _validated_wave_basis(dict(GOOD), SIDECAR) == GOOD


@pytest.mark.parametrize(
    ("label", "key", "value"),
    [
        ("a bool heading", "heading_deg", True),
        ("a bool wave height", "wave_height_full_m", True),
        ("a list heading", "heading_deg", [0.0, 45.0]),
        ("a string height", "wave_height_model_m", "0.484"),
        ("a non-string window", "window", 5),
    ],
)
def test_R877_a_BAD_FIELD_is_refused_at_the_reader(label: str, key: str, value: Any) -> None:
    """Every published field, not only the one a comparison happens to read.

    `wave_height_full_m: true` published `True m full scale` at exit 0 before this.
    """
    basis = dict(GOOD) | {key: value}
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(basis, SIDECAR)
    assert f"run.{key}" in str(caught.value), (label, str(caught.value))


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_R879_a_NON_FINITE_recorded_value_is_refused_BY_NAME(value: float) -> None:
    """By name here, rather than one line later by a coverage message.

    R873's condition asked for NaN refused by name and the first repair caught it only
    where a comparison happened to look -- which is to say, only when one was asked for.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"heading_deg": value}, SIDECAR)
    assert "not finite" in str(caught.value), str(caught.value)


@pytest.mark.parametrize("value", [450.0, -10.0, 360.1])
def test_R879_a_recorded_heading_OUTSIDE_the_declared_domain_is_refused(value: float) -> None:
    """One domain, not two -- and the RAW value, which the first repair got wrong.

    It tested `heading % 360.0`, so `450.0` passed (`450 % 360` is `90`) and the run
    published `450.0 deg` in all three artifacts at exit 0: `member_forces.csv` 193718
    bytes against the control's 193716, the two extra bytes being the digits.

    The two uses of 360 pull opposite ways and both are right: COMPARING asks whether two
    headings are the same direction and normalises; RANGE-CHECKING asks whether a recorded
    value is one a configuration could legally declare, and that is `0..360` raw.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"heading_deg": value}, SIDECAR)
    message = str(caught.value)
    # **THE HEADING HAS ITS OWN MESSAGE NOW, AND FY1 IS WHY (FY1, FY5.1).** It no longer
    # shares the generic "outside the declared domain" wording, because FY1 asks the
    # refusal to name the value, the accepted range AND the remedy -- so a reader whose
    # export wrote a signed heading is told to normalise it mod 360 under the convention
    # in `docs/conventions.md:150` rather than left to work that out. All three are
    # asserted, because a message that names the value and not the remedy is the half of
    # this that R885 already had.
    assert "accepted range 0 <= heading <= 360 deg" in message, message
    assert f"{value:g} deg" in message, message
    assert "docs/conventions.md:150" in message, message
    assert "mod 360" in message, message


@pytest.mark.parametrize("value", [0.0, 360.0, 180.0])
def test_R879_the_domain_is_INCLUSIVE_at_both_ends(value: float) -> None:
    """`HEADING` is `(0.0, 360.0)` inclusive, so neither end is excluded here either."""
    assert _validated_wave_basis(dict(GOOD) | {"heading_deg": value}, SIDECAR)


@pytest.mark.parametrize("key", ["wave_height_full_m", "wave_height_model_m"])
@pytest.mark.parametrize("value", [-24.2, -0.484, -1e-9, 100.1, 1000.0])
def test_R881_a_recorded_WAVE_HEIGHT_outside_its_declared_domain_is_refused(
    key: str, value: float
) -> None:
    """R879 range-checked the HEADING and left both heights typed but unbounded.

    One variable moved, the committed sidecar with its two heights negated, through the
    real CLI:

        wave_height_full_m =  24.2  ->  EXIT=0, "24.2 m full scale (0.484 m model)"
        wave_height_full_m = -24.2  ->  EXIT=0, "-24.2 m full scale (-0.484 m model)"

    with `member_forces.csv` at 193716 bytes against the control's 193714. A negative
    wave height is not a wave, and it reached all three published artifacts at exit 0.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {key: value}, SIDECAR)
    message = str(caught.value)
    assert f"run.{key}" in message, message
    # **THE TWO HEIGHTS NOW FAIL WITH DIFFERENT MESSAGES, AND THAT IS FY2 (FY2).** The
    # full-scale height carries `WAVE_HEIGHT`'s declared `0..100 m`. The model height
    # carries no constant at all: its ceiling is DERIVED as `100/lambda`, which at the
    # committed lambda of 50 is 2 m, so the message names the derivation rather than a
    # declared domain. Asserting one message for both would have passed while saying
    # nothing about which bound each was checked against.
    if key == "wave_height_full_m":
        assert "outside the declared domain" in message, message
    else:
        assert "That ceiling is DERIVED" in message, message


@pytest.mark.parametrize("value", [0.0, 100.0, 24.2])
def test_R881_the_WAVE_HEIGHT_domain_is_INCLUSIVE_at_both_ends(value: float) -> None:
    """`WAVE_HEIGHT` is `(0.0, 100.0)` inclusive, as the configured side already is.

    A calm sea is `0.0` m and the bound admits it; the refusal above is about values no
    declaration could express, not about small ones.

    **THE PAIR MOVES TOGETHER NOW, AND NOT BECAUSE THE ASSERTION NEEDED HELP (FY2).** This
    cell used to set the full height alone and leave the model height at `0.484`, which
    was admissible only while nothing related the two. Under FY2 `100.0` m full against
    `0.484` m model at lambda 50 is a refusal -- correctly, since it implies `24.2` m --
    so varying one leg of the triple in isolation stopped being a test of the BOUND and
    became a test of the pair check. The model height is set to `value / lambda`, which is
    what an exporter would have written, and the bound is still what is under test: at
    `100.0` the model height is `2.0`, exactly its derived ceiling, so this also pins the
    inclusive end of the DERIVED bound.
    """
    lam = float(GOOD["lambda"])
    assert _validated_wave_basis(
        dict(GOOD) | {"wave_height_full_m": value, "wave_height_model_m": value / lam},
        SIDECAR,
    )


def test_R881_EVERY_numeric_recorded_field_HAS_a_declared_domain() -> None:
    """The shape of the defect, not the two instances of it.

    R881 was a field carrying a type check and no domain. A fifth field added to
    `WAVE_BASIS_KEYS` with a type check and no entry in `RECORDED_BOUNDS` would be the
    same defect again, and nothing above would notice: the cases are keyed on the names
    that exist today.
    """
    from floatfea.run.pipeline import HEIGHT_PAIR, RECORDED_BOUNDS, WAVE_BASIS_KEYS

    # **DECLARED OR DERIVED, AND THE DISTINCTION IS THE WHOLE OF FY2 (FY2).** The invariant
    # this cell protects is that no recorded numeric field reaches a deliverable with a
    # type check and no domain -- which is what R881 was. `wave_height_model_m` left
    # `RECORDED_BOUNDS` because its ceiling is `100/lambda` rather than a constant, so the
    # old equality would now fail for the one field whose bound got STRICTER. The
    # invariant is restated to cover both kinds, and the derived one is named rather than
    # excused, so a sixth field added with neither is still caught.
    derived = {HEIGHT_PAIR[1]}
    numeric = [k for k in WAVE_BASIS_KEYS if not isinstance(GOOD[k], str)]
    assert set(numeric) == set(RECORDED_BOUNDS) | derived, (
        f"these recorded numeric fields have no domain, declared or derived: "
        f"{sorted(set(numeric) - set(RECORDED_BOUNDS) - derived)}"
    )
    for key, (unit, low, high) in RECORDED_BOUNDS.items():
        assert low < high and unit, (key, unit, low, high)
    # And the derived one really is bounded: at the committed lambda its ceiling is 2 m,
    # which is `WAVE_HEIGHT`'s high bound divided by lambda and not a second constant.
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(
            dict(GOOD) | {"wave_height_model_m": 2.001, "wave_height_full_m": 100.0}, SIDECAR
        )
    assert "That ceiling is DERIVED" in str(caught.value), str(caught.value)


@pytest.mark.parametrize(
    "missing", [k for k in GOOD if k not in ("wave_height_full_m", "wave_height_model_m")]
)
def test_R878_a_PARTIAL_sidecar_is_refused_rather_than_downgraded(missing: str) -> None:
    """A sidecar missing a field is WRONG, not absent.

    `_header_lines` subscripts all four keys and `_write_report` `.get`s the same four, so
    a partial record made the dict truthy, took the subscripting branch and raised
    `KeyError` AFTER the solve -- exit 1, with a zero-byte `member_forces.csv` already in
    the outputs directory. That is R829/FQ3's single-branch repair never reaching the
    report path.
    """
    partial = {k: v for k, v in GOOD.items() if k != missing}
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(partial, SIDECAR)
    message = str(caught.value)
    assert "PARTIAL wave basis" in message and missing in message, message


@pytest.mark.parametrize("value", ["fifty", -50.0, 0.0, True, 1.0e9, 1000.1, float("nan"), [50.0]])
def test_R903_a_bad_recorded_LAMBDA_is_refused(value: Any) -> None:
    """The scale was read raw and published in the same sentence as the two heights.

    `scripts/measure/f6_results_report.py` printed `Froude lambda = {run['lambda']}`
    straight from the JSON, so `fifty`, `-50.0`, `True` and `1e9` each reached a published
    deliverable at EXIT=0 -- beside two heights that the same line had just validated.

    And lambda is the one recorded field whose CONFIGURED counterpart genuinely exists:
    `FROUDE_LAMBDA = ("-", 1.0, 1000.0)` in `config.py`, applied by `_checked`. So
    `RECORDED_BOUNDS`' original justification was literally true of the only key that was
    not in it (R895's other half).
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"lambda": value}, SIDECAR)
    assert "run.lambda" in str(caught.value), str(caught.value)


@pytest.mark.parametrize("value", [1.0, 50.0, 1000.0])
def test_R903_the_LAMBDA_domain_is_inclusive_and_admits_the_committed_scale(
    value: float,
) -> None:
    """`FROUDE_LAMBDA` is `(1.0, 1000.0)` inclusive, and 50 is the committed export.

    **THE MODEL HEIGHT MOVES WITH LAMBDA, BECAUSE UNDER FY2 IT MUST (FY2).** This cell set
    lambda alone and left both heights at the committed pair, which was admissible only
    while nothing related the three. At lambda 1000 the committed `0.484` m model height is
    above its derived ceiling of `0.1` m AND implies `484` m full scale -- two refusals, for
    a cell whose subject is the lambda BOUND. The model height is set to `full / lambda`,
    so the triple is consistent at every rung and what is under test is the bound.
    """
    full = float(GOOD["wave_height_full_m"])
    assert _validated_wave_basis(
        dict(GOOD) | {"lambda": value, "wave_height_model_m": full / value}, SIDECAR
    )


def test_R877_the_READER_ITSELF_validates_not_only_the_helper(tmp_path: Path) -> None:
    """Through `exported_wave_basis`, which is the CALL SITE (R828's shape, third time).

    **THE CASES ABOVE DRIVE `_validated_wave_basis` DIRECTLY AND ARE GREEN WITH THE CALL
    REMOVED FROM THE READER:** measured `52 passed` with `return _validated_wave_basis(...)`
    replaced by `return present`. That is the hole R866 was, and the hole R877 was, and
    testing a helper while nothing holds its caller is how both shipped. So this one reads
    a real sidecar off disk.
    """
    import json as _json

    from floatfea.run.pipeline import exported_wave_basis

    npz = tmp_path / "dynamic_inputs.npz"
    npz.write_bytes(b"")  # never opened: the sidecar is read from the path alone
    sidecar = npz.with_suffix(".provenance.json")

    sidecar.write_text(_json.dumps({"run": dict(GOOD)}), encoding="utf-8")
    assert exported_wave_basis(npz) == GOOD

    sidecar.write_text(_json.dumps({"run": dict(GOOD) | {"heading_deg": True}}), encoding="utf-8")
    with pytest.raises(ConfigError) as caught:
        exported_wave_basis(npz)
    assert "run.heading_deg" in str(caught.value), str(caught.value)

    # **THE PARTIAL CASE DROPS `window`, NOT A HEIGHT, AND FY2 IS WHY.** Dropping
    # `wave_height_full_m` is no longer partial: FY2 derives it from the model height and
    # lambda, so this case would have asserted a refusal that is now a feature. `window`
    # is one of the three fields that are one quantity each, where R878's rule is
    # unchanged -- a sidecar missing one of those is WRONG rather than ABSENT.
    partial = {k: v for k, v in GOOD.items() if k != "window"}
    sidecar.write_text(_json.dumps({"run": partial}), encoding="utf-8")
    with pytest.raises(ConfigError) as caught:
        exported_wave_basis(npz)
    assert "PARTIAL wave basis" in str(caught.value), str(caught.value)

    # AND THE HEIGHT PAIR AT THE CALL SITE: one recorded, the other derived, through the
    # reader rather than the helper -- which is this cell's whole reason for existing.
    model_only = {k: v for k, v in GOOD.items() if k != "wave_height_full_m"}
    sidecar.write_text(_json.dumps({"run": model_only}), encoding="utf-8")
    assert exported_wave_basis(npz) == GOOD

    # R881 AT THE CALL SITE TOO. The helper cases above are green with the call removed
    # from the reader, which is exactly how R866, R877 and R881 each shipped.
    sidecar.write_text(
        _json.dumps({"run": dict(GOOD) | {"wave_height_full_m": -24.2}}), encoding="utf-8"
    )
    with pytest.raises(ConfigError) as caught:
        exported_wave_basis(npz)
    assert "run.wave_height_full_m" in str(caught.value), str(caught.value)

    # AND A MISSING SIDECAR IS STILL NOT RECORDED rather than an error (FL1(a)).
    sidecar.unlink()
    assert exported_wave_basis(npz) == {}


# --------------------------------------------------------------- R919 / R908: the scale
#
# `exported_froude_lambda` is a READER. It reports WHERE it found a value and validates
# nothing about WHAT it found, and R906's commit message called it "the validated door",
# which it is not. `validated_export_scale` is the resolver every PUBLISHING path uses.


def _pair(tmp: Path, npz_lam, side_lam) -> Path:
    """A synthetic npz and sidecar, each optionally recording a scale."""
    import json as _json

    import numpy as np

    npz = tmp / "x.npz"
    arrays: dict[str, object] = {"periods_full_s": np.array([12.5])}
    if npz_lam is not None:
        arrays["froude_lambda"] = np.array(npz_lam)
    np.savez(npz, **arrays)
    run: dict[str, object] = {}
    if side_lam is not None:
        run["lambda"] = side_lam
    npz.with_suffix(".provenance.json").write_text(_json.dumps({"run": run}), encoding="utf-8")
    return npz


@pytest.mark.parametrize(
    ("npz_lam", "side_lam"),
    [(50.0, 25.0), (25.0, 50.0), (1.0, 1000.0), (50.0, 50.000001)],
)
def test_R908_the_two_RECORDS_of_the_scale_must_agree(
    tmp_path: Path, npz_lam: float, side_lam: float
) -> None:
    """FN0's PREFERENCE says which to read; it is not a licence to publish from one.

    `exported_froude_lambda` prefers the npz key deliberately -- a sidecar can be
    separated from its npz by a copy and the key cannot -- and
    `test_FN0_the_npz_key_is_PREFERRED_over_the_sidecar` gives them different values on
    purpose to prove which wins. That test stays green: this is a different question.

    Two `scripts/measure/` readers were resolving this quantity for the same file from
    DIFFERENT sources, and both publish it -- the CSV header states the scale and the
    report prints it. Measured at `run.lambda = 25.0`: 2402 diff lines in
    `docs/F4_member_forces.csv` and governing ROOT stress `455.7 -> 275.3 MPa`, at exit 0.

    The comparison is `!=`, the form `run()` already uses at the config/npz door. Give it
    a margin and it becomes a tolerance under another name.
    """
    from floatfea.run.pipeline import validated_export_scale

    with pytest.raises(ConfigError) as caught:
        validated_export_scale(_pair(tmp_path, npz_lam, side_lam))
    assert "scale disagreement" in str(caught.value), str(caught.value)


@pytest.mark.parametrize("lam", [0.5, 1.0e-3, 1.0e6, 1.0e9, 0.999, 1000.1])
def test_R919_a_scale_outside_the_DECLARED_domain_is_refused(tmp_path: Path, lam: float) -> None:
    """One domain per quantity, whichever side of the I/O boundary it arrives from.

    `froude_factor("force", lam)` refuses `0.0`, a negative and a non-finite and ADMITS
    `0.5`, `1e-3`, `1e6` and `1e9` -- four decades beyond the range a CONFIGURED
    `floatsim.froude_lambda` is held to by `_checked`. Nothing applied `FROUDE_LAMBDA` to
    the value read out of a file, so every force and stress published downstream carried
    whatever was there.
    """
    from floatfea.run.pipeline import validated_export_scale

    with pytest.raises(ConfigError) as caught:
        validated_export_scale(_pair(tmp_path, lam, lam))
    assert "outside the admissible range" in str(caught.value), str(caught.value)


@pytest.mark.parametrize("lam", [1.0, 50.0, 1000.0])
def test_R919_the_domain_is_inclusive_and_the_committed_scale_passes(
    tmp_path: Path, lam: float
) -> None:
    """`FROUDE_LAMBDA` is `(1.0, 1000.0)` inclusive; 50 is the committed export."""
    from floatfea.run.pipeline import validated_export_scale

    assert validated_export_scale(_pair(tmp_path, lam, lam)) == lam


def test_R919_a_file_recording_NO_scale_is_refused_not_defaulted(tmp_path: Path) -> None:
    """FN0: a scale nobody declared cannot be inferred, and is not assumed here either."""
    from floatfea.run.pipeline import validated_export_scale

    with pytest.raises(ConfigError) as caught:
        validated_export_scale(_pair(tmp_path, None, None))
    assert "no way to know what scale" in str(caught.value), str(caught.value)


def test_R919_the_SIDECAR_alone_still_answers(tmp_path: Path) -> None:
    """FN0's fallback is intact: the sidecar answers when the npz carries no key."""
    from floatfea.run.pipeline import validated_export_scale

    assert (
        validated_export_scale(_pair(tmp_path, None, 50.0))
        # not-a-tolerance: the scale written INTO the synthetic sidecar on the same line.
        # The assertion is that the resolver returned the value it was GIVEN when the npz
        # carries no key -- an identity on an input, not a comparison of two computed
        # quantities, so there is nothing here a tolerance could be loosened against.
        # Same form and same reason as `test_FN0_the_npz_key_is_PREFERRED_over_the_sidecar`
        # in `tests/regression/test_r1_example_golden.py`.
        == 50.0
    )


def test_R1041_a_BOOL_TYPED_npz_SCALE_is_REFUSED_not_read_as_ONE(tmp_path: Path) -> None:
    """R1033's family at the THIRD site, which neither the verdict nor I had named.

    `exported_froude_lambda` converted whatever the key held, so a bool-typed
    `froude_lambda` became `1.0` -- the BOTTOM of `FROUDE_LAMBDA`'s admissible range, so
    the range check admits it, and a sidecar recording `lambda: 1.0` agrees with it so
    R908's two-record comparison passes too. Driven before the repair:

        exported_froude_lambda  -> (1.0, 'the npz')
        validated_export_scale  -> ADMITTED lambda = 1.0

    `lambda = 1` is NO Froude scaling: every full-scale force equals the model-scale one,
    in the scale `member_forces_table.py` and `f6_results_report.py` both resolve through
    `validated_export_scale` before publishing an EZ0 deliverable.
    """
    import json as _json

    import numpy as np

    from floatfea.run.config import ConfigError
    from floatfea.run.pipeline import exported_froude_lambda, validated_export_scale

    committed = ROOT / "data" / "f4" / "dynamic_inputs.npz"
    raw = np.load(committed, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files}
    flat["froude_lambda"] = np.array(True)
    npz = tmp_path / "boolscale.npz"
    np.savez(npz, **flat)
    side = _json.loads((committed.with_suffix(".provenance.json")).read_text(encoding="utf-8"))
    # The sidecar AGREES with what the bool converts to, so R908's comparison cannot be
    # what refuses this -- without that, the cell would pass without reaching the gate.
    side["run"]["lambda"] = 1.0
    (tmp_path / "boolscale.provenance.json").write_text(_json.dumps(side), encoding="utf-8")

    value, where = exported_froude_lambda(npz)
    assert value is None, (value, where)
    assert "ndarray of dtype bool" in where, where
    assert "NO Froude scaling" in where, where
    with pytest.raises(ConfigError) as excinfo:
        validated_export_scale(npz, tmp_path / "boolscale.provenance.json")
    assert "is not a recorded number" in str(excinfo.value), str(excinfo.value)

    # THE WEAKENING DIRECTION: the committed pair still resolves, at the scale it records.
    #
    # **THE SCALE IS READ FROM THE FILE, NOT TYPED.** The first draft of these two lines
    # compared against `50.0`, which `tests/test_no_tolerance_literals.py` flagged -- an
    # undeclared comparison literal in the cell written to hold a repair, which is R1006
    # for the third consecutive round. Reading it from the npz removes the literal AND
    # makes the assertion the property that matters: the reader returns what the file
    # records, and the resolver agrees with it, rather than both matching a number typed
    # here that would go stale if the committed pair were ever re-exported.
    recorded = float(np.asarray(np.load(committed, allow_pickle=False)["froude_lambda"]).item())
    value, where = exported_froude_lambda(committed)
    assert value == recorded and where == "the npz", (value, where, recorded)
    assert validated_export_scale(committed, committed.with_suffix(".provenance.json")) == recorded


# ---------------------------------------------------------------------------
# R1042: THE SIDECAR BRANCH OF THE SCALE READER, FOUR LINES BELOW R1041's REPAIR
#
# `exported_froude_lambda` has two branches. R1041 repaired the npz one and left this one
# converting unconditionally, in the same function -- so the defect moved to whichever
# record the file happens to carry. `lambda` is cubed on every published force.


def _scale_pair(tmp: Path, sidecar_lambda: object) -> tuple[Path, Path]:
    """A pair whose npz has NO `froude_lambda` key, so the SIDECAR branch answers.

    Without dropping the key the npz branch returns first and this cell would pass
    without reaching the site it is about.
    """
    import json as _json

    import numpy as np

    committed = ROOT / "data" / "f4" / "dynamic_inputs.npz"
    raw = np.load(committed, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files if k != "froude_lambda"}
    npz = tmp / "nokey.npz"
    np.savez(npz, **flat)
    side = _json.loads(committed.with_suffix(".provenance.json").read_text(encoding="utf-8"))
    side["run"]["lambda"] = sidecar_lambda
    prov = tmp / "nokey.provenance.json"
    prov.write_text(_json.dumps(side), encoding="utf-8")
    return npz, prov


@pytest.mark.parametrize(
    "spelling, value",
    [
        pytest.param("JSON true", True, id="json_bool"),
        pytest.param("JSON string", "50", id="json_str"),
        pytest.param("JSON null-in-a-list", [50.0], id="json_list"),
    ],
)
def test_R1042_a_NON_NUMERIC_SIDECAR_SCALE_is_REFUSED_not_converted(
    spelling: str, value: object, tmp_path: Path
) -> None:
    """The three spellings `json.loads` can produce that are not numbers.

    Measured before the repair, on a pair whose npz carries no `froude_lambda`:

        run.lambda = true   -> exported 1.0, validated_export_scale ADMITTED 1.0,
                               froude_factor force x1 and moment x1 -- NO scaling at all
        run.lambda = "50"   -> exported 50.0, a STRING used as a declared number

    And `wave_basis_from_sidecar` REFUSES that same file by name, because `lambda` is in
    `WAVE_BASIS_KEYS` -- one input, two readers, two answers, which is R896 verbatim.
    """
    from floatfea.run.config import ConfigError
    from floatfea.run.pipeline import exported_froude_lambda, validated_export_scale

    npz, prov = _scale_pair(tmp_path, value)
    resolved, where = exported_froude_lambda(npz)
    assert resolved is None, (spelling, resolved, where)
    assert "is not a recorded number" in where, where
    assert "NO Froude scaling" in where, where
    with pytest.raises(ConfigError) as excinfo:
        validated_export_scale(npz, prov)
    assert "is not a recorded number" in str(excinfo.value), str(excinfo.value)


def test_R1042_the_CONTROL_a_numeric_sidecar_scale_still_resolves(tmp_path: Path) -> None:
    """The weakening direction: the repair must not refuse a sidecar that is a number.

    Without this the three arms above could be an unconditional refusal of the sidecar
    branch, which would break every pair whose npz records no scale.
    """
    import json as _json

    from floatfea.run.pipeline import exported_froude_lambda, validated_export_scale

    # THE CONTROL'S SCALE IS THE ONE THIS REPOSITORY SHIPS, read from the committed
    # sidecar rather than typed. The first draft of these three lines compared against
    # `50.0` twice and `tests/test_no_tolerance_literals.py` flagged both -- R1006 for the
    # fourth consecutive round, and the SECOND time in this file, which already had that
    # literal removed for the same reason two commits ago. Deriving it removes the
    # offence and the staleness together: if the pair is ever re-exported at another
    # scale, this cell follows it instead of breaking.
    declared = _json.loads(
        (ROOT / "data" / "f4" / "dynamic_inputs.provenance.json").read_text(encoding="utf-8")
    )["run"]["lambda"]
    npz, prov = _scale_pair(tmp_path, declared)
    resolved, where = exported_froude_lambda(npz)
    assert resolved == declared, (resolved, where, declared)
    assert "run.lambda" in where, where
    assert validated_export_scale(npz, prov) == declared


def test_R1042_a_BOOL_SIDECAR_cannot_pass_the_TWO_RECORD_comparison(tmp_path: Path) -> None:
    """The second half: `float(beside)` decided whether the two records AGREE.

    A bool-typed sidecar scale converts to `1.0`, so beside a `1.0` npz key it compared
    EQUAL and R908's disagreement check could not see it. "They agree" is a claim about two
    recorded numbers, and one of them was not one.
    """
    import json as _json

    import numpy as np

    from floatfea.run.config import ConfigError
    from floatfea.run.pipeline import validated_export_scale

    committed = ROOT / "data" / "f4" / "dynamic_inputs.npz"
    raw = np.load(committed, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files}
    flat["froude_lambda"] = np.array(1.0)  # a NUMBER, so the npz branch answers cleanly
    npz = tmp_path / "one.npz"
    np.savez(npz, **flat)
    side = _json.loads(committed.with_suffix(".provenance.json").read_text(encoding="utf-8"))
    side["run"]["lambda"] = True  # float(True) == 1.0 == the npz key, so it "agreed"
    prov = tmp_path / "one.provenance.json"
    prov.write_text(_json.dumps(side), encoding="utf-8")

    assert float(True) == 1.0  # non-vacuous: the conversion really does make them equal
    with pytest.raises(ConfigError) as excinfo:
        validated_export_scale(npz, prov)
    message = str(excinfo.value)
    assert "cannot be compared" in message, message
    assert "True (bool)" in message, message


# --------------------------------------------------------------------------
# FY1 / FY5.1 -- a signed heading is REFUSED and not normalised, over [0, 360].
# FY2 / FY5.2 -- the height pair against lambda, and the derived-height mark.
# --------------------------------------------------------------------------


@pytest.mark.parametrize("value", [360.0, 0.0, 359.999, 180.0])
def test_FY5_1_a_recorded_heading_of_360_is_ACCEPTED(value: float) -> None:
    """The range is CLOSED at both ends, which FY5.1 settled.

    **THIS CELL EXISTS BECAUSE THE CODE SHIPPED HALF-OPEN FOR ONE COMMIT.** FY1's text
    said `[0, 360)`; implemented as worded it refused a recorded `360.0` while a DECLARED
    `headings: [360.0]` stayed accepted and compared modulo 360 under R1100 -- the two
    sides of one quantity disagreeing at exactly one value. FY5.1: "That was my wording,
    not a decision."

    So `360.0` is accepted here, and `test_R872_360_and_0_are_ONE_direction` is what makes
    it mean the direction `0.0` names. Nothing on the comparison path changed.
    """
    lam = float(GOOD["lambda"])
    assert _validated_wave_basis(
        dict(GOOD) | {"heading_deg": value, "wave_height_model_m": 24.2 / lam}, SIDECAR
    )


@pytest.mark.parametrize("value", [-10.0, -0.001, 360.1, 450.0])
def test_FY1_a_SIGNED_or_past_turn_heading_is_refused_with_the_remedy(value: float) -> None:
    """FY1's three requirements of the message, asserted one by one.

    `docs/conventions.md:150` records that the BEM reader converts a heading straight
    through with no sign flip and no offset, so a Capytaine dataset carrying a negative
    `wave_direction` records a negative heading -- a legal direction written with the
    other sign. **FY1 rules REFUSE rather than normalise**, because a signed recording may
    be a sign-convention error in the export and normalising it silently is what would
    hide that.

    `-0.001` is the row that matters most: it is the smallest signed value, a hair below
    the boundary, and it is the one an over-eager `abs()` or a tolerance would let through.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"heading_deg": value}, SIDECAR)
    message = str(caught.value)
    assert f"{value:g} deg" in message, message
    assert "accepted range 0 <= heading <= 360 deg" in message, message
    assert "docs/conventions.md:150" in message, message
    assert f"{value % 360.0:g}" in message, message


def test_FY2_case_D_the_pair_R895_FOUND_is_refused() -> None:
    """R895's own case, through the validator: `24.2 m` full and `100.0 m` model.

    **THIS IS THE STATE THAT PUBLISHED AT EXIT 0.** Both numbers reached `report.md` and
    both CSV headers, beside the correct lambda, describing a sea state that cannot exist
    -- at lambda 50 a 100 m model wave is a 5000 m full-scale wave. Nothing said which of
    the two was wrong, and the contradiction was readable only to someone who did the
    division.

    The ceiling catches it first and the message says the ceiling is DERIVED, which is the
    half of FY2 that makes the bound right rather than merely tighter: a single shared
    `0..100 m` was vacuous by exactly lambda.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"wave_height_model_m": 100.0}, SIDECAR)
    message = str(caught.value)
    assert "run.wave_height_model_m" in message, message
    assert "That ceiling is DERIVED" in message, message
    assert "0..2 m" in message, message


@pytest.mark.parametrize("model", [0.3, 0.6, 0.4839, 0.4841])
def test_FY2_case_C_a_MISMATCHED_pair_is_refused_naming_both(model: float) -> None:
    """A pair that is inside both bounds and still disagrees with lambda.

    **THE CEILING ALONE WOULD NOT CATCH THESE.** Every value here is under the derived
    `2 m`, so a bound on one member of the pair is green on all of them; it is the pair
    CHECK that refuses. `0.4839` and `0.4841` are the rows that say the check is not a
    rounding allowance -- they are a tenth of a millimetre from the recorded `0.484`, and
    `RECORDED_HEIGHT_PAIR_RELATIVE` is `1e-9`.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"wave_height_model_m": model}, SIDECAR)
    message = str(caught.value)
    assert "disagree with the recorded lambda" in message, message
    assert "wave_height_full_m" in message and "wave_height_model_m" in message, message
    assert "RECORDED_HEIGHT_PAIR_RELATIVE" in message, message


def test_FY2_the_COUNTER_is_detected_and_the_committed_pair_is_not() -> None:
    """The declared tolerance and its counter, from the two ends they are declared for.

    `RECORDED_HEIGHT_PAIR_COUNTER` is the smallest pair inconsistency the same assertion
    in the same quantity must DETECT. `RECORDED_HEIGHT_PAIR_RELATIVE` is the width it may
    not detect. Both are asserted here against the committed pair, so neither can be
    widened without this cell saying so -- which is what a counter is for.

    The committed pair's own disagreement is round-off and nothing else: `0.484 * 50` is
    `24.200000000000003`, a relative discrepancy of about `1.5e-16`.
    """
    from floatfea.tolerances import (
        RECORDED_HEIGHT_PAIR_COUNTER,
        RECORDED_HEIGHT_PAIR_RELATIVE,
    )

    full = float(GOOD["wave_height_full_m"])

    # the committed pair, unperturbed: accepted
    assert _validated_wave_basis(dict(GOOD), SIDECAR)

    # perturbed by the COUNTER: refused
    with pytest.raises(ConfigError):
        _validated_wave_basis(
            dict(GOOD) | {"wave_height_full_m": full * (1.0 + RECORDED_HEIGHT_PAIR_COUNTER)},
            SIDECAR,
        )

    # **AND THE COUNTER IS STRICTLY CLEAR OF THE TOLERANCE, constant against constant.**
    # My first version of this line was `> RECORDED_HEIGHT_PAIR_RELATIVE * 100.0`, to say
    # "three decades clear" -- and `tests/test_no_tolerance_literals.py` refused it,
    # correctly: the bound of that comparison is the PRODUCT, so `100.0` is an undeclared
    # factor deciding a comparison, which is a tolerance under another name. HOW FAR apart
    # they are is reasoned in the two `tolerances.py` entries, where a reader can check the
    # reasoning against the quantity; what belongs here is the ORDERING, which is what the
    # two rows above rest on.
    assert RECORDED_HEIGHT_PAIR_COUNTER > RECORDED_HEIGHT_PAIR_RELATIVE


@pytest.mark.parametrize("dropped", ["wave_height_full_m", "wave_height_model_m"])
def test_FY2_ONE_recorded_height_DERIVES_the_other(dropped: str) -> None:
    """FY2's "if only one is recorded, derive the other", and R878 is not reopened.

    **THIS IS ALSO THE SECOND OF THE TWO DEFECTS FY5 ASKS BE PINNED.** Making
    `wave_height_full_m` optional made the type-check loop subscript a key that was no
    longer guaranteed, and it raised `KeyError` out of that line on exactly this path. It
    was found by probing FY2's own "model only" case before any test existed, which is why
    FY5 asks for the row: nothing else in the suite went down this path.

    R878's rule is untouched for the three fields that are one quantity each -- the cell
    above still refuses a sidecar missing `heading_deg`, `lambda` or `window`. The two
    heights are one quantity at two scales, and the dict this returns is COMPLETE whichever
    way it arrived, so R878's own defect -- a `KeyError` after the solve from a consumer
    subscripting a truthy-but-partial dict -- cannot come back through this door.
    """
    partial = {k: v for k, v in GOOD.items() if k != dropped}
    out = _validated_wave_basis(partial, SIDECAR)
    # **EXACT EQUALITY, DELIBERATELY, AND THE DIRECTION OF THE DERIVATION IS WHY IT CAN
    # BE.** This is the natural place for an epsilon and it does not need one: `24.2 / 50`
    # is `0.484` exactly in binary, while `0.484 * 50` is `24.200000000000003`. The
    # derivation runs from whichever height the file recorded, so the reconstructed dict
    # compares equal to the committed one on the nose in both directions -- and an
    # `approx` here would have hidden the day that stopped being true.
    assert out == GOOD, (out, GOOD)


@pytest.mark.parametrize("value", [True, False, float("nan"), float("inf"), "0.5", [0.5]])
def test_FY2_the_MODEL_height_keeps_its_type_and_finiteness_checks(value: object) -> None:
    """The FIRST of the two defects FY5 asks be pinned, by name.

    **`wave_height_model_m` LEFT `RECORDED_BOUNDS` UNDER FY2**, because its ceiling is
    derived from lambda rather than declared. The loop that type-checks every recorded
    number was keyed on that dict, so the field lost its bool, type, overflow and
    finiteness checks in the same edit that tightened its range -- and a model height of
    `true` or `nan` would have published `True m model` in `report.md` at exit 0. That is
    the exact shape R903 found for `rho_inf`, re-created by a repair.

    It was found by probing, not by reading, and no test in the suite covered it. The loop
    now iterates what is PRESENT and range-checks only what has a static bound.
    """
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(dict(GOOD) | {"wave_height_model_m": value}, SIDECAR)
    assert "run.wave_height_model_m" in str(caught.value), str(caught.value)


def test_FY2_BOTH_heights_absent_is_still_PARTIAL() -> None:
    """Deriving from one is not deriving from none.

    FY2 relaxes completeness for the PAIR, not for the quantity: a sidecar recording
    neither height records no wave height at all, and there is nothing to derive from.
    """
    partial = {
        k: v for k, v in GOOD.items() if k not in ("wave_height_full_m", "wave_height_model_m")
    }
    with pytest.raises(ConfigError) as caught:
        _validated_wave_basis(partial, SIDECAR)
    message = str(caught.value)
    assert "PARTIAL wave basis" in message, message
    assert "wave_height_full_m" in message and "wave_height_model_m" in message, message


@pytest.mark.parametrize(
    ("recorded", "expected"),
    [
        (("wave_height_full_m", "wave_height_model_m"), ""),
        (("wave_height_model_m",), "**full scale derived**"),
        (("wave_height_full_m",), "**model scale derived**"),
        ((), ""),
    ],
    ids=["both recorded", "model only", "full only", "no sidecar"],
)
def test_FY5_2_the_report_MARKS_a_derived_height_and_only_then(
    recorded: tuple[str, ...], expected: str
) -> None:
    """FY5.2's three rows, plus the no-sidecar row, on the report clause itself.

    **A RECORDED PAIR PRINTS EXACTLY AS IT PRINTED BEFORE FY5.2**, which is the row that
    protects the golden: the shipped example records both, so `report.md` is byte-identical
    and `results/R1/example/` does not move. The mark appears only where a number was
    derived, and it names which of the two the file carried and the arithmetic that
    produced the other.

    The no-sidecar row is here because an empty provenance set must mean "say nothing"
    rather than "say derived": a run with no sidecar states the basis is NOT RECORDED
    everywhere already, and a derived-height clause there would be a claim about a file
    that does not exist.
    """
    from floatfea.cli import _derived_height_note

    note = _derived_height_note(dict(GOOD), frozenset(recorded))
    if expected:
        assert expected in note, note
        assert "lambda = 50.0" in note, note
    else:
        assert note == "", note
