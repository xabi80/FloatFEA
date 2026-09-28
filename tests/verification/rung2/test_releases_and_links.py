"""V2.6 -- end releases and rigid links (D2 step 11).

`docs/verification/README.md`: "A pinned-end member carries no end moment; a
rigid link reproduces exact kinematic transfer. Both are constraint-handling
tests disguised as element tests." Q1b puts V2.6's provenance at **constructed**:
this is about constraint behaviour, not accuracy, so every comparison here is a
quantity that is exact in exact arithmetic and every threshold is
`ROUNDOFF_IDENTITY`.

`RIGID_LINK_CONSTRAINT` IS NOT CREATED, AND THAT IS THE CONSERVATIVE DIRECTION.
§D5 anticipated an ACCURACY entry for it with "a lever arm dropped from the MPC"
as the counter. The counter is here and it fires. What the entry would have
carried is a band, and there is no band to carry: rigid-body kinematics is exact,
the measured agreement is at round-off, and a new looser constant would be a
weaker assertion than the one this file makes. The counter's measurement is in
the step report so the entry can be added if F3 finds a case that needs one.

DJ0's GIMBAL is one of the cases, as DK2 requires: a two-rotation gimbal releases
the two free moments and transmits the moment about the locked axis.
"""

from __future__ import annotations

import numpy as np
import pytest

from floatfea import basis
from floatfea.assemble.system import (
    BeamElement,
    assemble_dense,
    element_global_stiffness,
    element_length,
)
from floatfea.element.beam import local_mass, local_stiffness
from floatfea.element.constraints import (
    constraint_transform,
    reduce_matrix,
    rigid_link_block,
    skew,
    slave_motion,
)
from floatfea.element.releases import (
    MOMENT_DOFS,
    condense,
    gimbal_release,
    recovery_matrix,
    released_local_stiffness,
)
from floatfea.element.transform import rotation_matrix, transformation
from floatfea.model.material import Material, Section
from floatfea.model.nodes import Model, Node, NodeSet
from floatfea.tolerances import ROUNDOFF_IDENTITY

STEEL = Material(E=2.1e11, nu=0.3, rho=7850.0, fy=355.0e6, name="S355")


def _tube(d_outer: float, t: float) -> Section:
    inertia = basis.tube_second_moment(d_outer, t)
    return Section(
        A=basis.tube_area(d_outer, t),
        I_y=inertia,
        I_z=inertia,
        J=basis.torsion_constant("thin_tube", inertia, inertia),
        shape="thin_tube",
    )


# --------------------------------------------------------------------------
# A pinned end carries no moment
# --------------------------------------------------------------------------


@pytest.mark.parametrize("end", ["a", "b"])
@pytest.mark.parametrize("axis", ["y", "z"])
@pytest.mark.parametrize("length", [1.0, 4.0, 60.0])
def test_a_PINNED_END_carries_NO_MOMENT(end: str, axis: str, length: float, capsys) -> None:
    """The defining property, read off the condensed matrix itself.

    A released DOF transmits no force for ANY retained displacement, so the
    released row of the condensed stiffness is identically zero -- not small for
    the particular load case someone happened to try. That is the strongest form
    of the statement and it is one line.
    """
    section = _tube(0.4, 0.010)
    k = local_stiffness(section, STEEL, length)
    released = (MOMENT_DOFS[axis][0 if end == "a" else 1],)
    condensed = released_local_stiffness(k, released)

    scale = float(np.max(np.abs(k)))
    worst = float(np.max(np.abs(condensed[released[0], :]))) / scale
    with capsys.disabled():
        print(f"\n  end {end}, moment about {axis}, L={length}: worst row entry {worst:.3e}")
    assert worst <= ROUNDOFF_IDENTITY, (
        f"the released row of the condensed stiffness is not zero -- worst "
        f"{worst:.4e} relative to max|k|, over {ROUNDOFF_IDENTITY:g}. A released "
        "DOF that transmits a force is a restraint, which is the opposite of a pin."
    )


