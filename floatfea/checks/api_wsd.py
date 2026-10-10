"""API RP 2A-WSD tubular member checks, closed form, one function per clause.

**THESE ARE A SIZING SCREEN, NOT A COMPLIANCE CALCULATION.** `PLAN.md`'s framing, adopted
rather than softened: API RP 2A and ISO 19902 are written for fixed jackets and neither is a
certification basis for a floating platform. Certification lives in the DNV series, and
shell buckling of the buoy cans is DNV-RP-C202 territory. F6 exists to find the governing
members and their approximate utilisations, and every report it feeds says so on its face.

WHY WORKING-STRESS DESIGN. `PLAN.md`'s locked decision: WSD's clauses are compact
closed-form equations, so each one can be verified against an independent hand calculation
-- which is what G6.1 requires when the checks are implemented from scratch. ISO 19902 is
LRFD and its partial factors depend on a load categorisation the schema does not carry.

UNITS ARE SI THROUGHOUT, newtons and metres and pascals, per `CLAUDE.md`. **The clause
coefficients are the SI forms**, which matters: § 3.2.3's branch limits are `10340/F_y` and
`20680/F_y` with `F_y` in MPa, and writing the US coefficients (`1500/F_y`, `3000/F_y`, ksi)
against a pascal `F_y` would misplace every branch boundary by a factor of about 145. The
two conversions are done in one place each and named.

NO ONE-THIRD INCREASE (EZ4 Q2, locked). § 3.1.2 permits a one-third increase in allowables
for storm loading. It is **not applied**, and the reason is kept rather than reduced to a
default: the increase is written for a declared extreme environmental event in a
fixed-jacket design basis, and F4's cases are design waves from a screening sweep with no
return period. Applying it would widen every allowable by 33% on a categorisation the
schema does not carry -- the same argument `PLAN.md` uses to reject ISO's partial factors.

EVERY TOLERANCE LIVES IN `floatfea/tolerances.py` (`CLAUDE.md`). There are no numerical
tolerances in this module: the clauses are exact closed forms and the only numbers here are
the code's own coefficients, which are the clauses themselves and not thresholds anything
is compared against.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Final

from floatfea.basis import E_STEEL, FY_S355
from floatfea.tolerances import F6_API_FY_PLAUSIBLE_MAX, F6_API_FY_PLAUSIBLE_MIN

__all__ = [
    "CM_JOINT_TRANSLATION",
    "MemberCheck",
    "SectionClass",
    "allowable_axial_compression",
    "allowable_axial_tension",
    "allowable_bending",
    "allowable_shear",
    "check_member",
    "column_slenderness_parameter",
    "euler_stress",
    "local_buckling_stress",
    "section_class",
]

PASCAL_PER_MPA: Final[float] = 1.0e6
"""The one place § 3.2.3's MPa-based branch limits meet an SI `F_y`."""

ALLOWABLE_TENSION_FACTOR: Final[float] = 0.6
"""§ 3.2.1: `F_t = 0.6 F_y`."""

LOCAL_BUCKLING_DT: Final[float] = 60.0
"""§ 3.2.2(b): above this `D/t`, local buckling must be considered (R741)."""

ELASTIC_LOCAL_BUCKLING_C: Final[float] = 0.3
"""§ 3.2.2(b)'s `C` in `F_xe = 2 C E t / D`."""

