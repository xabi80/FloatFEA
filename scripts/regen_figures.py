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
import os
import platform
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "milestones" / "F2_figures.md"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))


class _Silent:
    """The `capsys` fixture the shipped headroom test takes, without pytest."""

    @staticmethod
    def disabled():
        import contextlib

        return contextlib.nullcontext()


def _figures() -> list[tuple[str, str]]:
    import test_corpus_configurations as C

    from floatfea.tolerances import (
        FIGURE_ARGMIN_TIE_WINDOW,
        PATCH_TEST_COUNTER_HEADROOM,
        PATCH_TEST_EXACTNESS,
    )
    from floatfea.tolerances import (
        PATCH_TEST_EXACTNESS_COUNTER_DEFECT as CD,
    )

    ceil = PATCH_TEST_EXACTNESS
    rows: list[tuple[str, str]] = []

    # G2.1 / V1.1 (D2 step 5). Both halves of the rigid-body gate, generated
    # from the shipped frame so the plan and `tolerances.py` cite them by name
    # instead of typing them -- R194's remedy, applied from this gate's first
    # commit rather than five rounds into it.
    import test_rigid_body_modes as RB

    model, els = RB._frame()
    k_rb = RB.assemble_dense(model, els)
    rows.append(("rigid_body_mode_ratio", f"{RB.mode_ratio(k_rb):.4e}"))
    rows.append(("rigid_body_subspace_loss", f"{RB.subspace_loss(k_rb, model):.4e}"))
    rows.append(("rigid_body_counter_ratio", f"{RB.counter_response('ratio'):.4e}"))
    rows.append(("rigid_body_counter_loss", f"{RB.counter_response('loss'):.4e}"))

    rows.append(("corpus_entries", f"{len(C.ENTRIES)}"))
    rows.append(("corpus_solved", f"{len(C.SOLVED)}"))

    worst = max((max(C._oob_state(e, st) for st in C.STATES) / ceil, e["id"]) for e in C.SOLVED)
    rows.append(("clean_worst_ratio", f"{worst[0]:.4f}x"))
    rows.append(("clean_worst_entry", worst[1]))

    for kind in C.INJECTED_DEFECTS:
        vals = [
            (
                max(C._oob_with_injected(e, st, kind) for st in C.STATES) / ceil,
                e["id"],
                C.member_lambda(e),
            )
            for e in C.SOLVED
        ]
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
            if max(C._oob_with_injected(e, st, kind) for st in C.STATES) > ceil:
                detected += 1
    rows.append(
        ("exempt_total", f"{sum(exempt.values())} of " f"{len(C.SOLVED) * len(C.INJECTED_DEFECTS)}")
    )
    rows.append(("exempt_by_defect", ", ".join(f"{k} {v}" for k, v in sorted(exempt.items()))))
    rows.append(("exempt_detected", f"{detected}"))

    dev = [abs(C.injected_delta(e, "one_element_scaled") - CD) / math.ulp(CD) for e in C.SOLVED]
    rows.append(("calibration_ulp_worst", f"{max(dev):.3f} ULP"))

    # THE EXTREMUM NAMES ITS TIE SET, NOT ITS WINNER (CH0). `detection_edge_at`
    # is a NAME, and the winner flips between two entries on two machines --
    # measured, 1.0041x apart. No tolerance on a value can say which name is
    # admissible, and dropping the name destroys the location of an extremum.
    # So every entry inside `FIGURE_ARGMIN_TIE_WINDOW` of the minimum is named,
    # sorted, and a flip inside the set changes no byte.
    edges = sorted((C._detection_edge(e), e["id"]) for e in C.SOLVED)
    edge = edges[0][0]
    tied = tie_set(edges, FIGURE_ARGMIN_TIE_WINDOW)
    rows.append(("detection_edge", f"{edge:.4e}"))
    rows.append(("detection_edge_at", ", ".join(tied)))
    rows.append(("detection_edge_tie_set", f"{len(tied)} within {FIGURE_ARGMIN_TIE_WINDOW}x"))
    rows.append(("counter_defect_over_edge", f"{CD / edge:.4g}x"))
    rows.append(("counter_headroom_room", f"{PATCH_TEST_COUNTER_HEADROOM / (CD / edge):.2f}x"))

    # THE BOUNDARY IS SOLVED HERE, NOT TYPED INTO THE PLAN (R207). The plan's
    # justification for `PATCH_TEST_COUNTER_HEADROOM` carried `2.36e-6 passes
    # and 2.38e-6 fails` in the present tense; two reviewer corpus rounds moved
    # the edge and `2.36e-6` now FAILS -- the sentence declared a defect size
    # admissible that the shipped test rejects, an 8% error in the unsafe
    # direction. It was typed at `d920a8d`, before this file existed.
    #
    # SOLVED means the SHIPPED assertion is run either side of the boundary,
    # with the counter-defect size moved and nothing else. The detection edge is
    # cached by `_smallest_detection_edge`, so this costs one comparison.
    boundary = PATCH_TEST_COUNTER_HEADROOM * edge
    outcomes = []
    original_cd = C.PATCH_TEST_EXACTNESS_COUNTER_DEFECT
    for probe in (boundary * (1.0 - 1.0e-3), boundary * (1.0 + 1.0e-3)):
        C.PATCH_TEST_EXACTNESS_COUNTER_DEFECT = probe
        try:
            C.test_the_counter_DEFECT_SIZE_cannot_be_raised(_Silent)
            outcomes.append("passes")
        except AssertionError:
            outcomes.append("fails")
        finally:
            C.PATCH_TEST_EXACTNESS_COUNTER_DEFECT = original_cd
    rows.append(
        (
            "counter_defect_boundary",
            f"{boundary * (1.0 - 1.0e-3):.4g} {outcomes[0]}, "
            f"{boundary * (1.0 + 1.0e-3):.4g} {outcomes[1]}",
        )
    )

    lo, hi, lo_at, hi_at, n, unbracketed, refused, lo_n = _boundary_margins(C, ceil, CD)
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
    rows.append(
        ("boundary_margin_unbracketed", f"{len(unbracketed)}: {', '.join(unbracketed) or 'none'}")
    )
    rows.append(("boundary_margin_refused", f"{len(refused)}: {', '.join(refused) or 'none'}"))
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
        k = int(round(abs(C.injected_delta(entry, "one_element_scaled") - CD) / math.ulp(CD)))
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
        from floatfea.tolerances import BEAM_ADMISSION_L_OVER_D, BOUNDARY_BISECTION_CONVERGENCE

        try:
            outer = 1.0 / member_l_over_d(1.0, C._entry_section(entry))
        except Exception as exc:
            refused.append(f"{entry['id']} ({type(exc).__name__})")
            continue
        lo, hi = ((1.0 + BOUNDARY_BISECTION_CONVERGENCE) * BEAM_ADMISSION_L_OVER_D * outer), 1.0e9

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
            resp = (
                max(C._oob_with_injected(base, st, "dropped_shear_parameter") for st in C.STATES)
                / ceil
            )
        except Exception as exc:
            refused.append(f"{entry['id']} ({type(exc).__name__})")
            continue
        out.append((float(resp / (eff / CD)), entry["id"]))

    if not out:
        raise RuntimeError(
            "no base bracketed the classification boundary; the range below "
            "would be empty and the figures would publish nothing"
        )
    out.sort()
    # The plateau: how many bases share the minimum to the digits published.
    lo_n = sum(1 for v, _ in out if f"{v:.6g}" == f"{out[0][0]:.6g}")
    return (
        out[0][0],
        out[-1][0],
        out[0][1],
        out[-1][1],
        len(out),
        sorted(unbracketed),
        sorted(refused),
        lo_n,
    )


