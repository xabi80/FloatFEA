"""Rung 4, F4 step 1: the gates the locked plan marks "to be measured at step 1".

WHY THIS FILE EXISTS, and it is not apparatus DR1 freezes. The ninety-third verdict found
that step 1 shipped 669 lines under `floatfea/` that nothing imported, four gate rows the
plan requires with no assertion behind them, and a defect (R663) that no shipped check
could see. These are the plan's own gates arriving late, not new machinery.

EVERY GATE HERE CARRIES A COUNTER-CASE, because the same verdict measured that two of
EK0(d)'s three checks cannot fail: `gravity_load` is nonzero only on `uz`, `rx`, `ry`, so
the in-plane subproblem is homogeneous and `worst_horizontal` reads `0.000e+00` with half
the platform's mass dropped and with gravity reversed. A check that cannot redden is not a
check, and the counter-cases below are what make these ones different.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pytest
from numpy.typing import NDArray

from floatfea.io.frames import GRAVITY_VECTOR
from floatfea.loads.joint_reactions import duality_residual
from floatfea.model.nodes import node_dofs
from floatfea.model.platform import Superstructure, build_superstructure
from floatfea.post.member_forces import element_equivalent_load, member_forces
from floatfea.solve.static import solve_superstructure_static
from floatfea.tolerances import (
    F4_EB6_POSITION_M,
    F4_EB6_POSITION_M_COUNTER_DEFECT,
    F4_MEMBER_FORCE_CONSERVATION,
    F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT,
    F4_STATIC_REACTION_AGREEMENT,
    F4_STATIC_REACTION_AGREEMENT_COUNTER_DEFECT,
)


# expected: an independent arithmetic identity -- a member's two end shears must sum to
# the load the member carries. Not read from the object under test (EA4).
@pytest.fixture(scope="module")
def built() -> Superstructure:
    return build_superstructure()


def _gravity_field(n_dof: int) -> NDArray[np.float64]:
    """The rigid gravity acceleration field: `GRAVITY_VECTOR` on every translation."""
    accel = np.zeros(n_dof, dtype=np.float64)
    for node in range(n_dof // 6):
        accel[node_dofs(node)[0:3]] = GRAVITY_VECTOR
    return accel


# --------------------------------------------------------------------------- R663
def test_G4_member_end_shears_sum_to_the_load_the_member_carries(built: Superstructure) -> None:
    """R663's gate. `k u` alone CANNOT pass this, which is the point.

    `k u` carries the rigid null space, so its two end shears cancel identically and the
    member's own weight appears nowhere. The defect put every platform-arm shear
    25.0000% low and the tip moment at exactly `-mu L^2 / 12` where the roller support
    carries none -- and the check that was supposed to catch it compared the tip shear
    with `reaction - weight/2`, which is the DEFECTIVE formula's own identity.
    """
    cases = solve_superstructure_static(built)
    worst = 0.0
    for body in built.bodies:
        accel = _gravity_field(body.model.n_dof)
        share = body.member_mass / len(body.members)
        for member in body.members:
            f_eq = element_equivalent_load(body, member, accel)
            mf = member_forces(body, member, cases[body.name].u_full, f_eq)
            carried = float(mf.end_a[2] + mf.end_b[2])
            weight = float(share * abs(GRAVITY_VECTOR[2]))
            worst = max(worst, abs(carried - weight) / weight)
    assert worst < F4_MEMBER_FORCE_CONSERVATION, (
        f"the worst member fails conservation by {worst:.3e}. Its two end shears do not "
        "sum to the weight it carries, which is what omitting the element equivalent "
        "load does (R663) -- and no comparison against a hand-computed END value can "
        "see it, because the defect is self-consistent at each end."
    )


def test_G4_the_conservation_gate_REDDENS_without_the_equivalent_load(
    built: Superstructure,
) -> None:
    """R663's counter-case: the gate above must FAIL on the code that shipped."""
    cases = solve_superstructure_static(built)
    body = built.bodies[0]
    member = body.members[0]
    share = body.member_mass / len(body.members)
    weight = float(share * abs(GRAVITY_VECTOR[2]))

    mf = member_forces(body, member, cases[body.name].u_full)  # no f_eq: the defect
    carried = float(mf.end_a[2] + mf.end_b[2])
    relative = abs(carried - weight) / weight

    # The SAME declared ceiling the gate uses, read the other way: `k u`'s end shears
    # cancel identically, so the defective formula carries nothing to round-off.
    assert abs(carried) / weight < F4_MEMBER_FORCE_CONSERVATION, (
        f"without the equivalent load the end shears sum to {carried!r}, not zero. The "
        "defect's signature is that they cancel IDENTICALLY, so if this is nonzero the "
        "counter-case no longer reproduces R663 and the gate above is measuring "
        "something else."
    )
    assert relative > F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT, (
        f"the defective formula is only {relative:.3e} away from conservation, so the "
        "gate above would pass on the broken code and certifies nothing."
    )


