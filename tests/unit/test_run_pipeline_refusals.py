"""The pipeline refuses what the schema cannot see (FL1).

The schema in `floatfea/run/config.py` checks a configuration against itself: ranges,
spelling, which fields are mutually exclusive. It cannot check a configuration against
THE MODEL, because the model does not exist until the deck is read. These are the
refusals that need the built model, and every one of them exists to stop a run whose
report would describe something other than what was solved.

**NONE OF THESE IS A FAILED SOLVE.** Each is a configuration that would have produced
numbers -- plausible ones -- for a structure nobody asked for. `CLAUDE.md`: a wrong
answer that looks right is worse than a crash.

Built once per module: the build is about 0.1 s, but there is no reason to pay it per
case, and none of these cases needs a solve.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml

from floatfea.run.config import ConfigError, load_config
from floatfea.run.pipeline import _check_material, _utilisations, build_model

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"


@pytest.fixture(scope="module")
def built() -> Any:
    return build_model(load_config(EXAMPLE))


def _absolutise(data: dict[str, Any]) -> dict[str, Any]:
    """Resolve the configuration's paths, so the file can live outside the source tree.

    Same reason as in `tests/unit/test_run_config.py`: a configuration's relative paths
    resolve against its own directory, so a damaged copy written to `tmp_path` would fail
    on the deck path and the refusal under test would never be reached.
    """
    out = copy.deepcopy(data)
    out["floatsim"]["deck"] = str((EXAMPLE.parent / out["floatsim"]["deck"]).resolve())
    if out["load_cases"].get("npz"):
        out["load_cases"]["npz"] = str((EXAMPLE.parent / out["load_cases"]["npz"]).resolve())
    out["outputs"]["directory"] = str((EXAMPLE.parent / out["outputs"]["directory"]).resolve())
    return out


@pytest.fixture
def write(tmp_path: Path) -> Any:
    """A damaged copy of the example, written to `tmp_path` with absolute inner paths."""

    def make(mutate: Any) -> Path:
        data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
        mutate(data)
        path = tmp_path / "config.yaml"
        path.write_text(yaml.safe_dump(_absolutise(data), sort_keys=False), encoding="utf-8")
        return path

    return make


def test_a_declared_E_the_STIFFNESS_DOES_NOT_USE_is_refused(write: Any, built: Any) -> None:
    """The case that matters most, because both halves would look right on their own.

    `check_member` takes `e=`, so a configuration declaring `E = 200e9` would have the
    code check use 200 GPa while every element stiffness used the 210 GPa the builder
    fixes. The utilisation would then describe a structure that was never solved, and
    nothing in either number would look wrong.
    """

    def mutate(data: dict[str, Any]) -> None:
        data["sections"]["material"]["E"] = 200000000000.0

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        _check_material(cfg, built)
    message = str(caught.value)
    assert "would use the declared value while the solve used the built one" in message, message
    assert "210000000000" in message.replace(",", ""), message


def test_a_declared_G_that_implies_a_different_nu_is_refused(write: Any, built: Any) -> None:
    """G is DERIVED from E and nu, so a declared G reaches nothing.

    Refused rather than recorded, because a G printed in a provenance block reads as an
    input. The refusal prints the exact value to declare.
    """

    def mutate(data: dict[str, Any]) -> None:
        data["sections"]["material"]["G"] = 81000000000.0

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        _check_material(cfg, built)
    message = str(caught.value)
    assert "used by nothing" in message, message
    assert "80769230769.23077" in message, message


def test_the_example_declares_G_EXACTLY_and_round_trips_through_yaml(built: Any) -> None:
    """No epsilon is needed, and this is why.

    The comparison in `_check_material` is exact. That only works if the decimal the
    example declares parses back to the identical double, so that is asserted here rather
    than assumed -- it is the whole reason an epsilon was removable.
    """
    cfg = load_config(EXAMPLE)
    material = built.bodies[0].material
    expected = float(material.E) / (2.0 * (1.0 + float(material.nu)))
    assert cfg.sections.material.g == expected, (
        f"the example declares G = {cfg.sections.material.g!r} and the model derives "
        f"{expected!r}; they must be the identical double for an exact comparison to be "
        f"the right check."
    )
    assert _check_material(cfg, built), "the consistency notes must not be empty"


def test_rho_is_reported_as_BACK_COMPUTED_and_not_silently_ignored(built: Any) -> None:
    """A declared rho is an output here, so the run says so in as many words.

    Not a refusal: the nominal is useful to compare against, and DZ5 / ER1(e) is a
    recorded finding about exactly that comparison. What would be wrong is printing it as
    though the model used it.
    """
    notes = _check_material(load_config(EXAMPLE), built)
    joined = " ".join(notes)
    assert "BACK-COMPUTED per body" in joined, notes
    assert "11433" in joined, f"the hub equivalent density must be reported: {notes}"
    assert "DZ5 / ER1(e)" in joined, (
        f"the equivalent density above the nominal is a recorded finding and the run must "
        f"surface it: {notes}"
    )


def test_a_PER_BODY_fraction_the_builder_cannot_express_is_refused(write: Any) -> None:
    """`build_superstructure` takes ONE scalar fraction for every body.

    Running at one of two declared fractions would report a mass distribution the
    configuration did not ask for, so it is refused until FL2(a) gives the builder
    per-body fractions.
    """

    def mutate(data: dict[str, Any]) -> None:
        data["mass_distribution"]["hub1"]["f"] = 0.5

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        build_model(cfg)
    message = str(caught.value)
    assert "applies ONE fraction to every body" in message, message


def test_the_EXPLICIT_mass_mode_is_refused_while_nothing_consumes_it(write: Any) -> None:
    """Declared, validated, and not yet wired -- so it refuses rather than half-applies.

    FL1(a) asks the schema to accept an explicit distribution and it does. What it must
    not do is accept one and then build from `f`, which would report line masses that
    reached nothing.
    """

    def mutate(data: dict[str, Any]) -> None:
        data["mass_distribution"]["platform"] = {
            "line_masses": {"platform": 9375.0},
            "lumped": [{"label": "winch", "mass": 12000.0, "at": [1.0, 0.0, 2.0]}],
        }

    cfg = load_config(write(mutate))
    assert cfg.mass_distribution["platform"].mode == "explicit"
    assert cfg.mass_distribution["platform"].line_masses == {"platform": 9375.0}
    with pytest.raises(ConfigError) as caught:
        build_model(cfg)
    assert "nothing consumes it yet" in str(caught.value), caught.value


def test_a_MISSING_section_group_is_refused_not_defaulted(write: Any) -> None:
    """A defaulted group would be built with the stand-in and reported as configured."""

    def mutate(data: dict[str, Any]) -> None:
        del data["sections"]["groups"]["hub3"]

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        build_model(cfg)
    message = str(caught.value)
    assert "missing ['hub3']" in message, message


def test_a_section_group_matching_NO_MEMBER_is_refused(write: Any) -> None:
    """A typo'd group name would leave the real group on the stand-in tube."""

    def mutate(data: dict[str, Any]) -> None:
        data["sections"]["groups"]["hub5"] = {"d_outer": 2.5, "wall": 0.18}

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        build_model(cfg)
    assert "which the deck does not have" in str(caught.value), caught.value