@pytest.mark.parametrize("length", [1.0, 4.0, 60.0])
def test_the_condensed_element_matches_an_INDEPENDENTLY_TRANSCRIBED_propped_beam(
    length: float,
) -> None:
    """The condensation against the textbook propped-cantilever stiffness.

    With node B's rotation about local z released, the x-y bending block reduces
    to the standard propped form (Przemieniecki eq. 6.31 / Cook Table 2.3-1)::

                3 EI  [  1    L   -1 ]
        k_b =  ------ [  L   L^2  -L ]     on (v_A, rz_A, v_B)
                 L^3  [ -1   -L    1 ]

    TRANSCRIBED, not obtained by calling the condensation with a different
    argument. This is the Euler-Bernoulli form, so it is compared against the
    condensation run at `Phi = 0`; the shear-flexible case has no textbook
    propped matrix to transcribe and is covered by the released-row property
    above, which holds at any `Phi`.
    """
    section = _tube(0.4, 0.010)
    inertia = section.I_z
    ei = STEEL.E * inertia

    # Phi = 0 by construction: a bending block built from the transcribed
    # Euler-Bernoulli 4x4 rather than from `local_stiffness`.
    from floatfea.element.beam import euler_bernoulli_bending_stiffness

    k_full = np.zeros((12, 12), dtype=np.float64)
    block = euler_bernoulli_bending_stiffness(ei, length)
    k_full[np.ix_([1, 5, 7, 11], [1, 5, 7, 11])] = block
    # The axial and torsional terms keep k_cc invertible without touching the
    # bending block that is under test.
    k_full[np.ix_([0, 6], [0, 6])] = (STEEL.E * section.A / length) * np.array(
        [[1.0, -1.0], [-1.0, 1.0]]
    )
    k_full[np.ix_([3, 9], [3, 9])] = (STEEL.G * section.J / length) * np.array(
        [[1.0, -1.0], [-1.0, 1.0]]
    )

    condensed = released_local_stiffness(k_full, (11,))
    got = condensed[np.ix_([1, 5, 7], [1, 5, 7])]

    ll = length
    want = (3.0 * ei / ll**3) * np.array(
        [[1.0, ll, -1.0], [ll, ll**2, -ll], [-1.0, -ll, 1.0]], dtype=np.float64
    )
    worst = float(np.max(np.abs(got - want))) / float(np.max(np.abs(want)))
    assert worst <= ROUNDOFF_IDENTITY, (
        f"L={length}: the condensed bending block is not the transcribed propped "
        f"form -- worst {worst:.4e} relative, over {ROUNDOFF_IDENTITY:g}.\n"
        f"got\n{got}\nwant\n{want}"
    )


def test_the_MASS_is_condensed_by_the_SAME_recovery_matrix(capsys) -> None:
    """`m~ = R^T m R`, and `m_rr` is measurably not it.

    A released element's kinematics are `d = R d_r`, so its kinetic energy is the
    quadratic form on `R`. Taking `m_rr` instead drops the coupling to the
    released rotation, and the control here measures how much that is rather than
    asserting it matters.
    """
    section = _tube(0.4, 0.010)
    length = 4.0
    k = local_stiffness(section, STEEL, length)
    m = local_mass(section, STEEL, length)
    released = (11,)
    recovery = recovery_matrix(k, released)

    condensed = condense(m, recovery)
    naive = m.copy()
    naive[released[0], :] = 0.0
    naive[:, released[0]] = 0.0

    scale = float(np.max(np.abs(m)))
    difference = float(np.max(np.abs(condensed - naive))) / scale
    with capsys.disabled():
        print(f"\n  R^T m R against m_rr: {difference:.4e} relative to max|m|")
    assert difference > ROUNDOFF_IDENTITY, (
        "condensing the mass by the recovery matrix and simply deleting the "
        "released row give the same answer, so this test cannot tell the correct "
        "rule from the convenient one."
    )
    # And the rigid-body mass survives condensation: a released rotation does not
    # change how much the member weighs.
    translation = np.zeros(12)
    translation[1] = 1.0
    translation[7] = 1.0
    retained = translation.copy()
    got = float(retained @ condensed @ retained)
    want = STEEL.rho * section.A * length
    assert abs(got - want) / want <= ROUNDOFF_IDENTITY, (
        f"the condensed mass gives the member's mass as {got:.9e} against "
        f"{want:.9e}. A moment release cannot change a mass."
    )


# --------------------------------------------------------------------------
# DJ0's gimbal
# --------------------------------------------------------------------------


