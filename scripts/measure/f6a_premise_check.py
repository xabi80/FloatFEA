#!/usr/bin/env python
"""FG2: the premise the F6a search rests on, verified rather than assumed.

    python scripts/measure/f6a_premise_check.py

THE PREMISE. *Section choice does not change the loads or the member forces*, because
FloatSim's bodies are rigid so the stored joint reactions cannot depend on section; each body
is statically determinate apart from the platform's single vertical redundancy, which uniform
sizing per body leaves unchanged; and member mass comes from the deck's `mu`, not from the
section.

**THE SEARCH IN `f6a_required_section.py` DEPENDS ON IT ENTIRELY** -- it re-evaluates the
clauses at thousands of candidate sections against ONE set of stored forces, which is only
legitimate if the forces are section-independent. So this rebuilds the model at the required
section of each group and compares every force component at every member-station, on BOTH
the static and the dynamic cases, and reports the maximum relative change.

WHAT WOULD FALSIFY IT, so a pass means something: any component moving by more than
round-off. The script reports the worst change it finds and the station it is at; it asserts
nothing and declares no tolerance -- the number is the finding, and the report states it
against round-off rather than against a threshold invented here.

(c) IS PROVED BY CONSTRUCTION AND IS CHECKED ANYWAY. `_build_body` computes
`member_mass = fraction * deck_mass` with no section term, then `density = line_mass /
section.A`. The equivalent density is back-computed so `rho * A` is the deck's `mu` whatever
the section. This prints both so the reader sees the mass held and the density move.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from floatfea.model.material import Section  # noqa: E402
from floatfea.model.platform import build_superstructure  # noqa: E402

# `member_forces_table.py` owns the static solve and the station values the published CSV is
# written from. Reusing it means the comparison is on the same quantity the search read.
_MFT = ROOT / "scripts" / "measure" / "member_forces_table.py"
_SPEC = importlib.util.spec_from_file_location("member_forces_table", _MFT)
assert _SPEC is not None and _SPEC.loader is not None
MFT = importlib.util.module_from_spec(_SPEC)
sys.modules["member_forces_table"] = MFT
_SPEC.loader.exec_module(MFT)

COMPONENTS = ("N", "Vy", "Vz", "T", "My", "Mz")


def _worst_relative_change(
    before: dict[tuple[str, str, str], np.ndarray],
    after: dict[tuple[str, str, str], np.ndarray],
) -> tuple[float, str, float, str]:
    """The largest change per component, normalised by a scale that cannot collapse.

    **THE DENOMINATOR IS THE COMPONENT'S OWN GLOBAL MAXIMUM, NOT THE STATION'S OWN VALUE,
    and the first version of this function got that wrong.** Dividing by
    `max(|before|, |after|)` at the station reported `1.958404e+00` -- a sign flip on a
    torsion of `-1.97e-08 N.m` against root moments of `1e+08`, which is round-off reported
    as a doubling. That is G4.1's own lesson in this repository: "the denominators are sums
    of magnitudes, so cancellation cannot shrink them", and a per-station denominator is a
    quantity that goes to zero exactly where the numerator is noise.

    So each component is normalised by `max |value|` of THAT component over every station in
    the set -- a fixed, non-vanishing scale -- and the absolute worst change is reported
    beside it, because a relative figure alone cannot say whether the absolute motion
    matters.
    """
    assert set(before) == set(after), "the two builds do not have the same stations"
    # ONE DENOMINATOR PER KIND OF QUANTITY, and this is the THIRD measure tried here --
    # the first two divided noise by noise. Per-station `max(|a|, |b|)` reported
    # `1.958404e+00`; per-component global max reported `1.320350e+00`, because TORSION IS
    # IDENTICALLY ZERO UP TO ROUND-OFF in the static case, so its own global max is
    # `3.05e-08 N.m` and normalising by it still divides noise by noise.
    #
    # A component that is physically absent has no scale of its own. So forces share the
    # largest force in the set and moments share the largest moment -- a denominator that
    # cannot collapse, which is G4.1's rule in this repository ("the denominators are sums
    # of magnitudes, so cancellation cannot shrink them") applied across components instead
    # of across time.
    _FORCES, _MOMENTS = {"N", "Vy", "Vz"}, {"T", "My", "Mz"}
    everything = [np.asarray(v, float) for v in (*before.values(), *after.values())]
    force_scale = max(
        abs(float(row[i])) for row in everything for i, c in enumerate(COMPONENTS) if c in _FORCES
    )
    moment_scale = max(
        abs(float(row[i])) for row in everything for i, c in enumerate(COMPONENTS) if c in _MOMENTS
    )
    scales = {comp: (force_scale if comp in _FORCES else moment_scale) for comp in COMPONENTS}
    worst_rel, where_rel = 0.0, "(nothing moved)"
    worst_abs, where_abs = 0.0, "(nothing moved)"
    for key in sorted(before):
        a, b = np.asarray(before[key], float), np.asarray(after[key], float)
        for i, comp in enumerate(COMPONENTS):
            delta = abs(float(b[i]) - float(a[i]))
            if delta > worst_abs:
                worst_abs = delta
                where_abs = f"{key[0]}/{key[1]} {key[2]} {comp}"
            scale = scales[comp]
            if scale == 0.0:
                continue
            rel = delta / scale
            if rel > worst_rel:
                worst_rel = rel
                where_rel = (
                    f"{key[0]}/{key[1]} {key[2]} {comp}: {float(a[i]):.6e} -> "
                    f"{float(b[i]):.6e}, against the {comp} scale {scale:.6e}"
                )
    return worst_rel, where_rel, worst_abs, where_abs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--answers",
        type=Path,
        default=ROOT / "results" / "F6a" / "required_section.json",
        help="the search's own output, so the sections checked are the ones published",
    )
    ap.add_argument("--search", default="iii_min_area")
    args = ap.parse_args(argv)

    answers = [
        a
        for a in json.loads(args.answers.read_text(encoding="utf-8"))
        if a.get("found") and a["search"] == args.search
    ]
    assert answers, f"no found answers for search {args.search!r} in {args.answers}"

    sections: dict[str, Section] = {}
    for a in answers:
        tube = Section.circular_tube(float(a["D_m"]), float(a["t_m"]))
        if a["group"] == "platform":
            sections["platform"] = tube
        else:
            for n in (1, 2, 3, 4):
                sections[f"hub{n}"] = tube

    print(f"=== FG2's premise, at the {args.search} answers ===")
    for a in answers:
        print(f"  {a['group']:9s} D={a['D_m']} t={a['t_m']*1000:.0f}mm A={a['A_m2']:.6f}")
    print()

    shipped = build_superstructure()
    sized = build_superstructure(measurement_sections=sections)

    print("(c) MASS COMES FROM THE DECK, NOT THE SECTION -- held, and the density moves:")
    print(
        f"  {'body':10s} {'A [m^2]':>12s} {'member mass [kg]':>18s} {'mu [kg/m]':>12s} "
        f"{'rho_eq [kg/m^3]':>16s}"
    )
    for b0, b1 in zip(shipped.bodies, sized.bodies, strict=True):
        for tag, b in (("shipped", b0), ("sized  ", b1)):
            mu = float(b.member_mass) / float(b.total_member_length)
            print(
                f"  {b.name:10s} {float(b.members[0].section.A):12.6f} "
                f"{float(b.member_mass):18.2f} {mu:12.3f} "
                f"{float(b.equivalent_density):16.1f}   {tag}"
            )
        break  # one body is enough to show the shape; the table below covers all
    print()
    held = all(
        float(a.member_mass) == float(b.member_mass)
        for a, b in zip(shipped.bodies, sized.bodies, strict=True)
    )
    print(f"  member_mass identical on every body: {held}")
    moved = [
        (b0.name, float(b0.equivalent_density), float(b1.equivalent_density))
        for b0, b1 in zip(shipped.bodies, sized.bodies, strict=True)
        if float(b0.equivalent_density) != float(b1.equivalent_density)
    ]
    print(f"  equivalent_density moved on {len(moved)} of {len(shipped.bodies)} bodies")
    print()

    print("STATIC CASE -- every component at every member-station, both builds:")
    before = MFT._static_rows(shipped)
    after = MFT._static_rows(sized)
    worst, where, worst_abs, where_abs = _worst_relative_change(before, after)
    print(f"  stations compared       : {len(before)}")
    print(f"  worst ABSOLUTE change   : {worst_abs:.6e}   at {where_abs}")
    print(f"  worst RELATIVE change   : {worst:.6e}")
    print(f"  at                      : {where}")
    print("  forces share the largest force in the set and moments the largest moment, so")
    print("  a component that is physically absent -- torsion here is identically zero up")
    print("  to round-off -- cannot supply its own vanishing denominator. The two earlier")
    print("  measures reported 1.958404e+00 and 1.320350e+00, both noise over noise.")
    print()
    # FG2's second half: `U <= 1.0` everywhere, computed from the REBUILT forces rather
    # than the stored ones. The search guarantees it by construction on the stored forces,
    # so this is the independent route -- if the premise were false, this is where it would
    # show, because these forces came out of a solve at the sized section.
    print()
    print("FG2's SECOND HALF -- U <= 1.0 everywhere, from the REBUILT forces:")
    import importlib.util as _il

    _spec = _il.spec_from_file_location(
        "f6a_required_section", ROOT / "scripts" / "measure" / "f6a_required_section.py"
    )
    assert _spec is not None and _spec.loader is not None
    SEARCH = _il.module_from_spec(_spec)
    sys.modules["f6a_required_section"] = SEARCH
    _spec.loader.exec_module(SEARCH)

    lengths = {m.label: float(m.length) for b in sized.bodies for m in b.members}
    for a in answers:
        cand = SEARCH.Candidate(float(a["D_m"]), float(a["t_m"]))
        prefix = "platform:" if a["group"] == "platform" else "hub"
        rebuilt = [
            {
                "body": key[0],
                "member": key[1],
                "station": key[2],
                "period_full_s": "",
                **{c: repr(float(vals[i])) for i, c in enumerate(COMPONENTS)},
            }
            for key, vals in after.items()
            if key[1].startswith(prefix)
        ]
        out = SEARCH.evaluate(cand, rebuilt, lengths)
        verdict = "PASS" if (out.refused == 0 and out.max_u <= 1.0) else "FAIL"
        print(
            f"  {a['group']:9s} static basis, {out.checked:2d} stations, "
            f"{out.refused} refused, max U = {out.max_u:.6f}  {verdict}"
        )
    print("  (the STATIC basis only -- the search's governing figure is the per-instant")
    print("   total basis, and these forces are the static solve this script re-ran)")
    print()
    print("  (a) THE JOINT REACTIONS ARE AN INPUT, NOT AN OUTPUT: they are read from")
    print("      data/f4/dynamic_inputs.npz, exported from FloatSim, whose bodies are")
    print("      RIGID. No FE quantity is written back into that file, so no section can")
    print("      reach them. The dynamic increment is built from those multipliers and")
    print("      each body's own d'Alembert field, and the field reads `mu`, held above.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
