"""FT2.5: the truss resolution, reported at the sections the loop actually chose.

**WHAT THIS IS AND, MORE IMPORTANTLY, WHAT IT IS NOT.** `floatfea/run/sizing.py` runs
FM0's loop over the DECLARED TUBE GRID and re-solves the FE model at each candidate. This
module takes the member forces of the tube the loop ACCEPTED and resolves them into the
chord and diagonal forces a parallel-chord truss of declared depth and width would carry,
then sizes those members to API RP 2A-WSD.

**THE TRUSS IS NOT RE-SOLVED, AND NO `U` PUBLISHED BY THIS TOOL IS A STATEMENT ABOUT IT.**
That is a ruling and not a shortcut, and the reasoning is worth carrying here because the
alternative looks reasonable until it is measured:

* `docs/milestones/R1.md` section 4 fixes the candidate grid as "the config declared
  section list", for BOTH sizing analyses, and does so as one of the three reasons R1
  needs no tolerance at all. The declared section list is tubes -- `sections.groups` and
  `sections.candidates` both go through `_parse_tube`, which admits `d_outer` and `wall`
  and nothing else. So re-solving at a truss would contradict the locked plan at precisely
  the clause that says to stop and ask.
* The only truss-to-tube stiffness bridge in the repository is
  `scripts/measure/f6b_truss_sizing.py`'s `I_over_standin_h = A_c h^2 / STANDIN_I`, and
  `STANDIN_I = 0.888` is the second moment of ONE section -- the `D = 2.5 m`, `t = 0.180 m`
  stand-in. Measured across the grid `required_section` actually walks, that denominator is
  exact for the declared section and wrong by `1.719x` at the section the loop CHOSE
  (`I_y = 1.5264` against `0.888` at `t = 0.410 m`). A loop that steps the section must
  step the denominator too, so the bridge is not a constant but a function of the
  configuration -- and a constant standing in for a function on a production path is R694
  by name.
* `docs/milestones/F1.md:390` records the arm as "50 m span, triangulated, depth
  undecided". The tube is the stand-in FOR the truss; making the undecided depth an input
  to the section the solver runs at would invert that, and every published `U` would carry
  it.
* The proxy's own field names say it: `EI_proxy_Ac_h2`, `EI_proxy_Ac_b2`,
  `I_over_standin_h`. It ignores the chords' own `I`, the diagonals entirely and shear
  flexibility.

A truss re-solve needs the depth DECIDED and the equivalence LOCKED, and the model would
have to build chords and diagonals as members -- a capability nothing in R1 has.

**EVERY DECLARED PARAMETER COMES FROM THE CONFIGURATION.** `scripts/measure/f6b_truss_sizing.py`
holds `D_OVER_T`, `JOINT_ALLOWANCE`, the `(h, b)` grid and the bisection bracket as module
constants, which is right for a measure script and forbidden here: a hard-coded `0.888` or
`24.0` on a production path is a tolerance under another name. They are `sections.truss`.

The resolutions below are ported from that script with their derivations intact, because
`CLAUDE.md` asks element mathematics to carry a reference that can be checked against a
source rather than re-derived.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from floatfea.checks.api_wsd import allowable_axial_compression, allowable_axial_tension
from floatfea.model.material import Section
from floatfea.run.config import ConfigError, Material, TrussOptions

__all__ = [
    "ChordForces",
    "Face",
    "GroupTruss",
    "TrussCell",
    "area_for_compression",
    "area_for_tension",
    "box_resolution",
    "chord_buckling_length",
    "enclosed_area",
    "faces",
    "panel_and_diagonal",
    "resolve_group",
    "triangle_resolution",
]

GEOMETRIES: tuple[str, ...] = ("per_face_45", "uniform_panel")
"""FI1's two consistent readings of "diagonals at 45 degrees (panel length = the face
dimension)", on a box whose two faces have different dimensions.

