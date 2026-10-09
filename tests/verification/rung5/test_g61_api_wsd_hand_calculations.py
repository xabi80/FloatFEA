"""G6.1: every API RP 2A-WSD clause against an INDEPENDENT hand calculation.

**`# expected:` IS THE CLAUSE FORMULA WORKED IN THIS FILE, IN SI, WITH THE CLAUSE CITED.
NEVER THE MODULE'S OWN FUNCTION** (FB0, EA4). Each expected value below is written as
arithmetic a reader can follow on paper -- `0.6 * 355e6`, not `allowable_axial_tension()` --
so a transcription error in `floatfea/checks/api_wsd.py` cannot be reproduced by the thing
checking it.

WHY THIS FILE EXISTS, AND WHY IT EXISTS *NOW*. FB0 puts G6.1 before the next deliverable
send, amending FA3's ordering, because six of the eight findings in the round before it
were inside G6.1's scope: R741 (section 3.2.2(b) absent, a slender section not refused),
R742 (`F_b` returned above `0.75 F_y`), R743 (`C_m`'s direction stated backwards), and
three more. Nothing between the arithmetic and the send was reading either file.

TWO OR MORE POINTS PER BRANCH (FB0), and the points sit **either side of every boundary**
rather than in the middle of a range -- `C_c`, the three `D/t` limits, the local-buckling
limit, the tension/compression switch. A point taken only in a branch's interior cannot see
a misplaced boundary, which is R742's whole mechanism.

**AND THREE OF THE POINTS WERE CHOSEN BY MEASUREMENT RATHER THAN BY INSPECTION**, because
the obvious point was vacuous in each case. They are marked where they appear:

* section 3.3.2's amplified form does not govern at a moderate axial load -- `max(amplified,
  simple)` selects the SIMPLE form, in which `F_a`, `F_e'` and `C_m` do not appear at all,
  so `u_combined` is correct whatever the amplified branch computes;
* section 3.2.2(b)'s `F_xe = 2 C E t / D` never governs `min(F_xc, F_xe)` at
  `F_y = 355 MPa`, at any `D/t` the clause admits, so half of that clause is unreachable at
  the grade F6 locks and is taken at `F_y = 690 MPa`;
* a pure-compression utilisation cannot reach `1.0` on the elastic branch, because `F_a`
  and `F_e'` are the same expression there.
"""

from __future__ import annotations

import inspect
import math

import pytest

from floatfea.basis import E_STEEL, FY_S355
from floatfea.checks import api_wsd
from floatfea.checks.api_wsd import (
    CM_JOINT_TRANSLATION,
    allowable_axial_compression,
    allowable_axial_tension,
    allowable_bending,
    allowable_shear,
    check_member,
    column_slenderness_parameter,
    euler_stress,
    local_buckling_stress,
    section_class,
)
from floatfea.testing import assert_close
from floatfea.tolerances import (
    F4_WINDOW_RULE_MIN_EDGE,
    F6_API_CLAUSE_AGREEMENT,
    F6_API_CLAUSE_AGREEMENT_COUNTER,
    F6_API_CLAUSE_INJECTION_EPS,
    F6_API_UTILISATION_COUNTER_FACTOR,
)

TOL = F6_API_CLAUSE_AGREEMENT
FY = 355e6
FY_HIGH = 690e6
E = 210e9
FLOOR = 1.0
"""One pascal: the round-off floor of a stress in SI. `assert_close` refuses a comparison
whose operands sit within 100x of it, so a clause that returned zero could not pass."""
RATIO_FLOOR = 1.0e-12
"""The floor for the dimensionless quantities -- `C_c` and the utilisations."""

# The F1 stand-in tube, which is the section F6 checks (EZ4 Q3). Exact reprs, tied back to
# the builder by `test_the_section_properties_are_the_tube_the_milestone_CHECKS` below.
#
# `W` AND `W_t` WERE `0.7104` AND `1.4208` HERE FIRST, which is what
# `scripts/measure/api_wsd_utilisation.py`'s summary PRINTS at `{:.4f}`. The script itself
# derives them from the section, so the rounded pair would have made the gate check the
# clauses on a section `0.0023%` away from the one the deliverable uses.
D_OUTER = 2.5
WALL = 0.18
AREA = 1.3119290921390976
W_SECTION = 0.7103833648114783
W_TORSION = 1.4207667296229567


def _member(**over: float):
    """One member-station, every load zero unless named. Keyword-only, as the module is."""
    kw: dict[str, float] = dict(
        axial_n=0.0,
        shear_y_n=0.0,
        shear_z_n=0.0,
        torsion_nm=0.0,
        moment_y_nm=0.0,
        moment_z_nm=0.0,
        area_m2=AREA,
        section_modulus_m3=W_SECTION,
        torsional_modulus_m3=W_TORSION,
        d_outer_m=D_OUTER,
        wall_m=WALL,
        k_l_over_r=60.8,
        fy=FY,
        e=E,
    )
    kw.update(over)
    return check_member(**kw)  # type: ignore[arg-type]


# ===========================================================================  the basis
def test_the_module_runs_at_the_basis_this_file_HAND_CALCULATES_at() -> None:
    """A hand calculation at the wrong `F_y` or `E` would agree with nothing.

    R742's cause was a mismatch of exactly this kind one level down: the clause's `D/t`
    branch limits are continuous at `E = 29000 ksi = 199948 MPa` and the module runs at
    `210000 MPa`, which is why the first reduced branch could exceed the compact value.
    """
    # not-a-tolerance: the basis the clause arithmetic below is written at. An exact
    # equality between two declared constants, not a comparison with slack -- a hand
    # calculation at the wrong F_y would agree with nothing, so there is no band to allow.
    assert (
        FY_S355 == FY
    ), (  # not-a-tolerance: exact, see above
        f"basis F_y is {FY_S355}, this file hand-calculates at {FY}"
    )
    assert (
        E_STEEL == E
    ), (  # not-a-tolerance: exact, see above
        f"basis E is {E_STEEL}, this file hand-calculates at {E}"
    )


def test_the_section_properties_are_the_tube_the_milestone_CHECKS() -> None:
    """The points below mean nothing unless the section is F1's stand-in tube.

    `A` and the moduli are hand-written constants here so the clause arithmetic does not
    depend on the model builder; this is what ties them back to it, and it is an exact
    equality because both sides are the same double.
    """
    from floatfea.model.platform import build_superstructure

    section = build_superstructure().bodies[0].members[0].section
    # not-a-tolerance: the section the gate checks against the section the builder makes.
    # Bit-identical by construction -- the constants above are that section's own reprs --
    # so any difference at all is a changed section, not a numerical one.
    assert section.A == AREA, (section.A, AREA)  # not-a-tolerance: bit-identical, see above
    assert 2.0 * section.I_y / D_OUTER == W_SECTION  # not-a-tolerance: bit-identical, see above
    assert 2.0 * section.J / D_OUTER == W_TORSION  # not-a-tolerance: bit-identical, see above
    assert section_class(D_OUTER, WALL, FY).d_over_t == D_OUTER / WALL  # not-a-tolerance: exact


# ===========================================================================  3.2.1
@pytest.mark.parametrize("fy, hand_f_t", [(355e6, 213.0e6), (275e6, 165.0e6)])
def test_G61_axial_tension(fy: float, hand_f_t: float) -> None:
    """Section 3.2.1: `F_t = 0.6 F_y`. Two grades, because the clause is linear in `F_y`.

    # expected: 0.6 * F_y, worked here -- 213.0e6 Pa at S355 and 165.0e6 Pa at S275. The
    # hand value is carried as a PARAMETER so that the arithmetic and the number a reader
    # would write down are both in the file and must agree.
    """
    expected = 0.6 * fy
    assert expected == hand_f_t  # not-a-tolerance: two spellings of one product, exact
    assert_close(allowable_axial_tension(fy), expected, TOL, floor=FLOOR, what="section 3.2.1 F_t")


