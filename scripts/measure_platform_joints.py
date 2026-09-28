"""DQ2 / DJ0: measure every platform joint against the two-rotation gimbal claim.

WHAT THIS ANSWERS. `docs/milestones/F3.md` § 1 records DJ0's second half -- "all 16
joints are two-rotation gimbals" -- as **a claim to VERIFY, not a fact to assume**,
and defers the verification to F5-prep. This script is that verification, run early
because F3's joint work consumes its result: if a joint were not a gimbal, F3's
builder must refuse the model rather than idealise it.

WHAT A TWO-ROTATION GIMBAL IS, in the form the FE model needs (DJ0, verbatim): "a
release of the two free moments with the locked-axis moment transmitted". So the
measurement is not a property of the joint's NAME. It is a property of the
constraint's REACTION: for an arbitrary multiplier vector, the moment delivered to
body A *at the joint point* must lie along the locked axis, and the two
perpendicular components must be absent.

THE CELL THAT DISTINGUISHES THE TWO RANKS, AND IT IS WHY THIS FILE EXISTS.
A first measurement of this took the rank of ALL FOUR constraint rows in body A's
rotational columns and read rank 3 on the twelve buoy-hub joints -- which would say
they are not gimbals. That rank is real and it is not the joint's moment:

    rows 0:3   the TRANSLATIONAL lock. Its entries in the rotational columns are
               `-skew(arm_a)`, the moment of the constraint FORCE about body A's
               REFERENCE POINT. Rank 3 whenever the attach offset is non-zero.
    row  3     the ROTATIONAL lock. One row, `axis_world`, and the only row that
               carries a joint moment.

The variable that separates them is the attach offset, and the platform holds it at
two values with nothing else changed: the four hub-platform joints have
`|attach_a| = 0` and read rank 1 over all four rows; the twelve buoy-hub joints
have `|attach_a| = 1.689 m` and read rank 3 over all four rows and rank 1 over row
3 alone. Same joint kind, same axis, same code path -- one variable.

Shifting the moment to the joint point (`M_ref - arm x F`) removes the offset term
and is the measurement that means what DJ0 says.

RUN IT:  python scripts/measure_platform_joints.py
It imports the pinned HSP worktree read-only and writes nothing.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.spatial.transform import Rotation

HSP_RUNS = Path(__file__).resolve().parents[2] / "HSP-runs"
STUDY = HSP_RUNS / "studies" / "platform-12buoy"
SEED = 20260928
"""not-a-tolerance: the seed of the probe state. Nothing is compared against it;
it fixes WHICH arbitrary configuration and multiplier vector are used, so the
figures below are reproducible rather than re-rolled on every run."""


def _load_deck():
    """Import the pinned platform study and build its deck. Read-only."""
    for path in (HSP_RUNS, STUDY, STUDY.parent / "cluster-3buoy-rigid"):
        sys.path.insert(0, str(path))
    import platform_rao_pilot as prp

    return prp._deck_with_drag()


def measure() -> tuple[list[dict[str, object]], dict[str, float]]:
    """Return one row per joint and the worst figures across all of them."""
    from floatsim.bodies.joints import Joint, JointSet

    deck = _load_deck()
    names = [b.name for b in deck.bodies]
    index = {n: i for i, n in enumerate(names)}
    joints = [
        Joint(
            kind=d["type"],
            body_a=index[d["body_a"]],
            body_b=index[d["body_b"]],
            attach_a=np.asarray(d["attach_a_body"], float),
            attach_b=np.asarray(d["attach_b_body"], float),
            axis=np.asarray(d["axis"], float),
        )
        for d in (j.model_dump() for j in deck.joints)
    ]
    js = JointSet(joints=tuple(joints), n_bodies=len(names))

    # Every body at a DIFFERENT finite rotation, so no joint is evaluated at the
    # identity where a body-fixed axis and the world axis coincide by accident.
    rng = np.random.default_rng(SEED)
    xi = np.zeros(js.n_dof)
    for k in range(len(names)):
        xi[6 * k : 6 * k + 3] = rng.standard_normal(3) * 0.5
        xi[6 * k + 3 : 6 * k + 6] = rng.standard_normal(3) * 0.15
    G = js.jacobian(xi)
    multipliers = rng.standard_normal(js.n_constraints) * 1e3

    rows: list[dict[str, object]] = []
    worst = {"leak": 0.0, "axis_drift": 0.0, "reaction_asymmetry": 0.0}
    cursor = 0
    for joint in joints:
        m = joint.n_rows
        block = G[cursor : cursor + m, :]
        a0, b0 = 6 * joint.body_a, 6 * joint.body_b
        rot = Rotation.from_rotvec(xi[a0 + 3 : a0 + 6])
        arm = rot.apply(joint.attach_a)
        axis = rot.apply(joint.axis / np.linalg.norm(joint.axis))

        # THE CELL: the same three columns, read over all four rows and over the
        # rotational lock row alone.
        rank_all_rows = int(np.linalg.matrix_rank(block[:, a0 + 3 : a0 + 6], tol=1e-10))
        rank_lock_row = int(np.linalg.matrix_rank(block[m - 1 :, a0 + 3 : a0 + 6], tol=1e-10))

        reaction = block.T @ multipliers[cursor : cursor + m]
        force = reaction[a0 : a0 + 3]
        moment_at_joint = reaction[a0 + 3 : a0 + 6] - np.cross(arm, force)
        released = moment_at_joint - (moment_at_joint @ axis) * axis
        leak = float(np.linalg.norm(released)) / max(float(np.linalg.norm(moment_at_joint)), 1e-300)

        drift = float(np.max(np.abs(block[m - 1, a0 + 3 : a0 + 6] - axis)))
        asymmetry = float(
            np.max(np.abs(block[m - 1, a0 + 3 : a0 + 6] + block[m - 1, b0 + 3 : b0 + 6]))
        )

        rows.append(
            {
                "a": names[joint.body_a],
                "b": names[joint.body_b],
                "kind": joint.kind,
                "n_rows": m,
                "translations_locked": int(
                    np.linalg.matrix_rank(block[0:3, a0 : a0 + 3], tol=1e-10)
                ),
                "moments_locked": rank_lock_row,
                "moments_released": 3 - rank_lock_row,
                "rank_over_all_rows": rank_all_rows,
                "attach_offset_m": float(np.linalg.norm(joint.attach_a)),
                "released_moment_leak": leak,
            }
        )
        worst["leak"] = max(worst["leak"], leak)
        worst["axis_drift"] = max(worst["axis_drift"], drift)
        worst["reaction_asymmetry"] = max(worst["reaction_asymmetry"], asymmetry)
        cursor += m

    # At the reference configuration every locked axis must be world z exactly.
    G0 = js.jacobian(np.zeros(js.n_dof))
    cursor = 0
    worst["reference_axis_error"] = 0.0
    for joint in joints:
        a0 = 6 * joint.body_a
        row = G0[cursor + joint.n_rows - 1, a0 + 3 : a0 + 6]
        worst["reference_axis_error"] = max(
            worst["reference_axis_error"],
            float(np.max(np.abs(row - np.array([0.0, 0.0, 1.0])))),
        )
        cursor += joint.n_rows
    return rows, worst


def main() -> int:
    rows, worst = measure()
    header = (
        f"{'#':>3} {'body A':<9} {'body B':<9} {'kind':<11} {'rows':>4} "
        f"{'T':>2} {'M lock':>6} {'M free':>6} {'|attach|':>9} {'rank(4 rows)':>12} "
        f"{'leak':>10}"
    )
    print(header)
    print("-" * len(header))
    for i, r in enumerate(rows, 1):
        print(
            f"{i:>3} {r['a']:<9} {r['b']:<9} {r['kind']:<11} {r['n_rows']:>4} "
            f"{r['translations_locked']:>2} {r['moments_locked']:>6} "
            f"{r['moments_released']:>6} {r['attach_offset_m']:>9.4f} "
            f"{r['rank_over_all_rows']:>12} {r['released_moment_leak']:>10.2e}"
        )

    gimbals = [
        r
        for r in rows
        if r["translations_locked"] == 3 and r["moments_locked"] == 1 and r["moments_released"] == 2
    ]
    print()
    print(f"two-rotation gimbals: {len(gimbals)} of {len(rows)}")
    print(f"worst released-moment leak at the joint point : {worst['leak']:.3e}")
    print(f"worst locked axis vs R_A z                    : {worst['axis_drift']:.3e}")
    print(f"worst A/B reaction asymmetry                  : {worst['reaction_asymmetry']:.3e}")
    print(f"worst locked axis vs world z at xi = 0        : {worst['reference_axis_error']:.3e}")
    print()
    print("THE CELL -- the same three columns, two row sets, one variable:")
    offsets = sorted({round(r["attach_offset_m"], 4) for r in rows})
    for offset in offsets:
        at = [r for r in rows if round(r["attach_offset_m"], 4) == offset]
        print(
            f"  |attach_a| = {offset:.4f} m  ({len(at):>2} joints)"
            f"   rank over all 4 rows = {at[0]['rank_over_all_rows']}"
            f"   rank over the lock row = {at[0]['moments_locked']}"
        )
    print(
        "  The rank over all four rows moves with the offset and the rank over the\n"
        "  lock row does not, which is what identifies the first as the moment of the\n"
        "  constraint FORCE about the reference point rather than a joint moment."
    )
    return 0 if len(gimbals) == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