Both are computed and both are published, because which one FI means changes the answer and
a reader needs to see whether the recommendation survives either. R801 is why: the first
version of the measure script took the SHORTER buckling length from one reading and the
SHORTER diagonal from the other -- the favourable half of each -- through a single
`panel_length=min(h, b)` while its own comment said "the face dimension".

    per_face_45     45 degrees on every face, so the panel length is that face's own
                    dimension. A chord is braced every `h` by the vertical faces and every
                    `b` by the horizontal ones, at non-coincident stations; the chord is a
                    circular tube so `r_y = r_z`, and the governing buckling length is
                    `max(h, b)`.
    uniform_panel   one panel length `min(h, b)` for the whole truss, so the chord's
                    buckling length is `min(h, b)` -- but then the larger faces' diagonals
                    are NOT at 45 degrees: across a face of transverse dimension `d` over a
                    panel `p` they sit at `atan(d/p)` and are `hypot(p, d)` long.

What may NOT stand is `min` for the chord and 45 degrees for the diagonals at once.
"""


@dataclass(frozen=True)
class ChordForces:
    """The chord axial forces and the face shears one beam-force set produces."""

    chords: dict[str, float]
    face_shear: dict[str, float]


def box_resolution(
    n: float, vy: float, vz: float, t: float, my: float, mz: float, h: float, b: float
) -> ChordForces:
    """FI1(a). Four chords at `(+-b/2, +-h/2)`; `N/4 +- My/(2h) +- Mz/(2b)`.

    Derivation of the two bending terms, so the formula is checkable rather than quoted:
    with four equal chords, `My = sum F_i z_i = 2f(h/2) + 2f(h/2) = 2fh`, hence
    `f = My/(2h)`, and `Mz = 2g(b/2)*2 = 2gb`, hence `g = Mz/(2b)`. Signs are preserved
    (FI1), so each chord gets its own combination rather than a worst-case magnitude.
    """
    axial = n / 4.0
    f_my = my / (2.0 * h)
    f_mz = mz / (2.0 * b)
    chords = {
        "top_+b": axial + f_my + f_mz,
        "top_-b": axial + f_my - f_mz,
        "bot_+b": axial - f_my + f_mz,
        "bot_-b": axial - f_my - f_mz,
    }
    # Shear: `Vz` to the two vertical faces, `Vy` to the two horizontal faces, plus the
    # torsion shear flow `q = T/(2 A_enc)` around the perimeter (FI1). A vertical face of
    # depth `h` carries `q h`; a horizontal face of width `b` carries `q b`. The two signs
    # are combined to the larger magnitude, because the flow adds on one face of each pair
    # and subtracts on the other.
    q = t / (2.0 * enclosed_area("box", h, b))
    face = {
        "vertical": abs(vz) / 2.0 + abs(q * h),
        "horizontal": abs(vy) / 2.0 + abs(q * b),
    }
    return ChordForces(chords, face)


def triangle_resolution(
    n: float, vy: float, vz: float, t: float, my: float, mz: float, h: float, b: float
) -> ChordForces:
    """FI1(b). Three chords: two bottom at `(+-b/2, 0)`, one top at `(0, h)`, apex UP.

    The section properties, for three equal areas `A_c` with centroid at `zbar = h/3`:

        I_yy = A_c[2(h/3)^2 + (2h/3)^2] = (2/3) A_c h^2
        I_zz = A_c * 2 (b/2)^2          = A_c b^2 / 2

    and `F_i = A_c M z_i / I` gives

        top         N/3 + My/h          and NO Mz term at all (it is on the centreline)
        bottom +-   N/3 - My/(2h)  +- Mz/b

    Both checks are exact: `sum F = My/h - 2*My/(2h) = 0`, and
    `sum M = (My/h)(2h/3) + 2(My/(2h))(h/3) = My`.

    **THE ASYMMETRY IS A RESULT, NOT A DETAIL.** The apex carries twice either bottom
    chord's `My` force and carries no `Mz`, so horizontal bending is resisted by the bottom
    pair alone on lever `b` where the box has two pairs. Apex-up is declared; both moment
    signs are evaluated per instant, so hogging and sagging are both found.
    """
    axial = n / 3.0
    chords = {
        "apex": axial + my / h,
        "bot_+b": axial - my / (2.0 * h) + mz / b,
        "bot_-b": axial - my / (2.0 * h) - mz / b,
    }
    q = t / (2.0 * enclosed_area("triangle", h, b))
    # **EACH INCLINED FACE CARRIES ITS IN-PLANE SHARE, OVER ITS OWN LENGTH (FY3 Q1,
    # answering R1072).** A braced face resists shear IN ITS OWN PLANE. For an apex-up
    # triangle with bottom chords at `(-b/2, 0)` and `(+b/2, 0)` and the apex at `(0, h)`,
    # each inclined wall runs along `e = (+-b/2, h)/Lf` with `Lf = hypot(h, b/2)`, so a
    # face whose VERTICAL component must be `|Vz|/2` carries an in-plane force of
    # `|Vz|/2 * Lf/h`. Bredt's shear flow acts along the wall too, so its contribution is
    # `q * Lf` and not `q * h`.
    #
    # WHAT THIS REPLACES, AND IT DID NOT CLOSE. The previous form gave each face the
    # VERTICAL PROJECTION of both -- `|Vz|/2 + q*h` -- so the faces' own components did
    # not sum to the applied load. Measured over the example's declared grid, the
    # recovered fraction of `Vz` ran from `0.982872` at `h=8, b=3` down to `0.447214` at
    # `h=2, b=8`, and the recovered `Mx/T` from `0.988581` to `0.631476`. The box closed
    # at `1.000000` on both channels at every aspect ratio, which is what said the error
    # was in the triangle's treatment and not in the reference.
    #
    # The consequence was UNCONSERVATIVE and it reached a published column: triangular
    # `diag A` in `truss_sizing.md` was low by up to `1.7723x` on the example's own grid
    # and `2.3792x` at `h=2, b=8`. `docs/milestones/F6b.md` declares nothing about an
    # inclined face -- FI1 says `Vz` goes to the VERTICAL faces, and a triangle has none --
    # so this was an unexamined carry-over from `scripts/measure/f6b_truss_sizing.py`
    # rather than a declared idealisation. FY3 rules both halves fixed.
    #
    # **THE KEYS ARE `inclined` AND `bottom`, NOT `vertical` AND `horizontal` (R1078).**
    # They were the box's names, and a triangle has no vertical face -- so a caller
    # counting faces by this key could not tell a box's GENUINELY vertical face from a
    # triangle's inclined one, and `_governing_faces` published "15 are governed by the
    # vertical face" on a grid where the true answer for inclined faces was 0 and all 15
    # were box cells. A name that is false of the thing it names will eventually be
    # believed by something; renaming makes the conflation impossible rather than caught.
    lf = inclined_face_length(h, b)
    face = {
        "inclined": abs(vz) * lf / (2.0 * h) + abs(q * lf),
        "bottom": abs(vy) + abs(q * b),
    }
    return ChordForces(chords, face)


def enclosed_area(shape: str, h: float, b: float) -> float:
    """`A_enclosed` for FI1's shear flow: `b h` for the box, `b h / 2` for the triangle."""
    return b * h if shape == "box" else 0.5 * b * h