# ===========================================================================  3.2.2
def test_G61_the_slenderness_boundary() -> None:
    """`C_c = sqrt(2 pi^2 E / F_y)`.

    # expected: sqrt(2 * pi**2 * 210e9 / 355e6), worked here.
    """
    expected = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    assert_close(column_slenderness_parameter(FY, E), expected, TOL, floor=RATIO_FLOOR, what="C_c")


@pytest.mark.parametrize("k_l_over_r", [30.4, 60.8, 100.0, 108.0])
def test_G61_axial_compression_inelastic_branch(k_l_over_r: float) -> None:
    """Section 3.2.2(a), `KL/r < C_c`. Four points, the last just below the boundary.

    `30.4` and `60.8` are the hub arm's and the platform arm's own `KL/r` at `K = 1.0`;
    `60.8` is also the hub arm's at the locked `K = 2.0` (F6.md section 0, Q3).

    # expected:
    #     C_c = sqrt(2 pi^2 E / F_y)
    #     F_a = [1 - (KL/r)^2 / (2 C_c^2)] F_y
    #           / [5/3 + (3/8)(KL/r)/C_c - (KL/r)^3 / (8 C_c^3)]
    # worked here from the clause.
    """
    c_c = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    assert k_l_over_r < c_c, "this point is meant to be on the inelastic branch"
    r = k_l_over_r / c_c
    numerator = (1.0 - (k_l_over_r**2) / (2.0 * c_c**2)) * 355e6
    denominator = 5.0 / 3.0 + (3.0 / 8.0) * r - (r**3) / 8.0
    expected = numerator / denominator

    got, branch = allowable_axial_compression(k_l_over_r, D_OUTER, WALL, FY, E)
    assert branch == "inelastic", branch
    assert_close(got, expected, TOL, floor=FLOOR, what="section 3.2.2(a) F_a inelastic")


@pytest.mark.parametrize("k_l_over_r", [108.1, 121.5, 150.0, 200.0])
def test_G61_axial_compression_elastic_branch(k_l_over_r: float) -> None:
    """Section 3.2.2(a), `KL/r >= C_c`. Four points, the first just above the boundary.

    `121.5` is the platform arm's own `KL/r` at the locked `K = 2.0`, which is the crossing
    F6.md section 0 predicted.

    # expected: F_a = 12 pi^2 E / (23 (KL/r)^2), worked here.
    """
    c_c = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    assert k_l_over_r >= c_c, "this point is meant to be on the elastic branch"
    expected = 12.0 * math.pi**2 * 210e9 / (23.0 * k_l_over_r**2)

    got, branch = allowable_axial_compression(k_l_over_r, D_OUTER, WALL, FY, E)
    assert branch == "elastic", branch
    assert_close(got, expected, TOL, floor=FLOOR, what="section 3.2.2(a) F_a elastic")


def test_G61_the_two_compression_branches_are_CONTINUOUS_at_C_c() -> None:
    """The boundary itself, which is what a misplaced limit breaks.

    # expected: at `KL/r = C_c` the inelastic form reduces to
    #     (1 - 1/2) F_y / (5/3 + 3/8 - 1/8)
    # and the elastic form to
    #     12 pi^2 E / (23 C_c^2) = 6 F_y / 23
    # Both are worked here, and the clause is continuous only if they agree.
    """
    c_c = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    inelastic = (1.0 - 0.5) * 355e6 / (5.0 / 3.0 + 3.0 / 8.0 - 1.0 / 8.0)
    elastic = 12.0 * math.pi**2 * 210e9 / (23.0 * c_c**2)
    assert_close(inelastic, elastic, TOL, floor=FLOOR, what="section 3.2.2 continuity")
    assert_close(elastic, 6.0 * 355e6 / 23.0, TOL, floor=FLOOR, what="the closed form at C_c")


def test_G61_the_branch_the_LOCKED_K_puts_each_arm_on() -> None:
    """F6.md section 0 Q3 states the crossing; this is the assertion behind the sentence.

    # expected: r = 0.8227 m, L = 50 m and 25 m, K = 2.0; so KL/r = 121.5 and 60.8 against
    # C_c = 108.06 -- the platform arms elastic, the hub arms inelastic.
    """
    c_c = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    radius_of_gyration = 0.8227
    for length, want in ((50.0, "elastic"), (25.0, "inelastic")):
        k_l_over_r = 2.0 * length / radius_of_gyration
        got = "elastic" if k_l_over_r >= c_c else "inelastic"
        assert got == want, f"L = {length} m gives KL/r = {k_l_over_r:.1f}, read as {got}"


# ======================================================================  3.2.2(b), R741
def test_G61_local_buckling_does_NOT_reduce_a_compact_tube() -> None:
    """Section 3.2.2(b): `F_xc = F_y` for `D/t <= 60`. Both sides of the limit.

    # expected: exactly F_y below the limit, because the clause says so; and strictly less
    # than F_y above it.
    """
    # not-a-tolerance: the clause says F_xc IS F_y below the limit, so the equality is
    # exact by the clause and a band would admit a reduction the clause does not make.
    assert local_buckling_stress(D_OUTER, WALL, FY, E) == FY  # not-a-tolerance: exact by the clause
    assert local_buckling_stress(D_OUTER, D_OUTER / 60.0, FY, E) == FY  # not-a-tolerance: exact
    assert local_buckling_stress(D_OUTER, D_OUTER / 60.5, FY, E) < FY  # not-a-tolerance: exact


@pytest.mark.parametrize("d_over_t", [61.0, 100.0, 200.0, 300.0])
def test_G61_local_buckling_reduces_a_slender_tube(d_over_t: float) -> None:
    """Section 3.2.2(b): `F_xc = F_y [1.64 - 0.23 (D/t)^(1/4)] <= F_xe`, `F_xe = 2 C E t/D`.

    # expected: both forms worked here with C = 0.3, and the minimum taken.
    """
    wall = D_OUTER / d_over_t
    f_xe = 2.0 * 0.3 * 210e9 * wall / D_OUTER
    f_xc = 355e6 * (1.64 - 0.23 * d_over_t**0.25)
    expected = min(f_xc, f_xe)

    # not-a-tolerance: a statement about which SIDE of the clause this point is on, so
    # that a point which stopped being reduced would fail loudly instead of passing
    # against an unreduced allowable.
    assert expected < 355e6, "this point is meant to be reduced"  # not-a-tolerance: exact
    assert_close(
        local_buckling_stress(D_OUTER, wall, FY, E),
        expected,
        TOL,
        floor=FLOOR,
        what="section 3.2.2(b) F_xc",
    )


