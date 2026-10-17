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
from floatfea.run.pipeline import (
    _check_material,
    _refuse_inadmissible,
    _utilisations,
    build_model,
)

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


# ---------------------------------------------------------------------------
# FN1: an inadmissible mass distribution refuses, and a study says so
# ---------------------------------------------------------------------------
#
# R810 is why these exist, and the shape of it is worth stating once. Before R1,
# `build_superstructure()` with no fraction descended `MASS_FRACTION_LADDER` and took the
# first rung where `admissible()` held, so a non-PSD remainder was unreachable BY
# CONSTRUCTION. A configuration handing `f` in goes down the `measurement_fraction` path,
# which bypasses the ladder -- documented, and I read the documentation and did not act on
# it. Measured: `f = 1.0` and `f = 0.999999` gave `PSD = False` on four of five bodies and
# the run COMPLETED AND PUBLISHED; the only trace was the word `FAILS` in one table cell.


@pytest.mark.parametrize(
    ("fraction", "because"),
    [
        (1.0, "not PSD"),
        (0.999999, "not PSD"),
        (0.0, "no mass at all"),
    ],
)
def test_FO0_only_a_NON_STRUCTURE_is_refused(write: Any, fraction: float, because: str) -> None:
    """The two refusals FO0 permits, and nothing else. One case each.

    `1.0` and `0.999999` fail `admissible()`; `0.0` is PSD with exactly zero slack and
    fails because the members carry no mass. Two different conditions, so two different
    sentences, and the message must name the one that fired.
    """

    def mutate(data: dict[str, Any]) -> None:
        for body in data["mass_distribution"]:
            data["mass_distribution"][body] = {"f": fraction}

    cfg = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        _refuse_inadmissible(cfg, build_model(cfg))
    message = str(caught.value)
    assert "not a structure" in message, message
    assert because in message, f"the message must name the condition that fired: {message}"
    assert "study_only: true" in message, message
    # R814: the old message opened "one the shipped builder would never have reached",
    # which is FALSE of f = 0 -- the ladder's last rung, admissible on all five bodies.
    assert "never have reached" not in message, (
        f"the refusal must be true of every value it refuses, and f = 0 IS reachable by "
        f"the shipped ladder: {message}"
    )


def test_FO0_a_SMALL_fraction_is_a_LEGITIMATE_INPUT(write: Any) -> None:
    """`f = 0.0106` runs. This is the case R814 was about and the guard must NOT refuse it.

    Measured: the equivalent density there is `100.9963 kg/m^3`, which the old floor of
    `100.0` admitted by `1 kg/m^3` -- so the run published `U = 2.15615` unlabelled while
    the platform's members carried `26500 kg` of a `2.5e+06 kg` body. **The defect was
    never that this configuration ran; it was that a threshold nobody justified decided
    whether it ran.** FO0: it is a legitimate input, it runs, and the mass table shows the
    split.
    """

    def mutate(data: dict[str, Any]) -> None:
        for body in data["mass_distribution"]:
            data["mass_distribution"][body] = {"f": 0.0106}

    cfg = load_config(write(mutate))
    built = build_model(cfg)
    _refuse_inadmissible(cfg, built)  # must not raise

    platform = next(b for b in built.bodies if b.name == "platform")
    assert float(platform.equivalent_density) > 0.0
    assert float(platform.member_mass) > 0.0
    assert cfg.study_only is False, (
        "a legitimate small fraction must not need the study flag; needing it would mean "
        "the guard still judges it inadmissible"
    )


@pytest.mark.parametrize("fraction", [1e-09, 1e-04, 0.0053, 0.0106])
def test_FP2_NO_FLOOR_REMAINS_measured_as_ACCEPTANCE(write: Any, fraction: float) -> None:
    """Every positive density is accepted, however small. R820, and it is BEHAVIOUR.

    **THE TEST THIS REPLACES COULD NOT FAIL, AND THAT WAS THE FINDING.** It read
    `_refuse_inadmissible`'s own source and asserted the absence of `DENSITY`, of ordering
    comparisons and of the import. The reviewer reintroduced the SAME 100 kg/m^3 floor
    through a local binding and got 22 passed, then 186 passed over `tests/unit` plus the
    published-artifact file, with the source test green. Four of five rungs changed
    behaviour and no test moved. Source-reading is a legitimate instrument; my needles
    were the defect, because a floor can arrive by a route no needle names.

    **THE PIN IS AN ACCEPTANCE CASE, NOT AN ABSENCE.** `f = 1e-09` gives an equivalent
    density of `9.52795e-06` kg/m^3 -- positive, and seven orders of magnitude below any
    floor anyone would write. It is accepted today and it reddens under ANY positive
    floor, by any route, while introducing no threshold of its own: the assertion is
    "accepted", not "accepted above X".

    `f = 0.0106` is here because it is the case R814 was about -- the old floor admitted it
    by `0.996` kg/m^3 and published `U = 2.15615` unlabelled -- and `1e-04` and `0.0053`
    sit between, so a floor placed anywhere across six decades fails at least one case.
    """

    def mutate(data: dict[str, Any]) -> None:
        for body in data["mass_distribution"]:
            data["mass_distribution"][body] = {"f": fraction}

    cfg = load_config(write(mutate))
    built = build_model(cfg)
    _refuse_inadmissible(cfg, built)  # must not raise, at any positive density

    platform = next(b for b in built.bodies if b.name == "platform")
    assert float(platform.equivalent_density) > 0.0, platform.equivalent_density
    assert cfg.study_only is False, (
        "a positive density must not need the study flag; needing it would mean the guard "
        "still judges the fraction rather than refusing a non-structure"
    )


