"""FL2(d): the period-band check, per case, and the set that cannot govern.

**WHAT THIS CLOSES, MEASURED BEFORE IT WAS BUILT.** `floatfea/cli.py`'s EZ2 caveat has
shipped on every artifact since F4 -- "only the declared governing periods may set the
envelope. Cases outside the associated-period range for this wave height -- and any
exceeding the deep-water breaking steepness -- are reported as SENSITIVITY ONLY and
cannot govern" -- while nothing in `floatfea/` checked that the declared set was inside
the range. One variable moved on the shipped example, the breaking wave added to
`governing_periods` and everything else held:

    governing_periods: [12.5, 14, 15, 16.2]        EXIT=0   U = 1.71167
    governing_periods: [10, 12.5, 14, 15, 16.2]    EXIT=0   U = 2.78942

`T = 10 s` at `H = 24.2 m` has `H/lambda = 0.155`, above `1/7 = 0.1429`. It set the
governing utilisation 63% high, at exit 0, in a `utilisation.csv` that carried the caveat
denying it could. Under FR1 that is a wrong number in a published deliverable (EZ0).

The cells below are ordered: the logic directly, then the END-TO-END wiring, because
FT2's standing rule is that every repair's CALLER is held by a test and a correct
function nothing calls was three findings in this step already.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.loads.period_band import Admissibility
from floatfea.run.config import ConfigError, load_config
from floatfea.run.pipeline import (
    _recorded_height,
    refuse_cases_that_cannot_govern,
)
from floatfea.run.pipeline import run as run_pipeline

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"
PUBLISHED_REPORT = ROOT / "results" / "R1" / "example" / "report.md"

# The npz's six cases and the shipped sea state.
PERIODS = (10.0, 12.5, 14.0, 15.0, 16.2, 20.0)
H_FULL = 24.2
BASIS = {
    "heading_deg": 0.0,
    "wave_height_full_m": H_FULL,
    "wave_height_model_m": 0.484,
    "window": "the committed window per case",
}


class _Cfg:
    """The one field `refuse_cases_that_cannot_govern` reads, and nothing else.

    A stub rather than a real `RunConfig` so these cells cost milliseconds instead of
    the three minutes a full run takes; the END-TO-END cells below pay that cost once
    each and prove the stub is faithful to the wiring.
    """

    def __init__(self, governing: tuple[float, ...], override: tuple[float, ...] = ()):
        self.load_cases = type(
            "_LC", (), {"governing_periods": governing, "out_of_band_governing": override}
        )()


# ---------------------------------------------------------------------------
# The screen is reported for EVERY case, which is FL2(d)'s "and reported".
# ---------------------------------------------------------------------------
def test_the_screen_covers_EVERY_case_not_only_the_governing_ones() -> None:
    screen = refuse_cases_that_cannot_govern(
        _Cfg((12.5, 14.0, 15.0, 16.2), (12.5,)), PERIODS, BASIS
    )
    assert tuple(c.period_full_s for c in screen) == tuple(sorted(PERIODS))
    by_period = {c.period_full_s: c.verdict for c in screen}
    assert by_period == {
        10.0: Admissibility.BREAKING,
        12.5: Admissibility.TOO_SHORT,
        14.0: Admissibility.IN_BAND,
        15.0: Admissibility.IN_BAND,
        16.2: Admissibility.IN_BAND,
        20.0: Admissibility.TOO_LONG,
    }


def test_the_SHIPPED_declared_set_is_ACCEPTED() -> None:
    """The control arm: the example's own declaration must pass, or the check is wrong."""
    screen = refuse_cases_that_cannot_govern(
        _Cfg((12.5, 14.0, 15.0, 16.2), (12.5,)), PERIODS, BASIS
    )
    assert len(screen) == len(PERIODS)


