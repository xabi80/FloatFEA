"""The configuration refuses what it cannot honour, with a message (FL1(a)).

`CLAUDE.md`: "Never let a validation failure degrade to a warning. The reader rejects bad
records." Every case here asserts a REFUSAL and asserts that the message names the thing
the reader has to change -- a refusal that says "invalid configuration" and nothing else
sends someone back to the source to find out which field.

**THE SILENT-ACCEPTANCE CASES ARE THE POINT.** A bad number is easy: it is out of range
and the range is declared. The dangerous shapes are the ones a lenient parser would
accept and then not use -- a misspelled field, a mass total the deck owns, a code option
this tool does not implement, a per-body fraction the builder cannot express. Each of
those would produce a run whose report describes a configuration that was not run, which
is the failure mode this project exists to prevent.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.basis import FY_S355
from floatfea.run.config import (
    WAVE_PERIOD,
    ConfigError,
    _NoDuplicateLoader,
    checked_recorded_periods,
    is_recorded_number,
    load_config,
)

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"


def _example() -> dict[str, Any]:
    """The shipped example, as a mutable mapping to damage one field at a time."""
    loaded = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    assert isinstance(loaded, dict)
    return loaded


def _absolutise(data: dict[str, Any]) -> dict[str, Any]:
    """Resolve the configuration's paths, so the file can live anywhere.

    A configuration's relative paths resolve against ITS OWN directory, which is the
    behaviour `test_relative_paths_resolve_against_THE_CONFIG_FILE` pins. That is exactly
    why a damaged copy cannot simply be written to `tmp_path` and left relative: it would
    fail on the deck path, and every refusal below would pass without testing anything.

    Resolving here against the real example's directory keeps the fixtures out of the
    tracked source tree. Writing them next to the example worked -- the teardown removed
    them -- but a test that dies mid-run would leave a stray in a tracked directory.
    """
    # **A NON-STRING PATH IS PASSED THROUGH UNTOUCHED (R837).** `base / value` raises
    # `TypeError: unsupported operand type(s) for /: 'WindowsPath' and 'bool'`, so a
    # fixture that absolutises unconditionally kills the test before `load_config` is
    # reached -- and the case under test is precisely a path field that is not a string.
    # Leaving it alone is what lets the SCHEMA refuse it, which is the thing being checked.
    out = copy.deepcopy(data)
    for block, key in (("floatsim", "deck"), ("load_cases", "npz"), ("outputs", "directory")):
        value = out.get(block, {}).get(key)
        # **AND A BLANK STRING IS PASSED THROUGH TOO (R843).** `(EXAMPLE.parent / "")`
        # resolves to the examples directory, so absolutising a blank turned the case
        # under test into a perfectly good absolute path and the refusal never fired. A
        # blank directory IS the input R843 is about, so it has to reach `load_config`
        # unchanged -- the same reason a non-string does.
        if isinstance(value, str) and value.strip():
            out[block][key] = str((EXAMPLE.parent / value).resolve())
    return out


@pytest.fixture
def cfg_path(tmp_path: Path) -> Any:
    """A per-test configuration, written to `tmp_path` with absolute inner paths."""

    def make(data: dict[str, Any]) -> Path:
        path = tmp_path / "config.yaml"
        path.write_text(yaml.safe_dump(_absolutise(data), sort_keys=False), encoding="utf-8")
        return path

    return make


def test_the_shipped_example_loads(cfg_path: Any) -> None:
    """The control. Without it every refusal below could be refusing for free."""
    cfg = load_config(EXAMPLE)
    assert cfg.load_cases.governing_periods == (12.5, 14.0, 15.0, 16.2)
    # AGAINST THE DECLARED CONSTANT, NOT A LITERAL. `tests/test_no_tolerance_literals.py`
    # flagged `== 355000000.0` here and offered a `# not-a-tolerance:` annotation. The
    # literal is not a tolerance -- it is a yield stress, an input -- but naming the
    # constant is better than annotating it: this now also fails if the example and the
    # grade `floatfea.basis` declares ever drift apart, which an annotated literal could
    # not notice.
    assert cfg.sections.material.fy == FY_S355
    assert set(cfg.mass_distribution) == {"platform", "hub1", "hub2", "hub3", "hub4"}
    assert cfg.code_check.one_third_increase is False


# ---------------------------------------------------------------------------
# Out-of-range units
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("field", "value", "needle"),
    [
        ("E", 210.0, "outside the admissible range"),
        ("E", 2.1e15, "outside the admissible range"),
        ("rho", 0.0, "outside the admissible range"),
        ("Fy", 355.0, "outside the admissible range"),
    ],
)
def test_a_material_value_outside_its_range_is_REFUSED(
    cfg_path: Any, field: str, value: float, needle: str
) -> None:
    """`E: 210` is GPa typed into a Pa field, and it is the mistake worth catching.

    Parametrised one value per case: a single assertion over a list would report the
    first and hide the rest.
    """
    data = _example()
    data["sections"]["material"][field] = value
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert needle in message, message
    assert (
        f"material.{field}" in message
    ), f"the refusal must name the field the reader has to change; got: {message}"


def test_a_wall_thicker_than_its_own_radius_is_REFUSED(cfg_path: Any) -> None:
    """D/2 <= t is a solid or inverted tube, and `Section.circular_tube` would raise.

    Caught at the schema instead, so the message is about the configuration rather than
    about an internal constructor the reader did not call.
    """
    data = _example()
    data["sections"]["groups"]["platform"] = {"d_outer": 2.5, "wall": 1.3}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "half the outer diameter" in str(caught.value), caught.value


def test_a_NaN_is_REFUSED_rather_than_passing_every_comparison(cfg_path: Any) -> None:
    """`.nan` passes `low <= x <= high` by being false either way, so it is caught first.

    This is not hypothetical: a bare `low <= got <= high` check admits NaN silently, and
    a NaN section property propagates into every force in the run.
    """
    data = _example()
    data["sections"]["material"]["E"] = float("nan")
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "NaN is not a value" in str(caught.value), caught.value


def test_a_STRING_where_a_number_belongs_is_REFUSED(cfg_path: Any) -> None:
    """`Fy: "355 MPa"` is a unit written into a value, and YAML keeps it as a string."""
    data = _example()
    data["sections"]["material"]["Fy"] = "355 MPa"
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "expected a number" in str(caught.value), caught.value


def test_a_BOOLEAN_is_not_accepted_as_a_number(cfg_path: Any) -> None:
    """`True` is an `int` in Python, so `isinstance(value, int)` admits it.

    `f: true` would otherwise become `f = 1.0` -- the whole body mass on the members --
    and the run would report a fraction nobody declared.
    """
    data = _example()
    data["mass_distribution"]["platform"] = {"f": True}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "expected a number" in str(caught.value), caught.value


# ---------------------------------------------------------------------------
# Shapes a lenient parser would accept and then not use
# ---------------------------------------------------------------------------
def test_an_UNRECOGNISED_field_is_REFUSED_not_ignored(cfg_path: Any) -> None:
    """`fy` where `Fy` is meant would run at the default and report the default."""
    data = _example()
    data["sections"]["material"]["fy"] = 420000000.0
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "unrecognised field" in message, message
    assert "'fy'" in message, message


def test_a_BODY_TOTAL_in_the_config_is_REFUSED(cfg_path: Any) -> None:
    """FL1(a): body totals, CoG and inertia come FROM THE DECK.

    Accepting and ignoring a declared mass is the single most dangerous thing this
    schema could do, so it is named explicitly rather than caught as an unknown field.
    """
    data = _example()
    data["mass_distribution"]["platform"] = {"f": 0.75, "mass": 2.4e6}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "come FROM THE DECK" in message, message


@pytest.mark.parametrize("key", ["cog", "inertia", "total_mass"])
def test_every_deck_owned_quantity_is_REFUSED_by_name(cfg_path: Any, key: str) -> None:
    data = _example()
    data["mass_distribution"]["hub1"] = {"f": 0.75, key: [0.0, 0.0, 0.0]}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert key in str(caught.value), caught.value


def test_BOTH_mass_modes_at_once_is_REFUSED(cfg_path: Any) -> None:
    """`f` and an explicit distribution say the same thing twice, possibly differently."""
    data = _example()
    data["mass_distribution"]["platform"] = {"f": 0.75, "line_masses": {"platform": 9375.0}}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "will not guess which" in str(caught.value), caught.value


def test_a_LUMPED_MASS_WITHOUT_A_POSITION_is_REFUSED(cfg_path: Any) -> None:
    """FL1(a) asks for positions; a mass with nowhere to go cannot be placed."""
    data = _example()
    data["mass_distribution"]["platform"] = {"lumped": [{"label": "winch", "mass": 1000.0}]}
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "required field 'at' is missing" in str(caught.value), caught.value


def test_a_MISSING_SECTION_is_REFUSED(cfg_path: Any) -> None:
    data = _example()
    del data["sections"]
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "required section 'sections' is missing" in str(caught.value), caught.value


def test_BOTH_npz_AND_cases_is_REFUSED(cfg_path: Any) -> None:
    """One says use this file, the other says produce one. Ambiguous, so refused."""
    data = _example()
    data["load_cases"]["cases"] = [{"heading": 0.0, "H": 24.2, "T": 12.5}]
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "exactly one of" in str(caught.value), caught.value


def test_an_EMPTY_governing_period_list_is_REFUSED(cfg_path: Any) -> None:
    """With no declared governing set, any case could govern silently."""
    data = _example()
    data["load_cases"]["governing_periods"] = []
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "non-empty list" in str(caught.value), caught.value


def test_a_REPEATED_governing_period_is_REFUSED(cfg_path: Any) -> None:
    """A period counted twice would weight one case twice in the envelope."""
    data = _example()
    data["load_cases"]["governing_periods"] = [12.5, 12.5, 15.0]
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "contains a repeat" in str(caught.value), caught.value


def test_a_MISSING_DECK_is_REFUSED_with_the_path(cfg_path: Any) -> None:
    data = _example()
    data["floatsim"]["deck"] = "../data/platform/does_not_exist.yaml"
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "does not exist" in message and "does_not_exist.yaml" in message, message


def test_a_NON_BOOLEAN_one_third_increase_is_REFUSED(cfg_path: Any) -> None:
    """Section 3.1.2's increase is on or off, not scaled."""
    data = _example()
    data["code_check"]["one_third_increase"] = 0.5
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "expected true or false" in str(caught.value), caught.value


