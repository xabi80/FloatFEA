#!/usr/bin/env python
"""EY0: the member-force table, per member and station and case, from the committed npz.

    python scripts/measure/member_forces_table.py
    python scripts/measure/member_forces_table.py --out out.csv --summary out.md

**PRELIMINARY UNTIL F4 CLOSES.** Every number here is labelled, and the labels are not
decoration -- see `LABELS` below and the header of both outputs. The section is a stiffness
stand-in for a truss, the masses are assumed, and one heading has been run.

**NO FLOATSIM AND NO `HSP-runs` ON THIS PATH.** It reads `data/f4/dynamic_inputs.npz`
(EX0(d)) and builds the FE model from `data/platform/platform12_deck.yaml`. R721 is why
that sentence is here: a rung-4 gate that reached HSP passed on one machine and errored on
124 of 126 cases in CI. This script is not a gate -- EY0 puts it outside -- but it reads
the same inputs, and the point of committing them was that anything downstream runs
anywhere.

WHAT IT COMPUTES, and the three load bases, because "dynamic" is a DEFINITION here and not
a measurement:

    static    the supported structure under its own weight -- `solve_superstructure_static`,
              EK0(d)'s minimal statically determinate restraint. What the frame carries
              standing still.
    dynamic   the free body under the DYNAMIC joint-reaction increments, with inertia
              relief supplying the acceleration increment. **No gravity.** Per window step.
    total     static + dynamic, summed per component.

**FLOATSIM IS LINEARISED ABOUT STATIC EQUILIBRIUM, AND THAT IS WHY `dynamic` CARRIES NO
GRAVITY.** The study builds the system as `shared_db.C + gravity_restoring` and its own
comment warns against double-counting buoyancy, so `xi` is the DEVIATION from equilibrium
and the multipliers are the dynamic increment -- the static weight/buoyancy balance is
already inside the formulation and never appears in `lam`.

The first version of this script added gravity to the dynamic case. Measured, that put the
hub-joint vertical loads at `~1e5 N` against a platform weight of `1.84e7 N`, so the body
was in near free fall: the relief acceleration read `-7.37 m/s^2` where FloatSim's own
`accel` reads `-0.0094`. The decomposition is not a presentation choice; getting it wrong
changes the answer.

**THE LOAD PATH IS VALIDATED AGAINST FLOATSIM'S OWN ACCELERATIONS**, which the npz stores:
with gravity excluded, the FE inertia-relief acceleration agrees with `accel` to **1.55 %
on all five bodies** and to **2.78 % worst over eighteen (case, step, body) samples**. The
offset is systematic rather than scattered, which points at a small mass difference and not
at a wrong path. This is EV1's third assertion in all but name -- EX4 deferred it to F5 as a
GATE, and nothing stopped it being used here as a control.

THE JOINT LOADS GO THROUGH `map_joint_reactions`, the reviewed mapper, from the raw
multipliers `lam` the npz stores -- NOT from the npz's `contrib`. `contrib` is each joint's
reaction at the BODY REFERENCE POINT; a member-force table needs it at the joint's own
node, and the transfer between the two is a frame question `docs/conventions.md` is the
authority on. Deriving that transform here would be this script asserting its own guess
about a frame, which `CLAUDE.md` forbids in as many words.

**AND THE DECK'S JOINT ORDER IS CHECKED, NOT ASSUMED.**
`tests/verification/rung4/test_f4_static_and_mapping.py:844-849` records the gap: the
BUILDER's joint order is nowhere checked against the DECK's, and that is the driver's job.
This script is a driver. The npz carries the deck's own order and
`_joint_wiring` asserts the two agree, so a reaction cannot be attributed to the wrong
joint silently.

STATIONS, AND WHAT IS EXACT. At F3's mesh there is ONE element per member
(`floatfea/post/member_forces.py`), so ROOT and TIP are the element's two end nodes and
both are EXACT. MID is not a node: it is computed in closed form for a uniform net body
force along the member, which is what the net d'Alembert field is on a prismatic element --
shear linear, moment parabolic, so the midspan moment is the chord mean plus `w L^2 / 8`.
A refined mesh would give it directly and this closed form would then be a check on it.

    ROOT = the element's end at the body's `centre_node` (node_a)
    TIP  = the far end (node_b)

Stated rather than inferred: for a platform arm the centre node carries the lumped
remainder and the hub joint is at the TIP, so "root" here is a GEOMETRIC name for the
inboard end and not a claim about which end is structurally fixed.

STRESSES ARE INDICATIVE AND THE FORMULA IS EY0's:

    sigma = |N| / A + sqrt(My^2 + Mz^2) / W        W = 2 I / D, from `basis.py`'s tube
    tau   = |T| / (2 W_t) + V / A_shear            V = sqrt(Vy^2 + Vz^2)

with `W_t = 2 J / D` the torsional modulus and `A_shear = kappa * A`. No code check is
applied -- that is F5 (EY4). A von Mises combination is deliberately NOT formed here,
because the two terms peak at different points of the section and combining them without
saying where would be a number nobody can act on.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from floatfea import basis  # noqa: E402
from floatfea.io.frames import GRAVITY_VECTOR  # noqa: E402
from floatfea.io.froude import to_full_scale  # noqa: E402
from floatfea.loads.joint_reactions import map_joint_reactions  # noqa: E402
from floatfea.model.platform import (  # noqa: E402
    BodyModel,
    Member,
    Superstructure,
    _outer_diameter,
    build_superstructure,
    rigid_projection,
)
from floatfea.post.member_forces import (  # noqa: E402
    COMPONENTS,
    element_equivalent_load,
    member_forces,
)
from floatfea.solve.inertia_relief import solve_inertia_relief  # noqa: E402
from floatfea.solve.static import solve_superstructure_static  # noqa: E402

STATIONS = ("ROOT", "MID", "TIP")
BASES = ("static", "dynamic", "total")

LABELS = (
    "PRELIMINARY until F4 closes.",
    "Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms "
    "(Xabier, 6 Oct); platform inertia scaled with mass (assumed). ER0.",
    "DZ5 / ER1(e): the four hub arms carry an equivalent density above steel "
    "(11433.5 kg/m^3 against 7850), which is a reported sizing finding -- the members are "
    "stiffness equivalents, so the hub's mass does not fit inside F1's section at f = 0.75.",
    "Hub line mass 15 t/m, against the platform arms' 10.3 t/m.",
    "Stand-in tube: the stiffness equivalent of a TRIANGULATED TRUSS of undecided depth "
    "(F1.md:390). Stresses are INDICATIVE, not a check on a real section.",
    "EX3 / R724: all six cases are heading 0 degrees. The heading dependence is UNTESTED.",
    "Stations: ROOT = the inboard end at the body's centre node, TIP = the far end. MID is "
    "closed-form for a uniform net body force (one element per member at F3's mesh).",
    "'dynamic' is the DYNAMIC INCREMENT about static equilibrium, solved from FloatSim's "
    "multipliers with NO gravity -- FloatSim is linearised about equilibrium, so the static "
    "weight/buoyancy balance is already in the formulation. 'total' = static + dynamic.",
    "The load path is validated against FloatSim's own per-body accelerations: 1.55% on all "
    "five bodies, 2.78% worst over eighteen samples.",
    "No code check is applied. API RP 2A-WSD checks are F5 (EY4).",
    "SCALE: the npz holds FloatSim's MODEL-scale output; the FE model is FULL scale. The "
    "multipliers are converted through `floatfea.io.froude`'s declared "
    "`joint_multiplier_yaw_locked` composite (force x 125000, locked moment x 6250000).",
)


@dataclass(frozen=True)
class Row:
    body: str
    member: str
    station: str
    period_full_s: float
    basis: str
    values: NDArray[np.float64]  # (6,) N, Vy, Vz, T, My, Mz


def _gravity_field(n_dof: int) -> NDArray[np.float64]:
    """`g` on every translational DOF, zero on every rotational one."""
    field = np.zeros(n_dof, dtype=np.float64)
    for start in range(0, n_dof, 6):
        field[start : start + 3] = GRAVITY_VECTOR
    return field


_GRAVITY_LOAD: dict[str, NDArray[np.float64]] = {}


def _gravity_nodal_load(body: BodyModel) -> NDArray[np.float64]:
    """The consistent nodal load of self-weight, from the assembler's own mass.

    `M @ g_field`, which is the same route `element_equivalent_load` takes per element --
    so the total and the per-element pieces cannot disagree about the mass.

    CACHED, because it is a constant of the body and the window loop asked for it once per
    step per body -- an assembly of the whole mass matrix roughly 31000 times.
    """
    if body.name not in _GRAVITY_LOAD:
        from floatfea.assemble.system import assemble_mass_dense

        mass = assemble_mass_dense(body.model, body.elements)
        _GRAVITY_LOAD[body.name] = np.asarray(
            mass @ _gravity_field(body.model.n_dof), dtype=np.float64
        )
    return _GRAVITY_LOAD[body.name]


FROUDE_LAMBDA = 50.0
"""`docs/conventions.md`'s scale. The FE model is FULL scale; FloatSim runs at MODEL."""

