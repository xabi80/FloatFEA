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
from floatfea.run.config import ConfigError, load_config

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
