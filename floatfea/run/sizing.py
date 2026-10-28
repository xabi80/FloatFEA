"""FT2.4/FT2.5: propose a section from fixed forces, then RE-SOLVE at it (FM0).

**ONE LOOP, TWO PROPOSERS.** `required_section` and `truss_sizing` differ only in what
they propose candidates from. The loop -- propose, re-solve, compare `U` to 1.0, step the
grid, refuse on exhaustion, report the iteration count and BOTH `max U` values -- is
identical, and writing it twice is the defect R983 named. So `resolve_until_admissible`
takes a proposer; `propose_from_fixed_forces` is FT2.4's.

WHAT FM0 RETIRED, AND WHY THE SHAPE IS THIS WAY. An earlier revision of the plan put a
THRESHOLD on FG2's premise -- that section choice does not change the member forces -- and
sent its derivation to a lock Q&A. Directive FM0 ruled otherwise:

    FG2's premise is NOT checked by a threshold. The sizing analyses (`required_section`,
    `truss_sizing`) use fixed forces only to PROPOSE candidates. The tool then RE-SOLVES
    the FE model (static + dynamic) with the selected sections and reports `max U` from
    that re-solve. If `U > 1.0`, it steps the section up and re-solves, looping until
    `U <= 1.0` or the grid is exhausted (and then refuses). Report the iteration count and
    the fixed-force vs re-solved `max U`.

A threshold asks *is the premise true enough to trust the fixed forces?* -- a question
whose answer depends on the frame, the section spread and the heading. The re-solve does
not ask it at all: the fixed-force pass becomes a PROPOSAL MECHANISM whose only duty is to
land near the answer, and correctness comes from an ordinary FE solve at the sections
actually chosen. Determinate and indeterminate frames take the same code path, which is
what a tool for an unknown configuration needs.

**NO TOLERANCE, AND THE PLAN SAYS SO IN ITS OWN WORDS.** `U <= 1.0` is API RP 2A-WSD's
acceptance criterion, not a comparison epsilon; the grid is the configuration's declared
section list; the loop terminates on that grid or refuses. Nothing here is chosen to make
two numbers agree, and if a number were needed to make the loop terminate that would be a
misreading of FM0 rather than a case for an entry in `floatfea/tolerances.py`.

**WHY THE RE-SOLVE GOES THROUGH `run()` AND NOT THROUGH A PRIVATE SOLVE PATH.** FM0 asks
for an ordinary solve at the chosen sections. `run()` IS that solve, with every refusal
the production path carries -- the scale agreement, the period records, the band screen,
the material and admissibility checks. A second assembly path here would be a second
answer, and the first configuration it disagreed with would be the one nobody re-ran.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence
from dataclasses import dataclass, replace
from typing import Any

from floatfea.run.config import ConfigError, RunConfig, TubeSection
from floatfea.run.pipeline import RunResult, _utilisations, build_model
from floatfea.run.pipeline import run as run_pipeline

__all__ = [
    "GroupSizing",
    "SizingIteration",
    "SizingReport",
    "propose_from_fixed_forces",
    "resolve_until_admissible",
    "size_required_sections",
    "with_group_sections",
]


def with_group_sections(cfg: RunConfig, chosen: dict[str, TubeSection]) -> RunConfig:
    """`cfg` with the named groups' tubes replaced, everything else identical.

    The declared config is frozen and stays so: each iteration gets its own value rather
    than mutating the one the run was validated from, because a report that printed the
    configuration after the loop had walked over it would describe the last candidate as
    though it had been declared.

    `raw` is carried through unchanged ON PURPOSE. It is the provenance of what was
    DECLARED, and the sizing report states the sections it actually used; rewriting `raw`
    would leave nothing in the run that remembers what the file said.
    """
    groups = dict(cfg.sections.groups)
    unknown = sorted(set(chosen) - set(groups))
    if unknown:
        raise ConfigError(
            f"sizing asked for sections {unknown}, which are not member groups of this "
            f"model -- it has {sorted(groups)}. Substituting them would build the declared "
            f"section and report the substituted one."
        )
    groups.update(chosen)
    return replace(cfg, sections=replace(cfg.sections, groups=groups))


def max_utilisation(records: Sequence[dict[str, Any]], group: str) -> dict[str, Any]:
    """The worst checked station of one member group, with its whole row.

    **NOT AN AVERAGE (`CLAUDE.md`).** The row is carried rather than the number, because
    the loop's refusal has to name the governing case and the report has to name the
    clause -- and a maximum reduced to a float cannot.
    """
    rows = [r for r in records if r["body"] == group]
    if not rows:
        raise ConfigError(
            f"no checked station belongs to member group `{group}`, so there is nothing "
            f"to size it against. The screen covered "
            f"{sorted({str(r['body']) for r in records})}."
        )
    return max(rows, key=lambda r: float(r["utilisation"]))


def propose_from_fixed_forces(
    cfg: RunConfig,
    baseline: RunResult,
    group: str,
    grid: Sequence[TubeSection],
) -> tuple[int, float]:
    """FT2.4's proposer: the first candidate that passes ON THE BASELINE FORCES.

    Returns `(index, max U at that index)`. **The `max U` returned is the FIXED-FORCE
    one** -- the number FM0 asks to be reported beside the re-solved one, because the gap
    between them is the premise's error measured rather than assumed.

    The clauses are evaluated through `_utilisations`, the SAME function the production
    screen uses, with the candidate's own built model supplying the section properties and
    `K L / r` and the BASELINE rows supplying the forces. That is what "fixed forces" means
    here, and routing it through the production screen rather than re-deriving the clause
    calls is the difference between a proposal mechanism and a second code check.

    **If no candidate passes on the fixed forces the proposal is index 0**, not the last
    entry: the loop steps UP from there and reports each step, so the artifact shows the
    whole walk rather than jumping to the end of a grid that may pass earlier than the
    fixed-force pass predicted. The two can differ in either direction -- that is the
    premise error FM0 wants visible -- and starting low is the direction that cannot skip
    an admissible section.
    """
    at_zero = math.nan
    for i, candidate in enumerate(grid):
        trial = with_group_sections(cfg, {group: candidate})
        records = _utilisations(trial, build_model(trial), baseline.rows)
        worst = float(max_utilisation(records, group)["utilisation"])
        if i == 0:
            at_zero = worst
        if worst <= 1.0:
            return i, worst
    return 0, at_zero


@dataclass(frozen=True)
class SizingIteration:
    """One re-solve: the sections it ran at, and what came out of it."""

    index: int
    sections: dict[str, TubeSection]
    grid_index: dict[str, int]
    group_worst: dict[str, dict[str, Any]]
    """Per sized group, the worst checked station of the RE-SOLVE, whole row."""

    governing: dict[str, Any]
    """The worst station of the WHOLE model at this iteration, sized groups or not."""


@dataclass(frozen=True)
class GroupSizing:
    """What one member group was sized to, and the two `max U` values for it."""

    group: str
    grid: tuple[TubeSection, ...]
    proposed_index: int
    proposed_fixed_force_u: float
    chosen_index: int
    chosen: TubeSection
    resolved_u: float


@dataclass(frozen=True)
class SizingReport:
    """Everything one sizing analysis produced. FM0's reporting requirement, as data."""

    analysis: str
    iterations: tuple[SizingIteration, ...]
    groups: tuple[GroupSizing, ...]
    unsized: tuple[str, ...]
    """Member groups the model builds for which no grid was declared.

    Named rather than omitted: their declared section is carried into every re-solve, so a
    reader has to know which sections the published `max U` was produced at and which of
    them the analysis chose.
    """

    final: RunResult

    @property
    def iteration_count(self) -> int:
        """The number of RE-SOLVES, which is what FM0 asks to be reported."""
        return len(self.iterations)