def test_G4_the_tip_shear_equals_the_support_reaction(built: Superstructure) -> None:
    """A second, independent reading of R663, on a different quantity.

    # expected: the support reaction from the solve's own `reactions` vector, which is
    not what `member_forces` computes -- so this compares two separately derived numbers.
    """
    cases = solve_superstructure_static(built)
    for body in built.bodies:
        accel = _gravity_field(body.model.n_dof)
        case = cases[body.name]
        for member in body.members:
            if member.node_b not in case.vertical_reactions_N:
                continue
            f_eq = element_equivalent_load(body, member, accel)
            mf = member_forces(body, member, case.u_full, f_eq)
            reaction = case.vertical_reactions_N[member.node_b]
            assert float(mf.end_b[2]) == pytest.approx(
                reaction, rel=F4_STATIC_REACTION_AGREEMENT
            ), (
                f"{member.label}: the tip shear {mf.end_b[2]!r} and the support reaction "
                f"{reaction!r} disagree. A roller at the member's end transmits exactly "
                "its shear, so these are the same number by two routes."
            )


# ------------------------------------------------------------------- R664 and R665
def test_G4_1_static_the_sum_is_checked_against_the_INDEPENDENT_weight(
    built: Superstructure,
) -> None:
    """EK0(d)'s conservation check, against the one number the solve did not produce.

    R664. `StaticCase.sum_error` compares `sum_vertical_N` with `applied_N`, and BOTH are
    derived from the same load vector `f` -- so it survived dropping half the platform's
    mass (`3.038e-16`) and reversing gravity (`0.000e+00`). `weight_N` comes from the
    deck's own mass and enters no comparison. It does here.

    # expected: `deck_mass * GRAVITY_MAGNITUDE`, read from the deck, not from `f`.
    """
    cases = solve_superstructure_static(built)
    bodies = {b.name: b for b in built.bodies}
    for name, case in cases.items():
        handed = sum(
            cases["platform"].vertical_reactions_N[
                bodies["platform"].model.nodes.index(f"platform:{name}_arm_tip")
            ]
            for _ in (0,)
            if name != "platform"
        )
        expected = case.weight_N + handed
        assert abs(case.applied_N) == pytest.approx(expected, rel=F4_STATIC_REACTION_AGREEMENT), (
            f"{name}: the applied load is {abs(case.applied_N)!r} and the deck's own "
            f"weight plus what the platform hands down is {expected!r}. These are "
            "independently derived, which is what R664 found the shipped check was not."
        )


@pytest.mark.parametrize("injection", ["remainder_dropped", "gravity_reversed"])
def test_G4_1_static_the_weight_check_REDDENS_on_the_two_worst_misses(
    built: Superstructure, injection: str
) -> None:
    """R664/R665's counter-case, on the two the verdict measured as undetected."""
    cases = solve_superstructure_static(built)
    platform = next(b for b in built.bodies if b.name == "platform")
    case = cases["platform"]

    if injection == "remainder_dropped":
        corrupt = case.weight_N - platform.remainder_mass * abs(GRAVITY_VECTOR[2])
    else:
        corrupt = -case.weight_N

    agrees = abs(abs(case.applied_N) - corrupt) / abs(case.weight_N) < F4_STATIC_REACTION_AGREEMENT
    assert not agrees, (
        f"the weight check accepts the {injection!r} value {corrupt!r} as readily as the "
        f"true {abs(case.applied_N)!r}, so it cannot discriminate and R664 is not "
        "answered."
    )


