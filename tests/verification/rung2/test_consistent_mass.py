"""V2.5 -- the consistent mass matrix (D2 step 10; gate G2.4 in part).

WHAT IS ASSERTED HERE, AND WHAT IS HELD
---------------------------------------
Asserted:

* the ``Phi -> 0`` limit of the derived bending mass equals an independently
  transcribed Euler-Bernoulli consistent mass, at round-off;
* all six rigid-body inertias of one element are exact -- translational mass,
  polar inertia about the member axis, and the rotary inertia in each bending
  plane;
* at model level, ``Phi^T M Phi`` over the six global rigid-body vectors equals
  the analytic mass and inertia tensor of the same members, built from the
  members' own closed-form properties rather than from the matrix under test;
* each softening mechanism LOWERS the free-free frequency, in the order the
  physics requires.

**HELD: G2.4's one-sided band, and `FREE_FREE_FREQUENCY` with it.** The plan
pre-registers (AO4, §141)::

    0 <= (f_computed - f_exact) / f_exact <= FREE_FREE_FREQUENCY

against a *cited closed form* (Q1b), and the cited closed form for a free-free
beam is the Euler-Bernoulli frequency ``(beta L)^2 / (2 pi L^2) sqrt(EI/rho A)``
with ``cos(beta L) cosh(beta L) = 1``. **That reference is a different continuum
from the element.** Rayleigh-Ritz bounds a discretisation against the continuum
it discretises; it says nothing about a continuum that neglects rotary inertia
and shear flexibility when the element includes both. The measurement is in
`test_the_three_SOFTENING_MECHANISMS_are_ordered_as_the_physics_requires` below
and the finding is in the step report: the band is violated on the low side by a
**mesh-independent** offset, which is a modelling difference and not a
discretisation error, so refinement does not remove it and no tolerance value
can absorb it without becoming a fudge factor.

Nothing here widens, skips or xfails anything to get past that. The band is not
implemented, `FREE_FREE_FREQUENCY` is not created, and the decision is the
technical supervisor's.

Reference
---------
Free-free frequency equation ``cos(x) cosh(x) = 1`` -- Blevins, *Formulas for
Natural Frequency and Mode Shape*, Table 8-1; Timoshenko, *Vibration Problems in
Engineering*, §5. **The roots are SOLVED here rather than transcribed**, and the
transcribed table values are asserted against the solve, so a mistyped digit in
a reference table cannot become the reference.
"""

from __future__ import annotations

import numpy as np
import pytest
import scipy.linalg as sla

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import (  # noqa: E402
    BeamElement,
    assemble_dense,
    assemble_mass_dense,
    element_length,
)
from floatfea.element.beam import (  # noqa: E402
    bending_mass,
    euler_bernoulli_bending_mass,
    local_mass,
)
from floatfea.element.transform import rotation_matrix  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node, NodeSet  # noqa: E402
from floatfea.tolerances import ROUNDOFF_IDENTITY  # noqa: E402

RIGID = 6

STEEL = Material(E=2.1e11, nu=0.3, rho=7850.0, fy=355.0e6, name="S355")


def _tube(d_outer: float, t: float) -> Section:
    """A circular tube, with `J` from the basis rather than assumed `2 I`."""
    inertia = basis.tube_second_moment(d_outer, t)
    return Section(
        A=basis.tube_area(d_outer, t),
        I_y=inertia,
        I_z=inertia,
        J=basis.torsion_constant("thin_tube", inertia, inertia),
        shape="thin_tube",
    )


def _straight(length: float, n_el: int, section: Section) -> tuple[Model, list[BeamElement]]:
    """A straight beam along global x, `n_el` equal elements."""
    nodes = NodeSet()
    for x in np.linspace(0.0, length, n_el + 1):
        nodes.add(Node(x=float(x), y=0.0, z=0.0))
    model = Model(nodes=nodes)
    els = [
        BeamElement(node_a=i, node_b=i + 1, section=section, material=STEEL) for i in range(n_el)
    ]
    return model, els