BENDING_THIRD_BRANCH_NUMERATOR: Final[float] = 300000.0
"""§ 3.2.3's third-range upper limit as `this / F_y[MPa]` (FB1).

**FB1 SETS THIS AND IT ADMITS A NEGATIVE ALLOWABLE, WHICH IS MEASURED AND REFUSED RATHER
THAN PASSED ON.** At `F_y = 355 MPa` the limit is `845.1`, and the third branch
`(0.72 - 0.58 F_y (D/t) / E) F_y` crosses zero at `D/t = 0.72 E / (0.58 F_y) = 734.3`:

    D/t = 300  ->  Fb = +151.18 MPa
    D/t = 500  ->  Fb =  +81.57 MPa
    D/t = 734  ->  Fb =   +0.12 MPa
    D/t = 845  ->  Fb =  -38.52 MPa

FB1 also asks for `F_b <= 0.75 F_y` everywhere, and that assertion cannot see a negative.
So `allowable_bending` refuses a non-positive result as well, and the discrepancy goes back
to Xabier: the editions I can check give the third range a FLAT `D/t <= 300`, which at this
`F_y` is `2.8x` tighter and never reaches the sign change. In practice § 3.2.2(b)'s
`D/t > 60` refusal fires long before either limit on any compression member, so nothing in
F6 reaches this branch -- but the boundary is wrong in one of the two readings and it is
declared here rather than chosen silently.
"""

ALLOWABLE_SHEAR_FACTOR: Final[float] = 0.4
"""§ 3.2.4: `F_v = 0.4 F_y`, for beam shear and for torsional shear alike."""

BEAM_SHEAR_AREA_FACTOR: Final[float] = 0.5
"""§ 3.2.4 takes the beam shear stress as `V / (0.5 A)`, not `V / A`.

Written out because it is the clause's own idealisation and not a section property: the
factor stands in for the shear distribution over a tube, and using `A` would read 2x low.
"""

CM_JOINT_TRANSLATION: Final[float] = 0.85
"""§ 3.3.1 case (a): members in frames **subject to joint translation** (sidesway).

FB2 sets this, and it is the reading consistent with `K = 2.0`: EZ4 chose `K = 2.0` because
the gimbal end bears on a floating body and gives no reliable lateral restraint, which is
the sidesway case. The two assumptions now agree instead of one being sidesway and the
other not.

**AND THE DIRECTION WAS STATED BACKWARDS HERE (R743).** `C_m` MULTIPLIES the bending term
in § 3.3.2, so a LARGER `C_m` gives a LARGER utilisation: `C_m = 1.0` **raises** every
compression utilisation and `0.85` is the less onerous of the two, not the conservative one.
The earlier comment called `0.85` "the conservative reading", which is wrong in the
direction that matters. Measured one variable at a time on the K sensitivity:

    shipped                        0.024114
    axial sign fixed alone         0.034926
    C_m = 1.0 alone                0.128855
    both                           0.151293

`C_m` is the second-largest lever in the check and a `C_m = 1.0` column is reported beside
the `K = 1.0` one (FB2).
"""


@dataclass(frozen=True)
class SectionClass:
    """Which branch of § 3.2.3 a tube falls in, and the two limits that decide it."""

    d_over_t: float
    limit_1: float
    """`10340 / F_y`, `F_y` in MPa. Below it, `F_b = 0.75 F_y`."""
    limit_2: float
    """`20680 / F_y`. Between the two, the first reduced branch."""
    limit_3: float
    """`300000 / F_y` (FB1). Beyond it § 3.2.3 is not written and is refused."""
    branch: str
    """`"compact"`, `"reduced_1"`, `"reduced_2"`, or `"slender"`."""