@pytest.mark.parametrize("d_over_t", [260.0, 300.0])
def test_G61_the_F_xe_HALF_of_the_clause_which_S355_CANNOT_REACH(d_over_t: float) -> None:
    """Section 3.2.2(b)'s `F_xe = 2 C E t / D`, at the grade where it actually governs.

    **THIS POINT WAS FOUND BY MEASUREMENT, NOT BY READING THE CLAUSE.** `F_xe` never
    governs `min(F_xc, F_xe)` at `F_y = 355 MPa` -- not at `D/t = 61`, `100`, `200` or
    `300`, and not at any `D/t` the clause admits. Solved, `F_xe` first governs at
    `D/t = 491.94` for S460, which is outside `D/t <= 300`, and at `D/t = 252.53` for S690,
    which is inside. So `ELASTIC_LOCAL_BUCKLING_C` and the whole elastic half of section
    3.2.2(b) are **inert at the grade F6 locks**, and a G6.1 that checked only the shipped
    material would have certified nothing about them.

    # expected: F_xe = 2 * 0.3 * 210e9 * t / D, worked here, and it is the MINIMUM.
    """
    wall = D_OUTER / d_over_t
    f_xe = 2.0 * 0.3 * 210e9 * wall / D_OUTER
    f_xc = FY_HIGH * (1.64 - 0.23 * d_over_t**0.25)
    assert f_xe < f_xc, (
        f"at F_y = 690 MPa, D/t = {d_over_t} this point is meant to be governed by F_xe; "
        f"F_xe = {f_xe:.4e} against F_xc = {f_xc:.4e}"
    )
    assert_close(
        local_buckling_stress(D_OUTER, wall, FY_HIGH, E),
        f_xe,
        TOL,
        floor=FLOOR,
        what="section 3.2.2(b) F_xe",
    )
    # and the same D/t at S355 is governed by the OTHER half -- one variable moved (BG0)
    assert_close(
        local_buckling_stress(D_OUTER, wall, FY, E),
        355e6 * (1.64 - 0.23 * d_over_t**0.25),
        TOL,
        floor=FLOOR,
        what="section 3.2.2(b) F_xc at S355, same D/t",
    )


def test_G61_a_section_outside_the_clause_is_REFUSED_not_extrapolated() -> None:
    """R741's counter-case. The locked plan asks for the refusal in its own words.

    Before the repair this returned `1.3610e+08 Pa`, branch `inelastic`, at `D/t = 100`
    with no refusal and no reduction.
    """
    with pytest.raises(ValueError, match="exceeds 300"):
        allowable_axial_compression(60.8, D_OUTER, D_OUTER / 500.0, FY, E)
    # R749: BRACKETED AT THE LIMIT ITSELF, the way the local-buckling limit is bracketed at
    # 60 and 60.5. `300` and `500` left `if d_t > 300.0 -> 303.0` green.
    allowable_axial_compression(60.8, D_OUTER, D_OUTER / 300.0, FY, E)
    with pytest.raises(ValueError, match="exceeds 300"):
        allowable_axial_compression(60.8, D_OUTER, D_OUTER / 300.1, FY, E)
    # and the reduction IS applied where the clause applies, rather than skipped
    got, branch = allowable_axial_compression(60.8, D_OUTER, D_OUTER / 100.0, FY, E)
    assert branch.endswith("_local"), branch
    assert got < allowable_axial_compression(60.8, D_OUTER, WALL, FY, E)[0]


def test_G61_the_local_buckling_LIMIT_is_what_decides_the_reduction() -> None:
    """`LOCAL_BUCKLING_DT`'s counter-case: move the limit past a point, the branch changes.

    A threshold does not respond to a relative nudge -- only a point within `eps` of it
    would -- so the injection is a DISPLACEMENT of the limit, not a scaling of it.
    """
    wall = D_OUTER / 61.0
    assert allowable_axial_compression(60.8, D_OUTER, wall, FY, E)[1] == "inelastic_local"
    old = api_wsd.LOCAL_BUCKLING_DT
    api_wsd.LOCAL_BUCKLING_DT = 62.0
    try:
        moved = allowable_axial_compression(60.8, D_OUTER, wall, FY, E)[1]
    finally:
        api_wsd.LOCAL_BUCKLING_DT = old
    assert moved == "inelastic", (
        "the local-buckling limit was raised past D/t = 61 and the branch did not change, "
        f"so nothing here is sized by LOCAL_BUCKLING_DT; got {moved!r}"
    )
    assert allowable_axial_compression(60.8, D_OUTER, wall, FY, E)[1] == "inelastic_local"


# ===========================================================================  3.2.3
def test_G61_bending_compact_branch() -> None:
    """Section 3.2.3: `F_b = 0.75 F_y` for `D/t <= 10340/F_y[MPa]`.

    # expected: 0.75 * 355e6 = 266.25e6 Pa, worked here. The limit is 10340/355 = 29.13,
    # so D/t = 29.0 is the point just inside it.
    """
    expected = 0.75 * 355e6
    assert expected == 266.25e6  # not-a-tolerance: the hand value, exact

    # R749: THE TWO LIMITS ARE PINNED AGAINST THE MODULE, which is what `limit_3` already
    # had and these two did not. The line that stood here was
    # `assert 10340.0 / 355.0 == 29.12676056338028` -- both sides written in this file,
    # neither reading `api_wsd`, so it held byte for byte under `10340 -> 10430` and under
    # `+1%`. CW0's triple-whose-command-cannot-fail shape, in an assertion.
    # **These are the two numbers R742 was about.**
    klass = section_class(D_OUTER, WALL, FY)
    assert klass.limit_1 == 29.12676056338028  # not-a-tolerance: the hand value of 10340/F_y
    assert klass.limit_2 == 58.25352112676056  # not-a-tolerance: the hand value of 20680/F_y
    for d_over_t in (13.888888888888889, 29.0):
        got, branch = allowable_bending(D_OUTER, D_OUTER / d_over_t, FY, E)
        assert branch == "compact", (d_over_t, branch)
        assert_close(got, expected, TOL, floor=FLOOR, what="section 3.2.3 compact")


def test_G61_the_two_branch_LIMITS_decide_the_branch_within_0_25_percent() -> None:
    """R749's second half: a point either side of each limit, inside its own neighbourhood.

    The nearest points the sweep had were `29.0`/`30.0` and `58.0`/`60.0` -- `0.44%` below
    and `3.0%` above each limit -- so a limit moved by a digit swap (`10340 -> 10430`, which
    is `+0.87%`) moved no point across a boundary. `29.2` and `58.3` are inside the gap.

    # expected: 10340/355 = 29.12676056338028 and 20680/355 = 58.25352112676056, so
    # D/t = 29.0 is compact and 29.2 is reduced_1; 58.0 is reduced_1 and 58.3 is reduced_2.
    """
    for d_over_t, want in (
        (29.0, "compact"),
        (29.2, "reduced_1"),
        (58.0, "reduced_1"),
        (58.3, "reduced_2"),
    ):
        got = allowable_bending(D_OUTER, D_OUTER / d_over_t, FY, E)[1]
        assert got == want, (
            f"D/t = {d_over_t} reads {got!r} and the clause gives {want!r}. The two limits "
            "are 29.12676056338028 and 58.25352112676056, and these four points bracket "
            "them to better than 0.25%."
        )


@pytest.mark.parametrize("d_over_t", [30.0, 40.0, 50.0, 58.0])
def test_G61_bending_first_reduced_branch(d_over_t: float) -> None:
    """Section 3.2.3: `F_b = [0.84 - 1.74 F_y D/(E t)] F_y`, capped at `0.75 F_y` (FB1).

    # expected: the clause worked here, then min() with the compact value -- which is
    # R742's cap, and which the clause's own SI conversion violates near this branch's
    # lower boundary. `58.0` is just inside 20680/355 = 58.25.
    """
    wall = D_OUTER / d_over_t
    raw = (0.84 - 1.74 * 355e6 * D_OUTER / (210e9 * wall)) * 355e6
    expected = min(raw, 0.75 * 355e6)
    got, branch = allowable_bending(D_OUTER, wall, FY, E)
    assert branch == "reduced_1", branch
    assert_close(got, expected, TOL, floor=FLOOR, what="section 3.2.3 reduced_1")


@pytest.mark.parametrize("d_over_t", [60.0, 100.0, 300.0, 700.0])
def test_G61_bending_second_reduced_branch(d_over_t: float) -> None:
    """Section 3.2.3: `F_b = [0.72 - 0.58 F_y D/(E t)] F_y`.

    # expected: the clause worked here. `D/t = 700` is inside FB1's limit 300000/F_y =
    # 845.07 and is included deliberately: it is the point nearest the sign change at
    # D/t = 0.72 E / (0.58 F_y) = 734.3.
    """
    wall = D_OUTER / d_over_t
    expected = min((0.72 - 0.58 * 355e6 * D_OUTER / (210e9 * wall)) * 355e6, 0.75 * 355e6)
    assert expected > 0.0, "this point must still be positive"
    got, branch = allowable_bending(D_OUTER, wall, FY, E)
    assert branch == "reduced_2", branch
    assert_close(got, expected, TOL, floor=FLOOR, what="section 3.2.3 reduced_2")


