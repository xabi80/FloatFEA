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

import json
from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest
from numpy.typing import NDArray

from floatfea.io.frames import GRAVITY_MAGNITUDE, GRAVITY_VECTOR
from floatfea.loads.joint_reactions import duality_residual
from floatfea.model.nodes import node_dofs
from floatfea.model.platform import (
    BodyModel,
    Member,
    Superstructure,
    body_mass_matrix,
    build_superstructure,
)
from floatfea.post.member_forces import element_equivalent_load, member_forces
from floatfea.solve.static import solve_superstructure_static
from floatfea.tolerances import (
    F4_EB6_POSITION_M,
    F4_EB6_POSITION_M_COUNTER,
    F4_MEMBER_FORCE_CONSERVATION,
    F4_MEMBER_FORCE_CONSERVATION_COUNTER,
    F4_STATIC_REACTION_AGREEMENT,
    F4_STATIC_REACTION_AGREEMENT_COUNTER,
    F4_STATIC_TIP_MOMENT_N_M,
    F4_STATIC_TIP_MOMENT_N_M_COUNTER,
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
    """R663's gate, and R675's correction: THIS IS BLIND TO THE SOLVE, BY CONSTRUCTION.

    `k u`'s two end shears cancel identically, so the sum is always `-(f_eq_A + f_eq_B)`
    whatever `u` is. Measured: the real solve, `u = 0`, `u x 1000` and randomised `u` all
    give the same relative error, `<= 1.519e-16`. So this gate checks THE EQUIVALENT LOAD
    and nothing else -- it caught R663 because R663 deleted that load entirely, and it
    certifies nothing about the solution. `test_G4_the_tip_shear_equals_the_support_
    reaction` is the one that reads the solve, and its own blindness test is beside it.

    Saying so is the point: a gate whose reach is narrower than its name is how R663
    survived a check that looked like it covered this.

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

    # An explicit ZERO equivalent load is the defect, stated rather than omitted
    # (R677): `member_forces` no longer has a default to forget.
    mf = member_forces(body, member, cases[body.name].u_full, np.zeros(12))
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
    assert relative > F4_MEMBER_FORCE_CONSERVATION_COUNTER, (
        f"the defective formula is only {relative:.3e} away from conservation, so the "
        "gate above would pass on the broken code and certifies nothing."
    )


def test_G4_the_tip_shear_equals_the_support_reaction(built: Superstructure) -> None:
    """A second, independent reading of R663, on a different quantity.

    # expected: the support reaction from the solve's own `reactions` vector, which is
    not what `member_forces` computes -- so this compares two separately derived numbers.
    """
    cases = solve_superstructure_static(built)
    checked = 0
    for body in built.bodies:
        accel = _gravity_field(body.model.n_dof)
        case = cases[body.name]
        for member in body.members:
            if member.node_b not in case.vertical_reactions_N:
                continue
            checked += 1
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
    # R675's latent hazard, closed: the `continue` above skips nothing at F3's mesh --
    # measured, 16 run and 0 skipped -- but a silent skip is a hazard even when it is
    # currently empty, so the count is asserted and a topology change fails LOUDLY.
    assert checked == 16, (
        f"{checked} of 16 members were checked; the rest were skipped silently by the "
        "`continue`. A gate that quietly narrows its own subject is how a defect "
        "survives a green run."
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
        # SIGNED, not `abs()` (R674). Gravity acts in -z, so the applied vertical load
        # is NEGATIVE. Taking `abs()` made this blind to a sign flip, so the
        # `gravity reversed` injection -- the one verdict 93 measured as undetected --
        # PASSED on this very row.
        expected = -(case.weight_N + handed)
        assert case.applied_N == pytest.approx(expected, rel=F4_STATIC_REACTION_AGREEMENT), (
            f"{name}: the applied load is {case.applied_N!r} and minus the deck's own "
            f"weight plus what the platform hands down is {expected!r}. These are "
            "independently derived, which is what R664 found the shipped check was not."
        )


@pytest.mark.parametrize("injection", ["remainder_dropped", "gravity_reversed"])
def test_G4_1_static_the_weight_check_REDDENS_on_the_two_worst_misses(
    built: Superstructure, injection: str
) -> None:
    """R664's counter-case, INJECTED INTO THE MODEL rather than into the expected side.

    R674. The first version corrupted the number the gate compares AGAINST, which tests
    arithmetic rather than the gate. A gate reading a corrupted MODEL is the only thing
    that shows it would catch a corrupted model.
    """
    cases = solve_superstructure_static(built)
    platform = next(b for b in built.bodies if b.name == "platform")
    case = cases["platform"]

    corrupt_body = (
        replace(platform, remainder_mass=0.0) if injection == "remainder_dropped" else platform
    )
    accel = _gravity_field(corrupt_body.model.n_dof)
    if injection == "gravity_reversed":
        accel = -accel

    mass = body_mass_matrix(corrupt_body)
    n_nodes = mass.shape[0] // 6
    applied = float(sum((mass @ accel)[node_dofs(n)[2]] for n in range(n_nodes)))
    expected = -case.weight_N  # the platform receives nothing from upstream

    assert applied != pytest.approx(expected, rel=F4_STATIC_REACTION_AGREEMENT), (
        f"with {injection!r} the applied vertical load is {applied!r}, which the gate "
        f"accepts against the expected {expected!r}. It cannot discriminate, and R664 "
        "is not answered."
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

    mf = member_forces(platform, member, case.u_full, np.zeros(12))  # the defect
    reaction = case.vertical_reactions_N[member.node_b]
    shortfall = (reaction - float(mf.end_b[2])) / reaction

    assert shortfall == pytest.approx(
        F4_STATIC_REACTION_AGREEMENT_COUNTER, rel=F4_STATIC_REACTION_AGREEMENT
    ), (
        f"the defective formula falls {shortfall:.6%} short of the reaction and the "
        f"declared counter-case is {F4_STATIC_REACTION_AGREEMENT_COUNTER!r}. "
        "If these disagree the defect is not the one R663 names."
    )
    assert (
        shortfall > F4_STATIC_REACTION_AGREEMENT
    ), "the agreement ceiling would accept R663's defect, so it certifies nothing."


# --------------------------------------------------------------------------- R667 / EO0
EB6_SOURCE_BLOB = "b8b8123904aff2b79785043255cb28fcc6527ab5"
"""The HSP-stable blob the snapshot was generated from (EO0(b))."""

EB6_REFERENCE = Path(__file__).resolve().parents[3] / "data" / "platform" / "buoy_centers_ref.json"


def _eb6_reference() -> dict[str, object]:
    """EB6's expected side, from the PINNED SNAPSHOT (EO0).

    # expected: `data/platform/buoy_centers_ref.json`, generated by
    `scripts/export_buoy_centers_ref.py` from HSP-stable's own
    `studies/platform-12buoy/platform_common.py` -- CLUSTER_ARM_RADIUS `:33`,
    CLUSTER_ANGLES_DEG `:34`, BUOY_ANGLES_DEG `:35`, BUOY_RADIUS `:36`, Z_HUB_REF `:102`,
    `buoy_centers()` `:51-58`, the hub `Body` `:157` -- at blob
    `b8b8123904aff2b79785043255cb28fcc6527ab5`, tag `floatfea-ref-1`.

    THIS FILE IS NOT THE DECK EXPORT, which is the whole point: a permuted export cannot
    reach it. The snapshot is kept honest by `--check` in the DS0 preflight (EO0(c)), not
    by a pytest skip -- `scripts/run_rung.sh` fails a rung on any skip, which is what made
    this gate red as R670.
    """
    assert EB6_REFERENCE.is_file(), (
        f"{EB6_REFERENCE} is missing. It is committed precisely so this gate needs no "
        "HSP-stable worktree and therefore no skip; regenerate it with "
        "`python scripts/export_buoy_centers_ref.py` where that worktree exists."
    )
    data = json.loads(EB6_REFERENCE.read_text(encoding="utf-8"))
    assert data["provenance"]["blob_sha"] == EB6_SOURCE_BLOB, (
        f"the snapshot records blob {data['provenance']['blob_sha']!r} and this gate "
        f"expects {EB6_SOURCE_BLOB!r}. One of them has moved, and a gate whose expected "
        "side moved silently is R600's defect."
    )
    assert data["scale"] == "model", f"the snapshot is {data['scale']!r}, not model scale"
    return data


def test_EB6_every_buoy_label_sits_where_HSP_STABLE_SAYS(built: Superstructure) -> None:
    """EB6's first side, against the pinned snapshot. NO SKIP (EO0(b))."""
    reference = _eb6_reference()
    expected = np.asarray(reference["buoy_centres_xy_m"], dtype=np.float64) * built.froude_lambda
    bodies = {b.name: b for b in built.bodies}
    worst = 0.0
    checked = 0
    for buoy, (owner, node) in built.buoy_joint_nodes.items():
        index = int(buoy.removeprefix("buoy")) - 1
        got = bodies[owner].model.nodes.coords()[node][:2]
        worst = max(worst, float(np.linalg.norm(got - expected[index])))
        checked += 1
    assert checked == 12, f"{checked} of 12 buoy labels were checked, not all of them"
    assert worst < F4_EB6_POSITION_M, (
        f"the worst buoy-label position disagrees with the pinned reference by "
        f"{worst:.6e} m. Either a label names the wrong node or the geometry has moved."
    )


def test_EB6_every_HUB_label_sits_where_HSP_STABLE_SAYS(built: Superstructure) -> None:
    """DQ9's hub extension, which verdict 94 recorded as absent (R676)."""
    reference = _eb6_reference()
    expected = np.asarray(reference["hub_positions_xyz_m"], dtype=np.float64) * built.froude_lambda
    bodies = {b.name: b for b in built.bodies}
    worst = 0.0
    checked = 0
    for hub, owner in sorted(built.deck_joint_owner.items()):
        if owner != "platform":
            continue
        index = int(hub.removeprefix("hub")) - 1
        node = bodies["platform"].model.nodes.index(f"platform:{hub}_arm_tip")
        got = bodies["platform"].model.nodes.coords()[node]
        worst = max(worst, float(np.linalg.norm(got[:2] - expected[index][:2])))
        checked += 1
    assert checked == 4, f"{checked} of 4 hub joints were checked, not all of them"
    assert worst < F4_EB6_POSITION_M, (
        f"the worst hub-label position disagrees with the pinned reference by " f"{worst:.6e} m."
    )


def test_EB6_a_PERMUTED_export_reddens_the_gate(built: Superstructure) -> None:
    """EB6's counter-case, which EO0(d) keeps. Constructed, not asserted.

    The smallest permutation is a transposition of the two closest labels -- the hardest
    case, so anything the gate would miss it would miss here first.
    """
    reference = _eb6_reference()
    expected = np.asarray(reference["buoy_centres_xy_m"], dtype=np.float64) * built.froude_lambda
    permuted = expected.copy()
    permuted[[1, 3]] = permuted[[3, 1]]  # buoy2 <-> buoy4, the closest pair

    bodies = {b.name: b for b in built.bodies}
    worst = 0.0
    for buoy, (owner, node) in built.buoy_joint_nodes.items():
        index = int(buoy.removeprefix("buoy")) - 1
        got = bodies[owner].model.nodes.coords()[node][:2]
        worst = max(worst, float(np.linalg.norm(got - permuted[index])))

    assert worst == pytest.approx(F4_EB6_POSITION_M_COUNTER, abs=F4_EB6_POSITION_M), (
        f"the transposition moves a label {worst:.6f} m and the declared counter-case is "
        f"{F4_EB6_POSITION_M_COUNTER!r} m. If these disagree the counter no longer "
        "injects what it says it does."
    )
    assert worst > F4_EB6_POSITION_M, (
        f"with the two CLOSEST labels transposed the gate's own worst disagreement is "
        f"{worst:.6e} m, which the ceiling ACCEPTS. The gate is blind to the permutation "
        "it exists to catch."
    )


# --------------------------------------------------------------------------- EO1
def _analytic_static(body: BodyModel, member: Member, reaction: float) -> tuple[float, float]:
    """`(root Vz, root My)` from statics alone: deck masses, `f`, geometry.

    # expected: analytic. A cantilever-with-end-roller: vertical equilibrium gives the
    root shear as `R - wL`, and moments about the root give `R L - wL^2/2`. Nothing here
    reads the model's stiffness, its displacement or its member forces, which is what
    makes it an independent side rather than a second route to the same arithmetic.
    """
    span = member.length
    own_weight = body.member_mass / len(body.members) * GRAVITY_MAGNITUDE
    return reaction - own_weight, reaction * span - own_weight * span / 2.0


def test_EO1_static_member_forces_match_STATICS_not_the_model(built: Superstructure) -> None:
    """EO1, and it answers R675: this gate READS THE SOLVE.

    `root My` is `R L - wL^2/2`, and `R` is the support reaction the solve produced -- so
    a wrong displacement field moves this figure, where the conservation gate cannot see
    it. Confirmed against the directive's own arithmetic: platform `114960937.5 N*m`,
    hub `117515625 N*m`, both reproduced to every digit.
    """
    cases = solve_superstructure_static(built)
    checked = 0
    for body in built.bodies:
        accel = _gravity_field(body.model.n_dof)
        case = cases[body.name]
        for member in body.members:
            reaction = case.vertical_reactions_N[member.node_b]
            want_vz, want_my = _analytic_static(body, member, reaction)
            mf = member_forces(
                body, member, case.u_full, element_equivalent_load(body, member, accel)
            )
            checked += 1
            assert abs(float(mf.end_a[2])) == pytest.approx(
                want_vz, rel=F4_STATIC_REACTION_AGREEMENT
            ), f"{member.label}: root Vz {mf.end_a[2]!r} against statics' {want_vz!r}"
            assert abs(float(mf.end_a[4])) == pytest.approx(
                want_my, rel=F4_STATIC_REACTION_AGREEMENT
            ), f"{member.label}: root My {mf.end_a[4]!r} against statics' {want_my!r}"
            assert abs(float(mf.end_b[4])) < F4_STATIC_TIP_MOMENT_N_M, (
                f"{member.label}: the tip moment is {mf.end_b[4]!r}, and a roller "
                "support transmits none. R663's defect put it at exactly -mu L^2 / 12."
            )
    assert checked == 16, f"{checked} of 16 members were checked, not all of them"


def test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula(built: Superstructure) -> None:
    """EO1's counter-case: the shipped defect must fail the analytic comparison."""
    cases = solve_superstructure_static(built)
    body = next(b for b in built.bodies if b.name == "platform")
    member = body.members[0]
    case = cases[body.name]
    reaction = case.vertical_reactions_N[member.node_b]
    want_vz, want_my = _analytic_static(body, member, reaction)

    mf = member_forces(body, member, case.u_full, np.zeros(12))  # R663's formula
    assert abs(float(mf.end_a[2])) != pytest.approx(want_vz, rel=F4_STATIC_REACTION_AGREEMENT)

    # The declared counter IS the defect's own magnitude, `mu L^2 / 12`, and naming it
    # here is what makes it injected rather than a literal beside another literal.
    tip = abs(float(mf.end_b[4]))
    assert tip == pytest.approx(
        F4_STATIC_TIP_MOMENT_N_M_COUNTER, rel=F4_STATIC_REACTION_AGREEMENT
    ), (
        f"the defect's tip moment is {tip!r} and the declared counter is "
        f"{F4_STATIC_TIP_MOMENT_N_M_COUNTER!r}. If they disagree the counter no longer "
        "describes the defect it is supposed to inject."
    )
    assert (
        tip > F4_STATIC_TIP_MOMENT_N_M
    ), "the ceiling accepts R663's tip moment, so the gate certifies nothing."