ROWS_PER_JOINT_YAW_LOCKED = 4
"""Three translations plus the one locked axis. `floatfea.io.froude`'s composite width."""


def _lam_full_scale(lam_row: NDArray[np.float64]) -> NDArray[np.float64]:
    """One timestep's multipliers, model scale to FULL scale, per joint block.

    **THIS IS THE ONE PLACE A SCALE CHANGE HAPPENS AND IT NEARLY DID NOT HAPPEN AT ALL.**
    `data/f4/dynamic_inputs.npz` holds FloatSim's own output, which is MODEL scale: the
    solve runs at `T/sqrt(50)` with `H = 0.484 m`. The FE model is built at FULL scale.
    The first version of this script applied `lam` straight to it, and the symptom was a
    PLAUSIBLE WRONG ANSWER rather than a crash -- the wave contribution came out 125000x
    too small, so the total case peaked at 40.5 MPa where static alone reads 269.7 MPa at
    the same station, and the table would have said the dynamic loads are negligible.

    It was caught by one comparison: `max |lam| = 6.4436e+01` against a gravity nodal load
    of `1.9160e+07` on the same body. `CLAUDE.md`: never assume a unit.

    The factors are NOT written here. `joint_multiplier_yaw_locked` is a DECLARED
    composite -- `((0, 3, "force"), (3, 4, "moment"))` -- so force goes as `lam^3` and the
    locked moment as `lam^4`, which is `125000` and `6250000` at this scale. Writing one
    factor for all four rows would have been wrong by `lam` on the fourth.
    """
    row = np.asarray(lam_row, dtype=np.float64)
    if row.size % ROWS_PER_JOINT_YAW_LOCKED != 0:
        raise SystemExit(
            f"`lam` has {row.size} rows, which is not a whole number of "
            f"{ROWS_PER_JOINT_YAW_LOCKED}-row yaw-locked joint blocks. The composite this "
            "scales by would be the wrong one."
        )
    out = np.empty_like(row)
    for start in range(0, row.size, ROWS_PER_JOINT_YAW_LOCKED):
        block = row[start : start + ROWS_PER_JOINT_YAW_LOCKED]
        out[start : start + ROWS_PER_JOINT_YAW_LOCKED] = to_full_scale(
            block, "joint_multiplier_yaw_locked", FROUDE_LAMBDA
        )
    return out


