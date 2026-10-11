#!/usr/bin/env python
"""FI0-FI4: resolve F4's beam forces into truss chord and diagonal forces, and size them.

    python scripts/measure/f6b_truss_sizing.py

POST-PROCESSING ONLY (FI0). No FloatSim, no re-solve, no change to the frame model. The
input is `docs/F4_member_forces.csv` on the governing basis, and the legitimacy of reading
one set of forces for every candidate section is FG2's premise, verified in F6a: section
choice moves the static forces by `1.7e-15` relative and `max U` by `3.5e-06`.

**EVERY NUMBER HERE IS INDICATIVE.** A pin-jointed parallel-chord idealisation of an arm
whose real form is undecided, with no joint or connection check, placeholder masses, one
heading and an assumed grade. The deliverable's label carries that and so does this.

THE ONE DECISION THE DIRECTIVE LEFT OPEN, AND IT IS NOT A SMALL ONE. FI3 asks for one
section per arm group, and `Mz` is `2.689e+08` on two platform arms and `3e-01` on the other
two -- the split is the arm's ORIENTATION at heading 0°, not the physics. So the group's
requirement is the ENVELOPE over its members: `b` may not be made small because `Mz` is
small on the arm one happens to read. Sizing each arm for its own orientation would deliver
four different platform arms at one heading and is void the moment increment 3 moves the
heading. `docs/milestones/F6b.md` § 2b records this as the plan's one real decision.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
import sys  # noqa: E402

sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402

from floatfea.basis import E_STEEL, FY_S355  # noqa: E402
from floatfea.checks.api_wsd import (  # noqa: E402
    allowable_axial_compression,
    allowable_axial_tension,
)
from floatfea.model.material import Section  # noqa: E402
from floatfea.model.platform import build_superstructure  # noqa: E402

# ----------------------------------------------------------------- FI's declared inputs
RHO_STEEL = 7850.0
D_OVER_T = 24.0
JOINT_ALLOWANCE = 1.15
DIAGONAL_ANGLE_DEG = 45.0
GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
H_GRID = (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
B_GRID = (2.0, 3.0, 4.0, 5.0, 6.0, 8.0)
GROUPS = (("platform", "platform:", 50.0, 9375.0), ("hubs", "hub", 25.0, 15000.0))
STANDIN_I = 0.888  # the F6/F6a stand-in tube's second moment, for FI4(ii)

COMPONENTS = ("N", "Vy", "Vz", "T", "My", "Mz")


# ------------------------------------------------------------------------- the forces
def _rows(path: Path) -> list[dict[str, str]]:
    body = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(body))


def governing(rows: list[dict[str, str]], prefix: str) -> list[dict[str, str]]:
    """The group's per-instant rows on the governing basis, every station (EZ2/FA0).

    The same selection `scripts/measure/f6a_required_section.py::_governing` makes, so the
    two increments read one basis and a disagreement between them would be a disagreement
    about this function rather than about the data.
    """
    return [
        r
        for r in rows
        if r["basis"] == "total_instant"
        and r["member"].startswith(prefix)
        and float(r["period_full_s"] or "nan") in GOVERNING_PERIODS
    ]


# ------------------------------------------------------- FI1: the two cross-sections
@dataclass(frozen=True)
class ChordForces:
    """The chord axial forces and the face shears a single beam-force set produces."""

    chords: dict[str, float]
    face_shear: dict[str, float]


def box_resolution(
    n: float, vy: float, vz: float, t: float, my: float, mz: float, h: float, b: float
) -> ChordForces:
    """FI1(a). Four chords at `(±b/2, ±h/2)`; `N/4 ± My/(2h) ± Mz/(2b)`.

    Derivation of the two bending terms, so the formula is checkable rather than quoted:
    with four equal chords, `My = Σ F_i z_i = 2f(h/2) + 2f(h/2) = 2fh`, hence `f = My/(2h)`,
    and `Mz = 2g(b/2)·2 = 2gb`, hence `g = Mz/(2b)`. Signs are preserved (FI1), so each
    chord gets its own combination rather than a worst-case magnitude.
    """
    axial = n / 4.0
    f_my = my / (2.0 * h)
    f_mz = mz / (2.0 * b)
    chords = {
        "top_+b": axial + f_my + f_mz,
        "top_-b": axial + f_my - f_mz,
        "bot_+b": axial - f_my + f_mz,
        "bot_-b": axial - f_my - f_mz,
    }
    # Shear: `Vz` to the two vertical faces, `Vy` to the two horizontal faces, plus the
    # torsion shear flow `q = T/(2 A_enc)` around the perimeter (FI1). A vertical face of
    # depth `h` carries `q h`; a horizontal face of width `b` carries `q b`. The two signs
    # are combined to the larger magnitude, because the shear flow adds on one face of each
    # pair and subtracts on the other.
    q = t / (2.0 * b * h)
    face = {
        "vertical": abs(vz) / 2.0 + abs(q * h),
        "horizontal": abs(vy) / 2.0 + abs(q * b),
    }
    return ChordForces(chords, face)


def triangle_resolution(
    n: float, vy: float, vz: float, t: float, my: float, mz: float, h: float, b: float
) -> ChordForces:
    """FI1(b). Three chords: two bottom at `(±b/2, 0)`, one top at `(0, h)`, apex UP.

    The section properties the directive asks to be stated, for three equal areas `A_c`
    with centroid at `z̄ = h/3`:

        I_yy = A_c[2(h/3)^2 + (2h/3)^2] = (2/3) A_c h^2
        I_zz = A_c · 2 (b/2)^2          = A_c b^2 / 2

    and `F_i = A_c M z_i / I` gives

        top         N/3 + My/h          and NO Mz term at all (it is on the centreline)
        bottom ±    N/3 - My/(2h)  ±Mz/b

    Both checks are exact: `ΣF = My/h - 2·My/(2h) = 0`, and
    `ΣM = (My/h)(2h/3) + 2(My/(2h))(h/3) = My`.

    **THE ASYMMETRY IS A RESULT, NOT A DETAIL.** The apex carries twice either bottom
    chord's `My` force, and it carries no `Mz`, so horizontal bending is resisted by the
    bottom pair alone on lever `b` where the box has two pairs. Apex-up is declared; both
    moment signs are evaluated per instant, so hogging and sagging are both found.
    """
    axial = n / 3.0
    chords = {
        "apex": axial + my / h,
        "bot_+b": axial - my / (2.0 * h) + mz / b,
        "bot_-b": axial - my / (2.0 * h) - mz / b,
    }
    # A_enclosed is the triangle's own area.
    q = t / (2.0 * 0.5 * b * h)
    # Two inclined faces carry `Vz`; the single bottom face carries `Vy`. The inclined face
    # height is `h` (the vertical projection the chord separation provides).
    face = {
        "vertical": abs(vz) / 2.0 + abs(q * h),
        "horizontal": abs(vy) + abs(q * b),
    }
    return ChordForces(chords, face)


def enclosed_area(section: str, h: float, b: float) -> float:
    """`A_enclosed` for FI1's shear flow: `b h` for the box, `b h / 2` for the triangle."""
    return b * h if section == "box" else 0.5 * b * h