def test_relative_paths_resolve_against_THE_CONFIG_FILE(cfg_path: Any) -> None:
    """So a configuration means the same thing wherever it is run from.

    Asserted on the resolved absolute paths, because resolving against the working
    directory is the kind of bug that works for everyone who runs from the repo root and
    fails for everyone else.
    """
    cfg = load_config(EXAMPLE)
    assert cfg.floatsim.deck.is_absolute() and cfg.floatsim.deck.is_file()
    assert cfg.floatsim.deck == (ROOT / "data" / "platform" / "platform12_deck.yaml")
    # FT2.6: a bare string is a ONE-element tuple, which is the whole of the
    # scalar-or-list door -- the field is always plural so no caller sees a union.
    assert cfg.load_cases.npz_files == ((ROOT / "data" / "f4" / "dynamic_inputs.npz"),)
    assert cfg.outputs.directory == (ROOT / "results" / "R1" / "example")


# ---------------------------------------------------------------------------
# FQ2: the loader repairs, each held by a test that fails when it is reverted
# ---------------------------------------------------------------------------
#
# **R826 IS WHY THESE EXIST.** R822's and R823's repairs shipped with nothing holding
# them: the reviewer reverted both halves and the suite stayed green, because the only
# duplicate-key cases in the tree were TEXT-IDENTICAL ones (`Fy` twice, `platform.f`
# twice, `K` twice) which are caught by either keying. I had demonstrated the five typing
# classes by hand, pasted the output into a commit message, and never turned the
# demonstration into a gate.