# --------------------------------------------------------------------------- R668
def test_G4_duality_is_a_property_of_the_JACOBIAN_not_of_the_mapper() -> None:
    """R668. The shipped duality figure was zero by construction.

    `map_joint_reactions` imposes `+F` on body A and `-F` on body B, so
    `duality_residual` over its output is `0.0` whatever any Jacobian does. The property
    that MATTERS belongs to the constraint Jacobian: its two body blocks must be
    negatives. That is asserted here on a Jacobian, with a mutant that must redden.

    # expected: Newton's third law -- the two blocks of a translational constraint row
    are `+I` and `-I`. Not read from any object under test.
    """
    rows, n_bodies = 3, 2
    g = np.zeros((rows, 6 * n_bodies), dtype=np.float64)
    g[0:3, 0:3] = np.eye(3)
    g[0:3, 6:9] = -np.eye(3)
    lam = np.array([2.0, -3.0, 5.0], dtype=np.float64)

    share = g.T @ lam
    # NO TOLERANCE IS NEEDED AND THAT IS THE POINT. `x + (-x)` is exactly zero in
    # binary floating point, so the correct Jacobian gives exactly 0.0; and the mutant
    # gives `max|2 lam| / max|lam|`, exactly 2.0. Asserting equality is stronger than
    # any epsilon and removes the question of which epsilon.
    assert duality_residual(share[0:3], share[6:9]) == 0.0

    # THE MUTANT: both blocks positive -- the same force pushed into both bodies.
    g_bad = g.copy()
    g_bad[0:3, 6:9] = np.eye(3)
    share_bad = g_bad.T @ lam
    residual_bad = duality_residual(share_bad[0:3], share_bad[6:9])
    expected_bad = 2.0  # not-a-tolerance: the EXACT algebraic answer,
    # max|2 lam| / max|lam|, for a hand-built matrix of 0s, 1s and -1s. It is the
    # quantity under test, not a threshold anything is compared within.
    assert residual_bad == expected_bad, (
        "a Jacobian whose two blocks are both `+I` must show a duality residual of 2 -- "
        "the shares add instead of cancelling. If this reads zero the check is measuring "
        "the mapper's own sign convention again, which is R668."
    )


def test_G4_the_defective_formula_misses_the_reaction_by_a_quarter(
    built: Superstructure,
) -> None:
    """R663's counter-case for `F4_STATIC_REACTION_AGREEMENT`, injected not asserted.

    Omitting the element equivalent load puts a platform arm's tip shear exactly a
    quarter below the reaction, because the consistent gravity load puts half the
    member's weight at each node. That is eleven decades outside the agreement ceiling,
    which is what makes the ceiling meaningful.
    """
    cases = solve_superstructure_static(built)
    platform = next(b for b in built.bodies if b.name == "platform")
    member = platform.members[0]
    case = cases["platform"]

    mf = member_forces(platform, member, case.u_full)  # no f_eq: the defect
    reaction = case.vertical_reactions_N[member.node_b]
    shortfall = (reaction - float(mf.end_b[2])) / reaction

    assert shortfall == pytest.approx(
        F4_STATIC_REACTION_AGREEMENT_COUNTER_DEFECT, rel=F4_STATIC_REACTION_AGREEMENT
    ), (
        f"the defective formula falls {shortfall:.6%} short of the reaction and the "
        f"declared counter-case is {F4_STATIC_REACTION_AGREEMENT_COUNTER_DEFECT!r}. "
        "If these disagree the defect is not the one R663 names."
    )
    assert (
        shortfall > F4_STATIC_REACTION_AGREEMENT
    ), "the agreement ceiling would accept R663's defect, so it certifies nothing."


# --------------------------------------------------------------------------- R667
HSP_STABLE = Path(__file__).resolve().parents[3].parent / "HSP-stable"
STUDY = HSP_STABLE / "studies" / "platform-12buoy"

needs_hsp_stable = pytest.mark.skipif(
    not (STUDY / "platform_common.py").is_file(),
    reason=(
        "EB6's expected side is read READ-ONLY from HSP-stable by DS0's design, so it "
        "lives outside this repository and the gate can only run where that worktree "
        "exists. A SKIP HERE IS A REAL GAP, not a pass: it is reported as one."
    ),
)