def _require_plausible_fy(fy: float) -> None:
    """Refuse an `F_y` that is not plausibly in pascals (C60, widened by C72).

    **IT IS A FUNCTION BECAUSE THE REFUSAL REACHED TWO OF THE SIX ENTRY POINTS.** C60 put
    it inside `section_class`, which `allowable_bending` routes through -- and that is the
    production path, so nothing shipped was wrong. The API surface was:
    `allowable_axial_compression(121.5, 2.5, 0.025, 355e3)` returned `F_a = 1.928148e+05`
    on branch `'inelastic_local'` where the same call at `355e6` returns `7.325207e+07` on
    `'elastic_local'`, and `column_slenderness_parameter` moved
    `1.080589e+02 -> 3.417121e+03`. **The branch is a published CSV column and FA2 makes it
    a reported quantity**, so a caller reaching it through the axial clause got a label the
    table publishes. `allowable_axial_tension` and `allowable_shear` accepted it too and
    scale linearly, which is the quiet case: no branch moves and the number is simply wrong.

    "No shipped caller can reach it" was true and is a claim about today's callers.
    """
    if not F6_API_FY_PLAUSIBLE_MIN <= fy <= F6_API_FY_PLAUSIBLE_MAX:
        raise ValueError(
            f"F_y = {fy!r} Pa is outside the plausible range for structural steel "
            f"[{F6_API_FY_PLAUSIBLE_MIN:g}, {F6_API_FY_PLAUSIBLE_MAX:g}] Pa. Section "
            "3.2.3's branch limits are written as 10340/F_y and 20680/F_y with F_y in MPa, "
            "so this argument's UNIT decides which branch a section lands in -- S355 "
            "entered as 355e3 reads a D/t = 100 tube as `compact`. SI throughout: pascals "
            "(docs/conventions.md)."
        )


def _require_tube(d_outer: float, wall: float) -> None:
    """Refuse a `(D, t)` that is not a tube (C80).

    **A NEGATIVE DIAMETER OR WALL RETURNED `compact` -- THE BEST ALLOWABLE.** `D/t` came out
    negative and every branch test in section 3.2.3 is an UPPER bound, so a negative ratio
    satisfies the first one. A zero wall raised `ZeroDivisionError` rather than saying what
    was wrong, and a zero diameter gave `D/t = 0.0`, also `compact`.

    It is a function for C72's reason: `section_class` and `local_buckling_stress` both
    divide by `wall`, and a refusal in one of two dividers is a refusal a caller can walk
    past.
    """
    if not d_outer > 0.0 or not wall > 0.0 or wall >= 0.5 * d_outer:
        raise ValueError(
            f"D = {d_outer!r} m and t = {wall!r} m are not a tube: both must be positive "
            "and the wall must be under half the diameter. A negative D/t satisfies every "
            "branch test in section 3.2.3, because each is an upper bound -- so this "
            "returned `compact`, the best allowable, rather than refusing (C80)."
        )


def section_class(d_outer: float, wall: float, fy: float = FY_S355) -> SectionClass:
    """§ 3.2.3's branch for a circular tube.

    **`D/t > 300` IS REFUSED RATHER THAN EXTRAPOLATED.** The clause's third branch is
    written only to `D/t = 300`; beyond it local buckling governs and a beam-level check is
    not the binding one. Returning a number there would be inventing a clause.

    **AND AN `F_y` THAT IS NOT PLAUSIBLY IN PASCALS IS REFUSED TOO (C60).** The clause's
    own `10340/F_y` form, with `F_y` in MPa, makes this argument's unit load-bearing: at
    `fy = 355e3` -- S355 entered in kPa -- `D/t = 100` came back `compact` where the same
    section at `355e6` is `reduced_2`, so `F_b` was `0.75 F_y` instead of the reduced
    branch. Nothing refused it, and `fy = 0.0` raised `ZeroDivisionError` rather than
    saying what was wrong. FB1 had this module refuse a `D/t` outside the clause's range
    rather than extrapolate; this is that rule applied to the other load-bearing input.
    """
    _require_plausible_fy(fy)
    _require_tube(d_outer, wall)
    d_t = d_outer / wall
    fy_mpa = fy / PASCAL_PER_MPA
    limit_1 = 10340.0 / fy_mpa
    limit_2 = 20680.0 / fy_mpa
    limit_3 = BENDING_THIRD_BRANCH_NUMERATOR / fy_mpa
    if d_t <= limit_1:
        branch = "compact"
    elif d_t <= limit_2:
        branch = "reduced_1"
    elif d_t <= limit_3:
        branch = "reduced_2"
    else:
        branch = "slender"
    return SectionClass(
        d_over_t=d_t, limit_1=limit_1, limit_2=limit_2, limit_3=limit_3, branch=branch
    )