@pytest.mark.parametrize(
    ("label", "document"),
    [
        ("no / No", "{no: 1, No: 2}"),
        ("yes / true", "{yes: 1, true: 2}"),
        ("tilde / null", "{~: 1, null: 2}"),
        ("1 / 01", "{1: 1, 01: 2}"),
        ("1.0 / 1.00", "{1.0: 1, 1.00: 2}"),
    ],
)
def test_FQ2_R822_YAML_TYPING_collapses_are_REFUSED(label: str, document: str) -> None:
    """Two keys YAML's implicit typing makes equal are a duplicate (R822).

    One case per class, because the five are different productions of the YAML 1.1 schema
    -- booleans, nulls, integers with a leading zero, and floats with trailing zeros -- and
    a loader fixed for one is not fixed for another.

    The COUNT check is what catches these: the text differs, so the text check cannot.
    """
    with pytest.raises(ConfigError) as caught:
        yaml.load(document, _NoDuplicateLoader)
    message = str(caught.value)
    assert "became" in message and "THE SAME KEY" in message, (label, message)


def test_FQ2_R822_the_TEXT_IDENTICAL_control_still_names_its_key_and_line() -> None:
    """The text check survives the count check and still gives the better message.

    Both checks would refuse `{a: 1, a: 2}`. The text one runs first because it can name
    the key and the line, which is what a reader fixes the file with; the count check can
    only say that two of them collapsed.
    """
    with pytest.raises(ConfigError) as caught:
        yaml.load("{a: 1, a: 2}", _NoDuplicateLoader)
    message = str(caught.value)
    assert "duplicate key 'a'" in message and "line 1" in message, message


def test_FQ2_R822_a_CLEAN_document_still_loads() -> None:
    """The control. Nested mappings and repeated keys at DIFFERENT depths are legal."""
    got = yaml.load("{a: {b: 1, c: 2}, d: {b: 3}}", _NoDuplicateLoader)
    assert got == {"a": {"b": 1, "c": 2}, "d": {"b": 3}}


def test_FQ2_R823_a_MERGE_KEY_is_REFUSED() -> None:
    """`<<` is refused with a message (R823).

    It went from a hard `ConstructorError` to WORKING as a side effect of routing mapping
    construction through a custom constructor, and merged keys bypass the duplicate check
    entirely because `flatten_mapping` runs inside `construct_mapping`, after the loop.
    """
    document = "base: &b {x: 1}" + chr(10) + "use:" + chr(10) + "  <<: *b" + chr(10) + "  y: 2"
    with pytest.raises(ConfigError) as caught:
        yaml.load(document, _NoDuplicateLoader)
    message = str(caught.value)
    assert "merge key" in message and "bypasses the duplicate-key check" in message, message


def _at_line_masses(data: dict[str, Any], keys: Any) -> None:
    """`mass_distribution.<body>.line_masses` -- a mass per member group."""
    data["mass_distribution"]["platform"] = {"line_masses": keys}


