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


def test_R866_a_declared_heading_the_RUN_CANNOT_COVER_refuses_AT_THE_CALL_SITE(
    write: Any, tmp_path: Path, capsys: Any
) -> None:
    """The CALL SITE, not the function -- which is how R866 happened in the first place.

    **R828's SHAPE, ONE LAYER OVER.** `refuse_headings_this_run_cannot_cover` is asserted
    directly in `tests/unit/test_headings_and_bem_coverage.py`, and those cases are green
    with the call REMOVED from `run()`: measured `21 passed` with the line replaced by a
    no-op. That is exactly the hole R866 itself was -- a function that exists, is correct,
    is tested, and is called by nothing -- so the repair needs a case that fails when the
    CALLER goes, and this is it.

    END TO END THROUGH THE CLI, because the other half of the claim is that NOTHING IS
    WRITTEN. R809's recorded reason is that a refusal arriving after the outputs is a
    warning with a non-zero exit code, and only the directory can say which happened.
    It costs no solve: the refusal is before the build.
    """
    import floatfea.cli as cli

    out = tmp_path / "published"

    def mutate(data: dict[str, Any]) -> None:
        data["load_cases"]["headings"] = [0.0, 45.0, 90.0]
        data["outputs"]["directory"] = str(out)

    # `cli.main` CATCHES ConfigError, prints it and returns 2 -- its `except ConfigError`
    # handler in `floatfea/cli.py`, cited by NAME because the line reference here
    # (`cli.py:447-449`) was CORRECT at 3960026 and was staled by FL2(d)'s own commit
    # inserting the band-table section above it (R1013's class, two sites the census's
    # path-prefixed regex could not see) -- so the
    # contract here is the exit code and the message on stderr -- not an exception. A test
    # written against `pytest.raises` passed its control and failed this case, which is
    # how the real contract got measured rather than assumed.
    code = cli.main(["run", str(write(mutate))])
    assert code == 2, code
    message = capsys.readouterr().err
    assert "45.0" in message and "90.0" in message, message
    assert "before any output is written" in message, message
    # THE HALF A STUB CANNOT SEE: the refusal came before anything reached disk.
    assert not out.exists() or not list(out.iterdir()), sorted(p.name for p in out.iterdir())


def test_R866_the_matching_declaration_still_RUNS_and_publishes(write: Any, tmp_path: Path) -> None:
    """The control, end to end: declaring the heading the file carries is not an error.

    Without this, making the refusal unconditional would leave the test above green --
    the mistake FP2's own docstring records one paragraph down.
    """
    import floatfea.cli as cli

    out = tmp_path / "published"

    def mutate(data: dict[str, Any]) -> None:
        data["load_cases"]["headings"] = [0.0]
        data["outputs"]["directory"] = str(out)

    assert cli.main(["run", str(write(mutate))]) == 0
    assert sorted(p.name for p in out.iterdir()) == [
        "member_forces.csv",
        "report.md",
        "utilisation.csv",
    ]


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
    basis = exported_wave_basis(cfg.load_cases.npz_files[0])
    stub = RunResult(
        config=cfg,
        built=built,
        rows=[],
        utilisations=[],
        mass=(),
        timings={},
        # **`wave_bases`, PLURAL, SINCE R1093 DELETED THE SINGULAR FIELD.** It held the
        # FIRST file's basis so a one-file run reproduced byte for byte, and
        # `_write_report` read it -- so a two-file run published file one's heading under
        # "the wave basis these loads were exported at" while naming a different file as
        # governing. The one-file guarantee is this tuple having ONE entry.
        wave_bases=((cfg.load_cases.npz_files[0].name, basis),),
    )
    blob = " ".join(_header_lines(stub))
    assert "heading 0.0 deg" in blob, blob[:200]
    assert "24.2" in blob, blob[:200]