def inclined_face_length(h: float, b: float) -> float:
    """`Lf`, the true length of an apex-up triangle's inclined face (FY3).

    One function, because `Lf` is used in two places FY3 changes and they must not be able
    to disagree: the SHEAR each inclined face carries in its own plane (Q1) and the LENGTH
    that face is braced over (Q2). Those were `h` in both before FY3, and `h` is the
    vertical projection of this.
    """
    return math.hypot(h, 0.5 * b)


RESOLVERS = {"box": box_resolution, "triangle": triangle_resolution}


@dataclass(frozen=True)
class Face:
    """One braced face: how many there are, its transverse dimension, its shear key."""

    count: int
    dimension: float
    shear_key: str


def faces(shape: str, h: float, b: float) -> tuple[Face, ...]:
    """The braced faces and their transverse dimensions.

    The box has two vertical faces of depth `h` taking `Vz` and two horizontal faces of
    width `b` taking `Vy`. The triangle has two inclined faces taking `Vz` and one bottom
    face of width `b` taking `Vy` -- which is why `triangle_resolution` divides `Vy` by one
    rather than by two.
    """
    if shape == "box":
        return (Face(2, h, "vertical"), Face(2, b, "horizontal"))
    # **THE INCLINED FACE IS BRACED OVER `Lf`, NOT OVER `h` (FY3 Q2).** It was `h`, the
    # vertical projection, so the diagonal inside that face was sized and buckling-checked
    # as if the face were only as deep as the triangle is tall. This is the second half of
    # R1072 and it is INDEPENDENT of the first: the measurement that separated them found
    # the allocation worth `Lf/h` on the diagonal FORCE and `0` on the published area at
    # `per_face_45`, while the braced length alone moved 50 cells up and up to `27.0%`
    # DOWN -- a longer strut is weaker, and it is also compared against a different
    # slenderness limit. Correcting one and not the other gives a number defensible on one
    # axis and wrong on the other, which is why FY3 rules both.
    return (Face(2, inclined_face_length(h, b), "inclined"), Face(1, b, "bottom"))


