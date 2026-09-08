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
    from floatfea.tolerances import (PATCH_TEST_COUNTER_HEADROOM,
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

    lo, hi, lo_at, hi_at = _boundary_margins(C, ceil, CD)
    rows.append(("boundary_margin_min", f"{lo:.4g}x"))
    rows.append(("boundary_margin_max", f"{hi:.4g}x"))
    rows.append(("boundary_margin_spread", f"{hi / lo:.2f}x"))
    rows.append(("boundary_margin_min_at", lo_at))
    rows.append(("boundary_margin_max_at", hi_at))
    return rows


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
    out = []
    for entry in C.SOLVED:
        base = dict(entry)
        lo, hi = 1.0, 1.0e7
        try:
            for _ in range(200):
                mid = (lo * hi) ** 0.5
                base["stations"] = repr(mid)
                if C.injected_delta(base, "dropped_shear_parameter") < CD:
                    hi = mid
                else:
                    lo = mid
                if hi / lo < 1.000001:  # not-a-tolerance: bisection convergence
                    break
            base["stations"] = repr(lo)
            eff = C.injected_delta(base, "dropped_shear_parameter")
            resp = max(C._oob_with_injected(base, st, "dropped_shear_parameter")
                       for st in C.STATES) / ceil
        except Exception:
            continue
        if eff > 0.0:
            out.append((float(resp / (eff / CD)), entry["id"]))
    out.sort()
    return out[0][0], out[-1][0], out[0][1], out[-1][1]


def render() -> str:
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
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
    lines += ["", f"Generated at `{head}`." if head else ""]
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    text = render()
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        # The trailing commit line moves with every commit and is context, not a
        # figure; compare everything above it.
        cut = lambda s: s.split("\nGenerated at ")[0]  # noqa: E731
        if cut(current) != cut(text):
            print("regen_figures: F2_figures.md is stale", file=sys.stderr)
            return 1
        print("regen_figures: up to date")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"regen_figures: wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
