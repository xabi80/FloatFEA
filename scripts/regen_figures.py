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
    # THE FOUR RETIRED ROWS ARE `derived` (R445, by R439's rule). They were
    # marked `below`/`above` against `RIGID_BODY_MODE_RATIO` and
    # `RIGID_BODY_SUBSPACE_LOSS`, both retired at Q7/CS2, so `compare()` was
    # computing a margin against constants nothing asserts -- R428's species
    # at four sites its condition did not name. `derived` keeps the spread
    # check, which is what a diagnostic still owes a reader, and drops the
    # margin, which decides nothing.
    rows: list[tuple[str, str]] = []

    # G2.1 / V1.1 (D2 step 5). Both halves of the rigid-body gate, generated
    # from the shipped frame so the plan and `tolerances.py` cite them by name
    # instead of typing them -- R194's remedy, applied from this gate's first
    # commit rather than five rounds into it.
    import test_rigid_body_modes as RB

    from floatfea.tolerances import RIGID_MODE_FLOOR as RETIRED_FLOOR

    model, els = RB._frame()
    k_rb = RB.assemble_dense(model, els)
    rows.append(
        (
            _floor("rigid_body_mode_ratio", "derived"),
            f"{RB.mode_ratio(k_rb):.4e}",
        )
    )
    rows.append(
        (
            _floor("rigid_body_subspace_loss", "derived"),
            f"{RB.subspace_loss(k_rb, model):.4e}",
        )
    )
    # Q7's two quantities, which are what G2.1 is asserted with now. The ratio
    # and the RETIRED subspace loss above are kept as diagnostics and are
    # still generated, because the report cites the contrast between the two
    # forms and a withdrawn figure that nothing regenerates is how a contrast
    # goes stale.
    rows.append(
        (
            _floor("rigid_mode_residual", "below", "RIGID_MODE_EXACTNESS"),
            f"{RB.residual_exactness(k_rb, model):.4e}",
        )
    )
    rows.append(
        (
            _floor("rigid_mode_seventh_over_epsilon", "above", "RIGID_MODE_BOUND"),
            f"{RB.seventh_over_epsilon(k_rb):.4e}",
        )
    )
    # THE RETIRED PARAMETRISATION IS STILL GENERATED, for the same reason the
    # retired ratio and loss above are: revision 21 of the step report cites
    # these two by name, and a reference that stops resolving is how a record
    # turns into a dangling pointer. They are `log10(lambda_7 / tau)` with
    # `tau = RIGID_MODE_FLOOR * ||K_hat|| * eps`, DERIVED from the live ratio
    # rather than computed a second way, so the two cannot drift apart.
    #
    # AND THEY ARE WHY `log=True` IS NOT A DEAD FLAG (CU1, R418). These are
    # the repository's log-valued rows; the flag that says so is declared
    # here, at the line that produces them, and a rename cannot move them out
    # of the rule any more.
    rows.append(
        (
            # `derived`, NOT `above RIGID_MODE_GAP` (R428). The ceiling
            # this row named was retired in the same round that left the mark
            # on it, so `compare()` was computing a margin against a
            # RETIRED constant. The margin was `10**11.08` and would never have
            # fallen under the spread -- the form is what was wrong, and R399
            # asked for exactly this a round earlier.
            _floor("rigid_mode_seventh_orders", "derived", log=True),
            f"{math.log10(RB.seventh_over_epsilon(k_rb) / RETIRED_FLOOR):.3f}",
        )
    )

    # CV1: THE OTHER LOWER-LIMIT CANDIDATE, RENDERED HERE SO THE TWO COME
    # FROM ONE MACHINE. `RIGID_MODE_BOUND`'s window has two candidates below
    # it -- the largest of the six numerically-zero eigenvalues, and the
    # highest `lambda_7` a GENUINE seventh zero mode reaches. Both are
    # floor-class rows against the bound, so both clearances are recomputed
    # wherever `--check` runs and the gate is held to whichever is tighter
    # there.
    #
    # THE CELL IS THE CORPUS'S OWN UNIT AND SPAN SETS, at `subdiv=1`, one
    # torsional release, nothing else moved (CW2, R438). It was 7 units x 5
    # spans under a sentence claiming "every unit system and span the corpus
    # uses" -- 6 of the 19 unit values and 5 of the 31 span values, with one
    # unit the corpus does not use at all -- and over the set the sentence
    # named the mechanism reaches higher than the cell reported. The cell is
    # now that set: every distinct `unit` string crossed with every distinct
    # `stretch` string, which is 858 configurations and costs under a second.
    #
    # `subdiv` IS PINNED TO 1 AND THAT IS NOT AN OVERSIGHT. Above it,
    # `_assemble_with_torsional_release(..., released=6)` releases a member
    # that is no longer the axis-parallel tip member, so the injection stops
    # being a mechanism and leaves SIX under the bound rather than seven --
    # there is nothing to measure. Only the configurations that really do
    # carry a seventh zero mode are counted.
    import test_rigid_body_corpus as RBC

    mechanism = 0.0
    mechanisms = 0
    units = sorted({e["unit"] for e in RBC.ENTRIES}, key=float)
    spans = sorted({e["stretch"] for e in RBC.ENTRIES}, key=float)
    for unit in units:
        for stretch in spans:
            entry = dict(RBC.ENTRIES[0])
            entry.update(unit=unit, stretch=stretch, subdiv="1")
            m_m, els_m = RBC._build(entry)
            k_m = RB._assemble_with_torsional_release(m_m, els_m, released=6)
            if RB.zero_modes_under_the_bound(k_m) != RB.RIGID + 1:
                continue
            mechanisms += 1
            mechanism = max(mechanism, RB.seventh_over_epsilon(k_m))
    rows.append(
        (
            _floor("rigid_mode_mechanism_ceiling", "below", "RIGID_MODE_BOUND"),
            f"{mechanism:.4f}",
        )
    )
    rows.append(("rigid_mode_mechanism_cell", f"{len(units)} units x {len(spans)} spans, subdiv 1"))
    rows.append(
        (
            # `words`, BY R439'S OWN RULE, and this row is what caught it: how
            # many of the 858 configurations really carry a seventh zero mode
            # is decided by a spectrum, so it moves -- `350` on the
            # implementer's machine against `347` on the canonical runner --
            # both values stood here and are kept as the record. It
            # shipped plain for the length of one render and the guard refused
            # it, which is the rule written one commit earlier working on the
            # row written in the same commit.
            #
            # The CELL above is exact and stays plain: it counts distinct
            # strings in the corpus file and no arithmetic touches it.
            _floor("rigid_mode_mechanism_count", "words"),
            f"{mechanisms}",
        )
    )

    from floatfea.tolerances import FIGURE_FLOOR_CLASS_SPREAD as SPREAD

    worst_residual, smallest_decided = 0.0, float("inf")
    largest_refused, rigid_max = 0.0, 0.0
    refused = 0
    decided_clear = refused_clear = 0
    in_window: list[str] = []
    ratio_over = loss_over = 0
    for entry in RBC.ENTRIES:
        m_c, els_c = RBC._build(entry)
        k_c = RB.assemble_dense(m_c, els_c)
        worst_residual = max(worst_residual, RB.residual_exactness(k_c, m_c))
        over_c = RB.seventh_over_epsilon(k_c)
        if over_c >= RB.RIGID_MODE_BOUND:
            smallest_decided = min(smallest_decided, over_c)
        else:
            largest_refused = max(largest_refused, over_c)
            refused += 1
        # CV2: THE THREE-WAY SPLIT. A frame is decided ON EVERY MACHINE only
        # if it clears the bound by more than the declared platform spread,
        # and refused on every machine only if it misses by more than that.
        # What is between them is the window, and its size is the honest
        # statement about how portable the partition is.
        if over_c >= RB.RIGID_MODE_BOUND * SPREAD:
            decided_clear += 1
        elif over_c <= RB.RIGID_MODE_BOUND / SPREAD:
            refused_clear += 1
        else:
            in_window.append(entry["id"])
        rigid_max = max(rigid_max, RB.largest_rigid_eigenvalue(k_c))
        if RB.mode_ratio(k_c) > RB.RIGID_BODY_MODE_RATIO:
            ratio_over += 1
        if RB.subspace_loss(k_c, m_c) > RB.RIGID_BODY_SUBSPACE_LOSS:
            loss_over += 1
    rows.append(
        (
            _floor("rigid_mode_residual_worst_over_corpus", "below", "RIGID_MODE_EXACTNESS"),
            f"{worst_residual:.4e}",
        )
    )
    rows.append(
        (
            # NOT FLOOR-CLASS, deliberately. This figure IS the domain
            # boundary: the smallest value the gate accepts sits just above
            # the bound by construction, so asking it to clear the bound by
            # the platform spread would be asking the boundary to be far from
            # itself. What it reports is where the domain ends -- and how
            # close to the bound it is, which is the upper side of
            # `RIGID_MODE_BOUND`'s own window.
            #
            # `derived` AND NOT PLAIN: it is an eigenvalue and it moves
            # between machines -- `2.0494e+02` here against `2.0502e+02`
            # on the canonical runner -- so a plain row would call that
            # staleness. `derived` gets the spread without a margin, which
            # is exactly what a row that decides nothing needs.
            _floor("rigid_mode_smallest_decided", "derived"),
            f"{smallest_decided:.4e}",
        )
    )
    rows.append(
        (
            # The retired spelling of the row above, kept resolvable for the
            # same reason and `derived` for the same reason too -- and it
            # is log-valued, so it says so.
            _floor(
                "rigid_mode_seventh_orders_smallest_decided",
                "derived",
                log=True,
            ),
            f"{math.log10(smallest_decided / RETIRED_FLOOR):.3f}",
        )
    )
    rows.append(
        (
            # THE OTHER SIDE OF THE SAME BOUNDARY, published for the same
            # reason: together these two say how wide the corpus's own gap
            # around the bound is, and it is narrower than the declared
            # platform spread. `derived` for the reason above.
            _floor("rigid_mode_largest_refused", "derived"),
            f"{largest_refused:.4e}",
        )
    )
    rows.append(
        (
            # THE COURANT-FISCHER COMPOSITION, in one number: the largest of
            # the six numerically-zero eigenvalues over the corpus, in units
            # of `||K_hat||*eps`. It is the lower side of the bound's window
            # -- the bound has to exceed it or the six are not all under the
            # bound -- and it is what the retired floor's `6.84x` bracket
            # measured against a rule nothing applied.
            _floor("rigid_mode_largest_rigid_eigenvalue", "below", "RIGID_MODE_BOUND"),
            f"{rigid_max:.4f}",
        )
    )
    rows.append(("rigid_mode_corpus_frames", f"{len(RBC.ENTRIES)}"))
    rows.append(
        (
            # `words`, NOT `derived` (R448). `derived` reads only the
            # LEADING number of a cell, so off the canonical machine the
            # denominator of `N of M` was compared by nothing. The `words`
            # class compares the word sequence exactly AND every number
            # beside it for spread, which is what `counter_defect_boundary`
            # uses and for this reason.
            _floor("rigid_mode_corpus_refused", "words"),
            f"{refused} of {len(RBC.ENTRIES)}",
        )
    )
    # THE COUNT WITH ITS WINDOW (CV2). The first two are the sets the
    # determinism legs can speak for; the third is the set they cannot, and
    # naming its members is the only honest form the boundary has.
    rows.append(("rigid_mode_corpus_decided_clear", f"{decided_clear}"))
    rows.append(("rigid_mode_corpus_refused_clear", f"{refused_clear}"))
    rows.append(("rigid_mode_corpus_in_the_window", f"{len(in_window)}"))
    rows.append(("rigid_mode_corpus_window_members", " ".join(sorted(in_window)) or "none"))
    rows.append(
        (
            # SAME CLASS AS THE ROW ABOVE, AND THE RULE IS NOW WRITTEN ONCE
            # (R439). This was an exact row while its sibling was floor-class
            # and a third count was withheld -- three policies for a count in
            # twenty lines, with the sentence stating the rule refuted by the
            # row sixteen lines above it.
            #
            # THE RULE THIS FILE FOLLOWS, stated: a count is published when
            # something cites it, and its CLASS is decided by whether it can
            # move between machines. A count derived from eigenvalues can:
            # both of these compare a per-frame quantity with a ceiling and a
            # frame sitting near that ceiling changes sides. So both are
            # `words` -- the word sequence exact, both numbers compared for
            # spread. A count that cannot move at all, like the number of
            # frames in the corpus file, stays a plain row.
            #
            # "a count is not a measurement against a tolerance" stood below
            # this as the ground for withholding the third one. It is
            # withdrawn: these two ARE counts of measurements against
            # tolerances, and the class handles them.
            _floor("retired_ratio_over_ceiling_on_corpus", "words"),
            f"{ratio_over} of {len(RBC.ENTRIES)}",
        )
    )
    rows.append(
        (
            # AND THE LOSS'S COUNT IS PUBLISHED (R454), by the same rule. It
            # was withheld on three grounds in three rounds, each refuted:
            # "an exact row that disagrees between machines is staleness" --
            # answered by the class; "a count is not a measurement against a
            # tolerance" -- refuted by its two siblings; and "nothing cites
            # it" -- refuted by four sentences in four files, each of the
            # form "it breached at MORE of the reviewer's clean frames than
            # the ratio did". That comparison is between this count and the
            # published one, so withholding it made four true sentences
            # uncheckable by any reader.
            _floor("retired_loss_over_ceiling_on_corpus", "words"),
            f"{loss_over} of {len(RBC.ENTRIES)}",
        )
    )

    rows.append(
        (
            _floor("rigid_mode_counter_seventh", "below", "RIGID_MODE_BOUND"),
            f"{RB.counter_response('bound'):.4e}",
        )
    )
    rows.append(
        (
            _floor("rigid_body_counter_ratio", "derived"),
            f"{RB.counter_response('ratio'):.4e}",
        )
    )
    rows.append(
        (
            _floor("rigid_body_counter_loss", "derived"),
            f"{RB.counter_response('loss'):.4e}",
        )
    )

    rows.append(("corpus_entries", f"{len(C.ENTRIES)}"))
    rows.append(("corpus_solved", f"{len(C.SOLVED)}"))

    worst = max((max(C._oob_state(e, st) for st in C.STATES) / ceil, e["id"]) for e in C.SOLVED)
    rows.append((_floor("clean_worst_ratio", "below"), f"{worst[0]:.4f}x"))
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
    rows.append((_floor("detection_edge", "derived"), f"{edge:.4e}"))
    rows.append(("detection_edge_at", ", ".join(tied)))
    rows.append(("detection_edge_tie_set", f"{len(tied)} within {FIGURE_ARGMIN_TIE_WINDOW}x"))
    rows.append((_floor("counter_defect_over_edge", "derived"), f"{CD / edge:.4g}x"))
    rows.append(
        (
            _floor("counter_headroom_room", "above"),
            f"{PATCH_TEST_COUNTER_HEADROOM / (CD / edge):.2f}x",
        )
    )

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
            _floor("counter_defect_boundary", "words"),
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

    # DB1, APPLIED AT THE ONE PLACE ROWS BECOME THE PUBLISHED FILE. The
    # computations above still run: they are what the ladder's own tests
    # exercise, and several feed each other. What changes is that a
    # corpus-derived VALUE is not published, so the file no longer moves when
    # the reviewer adds entries. A reader who wants the number runs the named
    # test, which is the thing that actually asserts it.
    rows = [(n, _withdrawal(n) if _is_withdrawn(n) else v) for n, v in rows]
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
                # The 1.0 below is UNITY, the reference the ratio hi/lo is
                # compared to; the bound is the declared name beside it.
                # Marked because CQ3 flags a literal beside a declared
                # name, and for `+` the identity is 0, not 1.
                if (
                    hi / lo < 1.0 + BOUNDARY_BISECTION_CONVERGENCE
                ):  # not-a-tolerance: 1.0 is unity, the ratio's reference
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