def _at_sections_groups(data: dict[str, Any], keys: Any) -> None:
    """`sections.groups` -- THE SITE WHERE THE COLLAPSED VALUE IS A STIFFNESS (R833)."""
    data["sections"]["groups"] = keys


def _at_body_names(data: dict[str, Any], keys: Any) -> None:
    """`mass_distribution` itself -- the BODY names."""
    data["mass_distribution"] = keys


_TUBE = {"d_outer": 2.5, "wall": 0.18}

# THE CALL SITE IS A PARAMETER, WHICH IS R833's WHOLE CONTENT. The check was installed at
# three sites and held at one, and the one it was held at is the one the cycle chose. A
# finding that names sites is closed SITE BY SITE, so the site is an axis here.
_NAME_KEY_SITES = (
    ("line_masses", _at_line_masses, 100.0),
    ("sections.groups", _at_sections_groups, _TUBE),
    ("mass_distribution body names", _at_body_names, {"f": 0.75}),
)

_NAME_KEY_SHAPES = (
    ("bool and quoted bool", (True, "True")),
    ("null and quoted null", (None, "None")),
    ("a bare number", (1,)),
    ("a bare word", (False,)),
)


@pytest.mark.parametrize(
    ("site_label", "place", "value"), _NAME_KEY_SITES, ids=[s[0] for s in _NAME_KEY_SITES]
)
@pytest.mark.parametrize(
    ("shape_label", "keys"), _NAME_KEY_SHAPES, ids=[s[0] for s in _NAME_KEY_SHAPES]
)
def test_FQ2_R825_a_NON_STRING_NAME_KEY_is_REFUSED(
    cfg_path: Any,
    site_label: str,
    place: Any,
    value: Any,
    shape_label: str,
    keys: tuple[Any, ...],
) -> None:
    """A name key must be a string, AT EVERY CALL SITE (R825 / FQ1 / R833).

    **THE LAYER BELOW R822, WHICH R822's REPAIR DID NOT REACH.** PyYAML keeps the bool
    `True` and the string `'True'` as DISTINCT keys, so the count check is correctly
    silent -- and the schema then coerced both with `str()`, so one of two declared line
    masses vanished.

    **AND R833 IS WHY THE SITE IS A PARAMETER.** The first version of this test drove
    `line_masses` only. Measured by removing one call-site line at a time against a
    baseline of 171:

        `_require_name_keys(lines, ...)`      removed   4 failed, 167 passed
        `_require_name_keys(groups_raw, ...)` removed   171 passed      <- unheld
        `_require_name_keys(block, where)`    removed   171 passed      <- unheld

    `sections.groups` is the site verdict 5 ranked higher, because the value that
    disappears there is a STIFFNESS: two declared tubes become one with no message, and
    FL2(a) makes the group labels user-chosen.
    """
    data = _example()
    place(data, {k: value for k in keys})
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "are not strings" in message, (site_label, shape_label, message)
    assert "Quote the name" in message, (site_label, shape_label, message)


@pytest.mark.parametrize(
    ("site_label", "place", "value"), _NAME_KEY_SITES, ids=[s[0] for s in _NAME_KEY_SITES]
)
def test_FQ2_R825_a_STRING_name_key_LOADS_at_every_site(
    cfg_path: Any, site_label: str, place: Any, value: Any
) -> None:
    """The control PER SITE, so none of the refusals above is refusing everything there."""
    data = _example()
    place(data, {"platform": value})
    load_config(cfg_path(data))


@pytest.mark.parametrize(
    ("label", "place"),
    [
        ("lumped[].label", "lumped"),
        ("floatsim.tag", "tag"),
        ("load_cases.window_rule", "window_rule"),
        # R837: THE PATH STRINGS, WHICH ARE THE SAME CLASS WRAPPED IN `Path(...)`.
        # `outputs.directory` is the one the three EZ0 deliverables are written to.
        ("outputs.directory", "directory"),
        ("floatsim.deck", "deck"),
        ("load_cases.npz", "npz"),
    ],
)
def test_FQ2_R834_a_DECLARED_STRING_FIELD_refuses_a_non_string(
    cfg_path: Any, label: str, place: str
) -> None:
    """A declared string is a string, or it is refused (R834).

    **THE SCALAR HALF, AND THE COERCION FQ1 ORDERED DELETED SURVIVED AT THREE OF THEM.**
    `LumpedMass.label` is the only identifier a point mass has, and measured before the
    repair through the real `load_config`, two labels the reader distinguished arrived as
    one:

        LOADED. lumped labels: ["True", "True"]

    The reviewer named `lumped[].label`. `tag` and `window_rule` coerce the same way and
    both reach PUBLISHED provenance, so `tag: no` would publish `False` as the FloatSim
    tag -- which is why the site is a parameter here rather than one case.

    **AND IT WAS STILL ONE SITE SHORT, WHICH IS R837.** The census command that reported
    the class closed was a needle anchored on `= str(`, which requires `str(`
    immediately after the `=` and
    therefore cannot see `Path(str(...))`. Three sites hid behind that needle. Measured
    through the real `load_config`:

        outputs.directory: no   ->  Path("False")   LOADED
        outputs.directory: 12   ->  Path("12")      LOADED
        outputs.directory: ~    ->  Path("None")    LOADED

    `outputs.directory` is where the three published deliverables are WRITTEN, and four
    lines below it `known[1:]` refuses all five of its sibling flags by name. So the one
    key in that block which took a boolean silently was the one naming a directory.
    """
    data = _example()
    if place == "lumped":
        data["mass_distribution"]["platform"] = {
            "lumped": [
                {"label": True, "mass": 1000.0, "at": [0.0, 0.0, 0.0]},
                {"label": "True", "mass": 2000.0, "at": [1.0, 0.0, 0.0]},
            ]
        }
    elif place == "tag":
        data["floatsim"]["tag"] = False
    elif place == "window_rule":
        data["load_cases"]["window_rule"] = 1
    elif place == "directory":
        # `no` is the typo this block invites: FIVE of its five siblings are booleans in
        # the shipped example -- `report`, `member_forces_csv`, `utilisation_csv`,
        # `required_section`, `truss_sizing`, all written and all bool -- and every one of
        # them refuses a non-bool by name. R844: the `THREE` here was verdict 7's figure,
        # pasted into two shipped files without re-measurement.
        data["outputs"]["directory"] = False
    elif place == "deck":
        data["floatsim"]["deck"] = False
    else:
        data["load_cases"]["npz"] = 1
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "is not a string" in message, (label, message)
    assert "Quote the name" in message, (label, message)