def resolve_until_admissible(
    cfg: RunConfig,
    baseline: RunResult,
    analysis: str,
    grids: dict[str, Sequence[TubeSection]],
    propose: Callable[[RunConfig, RunResult, str, Sequence[TubeSection]], tuple[int, float]],
    progress: Callable[[str], None] | None = None,
) -> SizingReport:
    """FM0's loop. Propose, re-solve, step the grid on `U > 1.0`, refuse on exhaustion.

    **EVERY SIZED GROUP IS RE-READ FROM EVERY RE-SOLVE, not only the one just stepped.**
    One pass steps every group that is over 1.0, and the next pass reads all of them again
    from the new solve. `test_MORE_THAN_ONE_GROUP_steps_in_the_SAME_pass` is the cell for
    the first half; **the second half is a property this model does not exercise, and the
    honest statement is the bound rather than the mechanism.** Changing one group's section
    does redistribute into the others, so in principle a group accepted earlier can be
    pushed back above 1.0 -- but on this deck the redistribution is tiny:
    `results/F6a/premise_check.json` measures `max U` moving by at most `3.496e-06` when
    the model is rebuilt at a different section (hubs, `iii_min_area`), so a group would
    have to sit within that of 1.0 for the push-back to occur. The re-read is here because
    FM0's loop has to be right for a deck where it is not, and not because it has been seen
    to fire.

    **It terminates** because an index only ever rises and each grid is finite, so the
    number of re-solves is bounded by the total number of candidates declared.

    **EXHAUSTION REFUSES, naming the group and the governing case** (FM0). It does not
    report the last candidate as a section and it does not extend the grid.
    """
    say = progress or (lambda _line: None)
    if not grids:
        raise ConfigError(
            f"outputs.{analysis} is set and sections.candidates declares no grid, so there "
            f"is no section list to step through. FM0 requires the tool to walk a DECLARED "
            f"grid and forbids it extending one of its own, so this is refused rather than "
            f"reported as an analysis that found nothing: `no candidate passed` and `there "
            f"were no candidates` are different answers."
        )

    proposed: dict[str, tuple[int, float]] = {}
    for group in sorted(grids):
        index, fixed_u = propose(cfg, baseline, group, grids[group])
        proposed[group] = (index, fixed_u)
        say(
            f"  {analysis}: {group} proposed candidate {index} of "
            f"{len(grids[group])} at fixed-force max U = {fixed_u:.6g}"
        )

    at: dict[str, int] = {group: index for group, (index, _u) in proposed.items()}
    iterations: list[SizingIteration] = []
    while True:
        sections = {group: grids[group][at[group]] for group in at}
        trial = with_group_sections(cfg, sections)
        say(f"  {analysis}: re-solve {len(iterations) + 1} at {_spell(sections)}")
        result = run_pipeline(trial)
        worst = {group: max_utilisation(result.utilisations, group) for group in at}
        iterations.append(
            SizingIteration(
                index=len(iterations) + 1,
                sections=dict(sections),
                grid_index=dict(at),
                group_worst=worst,
                governing=result.governing(),
            )
        )
        over = sorted(g for g in at if float(worst[g]["utilisation"]) > 1.0)
        if not over:
            # **THE WHOLE MODEL, NOT ONLY THE GROUPS WITH GRIDS.** Without this the
            # analysis would publish a chosen section and an admissible `max U` for every
            # group it sized while some group it could NOT size sat above 1.0 -- and a
            # reader of `required_section.md` would take the structure as adequate. The
            # loop cannot step a group that has no declared grid, so this is a refusal
            # naming the group rather than a note: a validation failure does not degrade
            # to a warning (`CLAUDE.md`).
            gov = result.governing()
            if float(gov["utilisation"]) > 1.0:
                raise ConfigError(
                    f"outputs.{analysis}: every member group with a declared candidate "
                    f"grid re-solves at or below U = 1.0, but the model does not. The "
                    f"governing station is {gov['member']} {gov['station']} at U = "
                    f"{float(gov['utilisation']):.6g}, T_full = "
                    f"{float(gov['period_full_s']):g} s, clause "
                    f"{gov['governing_clause']} -- in member group `{gov['body']}`, for "
                    f"which sections.candidates declares no grid, so this loop has "
                    f"nothing to step it through. Sizing {sorted(at)} and publishing an "
                    f"admissible max U for each would read as a structure that passes. "
                    f"Declare a candidate grid for `{gov['body']}` as well, or size it "
                    f"outside this analysis."
                )
            groups = tuple(
                GroupSizing(
                    group=group,
                    grid=tuple(grids[group]),
                    proposed_index=proposed[group][0],
                    proposed_fixed_force_u=proposed[group][1],
                    chosen_index=at[group],
                    chosen=sections[group],
                    resolved_u=float(worst[group]["utilisation"]),
                )
                for group in sorted(at)
            )
            return SizingReport(
                analysis=analysis,
                iterations=tuple(iterations),
                groups=groups,
                unsized=tuple(sorted(set(cfg.sections.groups) - set(at))),
                final=result,
            )
        for group in over:
            if at[group] + 1 >= len(grids[group]):
                row = worst[group]
                raise ConfigError(
                    f"outputs.{analysis}: the candidate grid for member group `{group}` is "
                    f"exhausted and `max U` is still above 1.0. The largest candidate "
                    f"declared -- d_outer {sections[group].d_outer:g} m, wall "
                    f"{sections[group].wall:g} m, candidate {at[group]} of "
                    f"{len(grids[group])} -- re-solves to U = "
                    f"{float(row['utilisation']):.6g} at {row['member']} {row['station']}, "
                    f"T_full = {float(row['period_full_s']):g} s, governed by clause "
                    f"{row['governing_clause']} after {len(iterations)} re-solve(s). This "
                    f"is refused rather than reported: the last candidate is not a section "
                    f"the structure passes at, and FM0 forbids the tool extending the grid "
                    f"on its own. Declare larger candidates in sections.candidates."
                )
            at[group] += 1
            say(f"  {analysis}: {group} steps up to candidate {at[group]}")


def _spell(sections: dict[str, TubeSection]) -> str:
    """The sections of one iteration, for the progress line."""
    return ", ".join(
        f"{g} D={sections[g].d_outer:g} t={sections[g].wall:g}" for g in sorted(sections)
    )


def size_required_sections(
    cfg: RunConfig,
    baseline: RunResult,
    progress: Callable[[str], None] | None = None,
) -> SizingReport:
    """`outputs.required_section` (FT2.4): FM0's loop with the fixed-force proposer."""
    return resolve_until_admissible(
        cfg,
        baseline,
        "required_section",
        {group: grid for group, grid in cfg.sections.candidates.items()},
        propose_from_fixed_forces,
        progress,
    )