RESOLVERS = {"box": box_resolution, "triangle": triangle_resolution}
N_CHORDS = {"box": 4, "triangle": 3}
N_DIAGONAL_FACES = {"box": 4, "triangle": 3}


# ------------------------------------------------------------------------- FI2: sizing
def _tube(d_outer: float) -> Section:
    return Section.circular_tube(d_outer, d_outer / D_OVER_T)


def _radius_of_gyration(sec: Section) -> float:
    """`r = sqrt(I/A)`. `Section` carries `A`, `I_y`, `I_z`, `J` and no `r` (C99)."""
    return math.sqrt(float(sec.I_y) / float(sec.A))


def area_for_tension(force: float) -> float:
    """§ 3.2.1: `A = F / (0.6 Fy)`. Zero for a compressive or zero force."""
    if force <= 0.0:
        return 0.0
    return force / allowable_axial_tension(FY_S355)


def area_for_compression(force: float, panel_length: float) -> tuple[float, str]:
    """§ 3.2.2 at `K = 1.0`, `L` = the panel length, solved for the minimum area.

    `F_a` depends on `KL/r` and therefore on the section, so this is an implicit problem
    and is solved by bisection on `D` at the declared `D/t`: the demand `|F|/A(D)` falls
    as `D` grows and `F_a(D)` rises, so `|F|/A - F_a` is monotone decreasing and has one
    root. The bracket is refused rather than extrapolated if the upper bound does not pass.
    """
    if force >= 0.0:
        return 0.0, "tension"
    demand = abs(force)
    lo, hi = 0.02, 6.0

    def slack(d: float) -> float:
        sec = _tube(d)
        f_a, _ = allowable_axial_compression(
            panel_length / _radius_of_gyration(sec), d, d / D_OVER_T, FY_S355, E_STEEL
        )
        return f_a - demand / float(sec.A)

    if slack(hi) < 0.0:
        raise ValueError(
            f"no tube up to D = {hi} m at D/t = {D_OVER_T} carries {demand:.4e} N in "
            f"compression over a {panel_length:.3f} m panel. Refused, not extrapolated."
        )
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if slack(mid) >= 0.0:
            hi = mid
        else:
            lo = mid
    sec = _tube(hi)
    _, branch = allowable_axial_compression(
        panel_length / _radius_of_gyration(sec), hi, hi / D_OVER_T, FY_S355, E_STEEL
    )
    return float(sec.A), branch