def allowable_axial_tension(fy: float = FY_S355) -> float:
    """§ 3.2.1. `F_t = 0.6 F_y`."""
    _require_plausible_fy(fy)
    return ALLOWABLE_TENSION_FACTOR * fy


def column_slenderness_parameter(fy: float = FY_S355, e: float = E_STEEL) -> float:
    """`C_c = sqrt(2 pi^2 E / F_y)` -- § 3.2.2's boundary between the two branches.

    `F_y` here is `F_xc` on a slender tube, which is `local_buckling_stress`'s output and is
    therefore already inside the range -- so the refusal is on the PUBLIC entry and the
    internal call passes a value this module computed.
    """
    _require_plausible_fy(fy)
    return math.sqrt(2.0 * math.pi * math.pi * e / fy)


def euler_stress(k_l_over_r: float, e: float = E_STEEL) -> float:
    """`F_e' = 12 pi^2 E / (23 (KL/r)^2)` -- § 3.3.2's amplification denominator."""
    if k_l_over_r <= 0.0:
        raise ValueError(f"KL/r must be positive; got {k_l_over_r}")
    return 12.0 * math.pi * math.pi * e / (23.0 * k_l_over_r * k_l_over_r)


def local_buckling_stress(
    d_outer: float, wall: float, fy: float = FY_S355, e: float = E_STEEL
) -> float:
    """§ 3.2.2(b): `F_xc`, the local buckling stress that replaces `F_y` in the column form.

    R741 -- THIS WAS NOT IMPLEMENTED AT ALL, and the locked plan asks for it in its own
    words: "the check must still refuse rather than pass silently on one that is slender".
    Measured before the repair, `allowable_axial_compression` returned
    `1.3610e+08 Pa`, branch `inelastic`, at `D/t = 100` with no refusal.

        F_xe = 2 C E t / D,  C = 0.3                      (elastic local buckling)
        F_xc = F_y                                        for D/t <= 60
        F_xc = F_y [1.64 - 0.23 (D/t)^(1/4)] <= F_xe      for D/t > 60

    The stand-in tube is `D/t = 13.9`, so `F_xc = F_y` and nothing in F6 is reduced by
    this. It exists because a section that WOULD be reduced must not pass silently.
    """
    _require_plausible_fy(fy)
    _require_tube(d_outer, wall)
    d_t = d_outer / wall
    if d_t <= LOCAL_BUCKLING_DT:
        return fy
    f_xe = 2.0 * ELASTIC_LOCAL_BUCKLING_C * e * wall / d_outer
    f_xc = fy * (1.64 - 0.23 * d_t**0.25)
    return float(min(f_xc, f_xe))


def allowable_axial_compression(
    k_l_over_r: float,
    d_outer: float,
    wall: float,
    fy: float = FY_S355,
    e: float = E_STEEL,
) -> tuple[float, str]:
    """§ 3.2.2. Returns `(F_a, branch)` with the branch named.

    FA2 asks for the branch per member-station, and the reason is EZ4's `K = 2.0`: at
    `K = 1.0` both arm lengths sit below `C_c` and at `K = 2.0` the 50 m platform arms cross
    it, so the locked value does not scale an allowable -- it moves those four members onto
    a different formula. A caller that reported only `F_a` would hide that.

        inelastic   KL/r <  C_c :  F_a = [1 - (KL/r)^2 / (2 C_c^2)] F_y / CSF
                                   CSF = 5/3 + 3(KL/r)/(8 C_c) - (KL/r)^3/(8 C_c^3)
        elastic     KL/r >= C_c :  F_a = 12 pi^2 E / (23 (KL/r)^2)
    """
    if k_l_over_r <= 0.0:
        raise ValueError(f"KL/r must be positive; got {k_l_over_r}")
    d_t = d_outer / wall
    if d_t > 300.0:
        raise ValueError(
            f"D/t = {d_t:.1f} exceeds 300, beyond which API section 3.2.2 is not written. "
            "Refused rather than extrapolated (R741)."
        )
    # § 3.2.2(b): `F_y` is replaced by the local buckling stress on a slender tube.
    f_xc = local_buckling_stress(d_outer, wall, fy, e)
    reduced = f_xc < fy
    c_c = column_slenderness_parameter(f_xc, e)
    if k_l_over_r >= c_c:
        branch = "elastic"
        f_a = euler_stress(k_l_over_r, e)
    else:
        ratio = k_l_over_r / c_c
        safety = 5.0 / 3.0 + (3.0 / 8.0) * ratio - (ratio**3) / 8.0
        branch = "inelastic"
        f_a = (1.0 - 0.5 * ratio * ratio) * f_xc / safety
    return f_a, (branch + "_local" if reduced else branch)