# ---------------------------------------------------------------------------
# The refusals. Each names the period, the band and the margin, because a
# refusal that does not say which side to change leaves the operator nothing
# to do (R979's lesson).
# ---------------------------------------------------------------------------
def test_a_BREAKING_wave_declared_GOVERNING_is_REFUSED() -> None:
    """The exact state that published `U = 2.78942` at exit 0."""
    with pytest.raises(ConfigError) as caught:
        refuse_cases_that_cannot_govern(
            _Cfg((10.0, 12.5, 14.0, 15.0, 16.2), (12.5,)), PERIODS, BASIS
        )
    message = str(caught.value)
    assert "[10.0] s" in message, message
    assert "breaking" in message, message
    assert "12.542 .. 16.316 s" in message, message
    assert "0.1550" in message and "0.1429" in message, message
    assert (
        "out_of_band_governing" in message
    ), f"the refusal must name the field that would admit it deliberately: {message}"


def test_a_TOO_LONG_case_declared_GOVERNING_is_REFUSED() -> None:
    """The other side of the band, so the cell is not one-edged (R944's defect)."""
    with pytest.raises(ConfigError) as caught:
        refuse_cases_that_cannot_govern(_Cfg((14.0, 15.0, 20.0), ()), PERIODS, BASIS)
    message = str(caught.value)
    assert "[20.0] s" in message, message
    assert "too long for this height" in message, message
    assert "+3.684" in message, message


def test_FA0s_case_is_REFUSED_WITHOUT_the_declaration_and_ADMITTED_WITH_it() -> None:
    """The override is load-bearing in both directions, measured as one cell.

    This is the pair that shows `out_of_band_governing` is doing work: the SAME
    governing set is refused without it and accepted with it, so the field cannot be
    decoration and cannot be silently ignored.
    """
    governing = (12.5, 14.0, 15.0, 16.2)
    with pytest.raises(ConfigError) as caught:
        refuse_cases_that_cannot_govern(_Cfg(governing, ()), PERIODS, BASIS)
    message = str(caught.value)
    assert "[12.5] s" in message, message
    assert "-0.042" in message, f"the refusal must carry FA0's own margin: {message}"

    screen = refuse_cases_that_cannot_govern(_Cfg(governing, (12.5,)), PERIODS, BASIS)
    assert len(screen) == len(PERIODS)


def test_a_STALE_override_is_REFUSED_rather_than_ignored() -> None:
    """An override for an IN-BAND period admits nothing and is refused.

    Ignoring it would be the quiet failure: the entry would stop protecting the case it
    was written for the moment the recorded height moved, and would start admitting that
    period again the next time it moved back, with nothing in between saying so.
    """
    with pytest.raises(ConfigError) as caught:
        refuse_cases_that_cannot_govern(
            _Cfg((12.5, 14.0, 15.0, 16.2), (12.5, 14.0)), PERIODS, BASIS
        )
    message = str(caught.value)
    assert "[14.0] s" in message, message
    assert "INSIDE the band" in message, message
    assert "admits nothing" in message, message


