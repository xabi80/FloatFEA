#!/usr/bin/env python
"""FG3/FG4: the section each arm group needs to pass, and whether its mass is consistent.

    python scripts/measure/f6a_required_section.py

WHAT IT DOES. For each of the two sizing groups FG2 establishes -- all four platform arms
together, all twelve hub arms together -- it searches for the tube that brings
`max U <= 1.0` over F4's governing envelope, three ways (FG3 (i), (ii), (iii)), and then
asks FG4's question: does the steel that section is made of weigh more than the mass the
model assumed for it?

WHY THE SEARCH READS STORED FORCES AND DOES NOT REBUILD. FG2's premise is that section
choice does not change the member forces. `docs/F4_member_forces.csv` therefore holds the
forces for every candidate as well as for the shipped one, and the search is a re-evaluation
of the clauses at each candidate section -- thousands of candidates, no solve. **The premise
is not assumed on that account: `f6a_premise_check.py` rebuilds the model at each answer and
compares the forces.** The search is fast because the premise holds; the premise is checked
separately because the search depends on it.

WHAT IS HELD FIXED, all of it F6's: `F_y = 355 MPa`, `K = 2.0`, `C_m = 0.85`, no one-third
increase, and the governing basis is EZ2/FA0's four in-band periods on the per-instant rows.

A CANDIDATE OUTSIDE THE CLAUSE RANGES IS REFUSED AND RECORDED, NOT EXTRAPOLATED. The module
raises; this catches the refusal, counts it, and excludes the candidate -- so a search that
found nothing because every candidate was refused cannot look like a search that found
nothing because nothing passed.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from floatfea.basis import E_STEEL, FY_S355, RHO_STEEL  # noqa: E402
from floatfea.checks.api_wsd import (  # noqa: E402
    CM_JOINT_TRANSLATION,
    check_member,
)
from floatfea.model.platform import build_superstructure  # noqa: E402

GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
K_LOCKED = 2.0
GRAVITY = 9.80665

# The two sizing groups FG2 establishes. `prefix` is how `docs/F4_member_forces.csv`
# spells the member: platform arms are `platform:<hub>_arm`, hub arms `hub<n>:<buoy>_arm`.
GROUPS = (("platform", "platform:"), ("hubs", "hub"))


@dataclass(frozen=True)
class Candidate:
    """A tube, and the section properties the clauses need from it."""

    d_outer: float
    wall: float

    @property
    def area(self) -> float:
        inner = self.d_outer - 2.0 * self.wall
        return math.pi * 0.25 * (self.d_outer**2 - inner**2)

    @property
    def i_second(self) -> float:
        inner = self.d_outer - 2.0 * self.wall
        return math.pi / 64.0 * (self.d_outer**4 - inner**4)

    @property
    def section_modulus(self) -> float:
        return 2.0 * self.i_second / self.d_outer

    @property
    def torsional_modulus(self) -> float:
        return 4.0 * self.i_second / self.d_outer  # J = 2 I for a thin tube

    @property
    def radius_of_gyration(self) -> float:
        return math.sqrt(self.i_second / self.area)

    @property
    def d_over_t(self) -> float:
        return self.d_outer / self.wall


def _rows(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln[:1] != "#"]
    return list(csv.DictReader(lines))


def _governing(rows: list[dict[str, str]], prefix: str) -> list[dict[str, str]]:
    """The group's per-instant rows on the governing basis, every station."""
    return [
        r
        for r in rows
        if r["basis"] == "total_instant"
        and r["member"].startswith(prefix)
        and float(r["period_full_s"] or "nan") in GOVERNING_PERIODS
    ]


def _lengths() -> dict[str, float]:
    built = build_superstructure()
    return {m.label: float(m.length) for b in built.bodies for m in b.members}


@dataclass
class Outcome:
    """The worst station a candidate produces, or why the candidate was refused."""

    max_u: float
    worst: dict[str, str] | None
    refused: int
    checked: int
    u_k1: float
    u_cm1: float


