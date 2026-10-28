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


ROWS_PER_JOINT_YAW_LOCKED = 4
"""Three translations plus the one locked axis. `floatfea.io.froude`'s composite width."""


def checked_joint_reactions(raw: Any, index: int) -> Any:
    """`case{index}/lam`, held to all FOUR properties its schema declares.

    **FOUR, and the count is the point.** This enumeration said THREE for one commit, and
    listed `n_rows`, `dtype` and `values`. `docs/load-interchange-v1.md:110` declares
    `lam[N,n_rows]  multipliers, dt-free, physical` -- and `N` was the property missing
    from the list, which is how it came to be the property missing from the code. A
    sentence that is right about the axes its author swept and silent about the one with
    nothing on it is R755, this milestone's first blocking finding, and R1063 is it
    recurring as the newest:

        N        R1063 -- see THE WINDOW LENGTH. The axis the list omitted.
        n_rows   guarded since F4 -- `ROWS_PER_JOINT_YAW_LOCKED` below, which refuses a
                 transposed array by name
        dtype    R1051, and NARROWED by R1059 -- see WHICH FLOATING WIDTH
        values   R1058 -- see THE VALUES, which is the half a dtype cannot decide

    **IT TAKES THE FILE AND AN INDEX, NOT AN ARRAY.** Two reasons, and the first is the
    one that forced it: deciding `N` needs a SECOND key of the same case, which a caller
    handed only `lam` cannot supply. And it makes this the one door -- the previous
    signature let a caller reach `raw[f"case{i}/lam"]` and skip the decision entirely,
    which is the shape R1022 found at the period readers.

    `docs/load-interchange-v1.md:110` declares `lam[N,n_rows]  multipliers, dt-free,
    physical`. Nothing between the npz and this module checked that, and
    `np.asarray(..., dtype=np.float64)` converts whatever it is given:

        bool    -> 1.0 / 0.0
        <U8     -> re-parsed from TRUNCATED text
        int64   -> the truncated multipliers

    Driven by the reviewer through the real CLI on the shipped example's own recipe, one
    variable moved and everything else held:

        float64 (control)  EXIT 0  governing U = 1.71167  platform:hub4_arm  3.3.2
        bool               EXIT 0  governing U = 0.995379 platform:hub1_arm  3.3.2
        <U8                EXIT 0  governing U = 1.71654  platform:hub4_arm  3.3.2
        int64              EXIT 0  governing U = 1.73988  platform:hub4_arm  3.2.3 bending

    All four wrote all three artifacts. **`U = 0.995379` reads as PASSING where the truth
    is `1.71167`** -- a failing structure published as passing, which is the failure mode
    this project exists to prevent.

    **WHY NOT `is_recorded_number`.** That decision (R1033) admits dtype kinds `i` and `u`,
    and it is right to: a recorded PERIOD or Froude SCALE may arrive as an integer, and
    `50` is as good a scale as `50.0`. A physical multiplier may not. An integer `lam` is a
    TRUNCATED `lam`, and the int64 arm above is what truncation looks like from outside --
    a different governing CLAUSE at a utilisation nobody chose. So reusing the scalar
    decision here would have left the int64 arm exactly as it was.

    **WHICH FLOATING WIDTH, which is R1059 and is answered here rather than left open.**
    Kind `f` was the wrong AXIS for the reason the paragraph above gives: the
    justification is about PRECISION and `np.dtype("float16").kind` is `f` with eleven
    significand bits. Measured through the real CLI, one variable moved: **a float16 `lam`
    gave EXIT 0 and `U = 1.71177` against the control's `1.71167`, with 9535 of 16224
    cells of `member_forces.csv` changed** -- torsion at one station `1.5e-07` becoming
    `0.032`, `Vy` at another `-0.0032 N` becoming `-11.93 N`. So the gate is **float64
    exactly**, and the reason is not tidiness either:

        the schema declares no WIDTH, so this module declares one and names it here;
        `scripts/export_f4_dynamic_inputs.py` writes `np.float64`, and it is the only
        `np.savez` in `floatfea/` or `scripts/` -- so no TRACKED dynamic-inputs file has
        any other producer, and a narrower one did not come from the exporter the refusal
        points at. (`grep -rnF "np.savez" --include=*.py floatfea
        scripts` -- `-F`, a FIXED string, so the
        docstring carries no escape sequence of its own -- gives exactly TWO hits: the
        exporter's call, and the line
        above. Needling `savez(` instead would miss the exporter, whose call is the
        compressed variant; so the self-reference is disclosed rather than engineered
        around, and a reader matching the output against this paragraph sees both. The
        claim is deliberately about the library and the scripts and NOT about the
        repository: `tests/` writes this field too, at other dtypes and other values,
        because the counter-cases below are exactly that.)
        and `np.asarray(..., dtype=np.float64)` downstream WIDENS a lossy array back,
        so nothing after this point can tell a float16 file from a float64 one.

    A float32 file is therefore refused with a message that says to re-export rather than
    being computed from quietly. If a future exporter has reason to write a narrower
    width, that is a schema change in `docs/load-interchange-v1.md` and a change here, not
    a silent widening at the read.

    **THE VALUES, which is R1058 and is the half no dtype can decide.** `np.nan` is a
    float64, so it passed the dtype gate above on the commit that added it. Driven through
    the real CLI by the reviewer, one variable moved -- `case1/lam`, the GOVERNING case at
    `T_full = 12.5 s`, filled with `np.nan`:

        finite (CONTROL)   EXIT 0   U = 1.71167  hub4_arm ROOT  T = 12.5 s  3.3.2
        case1/lam = NaN    EXIT 0   U = 1.35117  hub4_arm ROOT  T = 14 s    3.3.2
        one entry = NaN    EXIT 0   U = 1.71167 unchanged, 216 of 1248 rows nan
        one entry = inf    EXIT 0   U = 1.71167 unchanged, 216 of 1248 rows nan

    **`U = 1.35117` where the truth is `1.71167` -- 21% low, in the direction that reads
    safer than it is**, with the governing period absent from `utilisation.csv` and not one
    `nan` in its 32 rows. The mechanism is that a NaN loses every comparison in the
    per-member-station peak selection below, so the polluted case is silently DROPPED from
    the envelope instead of reddening it, and the published governing utilisation becomes
    the best of the cases that remain. The existing guard is a COUNT (`len(peak) !=
    len(static)`, below): it catches EVERY case being NaN, because then no station has a
    peak at all, and it cannot see one of four cases contributing nothing, because the
    other three still supply a peak for all 48 stations. The collection the assertion
    inspects cannot contain the failure.

    **This repository had already ruled on it twice, in two sibling files, and the one read
    that publishes did not share the ruling:** `floatfea/io/reader.py` carries
    `NON_FINITE = "NaN or inf in a channel"`, and `scripts/export_f4_dynamic_inputs.py`
    refuses it for every array by name with "a non-finite value cannot be compared, so
    this is a failure rather than a difference of zero". The fault's words below are the
    reader's, not new ones.

    **THE WINDOW LENGTH, which is R1063 and is what the three-item list left open.**
    `compute_rows` uses `lam.shape[0]` as the window length and compares it with nothing.
    So a case with ZERO rows contributes no per-instant row at all and is silently DROPPED
    from the envelope rather than reddening it. Driven by the reviewer through the real CLI
    on the shipped file, one variable -- `case1/lam`, the GOVERNING case at
    `T_full = 12.5 s`, replaced by `lam[:0]` with the same dtype and column count:

        finite (CONTROL)     EXIT 0   U = 1.71167  hub4_arm ROOT  T = 12.5 s  3.3.2
        case1/lam -> (0,64)  EXIT 0   U = 1.35117  hub4_arm ROOT  T = 14   s  3.3.2
                             member_forces.csv : 1248 rows -> 1056 rows
                             utilisation.csv   : 32 rows, ZERO carry nan, 12.5 s absent

    **That is the same published number the NaN route produced, to the digit, and it is
    STRICTLY MORE SILENT.** The NaN route left 192 of 1248 `member_forces.csv` rows
    carrying `nan`, so the degradation was visible in one of the three artifacts; this one
    REMOVES those same 192 rows and leaves no `nan` anywhere, with `report.md` differing
    from the control in exactly one substantive line while still declaring
    `governing_periods_s [12.5, 14.0, 15.0, 16.2]` -- it says 12.5 s was screened when it
    was not. And truncation is monotone with no threshold anywhere: on a 40-step fixture,
    `k = 20` gives `1.71167`, `k = 5` `1.65695`, `k = 2` `1.62136`, `k = 1` `1.60798` and
    `k = 0` `1.35109`, every one at exit 0.

    The existing guard cannot see it, for the same reason it could not see the NaN route:
    `len(peak) != len(static)` below is a COUNT, so it fires only when NO station has a
    peak. With three of four governing cases still supplying a peak for all 48 stations,
    the collection the assertion inspects cannot contain the failure.

    **WHICH RECORD `N` IS CHECKED AGAINST, and why it is not the closed form.** The file
    declares `N` several times over: `times`, `accel`, `base`, `contrib` and
    `resid_control` all carry it per case, and `5 * (T_full / sqrt(lambda)) / dt` from the
    provenance sidecar's own `window`, `dt` and `lambda` reproduces it too. **The closed
    form reproduces it only to within one step** -- `707.1` against `707`, `883.9` against
    `884`, `1060.7` against `1061` -- so comparing against it needs a number chosen to make
    two quantities agree, which `CLAUDE.md` forbids by name. `case{index}/times` is exact,
    needs no arithmetic, and makes this the same kind of check as R1005: the file agreeing
    with ITSELF about which case is which, here about how long its window is.
    `m_xddot` is deliberately NOT in the comparison -- it is `N + 1` by design (708 against
    `times` 707 on case 0), so an all-arrays-agree check would be wrong.
    """
    key = f"case{index}/lam"
    window_key = f"case{index}/times"
    try:
        lam = raw[key]
    except KeyError:
        raise SystemExit(
            f"{key} is absent, and `docs/load-interchange-v1.md` declares one "
            f"`lam[N,n_rows]` per case. A case the envelope expects and the file does not "
            f"carry would drop out of it silently, which is R1063's defect reached by a "
            f"missing key instead of an empty one. Re-export the file with "
            f"`python scripts/export_f4_dynamic_inputs.py`."
        ) from None
    where = key
    dtype = getattr(lam, "dtype", None)
    # **`dtype is None` IS TESTED SEPARATELY AND IT IS NOT DEFENSIVE TIDINESS.**
    # `np.dtype(None)` is `float64`, so `None != np.dtype(np.float64)` is **False**: an
    # object with no `dtype` at all -- a python list, a float, a dict -- passes a bare
    # equality test. The kind test this replaced read
    # `getattr(getattr(lam, "dtype", None), "kind", None) != "f"` and refused those, so
    # narrowing the width to float64 REGRESSED them from refused to admitted, and the
    # adversarial probe over every dtype class and value shape is what found it rather
    # than anything in the diff. Measured: `[[1.0, 2.0]]` and `1.0` admitted, `None`
    # reaching `np.isfinite` and raising an uncaught `TypeError`.
    if dtype is None or dtype != np.dtype(np.float64):
        # `str(dtype)` and not `dtype.name`: the latter spells `<U8` as `str256`, which
        # is the bit width and not a spelling a reader would recognise from the file they
        # exported. `bool`, `<U8`, `int64` and `float16` all come back as themselves.
        spelling = (
            f"{type(lam).__name__} of dtype {dtype}" if dtype is not None else type(lam).__name__
        )
        raise SystemExit(
            f"{where}: the joint-reaction multipliers are {spelling}, and "
            f"`docs/load-interchange-v1.md` declares `lam[N,n_rows]  multipliers, dt-free, "
            f"physical` -- which this module reads at float64, the width "
            f"`scripts/export_f4_dynamic_inputs.py` writes. This is not refused for "
            f"tidiness: `np.asarray(..., dtype=np.float64)` converts a bool array to "
            f"1.0/0.0, a text array by re-parsing truncated digits, an integer array as "
            f"truncated multipliers, and WIDENS a float16 array back so that nothing "
            f"downstream can tell -- and each of those publishes a governing utilisation "
            f"at exit 0. A bool-typed `lam` publishes `U = 0.995379` -- PASSING -- where "
            f"the same file at float64 gives `1.71167` (R1051); a float16 one publishes "
            f"`1.71177` with 9535 of 16224 member-force cells moved (R1059). Re-export the "
            f"file with `python scripts/export_f4_dynamic_inputs.py`."
        )
    # **R1063, BEFORE the value check and not after.** An emptied `lam` has no non-finite
    # value in it at all, so the finiteness gate passes it; the window length is what is
    # wrong with it and the message has to say so.
    if getattr(lam, "ndim", None) != 2:
        raise SystemExit(
            f"{where}: the joint-reaction multipliers have {getattr(lam, 'ndim', None)} "
            f"dimensions, and `docs/load-interchange-v1.md` declares `lam[N,n_rows]` -- a "
            f"2-D array of N timesteps by n_rows joint-block components. A 0-d or 1-D "
            f"array reaches `lam.shape[0]` below and dies in an index error rather than "
            f"being refused here (R1063). Re-export the file with "
            f"`python scripts/export_f4_dynamic_inputs.py`."
        )
    try:
        times = raw[window_key]
    except KeyError:
        raise SystemExit(
            f"{where}: the file carries no `{window_key}`, so there is nothing to check "
            f"the window length of {lam.shape[0]} timesteps against. Every case this "
            f"repository exports carries `times` beside `lam` with the same first-axis "
            f"length; without it a truncated or emptied `lam` is indistinguishable from a "
            f"complete one, and a case that silently contributes no row DROPS OUT of the "
            f"envelope instead of reddening it (R1063). Re-export the file with "
            f"`python scripts/export_f4_dynamic_inputs.py`."
        ) from None
    if getattr(times, "ndim", None) != 1:
        raise SystemExit(
            f"{where}: `{window_key}` has {getattr(times, 'ndim', None)} dimensions where "
            f"the window record is a 1-D array of instants, so it cannot say how long this "
            f"case's window is (R1063)."
        )
    if lam.shape[0] != times.shape[0]:
        raise SystemExit(
            f"{where}: {lam.shape[0]} timesteps, and the file's own window record "
            f"`{window_key}` carries {times.shape[0]}. The two disagree about how long "
            f"this case is. This is refused rather than carried because a short or empty "
            f"`lam` does not redden the result, it LOWERS it: `compute_rows` reads "
            f"`lam.shape[0]` as the window length, so a case with too few instants "
            f"contributes too few per-instant rows -- or, at zero, none at all -- and "
            f"drops out of the governing envelope while every artifact goes on declaring "
            f"it was screened. Measured, with the governing case alone emptied: "
            f"`U = 1.35117` published at exit 0 where the whole file gives `1.71167`, 21% "
            f"low, with the governing period absent from `utilisation.csv` and 192 of 1248 "
            f"rows gone from `member_forces.csv` -- and not one `nan` anywhere to show it "
            f"(R1063). The usual cause is a truncated or partially-written export; "
            f"re-export with `python scripts/export_f4_dynamic_inputs.py`, whose own window "
            f"guard refuses a run shorter than two steps."
        )
    offending = int(np.count_nonzero(~np.isfinite(lam)))
    if offending:
        raise SystemExit(
            f"{where}: NaN or inf in a channel -- {offending} of {lam.size} joint-reaction "
            f"multipliers are not finite, and `docs/load-interchange-v1.md` declares "
            f"`lam[N,n_rows]  multipliers, dt-free, physical`. A non-finite value cannot "
            f"be compared, so this is a failure rather than a difference of zero -- which "
            f"is `floatfea/io/reader.py`'s own NON_FINITE wording and "
            f"`scripts/export_f4_dynamic_inputs.py`'s, both of which refuse it already. "
            f"It is refused rather than carried because it does not redden the result, it "
            f"LOWERS it: a NaN loses every comparison in the per-member-station peak "
            f"selection, so this case drops out of the envelope and the published "
            f"governing utilisation becomes the best of the cases that remain. Measured, "
            f"with the governing case alone polluted: `U = 1.35117` published at exit 0 "
            f"where the finite file gives `1.71167`, 21% low, with the governing period "
            f"absent from `utilisation.csv` and not one `nan` in it (R1058). The usual "
            f"cause is a FloatSim solve that diverged; re-run the export and check that "
            f"its own non-finite refusal fired."
        )
    return lam