def test_an_ORPHAN_override_is_refused_at_the_CONFIG_READER(tmp_path) -> None:
    """An override naming a period that is not governing at all is refused early.

    At the reader rather than at the comparison (R877): the relationship between the two
    declared lists needs no npz, so it is checked where no earlier return can skip it.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    data["outputs"]["directory"] = str(tmp_path / "out")
    data["load_cases"]["out_of_band_governing"] = [12.5, 20.0]
    path = tmp_path / "orphan.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    with pytest.raises(ConfigError) as caught:
        load_config(path)
    message = str(caught.value)
    assert "20.0" in message, message
    assert "does not ADD a period" in message, message


# ---------------------------------------------------------------------------
# No recorded height: the screen is NOT performed, and says so.
# ---------------------------------------------------------------------------
def test_with_NO_recorded_height_the_screen_is_SKIPPED_and_nothing_is_assumed() -> None:
    """FL1(a) admits a sidecar-less npz, so this is reachable and not hypothetical.

    An assumed height here would be R902 exactly -- a band decided from a constant while
    the header printed a recorded value -- and it would publish a BREAKING verdict for a
    sea state nobody recorded.
    """
    assert _recorded_height({}) is None
    assert refuse_cases_that_cannot_govern(_Cfg((10.0,), ()), PERIODS, {}) == ()


def test_the_report_SAYS_the_screen_was_not_performed_rather_than_omitting_it(
    tmp_path,
) -> None:
    """A missing section reads as "nothing to report"; the absence must be stated."""
    from floatfea.cli import _write_report
    from floatfea.run.pipeline import RunResult

    # One utilisation row, carrying exactly the six keys `_write_report` reads off the
    # governing row. The section under test comes BEFORE that block, but the report is
    # written whole, so a stub without it fails on `governing()` rather than on anything
    # FL2(d) does -- and the point of going through `_write_report` instead of calling
    # the section builder is that the CALLER is what FT2 asks to be held.
    one_row = {
        "member": "platform:hub4_arm",
        "station": "ROOT",
        "period_full_s": 12.5,
        "basis": "total_instant",
        "governing_clause": "3.3.2 interaction",
        "utilisation": 1.71167,
    }
    result = RunResult(
        config=load_config(_resolved_example(tmp_path)),
        built=type("_B", (), {"label": "", "assumptions": (), "bodies": ()})(),
        rows=[],
        utilisations=[one_row],
        mass=(),
        timings={},
        wave_basis={},
        band_screen=(),
    )
    out = tmp_path / "report.md"
    _write_report(out, result)
    text = out.read_text(encoding="utf-8")
    assert "Sea-state admissibility, per case" in text
    assert "the screen was NOT performed" in text
    assert "No height was assumed" in text


def test_the_report_RENDERS_the_table_and_the_override_note_from_the_SCREEN(
    tmp_path,
) -> None:
    """The section-GENERATING code, held directly.

    **WHY THIS CELL EXISTS, AND IT IS A GAP I FOUND IN MY OWN FIRST PASS.** The two
    cells that assert the published table read the COMMITTED artifact. That is
    deliberate -- it catches a regeneration that was never committed, which a test that
    regenerates cannot -- but it means neither can see the section being deleted from
    `floatfea/cli.py`: the committed file would still contain the rows. This one renders
    from a screen through `_write_report`, so the code path is covered too.
    """
    from floatfea.cli import _write_report
    from floatfea.run.pipeline import RunResult

    cfg = load_config(_resolved_example(tmp_path))
    screen = refuse_cases_that_cannot_govern(
        _Cfg((12.5, 14.0, 15.0, 16.2), (12.5,)), PERIODS, BASIS
    )
    result = RunResult(
        config=cfg,
        built=type("_B", (), {"label": "", "assumptions": (), "bodies": ()})(),
        rows=[],
        utilisations=[
            {
                "member": "platform:hub4_arm",
                "station": "ROOT",
                "period_full_s": 12.5,
                "basis": "total_instant",
                "governing_clause": "3.3.2 interaction",
                "utilisation": 1.71167,
            }
        ],
        mass=(),
        timings={},
        wave_basis=BASIS,
        band_screen=screen,
    )
    out = tmp_path / "report.md"
    _write_report(out, result)
    text = out.read_text(encoding="utf-8")
    assert "## Sea-state admissibility, per case (FL2(d) / EZ2)" in text
    assert "`12.542 .. 16.316 s`" in text
    assert "| 10 | 0.1550 | breaking | -2.542 | sensitivity only |" in text
    assert (
        "| 12.5 | 0.0992 | too short for this height | -0.042 | "
        "**GOVERNING, admitted out of band by declaration** |" in text
    )
    assert "| 14 | 0.0791 | in band | — | governing |" in text
    assert "is admitted to the envelope although the band excludes it" in text
    assert "not a widened band" in text


def _resolved_example(tmp_path: Path) -> Path:
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    data["outputs"]["directory"] = str(tmp_path / "out")
    path = tmp_path / "resolved.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# END TO END: the CALL SITE, not the helper (FT2's standing rule).
# ---------------------------------------------------------------------------
def test_END_TO_END_a_breaking_governing_period_REFUSES_AND_WRITES_NOTHING(
    tmp_path,
) -> None:
    """R809: a refusal that arrives after the artifacts is a warning with an exit code.

    So the assertion is not only that it refuses -- it is that the outputs directory
    holds nothing afterwards. The previous behaviour wrote all three artifacts with a
    breaking wave governing.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    out_dir = tmp_path / "out"
    data["outputs"]["directory"] = str(out_dir)
    data["load_cases"]["governing_periods"] = [10.0, 12.5, 14.0, 15.0, 16.2]
    path = tmp_path / "breaking.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    with pytest.raises(ConfigError) as caught:
        run_pipeline(load_config(path))
    assert "cannot set an envelope" in str(caught.value)
    written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
    assert written == [], (
        f"the refusal left {written} on disk; nothing should describe a run whose "
        f"envelope a breaking wave set"
    )


