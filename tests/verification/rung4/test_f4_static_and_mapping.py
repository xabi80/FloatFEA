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
from floatfea.io.froude import to_full_scale
from floatfea.loads.joint_reactions import ROWS_PER_JOINT, duality_residual, map_joint_reactions
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
    F4_MAPPING_CONSERVATION,
    F4_MAPPING_CONSERVATION_COUNTER,
    F4_MEMBER_FORCE_CONSERVATION,
    F4_MEMBER_FORCE_CONSERVATION_COUNTER,
    F4_STATIC_REACTION_AGREEMENT,
    F4_STATIC_REACTION_AGREEMENT_COUNTER,
    F4_STATIC_SYMMETRY_SPREAD,
    F4_STATIC_SYMMETRY_SPREAD_COUNTER,
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
        for member in body.members:
            # EACH ELEMENT'S OWN MASS, IN CLOSED FORM (R675). This was
            # `body.member_mass / len(body.members)`, a body AVERAGE that equals the
            # element mass only on a frame whose members are equal in length. I asserted
            # that premise and it is FALSE: `hub1`'s members measure 25.0, 25.0 and
            # 25.000000000000004 m, one and two ulp apart from the 120-degree geometry.
            # Equal to round-off is not equal, and on a frame with genuinely unequal
            # members the average would have made this gate FALSE-REDDEN -- a wrong
            # answer rather than a missed one. `rho A L` is the prismatic mass of THIS
            # element and it is also independent of the assembler (EA4): the consistent
            # mass matrix the gate reads through `element_equivalent_load` is not where
            # this number comes from.
            weight = float(
                body.material.rho * member.section.A * member.length * abs(GRAVITY_VECTOR[2])
            )
            f_eq = element_equivalent_load(body, member, accel)
            mf = member_forces(body, member, cases[body.name].u_full, f_eq)
            carried = float(mf.end_a[2] + mf.end_b[2])
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
    # `rho A L`, the same closed form the gate above uses after R675.
    weight = float(body.material.rho * member.section.A * member.length * abs(GRAVITY_VECTOR[2]))

    # An explicit ZERO equivalent load is the defect, stated rather than omitted
    # (R677): `member_forces` no longer has a default to forget.
    mf = member_forces(body, member, cases[body.name].u_full, np.zeros(12))
    carried = float(mf.end_a[2] + mf.end_b[2])
    relative = abs(carried - weight) / weight

    # SIGNATURE, against the COUNTER and NOT against the ceiling (R671). This read
    # `< F4_MEMBER_FORCE_CONSERVATION`, which made the assertion EASIER as the ceiling
    # rose and was half of why nothing bounded the ceiling above. `k u`'s end shears
    # cancel identically, so the defective formula carries nothing to round-off, and the
    # counter is a loose bound that the signature satisfies by fifteen decades.
    assert abs(carried) / weight < F4_MEMBER_FORCE_CONSERVATION_COUNTER, (
        f"without the equivalent load the end shears sum to {carried!r}, not zero. The "
        "defect's signature is that they cancel IDENTICALLY, so if this is nonzero the "
        "counter-case no longer reproduces R663 and the gate above is measuring "
        "something else."
    )
    assert relative > F4_MEMBER_FORCE_CONSERVATION_COUNTER, (
        f"the defective formula is only {relative:.3e} away from conservation, so the "
        "gate above would pass on the broken code and certifies nothing."
    )
    # AND AGAINST THE CEILING ITSELF, so that raising the ceiling makes THIS assertion
    # HARDER (R671). The defect's relative error is exactly 1.0 -- the whole of the
    # member's weight is missing -- so a ceiling at or above 1.0 reddens here, which is
    # the number the ninety-fourth verdict measured rising to `1.0e+6` with 150 green.
    assert relative > F4_MEMBER_FORCE_CONSERVATION, (
        f"the ceiling {F4_MEMBER_FORCE_CONSERVATION:.3e} is not below the error the "
        f"defect produces, {relative:.3e}. The gate above would ACCEPT R663. This "
        "assertion exists to get harder as the ceiling is widened, not easier."
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
    expected = np.asarray(
        to_full_scale(
            np.asarray(reference["buoy_centres_xy_m"], dtype=np.float64),
            "length",
            built.froude_lambda,
        ),
        dtype=np.float64,
    )
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
    expected = np.asarray(
        to_full_scale(
            np.asarray(reference["hub_positions_xyz_m"], dtype=np.float64),
            "length",
            built.froude_lambda,
        ),
        dtype=np.float64,
    )
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
    expected = np.asarray(
        to_full_scale(
            np.asarray(reference["buoy_centres_xy_m"], dtype=np.float64),
            "length",
            built.froude_lambda,
        ),
        dtype=np.float64,
    )
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


# --------------------------------------------------------------------------- R676 / EK0(d)
def _reaction_spread(case: object) -> float:
    """`(max - min) / mean` over a body's vertical reactions.

    Relative, because the quantity being tested is whether the four shares are the SAME,
    not what they are. Normalised by the mean rather than by the weight so the figure is
    about the split alone.
    """
    v = np.array(sorted(case.vertical_reactions_N.values()), dtype=np.float64)  # type: ignore[attr-defined]
    return float((v.max() - v.min()) / abs(v.mean()))


def _soften_one_arm(built: Superstructure, factor: float) -> Superstructure:
    """One platform arm's `I_y`, `I_z`, `J` scaled; `A` HELD, so the mass is unchanged.

    ONE VARIABLE MOVED (BG0). Scaling `A` too would change the body's mass and the weight
    it carries, and the reaction split would then move for two reasons at once.
    """
    bodies = []
    for body in built.bodies:
        if body.name != "platform":
            bodies.append(body)
            continue
        members = list(body.members)
        s = members[0].section
        members[0] = replace(
            members[0],
            section=replace(s, I_y=s.I_y * factor, I_z=s.I_z * factor, J=s.J * factor),
        )
        bodies.append(replace(body, members=tuple(members)))
    return replace(built, bodies=tuple(bodies))


def test_EK0d_the_platform_four_hub_reactions_are_EQUAL(built: Superstructure) -> None:
    """EK0(d)'s third check, which had no assertion until now (R676).

    # expected: the frame's four-fold symmetry, which is a property of the GEOMETRY and
    not of the solve -- the four arms are equal in length and equally spaced, so an
    equal split is the only answer compatible with the symmetry. This is the only one of
    EK0(d)'s three checks the FE stiffness participates in: the fourth vertical support
    is redundant, so the split between the four is a stiffness answer rather than a
    statics one, and a wrong stiffness shows up here and nowhere else in EK0(d).
    """
    case = solve_superstructure_static(built)["platform"]
    assert len(case.vertical_reactions_N) == 4, (
        f"{len(case.vertical_reactions_N)} vertical reactions on the platform, not 4. "
        "The symmetry statement is about the four hub supports and this gate is not "
        "reading them."
    )
    spread = _reaction_spread(case)
    assert spread < F4_STATIC_SYMMETRY_SPREAD, (
        f"the platform's four hub reactions spread by {spread:.6e} relative, which is "
        f"outside {F4_STATIC_SYMMETRY_SPREAD:.1e}. The frame is four-fold symmetric, so "
        "either the geometry is not what it should be or the stiffness that decides the "
        f"split is wrong. Reactions: {sorted(case.vertical_reactions_N.values())}"
    )


def test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame(built: Superstructure) -> None:
    """The counter-case: soften ONE arm in the MODEL and re-solve.

    Injected into the model and not into the expected side -- R674 was the finding that
    the expected side is the wrong place to corrupt, and this gate is written after it.
    """
    case = solve_superstructure_static(_soften_one_arm(built, 0.01))["platform"]
    spread = _reaction_spread(case)
    assert spread > F4_STATIC_SYMMETRY_SPREAD_COUNTER, (
        f"softening one arm 100x gives a spread of {spread!r}, which does not reach the "
        f"declared counter {F4_STATIC_SYMMETRY_SPREAD_COUNTER!r}. The counter is the "
        "smallest defect this gate must still fail, so an injection that no longer "
        "reaches it is no longer the defect the counter names."
    )
    assert spread > F4_STATIC_SYMMETRY_SPREAD, (
        f"with one arm 100x softer the spread is {spread:.6e}, which the ceiling "
        "ACCEPTS. The gate is blind to the asymmetry it exists to catch."
    )


# --------------------------------------------------------------------------- R676 / G4.4
def _joint_wiring(built: Superstructure) -> tuple[list[tuple[str, str, str]], dict, dict]:
    """`(joint_order, nodes, n_dof_of)` for `map_joint_reactions`, from the BUILDER.

    The production driver takes `joint_order` from the deck, which is the authority for
    it. Here it is formed from the builder's own maps, because this gate is a property of
    the MAPPER and must run without an HSP worktree -- the lesson of R670. What the gate
    therefore does NOT check is that this order matches the deck's; that is the driver's
    job and it is stated here rather than left to be found.
    """
    by_name = {b.name: b for b in built.bodies}
    n_dof_of = {b.name: b.model.n_dof for b in built.bodies}
    joint_order: list[tuple[str, str, str]] = []
    nodes: dict[tuple[str, str], int] = {}
    for buoy, (owner, node) in sorted(built.buoy_joint_nodes.items()):
        joint_order.append((buoy, buoy, owner))
        nodes[(buoy, owner)] = node
    for hub, owner in sorted(built.deck_joint_owner.items()):
        if owner != "platform":
            continue
        joint_order.append((hub, hub, "platform"))
        nodes[(hub, hub)] = by_name[hub].centre_node
        nodes[(hub, "platform")] = by_name["platform"].model.nodes.index(f"platform:{hub}_arm_tip")
    return joint_order, nodes, n_dof_of


def _resultants(
    built: Superstructure, loads: dict[str, NDArray[np.float64]]
) -> NDArray[np.float64]:
    """`[F, M]` about the GLOBAL ORIGIN of a mapped nodal load set."""
    by_name = {b.name: b for b in built.bodies}
    out = np.zeros(6, dtype=np.float64)
    for body, f in loads.items():
        coords = by_name[body].model.nodes.coords()
        for nd in range(f.size // 6):
            force = f[6 * nd : 6 * nd + 3]
            out[0:3] += force
            out[3:6] += f[6 * nd + 3 : 6 * nd + 6] + np.cross(coords[nd], force)
    return out


def _expected_resultants(
    built: Superstructure,
    lam_row: NDArray[np.float64],
    joint_order: list[tuple[str, str, str]],
    nodes: dict[tuple[str, str], int],
    n_dof_of: dict[str, int],
) -> NDArray[np.float64]:
    """What the deck's blocks and the builder's nodes say those resultants must be.

    # expected: formed from the MULTIPLIER BLOCKS and the node coordinates, not from the
    mapper's output (EA4). A hub-platform joint contributes `+(F, M)` and `-(F, M)` and
    its force cancels, but its MOMENT about the origin does not unless both sides act at
    the same point -- which is exactly the error a resultant force cannot see.
    """
    by_name = {b.name: b for b in built.bodies}
    out = np.zeros(6, dtype=np.float64)
    for i, (joint, body_a, body_b) in enumerate(joint_order):
        block = lam_row[ROWS_PER_JOINT * i : ROWS_PER_JOINT * (i + 1)]
        force = np.asarray(block[0:3], dtype=np.float64)
        moment = np.array([0.0, 0.0, float(block[3])], dtype=np.float64)
        for sign, body in ((1.0, body_a), (-1.0, body_b)):
            if body not in n_dof_of:
                continue  # a buoy is a load on the superstructure, not a modelled body
            x = by_name[body].model.nodes.coords()[nodes[(joint, body)]]
            out[0:3] += sign * force
            out[3:6] += sign * moment + np.cross(x, sign * force)
    return out


def _mapping_error(
    built: Superstructure,
    loads: dict[str, NDArray[np.float64]],
    want: NDArray[np.float64],
) -> float:
    """Worst relative departure, force and moment normalised separately."""
    got = _resultants(built, loads)
    f_scale = max(float(np.max(np.abs(want[0:3]))), 1.0)
    m_scale = max(float(np.max(np.abs(want[3:6]))), 1.0)
    return max(
        float(np.max(np.abs(got[0:3] - want[0:3]))) / f_scale,
        float(np.max(np.abs(got[3:6] - want[3:6]))) / m_scale,
    )


def _synthetic_lam(n_joints: int) -> NDArray[np.float64]:
    """One multiplier row, every block different.

    Pseudo-random with a fixed seed rather than a tidy pattern: equal blocks would let a
    sign error at one joint cancel against another's, and a gate that only works on
    awkward numbers should be given awkward numbers.
    """
    return np.asarray(
        np.random.default_rng(4).normal(0.0, 1.0e6, ROWS_PER_JOINT * n_joints),
        dtype=np.float64,
    )


def test_G4_4_the_mapping_CONSERVES_the_joint_resultants(built: Superstructure) -> None:
    """G4.4, which had no assertion and whose mapper no test called (R676).

    The property: everything `map_joint_reactions` puts on the five modelled bodies has
    the resultant force AND the resultant moment about the origin that the joint blocks
    and the joint nodes require. It catches a dropped joint, a sign on the wrong side,
    and a block on the wrong node.
    """
    joint_order, nodes, n_dof_of = _joint_wiring(built)
    assert len(joint_order) == 16, f"{len(joint_order)} joints wired, not 16"
    lam_row = _synthetic_lam(len(joint_order))
    loads = map_joint_reactions(lam_row, joint_order, nodes, n_dof_of)
    assert set(loads) == set(n_dof_of), (
        f"the mapper returned {sorted(loads)} and the bodies are {sorted(n_dof_of)}. A "
        "body missing from the output carries no joint load at all."
    )
    want = _expected_resultants(built, lam_row, joint_order, nodes, n_dof_of)
    error = _mapping_error(built, loads, want)
    assert error < F4_MAPPING_CONSERVATION, (
        f"the mapped load's resultants depart from the joint blocks' own by {error:.6e} "
        f"relative, outside {F4_MAPPING_CONSERVATION:.1e}. Either a block was dropped, "
        "or a sign is on the wrong side, or a block landed on the wrong node."
    )


@pytest.mark.parametrize("injection", ["sign_not_flipped", "wrong_node_same_body"])
def test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node(
    built: Superstructure, injection: str
) -> None:
    """Both counter-cases, injected into the MAPPED OUTPUT and not into the expected side.

    `wrong_node_same_body` is the one the declared counter is taken from, because it is
    the smaller of the two AND the one a resultant-force-only gate cannot see: measured,
    it leaves the force at `5.205e-17` and puts the moment at `0.2437`.
    """
    joint_order, nodes, n_dof_of = _joint_wiring(built)
    lam_row = _synthetic_lam(len(joint_order))
    loads = {
        k: v.copy() for k, v in map_joint_reactions(lam_row, joint_order, nodes, n_dof_of).items()
    }
    want = _expected_resultants(built, lam_row, joint_order, nodes, n_dof_of)

    hubs = [i for i, (_j, _a, b) in enumerate(joint_order) if b == "platform"]
    assert len(hubs) == 4, f"{len(hubs)} hub-platform joints, not 4"
    i = hubs[0]
    joint = joint_order[i][0]
    block = lam_row[ROWS_PER_JOINT * i : ROWS_PER_JOINT * (i + 1)]
    share = np.concatenate([-np.asarray(block[0:3]), [0.0, 0.0, -float(block[3])]])
    here = nodes[(joint, "platform")]

    if injection == "sign_not_flipped":
        loads["platform"][6 * here : 6 * here + 6] -= 2.0 * share
    else:
        there = nodes[(joint_order[hubs[1]][0], "platform")]
        loads["platform"][6 * here : 6 * here + 6] -= share
        loads["platform"][6 * there : 6 * there + 6] += share

    error = _mapping_error(built, loads, want)
    if injection == "wrong_node_same_body":
        assert error > F4_MAPPING_CONSERVATION_COUNTER, (
            f"the wrong-node injection reads {error!r}, which does not reach the declared "
            f"counter {F4_MAPPING_CONSERVATION_COUNTER!r}. That injection is the SMALLER "
            "of the two and the one the counter is taken from, so if it shrinks the "
            "counter stops describing the defect the gate must catch."
        )
    assert error > F4_MAPPING_CONSERVATION, (
        f"the `{injection}` injection reads {error:.6e}, which the ceiling ACCEPTS. The "
        "gate is blind to a defect it exists to catch."
    )


# --------------------------------------------------------------------------- R676 / EK0(a)
FE_BODY_NAMES = ("platform", "hub1", "hub2", "hub3", "hub4")
"""The five bodies F4 models structurally. EK0's scope correction: they are DRY."""


def _premise_violations(sites: list[str]) -> list[str]:
    """EK0(a)'s premise, as a function so the gate and its counter-case run the SAME code.

    Returns one sentence per violation. Written as a function rather than inline because a
    counter-case that re-states the assertion tests the counter-case: `duality_residual`
    was found passing on `(a, -a)` for exactly that reason, and this file is written after
    that finding.
    """
    out: list[str] = []
    for site in sites:
        for name in FE_BODY_NAMES:
            if name in site:
                out.append(
                    f"HSP-stable assigns `hydro_body_label = {site}`, which names the FE "
                    f"body `{name}`. EK0's scope correction says the five FE bodies are "
                    "DRY and EK0(a) says to STOP if they are not. This is that stop."
                )
        if "buoy" not in site:
            out.append(
                f"HSP-stable assigns `hydro_body_label = {site}`, which is not a buoy "
                "label. The premise is that only buoys are wet; a third kind of labelled "
                "body is something this milestone's scope has not been told about."
            )
    return out


def test_EK0a_no_FE_BODY_carries_a_hydro_label_in_HSP_STABLE() -> None:
    """EK0(a)'s premise, as an assertion rather than a report figure (R676).

    # expected: `data/platform/buoy_centers_ref.json`'s `hydro_body_label_sites`,
    generated by `scripts/export_buoy_centers_ref.py` from HSP-stable's own
    `studies/platform-12buoy/platform_common.py:140` at blob
    `b8b8123904aff2b79785043255cb28fcc6527ab5` -- independent of FloatFEA entirely (EA4).

    WHAT THIS ASSERTS AND WHAT THE REPORT MEASURED ARE NOT THE SAME STATEMENT, and the
    difference is the point. The report ran all six cases over 24,006 steps and found the
    per-body external hydrodynamic force identically `0.000000e+00 N`. That is a sample,
    however large. This is the STRUCTURAL reason it is zero: no excitation channel
    addresses a body that carries no `hydro_body_label`, so there is no cancellation to
    rely on. The sample cannot run in CI without an HSP worktree, and a gate that skips
    turns its rung red (R670); this one runs everywhere the snapshot does.

    WHAT IT DOES NOT CATCH: a body that acquires a label in HSP-stable AFTER this blob.
    The snapshot's `--check` in the DS0 preflight is what sees that, and it is the same
    limitation EB6's first side has for the same reason.
    """
    sites = _eb6_reference()["hydro_body_label_sites"]
    assert isinstance(sites, list) and sites, (
        f"the snapshot's hydro_body_label_sites is {sites!r}. An empty list would make "
        "the check below vacuously true, which is the one way this gate could certify "
        "nothing."
    )
    violations = _premise_violations(sites)
    assert not violations, " AND ".join(violations)


@pytest.mark.parametrize(
    "site", ['f"hub{k + 1}"', '"platform"', 'f"deck{k}"', '"buoy1_and_platform"']
)
def test_EK0a_the_premise_gate_REDDENS_on_a_LABELLED_FE_BODY(site: str) -> None:
    """The counter-case, which runs THE GATE'S OWN CHECK on a corrupted snapshot value.

    The injection is into the expected side, and that is correct here rather than a repeat
    of R674: this gate's whole content is a statement ABOUT HSP-stable's source, so the
    source's value IS the thing under test. The last entry is the one that matters --
    a label naming both a buoy and an FE body passes a "is there a buoy in it" check and
    must still redden.
    """
    assert _premise_violations([site]), (
        f"`hydro_body_label = {site}` produced no violation, so the gate above would "
        "accept a labelled FE body and EK0(a) would never stop the step."
    )
