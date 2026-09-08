"""Generate `docs/milestones/F2_figures.md` from the shipped runner (BT0).

Hand-typed numbers in `docs/milestones/F2.md` have moved **eight times** across
this milestone, and three review rounds running found a figure that described the
repository as it was one commit earlier. The plan is a locked artifact; a number
inside it that nothing regenerates is a claim with no owner.

So the numbers that have actually moved -- the per-defect margins, the floor, the
counts, the boundary -- are generated here and referenced from the plan by name:

    {{fig:margin_dropped_flip}}

`tests/test_plan_figures.py` asserts every name the plan references exists, and
that re-running this script reproduces the file byte for byte. A stale figure is
then a failing build rather than a review finding.

SCOPE, deliberately narrow (BT0): the figures that move. Not the whole document.
A generated file that tries to own every number becomes a second source of truth
nobody reads, and the prose around these figures is still prose.

Usage:  python scripts/regen_figures.py [--check]
"""
from __future__ import annotations

import argparse
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "milestones" / "F2_figures.md"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))


def _figures() -> list[tuple[str, str]]:
    import test_corpus_configurations as C
    from floatfea.tolerances import (BOUNDARY_BISECTION_CONVERGENCE,
                                     PATCH_TEST_COUNTER_HEADROOM,
                                     PATCH_TEST_EXACTNESS,
                                     PATCH_TEST_EXACTNESS_COUNTER_DEFECT as CD)

    ceil = PATCH_TEST_EXACTNESS
    rows: list[tuple[str, str]] = []

    rows.append(("corpus_entries", f"{len(C.ENTRIES)}"))
    rows.append(("corpus_solved", f"{len(C.SOLVED)}"))

    worst = max((max(C._oob_state(e, st) for st in C.STATES) / ceil, e["id"])
                for e in C.SOLVED)
    rows.append(("clean_worst_ratio", f"{worst[0]:.4f}x"))
    rows.append(("clean_worst_entry", worst[1]))

    for kind in C.INJECTED_DEFECTS:
        vals = [(max(C._oob_with_injected(e, st, kind) for st in C.STATES) / ceil,
                 e["id"], C.member_lambda(e)) for e in C.SOLVED]
        lo = min(vals)
        rows.append((f"margin_{kind}", f"{lo[0]:.4g}x"))
        rows.append((f"margin_{kind}_at", f"{lo[1]} (L/r_min {lo[2]:.0f})"))
        below = sum(1 for v in vals if v[0] <= 1.0)
        rows.append((f"below_ceiling_{kind}", f"{below} of {len(vals)}"))

    exempt: dict[str, int] = {}
    detected = 0
    for e in C.SOLVED:
        for kind in C.INJECTED_DEFECTS:
            if C.classify(e, kind) != "below resolution":
                continue
            exempt[kind] = exempt.get(kind, 0) + 1
            if max(C._oob_with_injected(e, st, kind)
                   for st in C.STATES) > ceil:
                detected += 1
    rows.append(("exempt_total", f"{sum(exempt.values())} of "
                 f"{len(C.SOLVED) * len(C.INJECTED_DEFECTS)}"))
    rows.append(("exempt_by_defect",
                 ", ".join(f"{k} {v}" for k, v in sorted(exempt.items()))))
    rows.append(("exempt_detected", f"{detected}"))

    dev = [abs(C.injected_delta(e, "one_element_scaled") - CD) / math.ulp(CD)
           for e in C.SOLVED]
    rows.append(("calibration_ulp_worst", f"{max(dev):.3f} ULP"))

    entry, edge = C._smallest_detection_edge()
    rows.append(("detection_edge", f"{edge:.4e}"))
    rows.append(("detection_edge_at", entry))
    rows.append(("counter_defect_over_edge", f"{CD / edge:.4g}x"))
    rows.append(("counter_headroom_room",
                 f"{PATCH_TEST_COUNTER_HEADROOM / (CD / edge):.2f}x"))

    lo, hi, lo_at, hi_at, n, unbracketed, refused, lo_n = _boundary_margins(
        C, ceil, CD)
    rows.append(("boundary_margin_min", f"{lo:.6g}x"))
    rows.append(("boundary_margin_max", f"{hi:.6g}x"))
    rows.append(("boundary_margin_spread", f"{hi / lo:.3f}x"))
    # `boundary_margin_min_at` IS WITHDRAWN (R187). The minimum is a PLATEAU,
    # and which base is reported as owning it is decided by the bisection's
    # convergence threshold rather than by anything about the gate: moving that
    # threshold moves the name while the value stands.
    rows.append(("boundary_margin_min_plateau", f"{lo_n} bases"))
    rows.append(("boundary_margin_max_at", hi_at))
    rows.append(("boundary_margin_bases", f"{n} converged"))
    rows.append(("boundary_margin_unbracketed",
                 f"{len(unbracketed)}: {', '.join(unbracketed) or 'none'}"))
    rows.append(("boundary_margin_refused",
                 f"{len(refused)}: {', '.join(refused) or 'none'}"))
    rows.append(("calibration_ulp_histogram", _ulp_histogram(C, CD)))
    return rows


