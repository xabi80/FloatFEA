"""Material and section CONTAINERS. They define no constants (D1, AS1/AS2).

Every value comes from `floatfea/basis.py`. This module holds the shapes of the
data, not the data.

**`kappa` is not a field here, and must never become one.** It depends on both the
section geometry and Poisson's ratio, so it belongs to neither `Material` nor
`Section` alone — it is a property of the *pair*, obtained by calling
`basis.kappa(shape, nu)`. A stored `kappa` is wrong as soon as either changes,
which is why the physics forbids the field and not merely the duplication.

`Section` therefore carries a **shape name**, and the shear coefficient is
computed on demand from that shape and the material's `nu`.
"""

from __future__ import annotations

from dataclasses import dataclass

from floatfea import basis


@dataclass(frozen=True)
class Material:
    """Isotropic elastic material. `G` is derived, never declared."""

    E: float
    nu: float
    rho: float
    fy: float
    name: str = ""

    @property
    def G(self) -> float:
        """Shear modulus, derived from E and nu.

        Declared as a property rather than a field so the three cannot drift
        apart: a `G` field would let a caller construct a material whose E, nu
        and G disagree, and nothing downstream would notice.
        """
        return self.E / (2.0 * (1.0 + self.nu))

    @property
    def sigma_allow(self) -> float:
        """Working-stress allowable on the project basis (`basis.ALLOWABLE_FACTOR`)."""
        return basis.ALLOWABLE_FACTOR * self.fy


S355: Material = Material(
    E=basis.E_STEEL,
    nu=basis.NU_STEEL,
    rho=basis.RHO_STEEL,
    fy=basis.FY_S355,
    name="S355",
)


@dataclass(frozen=True)
class Section:
    """A prismatic cross-section.

    Prismatic only, per Q3: taper enters through subdivision in the model builder,
    because a tapered element has no closed form to verify against and would
    violate the reference-provenance requirement by construction.

    ``shape`` names the geometry for the shear coefficient. It is a name and not a
    number precisely so that `kappa` stays computed.
    """

    A: float
    I_y: float
    I_z: float
    J: float
    shape: str

    def __post_init__(self) -> None:
        """Validate on the TYPE, not only on the convenience constructor (AW3).

        The AU3 guard was placed inside `circular_tube`, which meant
        `Section(...)` accepted any `J` and any `shape` with no check at all --
        so the claim that a non-circular section fails loudly at construction was
        false for every caller that did not happen to use the classmethod. A
        guard on one construction path is not a guard on the type.

        Found because a test constructed `I_y != I_z` while labelling the shape
        `thin_tube`, which additionally drew the CIRCULAR `kappa` for a
        non-circular section -- an incoherent object the production path could
        equally have built.
        """
        if self.A <= 0.0 or self.I_y <= 0.0 or self.I_z <= 0.0 or self.J <= 0.0:
            raise ValueError(
                f"section properties must be positive; got A={self.A}, "
                f"I_y={self.I_y}, I_z={self.I_z}, J={self.J}"
            )
        # `kappa` raises for an unknown shape; calling it here moves that failure
        # to construction rather than to first use in an element.
        basis.kappa(self.shape, basis.NU_STEEL)

        if self.shape in ("thin_tube", "solid_circular"):
            if self.I_y != self.I_z:
                raise ValueError(
                    f"shape {self.shape!r} is circular but I_y ({self.I_y}) != "
                    f"I_z ({self.I_z}). A circular section has equal second "
                    "moments; this object would draw the circular kappa and the "
                    "circular J for a section that is neither."
                )
            expected = basis.torsion_constant(self.shape, self.I_y, self.I_z)
            if expected != self.J:
                raise ValueError(
                    f"shape {self.shape!r} requires J = I_y + I_z = {expected}; "
                    f"got {self.J}. Supplying J directly bypasses "
                    "basis.torsion_constant, which is the only place the "
                    "no-warping assumption is checked."
                )

    def kappa(self, material: Material) -> float:
        """Shear correction factor for this section in this material.

        The only route. Takes the material because `kappa` depends on `nu`.
        """
        return basis.kappa(self.shape, material.nu)

    @classmethod
    def circular_tube(cls, d_outer: float, t: float) -> Section:
        """A circular hollow section, exact properties (not thin-wall).

        G3.3 asks for exact section properties, so the thin-wall forms
        ``A = pi D t`` and ``I = pi D^3 t / 8`` are deliberately not used here --
        they are close enough to pass a loose check and wrong enough to matter.
        """
        if t <= 0.0 or d_outer <= 2.0 * t:
            raise ValueError(
                f"invalid tube: D_outer={d_outer}, t={t}. The wall must be "
                "positive and thinner than the radius."
            )
        i = basis.tube_second_moment(d_outer, t)
        return cls(
            A=basis.tube_area(d_outer, t),
            I_y=i,
            I_z=i,  # circular: equal in both bending planes
            J=basis.torsion_constant("thin_tube", i, i),
            shape="thin_tube",
        )