@pytest.mark.parametrize("value", ["", "   ", "	"], ids=["empty", "spaces", "tab"])
def test_R843_an_EMPTY_outputs_directory_is_REFUSED(cfg_path: Any, value: str) -> None:
    """A directory that names nothing is refused (R843), EH4's weakening direction.

    `_require_string` closed R837 by refusing a non-string -- and it admits `""`. Then
    `base / Path("")` is `base`, so `directory: ""` resolved to the CONFIGURATION FILE's
    OWN directory. Measured before the check, on the shipped example:

        directory: ''     LOADED -> <repo>/examples
        directory: '   '  LOADED -> <repo>/examples

    `examples/` is TRACKED, so `floatfea run` would have written the three published
    deliverables into the source tree. This is the direction that WEAKENS the refusal --
    the one EH4 says is solved too -- and it was open because R837 was solved only from
    the side that makes the gate look strong.
    """
    data = _example()
    data["outputs"]["directory"] = value
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    assert "empty directory name" in str(caught.value), str(caught.value)


def test_R843_a_NAMED_relative_directory_still_loads(cfg_path: Any) -> None:
    """The control: the refusal is about a directory that names NOTHING, not about
    relative paths, which `test_relative_paths_resolve_against_THE_CONFIG_FILE` pins."""
    data = _example()
    data["outputs"]["directory"] = "../results/R1/example"
    cfg = load_config(cfg_path(data))
    assert cfg.outputs.directory.name == "example", cfg.outputs.directory


def test_FQ2_R834_two_QUOTED_labels_stay_two(cfg_path: Any) -> None:
    """The control: the repair refuses the collapse, it does not refuse labels."""
    data = _example()
    data["mass_distribution"]["platform"] = {
        "lumped": [
            {"label": "fore", "mass": 1000.0, "at": [0.0, 0.0, 0.0]},
            {"label": "aft", "mass": 2000.0, "at": [1.0, 0.0, 0.0]},
        ]
    }
    cfg = load_config(cfg_path(data))
    assert [m.label for m in cfg.mass_distribution["platform"].lumped] == ["fore", "aft"]


# ---------------------------------------------------------------------------
# R1019 / R1022: THE RECORDED PERIOD HAS THE DECLARED PERIOD DOMAIN, THROUGH ONE DOOR
#
# `_checked` holds every period a CONFIGURATION declares to `WAVE_PERIOD`. The same
# quantity also arrives RECORDED -- `periods_full_s` in the npz, and the sidecar copy of
# it -- and that side was read with a bare `tuple(float(x) for x in ...)`. R1019 put the
# check at ONE reader; R1022 made it a function and gave it the two it had missed. Whether
# those are every reader is not claimed here and is not asserted anywhere -- see the note
# in `checked_recorded_periods`, which says so rather than implying completeness.


# The recorded period the reviewer's own arm published a BREAKING sensitivity row at, at
# exit 0 (R1022). It is an INPUT to every cell below: what is asserted about it is that
# the declared domain EXCLUDES it, never that two computed numbers agree to within it.
_REFUSED_PERIOD_S = 0.5


def test_R1022_the_DOOR_admits_the_DECLARED_RANGE_and_refuses_both_ENDS() -> None:
    """Both directions (EH4), and the edges are inclusive exactly as `_checked` has them."""
    unit, low, high = WAVE_PERIOD
    assert checked_recorded_periods([low, 12.5, high], "x.npz: `periods_full_s`") == (
        low,
        12.5,
        high,
    )
    for bad in (0.5, 0.0, -12.5, low * 0.999, high * 1.001):
        with pytest.raises(ConfigError) as excinfo:
            checked_recorded_periods([10.0, bad], "x.npz: `periods_full_s`")
        message = str(excinfo.value)
        assert "1 of 2 recorded periods are not admissible" in message, message
        assert f"index 1: {bad:g} {unit}" in message, message
        assert f"[{low:g}, {high:g}]" in message, message