# Q8's third local class, DERIVED FROM THE GENERATOR RATHER THAN GRANTED BY A
# LIST (CI3, R312). A figure is floor-class when the code that produces it says
# so, at the line that produces it -- `_floor(name, "below", "CEILING")` beside
# the `rows.append` -- because the licence is a property of HOW the number is
# computed and not of whether it happened to move between two machines. The
# hand-written map this replaces had nine members and the round's nine movers
# were a different nine, and nothing said so.
#
#   below <ceiling>   a clean figure: it must stay under its ceiling
#   above <ceiling>   a counter: it must stay over the ceiling it defends
#   derived           no decision of its own; `counter_headroom_room` carries
#                     the decision for the detection-edge family
#   words             the decision is the pass/fail words; the numbers beside
#                     them are still compared for spread
#
# AND `log=True` SAYS THE VALUE IS log10 OF A RATIO (CU1, R418). It is a
# property of how the number is computed, so it is declared where the number
# is produced, exactly like the class beside it. It was inferred from the
# suffix `_orders` instead, and the round that introduced that rule renamed a
# log-valued row to end in `_decided`: the row kept its meaning, lost the
# suffix, and was silently compared by the wrong rule. A rename cannot move a
# figure between rules now. The rows that carry it are the RETIRED
# parametrisation's two, kept generated because revision 21 of the step report
# cites them by name; the quantity the gate decides on is a plain ratio under
# CU0 and declares nothing. `No shipped row declares it at this commit` stood
# here, in the same commit that added both declarations 409 lines above and a
# test asserting exactly that set (R424).
#
# claim: four lines in this file contain `log=True` -- the two `_floor(...)`
#        calls that declare it, both of them the retired parametrisation, and
#        two comment lines naming the flag: the one above this block and the
#        one beside the retired rows. `out: 6` stood here, which was the four
#        plus this triple's own `claim:` and `cmd:` lines, under an
#        enumeration that named two hits in the class vocabulary where a grep
#        over it finds none (R450).
# cmd:   count("scripts/regen_figures.py", "log=True")
# ctl:   log_declaration
# out:   4
#
# Every row NOT marked here must match the canonical render exactly, on any
# machine, so staleness is caught off the canonical runner as it always was.
_MARKS: dict[str, tuple[str, str | None, bool]] = {}


