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
from floatfea.run.pipeline import (  # noqa: F401
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
    assert "outside the declared domain" in str(caught.value), str(caught.value)


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
    assert "outside the declared domain" in message and f"run.{key}" in message, message


@pytest.mark.parametrize("value", [0.0, 100.0, 24.2])
def test_R881_the_WAVE_HEIGHT_domain_is_INCLUSIVE_at_both_ends(value: float) -> None:
    """`WAVE_HEIGHT` is `(0.0, 100.0)` inclusive, as the configured side already is.

    A calm sea is `0.0` m and the bound admits it; the refusal above is about values no
    declaration could express, not about small ones.
    """
    assert _validated_wave_basis(dict(GOOD) | {"wave_height_full_m": value}, SIDECAR)


def test_R881_EVERY_numeric_recorded_field_HAS_a_declared_domain() -> None:
    """The shape of the defect, not the two instances of it.

    R881 was a field carrying a type check and no domain. A fifth field added to
    `WAVE_BASIS_KEYS` with a type check and no entry in `RECORDED_BOUNDS` would be the
    same defect again, and nothing above would notice: the cases are keyed on the names
    that exist today.
    """
    from floatfea.run.pipeline import RECORDED_BOUNDS, WAVE_BASIS_KEYS

    numeric = [k for k in WAVE_BASIS_KEYS if not isinstance(GOOD[k], str)]
    assert set(numeric) == set(RECORDED_BOUNDS), (
        f"these recorded numeric fields have no declared domain: "
        f"{sorted(set(numeric) - set(RECORDED_BOUNDS))}"
    )
    for key, (unit, low, high) in RECORDED_BOUNDS.items():
        assert low < high and unit, (key, unit, low, high)


@pytest.mark.parametrize("missing", list(GOOD))
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
    """`FROUDE_LAMBDA` is `(1.0, 1000.0)` inclusive, and 50 is the committed export."""
    assert _validated_wave_basis(dict(GOOD) | {"lambda": value}, SIDECAR)


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

    partial = {k: v for k, v in GOOD.items() if k != "wave_height_full_m"}
    sidecar.write_text(_json.dumps({"run": partial}), encoding="utf-8")
    with pytest.raises(ConfigError) as caught:
        exported_wave_basis(npz)
    assert "PARTIAL wave basis" in str(caught.value), str(caught.value)

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
