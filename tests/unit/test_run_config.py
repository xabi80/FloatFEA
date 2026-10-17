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

import pytest
import yaml

from floatfea.basis import FY_S355
from floatfea.run.config import ConfigError, _NoDuplicateLoader, load_config

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
    out = copy.deepcopy(data)
    out["floatsim"]["deck"] = str((EXAMPLE.parent / out["floatsim"]["deck"]).resolve())
    if out["load_cases"].get("npz"):
        out["load_cases"]["npz"] = str((EXAMPLE.parent / out["load_cases"]["npz"]).resolve())
    out["outputs"]["directory"] = str((EXAMPLE.parent / out["outputs"]["directory"]).resolve())
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
    assert cfg.load_cases.npz == (ROOT / "data" / "f4" / "dynamic_inputs.npz")
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
    else:
        data["load_cases"]["window_rule"] = 1
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_path(data))
    message = str(caught.value)
    assert "is not a string" in message, (label, message)
    assert "Quote the name" in message, (label, message)


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