def _skew_frame(section: Section) -> tuple[Model, list[BeamElement]]:
    """Four members, none axis-aligned, so the transformation is exercised.

    A straight beam along x cannot see a rotation error in the element-to-global
    map, which is the same reason V2.4 exists. The mass check below runs on this
    as well as on the straight beam.
    """
    coords = [
        (0.0, 0.0, 0.0),
        (3.1, 0.7, -1.2),
        (5.9, 2.3, 0.8),
        (2.0, 4.1, 2.7),
        (-1.3, 2.9, 1.1),
    ]
    nodes = NodeSet()
    for x, y, z in coords:
        nodes.add(Node(x=x, y=y, z=z))
    model = Model(nodes=nodes)
    els = [
        BeamElement(node_a=a, node_b=b, section=section, material=STEEL)
        for a, b in ((0, 1), (1, 2), (2, 3), (3, 4))
    ]
    return model, els


def _analytic_rigid_inertia(model: Model, els: list[BeamElement], about: np.ndarray) -> np.ndarray:
    """The 6x6 rigid-body mass and inertia of the SAME members, in closed form.

    Built from each member's own analytic properties and the parallel-axis
    theorem, never from the matrix under test. In the member's local axes, about
    its own midpoint::

        I_xx = rho (I_y + I_z) L        the cross-section's polar inertia
        I_yy = rho (A L^3 / 12 + I_y L) slender rod plus its own rotary inertia
        I_zz = rho (A L^3 / 12 + I_z L)

    Ordering matches the rigid-body vector ordering: three translations then
    three rotations about `about`.
    """
    total = np.zeros((RIGID, RIGID), dtype=np.float64)
    for e in els:
        a = model.nodes[e.node_a].xyz
        b = model.nodes[e.node_b].xyz
        length = element_length(model, e)
        mass = e.material.rho * e.section.A * length
        centre = 0.5 * (a + b)
        rho = e.material.rho
        i_local = np.diag(
            [
                rho * (e.section.I_y + e.section.I_z) * length,
                rho * (e.section.A * length**3 / 12.0 + e.section.I_y * length),
                rho * (e.section.A * length**3 / 12.0 + e.section.I_z * length),
            ]
        )
        r = rotation_matrix(a, b, orientation_node=e.orientation_node, roll_rad=e.roll_rad)
        triad = r[:3, :3]
        i_global = triad.T @ i_local @ triad

        d = centre - about
        # Parallel axis: I += m (|d|^2 I_3 - d d^T).
        i_global = i_global + mass * (float(d @ d) * np.eye(3) - np.outer(d, d))

        total[:3, :3] += mass * np.eye(3)
        # The coupling block: a rotation about `about` translates the member's
        # centre of mass by `theta x d`, so the off-diagonal is `-m [d]_x`.
        dx = np.array([[0.0, -d[2], d[1]], [d[2], 0.0, -d[0]], [-d[1], d[0], 0.0]])
        total[:3, 3:] += -mass * dx
        total[3:, :3] += (-mass * dx).T
        total[3:, 3:] += i_global
    return total


def _model_rigid_vectors(model: Model, about: np.ndarray) -> np.ndarray:
    """`(n_dof, 6)` rigid-body vectors about an EXPLICIT point.

    `_analytic_rigid_body` fixes the centroid on purpose, because G2.1's
    residual is not invariant under the point. `Phi^T M Phi` IS a physical
    object at whatever point it is taken about, so the point is a parameter
    here and two different points are checked -- if it were ignored, the
    parallel-axis term would go untested.
    """
    xyz = model.nodes.coords()
    n = model.nodes.n_dof
    modes = np.zeros((n, RIGID), dtype=np.float64)
    for i in range(xyz.shape[0]):
        base = 6 * i
        d = xyz[i] - about
        for axis in range(3):
            modes[base + axis, axis] = 1.0
        for axis in range(3):
            unit = np.zeros(3)
            unit[axis] = 1.0
            modes[base : base + 3, 3 + axis] = np.cross(unit, d)
            modes[base + 3 + axis, 3 + axis] = 1.0
    return modes


# --------------------------------------------------------------------------
# The Euler-Bernoulli limit
# --------------------------------------------------------------------------


