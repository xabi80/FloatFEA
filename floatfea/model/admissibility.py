"""Where a beam element stops being a beam (BH0).

`docs/conventions.md` § "Beam admission limit" is the locked statement; this is
its enforcement. A member whose length is comparable to its cross-section depth
is not described by any beam theory — Timoshenko included, since shear-flexible
beam kinematics still assume plane sections and a length scale over which
stresses redistribute. Below the limit the answer is not "less accurate", it is
"a different model", and the route is an F7 shell sub-model.

THE LIMIT IS ON THE MEMBER, NOT THE ELEMENT, and the distinction is not
pedantic. Beam validity is a property of the physical member; subdividing a
valid member into short elements is ordinary practice and changes nothing about
the idealisation. Measured, on the gate's own mesh: the member is `L/D = 16.12`
and comfortably admissible while two of its five elements sit at `L/D = 1.32`
and `1.50`. An element-wise limit of 2 would reject the patch test's own model,
which is how it was found.

WHAT F2 CAN ENFORCE. F2's model has elements and no member concept — members
arrive with F3's builder (`docs/milestones/F2.md` §5 Q3: subdivide, do not
taper). So this function is the rule with a home and a test, called today by the
corpus runner, and F3's builder calls it per member as a named dependency.
"""
from __future__ import annotations

from floatfea.model.material import Section
from floatfea.tolerances import BEAM_ADMISSION_L_OVER_D


def member_l_over_d(length: float, section: Section) -> float:
    """Member length over cross-section depth.

    Depth is the OUTER diameter, recovered exactly from the section's own `A`
    and `I` rather than stored, so a section built by any route reports the same
    number. For a circular hollow section,

        R_o^2 + R_i^2 = 4 I / A        R_o^2 - R_i^2 = A / pi
        =>  D_o = 2 sqrt( 2 I / A  +  A / (2 pi) )

    which is exact for a tube of any wall thickness and reduces to the solid
    circle at R_i = 0. A first draft used `4 sqrt(I/A)`, the SOLID relation, and
    overstated the depth of a thin tube by sqrt(2): it made the gate's own
    section 0.8317 m deep instead of 0.6 m.
    """
    if length <= 0.0:
        raise ValueError(f"member length must be positive; got {length}")
    depth = _outer_diameter(section)
    return float(length / depth)


def _outer_diameter(section: Section) -> float:
    import math

    return 2.0 * math.sqrt(2.0 * section.I_z / section.A
                           + section.A / (2.0 * math.pi))


def assert_beam_admissible(length: float, section: Section, what: str = "") -> None:
    """Raise unless this member is inside the beam idealisation.

    Raises `ValueError`, never warns: `CLAUDE.md` § Non-negotiables — a
    validation failure does not degrade to a warning, and a stubby member
    analysed as a beam is exactly the wrong-answer-that-looks-right this
    repository is built to prevent.
    """
    ratio = member_l_over_d(length, section)
    if ratio < BEAM_ADMISSION_L_OVER_D:
        raise ValueError(
            f"{what or 'member'} has L/D = {ratio:.3f}, below the beam admission "
            f"limit {BEAM_ADMISSION_L_OVER_D:.1f} "
            f"(length {length:.4g}, outer diameter {_outer_diameter(section):.4g}). "
            "This is not a beam and no beam element will describe it. Route it to "
            "an F7 shell sub-model; see docs/conventions.md, 'Beam admission "
            "limit'."
        )


def member_lambda(length: float, section: Section) -> float:
    """`L / r` with `r = sqrt(I/A)` -- a REPORTED diagnostic axis, not a limit.

    Not `L/D`, which is the admission limit's axis. The two answer different
    questions: `L/D` asks whether this is a beam at all, `L/r` asks how far the
    round-off floor of a SOLVE has risen. Measured on a 2-D grid over element
    count and member `L/r` (F2.md sec. 5b, Q6): member `L/r` carries the
    frame-dependent part at exponent ~2 in skew against 0.68 axis-aligned, and
    element `L/r` is refuted as the axis because both exponents come out positive
    where a governing quantity would give equal and opposite ones.

    NOTHING IS GATED ON IT. `warn_outside_validated_domain` and the
    `G22_VALIDATED_MEMBER_LAMBDA` boundary it enforced were removed when G2.2
    stopped asserting a solved quantity: the floor this axis tracks belongs to
    the forward error of a linear solve, which is now reported and never
    asserted. The value is still worth carrying, because it is the axis along
    which the counter-case's sensitivity falls -- as `1/lambda^2`, which is why
    `PATCH_TEST_EXACTNESS_COUNTER` is recorded at the most slender configuration
    in the corpus.
    """
    if length <= 0.0:
        raise ValueError(f"member length must be positive; got {length}")
    return float(length / (section.I_z / section.A) ** 0.5)