def test_R1022_the_DOOR_names_EVERY_offending_index_not_just_the_first() -> None:
    """A re-export has to be aimed at the whole list, not at one entry at a time."""
    with pytest.raises(ConfigError) as excinfo:
        checked_recorded_periods([0.5, 12.5, 500.0], "x.npz: `periods_full_s`")
    message = str(excinfo.value)
    assert "2 of 3 recorded periods" in message, message
    assert "index 0: 0.5 s" in message, message
    assert "index 2: 500 s" in message, message


def test_R1022_the_DOOR_refuses_what_is_NOT_A_NUMBER_rather_than_converting_it() -> None:
    """NaN passes every comparison; text converts; a 401-digit integer overflows.

    Each of the three is an input accepted and used other than as declared (FR1 head two)
    if it gets past here, and the last is R883 arriving at a second field.
    """
    for bad, needle in (
        (float("nan"), "NaN is not a value"),
        ("12.5", "is not a recorded number"),
        (True, "is not a recorded number"),
        (10**400, "is not a period"),
        # **BP0: `None` MOVED CLASSIFICATION WITH R1033.** It used to be caught by
        # `float(None)` raising, and is now caught by the positive type gate before any
        # conversion is attempted -- a better refusal, and a different sentence.
        (None, "is not a recorded number"),
    ):
        with pytest.raises(ConfigError) as excinfo:
            checked_recorded_periods([10.0, bad], "x.npz: `periods_full_s`")
        assert needle in str(excinfo.value), (bad, str(excinfo.value))

    # And the 401-digit integer does not BECOME the message (it is capped).
    with pytest.raises(ConfigError) as excinfo:
        checked_recorded_periods([10**400], "x.npz: `periods_full_s`")
    assert "(401 characters)" in str(excinfo.value), str(excinfo.value)
    assert len(str(excinfo.value)) < 1000, len(str(excinfo.value))


def test_R1022_the_DOOR_refuses_something_that_is_not_a_SEQUENCE() -> None:
    """A scalar where an array belongs: `float(x) for x in 5` is a TypeError traceback."""
    with pytest.raises(ConfigError) as excinfo:
        checked_recorded_periods(5, "x.npz: `periods_full_s`")
    assert "cannot be iterated" in str(excinfo.value), str(excinfo.value)
    # The weakening direction: an EMPTY sequence is not an error here. Whether a file may
    # record zero cases is `refuse_cases_that_cannot_govern`, which asks a different
    # question; this door states a domain and an empty list satisfies it vacuously.
    assert checked_recorded_periods([], "x.npz: `periods_full_s`") == ()


def test_R1022_the_COMMITTED_ARRAY_and_SIDECAR_are_both_ADMITTED() -> None:
    """The weakening direction on the files this repository ships, both readers of them."""
    import json

    import numpy as np

    raw = np.load(ROOT / "data" / "f4" / "dynamic_inputs.npz", allow_pickle=False)
    from_npz = checked_recorded_periods(raw["periods_full_s"], "committed npz")
    recorded = json.loads(
        (ROOT / "data" / "f4" / "dynamic_inputs.provenance.json").read_text(encoding="utf-8")
    )
    from_sidecar = checked_recorded_periods(recorded["run"]["periods_full_s"], "committed sidecar")
    assert from_npz == from_sidecar, (from_npz, from_sidecar)
    assert len(from_npz) == 6, from_npz
    # NON-VACUOUS: the domain does not contain everything a recorded float could be.
    unit, low, high = WAVE_PERIOD
    # The assertion is about `WAVE_PERIOD`'s EXTENT -- that the domain does not contain
    # everything a recorded float could be -- and `_REFUSED_PERIOD_S` is the input it is
    # measured against, declared once at module scope with what it is.
    assert not (
        # not-a-tolerance: `_REFUSED_PERIOD_S` is a recorded INPUT -- the period the
        # reviewer's arm published a BREAKING row at -- and this asserts the declared
        # domain's EXTENT, that it does not contain everything a recorded float could be.
        # No two computed numbers are compared, and widening the domain to admit it would
        # turn the door off rather than turn a red green.
        low
        <= _REFUSED_PERIOD_S
        <= high
    ), WAVE_PERIOD
    assert unit == "s", WAVE_PERIOD


# ---------------------------------------------------------------------------
# R1033: THE TYPE GATE LISTED THE FORBIDDEN TYPES AND THE LIST COULD NOT BE COMPLETED
#
# Both gates for the R825 family tested `isinstance(value, (bool, str, bytes))` -- the
# python types a JSON sidecar can produce. The npz readers receive numpy scalars, and
# `np.bool_` is NOT a `bool` subclass although `np.str_` IS a `str` one, so `np.True_`
# reached `float()` and was admitted as `1.0` at every index.


