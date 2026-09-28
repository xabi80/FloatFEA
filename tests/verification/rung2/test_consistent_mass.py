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
pre-registered (AO4, §141)::

    0 <= (f_computed - f_exact) / f_exact <= FREE_FREE_FREQUENCY

against a *cited closed form* (Q1b), and the cited closed form for a free-free
beam is the Euler-Bernoulli frequency ``(beta L)^2 / (2 pi L^2) sqrt(EI/rho A)``
with ``cos(beta L) cosh(beta L) = 1``. **That reference is a different continuum
from the element.** Rayleigh-Ritz bounds a discretisation against the continuum
it discretises; it says nothing about a continuum that neglects rotary inertia
and shear flexibility when the element includes both.

DL0 answered that by referencing the element's own theory instead, on the
pinned-pinned case where the Timoshenko frequency equation is a closed-form
quadratic in ``omega^2``. **That reference is shipped and verified here.** DL1
time-boxed the band to one commit with a pre-registered fallback, and **the
fallback is what was taken.** Two reasons, both measured below:

1. The band needs a window on a convergence-order ratio, which is a tolerance by
   `CLAUDE.md`'s own definition. A lower bound's counter widens DOWNWARD, and
   `tests/test_counters_are_injected.py` computes every widened ceiling as
   ``WIDEN * ceiling``. Registering a lower-bound counter there means extending
   that guard, and CZ0 freezes apparatus through F6. The measured ratios are in
   the step report, so the band is one line to adopt when 4a is unfrozen.
