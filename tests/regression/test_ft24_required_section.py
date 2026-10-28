"""FT2.4: `outputs.required_section` -- propose from fixed forces, then RE-SOLVE (FM0).

**WHAT THIS CLOSES.** `outputs.required_section` was a declared flag that refused by name:
`floatfea/cli.py` raised "are FL2(b) and are not wired in R1 step 1". The sizing that
exists lives in `scripts/measure/f6a_required_section.py`, which searches thousands of
candidates by RE-EVALUATING THE CLAUSES ON STORED FORCES and never rebuilds -- so its
answer rests on FG2's premise that section choice does not change the member forces, and
a separate script, `f6a_premise_check.py`, is what rebuilds and checks it.

Directive FM0 retired that premise rather than putting a threshold on it: the fixed-force
pass PROPOSES, and the tool then re-solves at the proposal and loops on `U > 1.0`. So this
file's cells are about the loop, and the two things FM0 asks to be reported -- the
iteration count, and BOTH `max U` values.

**THE FIXTURE, AND WHY IT IS HONEST TO TRIM IT.** Every cell here solves the model, and
`compute_rows` solves every case in the dynamic-inputs file whatever `governing_periods`
says -- 66 s per `run()` on the shipped file, which a loop multiplies. The fixture trims
`case{i}/lam` to its first `TRIMMED_STEPS` timesteps, ONE VARIABLE, and
`test_the_TRIMMED_fixture_reproduces_the_SHIPPED_governing_figure` asserts that the
governing utilisation is the shipped `1.71167` to six digits -- measured, not assumed, and
2.6 s instead of 66. A fixture that changed the answer would be a different model and the
cells below would be about it instead.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.run.config import ConfigError, RunConfig, TubeSection, load_config
from floatfea.run.pipeline import RunResult
from floatfea.run.pipeline import run as run_pipeline
from floatfea.run.sizing import resolve_until_admissible, size_required_sections

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "platform12_placeholder.yaml"

TRIMMED_STEPS = 40
"""Timesteps kept per case. See the module docstring, and the cell that measures it."""

SHIPPED_GOVERNING_U = 1.71167
"""Step 1's pinned figure: `U` at `platform:hub4_arm` ROOT on the declared sections.