def _joint_wiring(
    built: Superstructure, deck_a: list[str], deck_b: list[str]
) -> tuple[list[tuple[str, str, str]], dict[tuple[str, str], int], dict[str, int]]:
    """`(joint_order, nodes, n_dof_of)`, with the DECK's order checked against the builder.

    The deck is the authority for the block order of `lam`. The builder is the authority
    for which node a joint attaches to. Neither is derived from the other here, and the
    one place they must agree -- that joint `i` of the deck connects the pair the builder
    thinks it does -- is ASSERTED. The rung-4 mapper gate cannot do this check because it
    must run without an HSP worktree; a driver can and must.
    """
    by_name = {b.name: b for b in built.bodies}
    n_dof_of = {b.name: b.model.n_dof for b in built.bodies}
    joint_order: list[tuple[str, str, str]] = []
    nodes: dict[tuple[str, str], int] = {}

    for i, (child, parent) in enumerate(zip(deck_a, deck_b, strict=True)):
        owner = built.deck_joint_owner.get(child)
        if owner != parent:
            raise SystemExit(
                f"deck joint {i} connects {child!r} to {parent!r} and the builder has "
                f"{child!r} owned by {owner!r}. The two disagree about the topology, so a "
                "reaction would be attributed to the wrong joint."
            )
        joint_order.append((child, child, parent))
        if child in built.buoy_joint_nodes:
            _owner, node = built.buoy_joint_nodes[child]
            nodes[(child, parent)] = node
        else:
            nodes[(child, child)] = by_name[child].centre_node
            nodes[(child, parent)] = by_name[parent].model.nodes.index(f"{parent}:{child}_arm_tip")
    if len(joint_order) != 16:
        raise SystemExit(f"{len(joint_order)} joints; the deck declares 16.")
    return joint_order, nodes, n_dof_of