2. **THIS REASON WAS A DEFECT IN THE ELEMENT AND IS WITHDRAWN (R541).** It read:
   the shipped element's frequencies are not monotone under refinement in either
   boundary condition, because ``Phi`` is computed from the element length so the
   interpolation spaces are not nested. **The sign of the shear term in
   `bending_interpolation` was wrong**, and with it corrected the largest rise in
   any frequency under refinement is ``0.000e+00`` in both boundary conditions --
   where the published figures were ``1.476e-04`` and ``7.924e-05``. The spaces
   ARE nested: the field family is ``{th in P2, w' = th - c th''}`` with
   ``c = EI/(kappa G A)``, a length-independent constant, and ``Phi = 12c/L^2`` is
   only its dimensionless rendering.

   **So the sign half of DL0's band ships**, and it is asserted in
   `test_the_SHIPPED_element_approaches_its_OWN_continuum` over the whole range
   that test prints.

**WHAT IS STILL NOT ASSERTED: the ORDER half of the band, DL0's [12, 20] window
on the convergence ratio.** DN0 time-boxed that to one hypothesis with a
pre-registered branch, and the hypothesis was refuted:

* **round-off floor** -- the discretisation error at ``n = 16`` is ``1.95e-06``
  against a floor ``0.5 * eps * lambda_max/lambda_1`` of ``1.93e-10``, four orders
  below it, while the ratio has already sagged to ``10.31``. The floor does become
  comparable at ``n = 128`` (``1.28e-08`` against an error of ``1.41e-08``), so it
  explains the finest meshes and not the sag;
* **rotary inertia** (the ``N_theta`` interpolation being one order lower than
  ``N_w``) -- refuted outright: with rotary inertia off against its own closed
  form the ratios are ``13.63, 10.31, 6.62, 4.47``, identical to four figures.

The residual signature is a weaker ``h^2`` term taking over from a dominant
``h^4`` one, and it is not identified. **Per DN0's second branch the order
question goes to F3 with these two cells as its starting point**, and no band is
asserted on it here.

Nothing here widens, skips or xfails anything. `FREE_FREE_FREQUENCY` is not
created. What is asserted needs no tolerance at all beyond `ROUNDOFF_IDENTITY`.

References
----------
Free-free frequency equation ``cos(x) cosh(x) = 1`` -- Blevins, *Formulas for
Natural Frequency and Mode Shape*, Table 8-1; Timoshenko, *Vibration Problems in
Engineering*, §5. **The roots are SOLVED here rather than transcribed**, and the
transcribed table values are asserted against the solve, so a mistyped digit in
a reference table cannot become the reference.

Timoshenko pinned-pinned frequencies -- Han, Benaroya & Wei, "Dynamics of
transversely vibrating beams using four engineering theories", *Journal of Sound
and Vibration* 225(5) 935-988 (1999), §5 and Table 4; Timoshenko, *Vibration
Problems in Engineering*, §2.15. For simple supports the mode shapes
``w = W sin(beta x)``, ``psi = Psi cos(beta x)`` with ``beta = n pi / L`` satisfy
the boundary conditions exactly, so the two coupled equations of motion collapse
to a quadratic in ``omega^2``::

    rho A rho I omega^4
      - (rho A E I beta^2 + rho A kappa G A + kappa G A rho I beta^2) omega^2
      + kappa G A E I beta^4                                          = 0

with the FLEXURAL branch the smaller root. **The transcription is verified by its
two limits rather than trusted** -- see
`test_the_TIMOSHENKO_reference_reduces_to_ITS_TWO_LIMITS`.
"""

from __future__ import annotations

import numpy as np
import pytest
import scipy.linalg as sla
from numpy.typing import NDArray

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import (  # noqa: E402
    BeamElement,
    assemble_dense,
    assemble_mass_dense,
    element_length,
)
from floatfea.element.beam import (  # noqa: E402
    bending_interpolation,
    bending_mass,
    bending_stiffness,
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
    asserted and `FREE_FREE_FREQUENCY` is not created.

    THERE ARE TWO SEPARATE REASONS THE BAND CANNOT BE ASSERTED and this test
    carries only the first. This one is about the REFERENCE: it describes a
    continuum the element does not discretise, so the offset is a modelling
    difference. The second is about the ELEMENT: its interpolation space is
    mesh-dependent, so it has no monotone approach from above to ANY reference,
    which is
    `test_the_MESH_DEPENDENT_interpolation_space_is_what_BREAKS_monotonicity`.
    Fixing the reference, as DL0 did for the pinned-pinned case, removes the
    first and not the second.
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


# --------------------------------------------------------------------------
# The Timoshenko pinned-pinned reference (DL0), and what replaced the band (DL1)
# --------------------------------------------------------------------------


def euler_bernoulli_pinned_pinned(
    mode: int, length: float, section: Section, material: Material, inertia: float
) -> float:
    """`omega^2 = E I beta^4 / (rho A)`, written INDEPENDENTLY of the quadratic.

    The classical simply-supported beam frequency. Transcribed, not derived from
    the Timoshenko form, for the same reason `euler_bernoulli_bending_mass` is.
    """
    beta = mode * np.pi / length
    omega_sq = material.E * inertia * beta**4 / (material.rho * section.A)
    return float(np.sqrt(omega_sq) / (2.0 * np.pi))


def rayleigh_pinned_pinned(
    mode: int, length: float, section: Section, material: Material, inertia: float
) -> float:
    """`omega^2 = E I beta^4 / (rho A + rho I beta^2)` -- rotary inertia, no shear.

    The Rayleigh beam. Also written independently; it is the second of the two
    limits the Timoshenko transcription is checked against.
    """
    beta = mode * np.pi / length
    denominator = material.rho * section.A + material.rho * inertia * beta**2
    omega_sq = material.E * inertia * beta**4 / denominator
    return float(np.sqrt(omega_sq) / (2.0 * np.pi))


def timoshenko_pinned_pinned(
    mode: int,
    length: float,
    section: Section,
    material: Material,
    inertia: float,
    *,
    rotary_factor: float = 1.0,
    shear_factor: float = 1.0,
    stable_root: bool = True,
) -> float:
    """The EXACT Timoshenko pinned-pinned frequency, flexural branch, in Hz.

    Han, Benaroya & Wei (1999) §5; the quadratic is written out in the module
    docstring. `rotary_factor` and `shear_factor` scale `rho I` and `kappa G A`
    and exist ONLY so the two limits can be taken by the test below -- they are
    both 1.0 in every other call.

    THE SMALLER ROOT IS TAKEN AS `2c / (-b + sqrt(disc))`, NOT `(-b - sqrt(disc))
    / (2a)`, and the difference is measured rather than asserted. For a slender
    beam ``b^2 >> 4ac``, so `-b - sqrt(disc)` subtracts two numbers that agree to
    seven digits and throws away the precision the reference is supposed to
    supply. At the first mode of the shipped case the two branches differ by
    3.7e-10 relative -- small, and large enough to matter when the quantity being
    compared against it converges to 1e-8.

    not-a-tolerance: `rotary_factor` and `shear_factor` are inputs that switch
    between three named beam theories. Nothing is compared against either.
    """
    beta = mode * np.pi / length
    rho_a = material.rho * section.A
    rho_i = material.rho * inertia * rotary_factor
    ei = material.E * inertia
    kga = section.kappa(material) * material.G * section.A * shear_factor

    a = rho_a * rho_i
    b = -(rho_a * ei * beta**2 + rho_a * kga + kga * rho_i * beta**2)
    c = kga * ei * beta**4
    disc = np.sqrt(b * b - 4.0 * a * c)
    omega_sq = (2.0 * c / (-b + disc)) if stable_root else ((-b - disc) / (2.0 * a))
    return float(np.sqrt(omega_sq) / (2.0 * np.pi))


def _pinned_pinned_frequencies(
    length: float, n_el: int, section: Section, count: int, plane: str
) -> list[float]:
    """Bending frequencies of a pinned-pinned beam, ONE plane at a time.

    Pinned means the translation is held and the bending rotation is free, which
    is `M = 0` at each end -- exactly the condition the analytic mode shape
    satisfies. Every DOF outside the chosen bending plane is held, including the
    axial one, so mode identification is unambiguous: taking the three smallest
    eigenvalues of a fully three-dimensional model would pick up the second
    bending plane and read the first mode against the second analytic root,
    which is a 60% error and nothing of the kind.
    """
    nodes = NodeSet()
    for x in np.linspace(0.0, length, n_el + 1):
        nodes.add(Node(x=float(x), y=0.0, z=0.0))
    model = Model(nodes=nodes)
    els = [
        BeamElement(node_a=i, node_b=i + 1, section=section, material=STEEL) for i in range(n_el)
    ]
    k = assemble_dense(model, els)
    m = assemble_mass_dense(model, els)

    n_nodes = n_el + 1
    free: list[int] = []
    for i in range(n_nodes):
        base = 6 * i
        if plane == "xy":
            if 0 < i < n_nodes - 1:
                free.append(base + 1)  # u_y, interior only
            free.append(base + 5)  # r_z, every node
        else:
            if 0 < i < n_nodes - 1:
                free.append(base + 2)  # u_z, interior only
            free.append(base + 4)  # r_y, every node
    index = np.array(free)
    w = np.sqrt(
        np.clip(
            sla.eigh(k[np.ix_(index, index)], m[np.ix_(index, index)], eigvals_only=True), 0.0, None
        )
    ) / (2.0 * np.pi)
    return [float(v) for v in w[:count]]


@pytest.mark.parametrize("mode", [1, 2, 3])
def test_the_TIMOSHENKO_reference_reduces_to_ITS_TWO_LIMITS(mode: int, capsys) -> None:
    """DL0's independent verification of the transcription.

    A frequency equation copied from a paper is a transcription, and this
    repository's answer to a transcription is not to trust it. Two limits, each
    against a closed form written separately in this file:

      rotary -> 0 and shear -> infinity   =>  Euler-Bernoulli
      shear  -> infinity                  =>  Rayleigh

    If a term were dropped or a sign flipped, at least one limit moves.
    """
    section = _tube(0.3, 0.008)
    length = 30.0
    inertia = section.I_y
    big = 1.0e12
    small = 1.0e-12

    got_eb = timoshenko_pinned_pinned(
        mode, length, section, STEEL, inertia, rotary_factor=small, shear_factor=big
    )
    want_eb = euler_bernoulli_pinned_pinned(mode, length, section, STEEL, inertia)
    got_rayleigh = timoshenko_pinned_pinned(mode, length, section, STEEL, inertia, shear_factor=big)
    want_rayleigh = rayleigh_pinned_pinned(mode, length, section, STEEL, inertia)

    naive = timoshenko_pinned_pinned(mode, length, section, STEEL, inertia, stable_root=False)
    stable = timoshenko_pinned_pinned(mode, length, section, STEEL, inertia)
    with capsys.disabled():
        print(
            f"\n  mode {mode}: EB limit {abs(got_eb - want_eb) / want_eb:.3e}, "
            f"Rayleigh limit {abs(got_rayleigh - want_rayleigh) / want_rayleigh:.3e}, "
            f"root branches differ by {abs(stable - naive) / stable:.3e}"
        )

    for label, got, want in (
        ("Euler-Bernoulli", got_eb, want_eb),
        ("Rayleigh", got_rayleigh, want_rayleigh),
    ):
        rel = abs(got - want) / want
        assert rel <= ROUNDOFF_IDENTITY, (
            f"mode {mode}: the Timoshenko quadratic does not reduce to the "
            f"{label} closed form in its own limit -- {got:.12f} against "
            f"{want:.12f}, relative {rel:.4e} over {ROUNDOFF_IDENTITY:g}. The "
            "transcription has a wrong term or a wrong sign."
        )


def test_the_frequency_sequence_is_MONOTONE_under_refinement(capsys, monkeypatch) -> None:
    """Rayleigh-Ritz on nested subspaces: no frequency may RISE when the mesh is
    refined, in either boundary condition, with `Phi` on or off.

    THIS TEST WAS NAMED `..._MESH_DEPENDENT_interpolation_space_is_what_BREAKS_
    monotonicity` AND IT MEASURED A DEFECT (R541). The shipped element did
    produce rises -- `1.476e-04` free-free and `7.924e-05` pinned-pinned, both at
    n=64 -- and the conclusion drawn from them, that `Phi`'s dependence on the
    element length makes the spaces non-nested, was wrong. The spaces are nested;
    the shear term's sign was not. The old body asserted only the `Phi = 0` half
    and REPORTED the shipped half, "because asserting that a defect is present
    would redden the day it was fixed" -- which is exactly what a report of a
    defect should do, and is why the assertion now covers both.

    cell  ONE VARIABLE: `Phi`. Same beam, same meshes, same eigensolver, both
          boundary conditions, and now both halves asserted at zero rises.
    """
    import floatfea.element.beam as beam_module

    section = _tube(0.3, 0.008)
    length = 30.0
    meshes = (4, 8, 16, 32, 64)

    def sequences(no_phi: bool) -> dict[str, list[list[float]]]:
        # C17: ONE VARIABLE, AND IT USED TO BE TWO. The `Phi = 0` leg also
        # rewrote `bending_mass` to pass `rho_i = 0.0`, so it had no rotary
        # inertia either and the cell did not isolate what it said it did. BG0
        # asks for one variable moved; rotary inertia is now on in both legs.
        out: dict[str, list[list[float]]] = {}
        with monkeypatch.context() as patch:
            if no_phi:
                patch.setattr(beam_module, "shear_parameter", lambda *a, **k: 0.0)
            out["free-free"] = [
                _bending_frequencies(*_straight(length, n_el, section), 3) for n_el in meshes
            ]
            out["pinned-pinned"] = [
                _pinned_pinned_frequencies(length, n_el, section, 3, "xy") for n_el in meshes
            ]
        return out

    def worst_rise(rows: list[list[float]]) -> tuple[float, int, int]:
        worst, at_mesh, at_mode = 0.0, 0, 0
        for i in range(len(rows) - 1):
            for mode, (coarse, fine) in enumerate(zip(rows[i], rows[i + 1], strict=True)):
                if fine > coarse:
                    rise = (fine - coarse) / coarse
                    if rise > worst:
                        worst, at_mesh, at_mode = rise, meshes[i + 1], mode + 1
        return worst, at_mesh, at_mode

    nested = sequences(no_phi=True)
    shipped = sequences(no_phi=False)

    with capsys.disabled():
        print("\n  largest RISE in a frequency under mesh refinement:")
        for label in ("free-free", "pinned-pinned"):
            a = worst_rise(nested[label])
            c = worst_rise(shipped[label])
            print(f"    {label:14s} Phi=0: {a[0]:.3e}   shipped: {c[0]:.3e}")

    for label in ("free-free", "pinned-pinned"):
        for which, rows in (("Phi = 0", nested[label]), ("shipped", shipped[label])):
            rise, at_mesh, at_mode = worst_rise(rows)
            assert rise == 0.0, (
                f"{label}, {which}: a frequency ROSE by {rise:.4e} at "
                f"n={at_mesh}, mode {at_mode}. The interpolation family is "
                "length-independent, so the meshes are nested and Rayleigh-Ritz "
                "forbids it. R541 was exactly this assertion failing on the "
                "shipped element, and the cause was the shear term's sign."
            )


@pytest.mark.parametrize("plane", ["xy", "xz"])
def test_the_SHIPPED_element_approaches_its_OWN_continuum(plane: str, capsys) -> None:
    """The shipped element against the exact Timoshenko pinned-pinned frequency.

    The reference is now the element's own theory, which is what DL0 asked for,
    and both bending planes are run because the `xz` plane carries the sign flip
    a planar case cannot see.

    ASSERTED OVER THE WHOLE RANGE THIS TEST PRINTS: the error is POSITIVE at
    every mesh and falls at every refinement, both planes, all three modes. That
    is the sign half of DL0's band and on the corrected element it is exact
    theory rather than a measurement that happened to come out that way.

    THE RANGE USED TO STOP AT 16 AND THE REASON WAS A DEFECT (R542, R541). It
    read: "beyond it the non-nested wobble is the same size as the discretisation
    error, and the error changes sign at n=32." The sign change at n=32 WAS the
    defect. Corrected, the error is positive and falling from n=4 to n=128, so
    there is nothing to truncate -- and the reviewer's own measurement showed the
    old assertion passing on BOTH signs over 4 -> 8 -> 16, so the narrowed domain
    certified nothing about the thing that was wrong. A test correct about a
    domain that excludes the fault is the shape this finding is named for.

    STILL NOT ASSERTED: DL0's [12, 20] window on the convergence RATIO. The
    module docstring carries the two cells that refuted the round-off-floor and
    rotary-inertia explanations for the order sagging toward 2 at fine meshes,
    and DN0's second branch sends that question to F3.
    """
    section = _tube(0.3, 0.008)
    length = 30.0
    inertia = section.I_y
    reference = [
        timoshenko_pinned_pinned(mode, length, section, STEEL, inertia) for mode in (1, 2, 3)
    ]
    reported = (4, 8, 16, 32, 64, 128)
    errors: dict[int, list[float]] = {}
    for n_el in reported:
        got = _pinned_pinned_frequencies(length, n_el, section, 3, plane)
        errors[n_el] = [(value - want) / want for value, want in zip(got, reference, strict=True)]

    with capsys.disabled():
        print(f"\n  plane {plane}, against the EXACT Timoshenko pinned-pinned reference:")
        for n_el in reported:
            print(f"    n={n_el:4d}  " + "  ".join(f"{e:+.4e}" for e in errors[n_el]))

    for mode in range(3):
        for n_el in reported:
            assert errors[n_el][mode] > 0.0, (
                f"plane {plane}, mode {mode + 1}, n={n_el}: the computed frequency "
                f"is BELOW the exact Timoshenko value by {errors[n_el][mode]:.4e}. "
                "The interpolation family is length-independent and conforming, so "
                "Rayleigh-Ritz forbids it -- R541 was this assertion failing, and "
                "the cause was the shear term's sign."
            )
    for coarse, fine in zip(reported[:-1], reported[1:], strict=True):
        for mode in range(3):
            before = abs(errors[coarse][mode])
            after = abs(errors[fine][mode])
            assert after < before, (
                f"plane {plane}, mode {mode + 1}: refining from n={coarse} to "
                f"n={fine} did not reduce the error against the element's own "
                f"continuum -- {before:.4e} then {after:.4e}. That reference is "
                "exact for these boundary conditions, so refinement has to "
                "approach it."
            )


# --------------------------------------------------------------------------
# DN1. The convention-free check: the interpolated field's own strain energy
# --------------------------------------------------------------------------


def _field_coefficients(
    length: float, phi: float, q: NDArray[np.float64], interp=bending_interpolation
) -> tuple[float, float, float]:
    """`(c2, c3, gamma)` read OUT of the interpolation, assuming nothing.

    `theta` is exactly quadratic in `xi` and `w` exactly cubic, so three and four
    exact samples determine them. **Nothing here re-derives the shear term**: the
    shape functions are sampled and the coefficients fitted, so a wrong sign
    shows up in `gamma` rather than being cancelled by a reference that shares
    the mistake. That is the whole point -- V2.5's four other checks all live
    where the shear coefficient cannot be seen.

    `interp` IS A PARAMETER AND NOT A PATCHED MODULE ATTRIBUTE. The first version
    of the counter below patched `floatfea.element.beam.bending_interpolation`
    while this function read the name imported into THIS module, so the defect
    was never injected and the counter reported that it could not see it. That is
    the resolution mistake the reviewer recorded against its own first cell in
    the sixty-first verdict, made here a round later.
    """

    def theta(xi: float) -> float:
        return float(interp(length, phi, xi)[1] @ q)

    def w(xi: float) -> float:
        return float(interp(length, phi, xi)[0] @ q)

    t0, t_half, t1 = theta(0.0), theta(0.5), theta(1.0)
    c3 = 2.0 * (t1 - 2.0 * t_half + t0)
    c2 = t1 - t0 - c3
    nodes = np.array([0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    coeffs = np.linalg.solve(np.vander(nodes, 4, increasing=True), np.array([w(x) for x in nodes]))
    slope = coeffs[1] + 2.0 * coeffs[2] * 0.5 + 3.0 * coeffs[3] * 0.25
    gamma = slope / length - t_half
    return c2, c3, gamma


PHI_PROBES = (1.0e-3, 1.0e-2, 0.1, 1.0, 10.0)
"""not-a-tolerance: the shear parameters the identity below is probed at. They
span four decades because the term under test is proportional to `Phi` and
vanishes at `Phi = 0`, where no check can see it."""


def _energy_mismatch(phi_target: float, interp) -> float:
    """Worst relative gap between `q^T k q` and the field's own strain energy.

        integral_0^L EI theta'^2 dx = (EI/L) (c2^2 + 2 c2 c3 + 4 c3^2 / 3)
        kappa G A gamma^2 L          with gamma constant over the element

    Closed form, not sampled. The rigid part of `q` is projected out, because a
    rigid motion has zero energy on both sides and would dilute the comparison.
    """
    d_outer, thickness = 0.6, 0.012
    area = basis.tube_area(d_outer, thickness)
    inertia = basis.tube_second_moment(d_outer, thickness)
    section = Section(
        A=area,
        I_y=inertia,
        I_z=inertia,
        J=basis.torsion_constant("thin_tube", inertia, inertia),
        shape="thin_tube",
    )
    ei = STEEL.E * inertia
    kga = section.kappa(STEEL) * STEEL.G * area
    length = float(np.sqrt(12.0 * ei / (kga * phi_target)))
    k = bending_stiffness(ei, length, phi_target)

    rigid = np.column_stack([np.array([1.0, 0.0, 1.0, 0.0]), np.array([0.0, 1.0, length, 1.0])])
    rng = np.random.default_rng(20260927)
    worst = 0.0
    for _ in range(24):
        q = rng.standard_normal(4)
        q = q - rigid @ np.linalg.lstsq(rigid, q, rcond=None)[0]
        c2, c3, gamma = _field_coefficients(length, phi_target, q, interp)
        want = (ei / length) * (c2**2 + 2.0 * c2 * c3 + 4.0 * c3**2 / 3.0)
        want += kga * gamma**2 * length
        worst = max(worst, abs(float(q @ k @ q) - want) / abs(want))
    return worst


def _flipped(length: float, phi: float, xi: float):
    """The interpolation with the shear term's sign as it SHIPPED (R541)."""
    return bending_interpolation(length, -phi, xi)


@pytest.mark.parametrize("phi_target", PHI_PROBES)
def test_the_INTERPOLATED_FIELDS_OWN_ENERGY_equals_the_stiffness(phi_target: float, capsys) -> None:
    """`q^T k q == integral EI theta'^2 dx + kappa G A gamma^2 L`, exactly.

    THIS IS THE CHECK THAT WOULD HAVE CAUGHT R541 ON THE DAY, and it is here
    because none of V2.5's other four reach the shear coefficient: the
    Euler-Bernoulli checkpoint is at `Phi = 0` by construction, and the
    rigid-body inertias and `Phi^T M Phi` are quadratic forms of vectors whose
    `c3` is zero -- `c3` being the only coefficient the shear term multiplies.

    WHY IT IS CONVENTION-FREE. Przemieniecki eq. 5.36 is the exact stiffness of
    the exact homogeneous Timoshenko field, so it IS the strain energy of the
    field the interpolation describes. Both sides are scalars built from the same
    `q`, and no sign convention between `theta` and `dw/dx` survives into either.
    """
    worst = _energy_mismatch(phi_target, bending_interpolation)
    with capsys.disabled():
        print(f"\n  Phi={phi_target:<8g} worst {worst:.4e}")
    assert worst <= ROUNDOFF_IDENTITY, (
        f"Phi={phi_target:g}: the interpolated field's strain energy disagrees "
        f"with eq. 5.36 by {worst:.4e} relative, against {ROUNDOFF_IDENTITY:g}. "
        "The stiffness IS that field's energy, so the two cannot differ unless "
        "the interpolation is not the field the stiffness was derived for."
    )


def test_the_SHIPPED_SIGN_FLIP_breaks_the_energy_identity(capsys) -> None:
    """R541's counter, and it is the defect that shipped rather than an invention.

    The response has to grow with `Phi`, because at `Phi = 0` the term vanishes
    and no check can see it. That is why the probes start at `1e-3` and why this
    test says so rather than claiming coverage it does not have.
    """
    rows = []
    for phi_target in PHI_PROBES:
        try:
            rows.append((phi_target, _energy_mismatch(phi_target, _flipped)))
        except np.linalg.LinAlgError:
            rows.append((phi_target, float("inf")))
    with capsys.disabled():
        print("\n  the shipped sign flip, against the energy identity:")
        for phi_target, gap in rows:
            shown = "LinAlgError (singular at Phi = 1)" if gap == float("inf") else f"{gap:.4e}"
            print(f"    Phi={phi_target:<8g} {shown}   ceiling {ROUNDOFF_IDENTITY:g}")

    blind = [phi for phi, gap in rows if gap <= ROUNDOFF_IDENTITY]
    assert not blind, (
        f"the flipped sign passes the energy identity at Phi={blind}, so that "
        "check cannot see the defect R541 was."
    )
    ordered = [gap for _, gap in rows]
    assert ordered[0] < ordered[1] < ordered[2], (
        f"the response does not grow with Phi -- {ordered[:3]}. The term under "
        "test is proportional to Phi, so a response that does not grow with it "
        "is not measuring that term."
    )
