"""`floatfea run` and `floatfea export` (FL1(b)).

Two commands, one configuration file. `run` builds, solves, computes member forces,
screens them against API RP 2A-WSD and writes the outputs. `export` produces a
dynamic-inputs file from FloatSim runs and needs the HSP worktree, which is kept
separate on purpose -- `docs/hsp-coupling.md` -- so that `run` works on committed data
with no HSP present.

A `ConfigError` prints as a message and exits non-zero, WITHOUT a traceback: a traceback
for a typo in a YAML file tells the reader nothing they can act on. Anything else
propagates, because an unexpected failure in the solve is not something this layer should
be swallowing.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any, Final

from floatfea.basis import BREAKING_STEEPNESS_LIMIT
from floatfea.post.forces_table import _stresses
from floatfea.post.member_forces import COMPONENTS
from floatfea.run.config import ConfigError, RunConfig, load_config
from floatfea.run.pipeline import RunResult
from floatfea.run.pipeline import run as run_pipeline
from floatfea.run.sizing import (
    SizingReport,
    TrussReport,
    ordinal,
    position,
    size_required_sections,
    size_truss,
)

__all__ = ["main"]

LABEL = (
    "INDICATIVE SIZING SCREEN -- NOT A CODE CASE. Produced by `floatfea run` from a "
    "declared configuration. The section is a stiffness stand-in for a truss of "
    "undecided depth (docs/milestones/F1.md:389-390)."
)

WALL_TIME_STAGES: Final[tuple[str, ...]] = (
    "build",
    "load",
    "solve",
    "code_check",
    "total",
)
"""The stages the published report's `| stage | seconds |` table carries, in order.

**A MODULE CONSTANT BECAUSE A HAND COPY OF IT DRIFTED ONCE ALREADY (R860).** This was a
literal inside `_write_report`, and the gate that excludes these rows from its byte
comparison -- `tests/regression/test_r1_example_regenerates.py` -- carried its own copy
naming three of the five. `| load |` and `| code_check |` then sat inside the comparison
as sub-10-ms values printed at two decimals, so the row flipped between `0.00` and `0.01`
at 5 ms and the gate was machine-dependent (R850).

Repairing that by writing five names in the test would have left the drift that caused it:
these rows are WALL CLOCKS, so a sixth stage must be excluded the moment it is published,
and the test cannot know. **FL2 is what makes that live** -- a `truss_sizing` re-solve loop
that times itself adds exactly such a row -- so the tuple is exported and the gate imports
it rather than restating it.
"""

STUDY_LABEL = "STUDY -- NOT FOR DESIGN. "
"""FN1. Prefixed to every label and header when `study_only` is set.

A study run is one the shipped builder would never have reached -- a mass distribution
that fails `admissible()`, or members below the declared density floor. It is permitted
only behind the flag, and then it says so on every artifact it writes, because the one
thing worse than refusing a study is publishing one that reads like a design.
"""

TABLE_CAVEATS = (
    "R739: the N column is TENSION-POSITIVE (docs/conventions.md:320). Published "
    "compression-positive it put every over-unity station on section 3.3.1 instead of "
    "3.3.2.",
    "R740: a utilisation must be read from the `total_instant` rows -- the six components "
    "AT the step where sigma peaks. `total_max` / `total_min` max each component "
    "INDEPENDENTLY over the window, so their six values do not occur together and a "
    "stress formed from them is an UPPER BOUND, not a stress at any instant.",
    "FA3: ROOT and TIP are the element's two ends and are exact. MID is a closed form "
    "whose bending term is a measured 4.0% approximation, unverified against a refined "
    "mesh (R730).",
    "EZ2: only the declared governing periods may set the envelope. Cases outside the "
    "associated-period range for this wave height -- and any exceeding the deep-water "
    "breaking steepness -- are reported as SENSITIVITY ONLY and cannot govern.",
    "EX3 / R724: where a run covers a SINGLE heading the heading dependence is UNTESTED, "
    "and no column here is evidence about any other heading. The heading itself is in the "
    "wave-basis line above WHEN THE EXPORT RECORDED ONE; that line says so either way.",
    "FA0: a governing period sitting just below the associated-period band's lower "
    "bound is admitted by FA0's ruling rather than by rounding. Which period governs is "
    "a RESULT of this run and is in the period column; it is not a property of the "
    "band.",
    "FA1: a generic 0.6*Fy reference stress is NOT the API bending allowable and is "
    "SUPERSEDED by the clause results in these columns. Section 3.2.3's branches decide "
    "the bending allowable from D/t, not from 0.6*Fy.",
    "R741 / R742 / FQ0: section 3.2.2(b) local buckling is implemented and applies for "
    "60 < D/t <= 300. Section 3.2.3's third range ends at a FLAT D/t <= 300 -- not a "
    "grade-dependent limit -- above which the section is refused rather than "
    "extrapolated. F_b = 0.75*Fy IS the compact allowable; section 3.2.3's reductions "
    "apply above the compact limit, not below it. Every clause is verified against an "
    "independent hand calculation in tests/verification/rung5/.",
    "R743: C_m MULTIPLIES the bending term in section 3.3.1's interaction, so a LARGER "
    "C_m RAISES the compression utilisation. The value used is in the provenance above, "
    "and the run reports a one-variable sensitivity beside it.",
)
"""What the COLUMNS mean, which is the writer's business rather than the builder's.

**R806 IS WHY THIS EXISTS AND WHY IT IS SHORT.** The first version of these outputs
carried 11 header lines against the committed deliverables' 17 and 12, and the lines it
dropped were the ones that stop a reader misusing a column -- the tension sign, the
upper-bound caveat on 576 envelope rows, the MID approximation, the governing-basis rule
-- while `LABEL` claimed "every assumption it rests on is listed in the run report" and
the report mentioned none of them.