def test_END_TO_END_the_SHIPPED_example_still_carries_its_screen_on_the_RESULT() -> None:
    """The screen reaches `RunResult`, so an artifact can state it.

    Read from the COMMITTED deliverable rather than by re-running, which keeps this cell
    cheap and also catches a regeneration that was never committed -- the thing a test
    that regenerates cannot see (`tests/regression/test_r1_published_artifacts.py`).
    """
    text = PUBLISHED_REPORT.read_text(encoding="utf-8")
    assert "## Sea-state admissibility, per case (FL2(d) / EZ2)" in text
    assert "`12.542 .. 16.316 s`" in text
    for row in (
        "| 10 | 0.1550 | breaking | -2.542 | sensitivity only |",
        "| 12.5 | 0.0992 | too short for this height | -0.042 | "
        "**GOVERNING, admitted out of band by declaration** |",
        "| 14 | 0.0791 | in band | — | governing |",
        "| 20 | 0.0387 | too long for this height | +3.684 | sensitivity only |",
    ):
        assert row in text, f"missing published row: {row}"


def test_the_OVERRIDE_reaches_every_published_artifact() -> None:
    """R812's rule: declared AND consumed.

    An override that admitted an out-of-band case and appeared nowhere would leave a
    reader unable to tell an envelope the band screened from one a declaration widened.

    This reads the COMMITTED artifacts, so it is blind to a code change -- see the
    companion cell below, which holds `provenance()` itself. Both are needed and my own
    revert cycle is what showed it: renaming the key in `config.py` left this cell green.
    """
    for name in ("report.md", "member_forces.csv", "utilisation.csv"):
        path = ROOT / "results" / "R1" / "example" / name
        text = path.read_text(encoding="utf-8")
        assert "out_of_band_governing_s" in text, f"{name} does not state the override"
        assert "12.5" in text, name


def test_the_CONFIG_SELF_RECORD_carries_the_override_and_says_so_when_there_is_none(
    tmp_path,
) -> None:
    """`RunConfig.provenance()` is what puts the override into all three artifacts.

    **THIS CELL EXISTS BECAUSE THE REVERT CYCLE FOUND NOTHING HOLDING IT.** Renaming
    `out_of_band_governing_s` in `floatfea/run/config.py` left every other cell in this
    file green: the two artifact cells read committed files, and the report-section cell
    asserts text that `floatfea/cli.py` writes rather than text `provenance()` supplies.
    An eighth revert arm that cannot go red is a guard that is not there, which is the
    whole reason the cycle is run per repair rather than per commit.

    Both branches, because a blank line reads as "no override" exactly as a missing one
    does -- so the empty case must state itself too.
    """
    cfg = load_config(_resolved_example(tmp_path))
    record = cfg.provenance()
    assert record["out_of_band_governing_s"] == [12.5], record

    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    data["outputs"]["directory"] = str(tmp_path / "out2")
    # Dropping BOTH the override and the case it protects, so the configuration is
    # internally consistent and the band admits every declared period on its own terms.
    data["load_cases"]["governing_periods"] = [14.0, 15.0, 16.2]
    data["load_cases"].pop("out_of_band_governing")
    path = tmp_path / "no_override.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    plain = load_config(path).provenance()
    assert plain["out_of_band_governing_s"] == (
        "(none -- every governing period is inside the band)"
    ), plain


