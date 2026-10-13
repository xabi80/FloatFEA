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
    "declared configuration; every assumption it rests on is listed in the run report, "
    "and the section is a stiffness stand-in for a truss of undecided depth."
)


def _write_member_forces(path: Path, result: RunResult) -> int:
    """F4's table, from this run. One row per (member, station, case, basis)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        fh.write("# " + LABEL.replace(",", ";") + "\n")
        for key, value in result.config.provenance().items():
            fh.write(f"# {key}: {str(value).replace(',', ';')}\n")
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
        fh.write("# " + LABEL.replace(",", ";") + "\n")
        for key, value in result.config.provenance().items():
            fh.write(f"# {key}: {str(value).replace(',', ';')}\n")
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
    lines: list[str] = [
        "# FloatFEA run report",
        "",
        f"**{LABEL}**",
        "",
        "## What was configured",
        "",
    ]
    for key, value in cfg.provenance().items():
        lines.append(f"* **{key}** — {value}")

    lines += [
        "",
        "## The governing utilisation",
        "",
        f"**U = {float(governing['utilisation']):.6g}** at "
        f"`{governing['body']}:{governing['member']}` {governing['station']}, "
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
    print(
        f"\n  governing U = {float(governing['utilisation']):.6g} at "
        f"{governing['member']} {governing['station']} "
        f"(T = {float(governing['period_full_s']):g} s, {governing['governing_clause']})"
    )
    print(f"  total wall time {result.timings['total']:.2f} s")

    if cfg.outputs.required_section or cfg.outputs.truss_sizing:
        raise ConfigError(
            "outputs.required_section / outputs.truss_sizing are FL2(b) and are not wired "
            "in R1 step 1. Under FM0 they must propose from fixed forces and then RE-SOLVE "
            "at the selected sections, reporting the iteration count and both max U values; "
            "running them off a single fixed force set is what FM0 ruled out. Refused "
            "rather than silently skipped."
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
