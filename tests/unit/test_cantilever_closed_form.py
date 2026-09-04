"""One-element cantilever against closed forms — over-determined, both planes (AU1/AU2).

Why this is stronger than the `Phi = 0` checkpoint
--------------------------------------------------
Passing `Phi = 0` exactly verifies the Przemieniecki transcription, and nothing
more. **Any formulation `K_EB * f(Phi)` with `f(0) = I` passes it** — including
`(1 - Phi)` where `1/(1 + Phi)` belongs. The exact-zero test cannot discriminate
*where* `Phi` sits, and its negative control cannot either: a bit-exact comparison
reddens on any perturbation whatsoever, so it proves the assertion is wired up,
not that it discriminates.

**The closed forms below are what pin the placement**, because
`delta = PL^3/3EI + PL/(kappa G A)` is independent of the element formulation.

Over-determined, not inferred
-----------------------------
A cantilever's free block in one bending plane is a symmetric 2x2 — three
independent entries. Asserting one scalar per load case gives two equations for
three unknowns. Asserting **deflection AND rotation** under **end force AND end
moment** gives **four equations for three unknowns** at each `Phi`, so the block is
fully pinned rather than inferred.

Closed forms, cantilever fixed at A, free at B (Przemieniecki §2; any strength of
materials text). Shear contributes to deflection under end force only — under an
end moment there is no shear force, and shear never contributes to rotation::

    end force P    delta = P L^3 / (3 EI) + P L / (kappa G A)
                   theta = P L^2 / (2 EI)
    end moment M   delta = M L^2 / (2 EI)
                   theta = M L / (EI)
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.element.beam import bending_stiffness, local_stiffness, shear_parameter
from floatfea.model.material import S355, Section
from floatfea.tolerances import ROUNDOFF_IDENTITY

# Slender and stubby. Phi = 0.0112 and 0.7769 -- at the stubby end the shear share
# of tip deflection is (Phi/4)/(1+Phi/4) = 16.3%, so an Euler-Bernoulli element
# mislabelled as Timoshenko misses by 16%, not by a tolerance width.
CASES = [
    ("slender", Section.circular_tube(0.4, 0.010), 10.0),
    ("stubby", Section.circular_tube(0.8, 0.020), 2.4),
]
LOAD = 1.0e6
ULP = 1e-13          # provisional; V2.2's tolerance is measured at step 8


def _free_block(section: Section, length: float) -> np.ndarray:
    """Node A fully fixed; the six free DOF of node B."""
    k = local_stiffness(section, S355, length)
    return k[np.ix_([6, 7, 8, 9, 10, 11], [6, 7, 8, 9, 10, 11])]


def _solve(section: Section, length: float, dof: int) -> np.ndarray:
    f = np.zeros(6)
    f[dof] = LOAD
    return np.linalg.solve(_free_block(section, length), f)


def _constants(section: Section, length: float, plane: str):
    inertia = section.I_z if plane == "xy" else section.I_y
    ei = S355.E * inertia
    kga = section.kappa(S355) * S355.G * section.A
    return ei, kga


@pytest.mark.parametrize("label, section, length", CASES, ids=lambda c: c if isinstance(c, str) else "")
def test_xy_plane_is_over_determined_by_closed_forms(
    label: str, section: Section, length: float
) -> None:
    """Four equations, three unknowns, in the x-y plane."""
    ei, kga = _constants(section, length, "xy")
    l = length

    d = _solve(section, length, 1)          # end force in +y
    assert d[1] == pytest.approx(LOAD * l**3 / (3 * ei) + LOAD * l / kga, rel=ULP)
    assert d[5] == pytest.approx(LOAD * l**2 / (2 * ei), rel=ULP)

    d = _solve(section, length, 5)          # end moment about +z
    assert d[1] == pytest.approx(LOAD * l**2 / (2 * ei), rel=ULP)
    assert d[5] == pytest.approx(LOAD * l / ei, rel=ULP)


@pytest.mark.parametrize("label, section, length", CASES, ids=lambda c: c if isinstance(c, str) else "")
def test_xz_plane_matches_its_own_closed_form_SIGNED(
    label: str, section: Section, length: float
) -> None:
    """AU2 — the `diag(1,-1,1,-1)` flip, measured now rather than at V2.4.

    In the x-z plane `w' = -theta_y`, so the signs differ from the x-y plane:
    positive deflection under end force comes with NEGATIVE rotation, and a
    positive end moment produces NEGATIVE deflection.

    Asserted against the closed form, signed. This is external, not
    self-consistency -- self-consistency is precisely the state in which a sign
    error survives.
    """
    ei, kga = _constants(section, length, "xz")
    l = length

    d = _solve(section, length, 2)          # end force in +z
    assert d[2] == pytest.approx(LOAD * l**3 / (3 * ei) + LOAD * l / kga, rel=ULP)
    assert d[4] == pytest.approx(-LOAD * l**2 / (2 * ei), rel=ULP)

    d = _solve(section, length, 4)          # end moment about +y
    assert d[2] == pytest.approx(-LOAD * l**2 / (2 * ei), rel=ULP)
    assert d[4] == pytest.approx(LOAD * l / ei, rel=ULP)


def test_a_MAGNITUDE_only_check_would_MISS_a_wrong_flip() -> None:
    """Negative control for AU2, and the reason the test above is signed.

    A wrong flip leaves the deflection magnitude under end force unchanged, so a
    magnitude-only assertion passes while the defect stands. Demonstrated by
    building the x-z block with the flip omitted and comparing both ways.
    """
    section, length = CASES[1][1], CASES[1][2]
    ei, _ = _constants(section, length, "xz")
    phi = shear_parameter(section, S355, length, plane="xz")
    ky = bending_stiffness(ei, length, phi)
    flip = np.diag([1.0, -1.0, 1.0, -1.0])

    correct = flip @ ky @ flip
    wrong = ky                                    # flip omitted

    # Free block for (w_B, ry_B) is rows/cols 2,3 of the 4x4.
    def tip(block, dof):
        f = np.zeros(2)
        f[dof] = LOAD
        return np.linalg.solve(block[np.ix_([2, 3], [2, 3])], f)

    c_force, w_force = tip(correct, 0), tip(wrong, 0)
    c_mom, w_mom = tip(correct, 1), tip(wrong, 1)

    # Under END FORCE the deflection magnitude is identical -- the trap.
    assert abs(c_force[0]) == pytest.approx(abs(w_force[0]), rel=ROUNDOFF_IDENTITY)
    # But the rotation sign is reversed, and so is the deflection under moment.
    assert c_force[1] == pytest.approx(-w_force[1], rel=ROUNDOFF_IDENTITY)
    assert c_mom[0] == pytest.approx(-w_mom[0], rel=ROUNDOFF_IDENTITY)
    assert c_force[1] != pytest.approx(w_force[1], rel=1e-6)  # not-a-tolerance: negative control -- asserts the two DIFFER, so loosening cannot hide a defect


def test_the_stubby_case_has_a_shear_share_worth_detecting() -> None:
    """AU0: V2.2 must have teeth.

    If the shear contribution were tolerance-width, an Euler-Bernoulli element
    mislabelled as Timoshenko would pass V2.2 and the gate would be decorative.
    """
    section, length = CASES[1][1], CASES[1][2]
    phi = shear_parameter(section, S355, length, plane="xy")
    share = (phi / 4.0) / (1.0 + phi / 4.0)
    assert phi == pytest.approx(0.7769, abs=5e-4)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged
    assert share > 0.15, f"shear share only {share:.1%}; V2.2 would not discriminate"  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small


def test_the_slender_case_is_nearly_euler_bernoulli() -> None:
    """The other end of the pair: the two cases must actually differ."""
    section, length = CASES[0][1], CASES[0][2]
    phi = shear_parameter(section, S355, length, plane="xy")
    assert phi == pytest.approx(0.0112, abs=5e-4)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged
    assert (phi / 4.0) / (1.0 + phi / 4.0) < 0.01  # not-a-tolerance: fixture property -- bounds an input, not a computed discrepancy
