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
from typing import Any

from floatfea.post.forces_table import _stresses
from floatfea.post.member_forces import COMPONENTS
from floatfea.run.config import ConfigError, RunConfig, load_config
from floatfea.run.pipeline import RunResult
from floatfea.run.pipeline import run as run_pipeline

__all__ = ["main"]

LABEL = (
    "INDICATIVE SIZING SCREEN -- NOT A CODE CASE. Produced by `floatfea run` from a "
    "declared configuration. The section is a stiffness stand-in for a truss of "
    "undecided depth (docs/milestones/F1.md:389-390)."
)

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
    for stage in ("build", "load", "solve", "code_check", "total"):
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


def _cmd_run(args: argparse.Namespace) -> int:
    cfg: RunConfig = load_config(args.config)

    # R809: REFUSED BEFORE ANYTHING IS WRITTEN, NOT AFTER. This check sat at the end of
    # the function, so `required_section: true` wrote member_forces.csv (186958 B),
    # utilisation.csv (8280 B) and report.md (3575 B), printed the governing U, and THEN
    # exited 2 -- leaving three artifacts on disk that mention the refusal nowhere. A
    # refusal that arrives after the outputs is not a refusal; it is a warning with a
    # non-zero exit code.
    if cfg.outputs.required_section or cfg.outputs.truss_sizing:
        raise ConfigError(
            "outputs.required_section / outputs.truss_sizing are FL2(b) and are not wired "
            "in R1 step 1. Under FM0 they must propose from fixed forces and then "
            "RE-SOLVE at the selected sections, reporting the iteration count and both "
            "max U values; running them off a single fixed force set is what FM0 ruled "
            "out. Refused before any output is written, so nothing on disk describes a "
            "run that did not happen."
        )

    print(f"floatfea run {cfg.source.name}")
    result = run_pipeline(cfg, progress=lambda line: print(line, flush=True))

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

    governing = result.governing()
    if cfg.study_only:
        print(f"\n  {STUDY_LABEL.strip()}")
    print(
        f"\n  governing U = {float(governing['utilisation']):.6g} at "
        f"{governing['member']} {governing['station']} "
        f"(T = {float(governing['period_full_s']):g} s, {governing['governing_clause']})"
    )
    print(f"  total wall time {result.timings['total']:.2f} s")

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