@dataclass
class Sized:
    """One `(section, group, h, b, geometry)` answer."""

    chord_area: float
    chord_force: float
    chord_governing: str
    chord_branch: str
    chord_buckling_length: float
    diagonal_area_max: float
    diagonal_force_max: float
    diagonal_governing: str
    diagonal_steel_per_m: float
    line_mass: float
    mass_ratio: float
    torsion_share_of_face_shear: float
    torsion_share_max: float


# FACE GEOMETRY -- THE THING R801 WAS ABOUT, AND IT IS NOW STATED ONCE.
#
# A box of depth `h` and width `b` has TWO face dimensions, and FI1's "diagonals at 45°
# (panel length = the face dimension)" therefore has two consistent readings. The first
# version of this script took the SHORTER buckling length from one of them and the SHORTER
# diagonal from the other -- the favourable half of each -- via a single
# `panel_length=min(h, b)` while its own comment said "the face dimension". At the headline
# answer's 8:3 aspect ratio that mattered, and it mattered most exactly where the sweep's
# answer sat.
#
# Both readings are computed and BOTH are published, because which one FI means changes the
# answer and a reader needs to see that the recommendation survives either:
#
#   "per_face_45"  -- 45° on every face, so the panel length is that face's own dimension.
#                     The diagonals are all at 45° and each face's panel differs. A chord
#                     is braced every `h` by the vertical faces and every `b` by the
#                     horizontal ones, at non-coincident stations; the tube is circular so
#                     `r_y = r_z`, and the governing buckling length is `max(h, b)`.
#   "uniform_panel"-- one panel length `min(h, b)` for the whole truss, so the chord's
#                     buckling length is `min(h, b)` -- but then the larger faces' diagonals
#                     are NOT at 45°: across a face of transverse dimension `d` over a panel
#                     `p` they sit at `atan(d/p)` and are `hypot(p, d)` long, so they cost
#                     `hypot(p, d)/p` of their area per unit length of truss.
#
# What may not stand is `min` for the chord and 45° for the diagonals at the same time.
GEOMETRIES = ("per_face_45", "uniform_panel")


@dataclass(frozen=True)
class Face:
    """One braced face: how many there are, its transverse dimension, its shear key."""

    count: int
    dimension: float
    shear_key: str


def faces(section: str, h: float, b: float) -> tuple[Face, ...]:
    """The braced faces and their transverse dimensions.

    The box has two vertical faces of depth `h` taking `Vz`, and two horizontal faces of
    width `b` taking `Vy`. The triangle has two inclined faces taking `Vz` and one bottom
    face of width `b` taking `Vy`, which is why `triangle_resolution` divides `Vy` by one
    rather than by two.
    """
    if section == "box":
        return (Face(2, h, "vertical"), Face(2, b, "horizontal"))
    return (Face(2, h, "vertical"), Face(1, b, "horizontal"))