def chord_buckling_length(geometry: str, h: float, b: float) -> float:
    """The chord's unbraced length, which depends on the READING and not on a face."""
    return max(h, b) if geometry == "per_face_45" else min(h, b)


def panel_and_diagonal(geometry: str, h: float, b: float, face: Face) -> tuple[float, float]:
    """`(diagonal length, diagonal steel per unit truss length)` for one braced face.

    The second decides mass: a diagonal of length `L` repeated every `p` along the truss
    contributes `A_d * L / p` of area per unit length. **It is NOT the force ratio** -- see
    `_cell`, and see R1069, which is the defect of believing it was.

    **THIS NO LONGER RETURNS THE CHORD BUCKLING LENGTH, AND THAT IS PART OF R1069's
    REPAIR.** It used to return it first, as a second copy of what `chord_buckling_length`
    already computes -- and a caller bound that first element to a variable named `panel`
    and used it as the panel spacing. Under `uniform_panel` the two coincide, so the
    mis-binding was invisible there and wrong under `per_face_45`. One quantity, one
    function: the buckling length comes from `chord_buckling_length` and nowhere else.
    """
    panel = face.dimension if geometry == "per_face_45" else min(h, b)
    diagonal = (
        panel * math.sqrt(2.0) if geometry == "per_face_45" else math.hypot(panel, face.dimension)
    )
    return diagonal, diagonal / panel


def area_for_tension(force: float, material: Material) -> float:
    """Clause 3.2.1: `A = F / (0.6 Fy)`. Zero for a compressive or zero force."""
    if force <= 0.0:
        return 0.0
    return force / allowable_axial_tension(material.fy)


def area_for_compression(
    force: float, panel_length: float, truss: TrussOptions, material: Material
) -> tuple[float, str]:
    """Clause 3.2.2 at `K = 1.0`, `L` = the panel length, solved for the minimum area.

    `F_a` depends on `KL/r` and therefore on the section, so this is implicit and is solved
    by bisection on `D` at the declared `D/t`: the demand `|F|/A(D)` falls as `D` grows and
    `F_a(D)` rises, so `|F|/A - F_a` is monotone decreasing with one root. **The bracket is
    REFUSED rather than extrapolated** if its upper bound does not pass.

    **NO THRESHOLD AND NO CONVERGENCE TEST.** The loop halves a declared interval a fixed
    number of times, so the result is exact to float precision; there is no epsilon here
    that could be loosened to make two numbers agree. `sections.truss.diameter_search` is a
    declared domain, which can be widened but not slackened.
    """
    if force >= 0.0:
        return 0.0, "tension"
    demand = abs(force)
    lo, hi = truss.diameter_search

    def tube(d: float) -> Section:
        return Section.circular_tube(d, d / truss.d_over_t)

    def slack(d: float) -> float:
        sec = tube(d)
        r = math.sqrt(float(sec.I_y) / float(sec.A))
        f_a, _ = allowable_axial_compression(
            panel_length / r, d, d / truss.d_over_t, material.fy, material.e
        )
        return f_a - demand / float(sec.A)

    if slack(hi) < 0.0:
        raise ConfigError(
            f"no tube up to D = {hi:g} m at D/t = {truss.d_over_t:g} carries "
            f"{demand:.4e} N in compression over a {panel_length:.3f} m panel. Refused, "
            f"not extrapolated: a section outside the bracket is a section nobody declared. "
            f"Widen `sections.truss.diameter_search`, or declare a deeper truss so the "
            f"panel is shorter and the chord force lower."
        )
    # 200 halvings of a bracket at most 6 m wide is 6 / 2**200 -- below float precision, so
    # this terminates on the interval rather than on a tolerance.
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if slack(mid) >= 0.0:
            hi = mid
        else:
            lo = mid
    sec = tube(hi)
    _, branch = allowable_axial_compression(
        panel_length / math.sqrt(float(sec.I_y) / float(sec.A)),
        hi,
        hi / truss.d_over_t,
        material.fy,
        material.e,
    )
    return float(sec.A), branch


