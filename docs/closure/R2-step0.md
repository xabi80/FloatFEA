# R2 step 0 — closure

**Closed by verdict 65 (PASS) at `0fb8c93`, with one blocking item carried.** Step 0 was
GI3's measure-only step: five measurements, one permitted code change, and GI6's
instruction to report and stop. It consumed all three ES0 revisions and five reviewer
rounds (three interim checks, which count against none, plus three reviewed revisions).

## What was built

GI3's five items, all answered in `docs/reports/R2/step-0.md`:

* **(a)** the inertial/joint-reaction split, and the loop gain it implies. At the body the
  split is 1:1 by construction; at the governing member the stress is 59.2 % static /
  40.8 % dynamic. Loop gain `g = k·m_steel/m_body` is 0.53–0.77, so the loop converges
  **monotonically** and 11–14 iterations are needed to reach D3's 0.5 % band.
* **(b)** one D4 iteration is **25 min 56 s** with threads pinned. D3's cap of 8 is ≈ 3.5 h.
* **(c)** the in-memory mass/inertia override already exists and HSP's deck builder takes
  **no file input at all**, so the returned Deck object is the only override point and
  **GI3(c) raises no escalation**.
* **(d)** only the 12 buoys carry buoyancy; the five bodies R2 resizes have no draft of
  their own. The system gets **lighter** on iteration one, so ballast is **added**.
* **(e)** the two-key worktree resolver, seven assignments across six files, with tests.

## Which gates pass

| | |
|---|---|
| whole suite at `a3a30d2` | 3970 passed, 2 failed, 0 skipped |
| the three report-guard files | 468 + 24 passed |
| `scripts/check_carried.py` | all 29 findings carried |
| the CI workflow guards | 85 passed |
| `ruff`, `black --check`, `mypy` | clean |

**The two failures are the whole of the FQ3 escalation** — the npz staleness guard and the
F6 deliverable test downstream of it — and neither is clearable by any edit of the
implementer's.

## What is escalated, and it is the substance of this step

**The committed `data/f4/dynamic_inputs.npz` does not regenerate from this tree.** numpy
and scipy sit off `requirements-lock.txt` (2.5.4 / 1.18.1 against 2.4.4 / 1.17.1), the
difference is round-off — ~197 eps relative to each array's own scale, on the one case
measured — and FQ3 already ruled this case in advance: *"if the golden moves under these
pins, STOP and report rather than re-baselining."* Two options, both costed in the
report's §7, and the choice is Xabier's.

**And GI's own D1 and GI5 step 2 (iii) contradict each other** — consistent only if
ballast is identically zero, and then D2's draft cannot be held when steel moves.

## What was deferred and why

* **R1243 — carried into step 1 by name and still blocking.** R1239's observation stands
  (chaining rungs in one job means a red rung hides every rung after it) and its repair
  does not. The fix is to stop the chaining — separate jobs, or `if: always()` per step,
  with a CI section that names skipped STEPS — which is apparatus work and not step 0's.
* **R1248 — carried to step 2.** `scripts/export_buoy_centers_ref.py` checks the stable
  tree's NAME and never its TAG, so a tree merely *named* `HSP-stable` regenerates EB6's
  input while the file declares the pinned tag. Documented rather than hidden, and the
  committed snapshot is untouched.
* **R1232** stands for the write run: `pin_threads()` cannot be called below the module's
  own numpy import, so the environment is **recorded** in the provenance and not held.
* **Rungs 4 and 5 are unmeasurable in CI while the escalation stands.** Rung 6 is red, so
  the rungs after it do not execute. Written down rather than fixed wrongly — which is
  exactly what R1243 was.

## R1243, and the two records the report must not carry (EK3)

**R1243 is the closure commit's first item (FF0) and it is a defect introduced while
repairing another.** R1239's observation was right -- CI had never measured rung 4 -- and
the repair chosen for it was wrong in a way the file already said.

```
claim  the rungs should run in the ladder's own order, and CI's ladder job would go from
       one red to two, the second being the escalation becoming visible
cmd    sed -n '496,503p' .github/workflows/ci.yml       (UNCHANGED by that diff)
out    "AND RUNG 6 RUNS BEFORE RUNG 4 (CH3). The goldens ask whether today's bytes equal
        yesterday's, which stays interpretable whatever ladder 4 says; chained behind it
        they were skipped for eleven rounds while running on ten determinism legs ...
        `tests/test_ci_determinism_gate.py` asserts that position."
cmd    pytest -q tests/test_ci_determinism_gate.py      (at the reordered commit)
out    1 failed, 12 passed -- test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8
cell   ONE VARIABLE, the step order, from the two runs rather than from reasoning:
         rungs 1,2,3,6   ladder row  2143 passed, 1 failed, 0 skipped
         rungs 1,2,3,4   ladder row  2011 passed, 1 failed, 0 skipped
       -477 (rung 6 AND the whole of tests/regression), +345 (rung 4), SAME `1 failed`
rule   CH3, and `tests/test_ci_determinism_gate.py`, which asserts the position
judge  **THE PREDICTION IS REFUTED BY ITS OWN COMMIT'S RUN: one red, not two.** Rung 4
       fails while the escalation stands, so rungs 5 AND 6 skip -- the very mechanism
       R1239 identified, applied to R1239's repair. The escalation did not become
       visible; it MOVED, from the rung-6 deliverable red to the rung-4 staleness red,
       and the rung-6 one went invisible, taking the whole of `tests/regression` out of
       CI with it -- which FV1 assigns to CI in so many words, and which holds
       `test_f6_deliverable_agrees_with_itself.py`, the only automated check that a
       published deliverable still regenerates.
       Nothing would have said so: `ci_section.py` reads a JOB's conclusion and parses
       `run_rung:` lines, and a skipped STEP emits no such line.
       **A general principle was appealed to over a specific, measured, gated ruling
       recorded eight lines from the edit.** That is the whole error.
```