def test_G61_bending_never_exceeds_the_compact_value() -> None:
    """R742's counter-case, and FB1 asks for it as an assertion everywhere.

    Before the cap, `F_b = 267.785587 MPa` at `D/t = 29.1268` against the `266.25` cap, and
    it stayed above the cap all the way to `D/t = 30.5974`. The cause is the clause's own
    continuity point: `1500/F_y[ksi]` is continuous at `E = 29000 ksi = 199948 MPa` and
    this module runs at `210000 MPa`, so the converted limit and the SI `E` disagree.
    """
    cap = 0.75 * 355e6
    worst, where, checked = 0.0, 0.0, 0
    for i in range(1, 8460):
        d_over_t = i / 10.0
        try:
            f_b, _branch = allowable_bending(D_OUTER, D_OUTER / d_over_t, FY, E)
        except ValueError:
            continue
        checked += 1
        if f_b / cap > worst:
            worst, where = f_b / cap, d_over_t
    assert checked > 7000, f"only {checked} of 8459 D/t values returned -- domain too narrow"
    assert worst <= 1.0, f"F_b reaches {worst:.6f} of the 0.75 F_y cap at D/t = {where}"


def test_G61_a_non_positive_bending_allowable_is_REFUSED() -> None:
    """FB1's third limit admits one, the cap cannot see it, so it is refused separately.

    `0.72 - 0.58 F_y (D/t) / E` crosses zero at `D/t = 0.72 E / (0.58 F_y) = 734.3`, inside
    the `300000/F_y = 845.07` the directive sets.
    """
    crossing = 0.72 * 210e9 / (0.58 * 355e6)
    assert crossing == 734.3370568237008  # not-a-tolerance: the hand value of the crossing, exact
    assert allowable_bending(D_OUTER, D_OUTER / 734.0, FY, E)[0] > 0.0
    with pytest.raises(ValueError, match="not positive"):
        allowable_bending(D_OUTER, D_OUTER / 800.0, FY, E)


def test_G61_the_third_branch_LIMIT_is_what_decides_the_refusal() -> None:
    """`BENDING_THIRD_BRANCH_NUMERATOR`'s counter-case: move the limit past a point.

    The second of the two thresholds, same mechanism as the local-buckling limit: lower the
    numerator and a `D/t` that was inside the clause must be refused.
    """
    wall = D_OUTER / 700.0
    assert allowable_bending(D_OUTER, wall, FY, E)[1] == "reduced_2"
    old = api_wsd.BENDING_THIRD_BRANCH_NUMERATOR
    api_wsd.BENDING_THIRD_BRANCH_NUMERATOR = 200000.0
    try:
        with pytest.raises(ValueError, match="where API section 3.2.3 is not"):
            allowable_bending(D_OUTER, wall, FY, E)
    finally:
        api_wsd.BENDING_THIRD_BRANCH_NUMERATOR = old
    assert allowable_bending(D_OUTER, wall, FY, E)[1] == "reduced_2"


def test_G61_the_two_clauses_DISAGREE_about_the_slenderness_limit() -> None:
    """Section 3.2.2 refuses at a flat `D/t = 300`; section 3.2.3 at `300000/F_y = 845.07`.

    Both readings are in the module and they do not agree. Neither function is defective --
    each refuses rather than extrapolating, which is what the plan asks -- but the two
    numbers come from different transcriptions of the same edition, and the narrower one is
    what binds any member carrying both bending and compression. **Flagged for Xabier**:
    the editions available to me print a flat `300` in section 3.2.3's third range, where
    FB1 gives `300000/F_y`.
    """
    limit_3 = section_class(D_OUTER, D_OUTER / 100.0, FY).limit_3
    assert limit_3 == 845.0704225352113  # not-a-tolerance: the hand value of 300000/355, exact
    # bending admits D/t = 700; compression does not
    assert allowable_bending(D_OUTER, D_OUTER / 700.0, FY, E)[1] == "reduced_2"
    with pytest.raises(ValueError, match="exceeds 300"):
        allowable_axial_compression(60.8, D_OUTER, D_OUTER / 700.0, FY, E)
    # so a combined check on such a section refuses, which is the conservative direction
    with pytest.raises(ValueError, match="exceeds 300"):
        _member(axial_n=-1.0e6, moment_y_nm=1.0e6, wall_m=D_OUTER / 700.0)


# ===========================================================================  3.2.4
@pytest.mark.parametrize("fy, hand_f_v", [(355e6, 142.0e6), (275e6, 110.0e6)])
def test_G61_shear_and_torsion_allowable(fy: float, hand_f_v: float) -> None:
    """Section 3.2.4: `F_v = 0.4 F_y`, and the same allowable for torsional shear.

    # expected: 0.4 * F_y, worked here -- 142.0e6 Pa at S355 and 110.0e6 Pa at S275.
    """
    expected = 0.4 * fy
    assert expected == hand_f_v  # not-a-tolerance: two spellings of one product, exact
    assert_close(allowable_shear(fy), expected, TOL, floor=FLOOR, what="section 3.2.4 F_v")


def test_G61_the_beam_shear_stress_uses_HALF_the_area() -> None:
    """Section 3.2.4(a) takes `f_v = V / (0.5 A)`, not `V / A`.

    # expected: with V = 1e6 N and A = 1.3119290921390976 m^2, the clause gives
    #     1e6 / (0.5 * 1.3119290921390976)
    # worked here -- which is 2x what V/A gives. **The direction matters**: using A would
    # read 2x LOW on every shear utilisation in the table.
    """
    expected = 1.0e6 / (0.5 * AREA)
    got = _member(shear_y_n=1.0e6)
    assert_close(got.f_v, expected, TOL, floor=FLOOR, what="section 3.2.4(a) f_v")
    # THE DIRECTION, as its own comparison: 0.5 A in the denominator is 2x V/A, and using
    # A would read 2x LOW on every shear utilisation in the table.
    assert_close(
        got.f_v, 2.0 * 1.0e6 / AREA, TOL, floor=FLOOR, what="section 3.2.4(a) the 2x direction"
    )


def test_G61_the_shear_stress_is_the_RESULTANT_of_the_two_planes() -> None:
    """`f_v = sqrt(V_y^2 + V_z^2) / (0.5 A)`, not the larger component.

    # expected: with V_y = V_z = 1e6 the resultant is sqrt(2) * 1e6, so
    #     sqrt(2) * 1e6 / (0.5 * A)
    # worked here.
    """
    expected = math.sqrt(2.0) * 1.0e6 / (0.5 * AREA)
    assert_close(
        _member(shear_y_n=1.0e6, shear_z_n=1.0e6).f_v,
        expected,
        TOL,
        floor=FLOOR,
        what="section 3.2.4(a) f_v resultant",
    )


def test_G61_the_torsional_shear_stress() -> None:
    """Section 3.2.4's torsion form on `W_t = 2J/D`.

    # expected: T / W_t = 4e6 / 1.4208, worked here.
    """
    assert_close(
        _member(torsion_nm=4.0e6).f_vt,
        4.0e6 / W_TORSION,
        TOL,
        floor=FLOOR,
        what="section 3.2.4 f_vt",
    )