@pytest.mark.parametrize("locked", ["x", "y", "z"])
@pytest.mark.parametrize("end", ["a", "b"])
def test_the_GIMBAL_releases_TWO_moments_and_TRANSMITS_the_third(
    end: str, locked: str, capsys
) -> None:
    """DJ0: a two-rotation gimbal, both halves of the statement asserted.

    The released half is the zero rows. The TRANSMITTED half is the one a
    release test usually forgets: the locked axis must still carry a moment, and
    a pattern that released all three would pass a test that only checked the
    zeros.
    """
    section = _tube(0.4, 0.010)
    length = 4.0
    k = local_stiffness(section, STEEL, length)
    released = gimbal_release(end, locked)
    assert len(released) == 2, f"a gimbal releases two moments, not {len(released)}"

    condensed = released_local_stiffness(k, released)
    scale = float(np.max(np.abs(k)))

    freed = float(np.max(np.abs(condensed[list(released), :]))) / scale
    locked_dof = MOMENT_DOFS[locked][0 if end == "a" else 1]
    transmitted = float(np.max(np.abs(condensed[locked_dof, :]))) / scale
    with capsys.disabled():
        print(
            f"\n  end {end}, locked {locked}: released rows {freed:.3e}, "
            f"locked row {transmitted:.4e}"
        )

    assert freed <= ROUNDOFF_IDENTITY, (
        f"end {end}, locked {locked}: a gimbal's freed rotations still transmit "
        f"{freed:.4e} of max|k|."
    )
    assert transmitted > ROUNDOFF_IDENTITY, (
        f"end {end}, locked {locked}: the LOCKED axis transmits nothing either "
        f"({transmitted:.4e}), so this is a ball joint and not a gimbal. Both "
        "halves of DJ0's pattern have to hold."
    )


def test_releasing_a_RIGID_BODY_FREEDOM_raises_rather_than_pseudo_inverting() -> None:
    """A singular released set is refused, not smoothed over.

    Both end rotations about the same axis released together leaves the member's
    bending in that plane with a mechanism, and `k_cc` is then singular for the
    torsional axis. `CLAUDE.md`: a validation failure does not degrade to a
    warning, and a pseudo-inverse here would be a member transmitting something
    nobody chose.
    """
    section = _tube(0.4, 0.010)
    k = local_stiffness(section, STEEL, 4.0)
    with pytest.raises(ValueError, match="singular"):
        released_local_stiffness(k, (3, 9))


# --------------------------------------------------------------------------
# Rigid links
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "offset", [(1.0, 0.0, 0.0), (0.0, 2.5, 0.0), (0.7, -1.3, 2.9), (0.0, 0.0, 0.0)]
)
def test_a_RIGID_LINK_reproduces_EXACT_kinematic_transfer(offset: tuple[float, ...]) -> None:
    """`u_s = u_m + theta_m x d`, against the cross product written directly.

    The comparison is against `np.cross`, not against another matrix built the
    same way. A transposed skew would pass an energy test and fails this.
    """
    d = np.array(offset, dtype=np.float64)
    rng = np.random.default_rng(20260926)
    for _ in range(8):
        master = rng.standard_normal(6)
        got = slave_motion(master, d)
        want = np.concatenate([master[:3] + np.cross(master[3:], d), master[3:]])
        scale = max(float(np.max(np.abs(want))), 1.0)
        worst = float(np.max(np.abs(got - want))) / scale
        assert worst <= ROUNDOFF_IDENTITY, (
            f"offset {offset}: the link's transfer differs from `u_m + theta x d` "
            f"by {worst:.4e}. got {got}, want {want}"
        )


def test_a_DROPPED_LEVER_ARM_is_caught(capsys) -> None:
    """§D5's named counter for the rigid link: the lever arm dropped from the MPC.

    Measured rather than asserted to be catchable: with the arm dropped, a pure
    rotation at the master produces NO displacement at the slave, and the size of
    the miss is the lever arm times the rotation -- O(1), not a tolerance
    question.
    """
    d = np.array([0.7, -1.3, 2.9])
    master = np.array([0.0, 0.0, 0.0, 0.01, -0.02, 0.03])
    correct = slave_motion(master, d)
    dropped = np.eye(6) @ master  # the translation-only tie
    miss = float(np.max(np.abs(correct - dropped)))
    with capsys.disabled():
        print(f"\n  lever arm dropped: slave displacement misses by {miss:.4e} m")
    assert miss > ROUNDOFF_IDENTITY, (
        "dropping the lever arm changes nothing at the slave, so this test "
        "cannot see the defect §D5 names for `RIGID_LINK_CONSTRAINT`."
    )
    # And the sign matters: transposing the skew is exactly as wrong the other way.
    transposed = np.eye(6)
    transposed[:3, 3:] = skew(d)
    wrong_sign = transposed @ master
    assert float(np.max(np.abs(correct - wrong_sign))) > ROUNDOFF_IDENTITY, (
        "transposing the skew leaves the transfer unchanged, so the sign of the "
        "lever arm is untested."
    )


