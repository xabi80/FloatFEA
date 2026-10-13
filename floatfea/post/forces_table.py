"""The member-force core: one implementation, shared by the script and `floatfea run`.

**WHY THIS MODULE EXISTS (FL1).** `scripts/measure/member_forces_table.py` held the
whole of it, and `floatfea run <config.yaml>` has to produce the same member forces
from a declared configuration. Two copies of this arithmetic would make FL1(c)'s
"reproduces F4's envelope EXACTLY" a coincidence that holds until one copy is edited;
one copy makes it structural. The script keeps its CLI, its labels and its summary and
calls in here for the numbers.

**NOTHING WAS REWRITTEN ON THE WAY IN.** Every function below was moved verbatim from
that script, comments included, because those comments record what each line was
corrected FROM -- R730's segment-equilibrium convention, R734's opposite-signed sags,
R736's exact axial, R739's tension sign at the publishing boundary, R744's assertion on
the published value rather than the intermediate. The proof that the move changed no
number is a byte diff of the regenerated deliverable, recorded in F4's own golden test
and in R1 step 1's report.

Two deliberate exceptions, both named at the site:

* `_gravity_nodal_load` and its `_GRAVITY_LOAD` cache were NOT moved. They are unused
  repo-wide and the docstring described a per-step call the window loop does not make,
  which is a claim about the code that CW0 does not allow to stand as prose. Deleted
  rather than carried (EK2: fixed or deleted, never extended).
* `_rotation`'s cache key was `(body.name, member.label)` and is now keyed on the
  model's identity. The old key collides across two builds of one deck at different
  sections, which is precisely what FM0's re-solve loop does; see that function.

`SystemExit` is raised in two places here rather than a library exception. That is how
it arrived and it is left alone in this commit, because changing an exception type is a
behaviour change and this commit's whole claim is that behaviour did not change. It is
recorded in step 1's report.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

import numpy as np
from numpy.typing import NDArray

from floatfea import basis
from floatfea.io.frames import GRAVITY_VECTOR
from floatfea.io.froude import to_full_scale
from floatfea.loads.joint_reactions import map_joint_reactions
from floatfea.model.platform import (
    BodyModel,
    Member,
    Superstructure,
    _outer_diameter,
    rigid_projection,
)
from floatfea.post.member_forces import element_equivalent_load, member_forces
from floatfea.solve.inertia_relief import solve_inertia_relief
from floatfea.solve.static import solve_superstructure_static

__all__ = [
    "Row",
    "compute_rows",
    "ComputedForces",
]


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


_ROTATION: dict[tuple[int, str], tuple[object, NDArray[np.float64]]] = {}


def _rotation(body: BodyModel, member: Member) -> NDArray[np.float64]:
    """The member's local axes. A constant of the geometry, so cached (31000 steps).

    **KEYED ON THE MODEL'S IDENTITY, NOT ON `body.name` (FL1).** The key was
    `(body.name, member.label)`, which is not unique across two builds of the same
    deck: `build_superstructure(measurement_sections=...)` returns bodies with the
    SAME names at a different geometry, so the second build read the first build's
    rotations out of this cache and no test could see it -- every shipped caller
    builds once.

    FM0's re-solve loop builds repeatedly at different sections by design, so the
    collision stops being latent. The key is `id(body.model)` and the entry holds a
    reference to the model, which is what stops CPython reusing that id for a later
    object. Identical for one build; correct for many.
    """
    key = (id(body.model), member.label)
    hit = _ROTATION.get(key)
    if hit is None:
        from floatfea.element.transform import rotation_matrix

        coords = body.model.nodes.coords()
        hit = (
            body.model,
            rotation_matrix(coords[member.node_a], coords[member.node_b]),
        )
        _ROTATION[key] = hit
    return hit[1]


def _station_values(
    body: BodyModel, member: Member, u_full: NDArray[np.float64], net: NDArray[np.float64]
) -> dict[str, NDArray[np.float64]]:
    """ROOT, MID and TIP in the member's local frame.

    ROOT and TIP are the element's two ends and are exact. MID is closed-form for a
    uniform net load: shear linear, so its mid value is the chord mean; moment parabolic,
    so its mid value is the chord mean plus `w L^2 / 8` with `w` the local transverse
    load per unit length. `N` and `T` are taken as the chord mean.

    **AND "THE NET FIELD IS A TRANSLATION" WAS FALSE (R730).** That sentence stood here
    to justify treating `N` and `T` as constant along the member. `_net_field` is
    `-rigid_projection(coords, ref) @ relief.acceleration`, which includes the ANGULAR
    part, so the field varies along a member whenever the body has angular acceleration.
    Measured over ninety (case, step, body) samples:

        worst |alpha| L_max / |a|  =  0.2239

    The rotational contribution is not zero. But the conclusion I drew from that was wrong
    in BOTH directions (R736):

    * **`N` is provably exact, not an approximation.** The angular part of the field is
      `alpha x r`, which is perpendicular to `r`; along a member `r` is the member axis, so
      the axial projection of the angular field is identically zero and `N` is constant
      whatever `alpha` is. Measured end-to-end variation: `0.000` everywhere.
    * **The BENDING closed form is the approximation**, and the figure for it was stated
      nowhere. It is a measured `4.0%`.

    And `0.2239` is itself one operating point: over the window the table envelopes, the
    same ratio reaches `17.067` sampling every twentieth step and `50.297` every seventh.
    A refined mesh would settle the bending term; F4 closes carrying that into F5's ledger.
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

    # R730 -- THE CONVENTION, WHICH THE FIRST VERSION AVERAGED ACROSS.
    #
    # `member_forces` returns the forces the ELEMENT EXERTS ON ITS NODES, so `end_a` and
    # `end_b` are an ACTION AND A REACTION -- its own docstring says so. The internal
    # action is `end_a` at `x = 0` and `-end_b` at `x = L`. Averaging the two raw ends
    # therefore computes a LOAD, not an internal force, and the arithmetic says so
    # exactly: conservation gives `Vz_a + Vz_b = weight`, so `0.5 * (end_a + end_b)` on
    # `Vz` is HALF THE MEMBER'S WEIGHT. Measured on `platform:hub2_arm` under self-weight:
    #
    #   0.5 * (a + b)  ->  Vz = +2299218.75   = exactly mu g L / 2
    #   0.5 * (a - b)  ->  Vz = -3832031.25   = the internal shear at midspan
    #
    # The published column was 46% LOW on stress -- 94.4 MPa against 175.3 -- which is the
    # direction that matters, and it reached a sent deliverable.
    #
    # ALL THREE STATIONS ARE NOW ONE CONVENTION, so the profile has a meaning: the
    # internal action as seen from the A end. `TIP` is therefore `-end_b` and not `end_b`.
    # The shear then varies monotonically from `-1532812.5` to `-6131250.0` over the span,
    # a change of exactly `-mu g L`, where the raw ends had a spurious zero crossing.
    # R739 -- THE AXIAL COLUMN WAS COMPRESSION-POSITIVE, against a convention locked at F0.
    #
    # `docs/conventions.md:320`: "Positive axial force: **tension positive**." `member_forces`
    # returns `k_local @ (t @ u) - t @ f_eq`, and `k u` is the NODAL force on the element --
    # uniformly, for every component. For the transverse components that coincides with the
    # internal action at the A end, which is why R730's segment-equilibrium cut validated
    # `ROOT = end_a` and `TIP = -end_b`. **For the axial it does not.** Measured on a sense
    # that cannot be argued with -- node B moved 1 mm OUTWARD along the member axis:
    #
    #     end_a[0]                              = -5.5101e+06
    #     EA/L x 1e-3  (true tension, Hooke)    = +5.5101e+06
    #     published N  (= end_a[0])             = -5.5101e+06     <-- for a STRETCH
    #
    # So a member in tension published a negative `N`, and `floatfea/checks/api_wsd.py` read
    # `axial_n >= 0.0` as tension: every over-unity station went to section 3.3.1 with
    # `F_a = 0.6 F_y` instead of 3.3.2 with the column allowable.
    #
    # Corrected HERE, at the publishing boundary, because that is where the locked
    # convention applies: the CSV is a published deliverable (EZ0) and `conventions.md` is
    # what it has to agree with.
    span = float(member.length)
    tip_internal = -tip
    root = root.copy()
    root[0] = -root[0]
    tip_internal[0] = -tip_internal[0]
    mid = 0.5 * (root + tip_internal)
    # THE PARABOLIC SAG, AND THE TWO PLANES CARRY OPPOSITE SIGNS (R734).
    #
    # Derived, not calibrated. `e_x x F = (0, -F_z, +F_y)`, so the standard beam relations
    # are `dM_z/dx = +V_y` and `dM_y/dx = -V_z`, with `dV/dx = -w`. Hence
    # `M_z'' = -w_y` and `M_y'' = +w_z`, and for a parabola `f(L/2) = chord - f'' L^2/8`:
    #
    #     mid My  =  chord  -  w_z L^2 / 8
    #     mid Mz  =  chord  +  w_y L^2 / 8        <-- the OPPOSITE sign
    #
    # **THE FIRST REPAIR GAVE BOTH PLANES THE SAME SIGN, so one of them was always going
    # to be wrong.** It was calibrated against one measured cell rather than derived, and
    # the cell could not see the error: `w_local[1]` is EXACTLY ZERO on all sixteen members
    # on the static basis, so the `Mz` term is unobservable there. Both of my published
    # cells, both static controls my own closing condition asked for, and both of the
    # reviewer's independent figures sat at `w_y = 0`.
    #
    # **A control that can only be taken where the quantity is zero is not a control.**
    # Measured on the row where it is largest -- `hub4:buoy12_arm`, `T_full = 12.5 s`,
    # step 219, `w_y = -7.1836e+03` -- the subtracting form gives `Mz = +1.091976e+06` and
    # the adding form `-3.046460e+04`, and the second is what segment equilibrium gives.
    chord_my, chord_mz = float(mid[4]), float(mid[5])
    sag_y = -w_local[2] * span * span / 8.0
    sag_z = +w_local[1] * span * span / 8.0
    mid[4] = mid[4] + sag_y
    mid[5] = mid[5] + sag_z

    # THE CONTROL THE FIRST REPAIR DID NOT HAVE, and it runs where the quantity is
    # NONZERO. A control that can only be taken where the quantity is zero is not a
    # control: `w_local[1]` is exactly `0.0` on all sixteen members on the static basis,
    # which is why one calibrated cell, two static controls and two independent reviewer
    # figures all missed a flipped sign on `Mz`.
    #
    # **IT ASSERTS ON THE PUBLISHED VALUE, NOT ON THE INTERMEDIATE (R744).** It compared
    # `sag_y` and `sag_z` -- the two local variables -- against their own load components,
    # which is a check on the two lines that DEFINE them and on nothing else. A one-
    # character reversion at the line that APPLIES them (`mid[5] = mid[5] - sag_z`) leaves
    # both intermediates correct and the published `Mz` wrong, and the control passed.
    # What the published MID carries is `mid - chord`, so that is the subject: the chord
    # mean is taken before the sags are applied and the difference is what is signed.
    #
    # NO THRESHOLD AND NO TOLERANCE. The derivation fixes the SIGN of each sag against the
    # sign of its own load component -- `M_y'' = +w_z` and `M_z'' = -w_y` give sags of
    # `-w_z L^2/8` and `+w_y L^2/8` -- so the check is a sign comparison and needs no
    # constant. It catches exactly the defect that shipped, and it cannot be satisfied by
    # a configuration that happens to sit at zero because it skips those.
    published = (
        (w_local[2], float(mid[4]) - chord_my, -1.0, "My/w_z"),
        (w_local[1], float(mid[5]) - chord_mz, +1.0, "Mz/w_y"),
    )
    for load, applied, want, plane in published:
        if load == 0.0 or applied == 0.0:
            continue
        if math.copysign(1.0, applied) != math.copysign(1.0, want * load):
            raise SystemExit(
                f"{member.label}: the {plane} parabolic sag reaches the PUBLISHED MID "
                f"with the wrong sign -- load {load!r}, published sag {applied!r}. "
                "`M_y'' = +w_z` and `M_z'' = -w_y`, so the two planes carry OPPOSITE "
                "signs; giving them the same one is R734 and flipping one at the line "
                "that applies it is R744."
            )
    return {"ROOT": root, "MID": mid, "TIP": tip_internal}


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


