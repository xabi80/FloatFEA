#!/usr/bin/env python
"""EY0: the member-force table, per member and station and case, from the committed npz.

    python scripts/measure/member_forces_table.py
    python scripts/measure/member_forces_table.py --out out.csv --summary out.md

**PRELIMINARY UNTIL F4 CLOSES.** Every number here is labelled, and the labels are not
decoration -- see `LABELS` below and the header of both outputs. The section is a stiffness
stand-in for a truss, the masses are assumed, and one heading has been run.

**NO FLOATSIM AND NO `HSP-runs` ON THIS PATH.** It reads `data/f4/dynamic_inputs.npz`
(EX0(d)) and builds the FE model from `data/platform/platform12_deck.yaml`. R721 is why
that sentence is here: a rung-4 gate that reached HSP passed on one machine and errored on
124 of 126 cases in CI. This script is not a gate -- EY0 puts it outside -- but it reads
the same inputs, and the point of committing them was that anything downstream runs
anywhere.

WHAT IT COMPUTES, and the three load bases, because "dynamic" is a DEFINITION here and not
a measurement:

    static    the supported structure under its own weight -- `solve_superstructure_static`,
              EK0(d)'s minimal statically determinate restraint. What the frame carries
              standing still.
    dynamic   the free body under the DYNAMIC joint-reaction increments, with inertia
              relief supplying the acceleration increment. **No gravity.** Per window step.
    total     static + dynamic, summed per component.

**FLOATSIM IS LINEARISED ABOUT STATIC EQUILIBRIUM, AND THAT IS WHY `dynamic` CARRIES NO
GRAVITY.** The study builds the system as `shared_db.C + gravity_restoring` and its own
comment warns against double-counting buoyancy, so `xi` is the DEVIATION from equilibrium
and the multipliers are the dynamic increment -- the static weight/buoyancy balance is
already inside the formulation and never appears in `lam`.

The first version of this script added gravity to the dynamic case. Measured, that put the
hub-joint vertical loads at `~1e5 N` against a platform weight of `1.84e7 N`, so the body
was in near free fall: the relief acceleration read `-7.37 m/s^2` where FloatSim's own
`accel` reads `-0.0094`. The decomposition is not a presentation choice; getting it wrong
changes the answer.

**THE LOAD PATH IS VALIDATED AGAINST FLOATSIM'S OWN ACCELERATIONS**, which the npz stores:
with gravity excluded, the FE inertia-relief acceleration agrees with `accel` to **1.55 %
on all five bodies** and to **2.78 % worst over eighteen (case, step, body) samples**. The
offset is systematic rather than scattered, which points at a small mass difference and not
at a wrong path. This is EV1's third assertion in all but name -- EX4 deferred it to F5 as a
GATE, and nothing stopped it being used here as a control.

THE JOINT LOADS GO THROUGH `map_joint_reactions`, the reviewed mapper, from the raw
multipliers `lam` the npz stores -- NOT from the npz's `contrib`. `contrib` is each joint's
reaction at the BODY REFERENCE POINT; a member-force table needs it at the joint's own
node, and the transfer between the two is a frame question `docs/conventions.md` is the
authority on. Deriving that transform here would be this script asserting its own guess
about a frame, which `CLAUDE.md` forbids in as many words.

**AND THE DECK'S JOINT ORDER IS CHECKED, NOT ASSUMED.**
`tests/verification/rung4/test_f4_static_and_mapping.py:844-849` records the gap: the
BUILDER's joint order is nowhere checked against the DECK's, and that is the driver's job.
This script is a driver. The npz carries the deck's own order and
`_joint_wiring` asserts the two agree, so a reaction cannot be attributed to the wrong
joint silently.

STATIONS, AND WHAT IS EXACT. At F3's mesh there is ONE element per member
(`floatfea/post/member_forces.py`), so ROOT and TIP are the element's two end nodes and
both are EXACT. MID is not a node: it is computed in closed form for a uniform net body
force along the member, which is what the net d'Alembert field is on a prismatic element --
shear linear, moment parabolic, so the midspan moment is the chord mean plus `w L^2 / 8`.
A refined mesh would give it directly and this closed form would then be a check on it.

    ROOT = the internal action at the body's `centre_node` end (node_a)
    TIP  = the internal action at the far end, which is `-end_b` and NOT `end_b` (R730)

Stated rather than inferred: for a platform arm the centre node carries the lumped
remainder and the hub joint is at the TIP, so "root" here is a GEOMETRIC name for the
inboard end and not a claim about which end is structurally fixed.

STRESSES ARE INDICATIVE AND THE FORMULA IS EY0's:

    sigma = |N| / A + sqrt(My^2 + Mz^2) / W        W = 2 I / D, from `basis.py`'s tube
    tau   = |T| / (2 W_t) + V / A_shear            V = sqrt(Vy^2 + Vz^2)

with `W_t = 2 J / D` the torsional modulus and `A_shear = kappa * A`. No code check is
applied -- that is F5 (EY4). A von Mises combination is deliberately NOT formed here,
because the two terms peak at different points of the section and combining them without
saying where would be a number nobody can act on.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from floatfea import basis  # noqa: E402

# RE-EXPORTED ON PURPOSE, AND `ruff` CANNOT TELL (FL1). This file is not only a script:
# `f6a_premise_check.py` and `f6_results_report.py` both load it BY PATH through
# `importlib` and then reach for these as attributes of the loaded module. Before the
# core moved to `floatfea.post.forces_table` they were defined here, so the attribute
# lookups resolved; after the move they resolve only because these names are imported
# back into this namespace. Removing them as "unused" breaks two scripts silently --
# an `AttributeError` at the far end of an `importlib` load, with nothing in this file
# to point at.
from floatfea.loads.joint_reactions import map_joint_reactions  # noqa: E402,F401
from floatfea.model.platform import (  # noqa: E402
    BodyModel,
    Member,
    _outer_diameter,
    build_superstructure,
)
from floatfea.post.forces_table import (  # noqa: E402,F401
    Row,
    _joint_wiring,
    _lam_full_scale,
    _net_field,
    _section_properties,
    _static_rows,
    _station_values,
    _stresses,
    compute_rows,
)
from floatfea.post.member_forces import (  # noqa: E402
    COMPONENTS,
)
from floatfea.solve.inertia_relief import solve_inertia_relief  # noqa: E402,F401

WAVE_HEIGHT_FULL_M = 24.2
"""The DS1 design wave at full scale, `0.484 m` model times the Froude factor."""

GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
"""EZ2(a): the cases the GOVERNING envelope is taken over.