def _lam_full_scale(lam_row: NDArray[np.float64], froude_lambda: float) -> NDArray[np.float64]:
    """One timestep's multipliers, model scale to FULL scale, per joint block.

    **`froude_lambda` IS A PARAMETER AND THERE IS NO MODULE CONSTANT (R805, FN0).** This
    read `FROUDE_LAMBDA = 50.0` from module scope while `build_superstructure` took its
    scale from the caller. A configuration declaring `floatsim.froude_lambda: 25.0`
    therefore built the deck at scale 25 -- platform `deck_mass` 312500 against 2500000,
    arms 25 m against 50 m -- and scaled the joint reactions by 50 anyway. The composite
    goes as `lam^3` on force and `lam^4` on the locked moment, so that is **8x on force
    and 16x on the moment**, with `provenance()` printing `25.0` as though it had been
    used.

    Nothing was red. The declared range is `[1, 1000]` and the example sits on the one
    point in three decades where the constant and the configuration agree, so the golden
    test could not see it either. **That is the shape this project exists to prevent: a
    plausible wrong answer, not a crash.**

    So the scale is passed in, every caller states it, and there is no default -- a
    default would be the same constant wearing a different hat.

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
            block, "joint_multiplier_yaw_locked", froude_lambda
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
    froude_lambda: float,
    progress: Any = None,
) -> ComputedForces:
    """Every basis, over every case and step. Moved verbatim from the script's `main`.

    `governing_periods` is a PARAMETER rather than a module constant, because that is
    the whole of what a configuration changes about this loop (FL1(a)'s `load_cases`,
    FL2(d)'s per-case band check). The script passes its own `GOVERNING_PERIODS` and so
    is unchanged; a config passes the admitted set it declares.

    `progress` is called with one line per case when given, so the script keeps printing
    what it printed and the library stays silent by default.

    `froude_lambda` is required for the same reason `governing_periods` is: it is a
    property of the RUN and not of this module. R805 is what a module constant here cost.
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
        # R1051: the one bulk numeric array the solve consumes, and the only npz key read
        # inside `floatfea/` that had no dtype gate.
        lam = checked_joint_reactions(raw, i)
        # The worst of each component over the window, per member-station, keeping the
        # max and the min separately -- `CLAUDE.md` forbids averaging a per-case
        # diagnostic, and a signed envelope needs both ends.
        worst_hi: dict[tuple[str, str, str], NDArray[np.float64]] = {}
        worst_lo: dict[tuple[str, str, str], NDArray[np.float64]] = {}
        for step in range(lam.shape[0]):
            loads = map_joint_reactions(
                _lam_full_scale(lam[step], froude_lambda), joint_order, nodes, n_dof_of
            )
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