Not a tolerance -- a golden value, compared at the six digits the CLI prints.
"""

# Walls measured on this fixture, one variable each, all with the hubs at the declared
# 0.180 m. They are what the grids below are built from:
#
#     platform wall 0.180 m -> U = 1.71167   (the declared section; FAILS)
#     platform wall 0.300 m -> U = 1.18950   (FAILS)
#     platform wall 0.410 m -> U = 0.99570   (PASSES; f6a's search answer too)
#     platform wall 0.500 m -> U = 0.91067   (PASSES)
#     hub walls    0.180 m -> worst 0.80819  (PASSES)
#     hub walls    0.100 m -> worst 1.32040  (FAILS, at hub3:buoy9_arm)
WALL_FAILS = 0.180
WALL_FAILS_LESS = 0.300
WALL_PASSES = 0.410
WALL_HUB_FAILS = 0.100


def _tube(wall: float) -> dict[str, float]:
    return {"d_outer": 2.5, "wall": wall}


def _fixture(
    tmp_path: Path,
    *,
    candidates: dict[str, list[dict[str, float]]] | None = None,
    hub_wall: float = WALL_FAILS,
    required_section: bool = False,
    truss_sizing: bool = False,
    truss: dict[str, object] | None = None,
) -> tuple[Path, Path]:
    """The shipped example in `tmp_path`, with `case{i}/lam` trimmed. Returns config, out.

    Everything else is the shipped file: the deck, the sidecar, the provenance, the
    governing set, the material, the code-check options. The npz is COPIED first, so no
    cell can touch the committed data.
    """
    data: dict[str, Any] = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    src = (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()
    local = tmp_path / "data"
    local.mkdir(exist_ok=True)
    shutil.copy2(src, local / src.name)
    shutil.copy2(src.with_suffix(".provenance.json"), local / f"{src.stem}.provenance.json")
    npz = local / src.name
    raw = np.load(npz, allow_pickle=False)
    # **`times` IS TRIMMED WITH `lam`, AND R1063 IS WHY.** The first version of this
    # fixture trimmed `lam` alone and left `times` at full length -- a file disagreeing
    # with ITSELF about how long its window is, which is exactly what
    # `checked_joint_reactions` now refuses. So this was synthesising an invalid file to
    # test something else, and trimming both makes it a legitimate input rather than one
    # that happened to pass. `m_xddot` is deliberately left alone: it is `N + 1` by design.
    trim = ("/lam", "/times")
    np.savez(
        npz,
        **{k: (raw[k][:TRIMMED_STEPS] if k.endswith(trim) else raw[k]) for k in raw.files},
    )
    data["load_cases"]["npz"] = str(npz)
    for name in ("hub1", "hub2", "hub3", "hub4"):
        data["sections"]["groups"][name]["wall"] = hub_wall
    if candidates is not None:
        data["sections"]["candidates"] = candidates
    out_dir = tmp_path / "out"
    data["outputs"]["directory"] = str(out_dir)
    data["outputs"]["required_section"] = required_section
    data["outputs"]["truss_sizing"] = truss_sizing
    if truss is not None:
        data["sections"]["truss"] = truss
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path, out_dir


def _propose_the_smallest(
    _cfg: RunConfig, _baseline: RunResult, _group: str, _grid: Any
) -> tuple[int, float]:
    """A proposer that always proposes candidate 0, for the cells about the LOOP.

    **IT IS NOT A STUB STANDING IN FOR THE REAL PROPOSER; it is the reason
    `resolve_until_admissible` takes one.** The fixed-force proposer is very good on this
    model -- `test_the_PREMISE_error_is_measured_rather_than_assumed` finds the two `max U`
    values equal at the six digits either is printed at, and
    `results/F6a/premise_check.json` measures the same quantity independently at `1.554e-14`
    for the platform group -- so the proposal it makes is almost always accepted on the
    first re-solve, and the stepping branch, the iteration record and the exhaustion
    refusal would be reached only by an exhausting grid. FT2.5's `truss_sizing` proposer
    is a second real one and the loop must not depend on either being good.

    The `nan` is the fixed-force `max U`, which this proposer does not compute. It is
    reported as `nan` rather than as a number nobody measured.
    """
    return 0, float("nan")


# ---------------------------------------------------------------------------
# The fixture itself
# ---------------------------------------------------------------------------
def test_the_TRIMMED_fixture_reproduces_the_SHIPPED_governing_figure(tmp_path) -> None:
    """`TRIMMED_STEPS` timesteps give step 1's pinned `U = 1.71167`, to six digits.

    If this is red the cells below are measuring a different model from the one the gate
    pins, and their walls and grids mean nothing.
    """
    path, _out = _fixture(tmp_path)
    result = run_pipeline(load_config(path))
    governing = result.governing()
    # not-a-tolerance: a GOLDEN comparison, which `CLAUDE.md` section Tolerances
    # distinguishes from a threshold in those words -- "FL1(c)'s `exactly` is a golden
    # comparison". `SHIPPED_GOVERNING_U` is step 1's pinned figure and the `:.6g` is the
    # precision the CLI PRINTS it at, not a window: both sides are rounded the same way
    # and then compared exactly, so there is no value here that could be loosened to make
    # two numbers agree.
    printed = float(f"{float(governing['utilisation']):.6g}")
    assert printed == SHIPPED_GOVERNING_U, governing  # not-a-tolerance: golden
    assert governing["member"] == "platform:hub4_arm", governing
    assert governing["station"] == "ROOT", governing


# ---------------------------------------------------------------------------
# The loop
# ---------------------------------------------------------------------------
def test_the_PROPOSAL_is_accepted_when_the_RESOLVE_agrees(tmp_path) -> None:
    """One re-solve: the fixed-force proposal lands on a candidate the re-solve accepts.

    The grid is three walls, of which only the last passes. The proposer therefore
    proposes candidate 2, the re-solve at candidate 2 gives `U <= 1.0`, and the loop stops
    there -- `1` re-solve, which is FM0's iteration count.
    """
    path, _out = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_FAILS_LESS), _tube(WALL_PASSES)]},
        required_section=True,
    )
    cfg = load_config(path)
    report = size_required_sections(cfg, run_pipeline(cfg))

    assert report.iteration_count == 1, report.iterations
    assert len(report.groups) == 1, report.groups
    (platform,) = report.groups
    assert platform.group == "platform"
    assert platform.proposed_index == 2, platform
    assert platform.chosen_index == 2, platform
    assert platform.chosen == TubeSection(d_outer=2.5, wall=WALL_PASSES), platform
    # The groups with no grid are NAMED, not omitted: their declared sections are carried
    # into the re-solve, so a reader has to know which sections the figures came from.
    assert report.unsized == ("hub1", "hub2", "hub3", "hub4"), report.unsized


def test_the_PREMISE_error_is_measured_rather_than_assumed(tmp_path) -> None:
    """FM0's reporting requirement: the two `max U` values, side by side.

    This is the number the retired threshold would have hidden by either passing or
    refusing. On this configuration the premise is very good -- the fixed-force and
    re-solved values agree far beyond the six digits either is printed at -- and that is
    the finding, consistent with `results/F6a/premise_check.json`'s independent
    measurement of the same thing (`hubs max U 0.991135 -> 0.991139` on a rebuild).

    **The assertion is that BOTH NUMBERS EXIST AND AGREE AT THE PRINTED PRECISION**, not
    that they agree to machine precision: the premise error is a property of this
    configuration, and a cell that pinned it to 1e-14 would be asserting that no future
    deck may have a worse one.
    """
    path, _out = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_PASSES)]},
        required_section=True,
    )
    cfg = load_config(path)
    report = size_required_sections(cfg, run_pipeline(cfg))
    (platform,) = report.groups
    assert f"{platform.proposed_fixed_force_u:.6g}" == f"{platform.resolved_u:.6g}", platform
    assert platform.resolved_u <= 1.0, platform


def test_the_LOOP_STEPS_UP_and_records_every_RESOLVE(tmp_path) -> None:
    """Three re-solves, on a proposer that proposes the smallest candidate every time.

    Walls 0.180 and 0.300 both re-solve above 1.0 and 0.410 does not, so the loop steps
    twice and accepts on the third. What is asserted is the WALK -- which section each
    re-solve ran at, and that each iteration's record names its own worst station -- rather
    than only the answer, because "converged in 3 iterations" hides which group drove it.
    """
    path, _out = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_FAILS_LESS), _tube(WALL_PASSES)]},
        required_section=True,
    )
    cfg = load_config(path)
    report = resolve_until_admissible(
        cfg,
        run_pipeline(cfg),
        "required_section",
        dict(cfg.sections.candidates),
        _propose_the_smallest,
    )

    assert report.iteration_count == 3, [it.grid_index for it in report.iterations]
    assert [it.grid_index["platform"] for it in report.iterations] == [0, 1, 2]
    assert [it.sections["platform"].wall for it in report.iterations] == [
        WALL_FAILS,
        WALL_FAILS_LESS,
        WALL_PASSES,
    ]
    walk = [float(it.group_worst["platform"]["utilisation"]) for it in report.iterations]
    assert walk[0] > 1.0 and walk[1] > 1.0 and walk[2] <= 1.0, walk
    # STRICTLY DECREASING, which is the property that makes "steps the section up"
    # meaningful: a larger section at the same loads must not be worse.
    assert walk[0] > walk[1] > walk[2], walk
    (platform,) = report.groups
    assert platform.proposed_index == 0 and platform.chosen_index == 2, platform


def test_an_EXHAUSTED_grid_REFUSES_and_names_the_group_and_the_case(tmp_path) -> None:
    """FM0: exhaustion refuses. It does not report the last candidate as a section.

    Driven on the smallest-first proposer so that both entries are walked. The refusal has
    to carry the group, the largest candidate declared, the governing station with its
    period and clause, and the re-solve count -- without them a reader cannot tell a grid
    that was too small from a structure that cannot be made to pass.
    """
    path, _out = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_FAILS_LESS)]},
        required_section=True,
    )
    cfg = load_config(path)
    with pytest.raises(ConfigError) as caught:
        resolve_until_admissible(
            cfg,
            run_pipeline(cfg),
            "required_section",
            dict(cfg.sections.candidates),
            _propose_the_smallest,
        )
    message = str(caught.value)
    assert "exhausted" in message, message
    assert "`platform`" in message, message
    assert f"wall {WALL_FAILS_LESS:g} m" in message, message
    # R1067: the DISPLAY is 1-based, so the second of two candidates reads "2 of 2".
    assert "candidate 2 of 2" in message, message
    assert "platform:hub4_arm ROOT" in message, message
    assert "T_full = 12.5 s" in message, message
    assert "3.3.2 interaction" in message, message
    assert "2 re-solve(s)" in message, message


def test_a_sized_model_with_an_UNSIZED_group_over_1_REFUSES(tmp_path) -> None:
    """Every group with a grid passes, and the model does not. That is not a pass.

    The platform is sized to the wall that passes; the hub groups are left at 0.100 m,
    where the worst hub station is 1.32040, and no grid is declared for them -- so the loop
    cannot step them. Accepting here would publish `required_section.md` with a chosen
    section and an admissible `max U` for the one group it sized, which a reader would take
    as a structure that passes.

    A validation failure does not degrade to a warning (`CLAUDE.md`), so the refusal names
    the group, says it has no grid, and says what to do about it.
    """
    path, out_dir = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_PASSES)]},
        hub_wall=WALL_HUB_FAILS,
        required_section=True,
    )
    cfg = load_config(path)
    with pytest.raises(ConfigError) as caught:
        size_required_sections(cfg, run_pipeline(cfg))
    message = str(caught.value)
    assert "the model does not" in message, message
    assert "`hub3`" in message, message
    assert "declares no grid" in message, message
    assert not out_dir.exists() or sorted(out_dir.glob("*")) == [], list(out_dir.glob("*"))


def test_NO_GRID_AT_ALL_REFUSES_rather_than_reporting_an_empty_analysis(tmp_path) -> None:
    """`required_section: true` with no `sections.candidates` has nothing to step through.

    Reported as an analysis that found nothing, this would be indistinguishable from one
    where no candidate passed.
    """
    path, _out = _fixture(tmp_path, required_section=True)
    cfg = load_config(path)
    with pytest.raises(ConfigError) as caught:
        size_required_sections(cfg, run_pipeline(cfg))
    message = str(caught.value)
    assert "declares no grid" in message, message
    assert "different answers" in message, message


# ---------------------------------------------------------------------------
# End to end, through the real CLI -- which is what WRITES
# ---------------------------------------------------------------------------
def test_END_TO_END_the_CLI_writes_required_section_md_with_both_max_U_values(
    tmp_path,
) -> None:
    """The artifact, through `floatfea.cli.main`, beside the other three.

    FT2's standing rule is that every repair's CALLER is held by a test: a correct loop
    that nothing called was three findings in this step already.
    """
    from floatfea import cli

    path, out_dir = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_FAILS_LESS), _tube(WALL_PASSES)]},
        required_section=True,
    )
    assert cli.main(["run", str(path)]) == 0
    assert sorted(p.name for p in out_dir.glob("*")) == [
        "member_forces.csv",
        "report.md",
        "required_section.md",
        "utilisation.csv",
    ]
    text = (out_dir / "required_section.md").read_text(encoding="utf-8")
    assert "**1 re-solve(s).**" in text, text
    assert "fixed-force max U" in text and "re-solved max U" in text, text
    assert "| platform | 3 of 3 | 2.5 | 0.41 |" in text, text
    # The unsized groups are named IN THE ARTIFACT, with their declared sections.
    for name in ("hub1", "hub2", "hub3", "hub4"):
        assert f"`{name}` — declared d_outer 2.5 m, wall 0.18 m" in text, text
    # The whole-model verdict at the chosen sections, which is the line that keeps a
    # per-group `max U <= 1.0` from reading as a structure that passes.
    assert "the WHOLE model re-solves to **U = 0.995702**" in text, text


def test_END_TO_END_an_EXHAUSTED_grid_WRITES_NOTHING(tmp_path, capsys) -> None:
    """R809, at this very flag: a refusal after the artifacts is a warning, not a refusal.

    R809 was exactly this shape -- the old blanket refusal for `required_section` sat at
    the END of `_cmd_run`, so the flag wrote `member_forces.csv`, `utilisation.csv` and
    `report.md`, printed the governing `U`, and THEN exited 2. The sizing loop can refuse
    too, so it runs before any write.

    The grid here is the declared wall alone, on the REAL proposer: no candidate passes on
    the fixed forces, so it proposes candidate 0, the re-solve rejects it and there is
    nowhere to step.
    """
    from floatfea import cli

    path, out_dir = _fixture(
        tmp_path, candidates={"platform": [_tube(WALL_FAILS)]}, required_section=True
    )
    # `cli.main` CATCHES `ConfigError` and returns 2 with the message on stderr, which is
    # the behaviour a user sees: a message rather than a traceback. So the exit code and
    # the message are what this cell reads, not a raised exception.
    assert cli.main(["run", str(path)]) == 2
    assert "exhausted" in capsys.readouterr().err
    assert not out_dir.exists() or sorted(out_dir.glob("*")) == [], list(out_dir.glob("*"))


def test_truss_sizing_alone_is_WIRED_and_does_NOT_refuse(tmp_path, capsys) -> None:
    """The weakening direction of FT2.5's wiring, and a cell that had to be REWRITTEN.

    **IT USED TO ASSERT THE OPPOSITE, AND THE SUITE IS WHAT CAUGHT THAT.** Until FT2.5 this
    cell asserted that `truss_sizing` was still REFUSED and that the message named FT2.5 as
    what was missing -- and it was right at the time: FT2.4 narrowed a blanket refusal from
    both optional analyses to `truss_sizing` alone, and the weakening direction worth
    holding was that the narrowing had not removed the refusal altogether. FT2.5 then wired
    the flag, which made that assertion false -- and it failed in the regression run rather
    than being noticed, which is the behaviour a golden suite is for.

    (The old cell is described rather than named, because
    `tests/test_collected_set_golden.py` refuses prose that cites a test which no longer
    exists -- and it caught this docstring's first draft doing exactly that.)

    What is worth holding NOW is the other side: `truss_sizing: true` ALONE runs, writes
    `truss_sizing.md`, and does not refuse. Its own file holds the rest -- the artifact's
    content, the disclaimer, and the refusal when BOTH flags are set, which is where the
    old cell's concern now lives.
    """
    from floatfea import cli

    path, out_dir = _fixture(
        tmp_path,
        candidates={"platform": [_tube(WALL_FAILS), _tube(WALL_PASSES)]},
        truss={"depths": [8.0], "widths": [3.0], "shapes": ["box"]},
        truss_sizing=True,
    )
    assert cli.main(["run", str(path)]) == 0, capsys.readouterr().err
    assert sorted(p.name for p in out_dir.glob("*")) == [
        "member_forces.csv",
        "report.md",
        "truss_sizing.md",
        "utilisation.csv",
    ]


def test_MORE_THAN_ONE_GROUP_steps_in_the_SAME_pass(tmp_path) -> None:
    """The configuration none of the cells above chose: every sized group over 1.0 at once.

    Five grids, all starting at a wall that fails -- the platform at 0.180 m and all four
    hub groups at 0.100 m -- on the smallest-first proposer. One pass finds all five over
    1.0 and steps all five, and the second re-solve accepts. So the loop does not step one
    group at a time and leave the rest, which is the shape that would have published a
    first-group answer produced at four other groups' failing sections.

    **AND IT IS THE CELL THAT SAYS THE OUTER PASS IS REACHED**, which the single-group
    cells cannot: with one grid, "re-read every sized group from this re-solve" and "re-read
    the group I just stepped" are the same thing.
    """
    path, _out = _fixture(
        tmp_path,
        candidates={
            "platform": [_tube(WALL_FAILS), _tube(WALL_PASSES)],
            "hub1": [_tube(WALL_HUB_FAILS), _tube(WALL_FAILS)],
            "hub2": [_tube(WALL_HUB_FAILS), _tube(WALL_FAILS)],
            "hub3": [_tube(WALL_HUB_FAILS), _tube(WALL_FAILS)],
            "hub4": [_tube(WALL_HUB_FAILS), _tube(WALL_FAILS)],
        },
        hub_wall=WALL_HUB_FAILS,
        required_section=True,
    )
    cfg = load_config(path)
    report = resolve_until_admissible(
        cfg,
        run_pipeline(cfg),
        "required_section",
        dict(cfg.sections.candidates),
        _propose_the_smallest,
    )

    assert report.iteration_count == 2, [it.grid_index for it in report.iterations]
    first, second = report.iterations
    assert set(first.grid_index) == {"platform", "hub1", "hub2", "hub3", "hub4"}
    assert set(first.grid_index.values()) == {0}, first.grid_index
    assert set(second.grid_index.values()) == {1}, second.grid_index
    # EVERY sized group was over on the first pass, and every one was stepped.
    assert all(float(row["utilisation"]) > 1.0 for row in first.group_worst.values())
    assert all(float(row["utilisation"]) <= 1.0 for row in second.group_worst.values())
    assert report.unsized == (), report.unsized
    assert {g.group: g.chosen_index for g in report.groups} == {
        "platform": 1,
        "hub1": 1,
        "hub2": 1,
        "hub3": 1,
        "hub4": 1,
    }