def evaluate(cand: Candidate, rows: list[dict[str, str]], lengths: dict[str, float]) -> Outcome:
    """`max U` over every row, with the two sensitivities at the same station."""
    worst: dict[str, str] | None = None
    max_u = -1.0
    at_k1 = at_cm1 = 0.0
    refused = checked = 0
    for r in rows:
        kl_r = K_LOCKED * lengths[r["member"]] / cand.radius_of_gyration
        kw = dict(
            axial_n=float(r["N"]),
            shear_y_n=float(r["Vy"]),
            shear_z_n=float(r["Vz"]),
            torsion_nm=float(r["T"]),
            moment_y_nm=float(r["My"]),
            moment_z_nm=float(r["Mz"]),
            area_m2=cand.area,
            section_modulus_m3=cand.section_modulus,
            torsional_modulus_m3=cand.torsional_modulus,
            d_outer_m=cand.d_outer,
            wall_m=cand.wall,
            fy=FY_S355,
            e=E_STEEL,
        )
        try:
            got = check_member(k_l_over_r=kl_r, cm=CM_JOINT_TRANSLATION, **kw)
            k1 = check_member(
                k_l_over_r=1.0 * lengths[r["member"]] / cand.radius_of_gyration,
                cm=CM_JOINT_TRANSLATION,
                **kw,
            )
            cm1 = check_member(k_l_over_r=kl_r, cm=1.0, **kw)
        except ValueError:
            refused += 1
            continue
        checked += 1
        if got.utilisation > max_u:
            max_u = got.utilisation
            at_k1, at_cm1 = k1.utilisation, cm1.utilisation
            worst = {
                "body": r["body"],
                "member": r["member"],
                "station": r["station"],
                "period_full_s": r["period_full_s"],
                "clause": got.governing,
                "axial_branch": got.axial_branch,
                "interaction_form": got.interaction_form,
            }
    return Outcome(max_u, worst, refused, checked, at_k1, at_cm1)


def _passes(cand: Candidate, rows, lengths) -> tuple[bool, Outcome]:
    out = evaluate(cand, rows, lengths)
    return (out.checked > 0 and out.refused == 0 and out.max_u <= 1.0), out


def _frange(lo: float, hi: float, step: float) -> list[float]:
    n = int(round((hi - lo) / step)) + 1
    return [round(lo + i * step, 10) for i in range(n)]


T_STEPS = _frange(0.005, 0.600, 0.005)
D_STEPS = _frange(2.0, 6.0, 0.1)


def search_min_wall(d_outer: float, rows, lengths) -> tuple[Candidate | None, Outcome | None]:
    """FG3 (i): `D` fixed, the smallest `t` in 5 mm steps that passes."""
    for t in T_STEPS:
        if t >= 0.5 * d_outer:
            break
        cand = Candidate(d_outer, t)
        ok, out = _passes(cand, rows, lengths)
        if ok:
            return cand, out
    return None, None


def search_min_diameter(wall: float, rows, lengths) -> tuple[Candidate | None, Outcome | None]:
    """FG3 (ii): `t` fixed, the smallest `D` in 0.1 m steps that passes."""
    for d in D_STEPS:
        if wall >= 0.5 * d:
            continue
        cand = Candidate(d, wall)
        ok, out = _passes(cand, rows, lengths)
        if ok:
            return cand, out
    return None, None