def panel_and_diagonal(geometry: str, h: float, b: float, face: Face) -> tuple[float, float, float]:
    """`(chord buckling length, diagonal length, diagonal steel per unit truss length)`.

    The third is the one that decides mass: a diagonal of length `L_d` repeated every `p`
    along the truss contributes `A_d · L_d / p` of area per unit length.
    """
    if geometry == "per_face_45":
        panel = face.dimension
        diagonal = panel * math.sqrt(2.0)
        return max(h, b), diagonal, diagonal / panel
    panel = min(h, b)
    diagonal = math.hypot(panel, face.dimension)
    return panel, diagonal, diagonal / panel


def size(
    section: str,
    rows: list[dict[str, str]],
    h: float,
    b: float,
    mu: float,
    geometry: str,
) -> Sized:
    """FI2 + FI3 for one cross-section, one `(h, b)` and one reading of the geometry.

    The chord area is the worst over every chord, every station and every instant, in BOTH
    senses: the largest tension demand and the largest compression demand are sized
    separately and the larger area wins, because the compression branch is not a scaling of
    the tension one.

    **EACH FACE'S DIAGONALS ARE SIZED FOR THAT FACE'S OWN SHEAR** (R801). The first version
    sized one diagonal from the worst face shear anywhere and applied it to every face,
    which is conservative on mass but hides which face governs -- and FI2 asks for each
    member's governing case and station.
    """
    resolve = RESOLVERS[section]
    worst_t = (0.0, "")
    worst_c = (0.0, "")
    worst_face: dict[str, tuple[float, str]] = {}
    # The torsion term's share of the face shear, formed from its own terms. The second
    # resolution with `T = 0` that used to stand here, and the subtraction that used it,
    # are gone: they computed this by cancelling two numbers that agree to 16 figures and
    # returned exactly zero. G4.1's rule -- a small quantity comes from its own terms.
    torsion_share = 0.0
    torsion_share_max = 0.0
    governing_shear = (0.0, "")

    for r in rows:
        vals = {c: float(r[c]) for c in COMPONENTS}
        res = resolve(vals["N"], vals["Vy"], vals["Vz"], vals["T"], vals["My"], vals["Mz"], h, b)
        where = f"{r['member']} {r['station']} T={r['period_full_s']}s"
        for name, force in res.chords.items():
            if force > worst_t[0]:
                worst_t = (force, f"{where} chord {name}")
            if -force > worst_c[0]:
                worst_c = (-force, f"{where} chord {name}")
        q = abs(vals["T"]) / (2.0 * enclosed_area(section, h, b))
        term = {"vertical": q * h, "horizontal": q * b}
        for name, shear in res.face_shear.items():
            share = term[name] / shear if shear > 0.0 else 0.0
            torsion_share_max = max(torsion_share_max, share)
            if shear > worst_face.get(name, (0.0, ""))[0]:
                worst_face[name] = (shear, f"{where} face {name}")
            if shear > governing_shear[0]:
                governing_shear = (shear, f"{where} face {name}")
                torsion_share = share

    # --- the chord ------------------------------------------------------------------
    chord_L = panel_and_diagonal(geometry, h, b, faces(section, h, b)[0])[0]
    a_t = area_for_tension(worst_t[0])
    a_c, branch_c = area_for_compression(-worst_c[0], panel_length=chord_L)
    if a_t >= a_c:
        chord_area, chord_force, chord_where, chord_branch = a_t, worst_t[0], worst_t[1], "tension"
    else:
        chord_area, chord_force, chord_where, chord_branch = (
            a_c,
            -worst_c[0],
            worst_c[1],
            branch_c,
        )

    # --- the diagonals, per face ------------------------------------------------------
    diagonal_steel = 0.0
    worst_diag = (0.0, 0.0, "")
    for face in faces(section, h, b):
        shear, where = worst_face.get(face.shear_key, (0.0, "(no shear)"))
        _, diag_len, steel_per_m = panel_and_diagonal(geometry, h, b, face)
        # sin(theta) = dimension / diagonal length, for a diagonal spanning the panel.
        sin_theta = face.dimension / diag_len
        force = shear / sin_theta
        a_dt = area_for_tension(force)
        a_dc, _ = area_for_compression(-force, panel_length=diag_len)
        a_d = max(a_dt, a_dc)
        diagonal_steel += face.count * a_d * steel_per_m
        if a_d > worst_diag[0]:
            worst_diag = (a_d, force, where)

    chord_steel = N_CHORDS[section] * chord_area
    line_mass = (chord_steel + diagonal_steel) * RHO_STEEL * JOINT_ALLOWANCE
    return Sized(
        chord_area=chord_area,
        chord_force=chord_force,
        chord_governing=chord_where,
        chord_branch=chord_branch,
        chord_buckling_length=chord_L,
        diagonal_area_max=worst_diag[0],
        diagonal_force_max=worst_diag[1],
        diagonal_governing=worst_diag[2],
        diagonal_steel_per_m=diagonal_steel,
        line_mass=line_mass,
        mass_ratio=line_mass / mu,
        torsion_share_of_face_shear=torsion_share,
        torsion_share_max=torsion_share_max,
    )