**EZ2 corrects the case selection, and it is Xabier's correction of his own basis.** For
`H = 24.2 m` the associated-period range by DNV practice is
`sqrt(6.5 H) <= T <= sqrt(11 H)`, which is `12.542 .. 16.316 s`. The two cases outside it
are reported separately and are not allowed to govern:

    T = 10 s   H/lambda = 0.1550  -- EXCEEDS the deep-water breaking steepness 1/7 = 0.1429
    T = 20 s   H/lambda = 0.0387  -- below the range; the wave is too long for this height

**AND T = 12.5 s SITS 0.042 s BELOW THE LOWER BOUND IT IS BEING INCLUDED UNDER.**
`sqrt(6.5 x 24.2) = 12.542 s`. EZ2(a) names it as governing and that is what ships, but the
directive's own criterion and its own case list disagree by that much, so the fact is here
rather than passed over. It is the lowest-period governing case and therefore the one most
likely to carry the envelope, which is why the discrepancy is worth a reader's attention.
"""

SENSITIVITY_PERIODS = (10.0, 20.0)
"""EZ2(b): outside the associated-period range; `T = 10 s` exceeds breaking steepness."""


def steepness(period_full_s: float) -> tuple[float, float, str]:
    """`(lambda, H/lambda, position)` for one case, deep water.

    `lambda = g T^2 / (2 pi)`. The position string is what EZ2(d) asks for on every label
    line, and it names the two independent reasons a case can be out of range -- the
    period band and the steepness limit -- rather than collapsing them into "outside".
    """
    lam = 9.81 * period_full_s * period_full_s / (2.0 * math.pi)
    s = WAVE_HEIGHT_FULL_M / lam
    lo = math.sqrt(6.5 * WAVE_HEIGHT_FULL_M)
    hi = math.sqrt(11.0 * WAVE_HEIGHT_FULL_M)
    if s > 1.0 / 7.0:
        where = f"BREAKING (H/L {s:.4f} > 1/7); and below the band {lo:.3f}-{hi:.3f} s"
    elif period_full_s < lo:
        where = f"below the band {lo:.3f}-{hi:.3f} s by {lo - period_full_s:.3f} s"
    elif period_full_s > hi:
        where = f"above the band {lo:.3f}-{hi:.3f} s by {period_full_s - hi:.3f} s"
    else:
        where = f"in the band {lo:.3f}-{hi:.3f} s"
    return lam, s, where


STATIONS = ("ROOT", "MID", "TIP")
BASES = ("static", "dynamic", "total")

LABELS = (
    "PRELIMINARY until F4 closes.",
    "Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms "
    "(Xabier, 6 Oct); platform inertia scaled with mass (assumed). ER0.",
    "DZ5 / ER1(e): the four hub arms carry an equivalent density above steel "
    "(11433.5 kg/m^3 against 7850), which is a reported sizing finding -- the members are "
    "stiffness equivalents, so the hub's mass does not fit inside F1's section at f = 0.75.",
    "Hub line mass 15 t/m, against the platform arms' 10.3 t/m.",
    "Stand-in tube: the stiffness equivalent of a TRIANGULATED TRUSS of undecided depth "
    "(F1.md:390). Stresses are INDICATIVE, not a check on a real section.",
    "EX3 / R724: all six cases are heading 0 degrees. The heading dependence is UNTESTED.",
    "R739: the N column is TENSION POSITIVE (docs/conventions.md:320). It was published "
    "compression-positive -- a 1 mm stretch gave a negative N -- which put every "
    "over-unity station on API section 3.3.1 instead of 3.3.2.",
    "R740: `total_instant` rows carry the six components AT the step where sigma peaks. "
    "`total_max` / `total_min` are the PER-COMPONENT envelope; their six values do not "
    "occur together and a utilisation from them is an UPPER BOUND.",
    "FA1: the 213.0 MPa figure this table compares against is a GENERIC 0.6*Fy REFERENCE; "
    "it is SUPERSEDED by F6's API RP 2A-WSD clauses and it is NOT the API bending "
    "allowable. For D/t = 13.9 (below 10340/Fy = 29.13) API gives Fb = 0.75*Fy = "
    "266.25 MPa; the generic reference is 1.25x conservative on bending.",
    "FA0: T = 12.5 s STAYS in the governing set. It is 0.3% below sqrt(6.5*H) = 12.542 s -- "
    "within the guidance's precision -- and it was CHOSEN as the band's lower edge. The "
    "response rises as T falls across the band, so the lower edge governs and 12.5 s "
    "represents it. No new FloatSim run.",
    "EZ2: the GOVERNING envelope is T = 12.5; 14; 15 and 16.2 s only. T = 10 s and T = 20 s "
    "are outside the associated-period range for H = 24.2 m -- and T = 10 s exceeds the "
    "deep-water breaking steepness -- so they are reported as SENSITIVITY ONLY and cannot "
    "govern. T = 12.5 s sits 0.042 s below the band's lower bound; see the wave-basis table.",
    "Stations: ROOT = the inboard end at the body's centre node, TIP = the far end. MID is "
    "closed-form for a uniform net body force (one element per member at F3's mesh).",
    "R730: all three stations are INTERNAL ACTIONS in one convention (as seen from the A "
    "end), so TIP is `-end_b` and not the raw element end force. An earlier version "
    "averaged the two raw ends for MID, which computes a LOAD -- exactly half the member's "
    "weight on Vz -- and understated the midspan stress by 46%.",
    "'dynamic' is the DYNAMIC INCREMENT about static equilibrium, solved from FloatSim's "
    "multipliers with NO gravity -- FloatSim is linearised about equilibrium, so the static "
    "weight/buoyancy balance is already in the formulation. 'total' = static + dynamic.",
    "The load path is validated against FloatSim's own per-body accelerations: 1.55% on all "
    "five bodies, 2.78% worst over eighteen samples.",
    "No code check is applied. API RP 2A-WSD checks are F5 (EY4).",
    "SCALE: the npz holds FloatSim's MODEL-scale output; the FE model is FULL scale. The "
    "multipliers are converted through `floatfea.io.froude`'s declared "
    "`joint_multiplier_yaw_locked` composite (force x 125000, locked moment x 6250000).",
)


# EVERYTHING BELOW THIS LINE USED TO BE ABOVE IT (FL1).
#
# `Row`, the station arithmetic, the joint wiring, the scale change and the two stress
# helpers now live in `floatfea/post/forces_table.py`, and so does the window loop, as
# `compute_rows`. They were MOVED, not rewritten -- see that module's docstring for why,
# and for the two things that did change on the way (a dead helper deleted, one cache
# key corrected).
#
# This script is unchanged in what it PUBLISHES: the CLI, `LABELS`, the CSV writer and
# the summary are all still here, and the names it used to define are imported back into
# its namespace below, which is what keeps `f6a_premise_check.py` and
# `f6_results_report.py` working -- both load this file by path and reach for
# `MFT._station_values` and friends.
#
# That the eight still resolve is A TEST, not a sentence here:
# `tests/unit/test_forces_table_reexports.py` loads this file by path the way those two
# consumers do and checks each name individually. It has to be a test -- a lint autofix
# dropped four of them once already, with nothing red, and a comment cannot survive a
# tool that rewrites the lines it describes.


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "F4_member_forces.csv")
    ap.add_argument("--summary", type=Path, default=ROOT / "docs" / "F4_member_forces.md")
    args = ap.parse_args(argv)

    import f4_dynamic_residual as fdr

    inp = fdr.load()
    raw = np.load(fdr.NPZ, allow_pickle=False)
    built = build_superstructure()
    by_name = {b.name: b for b in built.bodies}

    # THE NUMBERS COME FROM `floatfea`, NOT FROM HERE (FL1). `GOVERNING_PERIODS` is
    # passed in rather than read as a module constant by the library, because that set is
    # exactly what a configuration changes about this loop.
    computed = compute_rows(
        built,
        inp,
        raw,
        GOVERNING_PERIODS,
        progress=lambda line: print(line, flush=True),
    )
    rows = computed.rows
    instant, instant_sens = computed.instant, computed.instant_sens

    _write_csv(args.out, rows, by_name)
    _write_summary(args.summary, rows, by_name, inp, instant, instant_sens)
    print(f"\n  wrote {args.out.relative_to(ROOT)} ({len(rows)} rows)")
    print(f"  wrote {args.summary.relative_to(ROOT)}")
    return 0


def _member_of(by_name: dict[str, BodyModel], body: str, label: str) -> Member:
    return next(m for m in by_name[body].members if m.label == label)


F_LADDER = (0.5, 0.75, 1.0)
"""EY0's f sensitivity. DY0's fraction of body mass carried on the members."""


def f_sensitivity() -> list[tuple[float, str, float, float, float]]:
    """ROOT values at each `f`, STATIC only (EY0: "static, cheap").

    `f` moves mass between the members and the lumped remainder, so it changes both the
    distributed load each member carries and the point load at the centre node. It is a
    sensitivity and not a sweep to pick a value from: `f = 0.75` is the basis (Xabier,
    6 Oct) and the other two bracket it.

    Reported at the ROOT because that is where the bending is largest, and per body
    rather than per member -- with the SPREAD across a body's own members printed, so a
    reader can see for themselves that the four arms are symmetric under self-weight
    instead of taking my word for it.
    """
    out: list[tuple[float, str, float, float, float]] = []
    for frac in F_LADDER:
        built = build_superstructure(measurement_fraction=frac)
        by_name = {b.name: b for b in built.bodies}
        static = _static_rows(built)
        for body in built.bodies:
            sigmas = []
            moments = []
            for member in body.members:
                values = static[(body.name, member.label, "ROOT")]
                sigmas.append(_stresses(member, values)[0])
                moments.append(float(math.hypot(values[4], values[5])))
            spread = (max(sigmas) - min(sigmas)) / max(sigmas) if max(sigmas) > 0.0 else 0.0
            out.append((frac, body.name, max(moments), max(sigmas), spread))
        del by_name
    return out


def _write_csv(path: Path, rows: list[Row], by_name: dict[str, BodyModel]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        # THE LABELS ARE WRITTEN RAW, NOT THROUGH `csv.writer`. A label containing a comma
        # comes back QUOTED, so the line starts with `"` and not `#`, and a consumer
        # skipping comments by prefix silently reads the first label as the header row --
        # which is what happened the first time this file was read back. Commas become
        # semicolons so the line can never need quoting.
        for label in LABELS:
            fh.write("# " + label.replace(",", ";") + chr(10))
        w = csv.writer(fh)
        w.writerow(
            [
                "body",
                "member",
                "station",
                "period_full_s",
                "basis",
                *COMPONENTS,
                "sigma_Pa",
                "tau_Pa",
            ]
        )
        for r in rows:
            member = _member_of(by_name, r.body, r.member)
            sigma, tau = _stresses(member, r.values)
            w.writerow(
                [
                    r.body,
                    r.member,
                    r.station,
                    "" if math.isnan(r.period_full_s) else f"{r.period_full_s:g}",
                    r.basis,
                    *[f"{v:.6e}" for v in r.values],
                    f"{sigma:.6e}",
                    f"{tau:.6e}",
                ]
            )


def _write_summary(
    path: Path,
    rows: list[Row],
    by_name: dict[str, BodyModel],
    inp: Any,
    instant: dict[tuple[str, str, str], tuple[float, float]],
    instant_sens: dict[tuple[str, str, str], tuple[float, float]],
) -> None:
    """The envelope over the six cases, the ten most loaded stations, and the f sweep."""
    env: dict[tuple[str, str, str], tuple[float, float, str]] = {}
    for r in rows:
        if not r.basis.startswith("total"):
            continue
        if r.period_full_s not in GOVERNING_PERIODS:
            continue  # EZ2(a): out-of-range cases do not set the envelope
        member = _member_of(by_name, r.body, r.member)
        sigma, _tau = _stresses(member, r.values)
        key = (r.body, r.member, r.station)
        where = f"T = {r.period_full_s:g} s, {r.basis}"
        if key not in env or sigma > env[key][0]:
            env[key] = (sigma, float(np.max(np.abs(r.values))), where)

    top = sorted(instant.items(), key=lambda kv: -kv[1][0])[:10]
    lines = [
        "# F4 step 3 — member forces, PRELIMINARY",
        "",
        "**Every line below is preliminary until F4 closes.** The labels are the deliverable "
        "as much as the numbers are.",
        "",
    ]
    lines += [f"* {label}" for label in LABELS]
    lines += [
        "",
        "## The ten most loaded member-stations, by indicative sigma",
        "",
        "| # | body | member | station | governing case "
        "| sigma at the instant (MPa) | envelope upper bound (MPa) |",
        "|---|---|---|---|---|---|---|",
    ]
    for n, ((body, label, station), (sigma, period)) in enumerate(top, start=1):
        bound = env.get((body, label, station), (0.0, 0.0, "-"))
        lines.append(
            f"| {n} | {body} | `{label}` | {station} | T = {period:g} s | "
            f"{sigma / 1e6:.1f} | {bound[0] / 1e6:.1f} |"
        )
    lines += [
        "",
        "## The two cases OUTSIDE the associated-period range (sensitivity only)",
        "",
        "**EZ2(b): these do not govern and are not in the table above.** `T = 10 s` exceeds "
        "the deep-water breaking steepness and `T = 20 s` is too long for this height, so "
        "neither can set a design envelope. They are reported because the response at "
        "`T = 10 s` is the largest in the whole sweep and a reader who saw only the "
        "governing block would not know that.",
        "",
        "| body | member | station | case | sigma at the instant (MPa) |",
        "|---|---|---|---|---|",
    ]
    for (body, label, station), (sigma, period) in sorted(
        instant_sens.items(), key=lambda kv: -kv[1][0]
    )[:10]:
        lines.append(f"| {body} | `{label}` | {station} | T = {period:g} s | {sigma / 1e6:.1f} |")
    lines += [
        "",
        "## The wave basis, per case (EZ2(d))",
        "",
        f"`H = {WAVE_HEIGHT_FULL_M} m` full scale. Deep-water `lambda = g T^2 / (2 pi)`; the "
        "associated-period band is `sqrt(6.5 H) .. sqrt(11 H)`; the breaking limit is "
        "`H/lambda = 1/7 = 0.1429`.",
        "",
        "| T (s) | lambda (m) | H/lambda | position | basis |",
        "|---|---|---|---|---|",
    ]
    for period in sorted(inp.periods_full_s):
        lam, s, where = steepness(period)
        # NOT named `basis`: that shadows the imported `floatfea.basis` module, and the
        # section below reads `basis.chs_class_limits()` -- which is how this was found.
        which = "**governing**" if period in GOVERNING_PERIODS else "sensitivity only"
        lines.append(f"| {period:g} | {lam:.1f} | {s:.4f} | {where} | {which} |")
    lines += [
        "",
        "**`T = 12.5 s` sits `0.042 s` below `sqrt(6.5 x 24.2) = 12.542 s`, and FA0 RULES "
        "THAT IT STAYS.** `0.3%` below the bound is within the guidance's own precision, "
        "and the case was CHOSEN as the band's lower edge. The reason it matters is the "
        "direction: **the response rises as `T` falls across the band**, so the lower edge "
        "is what governs and `12.5 s` is what represents it -- which is also why it carries "
        "8 of the governing top ten. No new FloatSim run.",
        "",
        "## The section these stresses are computed on",
        "",
    ]
    member = by_name["platform"].members[0]
    area, w_bend, j, w_tors, a_shear = _section_properties(member)
    d_outer = _outer_diameter(member.section)
    wall = 0.5 * (d_outer - math.sqrt(d_outer * d_outer - 4.0 * area / math.pi))
    lines += [
        f"* `D = {d_outer:.4f} m`, `t = {wall:.5f} m`, `D/t = {d_outer / wall:.1f}` "
        f"(EN 1993-1-1 class limits {', '.join(f'{x:.1f}' for x in basis.chs_class_limits())})",
        f"* `A = {area:.4f} m^2`, `W = 2I/D = {w_bend:.4f} m^3`, `J = {j:.4f} m^4`, "
        f"`W_t = 2J/D = {w_tors:.4f} m^3`, `A_shear = kappa A = {a_shear:.4f} m^2`",
        f"* `{member.section_basis}`",
        "",
        "",
        "## The `f` sensitivity at the ROOT (static only)",
        "",
        "`f` is DY0's fraction of body mass carried on the members; the remainder is "
        "lumped at the centre node on a rigid link. **`f = 0.75` is the basis (Xabier, "
        "6 Oct)** and the other two bracket it. The last column is the spread of sigma "
        "across a body's own members, which is round-off where the body is symmetric "
        "under self-weight.",
        "",
        "| f | body | worst root moment (N·m) | sigma (MPa) | spread across members |",
        "|---|---|---|---|---|",
    ]
    for frac, body, moment, sigma, spread in f_sensitivity():
        lines.append(f"| {frac:g} | {body} | {moment:.4e} | {sigma / 1e6:.1f} | {spread:.2e} |")
    lines += [
        "## What is exact and what is not",
        "",
        "* ROOT and TIP are the element's own end nodes: **exact** at F3's mesh.",
        "* MID is **closed-form** for a uniform net body force -- the chord mean plus "
        "`w L^2 / 8` on the two bending components. A refined mesh would give it directly.",
        "* `dynamic` is **solved**, not subtracted: the dynamic joint increments with no "
        "gravity. `total = static + dynamic`.",
        "* The load path is **validated** against FloatSim's own accelerations -- 1.55% on "
        "all five bodies, 2.78% worst over eighteen (case, step, body) samples.",
        "* sigma and tau are **indicative**: `sigma = |N|/A + sqrt(My^2+Mz^2)/W` and "
        "`tau = |T|/(2W_t) + sqrt(Vy^2+Vz^2)/A_shear`. No von Mises combination is formed, "
        "because the two peak at different points of the section.",
        "* **No code check is applied.** API RP 2A-WSD is F5.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    raise SystemExit(main())