def test_a_RIGID_LINK_carries_NO_STRAIN_ENERGY_under_a_rigid_body_motion() -> None:
    """The reduced system still has six zero-energy motions.

    A constraint that is truly rigid cannot invent strain energy out of a
    rigid-body motion of the whole model. Reducing by `T` and then applying the
    six global rigid-body vectors of the retained set is the check, and it is the
    property F3's joints are expressed in.
    """
    section = _tube(0.4, 0.010)
    nodes = NodeSet()
    for x, y, z in ((0.0, 0.0, 0.0), (4.0, 0.0, 0.0), (8.0, 0.0, 0.0), (8.0, 1.5, 0.6)):
        nodes.add(Node(x=x, y=y, z=z))
    model = Model(nodes=nodes)
    els = [
        BeamElement(node_a=0, node_b=1, section=section, material=STEEL),
        BeamElement(node_a=1, node_b=2, section=section, material=STEEL),
    ]
    k = assemble_dense(model, els)

    # Node 3 is rigidly linked to node 2.
    offset = model.nodes[3].xyz - model.nodes[2].xyz
    t = constraint_transform(model.n_dof, {3: (2, offset)})
    reduced = reduce_matrix(k, t)

    # The six rigid-body vectors of the RETAINED nodes, about the origin.
    retained_xyz = np.array([model.nodes[i].xyz for i in (0, 1, 2)])
    n_retained = 18
    modes = np.zeros((n_retained, 6), dtype=np.float64)
    for i in range(3):
        base = 6 * i
        for axis in range(3):
            modes[base + axis, axis] = 1.0
        for axis in range(3):
            unit = np.zeros(3)
            unit[axis] = 1.0
            modes[base : base + 3, 3 + axis] = np.cross(unit, retained_xyz[i])
            modes[base + 3 + axis, 3 + axis] = 1.0

    scale = float(np.max(np.abs(reduced)))
    for j in range(6):
        v = modes[:, j]
        energy = abs(float(v @ reduced @ v)) / (scale * float(v @ v))
        assert energy <= ROUNDOFF_IDENTITY, (
            f"rigid-body mode {j} of the link-reduced system carries "
            f"{energy:.4e} of normalised strain energy, over "
            f"{ROUNDOFF_IDENTITY:g}. A rigid link that resists a rigid-body "
            "motion has the wrong lever arm or the wrong sign."
        )


def test_a_MOMENT_through_the_link_equals_FORCE_times_LEVER_ARM(capsys) -> None:
    """The static side of the same statement, and the one a sign error shows in.

    A force applied at the slave becomes, at the master, that force plus the
    moment `d x F`. `T^T` is what carries loads, so this reads `T^T` rather than
    `T` -- and the two are not the same test: a transposed skew passes the
    kinematic check on the wrong component and fails here, or the reverse.
    """
    offset = np.array([0.7, -1.3, 2.9])
    force = np.array([120.0, -45.0, 310.0])
    slave_load = np.concatenate([force, np.zeros(3)])

    block = rigid_link_block(offset)
    at_master = block.T @ slave_load
    want_moment = np.cross(offset, force)

    worst_force = float(np.max(np.abs(at_master[:3] - force)))
    worst_moment = float(np.max(np.abs(at_master[3:] - want_moment)))
    reference = max(float(np.max(np.abs(force))), float(np.max(np.abs(want_moment))))
    with capsys.disabled():
        print(
            f"\n  force through the link {worst_force / reference:.3e}, "
            f"moment d x F {worst_moment / reference:.3e}"
        )
    assert (
        worst_force / reference <= ROUNDOFF_IDENTITY
    ), f"the force is not carried through the link unchanged; miss {worst_force:.4e} N."
    assert worst_moment / reference <= ROUNDOFF_IDENTITY, (
        f"the moment at the master is not `d x F`; miss {worst_moment:.4e} N m. "
        f"got {at_master[3:]}, want {want_moment}"
    )