**Reverted; `tests/test_ci_determinism_gate.py` is green again (13 passed).** R1239's
observation stands and its repair does not: chaining rungs in one job hides every rung
after a red one whichever order they sit in, so the fix is to stop the chaining -- separate
jobs, or `if: always()` per step, with a CI section that names skipped STEPS. That is step
1's and **R1243 carries into it by name, still blocking.** Meanwhile R1239's second exit is
taken as the honest record: **rungs 4 and 5 are unmeasurable in CI while the escalation
stands.**

**R1244 -- revision 2's rounds table has a wrong row, and it is corrected HERE rather than
there.** The row for the run at `0c5c864` reads `**no result** (status in_progress)`; that
run concluded `failure` at 18:58:00Z, thirty minutes before the commit carrying the table
was written. That is R1237, and the report's §17 states the defect without naming the run
or the row. **The table is left as it shipped.** Silently rewriting a reviewed generated
record so it no longer shows what was published would remove the evidence of the finding.

**AND EK3 IS WHY THESE TWO SIT HERE AND NOT IN THE REPORT.** The closure commit first put
them into `docs/reports/R2/step-0.md`, which EK3 forbids -- *"a closure commit NEVER touches
a step report after that report's final verdict"* -- and the guard said so immediately:

```
cmd    pytest -q tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
out    the report at `e71ecd5` is newer than the verdict at `e511161` and names `a3a30d2`.
       Written with the newest verdict available, it must answer that one.
rule   EK3, measured three ways in CLAUDE.md: "any commit that touches a closed report
       before a newer verdict exists reddens it"
judge  **FOURTH TIME IN THIS STEP THAT THE `Answers:` HEADER TRAILED THE NEWEST VERDICT**,
       and the first three were R1230, which this report answered two revisions ago. The
       report is restored byte-for-byte to its final-verdict state at `0fb8c93` and every
       post-closure word is in this file instead, which is exactly where EK3 routes it.
       The reviewer's own list said "closure artifact: R1243, R1244-R1247" and the report
       was never the right home for them.
```

## No number moved

No tolerance was added, widened or removed: `git diff` over `floatfea/tolerances.py` is
empty across every commit of this step, and no declared counter moved. §4 of
`docs/milestones/R2.md` lists the five values step 2 will need and classifies two of them
as **not** tolerances, with the reason.

## The one reusable rule this step produced

**Use the committed generator. Where one exists, a second implementation is the defect —
and the one you write will be the lenient one.**

Measured three times, each time by running the pair against each other rather than reading
either:

| | the two implementations | mine was |
|---|---|---|
| R1221 | the `MENTION` filter, guard and generator | present in one site only |
| R1240 | the Carried-section scoping | fixed in one site, pair unsatisfiable |
| the eight under-declared sites | the touched-line predicate | **lenient** — `range(380,405)` where the gate reads `{379,380}` |

And the fourth fact is what turns it from an observation into a rule:
**`scripts/untouched_sites.py` was committed the whole time**, its docstring already
saying *"IT IS THE GUARD'S OWN LIST, NOT A SECOND OPINION … a generator with its own regex
is a second implementation of the thing being satisfied, and the two drift — which is how
the first version of this script produced 68 rows against the guard's 87."* An ad-hoc
script was written beside it and drifted by the same mechanism, in the same direction.

**Both halves are measured.** Lenient: eight reds shipped. Already-solved: the committed
generator refuses on the unavailable-diff case the ad-hoc one would have read as "nothing
touched".

## The honest account of the round

Five reviewer rounds produced **nineteen blocking findings and every one was real.** The
implementer's own, recorded because the pattern matters more than any single instance:

* two wrong diagnoses of the `--check` refusal, the second with the refuting ablation
  already in git history;
* an escalation whose premise was never run (`.claude/hooks/` named as a blocking site; it
  has no such collision);
* a false claim in a reviewer brief about the implementer's own file contents;
* a figure attributing a red to a test that had not run, with the right answer printed
  twenty lines above;
* **a repair that broke the gate existing to prevent it**, with the reason recorded eight
  lines from the edit, and shipping a prediction its own run refuted;
* U+FFFD written into a published report by a script missing an `encoding` argument;
* a splice that deleted two sections by replacing a range instead of a token;
* a generator output pasted from a truncated console capture, publishing two red tests as
  green;
* three checks that could not fail, one of them eleven lines below a docstring warning
  about exactly that.

The common cause in nearly all of them is **asserting from reading rather than running**.
Every one was caught by something that ran, and none reached a number in front of Xabier.

**The two decisions that could have put a wrong number in front of him were both
declined**: pushing through the `--check` refusal, and regenerating the F6 deliverable to
agree with a red gate. Four rounds of not taking the cheap wrong repair is the best
evidence this step produced.
