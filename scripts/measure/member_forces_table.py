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
from floatfea.io.froude import froude_factor  # noqa: E402

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
from floatfea.run.pipeline import (  # noqa: E402
    validated_export_scale,
    wave_basis_from_sidecar,
)
from floatfea.solve.inertia_relief import solve_inertia_relief  # noqa: E402,F401

# R902: THE SCALE AND THE HEIGHT COME FROM THE SIDECAR, NOT FROM A LITERAL HERE.
# `FROUDE_LAMBDA = 50.0` and `WAVE_HEIGHT_FULL_M = 24.2` used to be module constants in
# this file, and `steepness()` computed the band, the H/lambda ratio and the BREAKING
# verdict from the second one. The comment a few lines above records R805 / FN0 -- "a
# module constant there silently overrode a configured scale" -- which is the same defect
# in the same file, and the docstring on the height asserted a derivation
# (`0.484 m model times the Froude factor`) that no code performed.
#
# Measured in the sibling generator, which had the identical pair: at a sidecar recording
# `model=1.0, full=50.0` the published band was computed at `H = 24.2 m`, giving
# `0.0992 ok 0.334% short` where the recorded height gives
# `0.2050 BREAKING 30.662% short`.

"""`docs/conventions.md`'s scale. The FE model is FULL scale; FloatSim runs at MODEL.

STATED HERE, BY THE CALLER, because `floatfea.post.forces_table` no longer carries it
(R805 / FN0): a module constant there silently overrode a configured scale. This script
analyses the committed npz, which `data/f4/dynamic_inputs.provenance.json` records as
exported at `run.lambda = 50.0`, so this is the file's own scale and not a default.
"""


GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
"""EZ2(a): the cases the GOVERNING envelope is taken over.

**EZ2 corrects the case selection, and it is Xabier's correction of his own basis.** For
At the recorded height the associated-period range by DNV practice is
`sqrt(6.5 H) <= T <= sqrt(11 H)`; the wave-basis table in the summary prints the edges it
was computed at, and no number for them is written here (R907 -- a literal here was false
at every height but one). The two cases outside it
are reported separately and are not allowed to govern:

**AND AT THE REFERENCE SEA STATE T = 12.5 s SITS BELOW THE LOWER BOUND IT IS BEING
INCLUDED UNDER.** Which cases fall where, and by how much, is computed per run and printed
in the summary's wave-basis table -- no figure for any of it is written here, because a
figure here was true at one height and false at every other (R907, R930: an earlier
revision of this paragraph said "no number for them is written here" two lines above a
line that wrote one). EZ2(a) names it as governing and that is what ships, but the
directive's own criterion and its own case list disagree by that much, so the fact is here
rather than passed over. It is the lowest-period governing case and therefore the one most
likely to carry the envelope, which is why the discrepancy is worth a reader's attention.
"""

SENSITIVITY_PERIODS = (10.0, 20.0)
"""EZ2(b): outside the associated-period range; `T = 10 s` exceeds breaking steepness."""