def allowable_bending(
    d_outer: float, wall: float, fy: float = FY_S355, e: float = E_STEEL
) -> tuple[float, str]:
    """§ 3.2.3. Returns `(F_b, branch)`.

    **FA1: this is the allowable F4's table did NOT use.** That table compared against a
    generic `0.6 F_y = 213.0 MPa`; for the stand-in tube `D/t = 13.9` is below
    `10340/F_y = 29.13`, so the clause gives `F_b = 0.75 F_y = 266.25 MPa` and the generic
    reference is `1.25x` conservative on bending.

        compact     D/t <= 10340/F_y            :  F_b = 0.75 F_y
        reduced_1   10340/F_y < D/t <= 20680/F_y:  F_b = [0.84 - 1.74 F_y D/(E t)] F_y
        reduced_2   20680/F_y < D/t <= 300      :  F_b = [0.72 - 0.58 F_y D/(E t)] F_y
    """
    klass = section_class(d_outer, wall, fy)
    cap = 0.75 * fy
    if klass.branch == "compact":
        f_b = cap
    elif klass.branch == "reduced_1":
        f_b = (0.84 - 1.74 * fy * d_outer / (e * wall)) * fy
    elif klass.branch == "reduced_2":
        f_b = (0.72 - 0.58 * fy * d_outer / (e * wall)) * fy
    else:
        raise ValueError(
            f"D/t = {klass.d_over_t:.1f} exceeds {klass.limit_3:.1f} "
            f"(= {BENDING_THIRD_BRANCH_NUMERATOR:g}/F_y), where API section 3.2.3 is not "
            "written. Extrapolating it would be an invented clause; DNV-RP-C202 is the "
            "reference and it is F7 sub-model work."
        )

    # R742: THE CAP, AND IT CAUGHT A REAL TRANSCRIPTION ERROR. The reduced branches must
    # never exceed the compact value, and the first one DID: `F_b = 267.785587 MPa` at
    # `D/t = 29.1268` against the `266.25` cap, staying above it to `D/t = 30.5974`. The
    # cause is the clause's own continuity point -- `1500/F_y[ksi]` is continuous at
    # `E = 29000 ksi = 199948 MPa` and this module runs at `210000 MPa`, so the SI
    # conversion of the limit and the SI value of `E` disagree. **The fix belongs in the
    # clause transcription and NOT in `E_STEEL`**, which is a material property.
    if f_b > cap:
        f_b = cap

    # AND THE CAP CANNOT SEE A NEGATIVE, which FB1's third limit admits (see
    # `BENDING_THIRD_BRANCH_NUMERATOR`). A non-positive allowable is refused rather than
    # returned: it would make every utilisation on that member negative or infinite.
    if f_b <= 0.0:
        raise ValueError(
            f"D/t = {klass.d_over_t:.1f} gives F_b = {f_b:.4e} Pa, which is not positive. "
            "Section 3.2.3's third branch crosses zero at "
            f"D/t = 0.72 E / (0.58 F_y) = {0.72 * e / (0.58 * fy):.1f}, inside the range "
            f"FB1's limit {klass.limit_3:.1f} admits. The clause does not describe a "
            "section this slender."
        )
    return f_b, klass.branch