def test_FP2_study_only_PERMITS_the_run_and_LABELS_EVERY_OUTPUT(write: Any, tmp_path: Path) -> None:
    """R821. Without the flag: refusal. With it: the run completes and says it is a study.

    **THIS TEST WAS DELETED BY THE COMMIT THAT REPLACED FN1's FLOOR-ERA CASES**, and with
    it went the only assertion that `study_only` does anything at all. The reviewer
    measured the hole: making the refusal unconditional -- `if not cfg.study_only:` to
    `if True:` -- left 186 passed, while the refusal message went on promising the escape.

    END TO END THROUGH THE CLI rather than through `_refuse_inadmissible`, because FP2's
    requirement is that the run COMPLETES and the label reaches EVERY output, and a stub
    cannot see the files. R816 is the finding that says a stub is not enough. It costs a
    real solve.
    """
    import floatfea.cli as cli

    def mutate(data: dict[str, Any]) -> None:
        for body in data["mass_distribution"]:
            data["mass_distribution"][body] = {"f": 0.0}
        data["outputs"]["directory"] = str(tmp_path / "study")

    refused = load_config(write(mutate))
    with pytest.raises(ConfigError) as caught:
        _refuse_inadmissible(refused, build_model(refused))
    assert "not a structure" in str(caught.value), caught.value

    def mutate_study(data: dict[str, Any]) -> None:
        mutate(data)
        data["study_only"] = True

    path = write(mutate_study)
    assert cli.main(["run", str(path)]) == 0, "a declared study must COMPLETE, not refuse"

    out = tmp_path / "study"
    written = sorted(q.name for q in out.iterdir())
    assert written == ["member_forces.csv", "report.md", "utilisation.csv"], written
    for name in written:
        text = (out / name).read_text(encoding="utf-8", errors="replace")
        assert "STUDY -- NOT FOR DESIGN" in text, (
            f"{name} carries no study label. A study that publishes without saying so is "
            f"worse than one that is refused."
        )


def test_FN1_study_only_must_be_a_BOOLEAN(write: Any) -> None:
    """It governs whether an inadmissible distribution runs at all, so it is not coerced."""

    def mutate(data: dict[str, Any]) -> None:
        data["study_only"] = "yes"

    with pytest.raises(ConfigError) as caught:
        load_config(write(mutate))
    assert "must be true or false" in str(caught.value), caught.value


# ---------------------------------------------------------------------------
# R811: a duplicate YAML key refuses
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("needle", "addition"),
    [
        ("    Fy: 355000000.0", "    Fy: 275000000.0"),
        ("  platform: {f: 0.75}", "  platform: {f: 0.30}"),
        ("  K: 2.0", "  K: 3.0"),
    ],
)
def test_R811_a_DUPLICATE_KEY_is_REFUSED(tmp_path: Path, needle: str, addition: str) -> None:
    """YAML's default is last-wins and SILENT, which is the worst of three behaviours.

    Each of these takes the second value while the first sits in the file looking
    authoritative: a different grade, a different mass split, a different effective-length
    factor. `_reject_unknown` cannot see it -- the key IS known, there are simply two of
    it -- and a diff that adds a field without removing the old one is how it happens.

    Parametrised across three sections because a loader fixed for one mapping depth can
    still be last-wins at another.
    """
    base = EXAMPLE.read_text(encoding="utf-8")
    assert needle in base, f"the example no longer contains {needle!r}"
    damaged = base.replace(needle, needle + chr(10) + addition, 1)
    path = tmp_path / "duplicate.yaml"
    path.write_text(damaged, encoding="utf-8")

    with pytest.raises(ConfigError) as caught:
        load_config(path)
    message = str(caught.value)
    assert "duplicate key" in message, message
    assert "last-wins and silent" in message, message