def steepness(period_full_s: float, h_full_m: float) -> tuple[float, float, str, str]:
    """`(lambda, H/lambda, position)` for one case, deep water.

    `lambda = g T^2 / (2 pi)`. The position string is what EZ2(d) asks for on every label
    line, and it names the two independent reasons a case can be out of range -- the
    period band and the steepness limit -- rather than collapsing them into "outside".
    """
    lam = 9.81 * period_full_s * period_full_s / (2.0 * math.pi)
    s = h_full_m / lam
    lo = math.sqrt(6.5 * h_full_m)
    hi = math.sqrt(11.0 * h_full_m)
    # **FOUR OUTCOMES, DECIDED ONCE (R944).** The prose below this table used to decide
    # the same question with `math.sqrt(6.5 * h_full) <= 12.5` -- ONE edge of a two-edged
    # interval -- so where the band's UPPER edge had fallen past 12.5 s, which happens at
    # `H = 156.25/11 = 14.2045 m`, the document published "`T = 12.5 s` is INSIDE the
    # band" while this row said "above the band ... by 2.012 s". Measured at H = 10 m:
    # three places in one file, two answers. The category is returned so the prose reads
    # the classification instead of repeating half of it.
    if s > 1.0 / 7.0:
        category = "breaking"
        where = f"BREAKING (H/L {s:.4f} > 1/7); and below the band {lo:.3f}-{hi:.3f} s"
    elif period_full_s < lo:
        category = "below"
        where = f"below the band {lo:.3f}-{hi:.3f} s by {lo - period_full_s:.3f} s"
    elif period_full_s > hi:
        category = "above"
        where = f"above the band {lo:.3f}-{hi:.3f} s by {period_full_s - hi:.3f} s"
    else:
        category = "in"
        where = f"in the band {lo:.3f}-{hi:.3f} s"
    return lam, s, where, category


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
    # R925: the two factors here were LITERALS at lambda = 50 -- "force x 125000, locked
    # moment x 6250000" -- published verbatim into `docs/F4_member_forces.csv:17` and
    # `docs/F4_member_forces.md:21` on BOTH caveat branches. At an npz legitimately
    # exported at lambda = 25, which the R908 validator ADMITS because both records agree,
    # `froude_factor` gives 15625 and 390625: the deliverables would state a conversion
    # 8x too large on force and 16x on moment, above a table whose numbers are right.
    # The placeholder is replaced in `main` from `froude_factor(..., lam_scale)`.
    "SCALE: (resolved per run; see main)",
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
    ap.add_argument(
        "--provenance",
        type=Path,
        default=ROOT / "data" / "f4" / "dynamic_inputs.provenance.json",
        help=(
            "the export's provenance sidecar; the authority for the scale AND the "
            "height, and the single record both are resolved from (R927)"
        ),
    )
    args = ap.parse_args(argv)
    # R902 / R903: through the one validated door (R896), so this reader and
    # `floatfea run` cannot disagree about the same recorded sidecar.
    _basis = wave_basis_from_sidecar(args.provenance)
    h_full = float(_basis["wave_height_full_m"])

    import f4_dynamic_residual as fdr

    inp = fdr.load()
    raw = np.load(fdr.NPZ, allow_pickle=False)
    # R908: ONE RESOLVED SCALE, not the sidecar's copy of it. This read was
    # `float(_basis["lambda"])`, which made a published CSV's Froude scale the sidecar's
    # `run.lambda` with nothing comparing it against the npz's own key -- 2402 diff lines
    # and governing ROOT stress 455.7 -> 275.3 MPa at `run.lambda = 25.0`, at exit 0.
    # R927: THE SAME RECORD the height came from, not `fdr.NPZ`'s own sidecar.
    lam_scale = validated_export_scale(fdr.NPZ, args.provenance)
    # R907: THE CAVEAT BLOCK STATES WHICH PERIODS ARE WHERE, AT ONE HEIGHT. Two entries
    # name `H = 24.2 m`, `sqrt(6.5*H) = 12.542 s` and the exact governing set, and they
    # are published verbatim into the summary. R902 made the band track the recorded
    # height and did not touch them, so at another height the caveats contradict the
    # wave-basis table printed a few lines below them. The premises are asserted and the
    # generator refuses, rather than a published caveat being false; generating the
    # caveat text from the computed sets is FT2.6's business, since FT2.6 is what
    # produces a sidecar at another sea state (FS3 already queues the caveat record).
    # NO HEIGHT LITERAL IN THE CHECK EITHER. My first version of this assertion was
    # `abs(h_full - 24.2) > 0.0` -- exact equality written in the shape of a tolerance,
    # against a hardcoded height, in the generator R902 had just removed a hardcoded
    # height from. What the check actually needs to know is whether the PUBLISHED caveat
    # text still agrees with the computed band, so it asks that directly: the figures the
    # caveats state must be the figures this run computes.
    _lo, _hi = math.sqrt(6.5 * h_full), math.sqrt(11.0 * h_full)
    _in = sorted(float(T) for T in inp.periods_full_s if _lo <= float(T) <= _hi)
    _kept = sorted(set(GOVERNING_PERIODS) - set(_in))
    _text = " ".join(LABELS)
    _stated = (f"H = {h_full:g} m" in _text) and (f"= {_lo:.3f} s" in _text)
    # NOT A REFUSAL -- see the long note in `f6_results_report.py`. Refusing here made the
    # generator unable to run at any sea state but one, which is what R902 exists to make
    # possible and what FT2.6 needs. The caveats that state a height and a band verbatim
    # are REPLACED by computed ones when they do not describe this run, so the summary is
    # always written and never carries a false caveat.
    _stale = not _stated or _kept != [12.5] or len(_in) != 3
    caveats = list(LABELS)
    # R925: THE SCALE CAVEAT IS ALWAYS COMPUTED, on both branches, because both published
    # it. `froude_factor` is the declared conversion and the only thing entitled to state
    # these numbers.
    _scale_caveat = (
        f"SCALE: the npz holds FloatSim's MODEL-scale output; the FE model is FULL scale. "
        f"The multipliers are converted through `floatfea.io.froude`'s declared "
        f"`joint_multiplier_yaw_locked` composite (force x "
        f"{_factor_text(froude_factor('force', lam_scale))}, locked moment x "
        f"{_factor_text(froude_factor('moment', lam_scale))})."
    )
    caveats = [_scale_caveat if c.startswith("SCALE: (resolved") else c for c in caveats]
    if _stale:
        caveats = [
            c
            for c in caveats
            if "associated-period range for H" not in c and "FA0: T = 12.5 s STAYS" not in c
        ]
        caveats.append(
            f"R907: the two caveats that named a height and a band verbatim DESCRIBED THE "
            f"REFERENCE SEA STATE and do not describe this run, so they are replaced by "
            f"this computed one. At H = {h_full:g} m the associated-period band is "
            f"{_lo:.3f}..{_hi:.3f} s; the periods inside it are {_in if _in else 'none'}; "
            f"periods EZ2 names as governing but which fall outside it are "
            f"{_kept if _kept else 'none'}, and each of those is kept only if a rule like "
            f"FA0 is stated for THIS height, which none is. The wave-basis table below "
            f"carries the per-case position."
        )
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
        lam_scale,
        progress=lambda line: print(line, flush=True),
    )
    rows = computed.rows
    instant, instant_sens = computed.instant, computed.instant_sens

    _write_csv(args.out, rows, by_name, caveats)
    _write_summary(args.summary, rows, by_name, inp, instant, instant_sens, h_full, caveats, _stale)
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