@pytest.mark.parametrize("length", [0.5, 1.0, 3.7, 40.0, 1.0e3])
def test_the_PHI_ZERO_limit_reproduces_the_TRANSCRIBED_mass_matrix(length: float) -> None:
    """`bending_mass(rho A, 0, L, 0)` against the transcribed classical 4x4.

    The derived interpolation is checked against a matrix nobody derived: the
    420-denominator Euler-Bernoulli consistent mass, transcribed from the
    source in `beam.py`. It is not `bending_mass(..., phi=0)` by another route,
    which is the fourteenth guard's failure shape.
    """
    got = bending_mass(2.5, 0.0, length, 0.0)
    want = euler_bernoulli_bending_mass(2.5, length)
    scale = float(np.max(np.abs(want)))
    worst = float(np.max(np.abs(got - want))) / scale
    assert worst <= ROUNDOFF_IDENTITY, (
        f"L={length}: the derived interpolation does not reduce to the classical "
        f"Euler-Bernoulli consistent mass at Phi=0; worst relative difference "
        f"{worst:.4e} against {ROUNDOFF_IDENTITY:g}. Either the shape functions "
        "are wrong or the quadrature is not exact for this integrand."
    )


def test_a_LUMPED_MASS_fails_the_euler_bernoulli_limit(capsys) -> None:
    """The counter the plan names for G2.4: lumped mass for consistent.

    A defect that a comparison against the classical matrix must catch, and the
    size is not a tolerance -- the lumped matrix is a different matrix, so the
    difference is O(1). Recorded with its number so "it is caught" is a
    measurement.
    """
    length = 3.7
    rho_a = 2.5
    lumped = np.diag([rho_a * length / 2.0, 0.0, rho_a * length / 2.0, 0.0])
    want = euler_bernoulli_bending_mass(rho_a, length)
    worst = float(np.max(np.abs(lumped - want))) / float(np.max(np.abs(want)))
    with capsys.disabled():
        print(f"\n  lumped against consistent: {worst:.4f} relative, ceiling {ROUNDOFF_IDENTITY:g}")
    assert worst > ROUNDOFF_IDENTITY, (
        "a lumped mass matrix passes the Euler-Bernoulli limit check, so that "
        "check cannot distinguish consistent from lumped -- which is the one "
        "defect the plan names for this gate."
    )


# --------------------------------------------------------------------------
# The six rigid-body inertias, per element
# --------------------------------------------------------------------------


@pytest.mark.parametrize("length", [0.5, 4.0, 100.0])
@pytest.mark.parametrize("dims", [(0.6, 0.012), (0.3, 0.008)])
def test_the_six_RIGID_BODY_inertias_of_ONE_ELEMENT_are_exact(
    length: float, dims: tuple[float, float]
) -> None:
    """Exact in exact arithmetic, so asserted at round-off.

    This is what F4's inertia relief reads: a mass matrix whose rigid-body
    content is right to round-off can be trusted to produce an inertial load
    that equilibrates, and one that is merely close cannot.
    """
    section = _tube(*dims)
    m = local_mass(section, STEEL, length)
    rho, area = STEEL.rho, section.A
    half = length / 2.0

    cases: list[tuple[str, np.ndarray, float]] = []
    for axis, label in ((0, "u_x"), (1, "u_y"), (2, "u_z")):
        v = np.zeros(12)
        v[axis] = 1.0
        v[6 + axis] = 1.0
        cases.append((f"translation {label}", v, rho * area * length))

    twist = np.zeros(12)
    twist[3] = 1.0
    twist[9] = 1.0
    cases.append(("twist about the member axis", twist, rho * (section.I_y + section.I_z) * length))

    # Rotation about local z: v(x) = theta (x - L/2), with the sign convention
    # `dv/dx = +r_z` that `bending_stiffness` uses.
    rz = np.zeros(12)
    rz[1], rz[5], rz[7], rz[11] = -half, 1.0, half, 1.0
    cases.append(
        ("rotation about local z", rz, rho * (area * length**3 / 12.0 + section.I_z * length))
    )

    # Rotation about local y: `dw/dx = -r_y`, which is the flip in `local_mass`.
    ry = np.zeros(12)
    ry[2], ry[4], ry[8], ry[10] = half, 1.0, -half, 1.0
    cases.append(
        ("rotation about local y", ry, rho * (area * length**3 / 12.0 + section.I_y * length))
    )

    for label, v, want in cases:
        got = float(v @ m @ v)
        rel = abs(got - want) / abs(want)
        assert rel <= ROUNDOFF_IDENTITY, (
            f"L={length}, D={dims[0]}: {label} gives {got:.9e} against the "
            f"analytic {want:.9e}, relative {rel:.4e} over {ROUNDOFF_IDENTITY:g}. "
            "A mass matrix whose rigid-body content is wrong cannot produce an "
            "inertial load that equilibrates, which is what F4 reads it for."
        )