# ---------------------------------------------------------------- DB1
# A COUNT OF CORPUS ENTRIES IS NOT A PUBLISHED FIGURE.
#
# The loop this breaks, which ran four times: the reviewer adds entries to a
# corpus it owns; every row below that is a count, a partition or a
# worst-over-corpus value moves; `test_the_generated_figures_are_not_stale`
# goes red; the implementer's repair is necessarily a commit after a closed
# step's report, which reddens the whole-suite-line guard. Two guards telling
# the truth, a red tree, and nothing wrong with the code.
#
# DB1's ruling: the TESTS that assert the ceiling over every entry are the
# claim. A count of entries is not, and it never was -- it is a fact about
# how much measuring has been done, which changes by design every time the
# reviewer does more of it.
#
# The name stays resolvable on purpose. `test_every_figure_reference_anywhere
# _resolves` checks every `{{fig:...}}` in the repository, and roughly ninety
# of them are in shipped step reports and in this milestone's plan. Deleting
# the rows would dangle all of them, including inside history that is
# supposed to stay as it was written; what a reader now gets in place of a
# stale count is the name of the test that carries the claim.
_WITHDRAWN = {
    # the rigid-body frame corpus -- G2.1 / V1.1
    "rigid_mode_corpus_frames": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_corpus_refused": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_corpus_decided_clear": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_corpus_refused_clear": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_corpus_in_the_window": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_corpus_window_members": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_residual_worst_over_corpus": ("tests/verification/rung1/test_rigid_body_corpus.py"),
    "rigid_mode_smallest_decided": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_largest_refused": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_largest_rigid_eigenvalue": ("tests/verification/rung1/test_rigid_body_corpus.py"),
    "rigid_mode_mechanism_cell": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_mechanism_count": "tests/verification/rung1/test_rigid_body_corpus.py",
    "rigid_mode_mechanism_ceiling": "tests/verification/rung1/test_rigid_body_corpus.py",
    "retired_ratio_over_ceiling_on_corpus": ("tests/verification/rung1/test_rigid_body_corpus.py"),
    "retired_loss_over_ceiling_on_corpus": ("tests/verification/rung1/test_rigid_body_corpus.py"),
    # the model-configuration corpus -- G2.2 / V1.2
    "corpus_entries": "tests/verification/rung1/test_corpus_configurations.py",
    "corpus_solved": "tests/verification/rung1/test_corpus_configurations.py",
    "clean_worst_ratio": "tests/verification/rung1/test_corpus_configurations.py",
    "clean_worst_entry": "tests/verification/rung1/test_corpus_configurations.py",
    "exempt_total": "tests/verification/rung1/test_corpus_configurations.py",
    "exempt_by_defect": "tests/verification/rung1/test_corpus_configurations.py",
    "exempt_detected": "tests/verification/rung1/test_corpus_configurations.py",
    "calibration_ulp_worst": "tests/verification/rung1/test_corpus_configurations.py",
    "detection_edge_at": "tests/verification/rung1/test_corpus_configurations.py",
    "detection_edge_worst": "tests/verification/rung1/test_corpus_configurations.py",
    "detection_edge": "tests/verification/rung1/test_corpus_configurations.py",
    "detection_edge_tie_set": "tests/verification/rung1/test_corpus_configurations.py",
    "counter_defect_over_edge": "tests/verification/rung1/test_corpus_configurations.py",
    "counter_defect_boundary": "tests/verification/rung1/test_corpus_configurations.py",
    "counter_headroom_room": "tests/verification/rung1/test_corpus_configurations.py",
    "calibration_ulp_histogram": "tests/verification/rung1/test_corpus_configurations.py",
    "rigid_mode_seventh_orders_smallest_decided": (
        "tests/verification/rung1/test_rigid_body_corpus.py"
    ),
}