Everything that is a property of the BUILD is NOT repeated here. It is read from
`Superstructure.assumptions`, `Superstructure.label` and each body's `findings`, which the
builder generates, so those cannot go stale against the model the way a copied list does.
"""


def _header_lines(result: RunResult) -> list[str]:
    """Every label, assumption and finding this run rests on, for an artifact's header.

    Generated rather than typed: `Superstructure.assumptions` and each body's `findings`
    come from the builder, so a change in the model reaches every artifact without anyone
    remembering to copy it. R807 is the other half -- nine findings were being computed
    and discarded, five of them saying in as many words "this body is a MEASUREMENT, not
    one to ship".
    """
    study = STUDY_LABEL if result.config.study_only else ""
    lines = [study + LABEL]
    for key, value in result.config.provenance().items():
        lines.append(f"{key}: {value}")
    # R817: THE HEADING AND THE WAVE HEIGHT, which two of the caveats below are about and
    # which no artifact stated. `(not recorded)` rather than a guess when the export did
    # not write them.
    # **TWO BRANCHES, NOT FOUR FALLBACKS (R829 / FQ3).** This emitted one line with
    # `(not recorded)` substituted field by field, so a sidecar-less npz produced a file
    # carrying BOTH "the heading ... is in the provenance above" and
    # "heading (not recorded) deg" -- two sentences that cannot both be true. FL1(a) admits
    # such an npz, so this is a reachable state and not a hypothetical.
    #
    # `_write_report` already had the branch; the CSV path did not, which is why the
    # contradiction only appeared in two of the three artifacts.
    basis = result.wave_basis
    if basis:
        lines.append(
            "wave basis: heading {} deg, H_full {} m, H_model {} m; window {}".format(
                basis["heading_deg"],
                basis["wave_height_full_m"],
                basis["wave_height_model_m"],
                basis["window"],
            )
        )
    else:
        lines.append(
            "wave basis: NOT RECORDED by the export of this dynamic-inputs file. The "
            "heading and wave height of these loads are not stated by this run, and no "
            "caveat below should be read as supplying them."
        )
    if result.built.label:
        lines.append(f"build label: {result.built.label}")
    lines.extend(f"assumption: {a}" for a in result.built.assumptions)
    for body in result.built.bodies:
        lines.extend(f"finding: {f}" for f in body.findings)
    lines.extend(f"caveat: {c}" for c in TABLE_CAVEATS)
    if result.config.study_only:
        lines.append(
            "STUDY: this run's mass distribution is one the shipped builder would never "
            "have reached. It is permitted only because `study_only: true` is declared. "
            "Nothing here is a design value."
        )
    return lines


def _write_header(fh: Any, result: RunResult) -> None:
    """The header block, one `#` line each, commas stripped so a CSV reader is safe."""
    for line in _header_lines(result):
        fh.write("# " + line.replace(",", ";") + "\n")


def _write_member_forces(path: Path, result: RunResult) -> int:
    """F4's table, from this run. One row per (member, station, case, basis)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        _write_header(fh, result)
        writer = csv.writer(fh)
        writer.writerow(
            [
                "body",
                "member",
                "station",
                "period_full_s",
                "basis",
                *COMPONENTS,
                "sigma_Pa",
                "tau_Pa",
            ]
        )
        # The two derived columns are carried so this table has the same SHAPE as the
        # committed deliverable it regresses against, rather than only the same forces.
        # `_stresses` is the same function the measure script calls, so they cannot
        # disagree about what sigma means.
        members = {
            (body.name, member.label): member
            for body in result.built.bodies
            for member in body.members
        }
        for row in result.rows:
            period = "" if row.period_full_s != row.period_full_s else f"{row.period_full_s:g}"
            sigma, tau = _stresses(members[(row.body, row.member)], row.values)
            writer.writerow(
                [
                    row.body,
                    row.member,
                    row.station,
                    period,
                    row.basis,
                    *(f"{v:.6e}" for v in row.values),
                    f"{sigma:.6e}",
                    f"{tau:.6e}",
                ]
            )
    return len(result.rows)


def _write_utilisations(path: Path, result: RunResult) -> int:
    """F6's screen, from this run."""
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = result.utilisations
    with path.open("w", newline="", encoding="utf-8") as fh:
        _write_header(fh, result)
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {k: (f"{v:.6g}" if isinstance(v, float) else v) for k, v in row.items()}
            )
    return len(rows)