@pytest.mark.parametrize(
    "spelling, value, admitted",
    [
        pytest.param("python float", 12.5, True, id="python_float"),
        pytest.param("python int", 12, True, id="python_int"),
        pytest.param("python bool", True, False, id="python_bool"),
        pytest.param("python str", "12.5", False, id="python_str"),
        pytest.param("python bytes", b"12.5", False, id="python_bytes"),
        pytest.param("python complex", 10 + 0j, False, id="python_complex"),
        pytest.param("None", None, False, id="none"),
        pytest.param("numpy float64", np.float64(12.5), True, id="numpy_float64"),
        pytest.param("numpy float32", np.float32(12.5), True, id="numpy_float32"),
        pytest.param("numpy int64", np.int64(12), True, id="numpy_int64"),
        pytest.param("numpy bool_", np.True_, False, id="numpy_bool_"),
        pytest.param("numpy complex128", np.complex128(10 + 0j), False, id="numpy_complex128"),
        pytest.param("numpy str_", np.str_("12.5"), False, id="numpy_str_"),
        pytest.param("zero-dim float array", np.array(12.5), True, id="zero_dim_array"),
        pytest.param("zero-dim bool array", np.array(True), False, id="zero_dim_bool_array"),
    ],
)
def test_R1033_the_RECORDED_NUMBER_test_decides_EVERY_spelling(
    spelling: str, value: Any, admitted: bool
) -> None:
    """One decision, both spellings, every dtype kind a recorded field can arrive as.

    The two it exists for are `numpy bool_` and `numpy complex128`: the first was admitted
    as `1.0` and the second as `10.0` with nothing but a `ComplexWarning`. The zero-dim
    arms are the spelling `refuse_disagreeing_period_records` receives.

    `numpy` is imported at MODULE scope because `pytest.param` arguments are evaluated at
    collection time -- the first draft of this cell passed the spellings as strings and
    `eval`-ed them here, which is a worse answer than an import.
    """
    assert is_recorded_number(value) is admitted, (spelling, type(value).__name__)


def test_R1033_numbers_Real_ALONE_WOULD_REFUSE_THE_COMMITTED_FILE() -> None:
    """**THE OTHER REPAIR THE VERDICT OFFERED BREAKS ONE OF THE TWO SITES**, measured.

    The condition allowed "`numbers.Real` with booleans excluded, or `np.issubdtype` on the
    dtype". The two callers receive DIFFERENT spellings of the same quantity: the top-level
    array is subscripted, so its elements are `np.float64` and `numbers.Real` is True; the
    per-case second record is read whole and is a ZERO-DIMENSIONAL array, for which
    `numbers.Real` is False. A `numbers.Real`-only gate would refuse the file this
    repository ships, at `refuse_disagreeing_period_records`, on its next run.

    This cell is what stops the dtype test being "simplified" to the shorter one later.
    """
    import numbers

    import numpy as np

    raw = np.load(ROOT / "data" / "f4" / "dynamic_inputs.npz", allow_pickle=False)
    second = raw["case0/period_full_s"]
    element = raw["periods_full_s"][0]

    assert second.ndim == 0 and second.dtype.kind == "f", (second.ndim, second.dtype)
    assert isinstance(second, numbers.Real) is False, type(second).__name__
    assert isinstance(element, numbers.Real) is True, type(element).__name__
    # AND THE TEST THAT SHIPPED ADMITS BOTH, which is the property the shorter one loses.
    assert is_recorded_number(second) and is_recorded_number(element)


def test_R1033_the_DOOR_refuses_the_two_it_was_admitting() -> None:
    """`np.True_` as `1.0` and `np.complex128(10+0j)` as `10.0`, both at exit 0 before."""
    import numpy as np

    for probe in (np.True_, np.complex128(10 + 0j), np.str_("12.5")):
        with pytest.raises(ConfigError) as excinfo:
            checked_recorded_periods([probe] * 2, "x.npz: `periods_full_s`")
        message = str(excinfo.value)
        assert "2 of 2 recorded periods are not admissible" in message, message
        assert "is not a recorded number" in message, message
    # THE WEAKENING DIRECTION: the committed array is still admitted, whole.
    #
    # The expected tuple is DERIVED from the file rather than typed. This cell's property
    # is that the array is ADMITTED, not what the six values are -- those are pinned by
    # `test_R1019_the_COMMITTED_array_is_INSIDE_the_declared_range` and by
    # `test_R1005_the_COMMITTED_npz_carries_the_SECOND_RECORD_for_EVERY_CASE`. Typing them
    # here would be a third copy that goes stale if the pair is ever re-exported, which is
    # the same mistake the `50.0` in `test_headings_and_bem_coverage.py` was.
    raw = np.load(ROOT / "data" / "f4" / "dynamic_inputs.npz", allow_pickle=False)
    expected = tuple(float(x) for x in raw["periods_full_s"])
    assert checked_recorded_periods(raw["periods_full_s"], "committed") == expected
    assert len(expected) == 6, expected  # non-vacuous: the array is not empty