# ===========================================================================  3.3
def test_G61_tension_plus_bending_interaction() -> None:
    """Section 3.3.1: `f_a / (0.6 F_y) + sqrt(f_by^2 + f_bz^2) / F_b <= 1`.

    # expected: worked here from the stresses, with F_b = 0.75 F_y for this compact tube.
    # The bending term is the RESULTANT, which is what section 3.3 is written on.
    """
    n, my, mz = 1.0e6, 5.0e7, 3.0e7
    f_a = n / AREA
    f_b = math.hypot(my / W_SECTION, mz / W_SECTION)
    expected = f_a / (0.6 * 355e6) + f_b / (0.75 * 355e6)

    got = _member(axial_n=n, moment_y_nm=my, moment_z_nm=mz)
    assert got.in_tension
    assert_close(got.u_combined, expected, TOL, floor=RATIO_FLOOR, what="section 3.3.1")
    assert got.governing == "3.3.1 interaction", got.governing


def test_G61_a_member_at_EXACTLY_zero_axial_reads_as_TENSION() -> None:
    """R749's third: the tension/compression switch, bracketed at its own boundary.

    `in_tension = axial_n >= 0.0`, so zero is TENSION and the allowable is `0.6 F_y` rather
    than the column value. `>= 0.0 -> > 0.0` left all 65 tests green, because no point sat
    at exactly zero: every axial load in the file is strictly positive or strictly
    negative. This is the one point that distinguishes them.

    # expected: at N = 0 the axial branch is "tension" and F_a = 0.6 F_y = 213.0e6 Pa; one
    # ULP below zero it is the column value, which at KL/r = 121.5 is the elastic branch.
    """
    at_zero = _member(axial_n=0.0, moment_y_nm=1.0e6, k_l_over_r=121.5)
    assert at_zero.in_tension
    assert at_zero.axial_branch == "tension", at_zero.axial_branch
    assert_close(
        at_zero.allow_axial, 0.6 * 355e6, TOL, floor=FLOOR, what="F_a at exactly zero axial"
    )
    # and one ULP below zero is the other side, so the boundary is bracketed rather than
    # approached from one side
    below = _member(axial_n=-5e-324, moment_y_nm=1.0e6, k_l_over_r=121.5)
    assert not below.in_tension
    assert below.axial_branch == "elastic", below.axial_branch


def test_G61_the_bending_term_is_the_RESULTANT_and_not_the_sum() -> None:
    """One variable moved: the same total moment, split two ways (BG0).

    # expected: My = Mz = M/sqrt(2) gives the same resultant as My = M, Mz = 0, so
    # `u_bending` must be identical; summing the two components instead would give
    # sqrt(2) = 1.414x more.
    """
    total = 5.0e7
    one_plane = _member(moment_y_nm=total).u_bending
    two_planes = _member(
        moment_y_nm=total / math.sqrt(2.0), moment_z_nm=total / math.sqrt(2.0)
    ).u_bending
    assert_close(one_plane, two_planes, TOL, floor=RATIO_FLOOR, what="section 3.3 resultant")
    summed = (total / math.sqrt(2.0) + total / math.sqrt(2.0)) / W_SECTION / (0.75 * 355e6)
    assert_close(
        summed,
        math.sqrt(2.0) * one_plane,
        TOL,
        floor=RATIO_FLOOR,
        what="the sqrt(2) a component SUM would have given",
    )


# `F_e'` at `KL/r = 30.4`, which the weak-end point below is placed by.
_F_E_AT_30_4 = 12.0 * math.pi**2 * 210e9 / (23.0 * 30.4**2)

AMPLIFIED_POINTS = [
    # (KL/r, N, My, the branch of 3.2.2 it is on). CHOSEN BY MEASUREMENT -- see below.
    (60.8, -1.0e8, 1.0e8, "inelastic"),
    (121.5, -1.0e7, 1.0e8, "elastic"),
    # **THE WEAK END (R750), AND IT IS THE POINT THE COUNTER IS DECLARED FROM.** The two
    # above were chosen for the STRONGEST `C_m` resolution, which is the direction that
    # makes the gate look sensitive; a dense sweep of the admissible domain puts the
    # MINIMUM at `KL/r = 30.4`, `f_a/F_e' = 0.40`, `My = 1e6`, where the axial term
    # dominates `u_combined` and `C_m`'s share of it is `3.074923e-03`.
    (30.4, -0.4 * _F_E_AT_30_4 * AREA, 1.0e6, "inelastic"),
]


@pytest.mark.parametrize("k_l_over_r, n, my, branch", AMPLIFIED_POINTS)
def test_G61_compression_plus_bending_AMPLIFIED_form(
    k_l_over_r: float, n: float, my: float, branch: str
) -> None:
    """Section 3.3.2's amplified form, at a point where it actually governs.

    **THE POINT WAS CHOSEN BY MEASUREMENT.** Section 3.3.2 requires BOTH forms and the
    larger governs. At a moderate axial load the SIMPLE form wins -- at `N = -1e6`,
    `My = 5e7`, `Mz = 3e7`, `KL/r = 121.5` the module returns `0.31185967`, which is the
    simple value, and `F_a`, `F_e'` and `C_m` do not appear in it at all. A hand
    calculation taken there is correct and measures nothing: the entire amplified branch
    could be wrong and `u_combined` would still agree.

    # expected, both forms worked here:
    #     F_e' = 12 pi^2 E / (23 (KL/r)^2)
    #     amplified = f_a/F_a + C_m sqrt(f_by^2+f_bz^2) / [(1 - f_a/F_e') F_b]
    #     simple    = f_a/(0.6 F_y) + sqrt(f_by^2+f_bz^2) / F_b
    #     u         = max(amplified, simple)
    """
    f_a = abs(n) / AREA
    f_b = my / W_SECTION
    c_c = math.sqrt(2.0 * math.pi**2 * 210e9 / 355e6)
    if branch == "inelastic":
        r = k_l_over_r / c_c
        f_a_allow = (
            (1.0 - (k_l_over_r**2) / (2.0 * c_c**2))
            * 355e6
            / (5.0 / 3.0 + (3.0 / 8.0) * r - (r**3) / 8.0)
        )
    else:
        f_a_allow = 12.0 * math.pi**2 * 210e9 / (23.0 * k_l_over_r**2)
    f_e = 12.0 * math.pi**2 * 210e9 / (23.0 * k_l_over_r**2)
    amplified = f_a / f_a_allow + CM_JOINT_TRANSLATION * f_b / ((1.0 - f_a / f_e) * 0.75 * 355e6)
    simple = f_a / (0.6 * 355e6) + f_b / (0.75 * 355e6)

    assert amplified > simple, (
        f"this point is meant to be governed by the AMPLIFIED form; amplified = "
        f"{amplified:.6f} against simple = {simple:.6f}. A point where the simple form "
        "governs measures nothing about F_a, F_e' or C_m."
    )
    got = _member(axial_n=n, moment_y_nm=my, k_l_over_r=k_l_over_r)
    assert not got.in_tension
    assert got.axial_branch == branch, got.axial_branch
    assert_close(got.u_combined, amplified, TOL, floor=RATIO_FLOOR, what="section 3.3.2")
    assert got.governing == "3.3.2 interaction", got.governing


def test_G61_compression_plus_bending_SIMPLE_form_governs_where_it_should() -> None:
    """The other half of `max(amplified, simple)`, which is also the clause.

    # expected: at N = -1e6, My = 5e7, Mz = 3e7, KL/r = 121.5 the simple form is the larger
    # and `u_combined` is it: f_a/(0.6 F_y) + f_b/F_b, worked here.
    """
    n, my, mz, kl = -1.0e6, 5.0e7, 3.0e7, 121.5
    f_a = abs(n) / AREA
    f_b = math.hypot(my / W_SECTION, mz / W_SECTION)
    simple = f_a / (0.6 * 355e6) + f_b / (0.75 * 355e6)
    f_a_allow = 12.0 * math.pi**2 * 210e9 / (23.0 * kl**2)
    amplified = f_a / f_a_allow + CM_JOINT_TRANSLATION * f_b / (
        (1.0 - f_a / f_a_allow) * 0.75 * 355e6
    )
    assert simple > amplified, "this point is meant to be governed by the simple form"

    got = _member(axial_n=n, moment_y_nm=my, moment_z_nm=mz, k_l_over_r=kl)
    assert_close(got.u_combined, simple, TOL, floor=RATIO_FLOOR, what="section 3.3.2 simple")