@dataclass(frozen=True)
class TrussCell:
    """One `(shape, h, b, geometry)` answer for one member group."""

    shape: str
    depth: float
    width: float
    geometry: str
    chord_area: float
    chord_force: float
    chord_station: str
    chord_branch: str
    chord_buckling_length: float
    diagonal_area: float
    diagonal_force: float
    diagonal_face: str
    steel_area_per_m: float
    """Chord steel plus diagonal steel per metre of truss, the allowance on BOTH (L6)."""


@dataclass(frozen=True)
class GroupTruss:
    """Every declared grid cell for one member group, at the ACCEPTED tube's forces."""

    group: str
    rows: int
    cells: tuple[TrussCell, ...]

    def lightest(self) -> TrussCell:
        """The cell with the least steel per metre, over every declared reading.

        **NOT AN AVERAGE AND NOT A RECOMMENDATION.** It is the argmin of a declared grid,
        reported with its own geometry named, because `CLAUDE.md` forbids reducing a
        per-case diagnostic to a summary and a reader needs to know WHICH reading produced
        the number they are looking at.
        """
        if not self.cells:
            raise ConfigError(
                f"no truss cell was resolved for member group `{self.group}`, so there is "
                f"nothing to report. The declared grid is "
                f"`sections.truss.depths` x `sections.truss.widths` x "
                f"`sections.truss.shapes`."
            )
        return min(self.cells, key=lambda c: c.steel_area_per_m)


def resolve_group(
    group: str,
    rows: list[tuple[str, tuple[float, ...]]],
    truss: TrussOptions,
    material: Material,
) -> GroupTruss:
    """Size the chords and diagonals of one group over the whole declared `(h, b)` grid.

    `rows` is `(station label, six components)` per checked instant, and **it must come
    from the ACCEPTED tube's re-solve, not from the baseline.** That is a condition of the
    ruling on FT2.5 and it is one line of sequencing in the caller: a truss resolved from
    baseline forces would be sized for loads the structure does not carry at the section
    the loop chose. On this deck the premise error is `1.554e-14` on the platform group so
    the defect would not show -- and "it does not show on this deck" is how R682 and R694
    both happened.

    **THE CHORD AREA IS THE WORST OVER EVERY CHORD, STATION AND INSTANT, IN BOTH SENSES.**
    The largest tension demand and the largest compression demand are sized separately and
    the larger area wins, because the compression branch is not a scaling of the tension
    one. Each face's diagonals are sized for THAT FACE's own shear (R801), not for the
    worst face shear anywhere.
    """
    if not rows:
        raise ConfigError(
            f"member group `{group}` supplied no checked instants, so its truss cannot be "
            f"resolved. A resolution over no rows would publish a section sized for "
            f"nothing."
        )
    # **THE SIX COMPONENTS ARE COUNTED, NOT UNPACKED BLIND.** `Row.values` is a
    # `tuple[float, ...]` as far as the type says, and the resolutions take exactly
    # `(N, Vy, Vz, T, My, Mz)`. A row of five would silently shift every argument one place
    # -- `My` arriving as `T` -- and produce a plausible truss from the wrong moment.
    for label, values in rows:
        if len(values) != 6:
            raise ConfigError(
                f"member group `{group}` station {label!r} carries {len(values)} force "
                f"components where the resolutions take six, `(N, Vy, Vz, T, My, Mz)` in "
                f"`docs/conventions.md`'s order. Unpacking it would shift every argument "
                f"one place and resolve a truss from the wrong moment."
            )
    cells: list[TrussCell] = []
    for shape in truss.shapes:
        resolve = RESOLVERS[shape]
        for h in truss.depths:
            for b in truss.widths:
                resolved = [
                    (label, resolve(v[0], v[1], v[2], v[3], v[4], v[5], h, b)) for label, v in rows
                ]
                for geometry in GEOMETRIES:
                    cells.append(_cell(shape, h, b, geometry, resolved, truss, material))
    return GroupTruss(group=group, rows=len(rows), cells=tuple(cells))