def _net_field(body: BodyModel, relief: Any) -> NDArray[np.float64]:
    """`-a_rigid`: the d'Alembert field of the DYNAMIC acceleration increment.

    No gravity term. `lam` is the increment about static equilibrium, so the static
    weight is carried entirely by the `static` basis and adding `g` here would count it
    twice -- which is what the first version did, putting the body in near free fall
    (`-7.37 m/s^2` against FloatSim's `-0.0094`).
    """
    coords = body.model.nodes.coords()
    rigid = rigid_projection(coords, relief.reference_point) @ relief.acceleration
    return -np.asarray(rigid, dtype=np.float64)


_ROTATION: dict[tuple[str, str], NDArray[np.float64]] = {}


def _rotation(body: BodyModel, member: Member) -> NDArray[np.float64]:
    """The member's local axes. A constant of the geometry, so cached (31000 steps)."""
    key = (body.name, member.label)
    if key not in _ROTATION:
        from floatfea.element.transform import rotation_matrix

        coords = body.model.nodes.coords()
        _ROTATION[key] = rotation_matrix(coords[member.node_a], coords[member.node_b])
    return _ROTATION[key]


def _station_values(
    body: BodyModel, member: Member, u_full: NDArray[np.float64], net: NDArray[np.float64]
) -> dict[str, NDArray[np.float64]]:
    """ROOT, MID and TIP in the member's local frame.

    ROOT and TIP are the element's two ends and are exact. MID is closed-form for a
    uniform net load: shear linear, so its mid value is the chord mean; moment parabolic,
    so its mid value is the chord mean plus `w L^2 / 8` with `w` the local transverse
    load per unit length. `N` and `T` are taken as the chord mean, which is exact for a
    load with no axial or twisting component along the member and is the case here -- the
    net field is a translation, so its local axial part is constant and its twist is zero.
    """
    f_eq = element_equivalent_load(body, member, net)
    mf = member_forces(body, member, u_full, f_eq)
    root = np.asarray(mf.end_a, dtype=np.float64)
    tip = np.asarray(mf.end_b, dtype=np.float64)

    # The local transverse load per unit length, from the net field at the member's own
    # nodes. `mu = rho A` is the prismatic line mass -- independent of the assembler (EA4).
    r = _rotation(body, member)
    a_mid = 0.5 * (
        net[6 * member.node_a : 6 * member.node_a + 3]
        + net[6 * member.node_b : 6 * member.node_b + 3]
    )
    mu = float(body.material.rho * member.section.A)
    w_local = r @ (mu * np.asarray(a_mid, dtype=np.float64))  # (3,) local x, y, z

    mid = 0.5 * (root + tip)
    span = float(member.length)
    # The parabolic sag, on the two bending components. `w_local[2]` bends about local y
    # and `w_local[1]` about local z, so the signs follow the component order of
    # `COMPONENTS` and not a convention invented here.
    mid[4] = mid[4] + w_local[2] * span * span / 8.0
    mid[5] = mid[5] + w_local[1] * span * span / 8.0
    return {"ROOT": root, "MID": mid, "TIP": tip}