_WITHDRAWN_PREFIXES = ("margin_", "below_ceiling_", "boundary_margin_")
"""Per-defect margins and counts, one pair per injected defect, every one of
them a minimum or a count over `C.SOLVED`."""


def _is_withdrawn(name: str) -> bool:
    return name in _WITHDRAWN or name.startswith(_WITHDRAWN_PREFIXES)


def _withdrawal(name: str) -> str:
    claim = _WITHDRAWN.get(name)
    if claim is None:
        claim = (
            "tests/verification/rung1/test_corpus_configurations.py"
            if name.startswith(_WITHDRAWN_PREFIXES)
            else "unknown"
        )
    return f"*withdrawn (DB1) -- the claim is `{claim}`*"


def _floor(name: str, kind: str, ceiling: str | None = None, log: bool = False) -> str:
    """Mark `name` floor-class and return it, so the call sites read as one."""
    assert kind in ("below", "above", "derived", "words"), kind
    _MARKS[name] = (kind, ceiling, log)
    return name


def floor_class() -> dict[str, tuple[str, str | None, bool]]:
    """The marks, from a render if one has not happened yet.

    A render is what executes the marks, so this triggers one when the caller
    has not. `--check` renders first and pays nothing.
    """
    if not _MARKS:
        _figures()
    # A WITHDRAWN ROW IS A `words` ROW (DB1). It was marked `below` or
    # `above` against a constant, and `compare()` then reads its value as a
    # number to take a margin and a spread -- which a pointer is not. The mark
    # is overridden here rather than at the ~25 call sites, so the reason sits
    # in one place and the call sites keep saying what the figure WAS.
    return {n: (("words", None, False) if _is_withdrawn(n) else m) for n, m in _MARKS.items()}


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

    kind, ceil_name, _log = floor_class()[name]
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
        if n not in floor_class() and not n.startswith("stamp_") and mine[n] != have[n]
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
    marks = floor_class()
    for n in sorted(marks):
        if n not in have or n not in mine:
            # A floor-class name the file does not carry is not a silent pass:
            # the row-set comparison above has already returned for any real
            # difference, so reaching here means the caller is checking a
            # SUBSET on purpose -- which is what the injected pairs in
            # `tests/test_figure_local_check.py` are.
            continue
        kind, _ceil, _log = marks[n]
        a, b = _number(have[n]), _number(mine[n])
        if kind == "words":
            # WHOLE WORDS (R313). Substituting over the character class
            # `[-+0-9.eE]` deleted the `e` out of `passes`, so `passes` and
            # `passees` compared equal. It was latent -- `passes` against
            # `fails` survives it -- and it was the only comparator in this
            # file that decides on words.
            words_a = re.findall(r"[A-Za-z]+", have[n])
            words_b = re.findall(r"[A-Za-z]+", mine[n])
            moved = words_a != words_b
            bad |= moved
            # AND THE NUMBERS BESIDE THEM GET THEIR SPREAD (R311c). The plan
            # says the spread is printed beside the value either way, and this
            # branch returned before any number was read: a row moving nine
            # orders of magnitude printed nothing and exited 0.
            nums_a = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", have[n])]
            nums_b = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", mine[n])]
            spreads = [
                max(a, b) / min(a, b)
                for a, b in zip(nums_a, nums_b, strict=False)
                if a > 0 and b > 0
            ]
            worst = max(spreads, default=1.0)
            note = "  <- THE DECISION MOVED" if moved else ""
            if worst > FIGURE_FLOOR_CLASS_SPREAD:
                note += f"  <- OVER {FIGURE_FLOOR_CLASS_SPREAD}x"
                bad = 1
            if len(nums_a) != len(nums_b):
                note += "  <- a different number of values"
                bad = 1
            out.append(f"  {n:<30}  {have[n]:<32} {mine[n]:<32} {worst:.4f}x{note}")
            continue
        if a is None or b is None or a <= 0 or b <= 0:
            out.append(f"  {n:<30}  {have[n]:<16} {mine[n]:<16} (not a positive number)")
            bad = 1
            continue
        # A LOG-VALUED FIGURE IS COMPARED AS A RATIO (CT3, R404), and it
        # says so itself (CU1, R418). `FIGURE_FLOOR_CLASS_SPREAD` is declared
        # on ratios -- its own entry says the value "is invariant under the
        # figure's units", and `log10` is not a unit change -- so dividing two
        # logarithms compared a quantity the spread was never about, and it
        # refused a floor with more room than the one it forced. The flag
        # comes from the row's declared class, because the first version read
        # the suffix `_orders` off the NAME and the same commit renamed a
        # log-valued row past it.
        as_ratio = floor_class().get(n, ("", None, False))[2]
        spread = 10 ** abs(a - b) if as_ratio else max(a, b) / min(a, b)
        note = ""
        if spread > FIGURE_FLOOR_CLASS_SPREAD:
            note = f"  <- OVER {FIGURE_FLOOR_CLASS_SPREAD}x"
            bad = 1
        out.append(f"  {n:<30}  {have[n]:<16} {mine[n]:<16} {spread:.4f}x{note}")

        if kind == "derived":
            continue
        ceil = _ceiling(n)
        if as_ratio:
            margin = 10 ** (ceil - b) if kind == "below" else 10 ** (b - ceil)
        else:
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