# --------------------------------------------------------------------------
# Phi^T M Phi at model level -- V2.5's second half
# --------------------------------------------------------------------------


@pytest.mark.parametrize("about_label", ["origin", "offset"])
@pytest.mark.parametrize("which", ["straight", "skew"])
def test_the_MODEL_rigid_body_block_is_the_ANALYTIC_mass_and_inertia(
    which: str, about_label: str, capsys
) -> None:
    """`Phi^T M Phi` against the closed-form 6x6, assembled and transformed.

    Two reference points, because the parallel-axis and coupling terms vanish
    from the comparison if the point is ignored by both sides; and a skew frame
    as well as a straight beam, because a straight beam along x cannot see an
    error in the element-to-global rotation.
    """
    section = _tube(0.4, 0.010)
    model, els = _straight(12.0, 5, section) if which == "straight" else _skew_frame(section)
    about = np.zeros(3) if about_label == "origin" else np.array([7.3, -2.1, 4.6])

    m = assemble_mass_dense(model, els)
    phi = _model_rigid_vectors(model, about)
    got = phi.T @ m @ phi
    want = _analytic_rigid_inertia(model, els, about)

    scale = float(np.max(np.abs(want)))
    worst = float(np.max(np.abs(got - want))) / scale
    with capsys.disabled():
        print(f"\n  {which}/{about_label}: worst {worst:.4e} of {scale:.4e}")
    assert worst <= ROUNDOFF_IDENTITY, (
        f"{which} frame about {about_label}: the assembled rigid-body block "
        f"differs from the analytic mass and inertia by {worst:.4e} relative, "
        f"against {ROUNDOFF_IDENTITY:g}.\ngot\n{got}\nwant\n{want}"
    )


def test_a_DROPPED_COUPLING_TERM_is_visible_in_the_analytic_comparison(capsys) -> None:
    """The counter for the check above: `RIGID_LINK_CONSTRAINT`'s shape, early.

    The plan's counter for the rigid-link gate is "a lever arm dropped from the
    MPC". The same defect in this comparison is the coupling block ``-m [d]_x``
    dropped from the analytic side, and it has to redden -- otherwise the check
    is only about the diagonal and the reference point is untested.
    """
    section = _tube(0.4, 0.010)
    model, els = _skew_frame(section)
    about = np.array([7.3, -2.1, 4.6])
    want = _analytic_rigid_inertia(model, els, about)
    defective = want.copy()
    defective[:3, 3:] = 0.0
    defective[3:, :3] = 0.0
    got = (
        _model_rigid_vectors(model, about).T
        @ assemble_mass_dense(model, els)
        @ _model_rigid_vectors(model, about)
    )
    worst = float(np.max(np.abs(got - defective))) / float(np.max(np.abs(want)))
    with capsys.disabled():
        print(f"\n  coupling block dropped: {worst:.4e} relative, ceiling {ROUNDOFF_IDENTITY:g}")
    assert worst > ROUNDOFF_IDENTITY, (
        "dropping the mass-coupling block from the analytic side leaves the "
        "comparison green, so the comparison is not reading the reference "
        "point at all."
    )


# --------------------------------------------------------------------------
# Free-free frequencies -- MEASURED, and G2.4's band is HELD
# --------------------------------------------------------------------------