def tie_set(edges: list[tuple[float, str]], window: float) -> list[str]:
    """Every entry within `window` of the extremum, sorted by name.

    A free function so the window can be run against injected values --
    including `FIGURE_ARGMIN_TIE_WINDOW_COUNTER_DEFECT`, the position of the
    first entry the window has to exclude -- instead of only against whatever
    the corpus happens to contain today.
    """
    smallest = min(v for v, _ in edges)
    return sorted(name for value, name in edges if value <= smallest * window)


# CH5: THE STAMP, AND WHAT COUNTS AS THE CANONICAL MACHINE.
#
# Q8: "a golden or figure whose stamp is not CI's pinned environment fails the
# build, so no canonical file can be produced on a laptop again." The stamp
# names the BLAS core type beside the three libraries because the kernel is
# what the split turned out to be -- a stamp naming the other three would have
# been identical across the two files the vendor split produced.
#
# `OPENBLAS_CORETYPE` is read from the environment rather than from OpenBLAS,
# and that is the honest reading: it is the variable the workflow sets and the
# one whose deletion `tests/test_ci_canonical_environment.py` reddens. What
# kernel OpenBLAS then selected is measured on CI by the ten legs agreeing.
CANONICAL_PYTHON = "3.13"
CANONICAL_CORETYPE = "Haswell"