def test_G61_a_LARGER_Cm_RAISES_the_compression_utilisation() -> None:
    """R743's direction, as a measurement rather than a sentence.

    The module's comment called `0.85` "the conservative reading", which is backwards:
    `C_m` MULTIPLIES the bending term in section 3.3.2, so `C_m = 1.0` gives a LARGER
    utilisation and `0.85` is the less onerous of the two. Stating it backwards is how a
    lever gets mis-weighted in a cover note, which is why FB2 asks for the `C_m = 1.0`
    column beside the `K = 1.0` one.

    Taken at an amplified-governing point, because at a simple-governing point `C_m` has no
    effect at all and the comparison would be vacuous in the direction being asserted.
    """
    k_l_over_r, n, my, _branch = AMPLIFIED_POINTS[1]
    low = _member(axial_n=n, moment_y_nm=my, k_l_over_r=k_l_over_r, cm=0.85)
    high = _member(axial_n=n, moment_y_nm=my, k_l_over_r=k_l_over_r, cm=1.0)
    assert high.u_combined > low.u_combined, (
        f"C_m = 1.0 gave {high.u_combined!r} and C_m = 0.85 gave {low.u_combined!r}. A "
        "larger C_m must raise the utilisation."
    )
    assert CM_JOINT_TRANSLATION == 0.85, CM_JOINT_TRANSLATION  # not-a-tolerance: FB2 sets it, exact


def test_G61_the_module_DEFAULT_for_Cm_is_the_declared_constant() -> None:
    """The default is bound at import, so the global and the default can drift apart.

    Found while building the counter-case family: scaling `api_wsd.CM_JOINT_TRANSLATION` at
    run time produced a response of exactly `0.000000e+00`, because `check_member`'s `cm`
    default was evaluated when the module was imported. Production is unaffected -- a
    source edit is picked up on the next import -- but it means the counter-case has to
    inject through the parameter, and it means nothing otherwise asserts that the default
    IS the declared constant. This is that assertion.
    """
    default = inspect.signature(check_member).parameters["cm"].default
    assert default == CM_JOINT_TRANSLATION, (
        f"check_member's cm default is {default!r} and CM_JOINT_TRANSLATION is "
        f"{CM_JOINT_TRANSLATION!r}"
    )


def test_G61_the_euler_stress_equals_the_elastic_allowable() -> None:
    """`F_e'` and the elastic `F_a` are the same expression; a divergence is a typo.

    # expected: both are 12 pi^2 E / (23 (KL/r)^2), worked here.

    **AND THE EQUALITY HAS A CONSEQUENCE** that the utilisation counter-case below runs
    into: on the elastic branch `F_a / F_e' = 1` exactly, so `u_axial = 1` is also where
    section 3.3.2's amplification is singular.
    """
    kl = 150.0
    expected = 12.0 * math.pi**2 * 210e9 / (23.0 * kl**2)
    assert_close(euler_stress(kl, E), expected, TOL, floor=FLOOR, what="F_e'")
    f_a, branch = allowable_axial_compression(kl, D_OUTER, WALL, FY, E)
    assert branch == "elastic"
    assert_close(f_a, expected, TOL, floor=FLOOR, what="elastic F_a against F_e'")
    assert f_a / euler_stress(kl, E) == 1.0


def test_G61_a_member_past_elastic_buckling_is_REFUSED() -> None:
    """Section 3.3.2's amplification is singular at `f_a = F_e'`; the module refuses there.

    # expected: F_e' at KL/r = 121.5 is 73252068.74097985 Pa, so N = F_e' * A is the
    # boundary.
    """
    f_e = 12.0 * math.pi**2 * 210e9 / (23.0 * 121.5**2)
    assert f_e == 73252068.74097985  # not-a-tolerance: exact
    _member(axial_n=-0.99 * f_e * AREA, moment_y_nm=1.0e6, k_l_over_r=121.5)
    with pytest.raises(ValueError, match="reaches the Euler stress"):
        _member(axial_n=-1.01 * f_e * AREA, moment_y_nm=1.0e6, k_l_over_r=121.5)


# =============================================  the counter-cases on the COMPARISON itself
COEFFICIENTS = [
    "ALLOWABLE_TENSION_FACTOR",
    "ALLOWABLE_SHEAR_FACTOR",
    "BEAM_SHEAR_AREA_FACTOR",
    "ELASTIC_LOCAL_BUCKLING_C",
    "CM_JOINT_TRANSLATION",  # injected through the parameter, not the global -- see above
]
_FA_POINTS = (30.4, 60.8, 100.0, 108.0, 108.1, 121.5, 150.0, 200.0)
_FXC_POINTS = (61.0, 100.0, 200.0, 300.0)
_FXE_POINTS = (260.0, 300.0)
_FB_POINTS = (
    13.888888888888889,
    29.0,
    29.2,
    30.0,
    40.0,
    50.0,
    58.0,
    58.3,
    60.0,
    100.0,
    300.0,
    700.0,
)
"""R749: `29.2` and `58.3` are inside each branch limit's own neighbourhood. The sweep's
nearest points were `29.0`/`30.0` and `58.0`/`60.0` -- `0.44%` below each limit and `3.0%`
above -- so a limit moved by a digit swap crossed no point and nothing reddened."""


def _quantities(cm: float | None = None) -> dict[str, float]:
    """Every quantity this file hand-calculates, at the points it uses -- from the MODULE.

    This is the domain of the ceiling, and therefore the domain the counter-case family is
    measured over. A family measured on a narrower domain than the ceiling it defends
    reports the strongest member as the quantity's, which is what R708 and R710 both were.
    """
    cm_v = CM_JOINT_TRANSLATION if cm is None else cm
    q: dict[str, float] = {
        "3.2.1 F_t": allowable_axial_tension(FY),
        "C_c": column_slenderness_parameter(FY, E),
        "3.2.4 F_v": allowable_shear(FY),
    }
    for kl in _FA_POINTS:
        q[f"3.2.2 F_a KL/r={kl}"] = allowable_axial_compression(kl, D_OUTER, WALL, FY, E)[0]
    for dt in _FXC_POINTS:
        q[f"3.2.2b F_xc D/t={dt}"] = local_buckling_stress(D_OUTER, D_OUTER / dt, FY, E)
    for dt in _FXE_POINTS:
        q[f"3.2.2b F_xe D/t={dt} Fy=690"] = local_buckling_stress(D_OUTER, D_OUTER / dt, FY_HIGH, E)
    for dt in _FB_POINTS:
        q[f"3.2.3 F_b D/t={dt}"] = allowable_bending(D_OUTER, D_OUTER / dt, FY, E)[0]
    m = _member(shear_y_n=1.0e6, torsion_nm=4.0e6)
    q["3.2.4a f_v"], q["3.2.4 f_vt"] = m.f_v, m.f_vt
    q["3.3.1 U"] = _member(axial_n=1.0e6, moment_y_nm=5.0e7, moment_z_nm=3.0e7).u_combined
    for kl, n, my, _branch in AMPLIFIED_POINTS:
        q[f"3.3.2 U KL/r={kl}"] = _member(
            axial_n=n, moment_y_nm=my, k_l_over_r=kl, cm=cm_v
        ).u_combined
    return q