def test_the_npz_CASE_LIST_and_the_screen_agree_on_LENGTH() -> None:
    """A screen shorter than the file would silently skip a case.

    R976's class: a wrong denominator from a multiplicity mismatch. The npz is the
    authority for which cases exist.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    npz = (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()
    with np.load(npz) as raw:
        periods = tuple(float(x) for x in raw["periods_full_s"])
    screen = refuse_cases_that_cannot_govern(
        _Cfg((12.5, 14.0, 15.0, 16.2), (12.5,)), periods, BASIS
    )
    assert len(screen) == len(periods) == 6
    assert tuple(c.period_full_s for c in screen) == tuple(sorted(periods))


def test_a_NEGATIVE_recorded_height_never_reaches_the_screen(tmp_path: Any) -> None:
    """R881's domain is at the reader, so the screen's own `sqrt` guard is unreachable
    through the real path -- which is checked here rather than assumed.

    Both halves matter: the configuration reader refuses it, AND the screen would too.
    """
    from floatfea.loads.period_band import associated_period_band

    with pytest.raises(ValueError, match="height"):
        associated_period_band(-H_FULL)
    # And through the module's own door, the recorded value is validated before it
    # could arrive here at all -- `_validated_wave_basis` range-checks against
    # WAVE_HEIGHT, whose domain is 0.0 .. 100.0 m.
    from floatfea.run.config import WAVE_HEIGHT

    assert WAVE_HEIGHT[1] == 0.0, WAVE_HEIGHT


# ---------------------------------------------------------------------------
# THE TWO WAYS THE SCREEN WAS BYPASSED AT EXIT 0, DRIVEN THROUGH `run()`
#
# Both were found by running the model at a configuration the FL2(d) commit did not
# choose, and neither is visible in that commit's diff.


def _example_in(tmp_path, **overrides):
    """The shipped example, rewritten into `tmp_path` with absolute inner paths.

    `copy_data=True` also copies the npz and its sidecar, so a cell may damage them
    without touching the committed files.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    npz = (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()
    if overrides.pop("copy_data", False):
        local = tmp_path / "data"
        local.mkdir(exist_ok=True)
        shutil.copy2(npz, local / npz.name)
        shutil.copy2(npz.with_suffix(".provenance.json"), local / f"{npz.stem}.provenance.json")
        npz = local / npz.name
    data["load_cases"]["npz"] = str(npz)
    out_dir = tmp_path / "out"
    data["outputs"]["directory"] = str(out_dir)
    for key, value in overrides.items():
        data["load_cases"][key] = value
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path, out_dir, npz


def test_END_TO_END_R1005_a_PERMUTED_period_array_REFUSES_AND_WRITES_NOTHING(
    tmp_path,
) -> None:
    """The file disagreeing with itself published `U = 2.78942` labelled `T = 14.0 s`.

    ONE VARIABLE MOVED: indices 0 and 2 of `periods_full_s` permuted, every `case{i}/`
    group byte-identical, the sidecar untouched, the shipped governing set. Before the
    repair: EXIT=0, `U = 2.78942` -- the breaking case's, 63% above the shipped figure --
    at `platform:hub2_arm ROOT`, over a band table reading
    `| 14 | 0.0791 | in band | — | governing |`, and the `period_full_s` column of all
    1248 rows of `member_forces.csv` naming a different case than the forces beside it.
    """
    path, out_dir, npz = _example_in(tmp_path, copy_data=True)
    raw = np.load(npz, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files}
    top = flat["periods_full_s"].copy()
    top[0], top[2] = top[2], top[0]
    flat["periods_full_s"] = top
    np.savez(npz, **flat)

    with pytest.raises(ConfigError) as caught:
        run_pipeline(load_config(path))
    message = str(caught.value)
    assert "disagrees with itself about which case is which" in message, message
    assert "differ at 2 of 6 indices" in message, message
    written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
    assert written == [], (
        f"the refusal left {written} on disk; nothing should describe a run whose forces "
        f"and period labels came from different cases"
    )


@pytest.mark.parametrize(
    "damage, needle",
    [
        pytest.param("list", "`run` is list, not an object", id="run_block_is_a_list"),
        pytest.param("int", "`run` is int, not an object", id="run_block_is_an_int"),
        pytest.param("null", "`run` is NoneType, not an object", id="run_block_is_null"),
        pytest.param("toplevel", "top level is list, not an object", id="top_level_is_a_list"),
        pytest.param("corrupt", "exists and cannot be read as JSON", id="sidecar_is_not_json"),
    ],
)
def test_END_TO_END_R1007_a_MALFORMED_SIDECAR_REFUSES_INSTEAD_OF_SKIPPING_THE_SCREEN(
    tmp_path, damage: str, needle: str
) -> None:
    """Every shape that used to make the whole FL2(d) screen vanish at exit 0.

    Measured before the repair, on the `run: []` arm with the breaking period declared and
    no override: EXIT=0, `screen_entries = 0`, governing `U = 2.78942` at `T = 10 s`, all
    three artifacts written -- under "wave basis: NOT RECORDED by the export of this
    dynamic-inputs file" and "the screen was NOT performed ... this dynamic-inputs file
    records none". Both sentences are false of a sidecar whose `run.wave_height_full_m`
    is `24.2`, and the EZ2 caveat denying that a breaking case can govern shipped beside
    them.

    The three `TypeError` shapes (`run: 5`, `run: true`, `run: null`) are the same defect
    arriving as a traceback instead of a wrong number.
    """
    path, out_dir, npz = _example_in(
        tmp_path,
        copy_data=True,
        governing_periods=[10.0, 12.5, 14.0, 15.0, 16.2],
        out_of_band_governing=[12.5],
    )
    sidecar = npz.with_suffix(".provenance.json")
    if damage == "corrupt":
        sidecar.write_text("{ this is not json", encoding="utf-8")
    elif damage == "toplevel":
        nested = json.loads(sidecar.read_text(encoding="utf-8"))
        sidecar.write_text(json.dumps([nested]), encoding="utf-8")
    else:
        record = json.loads(sidecar.read_text(encoding="utf-8"))
        record["run"] = {"list": [], "int": 5, "null": None}[damage]
        sidecar.write_text(json.dumps(record), encoding="utf-8")

    with pytest.raises(ConfigError) as caught:
        run_pipeline(load_config(path))
    assert needle in str(caught.value), str(caught.value)
    written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
    assert written == [], (
        f"the refusal left {written} on disk; nothing should describe a run that "
        f"published the wave basis as NOT RECORDED from a file that records one"
    )


def test_END_TO_END_a_SIDECAR_LESS_npz_still_RUNS_and_says_the_screen_was_not_performed(
    tmp_path,
) -> None:
    """The weakening direction of the repair above, and FL1(a) requires it.

    Every arm above refuses. Without this cell the repair could have been "refuse any
    sidecar that is not perfect", which would refuse the sidecar-less npz FL1(a) admits
    -- and the measurement that distinguishes them is which of the two states the file is
    in, not how strict the reader is.
    """
    path, out_dir, npz = _example_in(tmp_path, copy_data=True)
    npz.with_suffix(".provenance.json").unlink()

    result = run_pipeline(load_config(path))
    assert result.band_screen == (), "no height is recorded, so no band can be decided"
    assert result.wave_basis == {}, result.wave_basis


def test_END_TO_END_R1021_the_PERMUTATION_WITH_THE_SECOND_RECORDS_DELETED_REFUSES(
    tmp_path,
) -> None:
    """The evasion R1005 left open, driven exactly as the reviewer drove it.

    The same permutation as the cell above, plus `case0/period_full_s` and
    `case2/period_full_s` DELETED. Before R1021 the per-index abstention made that
    EXIT=0: `U = 2.78942` at a published `T = 14.0 s`, all three artifacts written, and a
    band table byte-identical to the correct run's. The refusal the cell above asserts was
    reachable only while the file still carried the evidence against itself.

    **THOSE FIGURES ARE THE REVIEWER'S (R1021), NOT MINE.** The reviewer also counted 384
    rows of `member_forces.csv` carrying byte-identical forces under a changed period
    label; I did not take that count and do not repeat it as though I had. What this cell
    measures is its own assertion below: refused, naming the indices, nothing on disk.
    """
    path, out_dir, npz = _example_in(tmp_path, copy_data=True)
    raw = np.load(npz, allow_pickle=False)
    flat = {k: raw[k] for k in raw.files if k not in ("case0/period_full_s", "case2/period_full_s")}
    top = flat["periods_full_s"].copy()
    top[0], top[2] = top[2], top[0]
    flat["periods_full_s"] = top
    np.savez(npz, **flat)

    with pytest.raises(ConfigError) as caught:
        run_pipeline(load_config(path))
    message = str(caught.value)
    assert "2 of 6 cases carry no " in message, message
    assert "indices [0, 2]" in message, message
    assert "refused rather than abstained on" in message, message
    written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
    assert written == [], (
        f"the refusal left {written} on disk; nothing should describe a run whose forces "
        f"and period labels came from different cases"
    )


# ---------------------------------------------------------------------------
# R1051: THE JOINT-REACTION ARRAY'S DTYPE, END TO END THROUGH THE REAL CLI
#
# `floatfea/post/forces_table.py` read `case{i}/lam` and converted it with
# `np.asarray(..., dtype=np.float64)`, which converts whatever it is given. The reviewer
# drove four dtypes through the shipped example's own recipe, one variable moved:
#
#     float64 (control)  EXIT 0  governing U = 1.71167  platform:hub4_arm  3.3.2
#     bool               EXIT 0  governing U = 0.995379 platform:hub1_arm  3.3.2
#     <U8                EXIT 0  governing U = 1.71654  platform:hub4_arm  3.3.2
#     int64              EXIT 0  governing U = 1.73988  platform:hub4_arm  3.2.3 bending
#
# All four wrote all three artifacts. `U = 0.995379` reads as PASSING where the truth is
# `1.71167` -- a failing structure published as passing.


def _lam_retyped(tmp_path, dtype_name: str):
    """The shipped example with every `case{i}/lam` cast to `dtype_name`.

    ONE VARIABLE: the dtype of that one array. Every other key, the sidecar, the deck and
    the configuration are the shipped ones, copied by `_example_in(copy_data=True)`.
    """
    path, out_dir, npz = _example_in(tmp_path, copy_data=True)
    raw = np.load(npz, allow_pickle=False)
    flat = {}
    for k in raw.files:
        v = raw[k]
        flat[k] = v.astype(dtype_name) if k.endswith("/lam") else v
    np.savez(npz, **flat)
    return path, out_dir


@pytest.mark.parametrize(
    "dtype_name, spelled",
    [
        pytest.param("bool", "bool", id="bool"),
        pytest.param("<U8", "<U8", id="U8_string"),
        pytest.param("int64", "int64", id="int64"),
    ],
)
def test_R1051_a_NON_FLOAT_lam_is_REFUSED_and_writes_NOTHING(
    tmp_path, dtype_name: str, spelled: str
) -> None:
    """The three arms the condition names, each driven through `floatfea.cli.main`.

    **`int64` is the arm that makes this a separate decision.** `is_recorded_number`
    (R1033) admits dtype kinds `i` and `u`, because a recorded period or Froude scale may
    legitimately be an integer -- so reusing that decision here would leave the int64 arm
    exactly as it was. A physical multiplier recorded as an integer is a TRUNCATED
    multiplier, and `docs/load-interchange-v1.md` declares the field physical.
    """
    from floatfea import cli

    path, out_dir = _lam_retyped(tmp_path, dtype_name)
    with pytest.raises(SystemExit) as caught:
        cli.main(["run", str(path)])
    message = str(caught.value)
    assert "joint-reaction multipliers are" in message, message
    # The dtype as the EXPORTER spells it, not as `dtype.name` does -- `<U8` is `str256`
    # there, which is the bit width and tells a reader nothing about their file.
    assert spelled in message, message
    assert "multipliers, dt-free, physical" in message, message
    written = sorted(p.name for p in out_dir.glob("*")) if out_dir.exists() else []
    assert written == [], (
        f"the refusal left {written} on disk; a run whose joint reactions were not numbers "
        f"must publish no utilisation at all"
    )


def test_R1051_the_CONTROL_the_shipped_float64_lam_still_publishes(tmp_path) -> None:
    """The weakening direction: the gate must not refuse the file this repository ships.

    Without this the three arms above could be an unconditional refusal, which would make
    `floatfea run` unable to run at all. The governing figure is NOT asserted here -- that
    is `tests/regression/test_r1_example_golden.py`'s job and it would be a second copy of
    it; what this cell holds is that the gate admits the shipped dtype and the three
    artifacts appear.
    """
    from floatfea import cli

    path, out_dir, npz = _example_in(tmp_path, copy_data=True)
    with np.load(npz, allow_pickle=False) as raw:
        assert raw["case0/lam"].dtype.kind == "f", raw["case0/lam"].dtype
    assert cli.main(["run", str(path)]) == 0
    written = sorted(p.name for p in out_dir.glob("*"))
    assert written == ["member_forces.csv", "report.md", "utilisation.csv"], written