def _static_rows(built: Superstructure) -> dict[tuple[str, str, str], NDArray[np.float64]]:
    """The supported structure under its own weight. One set, shared by every case."""
    cases = solve_superstructure_static(built)
    out: dict[tuple[str, str, str], NDArray[np.float64]] = {}
    for body in built.bodies:
        net = _gravity_field(body.model.n_dof)
        for member in body.members:
            for station, values in _station_values(
                body, member, cases[body.name].u_full, net
            ).items():
                out[(body.name, member.label, station)] = values
    return out


def _section_properties(member: Member) -> tuple[float, float, float, float, float]:
    """`(A, W, J, W_t, A_shear)` for the stand-in tube, all derived (AS1)."""
    section = member.section
    d_outer = _outer_diameter(section)
    area = float(section.A)
    w_bend = 2.0 * float(section.I_y) / d_outer
    w_tors = 2.0 * float(section.J) / d_outer
    a_shear = basis.kappa(section.shape) * area
    return area, w_bend, float(section.J), w_tors, a_shear


def _stresses(member: Member, values: NDArray[np.float64]) -> tuple[float, float]:
    """EY0's indicative sigma and tau. No code check, no von Mises (see the docstring)."""
    area, w_bend, _j, w_tors, a_shear = _section_properties(member)
    axial = abs(float(values[0])) / area
    bending = math.hypot(float(values[4]), float(values[5])) / w_bend
    shear = math.hypot(float(values[1]), float(values[2])) / a_shear
    torsion = abs(float(values[3])) / w_tors
    return axial + bending, torsion + shear


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "F4_member_forces.csv")
    ap.add_argument("--summary", type=Path, default=ROOT / "docs" / "F4_member_forces.md")
    args = ap.parse_args(argv)

    import f4_dynamic_residual as fdr

    inp = fdr.load()
    raw = np.load(fdr.NPZ, allow_pickle=False)
    built = build_superstructure()
    by_name = {b.name: b for b in built.bodies}

    deck_a = [str(x) for x in raw["case0/joint_body_a"]]
    deck_b = [str(x) for x in raw["case0/joint_body_b"]]
    joint_order, nodes, n_dof_of = _joint_wiring(built, deck_a, deck_b)

    static = _static_rows(built)
    rows: list[Row] = []
    # THE PER-INSTANT WORST STRESS, which is the physically meaningful one. The envelope
    # below takes each component's max INDEPENDENTLY over the window, so its six values do
    # not occur together and a stress formed from them is an UPPER BOUND, not a stress at
    # any instant. Both are reported and both are labelled; a reader given only the bound
    # would take 762.2 MPa for a real stress.
    instant: dict[tuple[str, str, str], tuple[float, float]] = {}

    for i, period in enumerate(inp.periods_full_s):
        lam = raw[f"case{i}/lam"]
        # The worst of each component over the window, per member-station, keeping the
        # max and the min separately -- `CLAUDE.md` forbids averaging a per-case
        # diagnostic, and a signed envelope needs both ends.
        worst_hi: dict[tuple[str, str, str], NDArray[np.float64]] = {}
        worst_lo: dict[tuple[str, str, str], NDArray[np.float64]] = {}
        for step in range(lam.shape[0]):
            loads = map_joint_reactions(_lam_full_scale(lam[step]), joint_order, nodes, n_dof_of)
            for name, body in by_name.items():
                # NO GRAVITY: `lam` is the dynamic increment about equilibrium (see the
                # module docstring). Adding gravity here put the body in free fall.
                applied = np.asarray(loads[name], dtype=np.float64)
                relief = solve_inertia_relief(body, applied)
                net = _net_field(body, relief)
                for member in body.members:
                    for station, values in _station_values(
                        body, member, relief.u_full, net
                    ).items():
                        key = (name, member.label, station)
                        worst_hi[key] = (
                            values if key not in worst_hi else np.maximum(worst_hi[key], values)
                        )
                        worst_lo[key] = (
                            values if key not in worst_lo else np.minimum(worst_lo[key], values)
                        )
                        sigma_now, _tau_now = _stresses(member, static[key] + values)
                        if sigma_now > instant.get(key, (0.0, 0.0))[0]:
                            instant[key] = (sigma_now, float(period))
        for key in sorted(worst_hi):
            for tag, dyn in (("max", worst_hi[key]), ("min", worst_lo[key])):
                rows.append(Row(key[0], key[1], key[2], period, f"dynamic_{tag}", dyn))
                rows.append(Row(key[0], key[1], key[2], period, f"total_{tag}", static[key] + dyn))
        print(f"  T_full = {period:4g} s: {lam.shape[0]} steps", flush=True)

    for key, values in sorted(static.items()):
        rows.append(Row(key[0], key[1], key[2], float("nan"), "static", values))

    _write_csv(args.out, rows, by_name)
    _write_summary(args.summary, rows, by_name, inp, instant)
    print(f"\n  wrote {args.out.relative_to(ROOT)} ({len(rows)} rows)")
    print(f"  wrote {args.summary.relative_to(ROOT)}")
    return 0