# ------------------------------------------------------------------------------ FI4
def my_mz_split(rows_all: list[dict[str, str]], prefix: str) -> dict[str, object]:
    """FI4(i). The `My`/`Mz` split, static and dynamic, and where it comes from."""
    gov = governing(rows_all, prefix)
    static = [r for r in rows_all if r["basis"] == "static" and r["member"].startswith(prefix)]
    per_member: dict[str, dict[str, float]] = {}
    for r in gov:
        d = per_member.setdefault(r["member"], {"My": 0.0, "Mz": 0.0})
        d["My"] = max(d["My"], abs(float(r["My"])))
        d["Mz"] = max(d["Mz"], abs(float(r["Mz"])))
    worst = max(gov, key=lambda r: math.hypot(float(r["My"]), float(r["Mz"])))
    return {
        "governing_station": f"{worst['member']} {worst['station']}",
        "governing_period_s": worst["period_full_s"],
        "governing_My": float(worst["My"]),
        "governing_Mz": float(worst["Mz"]),
        "governing_resultant": math.hypot(float(worst["My"]), float(worst["Mz"])),
        "governing_Mz_fraction_of_resultant": abs(float(worst["Mz"]))
        / math.hypot(float(worst["My"]), float(worst["Mz"])),
        "static_max_My": max(abs(float(r["My"])) for r in static),
        "static_max_Mz": max(abs(float(r["Mz"])) for r in static),
        "dynamic_envelope_max_My": max(abs(float(r["My"])) for r in gov),
        "dynamic_envelope_max_Mz": max(abs(float(r["Mz"])) for r in gov),
        "max_T": max(abs(float(r["T"])) for r in gov),
        "per_member": per_member,
    }


def hand_table_check() -> list[dict[str, float]]:
    """FI4(iii). The two-chord hand table, reproduced and then corrected for what it omits.

    The hand form is two chords at separation `h`: `M = 2 F (h/2) = F h`, so `F = M/h` and
    `A_c = M/(sigma h)` at `sigma = 213 MPa` -- which is `0.6 F_y` for `F_y = 355 MPa`, i.e.
    the TENSION allowable. The table is therefore a tension-only, bending-only, two-chord
    figure, and this reports what each omission costs.
    """
    sigma = 213.0e6
    moment = 324.0e6
    out = []
    for h in (3.0, 4.0, 5.0, 6.0):
        force = moment / h
        a_tension = force / sigma
        a_comp, branch = area_for_compression(-force, panel_length=h)
        out.append(
            {
                "h_m": h,
                "chord_force_N": force,
                "A_tension_m2": a_tension,
                "A_compression_m2": a_comp,
                "compression_over_tension": a_comp / a_tension,
                "branch": branch,
            }
        )
    return out