# ---------------------------------------------------------------------------
# FT2.4: `sections.candidates`, the declared grid FM0's loop steps through
#
# `docs/milestones/R1.md` section 4 is where the grid comes from -- "the candidate grid is
# the config's declared section list" -- and it is also why the loop needs no tolerance:
# it terminates on a list the configuration wrote rather than on a convergence threshold,
# and FM0 forbids the tool extending it.


def _sections_with(candidates: object) -> dict:
    """The shipped example's `sections` block with a `candidates` key bolted on."""
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    block = copy.deepcopy(data["sections"])
    block["candidates"] = candidates
    return block


def test_FT2_4_a_declared_grid_is_PARSED_in_order() -> None:
    """Declaration order is preserved, and every entry goes through the tube door."""
    from floatfea.run.config import _parse_sections

    parsed = _parse_sections(
        _sections_with(
            {
                "platform": [
                    {"d_outer": 2.5, "wall": 0.18},
                    {"d_outer": 2.5, "wall": 0.30},
                    {"d_outer": 3.0, "wall": 0.30},
                ]
            }
        )
    )
    grid = parsed.candidates["platform"]
    assert [c.wall for c in grid] == [0.18, 0.30, 0.30]
    assert [c.d_outer for c in grid] == [2.5, 2.5, 3.0]
    # The default is EMPTY, which is what every configuration before FT2.4 declares, and
    # what `required_section: false` needs it to be.
    assert (
        _parse_sections(yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))["sections"]).candidates
        == {}
    )


@pytest.mark.parametrize(
    "candidates, needle",
    [
        pytest.param(
            {"spar": [{"d_outer": 2.5, "wall": 0.18}]},
            "no member group `spar` is declared",
            id="a_group_the_model_does_not_build",
        ),
        pytest.param(
            {"platform": []},
            "none was offered",
            id="an_EMPTY_list",
        ),
        pytest.param(
            {"platform": [{"d_outer": 2.5, "wall": 0.30}, {"d_outer": 2.5, "wall": 0.18}]},
            "STEPS THE SECTION UP",
            id="a_grid_that_shrinks",
        ),
        pytest.param(
            {"platform": [{"d_outer": 2.5, "wall": 0.18}, {"d_outer": 2.5, "wall": 0.18}]},
            "STEPS THE SECTION UP",
            id="a_grid_that_REPEATS_a_candidate",
        ),
        pytest.param(
            {"platform": {"d_outer": 2.5, "wall": 0.18}},
            "expected a non-empty list of tubes",
            id="a_mapping_where_a_list_belongs",
        ),
        pytest.param(
            {"platform": [{"d_outer": 2.5, "wall": 1.5}]},
            "so the bore is zero or negative",
            id="a_candidate_that_is_not_a_tube",
        ),
        pytest.param(
            {"platform": [{"d_outer": 2.5, "wall": 0.18, "depth": 3.0}]},
            "depth",
            id="a_candidate_with_an_unknown_key",
        ),
        pytest.param(
            {"platform": [{"d_outer": 2.5}]},
            "wall",
            id="a_candidate_missing_a_key",
        ),
    ],
)
def test_FT2_4_the_grid_is_REFUSED_by_name(candidates: object, needle: str) -> None:
    """Each of these would otherwise reach FM0's loop and be stepped through.

    **The last three are the point of the shared tube door.** `_parse_tube` is what
    `sections.groups` goes through, so a candidate cannot carry a diameter, a wall or a key
    that a declared section could not -- without it the grid would have been a second,
    looser domain for the same quantity, which is the defect R1022 found at the period
    readers.

    `a_grid_that_REPEATS_a_candidate` is the boundary solved from the side that WEAKENS the
    check (EH4): the ordering test is `>`, not `>=`, so a repeated entry is refused too --
    a loop that "stepped up" onto the same section would re-solve the identical model and
    report a second iteration that moved nothing.
    """
    from floatfea.run.config import _parse_sections

    with pytest.raises(ConfigError) as excinfo:
        _parse_sections(_sections_with(candidates))
    assert needle in str(excinfo.value), str(excinfo.value)


def test_FT2_4_the_grids_ORDER_is_by_AREA_and_not_by_either_dimension() -> None:
    """A candidate larger in area and SMALLER in diameter is admissible, and is ordered.

    The thing FM0's loop steps up is the SECTION, and a tube may grow in area while its
    diameter falls. Ordering on `d_outer` or on `wall` alone would refuse a legitimate grid
    -- so this is the weakening direction of the ordering refusal above, and without it
    that refusal could have been an ordering on whichever dimension the first test used.
    """
    from floatfea.run.config import _parse_sections, _tube_area

    grid = _parse_sections(
        _sections_with(
            {
                "platform": [
                    {"d_outer": 3.0, "wall": 0.10},
                    {"d_outer": 2.5, "wall": 0.20},
                ]
            }
        )
    ).candidates["platform"]
    assert grid[0].d_outer > grid[1].d_outer, grid
    assert _tube_area(grid[0]) < _tube_area(grid[1]), grid