def _hand_quantities() -> dict[str, float]:
    """The same quantities, BY HAND. The clean side of the comparison, measured once."""
    c_c = math.sqrt(2.0 * math.pi**2 * E / FY)
    h: dict[str, float] = {"3.2.1 F_t": 0.6 * FY, "C_c": c_c, "3.2.4 F_v": 0.4 * FY}
    for kl in _FA_POINTS:
        if kl < c_c:
            r = kl / c_c
            h[f"3.2.2 F_a KL/r={kl}"] = (
                (1.0 - (kl**2) / (2.0 * c_c**2)) * FY / (5.0 / 3.0 + (3.0 / 8.0) * r - (r**3) / 8.0)
            )
        else:
            h[f"3.2.2 F_a KL/r={kl}"] = 12.0 * math.pi**2 * E / (23.0 * kl**2)
    for dt in _FXC_POINTS:
        h[f"3.2.2b F_xc D/t={dt}"] = min(
            FY * (1.64 - 0.23 * dt**0.25), 2.0 * 0.3 * E * (D_OUTER / dt) / D_OUTER
        )
    for dt in _FXE_POINTS:
        h[f"3.2.2b F_xe D/t={dt} Fy=690"] = min(
            FY_HIGH * (1.64 - 0.23 * dt**0.25), 2.0 * 0.3 * E * (D_OUTER / dt) / D_OUTER
        )
    for dt in _FB_POINTS:
        if dt <= 10340.0 / 355.0:
            h[f"3.2.3 F_b D/t={dt}"] = 0.75 * FY
        elif dt <= 20680.0 / 355.0:
            h[f"3.2.3 F_b D/t={dt}"] = min(
                (0.84 - 1.74 * FY * D_OUTER / (E * (D_OUTER / dt))) * FY, 0.75 * FY
            )
        else:
            h[f"3.2.3 F_b D/t={dt}"] = min(
                (0.72 - 0.58 * FY * D_OUTER / (E * (D_OUTER / dt))) * FY, 0.75 * FY
            )
    h["3.2.4a f_v"] = math.hypot(1.0e6, 0.0) / (0.5 * AREA)
    h["3.2.4 f_vt"] = 4.0e6 / W_TORSION
    f_a = 1.0e6 / AREA
    f_b = math.hypot(5.0e7 / W_SECTION, 3.0e7 / W_SECTION)
    h["3.3.1 U"] = f_a / (0.6 * FY) + f_b / (0.75 * FY)
    for kl, n, my, branch in AMPLIFIED_POINTS:
        f_a, f_b = abs(n) / AREA, my / W_SECTION
        if branch == "inelastic":
            r = kl / c_c
            f_a_allow = (
                (1.0 - (kl**2) / (2.0 * c_c**2)) * FY / (5.0 / 3.0 + (3.0 / 8.0) * r - (r**3) / 8.0)
            )
        else:
            f_a_allow = 12.0 * math.pi**2 * E / (23.0 * kl**2)
        f_e = 12.0 * math.pi**2 * E / (23.0 * kl**2)
        h[f"3.3.2 U KL/r={kl}"] = max(
            f_a / f_a_allow + CM_JOINT_TRANSLATION * f_b / ((1.0 - f_a / f_e) * 0.75 * FY),
            f_a / (0.6 * FY) + f_b / (0.75 * FY),
        )
    return h


def _worst_move(clean: dict[str, float], hurt: dict[str, float]) -> tuple[float, str]:
    """The MAXIMUM relative move over the points. Non-vacuity: something responded."""
    worst, where = 0.0, "-"
    for key, value in clean.items():
        scale = max(abs(value), abs(hurt[key]))
        rel = abs(value - hurt[key]) / scale if scale else 0.0
        if rel > worst:
            worst, where = rel, key
    return worst, where


def _weakest_live_move(clean: dict[str, float], hurt: dict[str, float]) -> tuple[float, str]:
    """The MINIMUM relative move over the points that respond AT ALL -- EH4's weakening
    direction, and the one this file never formed (R750).

    `weakest = min(responses)` over coefficients, where each response was itself a MAX over
    points, is min-over-coefficients of max-over-points. The declared margin was quoted in
    that direction, so a configuration where the gate resolves a defect 267x more weakly
    than published sat outside everything the file looked at.

    A point whose response is EXACTLY ZERO is skipped rather than returned, because zero is
    VACUOUS and not a failure -- and for `C_m` the zero is reachable: its share of
    `u_combined` tends to zero as the bending term does, so the infimum over the whole
    admissible domain is `0` and is ATTAINED. **No constant can be a floor beneath every
    admissible configuration**, which is why the counter is a floor beneath the gate's own
    points with those points placed AT the weak end.
    """
    best, where = float("inf"), "-"
    for key, value in clean.items():
        scale = max(abs(value), abs(hurt[key]))
        rel = abs(value - hurt[key]) / scale if scale else 0.0
        if 0.0 < rel < best:
            best, where = rel, key
    return best, where


def _injected(coefficient: str) -> dict[str, float]:
    """The 35 quantities with ONE clause coefficient scaled by the declared injection."""
    if coefficient == "CM_JOINT_TRANSLATION":
        # the module global is inert here: the default is bound at import (see above)
        return _quantities(cm=CM_JOINT_TRANSLATION * (1.0 + F6_API_CLAUSE_INJECTION_EPS))
    old = getattr(api_wsd, coefficient)
    setattr(api_wsd, coefficient, old * (1.0 + F6_API_CLAUSE_INJECTION_EPS))
    try:
        hurt = _quantities()
    finally:
        setattr(api_wsd, coefficient, old)
    assert getattr(api_wsd, coefficient) == old, "the injection was not undone"
    return hurt


def test_the_two_quantity_SETS_are_the_same_35_points() -> None:
    """A key on one side only would silently drop a point from the clean worst.

    A narrower domain than the ceiling defends reports the strongest member as the
    quantity's, which is what R708, R710 and now R750 all were.
    """
    hand, module = set(_hand_quantities()), set(_quantities())
    assert hand == module, f"only on one side: {sorted(hand ^ module)}"
    assert len(hand) == 35, len(hand)


@pytest.mark.parametrize("coefficient", COEFFICIENTS)
def test_an_INJECTED_clause_coefficient_exceeds_the_declared_COUNTER(coefficient: str) -> None:
    """The counter-case: a transcription defect in a clause coefficient must be caught.

    Each coefficient is scaled by `1 + F6_API_CLAUSE_INJECTION_EPS`, one at a time, which is
    what a transcription defect is -- `0.6` typed for `0.66`. The response must exceed
    `F6_API_CLAUSE_AGREEMENT_COUNTER`, which sits below the weakest LIVE POINT of the
    family -- not below the weakest coefficient's STRONGEST point, which is what it meant
    for one round (R750).
    """
    clean, hurt = _quantities(), _injected(coefficient)
    strongest, where_max = _worst_move(clean, hurt)
    weakest, where_min = _weakest_live_move(clean, hurt)

    # NON-VACUITY: something responded at all.
    assert strongest > F6_API_CLAUSE_AGREEMENT, (
        f"scaling {coefficient} by 1 + {F6_API_CLAUSE_INJECTION_EPS:g} moves NOTHING above "
        f"the ceiling -- its strongest point is {strongest:.6e} ({where_max})"
    )
    # **AND THE COUNTER IS ASSERTED AGAINST THE MINIMUM OVER LIVE POINTS (R750)**, which is
    # EH4's weakening direction. It was the MAXIMUM, so a point at which the gate resolves
    # the same defect `267x` more weakly satisfied it without ever being looked at.
    assert weakest > F6_API_CLAUSE_AGREEMENT_COUNTER, (
        f"scaling {coefficient} by 1 + {F6_API_CLAUSE_INJECTION_EPS:g} moves its WEAKEST "
        f"live point by only {weakest:.6e} ({where_min}), at or below the declared counter "
        f"{F6_API_CLAUSE_AGREEMENT_COUNTER:.6e}. Its strongest point moves "
        f"{strongest:.6e}, which is the direction that makes the gate look sensitive."
    )