def cog_reachability() -> dict[str, object]:
    """FI4(v). The remainder's height is NOT an input -- it is forced by the CoG.

    `_build_body` computes

        remainder_point = (deck_mass * deck_cog - first_moment) / remainder_mass

    and every arm midpoint lies in the joint plane, so the arms' first moment is
    `f * deck_mass * z_joint` and the remainder's height follows in closed form:

        z_r(f) = (z_cog - f * z_joint) / (1 - f)

    **THAT IS THE FLAG FI4(v) ASKS FOR, AND IT IS SHARPER THAN A SENSITIVITY.** The
    `41.33 m` is not a modelling choice that a shallow truss could be reconciled with by
    adjusting it: it is what the deck CoG at `35.0 m` REQUIRES once `f` of the mass is
    pinned at `24.67 m`. Inverting it gives the reachability statement increment 2 needs --
    the highest CoG any mass distribution inside a truss of depth `h` can reach is
    `z_joint + h/2`, because that is the highest the steel goes.
    """
    built = build_superstructure()
    body = built.bodies[0]
    z_joint = float(np.asarray(body.model.nodes[body.centre_node].xyz)[2])
    z_cog = float(np.asarray(body.deck_cog)[2])
    z_rem = float(np.asarray(body.remainder_point)[2])
    f = float(body.mass_fraction)

    closed_form = (z_cog - f * z_joint) / (1.0 - f)
    ladder = [
        {
            "f": ff,
            "z_remainder_m": (z_cog - ff * z_joint) / (1.0 - ff),
            "above_joints_m": (z_cog - ff * z_joint) / (1.0 - ff) - z_joint,
        }
        for ff in (0.5, 0.6, 0.75, 0.9)
    ]
    reach = [
        {
            "h_m": h,
            "max_cog_m": z_joint + h / 2.0,
            "above_joints_m": h / 2.0,
            "cog_shortfall_m": z_cog - (z_joint + h / 2.0),
        }
        for h in H_GRID
    ]
    return {
        "z_joint_m": z_joint,
        "z_deck_cog_m": z_cog,
        "deck_cog_above_joints_m": z_cog - z_joint,
        "z_remainder_m": z_rem,
        "remainder_above_joints_m": z_rem - z_joint,
        "remainder_mass_kg": float(body.remainder_mass),
        "mass_fraction": f,
        "closed_form_z_remainder_m": closed_form,
        "closed_form_error_m": abs(closed_form - z_rem),
        "ladder": ladder,
        "reachability": reach,
        "deepest_truss_still_short_m": max(
            (r["h_m"] for r in reach if r["cog_shortfall_m"] > 0.0), default=None
        ),
        "truss_depth_needed_for_the_cog_m": 2.0 * (z_cog - z_joint),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--forces", type=Path, default=ROOT / "docs" / "F4_member_forces.csv")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "F6b" / "truss_sizing.csv")
    ap.add_argument("--json", type=Path, default=ROOT / "results" / "F6b" / "truss_sizing.json")
    args = ap.parse_args(argv)

    rows_all = _rows(args.forces)
    answers: list[dict[str, object]] = []
    splits: dict[str, object] = {}

    for group, prefix, length, mu in GROUPS:
        rows = governing(rows_all, prefix)
        splits[group] = my_mz_split(rows_all, prefix)
        print(
            f"=== {group}: {len(rows)} governing rows, L = {length} m, mu = {mu} kg/m ===",
            flush=True,
        )
        for section in ("box", "triangle"):
            for h in H_GRID:
                for b in B_GRID:
                    row: dict[str, object] = {
                        "group": group,
                        "section": section,
                        "h_m": h,
                        "b_m": b,
                    }
                    ok_cell = True
                    for geometry in GEOMETRIES:
                        try:
                            s = size(section, rows, h, b, mu, geometry)
                        except ValueError as exc:
                            row["found"] = False
                            row[f"refused_{geometry}"] = str(exc)[:160]
                            ok_cell = False
                            continue
                        row[f"chord_A_m2_{geometry}"] = s.chord_area
                        row[f"chord_L_m_{geometry}"] = s.chord_buckling_length
                        row[f"chord_branch_{geometry}"] = s.chord_branch
                        row[f"diagonal_steel_m2_{geometry}"] = s.diagonal_steel_per_m
                        row[f"line_mass_kg_per_m_{geometry}"] = s.line_mass
                        row[f"mass_ratio_{geometry}"] = s.mass_ratio
                        if geometry == GEOMETRIES[0]:
                            row["chord_force_N"] = s.chord_force
                            row["chord_governing"] = s.chord_governing
                            row["diagonal_A_m2"] = s.diagonal_area_max
                            row["diagonal_force_N"] = s.diagonal_force_max
                            row["diagonal_governing"] = s.diagonal_governing
                            row["torsion_share_of_face_shear"] = s.torsion_share_of_face_shear
                            row["torsion_share_max"] = s.torsion_share_max
                            row["EI_proxy_Ac_h2"] = s.chord_area * h * h
                            row["EI_proxy_Ac_b2"] = s.chord_area * b * b
                            row["I_over_standin_h"] = s.chord_area * h * h / STANDIN_I
                    if ok_cell:
                        row["found"] = True
                        # THE HEADLINE MUST SURVIVE BOTH READINGS (R801). A cell that is
                        # mass-consistent under one geometry and not the other is not an
                        # answer, it is a choice of reading -- and the cell this sweep
                        # first reported, (3, 8), was exactly that.
                        row["mass_ratio_worst"] = max(
                            float(row[f"mass_ratio_{g}"]) for g in GEOMETRIES
                        )
                        row["consistent_under_both"] = float(row["mass_ratio_worst"]) <= 1.0
                    answers.append(row)
        ok = [
            a
            for a in answers
            if a["group"] == group and a.get("found") and a.get("consistent_under_both")
        ]
        if ok:
            shallowest = min(ok, key=lambda a: (float(a["h_m"]), float(a["b_m"])))
            print(
                "  shallowest mass-consistent UNDER BOTH readings: "
                f"{shallowest['section']} h={shallowest['h_m']} b={shallowest['b_m']} "
                f"worst ratio={float(shallowest['mass_ratio_worst']):.3f}"
            )
        else:
            print("  NO truss is mass-consistent under both readings in the declared grid")

    payload: dict[str, object] = {
        "answers": answers,
        "splits": splits,
        "hand_table": hand_table_check(),
        "cog_reachability": cog_reachability(),
        "inputs": {
            "D_over_t": D_OVER_T,
            "joint_allowance": JOINT_ALLOWANCE,
            "diagonal_angle_deg": DIAGONAL_ANGLE_DEG,
            "rho_steel": RHO_STEEL,
            "fy_pa": FY_S355,
            "h_grid": list(H_GRID),
            "b_grid": list(B_GRID),
            "governing_periods_s": list(GOVERNING_PERIODS),
            "standin_I_m4": STANDIN_I,
            "geometries": list(GEOMETRIES),
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    cols = sorted({k for a in answers for k in a})
    with args.out.open("w", encoding="utf-8", newline="") as fh:
        fh.write("# F6b truss sizing (FI) -- INDICATIVE: idealised pin-jointed truss, no\n")
        fh.write("# joint or connection checks, placeholder masses, heading 0 deg, Fy\n")
        fh.write("# assumed. Generated by scripts/measure/f6b_truss_sizing.py\n")
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for a in answers:
            w.writerow(a)
    cog = payload["cog_reachability"]
    assert isinstance(cog, dict)
    print()
    print("FI4(v) -- the remainder's height is FORCED, not chosen:")
    print(
        f"  joints at z = {cog['z_joint_m']:.3f} m; deck CoG at {cog['z_deck_cog_m']:.3f} m "
        f"({cog['deck_cog_above_joints_m']:.2f} m above)"
    )
    print(
        f"  remainder at z = {cog['z_remainder_m']:.3f} m "
        f"({cog['remainder_above_joints_m']:.2f} m above), closed form "
        f"{cog['closed_form_z_remainder_m']:.3f} m, error "
        f"{cog['closed_form_error_m']:.2e} m"
    )
    print(
        f"  a truss of depth h reaches a CoG of z_joint + h/2, so the CoG needs a depth "
        f"of {cog['truss_depth_needed_for_the_cog_m']:.2f} m"
    )

    args.json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\n  wrote {args.out.relative_to(ROOT).as_posix()} ({len(answers)} rows)")
    print(f"  wrote {args.json.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