def test_FQ3_R832_an_EMPTY_basis_says_so_AND_no_caveat_contradicts_it(built: Any) -> None:
    """The branch FQ3 required, asserted in BOTH halves (R832).

    **FQ3 NAMED THIS REPAIR AND NOTHING HELD IT.** The reviewer reverted the `if basis:` /
    `else` hunk to the old field-by-field `.get(..., "(not recorded)")` form and the
    measuring half of the suite was green at the identical count -- `113 passed` reverted,
    `113 passed` restored -- because the only test driving `_header_lines` passes the REAL
    sidecar's basis, so it exercises the `if` and never the `else`.

    That is R826's own finding one round later, inside a repair made to answer it: five
    repairs were cycled because a directive named five, and the sixth repair in the same
    commit was not.

    **BOTH HALVES, because one alone is what was wrong.** The old code produced a file
    carrying "heading (not recorded) deg" AND a caveat asserting the heading "is in the
    provenance above" -- two sentences that cannot both be true. So this asserts that the
    line says NOT RECORDED, and that nothing in the same output claims the heading is
    available. FL1(a) admits a sidecar-less npz, so the state is reachable.
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
        wave_bases=((cfg.load_cases.npz_files[0].name, {}),),
    )
    blob = " ".join(_header_lines(stub))
    assert "NOT RECORDED by the export" in blob, blob[:400]
    assert "(not recorded) deg" not in blob, blob[:400]
    # AND NO CAVEAT SUPPLIES THE HEADING THE HEADER SAYS IS ABSENT.
    #
    # THE NEEDLE IS THE RETIRED SENTENCE, NOT THE PHRASE IT CONTAINED. My first version
    # asserted `"is in the provenance above" not in blob` and it failed on the
    # MID-station caveat in `floatfea/cli.py`'s caveat tuple -- cited by name for the
    # same reason as above, the line having moved under FL2(d) --
    # a DIFFERENT caveat, correctly saying the `C_m` value used is in the provenance. A
    # test that reddens on a true sentence about another quantity is not this gate.
    assert "the heading these loads were exported at" not in blob, blob[:400]


def test_FQ3_R832_a_RECORDED_basis_still_states_it(built: Any) -> None:
    """The control: the `else` branch did not swallow the `if`."""
    from floatfea.cli import _header_lines
    from floatfea.run.pipeline import RunResult, exported_wave_basis

    cfg = load_config(EXAMPLE)
    stub = RunResult(
        config=cfg,
        built=built,
        rows=[],
        utilisations=[],
        mass=(),
        timings={},
        wave_bases=(
            (
                cfg.load_cases.npz_files[0].name,
                exported_wave_basis(cfg.load_cases.npz_files[0]),
            ),
        ),
    )
    blob = " ".join(_header_lines(stub))
    assert "heading 0.0 deg" in blob, blob[:300]
    assert "NOT RECORDED by the export" not in blob, blob[:300]


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


# ---------------------------------------------------------------------------
# THE DOOR'S SHAPE, AND THE TWO MEANINGS OF AN EMPTY BASIS
#
# **R1007 AND R884 ARE ONE DEFECT WITH TWO FACES, AND BOTH PUBLISHED A NUMBER.** A
# sidecar whose `run` block was not a mapping, or which existed and could not be parsed,
# came back from the door as `{}` -- indistinguishable from the legitimate "this export
# recorded no wave basis". Measured through the real CLI, one variable moved, the
# committed sidecar's `run` replaced by `[]` and `governing_periods` gaining the breaking
# period:
#
#     EXIT=0, screen_entries = 0, governing U = 2.78942 at T = 10 s, all three artifacts
#     written, report.md saying "the screen was NOT performed ... this dynamic-inputs
#     file records none" -- of a file whose `run.wave_height_full_m` is 24.2
#
# So the whole FL2(d) screen was bypassed in silence and the breaking wave set the
# envelope 63% high, beside the EZ2 caveat denying that it could.
#
# These cells are at the DOOR, where the distinction is made. The arms that reach them
# through `run()` are in `tests/regression/test_fl2d_band_check.py`; these are the ones
# CI runs.


def _sidecar_with(tmp_path: Path, payload: Any) -> Path:
    """A sidecar file carrying `payload` as its whole JSON document."""
    import json

    path = tmp_path / "dynamic_inputs.provenance.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _committed_run_block() -> dict[str, Any]:
    import json

    sidecar = ROOT / "data" / "f4" / "dynamic_inputs.provenance.json"
    block = json.loads(sidecar.read_text(encoding="utf-8"))["run"]
    assert isinstance(block, dict) and "wave_height_full_m" in block, sorted(block)
    return dict(block)


@pytest.mark.parametrize(
    "run_value",
    [
        pytest.param([], id="empty_list"),
        pytest.param(["wave_height_full_m", "heading_deg"], id="list_of_the_key_names"),
        pytest.param("wave_height_full_m heading_deg window lambda", id="string_of_them"),
        pytest.param(5, id="int"),
        pytest.param(True, id="bool"),
        pytest.param(None, id="null"),
    ],
)
def test_R884_a_NON_MAPPING_run_block_is_REFUSED_rather_than_read_as_ABSENT(
    tmp_path: Path, run_value: Any
) -> None:
    """Six shapes, one refusal. Three of them used to raise `TypeError` instead.

    `key in run_block` is a MEMBERSHIP test on a list and a SUBSTRING test on a string, so
    the two container shapes reported every key absent and published "NOT RECORDED"; `5`,
    `True` and `None` raised `TypeError` out of the comprehension. One defect, a traceback
    for three inputs and a silent wrong answer for the other three.

    The two list shapes are the ones that matter most: they are what a multi-heading
    export would write, which is the same shape `run.heading_deg` is already refused for
    one level down.
    """
    from floatfea.run.pipeline import wave_basis_from_sidecar

    sidecar = _sidecar_with(tmp_path, {"run": run_value})
    with pytest.raises(ConfigError) as excinfo:
        wave_basis_from_sidecar(sidecar)
    message = str(excinfo.value)
    assert "`run` is" in message, message
    assert type(run_value).__name__ in message, message
    # **THE EXPLANATION MATCHES THE SHAPE.** The multi-heading sentence is true of a list
    # and of nothing else, and the first version of this refusal printed it for every
    # type: "`run` is int, not an object. A LIST here is a multi-heading export ...".
    assert ("A LIST here" in message) is isinstance(run_value, list), message
    # AND THE REFUSAL NAMES THE ACTION, because R979's lesson is that a refusal whose
    # remedy cannot work leaves the operator nothing to do.
    assert "Delete the sidecar" in message, message


def test_R1007_a_NON_OBJECT_top_level_is_REFUSED(tmp_path: Path) -> None:
    """`recorded.get` is not defined on a list, and a list is valid JSON."""
    from floatfea.run.pipeline import wave_basis_from_sidecar

    sidecar = _sidecar_with(tmp_path, [{"run": _committed_run_block()}])
    with pytest.raises(ConfigError) as excinfo:
        wave_basis_from_sidecar(sidecar)
    assert "top level is list" in str(excinfo.value), str(excinfo.value)


def test_R1007_a_sidecar_that_EXISTS_and_cannot_be_PARSED_is_REFUSED(tmp_path: Path) -> None:
    """UNREADABLE IS NOT ABSENT, and that was the whole of R1007.

    The `except (OSError, json.JSONDecodeError): return {}` that used to stand here made a
    corrupt sidecar publish "wave basis: NOT RECORDED by the export" on all three
    artifacts and skipped the sea-state screen, at exit 0.
    """
    from floatfea.run.pipeline import wave_basis_from_sidecar

    sidecar = tmp_path / "dynamic_inputs.provenance.json"
    sidecar.write_text("{ this is not json", encoding="utf-8")
    with pytest.raises(ConfigError) as excinfo:
        wave_basis_from_sidecar(sidecar)
    message = str(excinfo.value)
    assert "exists and cannot be read as JSON" in message, message
    assert "is NOT an absent one" in message, message


def test_R1007_an_ABSENT_sidecar_still_returns_an_EMPTY_basis(tmp_path: Path) -> None:
    """The other half of the distinction, and FL1(a) requires it.

    Without this cell the repair above could have been written as "refuse everything",
    which would refuse the sidecar-less npz FL1(a) admits.
    """
    from floatfea.run.pipeline import wave_basis_from_sidecar

    assert wave_basis_from_sidecar(tmp_path / "does_not_exist.provenance.json") == {}


def test_R1007_a_run_block_that_RECORDS_NO_BASIS_is_absence_and_not_a_defect(
    tmp_path: Path,
) -> None:
    """The third `{}` return, and it is the only remaining one.

    A `run` block that IS a mapping and carries none of the five basis keys nor any of
    `RECORDED_PROVENANCE_NUMERIC` records no basis. That is absence, so it returns `{}` as
    before. After this commit every OTHER route to `{}` is a refusal, which is what makes
    `_recorded_height`'s `None` unambiguous again.

    **AND THE BOUNDARY IS NARROWER THAN IT LOOKS, WHICH I HAD WRONG.** This cell first
    used `{"lambda": 50.0}` as "a mapping recording no basis", and the door REFUSED it --
    `lambda` is one of `WAVE_BASIS_KEYS`, so `present` is non-empty and the five-key
    completeness check (R878) fires: "records a PARTIAL wave basis: ['heading_deg',
    'wave_height_full_m', 'wave_height_model_m', 'window'] missing from ['lambda']". So
    the empty-`present` exit is reached only by a block carrying NONE of the eight keys,
    and a block carrying some is wrong rather than absent -- which is R878's rule, already
    in force. Both halves are asserted below so the boundary is where it is measured to
    be and not where I assumed.
    """
    from floatfea.run.pipeline import wave_basis_from_sidecar

    none_of_them = _sidecar_with(tmp_path, {"run": {"sha": "abc"}, "git": {"tag": "v1"}})
    assert wave_basis_from_sidecar(none_of_them) == {}
    assert wave_basis_from_sidecar(_sidecar_with(tmp_path, {"run": {}})) == {}

    # SOME of them is PARTIAL, not absent (R878), and that is a refusal.
    partial = _sidecar_with(tmp_path, {"run": {"lambda": 50.0}})
    with pytest.raises(ConfigError) as excinfo:
        wave_basis_from_sidecar(partial)
    assert "records a PARTIAL wave basis" in str(excinfo.value), str(excinfo.value)


def test_R883_an_INTEGER_TOO_LARGE_FOR_A_FLOAT_is_a_NAMED_refusal(tmp_path: Path) -> None:
    """`_validated_wave_basis`'s docstring claimed this was caught. It was not.

    `isinstance(10**400, (int, float))` is True, so the type check passed and
    `float(10**400)` raised `OverflowError` -- a traceback out of the validator, for a
    value a JSON sidecar can carry. The repair makes the docstring's sentence true.
    """
    from floatfea.run.pipeline import wave_basis_from_sidecar

    block = _committed_run_block()
    block["wave_height_full_m"] = 10**400
    sidecar = _sidecar_with(tmp_path, {"run": block})
    with pytest.raises(ConfigError) as excinfo:
        wave_basis_from_sidecar(sidecar)
    message = str(excinfo.value)
    assert "too large to represent as a float" in message, message
    assert "401 digits" in message, message


def test_R883_the_UNCAUGHT_shape_is_what_the_repair_replaced(tmp_path: Path) -> None:
    """The control for the cell above: `float()` on that value really does raise.

    Without this, the cell above would pass equally if `OverflowError` had never been
    reachable -- it would be a test of a refusal with no defect behind it, which is the
    R994 shape this repository deletes rather than keeps.
    """
    with pytest.raises(OverflowError):
        float(10**400)


def test_R1012_the_PUBLIC_screen_refuses_a_period_with_NO_CASE_behind_it() -> None:
    """The guarantee was a property of the caller (R896's shape).

    Both of the screen's refusals are guarded by `T in by_period`, so a declared period
    absent from the file was passed over in silence. Unreachable through `floatfea run`,
    where `unknown` fires thirteen lines earlier -- but the function is in `__all__`.
    """
    from floatfea.run.pipeline import refuse_cases_that_cannot_govern

    class _Cfg:
        class load_cases:  # noqa: N801 -- a stub standing in for the dataclass
            governing_periods = (13.0,)
            out_of_band_governing: tuple[float, ...] = ()

    with pytest.raises(ConfigError) as excinfo:
        refuse_cases_that_cannot_govern(_Cfg(), (12.5, 14.0), {"wave_height_full_m": 24.2})
    message = str(excinfo.value)
    assert "[13.0] s as declared or overridden" in message, message
    assert "cannot be screened" in message, message


def test_R1012_the_SHIPPED_declared_set_is_still_admitted() -> None:
    """The weakening direction: the new refusal must not refuse the real configuration."""
    from floatfea.run.pipeline import refuse_cases_that_cannot_govern

    class _Cfg:
        class load_cases:  # noqa: N801
            governing_periods = (12.5, 14.0, 15.0, 16.2)
            out_of_band_governing = (12.5,)

    screen = refuse_cases_that_cannot_govern(
        _Cfg(), (10.0, 12.5, 14.0, 15.0, 16.2, 20.0), {"wave_height_full_m": 24.2}
    )
    assert len(screen) == 6


# ---------------------------------------------------------------------------
# R1005: THE TWO RECORDS OF EACH CASE'S PERIOD
#
# The npz records every case's period twice -- `periods_full_s[i]` and
# `case{i}/period_full_s` -- and nothing compared them. The screen, the governing
# selection and the published label read the first; the forces come from the `case{i}/`
# groups BY POSITION. A permutation of the top-level array alone published the breaking
# case's `U = 2.78942` under the label `T = 14.0 s`, at exit 0, over a band table calling
# that period admissible.


class _Npz:
    """`files` and `__getitem__`, as `np.load` returns them.

    A stub rather than a written npz, so these cells cost microseconds and the measured
    end-to-end arms in `tests/regression/test_fl2d_band_check.py` carry the real file.
    """

    def __init__(self, mapping: dict[str, Any]) -> None:
        self._m = mapping
        self.files = list(mapping)

    def __getitem__(self, key: str) -> Any:
        return self._m[key]


class _MappingOnly:
    """`__getitem__` and NO `files` -- R1021 half two, as a type.

    The check read `set(getattr(raw, "files", ()))`, so an object without the attribute
    got an empty set of available keys and compared 0 of N: a mapping carrying all six
    CORRECT second records was admitted having checked nothing, and so was one carrying
    six wrong ones. The repair has no attribute and no default -- absence is `raw[key]`
    raising `KeyError` -- so this class and `_Npz` must now behave identically, which is
    what `_BOTH_STUBS` parametrises.
    """

    def __init__(self, mapping: dict[str, Any]) -> None:
        self._m = mapping

    def __getitem__(self, key: str) -> Any:
        return self._m[key]


_BOTH_STUBS = (_Npz, _MappingOnly)


def _two_records(
    top: tuple[float, ...],
    per_case: tuple[float, ...],
    *,
    stub: type = _Npz,
    drop: tuple[int, ...] = (),
) -> Any:
    """A file recording the period twice per case, with `drop` indices missing the second.

    `drop` is how the reviewer expressed the evasion: indices 0 and 2 deleted alongside the
    same permutation gave EXIT=0, `U = 2.78942` at a published `T = 14.0 s`, all three
    artifacts written, and a band table byte-identical to the correct run.
    """
    mapping: dict[str, Any] = {"periods_full_s": list(top)}
    for i, value in enumerate(per_case):
        if i not in drop:
            mapping[f"case{i}/period_full_s"] = value
    return stub(mapping)


SIX = (10.0, 12.5, 14.0, 15.0, 16.2, 20.0)
PERMUTED = (14.0, 12.5, 10.0, 15.0, 16.2, 20.0)


def test_R1005_the_AGREEING_file_is_admitted() -> None:
    """The control. Without it the check below could be an unconditional refusal."""
    from floatfea.run.pipeline import refuse_disagreeing_period_records

    refuse_disagreeing_period_records(Path("dynamic_inputs.npz"), SIX, _two_records(SIX, SIX))


def test_R1005_a_PERMUTED_top_level_array_is_REFUSED_naming_both_values_and_the_index() -> None:
    """The arm that published `U = 2.78942` labelled `T = 14.0 s`."""
    from floatfea.run.pipeline import refuse_disagreeing_period_records

    with pytest.raises(ConfigError) as excinfo:
        refuse_disagreeing_period_records(
            Path("dynamic_inputs.npz"), PERMUTED, _two_records(PERMUTED, SIX)
        )
    message = str(excinfo.value)
    assert "disagrees with itself about which case is which" in message, message
    assert "differ at 2 of 6 indices" in message, message
    # BOTH values and the INDEX, which is what a re-export needs to be aimed at.
    assert "`periods_full_s[0]` = 14 s against `case0/period_full_s` = 10 s" in message, message
    assert "`periods_full_s[2]` = 10 s against `case2/period_full_s` = 14 s" in message, message


def test_R1005_a_SET_comparison_is_GREEN_on_the_very_input_this_refuses() -> None:
    """Why POSITIONALLY. The obvious fix is the one that fails here, and it is measured.

    This is the cell that keeps the repair from being rewritten as a set difference by
    someone who reads "compare the two records" and reaches for the shape `unknown` uses
    eight lines below.
    """
    assert set(PERMUTED) == set(SIX)
    assert sorted(PERMUTED) == sorted(SIX)
    assert PERMUTED != SIX


@pytest.mark.parametrize("stub", _BOTH_STUBS, ids=["np_load", "mapping_without_files"])
@pytest.mark.parametrize(
    "drop, count",
    [
        pytest.param((0, 2), 2, id="the_two_the_permutation_moves"),
        pytest.param(tuple(range(6)), 6, id="every_second_record_deleted"),
        pytest.param((3,), 1, id="one_the_permutation_does_not_touch"),
    ],
)
def test_R1021_a_MISSING_SECOND_RECORD_is_REFUSED_not_abstained_on(
    stub: type, drop: tuple[int, ...], count: int
) -> None:
    """**THIS CELL ASSERTED THE DEFECT.** It is inverted here, in the rule's own commit.

    The first version abstained at an index with no second record, on
    `validated_export_scale` and its `beside is not None` shape, and this cell asserted
    that abstention while the docstring above named it as the weak direction. Abstention
    is an EXIT: deleting `case0/period_full_s` and `case2/period_full_s` alongside the same
    permutation that `test_R1005_a_PERMUTED_...` refuses gave EXIT=0, `U = 2.78942` at a
    published `T = 14.0 s`, all three artifacts written, and a band table byte-identical
    to the correct run's.

    **THOSE FIGURES ARE THE REVIEWER'S (R1021), NOT MINE**, and the one I have dropped
    rather than repeat is "384 rows of `member_forces.csv` carrying byte-identical forces
    under a changed period label" -- I did not take that count, and a figure nobody in
    this file measured does not belong in it (BF0). What IS measured here is that the
    state is refused; the end-to-end arm is
    `tests/regression/test_fl2d_band_check.py::test_END_TO_END_R1021_...`.

    A check that is turned off by deleting the thing it reads is not a check, and the
    non-vacuity assertion that guarded it covers ONE file while `run()` is handed any npz.
    """
    from floatfea.run.pipeline import refuse_disagreeing_period_records

    with pytest.raises(ConfigError) as excinfo:
        refuse_disagreeing_period_records(
            Path("dynamic_inputs.npz"),
            PERMUTED,
            _two_records(PERMUTED, SIX, stub=stub, drop=drop),
        )
    message = str(excinfo.value)
    assert f"{count} of 6 cases carry no " in message, message
    assert f"indices {sorted(drop)}" in message, message
    assert "refused rather than abstained on" in message, message


def test_R1021_an_object_with_NO_files_ATTRIBUTE_compares_EVERY_index() -> None:
    """Half two, and the direction that makes it dangerous rather than merely odd.

    `set(getattr(raw, "files", ()))` turned "this object cannot list its keys" into "this
    file records nothing", so the check returned clean with 0 of 6 compared -- including on
    a mapping whose six second records were all CORRECT, which is the state that makes the
    evasion invisible. Absence is the read failing now, so the two stubs agree.
    """
    from floatfea.run.pipeline import refuse_disagreeing_period_records

    # NON-VACUOUS: the stub really does lack the attribute the old code reached for.
    assert not hasattr(_MappingOnly({}), "files")
    assert hasattr(_Npz({}), "files")

    # Admitted, both stubs, on an agreeing file -- the control.
    for stub in _BOTH_STUBS:
        refuse_disagreeing_period_records(
            Path("dynamic_inputs.npz"), SIX, _two_records(SIX, SIX, stub=stub)
        )

    # And refused, both stubs, on the permutation. Before the repair the second of these
    # was ADMITTED: 0 of 6 compared, nothing said.
    for stub in _BOTH_STUBS:
        with pytest.raises(ConfigError) as excinfo:
            refuse_disagreeing_period_records(
                Path("dynamic_inputs.npz"), PERMUTED, _two_records(PERMUTED, SIX, stub=stub)
            )
        assert "differ at 2 of 6 indices" in str(excinfo.value), str(excinfo.value)


def test_R1021_a_TEXT_second_record_is_REFUSED_rather_than_float_CONVERTED() -> None:
    """`float("14.0") == 14.0`, so a text record would AGREE with the array it checks.

    R825 and its family: a declared field arriving as a different type, accepted, and used.
    The two records would read as agreeing while one of them is not a recorded quantity at
    all, which is the one thing this function exists to be able to say.
    """
    from floatfea.run.pipeline import refuse_disagreeing_period_records

    # THE PLANTED STRING IS DERIVED FROM THE DATA, not typed. `str(SIX[2])` is `"14.0"`,
    # so there is no numeric literal here to declare or to drift: the cell asserts that
    # Python's own `float()` makes the text record and the exported period EQUAL, which is
    # the reason a text record would pass the cross-check at all.
    planted = str(SIX[2])
    assert float(planted) == SIX[2]  # non-vacuous: the conversion really does succeed
    mapping: dict[str, Any] = {"periods_full_s": list(SIX)}
    for i, value in enumerate(SIX):
        mapping[f"case{i}/period_full_s"] = value
    mapping["case2/period_full_s"] = planted
    with pytest.raises(ConfigError) as excinfo:
        refuse_disagreeing_period_records(Path("dynamic_inputs.npz"), SIX, _Npz(mapping))
    message = str(excinfo.value)
    assert "1 of 6 second period records are not numbers" in message, message
    assert "= '14.0' (str)" in message, message


def test_R1005_the_COMMITTED_npz_carries_the_SECOND_RECORD_for_EVERY_CASE() -> None:
    """The WEAKENING direction (EH4): the required record must not refuse the shipped file.

    This cell used to carry the whole defence of the abstention -- the check could go
    vacuous on a file recording the period once, so the committed file was asserted to
    carry the key for every case. R1021 removed the abstention, so the property is no
    longer what makes the check safe; it is what makes the new REQUIREMENT satisfiable by
    the file this repository ships. Both readings want the same six keys, and the figure is
    re-measured here rather than carried over.
    """
    import numpy as np

    raw = np.load(ROOT / "data" / "f4" / "dynamic_inputs.npz", allow_pickle=False)
    top = [float(x) for x in raw["periods_full_s"]]
    assert len(top) == 6, top
    per_case = [f"case{i}/period_full_s" for i in range(len(top))]
    assert [k for k in per_case if k in raw.files] == per_case, sorted(raw.files)
    # not-a-tolerance: the two records of the EXPORTED case periods, compared for exact
    # equality against each other. Nothing is allowed to differ here by any amount; that
    # is the whole content of R1005.
    assert [float(raw[k]) for k in per_case] == top, (top, per_case)


# ---------------------------------------------------------------------------
# R882 AND R1011: TWO SENTENCES, MADE CHECKABLE
#
# Both were prose repairs, and prose in the source tree does not get to claim things
# about the code (CW0). These are the assertions that hold them.


def test_R882_the_heading_refusal_DOES_NOT_recommend_removing_the_DECLARATION() -> None:
    """The remedy clause routed a reader from the refusal to the publication.

    Until R877 the message ended "Fix the sidecar beside the npz, or remove
    `load_cases.headings` so no comparison is claimed" -- and the path it recommended was
    the one on which the bad value was PUBLISHED: a run declaring no headings took an
    early return and printed `heading True deg` at exit 0. R877 moved validation to the
    reader, which makes the advice not merely dangerous but FALSE: the value is refused
    whether or not any heading is declared.
    """
    from floatfea.run.pipeline import _recorded_heading

    with pytest.raises(ConfigError) as excinfo:
        _recorded_heading({"heading_deg": [0.0, 90.0]})
    message = str(excinfo.value)
    assert "not a single heading in degrees" in message, message
    assert "remove `load_cases.headings`" not in message, message
    assert "refused at the READER whether or not any heading is declared" in message, message

    # AND THE ADVICE IS FALSE, which is the measurement behind the sentence: the door
    # refuses the same value with no `headings` declared at all.
    assert load_config(EXAMPLE).load_cases.headings == (), (
        "the shipped example is the configuration that declared nothing and published "
        "the bad value; if it now declares headings this cell's premise has moved"
    )


def test_R1011_the_heading_coverage_check_has_ONE_production_call_site() -> None:
    """`_recorded_height`'s docstring stated a false call graph as its reason.

    It said `refuse_headings_this_run_cannot_cover` "is reached by ... the CLI ... with a
    basis it did not get from this module's door", and used that to explain why
    `_recorded_heading` carries a type guard and `_recorded_height` does not. The true
    graph inverts the conclusion: the one production call site is `run()` in the same
    module, and the basis it passes is `exported_wave_basis(...)` -- the door. So the
    guard cannot fire in production, and the honest statement is that it is a contract on
    a public helper.

    Measured here rather than asserted there, because a sentence about a call graph goes
    stale the first time someone adds a caller.
    """
    import ast

    source = (ROOT / "floatfea" / "run" / "pipeline.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "refuse_headings_this_run_cannot_cover"
    ]
    assert len(calls) == 1, [node.lineno for node in calls]
    # **AND IT IS STILL HANDED THIS MODULE'S OWN DOOR -- one layer out since FT2.6.**
    # The call used to take `exported_wave_basis(...)` inline. It now takes one entry of
    # the `bases` list, and that list is built in `run()` from this module's own reader,
    # so the property this cell exists for is unchanged: the production call is never fed
    # a dict a CALLER chose. Asserted where the fact now lives rather than relaxed.
    passed = calls[0].args[1]
    assert isinstance(passed, ast.Subscript), ast.dump(passed)
    built = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "exported_wave_basis"
    ]
    assert built, "nothing in pipeline.py builds a basis from this module's own reader"
    bases_line = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(getattr(t, "id", "") == "bases" for t in node.targets)
    ]
    assert len(bases_line) == 1, [n.lineno for n in bases_line]
    assert "exported_wave_basis" in ast.dump(bases_line[0]), ast.dump(bases_line[0])

    # The guard is kept because TESTS reach it directly with dicts no door has seen --
    # which is what makes it a contract rather than dead code (R994).
    direct = ROOT / "tests" / "unit" / "test_headings_and_bem_coverage.py"
    assert "refuse_headings_this_run_cannot_cover(" in direct.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# R1019: THE RECORDED PERIOD ARRAY HAD NO DECLARED DOMAIN
#
# `config.py` runs every DECLARED period through `_checked(..., WAVE_PERIOD)`. `run()`
# read `periods_full_s` with `float(x)` and checked it against nothing -- R877/R881's
# asymmetry in the one recorded numeric field `RECORDED_BOUNDS` does not cover. Found by
# running R1010's equivalence grid over `WAVE_PERIOD x WAVE_HEIGHT`, a configuration
# nothing in the diff chose.


def test_R1019_a_RECORDED_period_outside_WAVE_PERIOD_is_REFUSED(tmp_path: Path) -> None:
    """Both ends of the declared range, and the index and value are named.

    `T = 0.5 s` is the one that mattered: it is accepted by every other check, gives
    `H/lambda = 62` at the recorded height, and would have been published as a BREAKING
    sensitivity row for a period outside the range every declared period is held to.
    """
    import numpy as np

    from floatfea.run.config import WAVE_PERIOD
    from floatfea.run.pipeline import run as run_pipeline

    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    npz_src = (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()
    raw = np.load(npz_src, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files}

    for bad in (0.5, 0.0, WAVE_PERIOD[2] * 1.01):
        top = flat["periods_full_s"].copy()
        top[0] = bad
        # **BOTH RECORDS MOVE, SO THE FILE IS SELF-CONSISTENT.** The first version of this
        # cell moved only the top-level array, which makes the file disagree with itself --
        # and `refuse_disagreeing_period_records` (R1005/R1021) refuses that eight lines
        # later for a different reason. The cell still passed, because it asserts the
        # DOMAIN message rather than merely that something raised; but the INPUT it
        # described was one two checks catch, so it could not show the domain check is
        # load-bearing. Moving both records leaves exactly one check that can refuse this
        # file, which is what the revert arm then measures.
        probe = dict(flat, periods_full_s=top)
        probe["case0/period_full_s"] = np.array(bad)
        npz = tmp_path / f"probe_{bad}.npz"
        np.savez(npz, **probe)

        local = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
        local["floatsim"]["deck"] = str((EXAMPLE.parent / local["floatsim"]["deck"]).resolve())
        local["load_cases"]["npz"] = str(npz)
        local["load_cases"]["governing_periods"] = [14.0, 15.0, 16.2]
        local["load_cases"]["out_of_band_governing"] = []
        out_dir = tmp_path / f"out_{bad}"
        local["outputs"]["directory"] = str(out_dir)
        path = tmp_path / f"cfg_{bad}.yaml"
        path.write_text(yaml.safe_dump(local, sort_keys=False), encoding="utf-8")

        with pytest.raises(ConfigError) as excinfo:
            run_pipeline(load_config(path))
        message = str(excinfo.value)
        # **THE NEEDLES MOVED WITH THE RULE (BP0).** R1019's refusal was written inline
        # here; R1022 made it `checked_recorded_periods` and gave it the readers it had
        # missed, so
        # the message is the door's. The cell still asserts the same three facts -- the
        # count, the range, and the index with its value -- against the text that now
        # carries them, rather than against the text of a refusal that no longer exists.
        assert "1 of 6 recorded periods are not admissible values in s" in message, message
        assert "[1, 100]" in message, message
        assert f"index 0: {bad:g} s is outside the admissible range" in message, message
        # AND THE SOURCE IS NAMED, which is what tells a reader which caller of the door
        # refused and which file to re-export.
        assert f"{npz.name}: `periods_full_s`" in message, message
        written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
        assert written == [], written


def test_R1019_the_COMMITTED_array_is_INSIDE_the_declared_range() -> None:
    """The weakening direction: the new refusal must not refuse the shipped file.

    **AND IT IS THE PIPELINE'S HALF OF ONE PROPERTY, NOT A SECOND COPY OF IT (R983).**
    `tests/unit/test_run_config.py::test_R1022_the_COMMITTED_ARRAY_and_SIDECAR_are_both_ADMITTED`
    asks the same question of the door and of BOTH shipped files, and of their agreement.
    This cell asks it of the array `run()` itself reads, through the key `run()` reads it
    by -- which is the thing that would go wrong if the npz were re-exported with a
    different key and the door were handed something else.
    """
    import numpy as np

    from floatfea.run.config import WAVE_PERIOD

    raw = np.load(ROOT / "data" / "f4" / "dynamic_inputs.npz", allow_pickle=False)
    periods = [float(x) for x in raw["periods_full_s"]]
    _unit, low, high = WAVE_PERIOD
    assert all(low <= T <= high for T in periods), periods
    # AND THE CHECK IS NON-VACUOUS: the range does not contain everything a float can be.
    # not-a-tolerance: `0.5` is the out-of-domain PERIOD the sibling cell injects, named
    # here to show `WAVE_PERIOD` excludes it. An input, and nothing is allowed to differ
    # from it by any amount.
    assert not (low <= 0.5 <= high)  # not-a-tolerance: the injected out-of-domain period


def test_R1033_a_BOOL_TYPED_second_record_is_REFUSED_not_read_as_ONE() -> None:
    """The same defect at the other gate, in the spelling that gate actually receives.

    `isinstance(np.True_, bool)` is False, so the list this gate tested admitted a
    bool-typed npz and `float(np.True_)` made every second record `1.0`. Where the top
    array was bool too, BOTH of `run()`'s period gates passed.

    The spelling matters: this gate reads `raw[key]` whole, so what arrives is a
    ZERO-DIMENSIONAL array and not a scalar -- which is why the shared decision asks the
    DTYPE and not `numbers.Real`.
    """
    import numpy as np

    from floatfea.run.pipeline import refuse_disagreeing_period_records

    assert isinstance(np.True_, bool) is False  # non-vacuous: the old list could not see it
    mapping: dict[str, Any] = {"periods_full_s": list(SIX)}
    for i, _value in enumerate(SIX):
        mapping[f"case{i}/period_full_s"] = np.array(True)  # 0-d, dtype bool
    with pytest.raises(ConfigError) as excinfo:
        refuse_disagreeing_period_records(Path("dynamic_inputs.npz"), SIX, _Npz(mapping))
    message = str(excinfo.value)
    assert "6 of 6 second period records are not numbers" in message, message
    # AND THE MESSAGE NAMES THE DTYPE IT DECIDED ON. `type(v).__name__` alone says
    # `ndarray`, which tells a reader nothing about why a zero-dimensional array was
    # refused; the gate reads `dtype.kind`, so the refusal says the dtype.
    assert "(ndarray of dtype bool)" in message, message