def _ulp_histogram(C, CD: float) -> str:
    """The calibration deviation's EXACT distribution over the solved corpus.

    One count per solved entry, no sampling. The version before this drew 5000
    times with replacement from those same deterministic points, which makes the
    cells a property of the SEED -- they swing +/-20% on it -- rather than of the
    code (R185). Resampling deterministic points measures the sampler.

    And the version before THAT was one unseeded draw published in
    `tolerances.py`, contradicting this in every cell (R184/BI3). It is removed.
    """
    counts: dict[int, int] = {}
    for entry in C.SOLVED:
        k = int(round(abs(C.injected_delta(entry, "one_element_scaled") - CD)
                      / math.ulp(CD)))
        counts[k] = counts.get(k, 0) + 1
    return ", ".join(f"{k} ULP x{counts[k]}" for k in sorted(counts))


def _boundary_margins(C, ceil: float, CD: float):
    """`(min, max, min_at, max_at)` of the margin at the classification boundary.

    The operating point the rule decides at: `one_element_scaled`'s effective
    size is `CD` identically on every entry, so "the corpus pair closest to the
    boundary" selects nothing (R157). This bisects each base's member length
    until the SHEAR defect's effective size crosses `CD`, and reports the range.

    A RANGE, BECAUSE IT IS NOT ONE NUMBER AND BOTH EARLIER CLAIMS SAID IT WAS
    (R169). This file published `9267x` "on one family" and the reviewer
    published `7630.2x` "to five digits across nine"; neither was a
    disagreement, because the held variable is ORIENTATION -- axis-aligned bases
    give ~7616-7659, skew ~9267, rolled and anisotropic up to ~23919. Both
    single-number claims are withdrawn on both sides, and what is published is
    what varies and by how much.

    It also stops depending on which base is selected: the bisection discards the
    base's length, so "the corpus's stubbiest entry" never determined the answer
    -- 38 bases give bit-identical results, and one admissible entry added to the
    corpus moved the published figure from 9267x to 7630x without anything about
    the gate changing.
    """
    out, unbracketed, refused = [], [], []
    for entry in C.SOLVED:
        base = dict(entry)

        # THE BRACKET STARTS AT THE SHORTEST ADMISSIBLE MEMBER, not at 1 metre.
        # A fixed low end of 1.0 is below `BEAM_ADMISSION_L_OVER_D` for most
        # sections, so `_build` raised and 80 of 110 bases were "refused" -- an
        # artefact of the probe, not a property of the base.
        from floatfea.model.admissibility import member_l_over_d
        from floatfea.tolerances import (BEAM_ADMISSION_L_OVER_D,
                                         BOUNDARY_BISECTION_CONVERGENCE)
        try:
            outer = 1.0 / member_l_over_d(1.0, C._entry_section(entry))
        except Exception as exc:
            refused.append(f"{entry['id']} ({type(exc).__name__})")
            continue
        lo, hi = ((1.0 + BOUNDARY_BISECTION_CONVERGENCE)
                  * BEAM_ADMISSION_L_OVER_D * outer), 1.0e9

        # THE BRACKET IS CHECKED BEFORE IT IS TRUSTED (R175). Without this the
        # loop ran inside a fixed [1, 1e7] and never asked whether the crossing
        # was in it: 13 of 110 bases never left `lo = 1.0`, and the published
        # MINIMUM was one of them -- reported as a margin "at the boundary" while
        # sitting at `eff/CD = 0.0296`, 34x below the crossing it was named for.
        # A base whose crossing lies outside the bracket is recorded by name as
        # unbracketed. It is never a margin.
        try:
            base["stations"] = repr(lo)
            at_lo = C.injected_delta(base, "dropped_shear_parameter")
            base["stations"] = repr(hi)
            at_hi = C.injected_delta(base, "dropped_shear_parameter")
        except Exception as exc:
            # AND NOTHING IS SWALLOWED (R175). `except: continue` dropped five
            # bases silently, which is a skip by another name.
            refused.append(f"{entry['id']} ({type(exc).__name__})")
            continue

        if not (at_lo >= CD > at_hi):
            unbracketed.append(entry["id"])
            continue

        # EVERY REFUSAL IS RECORDED BY NAME AND TYPE, never swallowed (R175).
        # Changing a base's length can make its orientation node degenerate or
        # its member inadmissible; that is a fact about the probe on that base
        # and it is published, not dropped.
        try:
            for _ in range(200):
                mid = (lo * hi) ** 0.5
                base["stations"] = repr(mid)
                if C.injected_delta(base, "dropped_shear_parameter") < CD:
                    hi = mid
                else:
                    lo = mid
                if hi / lo < 1.0 + BOUNDARY_BISECTION_CONVERGENCE:
                    break
            base["stations"] = repr(lo)
            eff = C.injected_delta(base, "dropped_shear_parameter")
            resp = max(C._oob_with_injected(base, st, "dropped_shear_parameter")
                       for st in C.STATES) / ceil
        except Exception as exc:
            refused.append(f"{entry['id']} ({type(exc).__name__})")
            continue
        out.append((float(resp / (eff / CD)), entry["id"]))

    if not out:
        raise RuntimeError(
            "no base bracketed the classification boundary; the range below "
            "would be empty and the figures would publish nothing")
    out.sort()
    # The plateau: how many bases share the minimum to the digits published.
    lo_n = sum(1 for v, _ in out if f"{v:.6g}" == f"{out[0][0]:.6g}")
    return (out[0][0], out[-1][0], out[0][1], out[-1][1],
            len(out), sorted(unbracketed), sorted(refused), lo_n)