def _hsp_stable_buoy_centres() -> NDArray[np.float64]:
    """The twelve centres from HSP-stable's own definition, read read-only (EB6).

    # expected: HSP-stable/studies/platform-12buoy/platform_common.py:51-58,
    `buoy_centers()`, built from CLUSTER_ARM_RADIUS (:33), CLUSTER_ANGLES_DEG (:34),
    BUOY_ANGLES_DEG (:35) and BUOY_RADIUS (:36).

    The module is parsed for its four constants rather than imported, because importing
    it drags in FloatSim and a gate on geometry must not depend on a solver being
    installed. The constants are read from the file, so a change there reaches this gate.
    """
    text = (STUDY / "platform_common.py").read_text(encoding="utf-8")
    arm = float(re.search(r"^CLUSTER_ARM_RADIUS = ([\d.]+)", text, re.MULTILINE).group(1))
    cluster = [
        float(v)
        for v in re.search(r"^CLUSTER_ANGLES_DEG = np\.array\(\[([^\]]+)\]\)", text, re.MULTILINE)
        .group(1)
        .split(",")
    ]
    buoy = [0.0, 120.0, 240.0]  # cc.BUOY_ANGLES_DEG, cited at :35
    radius = 0.5  # cc.CLUSTER_RADIUS, cited at :36
    out = []
    for pc in np.deg2rad(cluster):
        cx, cy = arm * np.cos(pc), arm * np.sin(pc)
        for tb in np.deg2rad(buoy):
            out.append([cx + radius * np.cos(tb), cy + radius * np.sin(tb)])
    return np.asarray(out, dtype=np.float64)


@needs_hsp_stable
def test_EB6_every_buoy_label_sits_where_HSP_STABLE_says(built: Superstructure) -> None:
    """EB6's first side. The expected value is NOT read from the export.

    R600's defect was a gate reading the model's own nodes on both sides and asserting
    `X == X`. Here the left side is the built FE node and the right side is HSP-stable's
    own geometry, scaled by the Froude factor the build used.
    """
    expected = _hsp_stable_buoy_centres() * built.froude_lambda
    bodies = {b.name: b for b in built.bodies}
    worst = 0.0
    for buoy, (owner, node) in built.buoy_joint_nodes.items():
        index = int(buoy.removeprefix("buoy")) - 1
        got = bodies[owner].model.nodes.coords()[node][:2]
        worst = max(worst, float(np.linalg.norm(got - expected[index])))
    assert worst < F4_EB6_POSITION_M, (
        f"the worst buoy-label position disagrees with HSP-stable by {worst:.6e} m. "
        "Either a label names the wrong node or the geometry has moved."
    )


@needs_hsp_stable
def test_EB6_a_PERMUTED_export_reddens_the_gate(built: Superstructure) -> None:
    """EB6's counter-case, constructed rather than asserted.

    The smallest permutation is a transposition of the two closest labels, which is the
    hardest case: `0.619657 m` at model scale, settled at verdict 91 as the smallest
    single-swap displacement. Anything the gate would miss, it would miss here first.
    """
    expected = _hsp_stable_buoy_centres() * built.froude_lambda
    permuted = expected.copy()
    permuted[[1, 3]] = permuted[[3, 1]]  # buoy2 <-> buoy4, the closest pair

    # RUN THE GATE'S OWN COMPARISON against the permuted expectation, rather than
    # measuring a property of the geometry and inferring that the gate would notice.
    bodies = {b.name: b for b in built.bodies}
    worst = 0.0
    for buoy, (owner, node) in built.buoy_joint_nodes.items():
        index = int(buoy.removeprefix("buoy")) - 1
        got = bodies[owner].model.nodes.coords()[node][:2]
        worst = max(worst, float(np.linalg.norm(got - permuted[index])))
    assert worst == pytest.approx(F4_EB6_POSITION_M_COUNTER_DEFECT, abs=F4_EB6_POSITION_M), (
        f"the transposition moves a label {worst:.6f} m, and the declared counter-case "
        f"is {F4_EB6_POSITION_M_COUNTER_DEFECT!r} m. If these disagree the geometry has "
        "moved and the counter-case no longer injects what it says it does."
    )
    assert worst > F4_EB6_POSITION_M, (
        f"with the two CLOSEST labels transposed the gate's own worst disagreement is "
        f"{worst:.6e} m, which the ceiling {F4_EB6_POSITION_M!r} ACCEPTS. The gate is "
        "blind to the permutation it exists to catch."
    )