def _free_free_roots(count: int) -> list[float]:
    """Roots of `cos(x) cosh(x) = 1`, SOLVED rather than transcribed.

    `cosh` overflows for large `x`, so the equation is solved in the equivalent
    form `cos(x) - 1/cosh(x) = 0`, which is bounded everywhere.
    """

    def f(x: float) -> float:
        return float(np.cos(x) - 1.0 / np.cosh(x))

    roots: list[float] = []
    x = 3.0
    step = 1.0e-3
    while len(roots) < count:
        if f(x) * f(x + step) < 0.0:
            lo, hi = x, x + step
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if f(lo) * f(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
            x += step
        x += step
    return roots


def test_the_transcribed_BETA_L_table_agrees_with_the_solved_roots() -> None:
    """Q1b's transcription risk, removed rather than accepted.

    The table values are the ones every reference prints. They are checked
    against the solve so a mistyped digit cannot become the reference.
    """
    table = ("4.730040745", "7.853204624", "10.995607838")
    solved = _free_free_roots(len(table))
    for text, got in zip(table, solved, strict=True):
        want = float(text)
        # not-a-tolerance: the printed precision of the transcribed value
        # itself. The table carries the digits a reference book prints, so the
        # strongest statement available is agreement to its OWN last digit --
        # half a unit in the last place written. It is read off the string
        # rather than typed, so no threshold is chosen here: a table quoted to
        # more digits is checked harder automatically.
        decimals = len(text.split(".")[1])
        allowed = 0.5 * 10.0 ** (-decimals)
        assert abs(got - want) <= allowed, (
            f"the transcribed free-free root {text} does not match the solved "
            f"{got:.12f} to its own last printed digit ({allowed:g}). One of the "
            "two is a typo and the solve is the one with no typist in it."
        )


def _bending_frequencies(model: Model, els: list[BeamElement], count: int) -> list[float]:
    """The first `count` DISTINCT flexible frequencies, in Hz.

    The beam is three-dimensional, so bending modes come in degenerate pairs
    when `I_y == I_z`. Taking `w[6:6+count]` would compare the first bending
    frequency against the second analytic root, which reads as a 60% error and
    is nothing of the kind.
    """
    k = assemble_dense(model, els)
    m = assemble_mass_dense(model, els)
    w = np.sqrt(np.clip(sla.eigh(k, m, eigvals_only=True), 0.0, None)) / (2.0 * np.pi)
    out: list[float] = []
    for value in w[RIGID:]:
        if not out or value > out[-1] * (1.0 + 1.0e-6):
            out.append(float(value))
        if len(out) == count:
            break
    return out


def test_the_three_SOFTENING_MECHANISMS_are_ordered_as_the_physics_requires(
    capsys, monkeypatch
) -> None:
    """G2.4's band is HELD, and this is the measurement that holds it.

    Three cells, one variable moved at a time, on the same beam and the same
    meshes. `f_exact` is the classical Euler-Bernoulli value, which neglects
    BOTH rotary inertia and shear flexibility.

      A  Phi = 0, rotary inertia off -- the continuum the reference describes
      B  Phi = 0, rotary inertia on  -- rotary inertia alone
      C  the shipped element          -- rotary inertia and shear

    Cell A is Rayleigh-Ritz and behaves exactly as AO4 pre-registers: every
    error positive, falling by ~16 per mesh halving, which is the fourth order
    a cubic interpolation gives. Cells B and C settle at a NEGATIVE,
    mesh-independent offset, because they discretise a different continuum from
    the reference. That offset is a modelling difference, not a discretisation
    error; refinement does not reduce it and widening a tolerance to cover it
    would be a fudge factor.

    ASSERTED: cell A is positive and converges, and the three cells are ordered
    ``C <= B <= A`` at every mesh -- each softening mechanism lowers the
    frequency. That much is physics and needs no tolerance. The BAND is not
    asserted, `FREE_FREE_FREQUENCY` is not created, and the choice of reference
    is the technical supervisor's.
    """
    import floatfea.element.beam as beam_module

    section = _tube(0.3, 0.008)
    length = 30.0
    inertia = section.I_y
    exact = [
        (root / length) ** 2 / (2.0 * np.pi) * np.sqrt(STEEL.E * inertia / (STEEL.rho * section.A))
        for root in _free_free_roots(3)
    ]

    real_phi = beam_module.shear_parameter
    real_bending_mass = beam_module.bending_mass

    def run(no_phi: bool, no_rotary: bool, n_el: int) -> list[float]:
        with monkeypatch.context() as patch:
            if no_phi:
                patch.setattr(beam_module, "shear_parameter", lambda *a, **k: 0.0)
            if no_rotary:
                patch.setattr(
                    beam_module,
                    "bending_mass",
                    lambda rho_a, rho_i, ll, phi: real_bending_mass(rho_a, 0.0, ll, phi),
                )
            model, els = _straight(length, n_el, section)
            return _bending_frequencies(model, els, 3)

    assert beam_module.shear_parameter is real_phi

    meshes = (4, 8, 16, 32)
    cells = {
        "A matched continuum": (True, True),
        "B rotary only": (True, False),
        "C shipped": (False, False),
    }
    measured: dict[str, dict[int, list[float]]] = {}
    with capsys.disabled():
        print(f"\n  free-free beam, L/r = {length / basis.tube_radius_of_gyration(0.3, 0.008):.1f}")
        print("  relative error against the Euler-Bernoulli analytic reference:")
        for label, (no_phi, no_rotary) in cells.items():
            measured[label] = {}
            for n_el in meshes:
                got = run(no_phi, no_rotary, n_el)
                measured[label][n_el] = got
                rel = [(g - e) / e for g, e in zip(got, exact, strict=True)]
                print(f"    {label:22s} n={n_el:3d}  " + "  ".join(f"{r:+.4e}" for r in rel))

    # Cell A: AO4's sign, and fourth-order convergence.
    for n_el in meshes:
        for got, want in zip(measured["A matched continuum"][n_el], exact, strict=True):
            assert got >= want, (
                f"n={n_el}: the MATCHED pair gives {got:.9e} below the analytic "
                f"{want:.9e}. Rayleigh-Ritz forbids that for a conforming "
                "displacement element on the continuum it discretises, so "
                "either the mass matrix or the stiffness is wrong."
            )
    coarse = (measured["A matched continuum"][8][0] - exact[0]) / exact[0]
    fine = (measured["A matched continuum"][16][0] - exact[0]) / exact[0]
    assert fine < coarse / 8.0, (
        f"halving the mesh reduced the matched-pair error only from {coarse:.4e} "
        f"to {fine:.4e}. A cubic interpolation gives fourth order, so a factor "
        "below 8 says the convergence is not what the interpolation implies."
    )

    # The ordering. Each softening mechanism lowers the frequency.
    for n_el in meshes:
        a = measured["A matched continuum"][n_el]
        b = measured["B rotary only"][n_el]
        c = measured["C shipped"][n_el]
        for i, (fa, fb, fc) in enumerate(zip(a, b, c, strict=True)):
            assert fb <= fa, (
                f"n={n_el}, mode {i + 1}: adding rotary inertia RAISED the "
                f"frequency, {fa:.9e} -> {fb:.9e}. Adding inertia cannot raise "
                "a frequency, so the rotary term is entering with the wrong sign."
            )
            assert fc <= fb, (
                f"n={n_el}, mode {i + 1}: adding shear flexibility RAISED the "
                f"frequency, {fb:.9e} -> {fc:.9e}. Adding flexibility cannot "
                "raise a frequency."
            )

    # And the offset is mesh-independent, which is what makes it a modelling
    # difference rather than something refinement would remove.
    offsets = [(measured["C shipped"][n_el][0] - exact[0]) / exact[0] for n_el in (16, 32)]
    assert offsets[0] < 0.0 and abs(offsets[1] - offsets[0]) < 0.1 * abs(offsets[0]), (
        f"the shipped element's offset from the reference moved from "
        f"{offsets[0]:.4e} to {offsets[1]:.4e} between two meshes. If it is "
        "mesh-dependent it is a discretisation error after all, and the "
        "finding in the step report is wrong."
    )