def test_the_ONE_THIRD_INCREASE_is_refused_because_it_is_NOT_IMPLEMENTED(
    write: Any, built: Any
) -> None:
    """FL1(a) lists it as an option; EZ4 Q2 locked it OFF and nothing implements it.

    This is the honest resolution of a conflict between the directive and a locked
    decision: the field is accepted by the schema, and the run refuses rather than
    reporting allowables a third lower than the configuration asked for.
    """

    def mutate(data: dict[str, Any]) -> None:
        data["code_check"]["one_third_increase"] = True

    cfg = load_config(write(mutate))
    assert cfg.code_check.one_third_increase is True, "the schema accepts the field"
    with pytest.raises(ConfigError) as caught:
        _utilisations(cfg, built, [])
    message = str(caught.value)
    assert "NOT implemented" in message and "EZ4 Q2" in message, message


def test_a_GOVERNING_PERIOD_WITH_NO_CASE_BEHIND_IT_is_refused(write: Any) -> None:
    """It would silently drop out of the envelope, leaving a smaller one than declared."""
    from floatfea.run.pipeline import run as run_pipeline

    def mutate(data: dict[str, Any]) -> None:
        data["load_cases"]["governing_periods"] = [12.5, 13.3]

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        run_pipeline(cfg)
    message = str(caught.value)
    assert "13.3" in message and "does not contain" in message, message


def test_provenance_records_every_declared_thing(write: Any) -> None:
    """A run nobody can audit is a run nobody can trust.

    Asserted on the KEYS rather than the formatting, so the test does not break when a
    sentence is reworded, and on the deck and the governing periods specifically because
    those two decide what was analysed.
    """
    cfg = load_config(EXAMPLE)
    prov = cfg.provenance()
    for key in (
        "config",
        "deck",
        "hsp_tag",
        "froude_lambda",
        "mass_distribution",
        "sections",
        "material",
        "load_cases",
        "governing_periods_s",
        "code_check",
    ):
        assert key in prov, f"provenance is missing {key!r}: {sorted(prov)}"
    assert prov["governing_periods_s"] == [12.5, 14.0, 15.0, 16.2]
    assert "platform12_deck.yaml" in str(prov["deck"])
    assert copy.deepcopy(prov) == prov, "provenance must be plain data"