def allowable_shear(fy: float = FY_S355) -> float:
    """§ 3.2.4. `F_v = 0.4 F_y`, for beam shear and torsional shear alike."""
    _require_plausible_fy(fy)
    return ALLOWABLE_SHEAR_FACTOR * fy


@dataclass(frozen=True)
class MemberCheck:
    """One member-station's stresses, allowables and utilisations.

    `governing` names the clause that binds, which is what FA3 asks the table to report --
    a utilisation without its clause tells a reader the member is hot but not why.
    """

    f_a: float
    f_b: float
    f_v: float
    f_vt: float
    allow_axial: float
    allow_bending: float
    allow_shear: float
    axial_branch: str
    bending_branch: str
    in_tension: bool
    interaction_form: str
    """Which half of section 3.3's interaction `u_combined` IS -- `"tension"` for
    section 3.3.1, or `"amplified"` or `"simple"` for the two forms section 3.3.2 requires
    and takes the larger of.

    **R752: THIS IS RECORDED BECAUSE A CALLER INFERRED IT AND GOT IT BACKWARDS.** The
    deliverable's summary derived "which form governs" from whether a `C_m = 1.0`
    sensitivity column differed from the shipped one, and published `10 of 17` amplified
    where the truth is **7 of 17 amplified and 10 of 17 simple** -- the ten it counted are
    exactly the ten where the SIMPLE form governs. That predicate detects something else:
    whether `C_m` visibly moves the station's governing utilisation, which it does on the
    bending-dominated ROOTs. **The explanation of why it is silent on the other seven was
    also wrong (C66)** and the measured one is three mechanisms, not one: all ten that fire
    are an OVERTAKE -- `amplified(C_m = 1.0)` exceeds `simple`, by `0.1153%` to `1.3129%`;
    five of the seven that miss do so because `u_combined` is not the governing channel at
    all (beam shear governs those TIPs); and two miss because the bending term is
    negligible, where the amplified form IS governing and `C_m` DOES reach `U`, by about
    `1e-10`. Both counts are true, neither implies the other, and the coincidence between
    them is contingent at one part in a thousand -- so the answer is reported rather than
    reconstructed.

    **THE TIE IS RECORDED AS `"simple"` (C69), AND THE TIE IS REACHABLE.** Where
    `amplified == simple` exactly, `max` returns the amplified operand and this field says
    `"simple"`. That is deliberate: at a tie the two forms give the same number, so no
    published figure depends on the choice, and `"simple"` is the label that does not claim
    the `C_m / (1 - f_a/F_e')` amplification is doing anything. Solved in closed form, the
    tie occurs at `KL/r = 60.8`, `f_a/F_e' = 0.02`, `My = 12633843.953476468 N.m`, where both
    forms are `0.09426368988411232` bit-identically -- so this is a documented convention
    rather than an unreachable branch.

    **AND THE `My` HERE WAS THE ROUNDED ONE FOR A ROUND (C83).** It read
    `1.263384395e+07`, and at THAT `My` this field returns `"amplified"` with
    `u_combined = 0.09426368986817012` -- the opposite label to the one this paragraph
    states, in the only place the convention is written down. The tie is a single double
    and a rounded neighbour of it is not a tie.
    """
    u_axial: float
    u_bending: float
    u_shear: float
    u_torsion: float
    u_combined: float
    governing: str

    @property
    def utilisation(self) -> float:
        """The largest of the five. The number a top-ten list sorts on."""
        return max(self.u_axial, self.u_bending, self.u_shear, self.u_torsion, self.u_combined)