def _write_report(path: Path, result: RunResult) -> None:
    """The run report: what was configured, what it produced, and what it rests on.

    **THE GOVERNING ROW IS NAMED, NOT SUMMARISED.** `CLAUDE.md` forbids averaging a
    per-case diagnostic, so the worst station is reported with its member, station,
    period and clause, and the per-body mass residuals are listed one by one.
    """
    cfg = result.config
    governing = result.governing()
    study = STUDY_LABEL if cfg.study_only else ""
    lines: list[str] = [
        "# FloatFEA run report",
        "",
        f"**{study}{LABEL}**",
        "",
        "## What was configured",
        "",
    ]
    for key, value in cfg.provenance().items():
        lines.append(f"* **{key}** — {value}")

    lines += ["", "## The wave basis these loads were exported at", ""]
    basis = result.wave_basis
    if basis:
        lines += [
            f"* **heading** — {basis.get('heading_deg', '(not recorded)')} deg",
            f"* **wave height** — {basis.get('wave_height_full_m', '(not recorded)')} m "
            f"full scale ({basis.get('wave_height_model_m', '(not recorded)')} m model)",
            f"* **window** — {basis.get('window', '(not recorded)')}",
        ]
    else:
        lines.append(
            "* the dynamic-inputs file records no wave basis, so the heading and height "
            "of these loads are **not stated by this run**."
        )

    lines += ["", "## Sea-state admissibility, per case (FL2(d) / EZ2)", ""]
    screen = result.band_screen
    if not screen:
        lines.append(
            "* **the screen was NOT performed.** The band is a function of the recorded "
            "wave height and this dynamic-inputs file records none, so there is no band "
            "to test against. No height was assumed: a band computed from a guessed "
            "height would be indistinguishable in this report from one computed from a "
            "recorded one. Every case below is reported with no admissibility verdict."
        )
    else:
        declared_governing = set(result.config.load_cases.governing_periods)
        declared_override = set(result.config.load_cases.out_of_band_governing)
        lines += [
            f"The associated-period band at the recorded height is "
            f"`{screen[0].band_low_s:.3f} .. {screen[0].band_high_s:.3f} s`, and the "
            f"deep-water breaking limit is `H/lambda = 1/7 = "
            f"{BREAKING_STEEPNESS_LIMIT:.4f}`.",
            "",
            "| T_full (s) | H/lambda | admissibility | outside by (s) | in the envelope |",
            "|---|---|---|---|---|",
        ]
        for case in screen:
            if case.period_full_s not in declared_governing:
                role = "sensitivity only"
            elif case.period_full_s in declared_override:
                role = "**GOVERNING, admitted out of band by declaration**"
            else:
                role = "governing"
            margin = f"{case.margin_s:+.3f}" if case.margin_s else "—"
            lines.append(
                f"| {case.period_full_s:g} | {case.steepness:.4f} | "
                f"{case.verdict.value} | {margin} | {role} |"
            )
        if declared_override:
            lines += [
                "",
                f"**{sorted(declared_override)} s is admitted to the envelope although the band "
                f"excludes it**, by `load_cases.out_of_band_governing`. That is a "
                f"declaration in the configuration, not a widened band: the band edges "
                f"are unchanged for every other case and at every other height. FA0 is "
                f"the ruling behind the shipped example's entry.",
            ]

    lines += ["", "## What this run assumes, as the builder records it", ""]
    if result.built.label:
        lines.append(f"* **build label** — {result.built.label}")
    lines += [f"* {a}" for a in result.built.assumptions]

    lines += ["", "## Findings the build raised, per body", ""]
    raised = [(b.name, f) for b in result.built.bodies for f in b.findings]
    if raised:
        lines += [f"* `{name}` — {text}" for name, text in raised]
    else:
        lines.append("* none.")

    lines += ["", "## What the columns mean", ""]
    lines += [f"* {c}" for c in TABLE_CAVEATS]

    lines += [
        "",
        "## The governing utilisation",
        "",
        f"**U = {float(governing['utilisation']):.6g}** at "
        f"`{governing['member']}` {governing['station']}, "
        f"`T_full = {float(governing['period_full_s']):g} s`, basis "
        f"`{governing['basis']}`, governing clause {governing['governing_clause']}.",
        "",
        f"Checked stations: {len(result.utilisations)}. "
        f"Over unity: {sum(1 for r in result.utilisations if float(r['utilisation']) > 1.0)}.",
        "",
        "## Mass, per body",
        "",
        "Body totals, centre of gravity and inertia come FROM THE DECK. The residual below",
        "is `deck - member - remainder`, formed from its own terms (G4.1) and reported per",
        "body rather than summed, because two bodies out in opposite directions would cancel.",
        "",
        "| body | f | deck mass (kg) | member (kg) | remainder (kg) | residual (kg) |"
        " rho_eq (kg/m^3) | PSD |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for entry in result.mass:
        lines.append(
            f"| `{entry.body}` | {entry.fraction:g} | {entry.deck_mass:.6e} | "
            f"{entry.member_mass:.6e} | {entry.remainder_mass:.6e} | {entry.residual:+.3e} | "
            f"{entry.equivalent_density:.1f} | {'OK' if entry.psd_admissible else 'FAILS'} |"
        )

    lines += ["", "## Wall time", "", "| stage | seconds |", "|---|---|"]
    for stage in WALL_TIME_STAGES:
        if stage in result.timings:
            lines.append(f"| {stage} | {result.timings[stage]:.2f} |")

    if result.notes:
        lines += ["", "## Declared, and what became of it", ""]
        lines += [f"* {note}" for note in result.notes]

    lines += [
        "",
        "## Limitations this run does not escape",
        "",
        "* The section is a **stiffness stand-in** for a triangulated truss of undecided",
        "  depth (`docs/milestones/F1.md:389-390`), so these are indicative sizes.",
        "* **Linear Airy waves** and a **rigid-body** FloatSim; the superstructure only.",
        "* The grade is **assumed** (S355), not certified.",
        "* **No joint or connection checks**, no fatigue, no shell sub-models.",
        "* API RP 2A-WSD is applied as a **working-stress screen**, with no one-third",
        "  increase (EZ4 Q2, locked).",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_required_section(path: Path, report: SizingReport) -> None:
    """FT2.4's artifact: the walk, the two `max U` values, and what was chosen.

    **BOTH `max U` VALUES, SIDE BY SIDE, IS FM0's OWN REQUIREMENT AND NOT A NICETY.** The
    fixed-force value is what the proposal was made on; the re-solved value is what the
    answer rests on. The gap between them is the error in FG2's premise -- that section
    choice does not change the member forces -- measured rather than assumed, and it is
    exactly the finding the retired threshold would have hidden by either passing or
    refusing.

    **EVERY ITERATION IS LISTED, not just the accepted one.** `CLAUDE.md` forbids
    averaging a per-case diagnostic, and the same reason applies here: a loop reported as
    "converged in 3 iterations" hides which group was driving it and how far each step
    moved the answer.
    """
    cfg = report.final.config
    accepted = report.final.governing()
    study = STUDY_LABEL if cfg.study_only else ""
    lines: list[str] = [
        f"# FloatFEA {report.analysis}",
        "",
        f"**{study}{LABEL}**",
        "",
        "Sections are PROPOSED from the declared configuration's member forces and then",
        "**re-solved at** (directive FM0). The acceptance is API RP 2A-WSD's own",
        "`U <= 1.0`; the grid is the configuration's declared `sections.candidates` list,",
        "which this tool steps through and does not extend.",
        "",
        f"**{report.iteration_count} re-solve(s).**",
        "",
        f"At the sections chosen below the WHOLE model re-solves to **U = "
        f"{float(accepted['utilisation']):.6g}** at {accepted['member']} "
        f"{accepted['station']}, `T_full = {float(accepted['period_full_s']):g} s`, "
        f"clause {accepted['governing_clause']} — member group `{accepted['body']}`. The "
        f"loop does not accept a state in which any group, sized or not, is above 1.0.",
        "",
        "## What was chosen, and the two max U values",
        "",
        "| group | candidate | d_outer (m) | wall (m) | proposed from | fixed-force max U "
        "| re-solved max U |",
        "|---|---|---|---|---|---|---|",
    ]
    for g in report.groups:
        lines.append(
            f"| {g.group} | {ordinal(g.chosen_index, len(g.grid))} | "
            f"{g.chosen.d_outer:g} | "
            f"{g.chosen.wall:g} | candidate {position(g.proposed_index)} | "
            f"{g.proposed_fixed_force_u:.6g} | {g.resolved_u:.6g} |"
        )

    lines += ["", "## The premise, measured rather than assumed", ""]
    for g in report.groups:
        if g.proposed_index == g.chosen_index:
            moved = "the proposal was accepted"
        else:
            moved = (
                f"the re-solve rejected the proposal and the loop stepped "
                f"{g.chosen_index - g.proposed_index} candidate(s) up"
            )
        lines.append(
            f"* **{g.group}** — fixed-force `max U = {g.proposed_fixed_force_u:.6g}` at "
            f"candidate {position(g.proposed_index)}, re-solved `max U = {g.resolved_u:.6g}` at "
            f"candidate {position(g.chosen_index)}; {moved}."
        )

    lines += ["", "## Every re-solve", ""]
    for it in report.iterations:
        sections = ", ".join(
            f"`{name}` D={it.sections[name].d_outer:g} t={it.sections[name].wall:g} "
            f"(candidate {position(it.grid_index[name])})"
            for name in sorted(it.sections)
        )
        lines.append(f"**Re-solve {it.index}** — {sections}")
        lines.append("")
        for name in sorted(it.group_worst):
            row = it.group_worst[name]
            lines.append(
                f"* `{name}` worst station — U = {float(row['utilisation']):.6g} at "
                f"{row['member']} {row['station']}, T_full = "
                f"{float(row['period_full_s']):g} s, clause {row['governing_clause']}"
            )
        gov = it.governing
        lines.append(
            f"* whole model — U = {float(gov['utilisation']):.6g} at {gov['member']} "
            f"{gov['station']}, T_full = {float(gov['period_full_s']):g} s, clause "
            f"{gov['governing_clause']}"
        )
        lines.append("")

    lines += ["## Member groups this analysis did NOT size", ""]
    if report.unsized:
        lines.append(
            "Their **declared** sections were carried into every re-solve above, so the "
            "`max U` values are produced at a mixture of chosen and declared sections. "
            "Declare a `sections.candidates` list for a group to size it."
        )
        lines.append("")
        for name in report.unsized:
            tube = cfg.sections.groups[name]
            lines.append(
                f"* `{name}` — declared d_outer {tube.d_outer:g} m, wall {tube.wall:g} m, "
                f"no candidate grid"
            )
    else:
        lines.append("None: every member group the model builds was sized.")

    lines += [
        "",
        "## Limitations this analysis does not escape",
        "",
        "* The section is a **stiffness stand-in** for a triangulated truss of undecided",
        "  depth (`docs/milestones/F1.md:389-390`), so these are indicative sizes.",
        "* The builder **back-computes an equivalent density** per body so that `rho A`",
        "  is the deck's own line mass whatever the section is, so stepping a section up",
        "  does NOT add mass to the model. The steel a chosen section is actually made of",
        "  is FG4's question and is not asked here.",
        "* **No joint or connection checks**, no fatigue, no shell sub-models.",
        "* API RP 2A-WSD is applied as a **working-stress screen**, with no one-third",
        "  increase (EZ4 Q2, locked).",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _governing_faces(report: TrussReport) -> str:
    """Which face governs the diagonal, counted over the cells THIS report publishes.

    R1074: the bullet that used this hard-coded `60 declared cells` and `at every declared
    cell here`, which are facts about one deck and one commented-out grid. A generator
    emits for every configuration, so every figure in it is computed from the report being
    written or it is a claim about someone else's run.
    """
    counts: dict[str, int] = {}
    for group in report.trusses:
        for cell in group.cells:
            counts[cell.diagonal_face or "(none)"] = (
                counts.get(cell.diagonal_face or "(none)", 0) + 1
            )
    if not counts:
        return "none has a governing face, because no cell was resolved"
    # `is` at one, `are` otherwise (L36): a two-group configuration printed "1 are
    # governed by the horizontal face" into a published sentence.
    return ", ".join(
        f"{n} {'is' if n == 1 else 'are'} governed by the {face} face"
        for face, n in sorted(counts.items())
    )


def _margin(group: Any) -> str:
    """How far ahead the lightest cell is, and WHAT IT IS AHEAD OF.

    `lightest()` is an argmin over a grid, and the artifact publishes it where a reader
    will take it as advice, so the margin belongs beside the answer.

    **THE RUNNER-UP IS NAMED, AND IT IS USUALLY NOT ANOTHER DECLARED `(h, b)` (R1077).**
    Each `(shape, h, b)` resolves once per READING, so a grid of one declared cell still
    has two cells and the runner-up is the OTHER READING of the winner. An earlier version
    of this sentence called it "the next declared cell" unconditionally: at a one-cell grid
    it published a reading margin as though a second declared geometry had come that close,
    and a reader comparing declared cells was told the grid was tight when it holds one
    entry. Naming the runner-up makes the number self-describing at every grid shape.
    """
    ranked = sorted(group.cells, key=lambda c: c.steel_area_per_m)
    # TWO conditions, TWO messages (L16). One text for both said "the only declared cell"
    # where there were two whose lightest was zero -- a guard against division by zero
    # reported as a fact about the grid. And ZERO cells is its own case: the old `< 2`
    # test answered "the only declared cell" for an EMPTY grid, which is a third thing.
    if not ranked:
        return "not reportable: no cell resolved, so there is no lightest cell to be ahead of"
    if len(ranked) < 2:
        return "the only cell that resolved, so there is no margin to report"
    best, next_up = ranked[0], ranked[1]
    if best.steel_area_per_m <= 0.0:
        return (
            "not reportable: the lightest cell needs no steel at all, so a relative "
            "margin against it is undefined"
        )
    gap = (next_up.steel_area_per_m - best.steel_area_per_m) / best.steel_area_per_m
    same_hb = (
        next_up.shape == best.shape and next_up.depth == best.depth and next_up.width == best.width
    )
    # **THREE STATES, NOT TWO (R1082).** `same_hb` alone cannot tell the OTHER READING of a
    # cell from a DUPLICATE of it, and the two want opposite sentences: a repeated
    # declaration put `per_face_45` ahead of "the OTHER READING (`per_face_45`)" by
    # `0.00%`, naming the winner's own reading as its runner-up. The grid refuses a repeat
    # now, so this branch is unreachable from a config -- it stays because `_margin` is
    # also called directly, and a total function that cannot misdescribe its own input is
    # worth more than one that relies on its caller.
    if same_hb and next_up.geometry == best.geometry:
        what = (
            f"an IDENTICAL cell (`{next_up.shape}`, `h = {next_up.depth:g} m`, "
            f"`b = {next_up.width:g} m`, `{next_up.geometry}`), which this grid declares "
            f"more than once -- so this is not a margin over any other geometry"
        )
    elif same_hb:
        what = f"the OTHER READING (`{next_up.geometry}`) of the same `{next_up.shape}` cell"
    else:
        what = (
            f"the next cell (`{next_up.shape}`, `h = {next_up.depth:g} m`, "
            f"`b = {next_up.width:g} m`, `{next_up.geometry}`)"
        )
    return f"ahead of {what} by {gap * 100.0:.2f}%"


def _write_truss_sizing(path: Path, report: TrussReport) -> None:
    """FT2.5's artifact. The acceptance is on the TUBE; the truss is reported, not solved.

    **CONDITION 1 OF THE RULING IS THE FIRST SECTION OF THE FILE AND IT IS NOT A FOOTNOTE.**
    A reader must not be able to read `U = 0.99` as a statement about the truss. The
    utilisation was evaluated on the tube the loop re-solved; the truss beside it was never
    assembled, never solved, and is not certified by that `U`. FT2.4's artifacts label two
    configurations of the SAME representation; this labels two REPRESENTATIONS, which is a
    stronger claim to have to disclaim.
    """
    sizing = report.sizing
    cfg = sizing.final.config
    truss = cfg.sections.truss
    accepted = sizing.final.governing()
    study = STUDY_LABEL if cfg.study_only else ""
    lines: list[str] = [
        "# FloatFEA truss_sizing",
        "",
        f"**{study}{LABEL}**",
        "",
        "## READ THIS BEFORE ANY NUMBER BELOW",
        "",
        "**The `U` values in this file were evaluated on the TUBE, not on the truss.**",
        "FM0's loop proposed and re-solved over `sections.candidates`, which is a grid of",
        "tubes -- `docs/milestones/R1.md` section 4 fixes the candidate grid as the",
        "configuration's declared section list. The truss resolution in the tables further",
        "down is **derived from the accepted tube's member forces and was never",
        "re-solved**: no finite element model of chords and diagonals was assembled, and",
        "nothing here certifies the truss against API RP 2A-WSD as a structure.",
        "",
        "What the truss tables ARE: the chord and diagonal areas a parallel-chord",
        "idealisation of declared depth and width would need in order to carry the forces",
        "the accepted tube carries, sized member by member. What they are NOT: a verified",
        "frame. A truss re-solve needs the depth DECIDED and a stiffness equivalence",
        "LOCKED, and `docs/milestones/F1.md` records the depth as undecided with the tube",
        "as the stand-in for it.",
        "",
        f"**{sizing.iteration_count} re-solve(s).** At the accepted sections the whole",
        f"model re-solves to **U = {float(accepted['utilisation']):.6g}** at "
        f"{accepted['member']} {accepted['station']},",
        f"`T_full = {float(accepted['period_full_s']):g} s`, clause "
        f"{accepted['governing_clause']}, member group `{accepted['body']}`.",
        "**That is the tube's utilisation.**",
        "",
        "## The tube the loop accepted, per group",
        "",
        "| group | candidate | d_outer (m) | wall (m) | fixed-force max U | " "re-solved max U |",
        "|---|---|---|---|---|---|",
    ]
    for g in sizing.groups:
        lines.append(
            f"| {g.group} | {ordinal(g.chosen_index, len(g.grid))} | {g.chosen.d_outer:g} "
            f"| {g.chosen.wall:g} | {g.proposed_fixed_force_u:.6g} | {g.resolved_u:.6g} |"
        )
    if sizing.unsized:
        lines += [
            "",
            "Member groups with no candidate grid, carried at their **declared** sections "
            "into every re-solve above and NOT sized: "
            + ", ".join(f"`{n}`" for n in sizing.unsized)
            + ". **No truss is resolved for them either** (L5): the tables below cover"
            " only the groups with a candidate grid, so a group named here has neither a"
            " chosen tube nor a truss anywhere in this file.",
        ]

    lines += [
        "",
        "## The truss those forces imply",
        "",
        "Declared parameters, all from `sections.truss`, reported because another",
        f"configuration may declare others: `D/t = {truss.d_over_t:g}`, joint allowance",
        f"`{truss.joint_allowance:g}`, depths `{list(truss.depths)}` m, widths",
        f"`{list(truss.widths)}` m, shapes `{list(truss.shapes)}`, diameter search",
        f"`{list(truss.diameter_search)}` m.",
        "",
        "**Both readings of FI1's 45-degree panel are published** (`per_face_45` and",
        "`uniform_panel`), because which one is meant changes the answer and a reader",
        "needs to see whether the recommendation survives either. Taking the shorter",
        "buckling length from one reading and the shorter diagonal from the other is R801.",
        "",
    ]
    for group in report.trusses:
        best = group.lightest()
        lines += [
            f"### `{group.group}` -- {group.rows} governing-basis instants",
            "",
            f"Lightest declared cell: **{best.shape}**, depth {best.depth:g} m, width "
            f"{best.width:g} m, reading `{best.geometry}` -- "
            f"{best.steel_area_per_m:.4f} m2 of steel per metre of truss.",
            "",
            f"**Read that as an ARGMIN OF A DECLARED GRID AND NOT AS A RECOMMENDATION,"
            f" and check the margin before acting on it.** It is {_margin(group)}. The two"
            f" readings of FI1's 45-degree panel can finish within a fraction of a percent"
            f" of each other, and a margin that thin is not a basis for choosing a truss"
            f" form. **AND WHICH CELL WINS CAN DEPEND ON THE LOAD, NOT ONLY ON THE"
            f" GEOMETRY (R1081):** the torsion alone, moved as the single variable over a"
            f" declared grid, has been measured to flip both the winning SHAPE and the"
            f" winning READING. So the argmin above is a property of THIS run's loads and"
            f" this grid, and carries over to neither another deck nor another heading.",
            "",
            "| shape | h (m) | b (m) | reading | chord A (m2) | chord force (N) | "
            "governing station | branch | diag A (m2) | steel/m (m2) |",
            "|---|---|---|---|---|---|---|---|---|---|",
        ]
        for c in group.cells:
            lines.append(
                f"| {c.shape} | {c.depth:g} | {c.width:g} | {c.geometry} | "
                f"{c.chord_area:.5f} | {c.chord_force:.4e} | {c.chord_station} | "
                f"{c.chord_branch} | {c.diagonal_area:.5f} | {c.steel_area_per_m:.4f} |"
            )
        lines.append("")

    lines += [
        "## Limitations this analysis does not escape",
        "",
        "* **The acceptance is the tube's.** See the first section of this file.",
        "* A **pin-jointed parallel-chord idealisation** of an arm whose real form is",
        "  undecided, with no joint or connection check.",
        "* **THE TRIANGLE'S SHEAR ALLOCATION DOES NOT CLOSE (R1072).** Each of the two",
        "  inclined faces is allocated `|Vz|/2`, as though it were vertical. It is not:",
        "  for its VERTICAL component to be `|Vz|/2`, an inclined face of length",
        "  `Lf = hypot(h, b/2)` must carry `|Vz| Lf / (2h)` in plane. The torsion share",
        "  is short by the same factor -- `q h` where Bredt gives `q Lf`. **THE BOX",
        "  CLOSES EXACTLY** on every `(h, b)`, which is the control: its faces really",
        "  are vertical, so `Lf = h` and the factor is one.",
        "* **`Lf/h` IS THE FORCE FACTOR UNDER THE ALLOCATION-ALONE CORRECTION, AT BOTH",
        "  READINGS -- AND THAT QUALIFICATION IS ITSELF THE FINDING (R1076).** It is exact",
        "  there for ANY LOAD, because both terms of the shipped face shear -- `|Vz|/2` and",
        "  `q h` -- scale by `Lf/h` together, so the ratio does not depend on the `Vz`/`T`",
        "  mix. Under the TWO-EDIT correction, which also takes the inclined face's own",
        "  dimension as `Lf`, it stays exact at `per_face_45`, where the diagonal force is",
        "  `shear * sqrt(2)` and the face dimension cancels -- and it is WRONG at",
        "  `uniform_panel`, whose panel is `min(h, b)` so the dimension does not cancel:",
        "  at `h = 3, b = 8` the force factor there is `1.37437` where `Lf/h` is `1.66667`.",
        "  Six previous versions of this bullet published a bare factor with neither its",
        "  correction nor its reading named, which is what made each of them refutable.",
        "* **THE FACTOR ON THE AREA IS NOT PUBLISHED HERE, AND THE REASON IS A FINDING",
        "  RATHER THAN AN OMISSION (R1076, R1079).** Every version that published one",
        "  stated a sample as a bound, and each was refuted by the next measurement:",
        "",
        "  * it depends on WHICH of the two defects is corrected -- the allocation, the",
        "    braced length, or both -- and that is the open question below;",
        "  * it depends on the LOAD. A table measured at one `Vz` was short by up to 36%",
        "    at another;",
        "  * it depends on the READING (`per_face_45` against `uniform_panel`);",
        "  * and it depends on `(h, b)`, over which a published maximum from one deck's",
        "    grid was exceeded threefold elsewhere.",
        "",
        "  **A quantity with four free inputs has no single factor, and publishing one",
        "  states a sample as a fact.** So this artifact gives the MECHANISM and does not",
        "  quantify the consequence. `Lf/h` stands only where it is exact: the force.",
        "  What that means for a reader, plainly -- **the triangle diagonal areas in the",
        "  tables above are unconservative by an amount this tool does not bound.**",
        "* **FI1 DECLARES NOTHING HERE.** `docs/milestones/F6b.md` says shear `Vz` goes",
        "  to the VERTICAL faces, and a triangle has none. The allocation is inherited",
        "  from `scripts/measure/f6b_truss_sizing.py`, which published it in",
        "  `results/F6b/truss_sizing.md`. **That file now carries this disclosure too,",
        "  and an earlier version of this sentence said it carried none** -- true when",
        "  written and false in the same commit that made it so, which is BP0's own",
        "  shape: a statement whose subject moved underneath it.",
        "* **It is escalated, not resolved.** Making the allocation close would diverge",
        "  from that published deliverable, and FI1 declares nothing to decide it by.",
        "  **Whether the inclined face should be braced over `Lf` as well is the second",
        "  half of the same question and is escalated with it.**",
        f"* **IT REACHES EVERY TRIANGLE ROW'S PUBLISHED `steel/m`, AND THE GOVERNING"
        f" FACE CANNOT BE USED TO BOUND THAT (R1080).** An earlier version of this bullet"
        f" said the error reaches `diag A` only where the INCLINED face governs, and"
        f" conditioned the reader's whole answer on the face named in the table."
        f" **That reasoning is circular: the governing face is itself chosen by comparing"
        f" face shears that the defect understates, so the attribution printed in these"
        f" tables is computed UNDER the defect and cannot delimit it.** The two published"
        f" quantities behave differently, and the reason is structural rather than"
        f" measured, so it holds for every configuration and not just for this one."
        f" **`steel/m` SUMS the faces' diagonal steel**, so raising the inclined faces'"
        f" share by `Lf/h > 1` raises the sum WHEREVER THOSE FACES CARRY MORE THAN THE"
        f" SMALLEST DECLARED TUBE ALREADY COVERS, whichever face governs -- and below"
        f" that, the sizing returns `sections.truss.diameter_search`'s own floor for the"
        f" shipped and the corrected demand alike, so the published figure does not move"
        f" at all. **That exception is a function of a DECLARED input, not a corner:**"
        f" raising the bracket's lower end raises the shear at which the defect begins to"
        f" surface, and on a grid declared with a large minimum tube it may not surface on"
        f" any row. **`diag A` is the MAXIMUM over"
        f" faces**, so it moves only where the corrected inclined face overtakes the"
        f" bottom one -- which is exactly the comparison the defect biases. The direction"
        f" is one-way in both: the areas are monotone in the force and `Lf/h > 1`, so"
        f" **every triangle figure in these tables is LOW, never high.** Of the"
        f" {sum(len(g.cells) for g in report.trusses)} cells in the tables above,"
        f" {_governing_faces(report)} -- reported as a fact about this run, and NOT as a"
        f" bound on the error. The box rows are unaffected: `Lf = h` there.",
        "* The chord and diagonal areas are **minimum areas at the declared `D/t`**, not",
        "  sections from a catalogue.",
        "* **Linear Airy waves** and a **rigid-body** FloatSim; the superstructure only.",
        "* The grade is **assumed** (S355), not certified.",
        "* API RP 2A-WSD is applied as a **working-stress screen**, with no one-third",
        "  increase (EZ4 Q2, locked).",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _cmd_run(args: argparse.Namespace) -> int:
    cfg: RunConfig = load_config(args.config)

    # R809: REFUSED BEFORE ANYTHING IS WRITTEN, NOT AFTER. This check sat at the end of
    # the function, so `required_section: true` wrote member_forces.csv (186958 B),
    # utilisation.csv (8280 B) and report.md (3575 B), printed the governing U, and THEN
    # exited 2 -- leaving three artifacts on disk that mention the refusal nowhere. A
    # refusal that arrives after the outputs is not a refusal; it is a warning with a
    # non-zero exit code.
    # **BOTH SET IS REFUSED, and it is not fussiness.** They run the SAME loop over the
    # same `sections.candidates` grid and differ only in what they report, so running both
    # would solve the whole model twice over and write two artifacts whose tube answer is
    # identical by construction -- and a reader comparing them would be comparing a file
    # with itself.
    if cfg.outputs.required_section and cfg.outputs.truss_sizing:
        raise ConfigError(
            "outputs.required_section and outputs.truss_sizing are both set. They run the "
            "same loop over the same `sections.candidates` grid and differ only in what "
            "they report, so running both solves the model twice for one answer. Set one: "
            "`truss_sizing` reports everything `required_section` does and adds the truss "
            "resolution, so it is the one to set if you want both. Refused before any "
            "output is written."
        )

    print(f"floatfea run {cfg.source.name}")
    result = run_pipeline(cfg, progress=lambda line: print(line, flush=True))

    # **BEFORE ANY ARTIFACT IS WRITTEN, which is R809's rule and not tidiness.** The loop
    # can refuse -- an exhausted grid is a refusal under FM0 -- and a refusal that arrives
    # after three files are on disk is a warning with a non-zero exit code. R809 was
    # exactly this shape at exactly this flag: the old blanket refusal sat at the END of
    # this function, so `required_section: true` wrote member_forces.csv, utilisation.csv
    # and report.md, printed the governing U, and THEN exited 2.
    sizing: SizingReport | None = None
    trussing: TrussReport | None = None
    if cfg.outputs.required_section:
        sizing = size_required_sections(cfg, result, progress=lambda line: print(line, flush=True))
    elif cfg.outputs.truss_sizing:
        trussing = size_truss(cfg, result, progress=lambda line: print(line, flush=True))
        sizing = trussing.sizing

    out = cfg.outputs.directory
    if cfg.outputs.member_forces_csv:
        n = _write_member_forces(out / "member_forces.csv", result)
        print(f"  wrote {out / 'member_forces.csv'} ({n} rows)")
    if cfg.outputs.utilisation_csv:
        n = _write_utilisations(out / "utilisation.csv", result)
        print(f"  wrote {out / 'utilisation.csv'} ({n} rows)")
    if cfg.outputs.report:
        _write_report(out / "report.md", result)
        print(f"  wrote {out / 'report.md'}")
    if trussing is not None:
        _write_truss_sizing(out / "truss_sizing.md", trussing)
        print(
            f"  wrote {out / 'truss_sizing.md'} "
            f"({trussing.sizing.iteration_count} re-solve(s), "
            f"{sum(len(g.cells) for g in trussing.trusses)} truss cells)"
        )
    elif sizing is not None:
        _write_required_section(out / "required_section.md", sizing)
        print(f"  wrote {out / 'required_section.md'} ({sizing.iteration_count} re-solve(s))")

    governing = result.governing()
    if cfg.study_only:
        print(f"\n  {STUDY_LABEL.strip()}")
    print(
        f"\n  governing U = {float(governing['utilisation']):.6g} at "
        f"{governing['member']} {governing['station']} "
        f"(T = {float(governing['period_full_s']):g} s, {governing['governing_clause']})"
    )
    print(f"  total wall time {result.timings['total']:.2f} s")

    # **AFTER the governing line and LABELLED as a different configuration.** The line
    # above is the DECLARED sections -- the structure as the configuration describes it --
    # and these are the sections the sizing chose. Printing them before it left
    # `governing U = 1.71167` as the last word under a sizing run that had just found an
    # admissible state, which reads as the sizing's answer.
    if sizing is not None:
        sized = sizing.final.governing()
        print(f"\n  {sizing.analysis} -- a DIFFERENT configuration from the line above:")
        for g in sizing.groups:
            print(
                f"    {g.group} -> candidate {ordinal(g.chosen_index, len(g.grid))}, "
                f"D = {g.chosen.d_outer:g} m, wall = {g.chosen.wall:g} m "
                f"(fixed-force U = {g.proposed_fixed_force_u:.6g}, re-solved U = "
                f"{g.resolved_u:.6g})"
            )
        for name in sizing.unsized:
            tube = cfg.sections.groups[name]
            print(
                f"    {name} NOT SIZED (no candidate grid) -- declared D = "
                f"{tube.d_outer:g} m, wall = {tube.wall:g} m, carried into every re-solve"
            )
        print(
            f"    whole model at those sections: U = {float(sized['utilisation']):.6g} at "
            f"{sized['member']} {sized['station']} "
            f"(T = {float(sized['period_full_s']):g} s, {sized['governing_clause']})"
        )

    return 0


def _cmd_export(args: argparse.Namespace) -> int:
    """FloatSim runs -> a dynamic-inputs npz. Needs the HSP worktree.

    **NOT IMPLEMENTED IN STEP 1, AND IT SAYS SO.** FL1(b) names the command and step 1
    is specified "on existing data", so what exists here is the configuration path and an
    honest refusal. Producing a file this command cannot actually produce -- or silently
    writing an empty one -- is the failure this project is built to prevent.
    """
    cfg: RunConfig = load_config(args.config)
    if cfg.load_cases.npz is not None:
        raise ConfigError(
            f"{cfg.source.name}: load_cases already points at an existing npz "
            f"({cfg.load_cases.npz}). `export` PRODUCES that file from FloatSim runs; "
            f"declare `cases` instead, or run `floatfea run` with this configuration."
        )
    # **FL2(c): THE HEADING REFUSAL BELONGS HERE, AND ITS INPUT IS NOT HERE YET.**
    # `refuse_uncovered_headings` is the naming half and it is complete and tested. What
    # it needs is the set the BEM dataset actually carries, and that is a fact about the
    # PINNED HSP STATE: the datasets and their reader live in HSP
    # (docs/hsp-coupling.md), this repository contains neither, and the committed
    # dynamic-inputs npz records one heading in its sidecar rather than a coverage list.
    #
    # So the call site is written where the dataset is opened, which is inside the export
    # this command still cannot perform. Hard-coding a covered set here to make the call
    # reachable would be FloatFEA asserting a fact about HSP's datasets that nothing in
    # this repository can check -- and the refusal below is the honest state until the
    # worktree is wired.
    raise ConfigError(
        f"`floatfea export` is not implemented in R1 step 1. It needs the pinned HSP "
        f"worktree (docs/hsp-coupling.md), and FL1 scopes step 1 to existing data. The "
        f"{len(cfg.load_cases.cases)} declared case(s) validated cleanly, so this "
        f"configuration is ready for the export path when FL2(c) wires it; what it cannot "
        f"do is invent dynamic inputs. Point `load_cases.npz` at a committed file to run "
        f"now."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="floatfea",
        description="Structural FE for the FloatSim floating platform.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="build, solve, member forces, code check, report")
    p_run.add_argument("config", type=Path, help="path to a run configuration (YAML)")
    p_run.set_defaults(handler=_cmd_run)

    p_export = sub.add_parser("export", help="FloatSim runs -> dynamic inputs (needs HSP)")
    p_export.add_argument("config", type=Path, help="path to a run configuration (YAML)")
    p_export.set_defaults(handler=_cmd_export)

    args = parser.parse_args(argv)
    handler: Any = args.handler
    try:
        return int(handler(args))
    except ConfigError as exc:
        print(f"floatfea: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":  # pragma: no cover - module entry
    raise SystemExit(main())