# Q8's third local class. A figure whose value IS a round-off magnitude, with
# the decision the gate makes about it:
#
#   below <ceiling>   a clean figure: it must stay under its ceiling
#   above <ceiling>   a counter: it must stay over the ceiling it defends
#   derived           no decision of its own; `counter_headroom_room` carries
#                     the decision for the detection-edge family
#   words             the decision is the pass/fail words, not the numbers
#
# Every other row in the file must match the canonical render EXACTLY, on any
# machine. Nine rows of forty-seven move between two machines and all nine are
# named here or are the tie set above.
FLOOR_CLASS: dict[str, tuple[str, str | None]] = {
    "rigid_body_mode_ratio": ("below", "RIGID_BODY_MODE_RATIO"),
    "rigid_body_subspace_loss": ("below", "RIGID_BODY_SUBSPACE_LOSS"),
    "rigid_body_counter_ratio": ("above", "RIGID_BODY_MODE_RATIO"),
    "rigid_body_counter_loss": ("above", "RIGID_BODY_SUBSPACE_LOSS"),
    "clean_worst_ratio": ("below", None),
    "counter_headroom_room": ("above", None),
    "detection_edge": ("derived", None),
    "counter_defect_over_edge": ("derived", None),
    "counter_defect_boundary": ("words", None),
}

_ROW = re.compile(r"^\| `([a-z0-9_]+)` \| (.+?) \|$", re.MULTILINE)


def _stamp_rows() -> list[tuple[str, str]]:
    import numpy
    import scipy

    return [
        ("stamp_platform", sys.platform),
        ("stamp_python", platform.python_version()),
        ("stamp_numpy", numpy.__version__),
        ("stamp_scipy", scipy.__version__),
        ("stamp_openblas_coretype", os.environ.get("OPENBLAS_CORETYPE", "unset")),
    ]


def is_canonical() -> bool:
    """Is THIS the machine Q8 makes canonical?

    Not "is the CI environment variable set": a fork of the workflow, a local
    container, or a future runner all count if they are the pinned
    environment, and a GitHub job that lost the kernel pin does not.
    """
    return (
        sys.platform.startswith("linux")
        and platform.python_version().startswith(CANONICAL_PYTHON + ".")
        and os.environ.get("OPENBLAS_CORETYPE") == CANONICAL_CORETYPE
    )


def _values(text: str) -> dict[str, str]:
    return dict(_ROW.findall(text))


def _number(value: str) -> float | None:
    """The leading number of a figure cell, or None if it has none."""
    m = re.match(r"\s*(-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)", value)
    return float(m.group(1)) if m else None


def _ceiling(name: str) -> float:
    import floatfea.tolerances as T

    kind, ceil_name = FLOOR_CLASS[name]
    if ceil_name is None:
        # `clean_worst_ratio` and `counter_headroom_room` are already
        # normalised by the quantity they are compared with, so their ceiling
        # is 1 by construction and there is no constant to name.
        return 1.0
    return float(getattr(T, ceil_name))


