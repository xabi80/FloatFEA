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