@dataclass(frozen=True)
class ComputedForces:
    """What one pass over the window produces.

    `rows` is the publishable table. `instant` and `instant_sens` carry the worst
    per-instant `(sigma, period)` per member-station, inside and outside the governing
    basis respectively, which is what the summary's two blocks report.
    """

    rows: list[Row]
    static: dict[tuple[str, str, str], NDArray[np.float64]]
    instant: dict[tuple[str, str, str], tuple[float, float]]
    instant_sens: dict[tuple[str, str, str], tuple[float, float]]


def compute_rows(
    built: Superstructure,
    inp: Any,
    raw: Any,
    governing_periods: tuple[float, ...],
    progress: Any = None,
) -> ComputedForces:
    """Every basis, over every case and step. Moved verbatim from the script's `main`.

    `governing_periods` is a PARAMETER rather than a module constant, because that is
    the whole of what a configuration changes about this loop (FL1(a)'s `load_cases`,
    FL2(d)'s per-case band check). The script passes its own `GOVERNING_PERIODS` and so
    is unchanged; a config passes the admitted set it declares.

    `progress` is called with one line per case when given, so the script keeps printing
    what it printed and the library stays silent by default.
    """
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
    instant_sens: dict[tuple[str, str, str], tuple[float, float]] = {}
    peak: dict[tuple[str, str, str], tuple[float, float, Any]] = {}

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
                        at_instant = static[key] + values
                        sigma_now, _tau_now = _stresses(member, at_instant)
                        # R740: KEEP THE COMPONENTS AT THE PEAK INSTANT, not just sigma.
                        # The CSV carried `static`, `dynamic_*` and `total_*` only -- all
                        # ENVELOPES -- so a consumer computing a utilisation got the
                        # per-component bound while a label said per-instant. The gap at the
                        # governing station is `0.103` in U, `4.3x` the K sensitivity.
                        # ONLY WITHIN THE GOVERNING BASIS. Tracking the global peak
                        # dropped every station whose largest response is at `T = 10 s` --
                        # the breaking wave, which is most of them -- so the first version
                        # of this emitted 2 `total_instant` rows instead of 32. The peak
                        # that matters is the peak of the cases allowed to govern.
                        if (
                            period in governing_periods
                            and sigma_now > peak.get(key, (0.0, 0.0, None))[0]
                        ):
                            peak[key] = (sigma_now, float(period), at_instant)
                        # EZ2(a)/(b): only the IN-RANGE cases may govern. The two outside
                        # are tracked separately and reported in their own block -- a
                        # breaking wave and a wave too long for this height cannot set a
                        # design envelope, and letting them would have been the finding.
                        target = instant if period in governing_periods else instant_sens
                        if sigma_now > target.get(key, (0.0, 0.0))[0]:
                            target[key] = (sigma_now, float(period))
        for key in sorted(worst_hi):
            for tag, dyn in (("max", worst_hi[key]), ("min", worst_lo[key])):
                rows.append(Row(key[0], key[1], key[2], period, f"dynamic_{tag}", dyn))
                rows.append(Row(key[0], key[1], key[2], period, f"total_{tag}", static[key] + dyn))
        if progress is not None:
            progress(f"  T_full = {period:4g} s: {lam.shape[0]} steps")

    # R740: one `total_instant` row per station -- the six components AT the step where
    # sigma peaks, on EZ2's governing basis. This is the row a code check must read, and
    # until it existed the only honest label for a utilisation was "envelope bound".
    if len(peak) != len(static):
        raise SystemExit(
            f"{len(peak)} per-instant rows for {len(static)} member-stations. Every station "
            "must have a governing-basis peak; a shortfall means a station's peak was taken "
            "outside the governing cases and then dropped."
        )
    for key, (_sigma, period, values) in sorted(peak.items()):
        rows.append(Row(key[0], key[1], key[2], period, "total_instant", values))

    for key, values in sorted(static.items()):
        rows.append(Row(key[0], key[1], key[2], float("nan"), "static", values))

    return ComputedForces(rows=rows, static=static, instant=instant, instant_sens=instant_sens)