def search_min_area(rows, lengths) -> tuple[Candidate | None, Outcome | None, int]:
    """FG3 (iii): the least-area tube over the whole grid that passes."""
    best: tuple[Candidate, Outcome] | None = None
    tried = 0
    for d in D_STEPS:
        for t in T_STEPS:
            if t >= 0.5 * d:
                break
            cand = Candidate(d, t)
            if best is not None and cand.area >= best[0].area:
                continue
            tried += 1
            ok, out = _passes(cand, rows, lengths)
            if ok:
                best = (cand, out)
    if best is None:
        return None, None, tried
    return best[0], best[1], tried


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--forces", type=Path, default=ROOT / "docs" / "F4_member_forces.csv")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "F6a" / "required_section.csv")
    ap.add_argument(
        "--json",
        type=Path,
        default=ROOT / "results" / "F6a" / "required_section.json",
        help="the same answers, for the report generator to read",
    )
    args = ap.parse_args(argv)

    rows_all = _rows(args.forces)
    lengths = _lengths()
    built = build_superstructure()
    mu = {
        "platform": float(built.bodies[0].member_mass) / float(built.bodies[0].total_member_length),
        "hubs": float(built.bodies[1].member_mass) / float(built.bodies[1].total_member_length),
    }

    answers: list[dict[str, object]] = []
    for group, prefix in GROUPS:
        rows = _governing(rows_all, prefix)
        print(f"=== {group}: {len(rows)} governing per-instant rows ===", flush=True)

        searches = [
            ("i_min_wall_at_D_2.5", *search_min_wall(2.5, rows, lengths), None),
            ("ii_min_diameter_at_t_180mm", *search_min_diameter(0.180, rows, lengths), None),
        ]
        cand, out, tried = search_min_area(rows, lengths)
        searches.append(("iii_min_area", cand, out, tried))

        for label, cand, out, tried in searches:
            if cand is None or out is None:
                print(f"  {label:28s} NO CANDIDATE PASSES in the declared grid")
                answers.append({"group": group, "search": label, "found": False})
                continue
            line_mass = RHO_STEEL * cand.area
            # FG4: what self-weight the required section IMPLIES, as the closed form for a
            # cantilever under its own uniform weight -- `M = mu g L^2 / 2` -- at the
            # longest member of the group. **NOT A MODEL RE-RUN, and the difference
            # matters:** the model holds the deck's `mu` fixed and back-computes the
            # density, so it cannot be asked this question directly; and this form carries
            # the ARM's own weight only, not the body's remainder mass, which the model
            # places at its own node. So it is a lower bound on the implied root moment and
            # is reported as the arm-weight term, not as the station's moment.
            span = max(lengths[r["member"]] for r in rows)
            implied = line_mass * GRAVITY * span * span / 2.0
            assumed = mu[group] * GRAVITY * span * span / 2.0
            # And against the WHOLE published static root moment of the group -- which
            # includes the remainder mass, so this ratio says how the arm's own weight at
            # the required section compares with everything the static case currently
            # carries. Above 1.0 it means the arm alone would outweigh the present total.
            published = max(
                abs(float(r["My"]))
                for r in rows_all
                if r["basis"] == "static"
                and r["station"] == "ROOT"
                and r["member"].startswith(prefix)
            )
            answers.append(
                {
                    "group": group,
                    "search": label,
                    "found": True,
                    "D_m": cand.d_outer,
                    "t_m": cand.wall,
                    "D_over_t": cand.d_over_t,
                    "A_m2": cand.area,
                    "W_m3": cand.section_modulus,
                    "r_m": cand.radius_of_gyration,
                    "max_U": out.max_u,
                    "U_K1": out.u_k1,
                    "U_Cm1": out.u_cm1,
                    "checked": out.checked,
                    "refused": out.refused,
                    "grid_tried": tried,
                    "steel_line_mass_kg_per_m": line_mass,
                    "assumed_mu_kg_per_m": mu[group],
                    "mass_ratio": line_mass / mu[group],
                    "span_m": span,
                    "implied_root_moment_nm": implied,
                    "assumed_root_moment_nm": assumed,
                    "implied_root_moment_ratio": implied / assumed,
                    "published_static_root_moment_nm": published,
                    "implied_over_published_static_root": implied / published,
                    **{f"worst_{k}": v for k, v in (out.worst or {}).items()},
                }
            )
            print(
                f"  {label:28s} D={cand.d_outer:.1f} t={cand.wall*1000:.0f}mm "
                f"D/t={cand.d_over_t:6.2f} A={cand.area:.4f} maxU={out.max_u:.4f} "
                f"rho*A/mu={line_mass / mu[group]:6.3f}"
            )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    cols = sorted({k for a in answers for k in a})
    with args.out.open("w", encoding="utf-8", newline="") as fh:
        fh.write("# F6a required section (FG3) -- INDICATIVE: stand-in tube for a truss,\n")
        fh.write("# placeholder masses, heading 0 deg, F_y assumed. Generated by\n")
        fh.write("# scripts/measure/f6a_required_section.py\n")
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for a in answers:
            w.writerow(a)
    args.json.write_text(json.dumps(answers, indent=2), encoding="utf-8")
    print(f"\n  wrote {args.out.relative_to(ROOT).as_posix()} ({len(answers)} rows)")
    print(f"  wrote {args.json.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