def test_a_CHAINED_link_is_refused_rather_than_resolved() -> None:
    """A slave that is also a master needs an ordering rule, and none is guessed."""
    with pytest.raises(ValueError, match="both a master and a slave"):
        constraint_transform(24, {1: (0, np.zeros(3)), 2: (1, np.zeros(3))})


def test_the_RELEASE_and_the_LINK_compose_on_a_real_member(capsys) -> None:
    """Both constraints on one element, in global axes, and the member still weighs
    what it weighs.

    V2.6's two halves are usually tested apart. F3's joints apply both at once --
    a braced member pinned at a gimbal and offset from the node the joint is
    defined at -- so the composition is what has to hold, and the invariant that
    survives both is the member's rigid-body mass.
    """
    section = _tube(0.4, 0.010)
    nodes = NodeSet()
    nodes.add(Node(x=0.0, y=0.0, z=0.0))
    nodes.add(Node(x=3.0, y=1.0, z=-2.0))
    model = Model(nodes=nodes)
    e = BeamElement(node_a=0, node_b=1, section=section, material=STEEL)
    length = element_length(model, e)

    k_local = local_stiffness(section, STEEL, length)
    m_local = local_mass(section, STEEL, length)
    released = gimbal_release("b", "x")
    recovery = recovery_matrix(k_local, released)
    k_rel = condense(k_local, recovery)
    m_rel = condense(m_local, recovery)

    r = rotation_matrix(model.nodes[0].xyz, model.nodes[1].xyz)
    t = transformation(r)
    m_global = t.T @ m_rel @ t
    k_global = t.T @ k_rel @ t

    mass_want = STEEL.rho * section.A * length
    worst = 0.0
    for axis in range(3):
        v = np.zeros(12)
        v[axis] = 1.0
        v[6 + axis] = 1.0
        worst = max(worst, abs(float(v @ m_global @ v) - mass_want) / mass_want)
    with capsys.disabled():
        print(f"\n  released and transformed: mass error {worst:.3e}, L={length:.6f} m")
    assert worst <= ROUNDOFF_IDENTITY, (
        f"after a gimbal release and a transformation to global axes the member's "
        f"mass is wrong by {worst:.4e} relative."
    )

    # And the release survives the transformation: the freed rotations still
    # transmit nothing, now in global axes, which is where a wrong transformation
    # of a released element would show.
    scale = float(np.max(np.abs(k_global)))
    freed_global = t.T @ np.eye(12)[:, list(released)]
    energy = float(np.max(np.abs(freed_global.T @ k_global))) / scale
    assert energy <= ROUNDOFF_IDENTITY, (
        f"the released directions transmit {energy:.4e} of max|k| after the "
        "transformation to global axes, so the release and the rotation do not "
        "commute the way they must."
    )


@pytest.mark.parametrize("length", [1.0, 4.0, 60.0])
def test_the_GLOBAL_assembly_path_agrees_with_the_local_one(length: float) -> None:
    """A guard on the composition above: `element_global_stiffness` unchanged.

    The release path builds its own global matrix, so this asserts the shipped
    assembly still produces the same thing for an UNRELEASED member -- otherwise
    a change to `to_global` could silently move only one of the two.
    """
    section = _tube(0.4, 0.010)
    nodes = NodeSet()
    nodes.add(Node(x=0.0, y=0.0, z=0.0))
    nodes.add(Node(x=length, y=0.0, z=0.0))
    model = Model(nodes=nodes)
    e = BeamElement(node_a=0, node_b=1, section=section, material=STEEL)

    shipped = element_global_stiffness(model, e)
    r = rotation_matrix(model.nodes[0].xyz, model.nodes[1].xyz)
    t = transformation(r)
    by_hand = t.T @ local_stiffness(section, STEEL, length) @ t
    worst = float(np.max(np.abs(shipped - by_hand))) / float(np.max(np.abs(shipped)))
    assert worst <= ROUNDOFF_IDENTITY, (
        f"L={length}: the shipped global assembly and the explicit "
        f"`T^T k T` differ by {worst:.4e}."
    )