def _cell(
    shape: str,
    h: float,
    b: float,
    geometry: str,
    resolved: list[tuple[str, ChordForces]],
    truss: TrussOptions,
    material: Material,
) -> TrussCell:
    """One grid cell, sized. Split out so `resolve_group` reads as the sweep it is."""
    worst_tension = (0.0, "")
    worst_compression = (0.0, "")
    for label, forces in resolved:
        for value in forces.chords.values():
            if value > worst_tension[0]:
                worst_tension = (value, label)
            if value < worst_compression[0]:
                worst_compression = (value, label)

    buckling = chord_buckling_length(geometry, h, b)
    area_t = area_for_tension(worst_tension[0], material)
    area_c, branch = area_for_compression(worst_compression[0], buckling, truss, material)
    if area_c >= area_t:
        chord_area, chord_force, chord_station = area_c, worst_compression[0], worst_compression[1]
    else:
        chord_area, chord_force, chord_station = area_t, worst_tension[0], worst_tension[1]
        branch = "tension"

    # Each face's own shear, each face's own panel (R801).
    diagonal_area = 0.0
    diagonal_force = 0.0
    diagonal_face = ""
    diagonal_steel_per_m = 0.0
    for face in faces(shape, h, b):
        length, steel_factor = panel_and_diagonal(geometry, h, b, face)
        shear = max(abs(forces.face_shear[face.shear_key]) for _label, forces in resolved)
        # **`F_d = V L / d`, FROM STATICS, AND NOT `V L / p` (R1069).** A cut
        # perpendicular to the truss axis crosses both chords and the diagonal. The chords
        # are parallel to the axis, so their transverse component is ZERO and the diagonal
        # alone carries the shear: `F_d (d/L) = V`, i.e. `F_d = V/sin(theta) = V L / d`.
        #
        # `steel_factor` is `L/p` and is the MASS ratio, not this one. They coincide only
        # where `p == d`, which is `per_face_45` by construction -- so a check run only
        # there cannot tell them apart, and mine did not. The control that needs no
        # algebra: at `p = 1, d = 50` a nearly transverse diagonal must carry nearly all of
        # `V`; statics gives `F/V = 1.0002` and `L/p` gives `50.01`. A ratio that grows
        # without bound as a member becomes transverse is not a force ratio.
        force = shear * length / face.dimension
        area, _b = area_for_compression(-force, length, truss, material)
        area = max(area, area_for_tension(force, material))
        if area > diagonal_area:
            diagonal_area, diagonal_force, diagonal_face = area, force, face.shear_key
        diagonal_steel_per_m += face.count * area * steel_factor

    n_chords = 4 if shape == "box" else 3
    # **THE JOINT ALLOWANCE APPLIES TO CHORD AND DIAGONAL STEEL BOTH (L3).** It was on
    # the chords alone here, where `scripts/measure/f6b_truss_sizing.py` has
    # `line_mass = (chord_steel + diagonal_steel) * RHO_STEEL * JOINT_ALLOWANCE` -- so
    # the published steel-per-metre understated the diagonals' share of the allowance,
    # in the unconservative direction, against the source this was ported from.
    steel_per_m = (n_chords * chord_area + diagonal_steel_per_m) * truss.joint_allowance
    return TrussCell(
        shape=shape,
        depth=h,
        width=b,
        geometry=geometry,
        chord_area=chord_area,
        chord_force=chord_force,
        chord_station=chord_station,
        chord_branch=branch,
        chord_buckling_length=buckling,
        diagonal_area=diagonal_area,
        diagonal_force=diagonal_force,
        diagonal_face=diagonal_face,
        steel_area_per_m=steel_per_m,
    )