def render() -> str:
    # NO `Generated at <sha>` LINE (R179). It recorded the commit the file was
    # written at, which is never the commit it is committed in -- so it was false
    # the moment it landed, and once `--check` compared the whole file it failed
    # on the sha rather than on a figure. Content equality answers the staleness
    # question by itself; the sha added a claim nothing could keep true.
    lines = [
        "# F2 figures — GENERATED, do not edit",
        "",
        "Produced by `scripts/regen_figures.py` from the shipped runner.",
        "`docs/milestones/F2.md` references these by name as `{{fig:NAME}}`, and",
        "`tests/test_plan_figures.py` fails if a referenced name is missing or if",
        "this file is not what a fresh run produces.",
        "",
        "| name | value |",
        "|---|---|",
    ]
    lines += [f"| `{n}` | {v} |" for n, v in _figures()]
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    text = render()
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        # THE WHOLE FILE, INCLUDING THE COMMIT LINE (R170/R179). The comparison
        # used to stop at `Generated at`, so anything appended below it was never
        # checked but WAS read by the plan's resolver -- a hand-typed row could
        # sit there, and one was planted to prove it. And the commit line itself
        # was false at the commit that published it, which only a whole-file
        # comparison can catch.
        if current != text:
            print("regen_figures: F2_figures.md is not what this script "
                  "produces at HEAD", file=sys.stderr)
            return 1
        print("regen_figures: up to date")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"regen_figures: wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