def _factor_text(factor: float) -> str:
    """A published Froude factor, at enough significant figures to be true (R937).

    **`:.0f` IS EXACT ONLY WHERE THE FACTOR IS AN INTEGER**, which is where `lambda**3`
    and `lambda**4` are. Solved over the whole declared `FROUDE_LAMBDA = (1.0, 1000.0)`:
    at `lambda = 1.1447` the run converts force by `1.499944` and `:.0f` published
    `force x 1` -- 33.33% too small -- and the moment factor is 33.32% out at
    `lambda = 1.1067`. The error is under 1% for `lambda` above about 2.6 and exact at
    every integer, which is why the committed `lambda = 50` pair never showed it.

    **This is a FORMAT and must never become a margin.** It chooses how many significant
    figures to print; it does not decide whether two numbers are close enough. An integer
    prints with no decimal part so the committed deliverables are unchanged, and anything
    else prints to six significant figures.
    """
    return f"{factor:.0f}" if float(factor).is_integer() else f"{factor:.6g}"


def _write_csv(
    path: Path, rows: list[Row], by_name: dict[str, BodyModel], caveats: list[str]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        # THE LABELS ARE WRITTEN RAW, NOT THROUGH `csv.writer`. A label containing a comma
        # comes back QUOTED, so the line starts with `"` and not `#`, and a consumer
        # skipping comments by prefix silently reads the first label as the header row --
        # which is what happened the first time this file was read back. Commas become
        # semicolons so the line can never need quoting.
        for label in caveats:
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
    h_full: float,
    caveats: list[str],
    stale: bool,
) -> None:
    """The envelope over the six cases, the ten most loaded stations, and the f sweep.

    `h_full` is the RECORDED full-scale wave height, passed in rather than read from a
    module constant (R902), so the band and the breaking verdict this section publishes
    are computed at the height the sidecar records and the header prints.
    """
    # R907: the membership this section states, computed once, and the reference
    # predicate that decides whether the hand-written clause still describes the run.
    _lo_b, _hi_b = math.sqrt(6.5 * h_full), math.sqrt(11.0 * h_full)
    _periods = sorted(float(x) for x in inp.periods_full_s)
    _breaking = [T for T in _periods if h_full / (9.81 * T * T / (2.0 * math.pi)) > 1.0 / 7.0]
    _past_long = [T for T in _periods if _hi_b < T]
    _in_b = [T for T in _periods if _lo_b <= T <= _hi_b]
    # **R936: ONE PREDICATE, NOT TWO THAT DISAGREE.** This was a local
    # `_reference = _breaking == [10.0] and _past_long == [20.0] and len(_in_b) == 3`,
    # a MEMBERSHIP test, while `main`'s `_stale` keys on whether the caveat text still
    # states this run's height and band. They are true on different sets, so one document
    # carried both branches at once. Measured at H = 30 m, full solve, exit 0:
    #
    #   line 20  "... kept only if a rule like FA0 is stated for THIS height, WHICH NONE IS."
    #   line 67  "... and FA0 RULES THAT IT STAYS.** `10.5%` below the bound is within
    #             the guidance's own precision"
    #
    # The criterion I wrote in the last commit -- "asserted only where a directive
    # actually ruled" -- is refuted by that run, and the membership predicate is why: it
    # is True on exactly H in [24.039, 30.153] m, a window nobody chose. The other
    # direction is in it too: at H = 24.0 the else branch published "sits `-0.010 s`
    # below ... `-0.1%` below the bound".
    #
    # `main` computes the predicate once, against the published caveat text, and passes
    # it here. There is no second definition to drift.
    _reference = not stale
    # R944: the position of `T = 12.5 s`, from the SAME call that fills the table below,
    # so the prose cannot classify it differently from the row that states it.
    _, _, _where_12_5, _cat_12_5 = steepness(12.5, h_full)
    _pos_12_5 = {"in": "INSIDE", "above": "ABOVE", "breaking": "BREAKING and below"}.get(
        _cat_12_5, "BELOW"
    )
    _breaking_txt = ", ".join(f"`T = {T:g} s`" for T in _breaking) if _breaking else "no case"
    _long_txt = ", ".join(f"`T = {T:g} s`" for T in _past_long) if _past_long else "no case"

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
    lines += [f"* {label}" for label in caveats]
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
        # R907: WHICH cases are outside, and WHY each is, are facts about one sea state.
        # At H = 50 m `T = 20 s` is IN the band (18.028..23.452 s) while this sentence
        # calls it "too long for this height", and `T = 12.5 s` is BREAKING while the
        # heading above calls the outside set two. Same two-branch form as
        # `f6_results_report.py`: the hand-written clause for the sea state it describes,
        # a computed one otherwise, so neither contradicts the table above it.
        (
            "**EZ2(b): these do not govern and are not in the table above.** `T = 10 s` "
            "exceeds the deep-water breaking steepness and `T = 20 s` is too long for "
            "this height, so neither can set a design envelope. They are reported "
            "because the response at `T = 10 s` is the largest in the whole sweep and a "
            "reader who saw only the governing block would not know that."
            if _reference
            else (
                "**EZ2(b): these do not govern and are not in the table above.** This is "
                f"not the reference sea state (`H = {h_full:g} m`), so the membership is "
                "computed rather than stated: breaking, and so unable to describe a real "
                f"wave of this height, {_breaking_txt}; longer than the band's upper edge "
                f"{_long_txt}. The reasoning in EZ2(b) is unchanged; which cases it "
                "applies to is not carried over, and the wave-basis table below gives "
                "each case's position."
            )
        ),
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
        f"`H = {h_full} m` full scale. Deep-water `lambda = g T^2 / (2 pi)`; the "
        "associated-period band is `sqrt(6.5 H) .. sqrt(11 H)`; the breaking limit is "
        "`H/lambda = 1/7 = 0.1429`.",
        "",
        "| T (s) | lambda (m) | H/lambda | position | basis |",
        "|---|---|---|---|---|",
    ]
    for period in sorted(inp.periods_full_s):
        lam, s, where, _cat = steepness(period, h_full)
        # NOT named `basis`: that shadows the imported `floatfea.basis` module, and the
        # section below reads `basis.chs_class_limits()` -- which is how this was found.
        which = "**governing**" if period in GOVERNING_PERIODS else "sensitivity only"
        lines.append(f"| {period:g} | {lam:.1f} | {s:.4f} | {where} | {which} |")
    lines += [
        "",
        # R907: COMPUTED, NOT WRITTEN. The two figures here were literals -- `0.042 s`
        # and `sqrt(6.5 x 24.2) = 12.542 s` -- so at any other recorded height this
        # published sentence stated an offset and a band edge that the table two lines
        # above contradicts. They are derived from `h_full` for the same reason the band
        # itself now is (R902).
        (
            f"**`T = 12.5 s` sits `{math.sqrt(6.5 * h_full) - 12.5:.3f} s` below "
            f"`sqrt(6.5 x {h_full:g}) = {math.sqrt(6.5 * h_full):.3f} s`, and FA0 RULES "
            f"THAT IT STAYS.** "
            f"`{(math.sqrt(6.5 * h_full) - 12.5) / math.sqrt(6.5 * h_full):.1%}` below the "
            "bound is within the guidance's own precision, "
            "and the case was CHOSEN as the band's lower edge. The reason it matters is the "
            "direction: **the response rises as `T` falls across the band**, so the lower edge "
            "is what governs and `12.5 s` is what represents it -- which is also why it carries "
            "8 of the governing top ten. No new FloatSim run."
            if _reference
            else (
                # **AND THE SIGN, WHICH THE FIRST VERSION PUBLISHED AS A NEGATIVE
                # "BELOW" (R936).** At H = 24.0 m the lower edge is 12.490 s, so
                # `T = 12.5 s` is ABOVE it and inside the band -- and the sentence read
                # "sits `-0.010 s` below ... `-0.1%` below the bound". A negative
                # distance in a direction word is not a smaller version of the same
                # fact; it is the opposite fact. Where 12.5 is inside the band there is
                # no FA0 question to answer at all.
                # **R944: THAT GUARD TESTED ONE EDGE OF A TWO-EDGED INTERVAL.** It was
                # `math.sqrt(6.5 * h_full) <= 12.5` -- the LOWER edge alone -- so once
                # the UPPER edge had fallen past 12.5 s, which happens at
                # `H = 156.25/11 = 14.2045 m`, this published "INSIDE the band" over a
                # table row reading "above the band ... by 2.012 s". Measured at
                # H = 10 m: three places in one document and two answers, and the
                # boundary straddled at H = 14.20 against 14.21.
                #
                # `steepness()` already decides this in four outcomes for the table, so
                # the classification is READ from that one call rather than half of it
                # being recomputed here.
                f"**`T = 12.5 s` is {_pos_12_5} the band at this height** -- its position "
                f"is `{_where_12_5}`, which is what the table above states. FA0 exists to "
                "rule on a case that falls BELOW the lower edge and is kept anyway; no "
                "such question arises here, so nothing is asserted about it."
                if _cat_12_5 != "below"
                else (
                    f"**`T = 12.5 s` sits `{math.sqrt(6.5 * h_full) - 12.5:.3f} s` below "
                    f"`sqrt(6.5 x {h_full:g}) = {math.sqrt(6.5 * h_full):.3f} s`, which "
                    f"is `{(math.sqrt(6.5 * h_full) - 12.5) / math.sqrt(6.5 * h_full):.1%}` "
                    "below the bound.** FA0 ruled that this case STAYS in the governing "
                    "set at the reference sea state, where the offset is `0.3%` and "
                    "within the guidance's own precision. **That ruling is NOT asserted "
                    "here**: an offset this size is not a rounding question, and no "
                    "directive has ruled on it for this height. The direction of the "
                    "response is unchanged -- it rises as `T` falls across the band -- "
                    "but which case represents the lower edge is a question for whoever "
                    "rules on the sea state."
                )
            )
        ),
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