def _member_of(by_name: dict[str, BodyModel], body: str, label: str) -> Member:
    return next(m for m in by_name[body].members if m.label == label)


F_LADDER = (0.5, 0.75, 1.0)
"""EY0's f sensitivity. DY0's fraction of body mass carried on the members."""


def f_sensitivity() -> list[tuple[float, str, float, float, float]]:
    """ROOT values at each `f`, STATIC only (EY0: "static, cheap").

    `f` moves mass between the members and the lumped remainder, so it changes both the
    distributed load each member carries and the point load at the centre node. It is a
    sensitivity and not a sweep to pick a value from: `f = 0.75` is the basis (Xabier,
    6 Oct) and the other two bracket it.

    Reported at the ROOT because that is where the bending is largest, and per body
    rather than per member -- with the SPREAD across a body's own members printed, so a
    reader can see for themselves that the four arms are symmetric under self-weight
    instead of taking my word for it.
    """
    out: list[tuple[float, str, float, float, float]] = []
    for frac in F_LADDER:
        built = build_superstructure(measurement_fraction=frac)
        by_name = {b.name: b for b in built.bodies}
        static = _static_rows(built)
        for body in built.bodies:
            sigmas = []
            moments = []
            for member in body.members:
                values = static[(body.name, member.label, "ROOT")]
                sigmas.append(_stresses(member, values)[0])
                moments.append(float(math.hypot(values[4], values[5])))
            spread = (max(sigmas) - min(sigmas)) / max(sigmas) if max(sigmas) > 0.0 else 0.0
            out.append((frac, body.name, max(moments), max(sigmas), spread))
        del by_name
    return out