def compare(committed: str, local: str) -> tuple[int, list[str]]:
    """The non-canonical machine's three assertions (Q8's third class, CH0).

    Returns `(exit code, lines to print)`. Split out from `main` so that
    `tests/test_figure_local_check.py` can run it against injected pairs --
    including the two counters -- rather than against whatever this machine
    happens to render.
    """
    from floatfea.tolerances import FIGURE_FLOOR_CLASS_SPREAD

    out: list[str] = []
    bad = 0
    have, mine = _values(committed), _values(local)

    missing = sorted(set(mine) - set(have))
    extra = sorted(set(have) - set(mine))
    if missing or extra:
        out.append(f"regen_figures: rows only in a fresh render: {missing or 'none'}")
        out.append(f"regen_figures: rows only in the committed file: {extra or 'none'}")
        return 1, out

    stamp = {k: v for k, v in have.items() if k.startswith("stamp_")}
    if not stamp:
        out.append(
            "regen_figures: the committed file carries NO environment stamp. "
            "Q8 requires one inside every canonical file; without it a laptop "
            "render and a canonical one are indistinguishable."
        )
        bad = 1
    else:
        if stamp.get("stamp_openblas_coretype") != CANONICAL_CORETYPE:
            out.append(
                f"regen_figures: the committed stamp says core type "
                f"{stamp.get('stamp_openblas_coretype')!r}, and the canonical "
                f"environment is {CANONICAL_CORETYPE!r}. This file was not "
                "produced on the canonical machine."
            )
            bad = 1
        if not str(stamp.get("stamp_python", "")).startswith(CANONICAL_PYTHON + "."):
            out.append(
                f"regen_figures: the committed stamp says Python "
                f"{stamp.get('stamp_python')!r}, and the plan pins "
                f"{CANONICAL_PYTHON}."
            )
            bad = 1

    exact = [
        n
        for n in sorted(mine)
        if n not in FLOOR_CLASS and not n.startswith("stamp_") and mine[n] != have[n]
    ]
    for n in exact:
        out.append(f"regen_figures: {n} is {mine[n]!r} here and {have[n]!r} in the file.")
        out.append(
            "    Not a floor-class figure: Q8 requires these to agree EXACTLY "
            "on every machine, so this is staleness rather than platform."
        )
        bad = 1

    out.append("")
    out.append("floor class -- the decision, and the spread beside it:")
    out.append("  figure                          committed        here             spread")
    for n in sorted(FLOOR_CLASS):
        if n not in have or n not in mine:
            # A floor-class name the file does not carry is not a silent pass:
            # the row-set comparison above has already returned for any real
            # difference, so reaching here means the caller is checking a
            # SUBSET on purpose -- which is what the injected pairs in
            # `tests/test_figure_local_check.py` are.
            continue
        kind, _ = FLOOR_CLASS[n]
        a, b = _number(have[n]), _number(mine[n])
        if kind == "words":
            words_a = re.sub(r"[-+0-9.eE]+", "", have[n]).strip()
            words_b = re.sub(r"[-+0-9.eE]+", "", mine[n]).strip()
            mark = "" if words_a == words_b else "  <- THE DECISION MOVED"
            bad |= words_a != words_b
            out.append(f"  {n:<30}  {have[n]:<16} {mine[n]:<16} {mark}")
            continue
        if a is None or b is None or a <= 0 or b <= 0:
            out.append(f"  {n:<30}  {have[n]:<16} {mine[n]:<16} (not a positive number)")
            bad = 1
            continue
        spread = max(a, b) / min(a, b)
        note = ""
        if spread > FIGURE_FLOOR_CLASS_SPREAD:
            note = f"  <- OVER {FIGURE_FLOOR_CLASS_SPREAD}x"
            bad = 1
        out.append(f"  {n:<30}  {have[n]:<16} {mine[n]:<16} {spread:.4f}x{note}")

        if kind == "derived":
            continue
        ceil = _ceiling(n)
        margin = ceil / b if kind == "below" else b / ceil
        if margin < 1.0:
            out.append(
                f"    THE DECISION MOVED: {n} is {b:.6g} and must be "
                f"{'below' if kind == 'below' else 'above'} {ceil:.6g}."
            )
            bad = 1
        elif margin < FIGURE_FLOOR_CLASS_SPREAD:
            out.append(
                f"    margin {margin:.4g}x is under the declared spread "
                f"{FIGURE_FLOOR_CLASS_SPREAD}x, so the platform alone could "
                "carry this decision across its ceiling."
            )
            bad = 1
    return (1 if bad else 0), out


def render() -> str:
    # NO `Generated at <sha>` LINE (R179). It recorded the commit the file was
    # written at, which is never the commit it is committed in -- so it was false
    # the moment it landed, and once `--check` compared the whole file it failed
    # on the sha rather than on a figure. Content equality answers the staleness
    # question by itself; the sha added a claim nothing could keep true.
    lines = [
        "# F2 figures — GENERATED, do not edit",
        "",
        "Produced by `scripts/regen_figures.py` from the shipped runner, on the",
        "machine named in the `stamp_*` rows. Q8 makes CI canonical for this",
        "file; a stamp that is not CI's pinned environment fails the build.",
        "`docs/milestones/F2.md` references these by name as `{{fig:NAME}}`, and",
        "`tests/test_plan_figures.py` fails if a referenced name is missing or if",
        "this file is not what a fresh run produces.",
        "",
        "| name | value |",
        "|---|---|",
    ]
    lines += [f"| `{n}` | {v} |" for n, v in _stamp_rows()]
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
        if is_canonical():
            # THE CANONICAL MACHINE COMPARES BYTES, and the stamp is part of
            # them: a patch-version bump on the runner reddens here, which is
            # what a version stamp is FOR. Regenerate and commit.
            if current != text:
                print(
                    "regen_figures: F2_figures.md is not what this script "
                    "produces on the canonical machine",
                    file=sys.stderr,
                )
                return 1
            print("regen_figures: up to date (canonical machine, byte-identical)")
            return 0
        # OFF THE CANONICAL MACHINE (Q8's third class, CH0). Every row that is
        # not floor-class must still agree exactly, so staleness is caught here
        # as it always was; the floor-class rows are checked at the DECISION and
        # their spread is printed either way.
        code, lines = compare(current, text)
        for line in lines:
            print(line, file=sys.stderr if code else sys.stdout)
        if code:
            print(
                "regen_figures: this is not the canonical machine, and the "
                "differences above are not the ones Q8's third class allows",
                file=sys.stderr,
            )
            return 1
        print(
            "regen_figures: up to date (non-canonical machine: every exact row "
            "agrees, every floor-class decision holds)"
        )
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"regen_figures: wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
