"""Containers hold no constants, and kappa is not a field (AS1)."""
from __future__ import annotations

import math
from dataclasses import fields

import pytest

from floatfea import basis
from floatfea.model.material import S355, Material, Section


def test_kappa_is_NOT_a_field_on_either_container() -> None:
    """The rule, asserted structurally rather than trusted.

    kappa depends on section geometry AND nu, so it belongs to neither container
    alone. A field here would be wrong the moment either changes.
    """
    for cls in (Material, Section):
        names = {f.name for f in fields(cls)}
        assert not {n for n in names if "kappa" in n.lower()}, (
            f"{cls.__name__} has a kappa field; it must be computed from "
            "basis.kappa(shape, nu) instead"
        )


def test_section_carries_a_SHAPE_not_a_coefficient() -> None:
    s = Section.circular_tube(0.6, 0.012)
    assert s.shape == "thin_tube"
    assert s.kappa(S355) == pytest.approx(basis.kappa("thin_tube", S355.nu))


def test_kappa_moves_with_the_material() -> None:
    from dataclasses import replace

    s = Section.circular_tube(0.6, 0.012)
    assert s.kappa(S355) != s.kappa(replace(S355, nu=0.45))


def test_G_is_derived_so_E_nu_G_cannot_drift() -> None:
    assert S355.G == pytest.approx(S355.E / (2 * (1 + S355.nu)))
    assert "G" not in {f.name for f in fields(Material)}


def test_sigma_allow_comes_from_the_project_basis() -> None:
    assert S355.sigma_allow == pytest.approx(basis.SIGMA_ALLOW_S355)
    assert S355.sigma_allow == pytest.approx(0.6 * S355.fy)


def test_tube_properties_are_exact_not_thin_walled() -> None:
    d, t = 0.6, 0.012
    s = Section.circular_tube(d, t)
    assert s.A == pytest.approx(basis.tube_area(d, t))
    assert s.A < math.pi * d * t                  # thin-wall over-states
    assert s.J == pytest.approx(s.I_y + s.I_z)    # circular: exact


def test_the_material_container_declares_no_values_of_its_own() -> None:
    """S355 must be assembled from basis.py, not typed in again."""
    assert S355.E == basis.E_STEEL
    assert S355.nu == basis.NU_STEEL
    assert S355.rho == basis.RHO_STEEL
    assert S355.fy == basis.FY_S355


def test_J_RAISES_for_a_non_circular_shape(monkeypatch) -> None:
    """AU3: the unsupported case is an error, never a default.

    J = I_y + I_z is the polar moment and is the torsion constant only for
    circular sections. Returning it for anything else makes the member
    torsionally over-stiff, and nothing downstream is looking for that.
    """
    with pytest.raises(ValueError, match="no torsion constant"):
        basis.torsion_constant("i_beam", 1.0, 2.0)


def test_J_is_exact_for_the_shapes_it_does_accept() -> None:
    assert basis.torsion_constant("thin_tube", 3.0, 4.0) == pytest.approx(7.0)
    assert basis.torsion_constant("solid_circular", 3.0, 4.0) == pytest.approx(7.0)


def test_a_non_circular_section_cannot_be_built_silently() -> None:
    """The guard must bite at CONSTRUCTION, not at first use.

    A Section carrying a wrong J would propagate into an assembled matrix before
    anything noticed.
    """
    with pytest.raises(ValueError, match="no torsion constant"):
        Section(A=1.0, I_y=1.0, I_z=1.0,
                J=basis.torsion_constant("rectangular", 1.0, 1.0),
                shape="rectangular")