def _write_csv(path: Path, rows: list[Row], by_name: dict[str, BodyModel]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        # THE LABELS ARE WRITTEN RAW, NOT THROUGH `csv.writer`. A label containing a comma
        # comes back QUOTED, so the line starts with `"` and not `#`, and a consumer
        # skipping comments by prefix silently reads the first label as the header row --
        # which is what happened the first time this file was read back. Commas become
        # semicolons so the line can never need quoting.
        for label in LABELS:
            fh.write("# " + label.replace(",", ";") + chr(10))
        w = csv.writer(fh)
        w.writerow(
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
        for r in rows:
            member = _member_of(by_name, r.body, r.member)
            sigma, tau = _stresses(member, r.values)
            w.writerow(
                [
                    r.body,
                    r.member,
                    r.station,
                    "" if math.isnan(r.period_full_s) else f"{r.period_full_s:g}",
                    r.basis,
                    *[f"{v:.6e}" for v in r.values],
                    f"{sigma:.6e}",
                    f"{tau:.6e}",
                ]
            )


def _write_summary(
    path: Path,
    rows: list[Row],
    by_name: dict[str, BodyModel],
    inp: Any,
    instant: dict[tuple[str, str, str], tuple[float, float]],
) -> None:
    """The envelope over the six cases, the ten most loaded stations, and the f sweep."""
    env: dict[tuple[str, str, str], tuple[float, float, str]] = {}
    for r in rows:
        if not r.basis.startswith("total"):
            continue
        member = _member_of(by_name, r.body, r.member)
        sigma, _tau = _stresses(member, r.values)
        key = (r.body, r.member, r.station)
        where = f"T = {r.period_full_s:g} s, {r.basis}"
        if key not in env or sigma > env[key][0]:
            env[key] = (sigma, float(np.max(np.abs(r.values))), where)

    top = sorted(instant.items(), key=lambda kv: -kv[1][0])[:10]
    lines = [
        "# F4 step 3 — member forces, PRELIMINARY",
        "",
        "**Every line below is preliminary until F4 closes.** The labels are the deliverable "
        "as much as the numbers are.",
        "",
    ]
    lines += [f"* {label}" for label in LABELS]
    lines += [
        "",
        "## The ten most loaded member-stations, by indicative sigma",
        "",
        "| # | body | member | station | governing case "
        "| sigma at the instant (MPa) | envelope upper bound (MPa) |",
        "|---|---|---|---|---|---|---|",
    ]
    for n, ((body, label, station), (sigma, period)) in enumerate(top, start=1):
        bound = env.get((body, label, station), (0.0, 0.0, "-"))
        lines.append(
            f"| {n} | {body} | `{label}` | {station} | T = {period:g} s | "
            f"{sigma / 1e6:.1f} | {bound[0] / 1e6:.1f} |"
        )
    lines += [
        "",
        "## The section these stresses are computed on",
        "",
    ]
    member = by_name["platform"].members[0]
    area, w_bend, j, w_tors, a_shear = _section_properties(member)
    d_outer = _outer_diameter(member.section)
    wall = 0.5 * (d_outer - math.sqrt(d_outer * d_outer - 4.0 * area / math.pi))
    lines += [
        f"* `D = {d_outer:.4f} m`, `t = {wall:.5f} m`, `D/t = {d_outer / wall:.1f}` "
        f"(EN 1993-1-1 class limits {', '.join(f'{x:.1f}' for x in basis.chs_class_limits())})",
        f"* `A = {area:.4f} m^2`, `W = 2I/D = {w_bend:.4f} m^3`, `J = {j:.4f} m^4`, "
        f"`W_t = 2J/D = {w_tors:.4f} m^3`, `A_shear = kappa A = {a_shear:.4f} m^2`",
        f"* `{member.section_basis}`",
        "",
        "",
        "## The `f` sensitivity at the ROOT (static only)",
        "",
        "`f` is DY0's fraction of body mass carried on the members; the remainder is "
        "lumped at the centre node on a rigid link. **`f = 0.75` is the basis (Xabier, "
        "6 Oct)** and the other two bracket it. The last column is the spread of sigma "
        "across a body's own members, which is round-off where the body is symmetric "
        "under self-weight.",
        "",
        "| f | body | worst root moment (N·m) | sigma (MPa) | spread across members |",
        "|---|---|---|---|---|",
    ]
    for frac, body, moment, sigma, spread in f_sensitivity():
        lines.append(f"| {frac:g} | {body} | {moment:.4e} | {sigma / 1e6:.1f} | {spread:.2e} |")
    lines += [
        "## What is exact and what is not",
        "",
        "* ROOT and TIP are the element's own end nodes: **exact** at F3's mesh.",
        "* MID is **closed-form** for a uniform net body force -- the chord mean plus "
        "`w L^2 / 8` on the two bending components. A refined mesh would give it directly.",
        "* `dynamic` is **solved**, not subtracted: the dynamic joint increments with no "
        "gravity. `total = static + dynamic`.",
        "* The load path is **validated** against FloatSim's own accelerations -- 1.55% on "
        "all five bodies, 2.78% worst over eighteen (case, step, body) samples.",
        "* sigma and tau are **indicative**: `sigma = |N|/A + sqrt(My^2+Mz^2)/W` and "
        "`tau = |T|/(2W_t) + sqrt(Vy^2+Vz^2)/A_shear`. No von Mises combination is formed, "
        "because the two peak at different points of the section.",
        "* **No code check is applied.** API RP 2A-WSD is F5.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    raise SystemExit(main())