# ---------------------------------------------------------------------------
# R806 / R807: what an artifact's header must carry
# ---------------------------------------------------------------------------
def test_R806_R807_the_header_carries_the_BUILDERS_OWN_assumptions_and_findings(
    built: Any,
) -> None:
    """Generated from the build, not copied, so it cannot go stale against the model.

    R806: the first version of these artifacts carried 11 header lines against the
    committed deliverables' 17 and 12, and the dropped lines were the ones that stop a
    reader misusing a column. R807: nine findings were computed and discarded, five of
    them saying in as many words that the body is a measurement and not one to ship.
    """
    from floatfea.cli import _header_lines
    from floatfea.run.pipeline import RunResult

    cfg = load_config(EXAMPLE)
    stub = RunResult(
        config=cfg,
        built=built,
        rows=[],
        utilisations=[],
        mass=(),
        timings={},
    )
    lines = _header_lines(stub)
    blob = " ".join(lines)

    assert built.assumptions, "the build records no assumptions; this test is vacuous"
    for assumption in built.assumptions:
        assert assumption in blob, f"header drops a recorded assumption: {assumption[:80]}"

    raised = [f for body in built.bodies for f in body.findings]
    assert len(raised) == 9, (
        f"the example build must raise nine findings -- one on the platform and two per "
        f"hub -- and this test is checking they reach the header; got {len(raised)}"
    )
    for finding in raised:
        assert finding in blob, f"header drops a build finding: {finding[:80]}"

    # ALL NINE (FO2). R815: this asserted four, and the other five -- EX3/R724, R743,
    # FA0, FA1, R741/R742 -- grepped `0 0 0` across the report and both CSVs while the
    # gate passed. A gate that lists a subset of what it is for is the shape R806 was.
    for marker in (
        "R739",
        "R740",
        "FA3",
        "EZ2",
        "EX3",
        "R724",
        "R743",
        "FA0",
        "FA1",
        "R741",
        "R742",
    ):
        assert marker in blob, (
            f"header drops the {marker} column caveat. These say what the COLUMNS mean, "
            f"and a reader without them can take an envelope bound for a stress."
        )
    assert "STUDY" not in blob, "a non-study run must not carry the study label"


def test_R806_a_STUDY_run_says_so_in_EVERY_header_line_block(write: Any, built: Any) -> None:
    """The study label is on the artifact, not only on the console."""
    from floatfea.cli import _header_lines
    from floatfea.run.pipeline import RunResult

    def mutate(data: dict[str, Any]) -> None:
        data["study_only"] = True

    cfg = load_config(write(mutate))
    stub = RunResult(config=cfg, built=built, rows=[], utilisations=[], mass=(), timings={})
    lines = _header_lines(stub)
    assert "STUDY -- NOT FOR DESIGN" in lines[0], lines[0]
    assert any("permitted only because" in line for line in lines), lines[-3:]


# ---------------------------------------------------------------------------
# FQ2: R817 and R818 at the GENERATOR, not at the committed file
# ---------------------------------------------------------------------------
#
# **R828 IS WHY THESE EXIST.** R817's and R818's reddening half held the committed
# artifacts: blanking `exported_wave_basis` to `{}` or deleting
# `code_check_sensitivities` from `provenance()` left 195 passed, because the only
# assertions were over files that had already been generated. Worse, the CSV header check
# DERIVES its expectation from `provenance()`, so it moves with the defect.


def test_FQ2_R817_the_READER_returns_the_wave_basis_from_the_sidecar() -> None:
    """The heading and height come from the export's own record (R817).

    At the generator, so blanking the reader reddens this rather than waiting for someone
    to regenerate an artifact.
    """
    from floatfea.run.pipeline import exported_wave_basis

    basis = exported_wave_basis(ROOT / "data" / "f4" / "dynamic_inputs.npz")
    assert basis, "the committed npz's sidecar records a wave basis; the reader found none"
    assert basis["heading_deg"] == 0.0, basis
    # not-a-tolerance: the wave height the EXPORT declared, read back out of its own
    # sidecar. It is an input carried through the file, and the assertion is that the
    # reader returns what was recorded -- exact equality is the point of it.
    assert basis["wave_height_full_m"] == 24.2, basis  # not-a-tolerance: a declared input
    assert "window" in basis, basis


def test_FQ2_R817_the_HEADER_carries_the_basis_the_reader_returned(built: Any) -> None:
    """The generator puts it in the header -- not a committed file's copy of it."""
    from floatfea.cli import _header_lines
    from floatfea.run.pipeline import RunResult, exported_wave_basis

    cfg = load_config(EXAMPLE)
    basis = exported_wave_basis(cfg.load_cases.npz)
    stub = RunResult(
        config=cfg,
        built=built,
        rows=[],
        utilisations=[],
        mass=(),
        timings={},
        wave_basis=basis,
    )
    blob = " ".join(_header_lines(stub))
    assert "heading 0.0 deg" in blob, blob[:200]
    assert "24.2" in blob, blob[:200]


def test_FQ2_R818_the_PROVENANCE_carries_the_sensitivity_operating_points() -> None:
    """Two published columns need their operating point published (R818).

    Asserted on `provenance()` itself, which is the generator. The CSV header check cannot
    serve here: it derives its expected key set FROM `provenance()`, so deleting a key
    moves the expectation with it.
    """
    prov = load_config(EXAMPLE).provenance()
    assert "code_check_sensitivities" in prov, sorted(prov)
    text = str(prov["code_check_sensitivities"])
    assert "K_sensitivity" in text and "Cm_sensitivity" in text, text
    assert "1" in text, text