def check_member(
    *,
    axial_n: float,
    shear_y_n: float,
    shear_z_n: float,
    torsion_nm: float,
    moment_y_nm: float,
    moment_z_nm: float,
    area_m2: float,
    section_modulus_m3: float,
    torsional_modulus_m3: float,
    d_outer_m: float,
    wall_m: float,
    k_l_over_r: float,
    fy: float = FY_S355,
    e: float = E_STEEL,
    cm: float = CM_JOINT_TRANSLATION,
) -> MemberCheck:
    """All six clauses on one member-station, plus § 3.3's interaction.

    KEYWORD-ONLY, because eleven positional floats of which several are section properties
    is a call nobody can read and a transposition nothing would catch.

    THE BENDING STRESS IS THE RESULTANT, `sqrt(f_by^2 + f_bz^2)`, which is what § 3.3 uses.
    The two components are not combined with the axial term separately: § 3.3.1 and § 3.3.2
    are written on the resultant.
    """
    f_a = abs(axial_n) / area_m2
    f_by = abs(moment_y_nm) / section_modulus_m3
    f_bz = abs(moment_z_nm) / section_modulus_m3
    f_b = math.hypot(f_by, f_bz)
    f_v = math.hypot(shear_y_n, shear_z_n) / (BEAM_SHEAR_AREA_FACTOR * area_m2)
    f_vt = abs(torsion_nm) / torsional_modulus_m3

    in_tension = axial_n >= 0.0
    allow_bending, bending_branch = allowable_bending(d_outer_m, wall_m, fy, e)
    allow_shear = allowable_shear(fy)
    if in_tension:
        allow_axial = allowable_axial_tension(fy)
        axial_branch = "tension"
    else:
        allow_axial, axial_branch = allowable_axial_compression(
            k_l_over_r, d_outer_m, wall_m, fy, e
        )

    u_axial = f_a / allow_axial
    u_bending = f_b / allow_bending
    u_shear = f_v / allow_shear
    u_torsion = f_vt / allow_shear

    # Section 3.3.1 (tension + bending) and 3.3.2 (compression + bending). The compression
    # form carries the amplification `Cm / (1 - f_a/F_e')`, and the clause ALSO requires the
    # simpler 0.6 Fy form -- both are evaluated and the larger governs, which is the clause
    # and not a choice made here.
    if in_tension:
        u_combined = f_a / (ALLOWABLE_TENSION_FACTOR * fy) + u_bending
        interaction_form = "tension"
    else:
        f_e = euler_stress(k_l_over_r, e)
        if f_a >= f_e:
            raise ValueError(
                f"f_a = {f_a:.4e} Pa reaches the Euler stress F_e' = {f_e:.4e} Pa, so "
                "section 3.3.2's amplification 1/(1 - f_a/F_e') is singular or negative. "
                "The member is past elastic buckling and the interaction formula does not "
                "describe it."
            )
        amplified = u_axial + cm * u_bending / (1.0 - f_a / f_e)
        simple = f_a / (ALLOWABLE_TENSION_FACTOR * fy) + u_bending
        u_combined = max(amplified, simple)
        interaction_form = "amplified" if amplified > simple else "simple"

    candidates = {
        "3.2.1 tension" if in_tension else "3.2.2 compression": u_axial,
        "3.2.3 bending": u_bending,
        "3.2.4 beam shear": u_shear,
        "3.2.4 torsional shear": u_torsion,
        "3.3.1 interaction" if in_tension else "3.3.2 interaction": u_combined,
    }
    governing = max(candidates, key=lambda k: candidates[k])
    return MemberCheck(
        f_a=f_a,
        f_b=f_b,
        f_v=f_v,
        f_vt=f_vt,
        allow_axial=allow_axial,
        allow_bending=allow_bending,
        allow_shear=allow_shear,
        axial_branch=axial_branch,
        bending_branch=bending_branch,
        in_tension=in_tension,
        interaction_form=interaction_form,
        u_axial=u_axial,
        u_bending=u_bending,
        u_shear=u_shear,
        u_torsion=u_torsion,
        u_combined=u_combined,
        governing=governing,
    )