def test_the_ceiling_and_its_counter_BRACKET_the_family_BOTH_ways() -> None:
    """EH4: both directions, including the two that WEAKEN the gate.

    The strengthening direction is how far the ceiling may FALL before a clean point
    reddens; the weakening direction is how far it may RISE before the weakest injection
    passes. Both edges must clear the window rule's floor.
    """
    clean_worst, clean_where = _worst_move(_quantities(), _hand_quantities())
    assert clean_worst > 0.0, (
        "every one of the 35 points is bit-identical, so the lower edge of the window is "
        "unbounded and the ceiling is pinned by nothing from below"
    )
    responses = [(_weakest_live_move(_quantities(), _injected(c))[0], c) for c in COEFFICIENTS]
    assert len(responses) == 5, responses
    assert all(
        r > 0.0 for r, _ in responses
    ), f"a family member with response 0.0 is VACUOUS, not passing: {responses}"
    weakest, weakest_name = min(responses)

    lower_edge = F6_API_CLAUSE_AGREEMENT / clean_worst
    upper_edge = weakest / F6_API_CLAUSE_AGREEMENT
    assert lower_edge > F4_WINDOW_RULE_MIN_EDGE, (
        f"the ceiling clears the clean worst ({clean_worst:.6e} at {clean_where}) by only "
        f"{lower_edge:.4g}x -- a correct transcription could redden on another platform"
    )
    assert upper_edge > F4_WINDOW_RULE_MIN_EDGE, (
        f"the ceiling sits only {upper_edge:.4g}x below the weakest injection "
        f"({weakest:.6e}, {weakest_name}) -- it could be widened past a defect it must catch"
    )
    assert weakest > F6_API_CLAUSE_AGREEMENT_COUNTER, (
        f"the declared counter {F6_API_CLAUSE_AGREEMENT_COUNTER:.6e} is ABOVE the weakest "
        f"live response {weakest:.6e} ({weakest_name}), so that member does not satisfy it"
    )


# ============================================  the counter-cases on the UTILISATIONS (plan)
UTILISATION_COUNTER_CASES = [
    # (channel, the loads the clause's closed form puts at U = 1.0, KL/r, the clause
    #  `governing` must name)
    ("tension", {"axial_n": 0.6 * FY * AREA}, 60.8, "3.2.1 tension"),
    ("bending", {"moment_y_nm": 0.75 * FY * W_SECTION}, 60.8, "3.2.3 bending"),
    ("beam shear", {"shear_y_n": 0.4 * FY * 0.5 * AREA}, 60.8, "3.2.4 beam shear"),
    ("torsion", {"torsion_nm": 0.4 * FY * W_TORSION}, 60.8, "3.2.4 torsional shear"),
    # compression on the INELASTIC branch -- see the docstring below for why not 121.5
    ("compression", {"axial_n": -1.0}, 60.8, "3.2.2 compression"),
    (
        "interaction",
        {
            "axial_n": 0.5 * 0.6 * FY * AREA,
            "moment_y_nm": 0.5 * 0.75 * FY * W_SECTION,
        },
        60.8,
        "3.3.1 interaction",
    ),
]


@pytest.mark.parametrize(
    "channel, loads, k_l_over_r, clause",
    UTILISATION_COUNTER_CASES,
    ids=[c[0] for c in UTILISATION_COUNTER_CASES],
)
def test_each_check_REDDENS_under_the_load_the_plan_asks_for(
    channel: str, loads: dict[str, float], k_l_over_r: float, clause: str
) -> None:
    """The locked plan's counter-case per check: "an injected input that must push the
    utilisation past 1.0, and the injection size is a declared constant with a plan row".

    The load that puts each channel at exactly `1.0` is in closed form -- `F_t A`, `F_b W`,
    `F_v (0.5 A)`, `F_v W_t`, `F_a A`, and half the budget in each term for the interaction
    -- so the injection is ONE declared factor rather than six calibrated loads.

    **THE COMPRESSION CASE IS TAKEN ON THE INELASTIC BRANCH AND THE REASON IS THE CLAUSE,
    not the test.** On section 3.2.2's elastic branch `F_a` and section 3.3.2's `F_e'` are
    the same expression, so `F_a/F_e' = 1.000000` exactly and `u_axial = f_a/F_a = 1`
    coincides with the singularity of `1/(1 - f_a/F_e')`. At `KL/r = 121.5` a
    pure-compression counter-case therefore hits the module's Euler refusal instead of
    reaching `U = 1.0`. At `KL/r = 60.8`, `F_a/F_e' = 0.550539` and it reaches it.
    """
    if channel == "compression":
        # F_a is not a closed form in F_y alone, so it is taken from the clause's own
        # branch at this KL/r -- which the inelastic-branch test above hand-calculates
        f_a_allow, branch = allowable_axial_compression(k_l_over_r, D_OUTER, WALL, FY, E)
        assert branch == "inelastic", branch
        loads = {"axial_n": -f_a_allow * AREA}

    at_unity = _member(k_l_over_r=k_l_over_r, **loads)
    assert_close(
        at_unity.utilisation,
        1.0,
        TOL,
        floor=RATIO_FLOOR,
        what=f"the {channel} load is meant to put the channel at exactly 1.0",
    )
    assert at_unity.governing == clause, at_unity.governing

    injected = {k: v * F6_API_UTILISATION_COUNTER_FACTOR for k, v in loads.items()}
    reddened = _member(k_l_over_r=k_l_over_r, **injected)
    assert reddened.utilisation > 1.0, (
        f"the {channel} check does not redden at {F6_API_UTILISATION_COUNTER_FACTOR}x the "
        f"load that puts it at unity: {reddened.utilisation!r}. A check that cannot redden "
        "certifies nothing."
    )
    assert reddened.governing == clause, (
        f"at {F6_API_UTILISATION_COUNTER_FACTOR}x the {channel} load the governing clause "
        f"moved to {reddened.governing!r}; the counter-case is then testing a different "
        "clause than the one it names"
    )
    # the branch did not move under the injection -- otherwise this is a different check
    assert reddened.bending_branch == at_unity.bending_branch
    assert reddened.axial_branch == at_unity.axial_branch


def test_the_compression_counter_case_CANNOT_be_taken_on_the_elastic_branch() -> None:
    """The measurement behind the docstring above, as an assertion (BG0).

    One variable moved: the same `U = 1.0` construction at `KL/r = 121.5` instead of
    `60.8`. It does not return a utilisation at all -- it refuses.
    """
    f_a_allow, branch = allowable_axial_compression(121.5, D_OUTER, WALL, FY, E)
    assert branch == "elastic"
    assert f_a_allow / euler_stress(121.5, E) == 1.0
    with pytest.raises(ValueError, match="reaches the Euler stress"):
        _member(axial_n=-f_a_allow * AREA, k_l_over_r=121.5)
    # while on the inelastic branch the same construction reaches unity
    f_a_allow, branch = allowable_axial_compression(60.8, D_OUTER, WALL, FY, E)
    assert branch == "inelastic"
    # It is this ratio that makes the inelastic branch admit the counter-case the elastic
    # branch refuses.
    assert f_a_allow / euler_stress(60.8, E) == 0.5505390764073391  # not-a-tolerance: exact
    assert_close(
        _member(axial_n=-f_a_allow * AREA, k_l_over_r=60.8).utilisation,
        1.0,
        TOL,
        floor=RATIO_FLOOR,
        what="the inelastic-branch construction reaches unity",
    )
