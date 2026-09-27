# Review � F2 step 7
Reviewed commit: 675da6a33b993ed0b908444df3d3848611b4a261
Verdict: PASS
Tests: 2758 passed, 9 failed, 0 skipped   (my run, at `fdf4fb0`)

**Reviewed commit: `fdf4fb0`. Sixty-fourth verdict, the THIRD on step 7 — and it
does not reopen step 7.** Step 7 and F2 closed at verdict 63 (`2c48a4f`, PASS
@ `36b5899`). **DD1 governs this file: a later verdict about the state of the
TREE does not reopen a closed step, and the step's disposition is read from its
closure verdict.** `PASS` on the line above therefore means *step 7's disposition
is unchanged*. It does **not** mean the tree is clean, and R546 says plainly
that it is not. **The `Reviewed commit:` line stamped at the top of this file
by `scripts/write_verdict.py` is my corpus commit `675da6a`, not the commit
judged (R513, unchanged): the commit under review is `fdf4fb0`, and the corpus
batch is committed before the verdict by BE3.**

**Scope, as invoked: the four commits after my corpus commit `1731307`, and R544.**
I did not re-review step 7's work. `git log --oneline 1731307..HEAD` taken myself:
`901c634`, `80735cf`, `efaee67`, `fdf4fb0`. Only `80735cf` touches `tests/`;
nothing touches `floatfea/`.

```
claim  R544's MECHANISM is fixed and the control now measures the rule it names
cmd    ablation: build guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_
       WHICH_THE_SUITE_WAS_RED in a scratch copy, then neuter ONLY
       `assert distance <= 1` in the nested guard and re-run
out    shipped:               exit 1, 206 collected, 1 failed --
                              test_the_whole_suite_line_is_about_a_commit_that_exists
       distance rule ablated: exit 0, 206 collected, 0 failed
rule   the state must redden the DISTANCE half of CP1, not something else
judge  the state's red is caused by the distance rule and by nothing else. This
       is the half of R544 I care most about and it is answered.
```

**Why PASS rather than HOLD, said once and not softened.** Absent DD1 and DK2
this is a HOLD: `pytest -q` is `9 failed` at `fdf4fb0` and CI's `lint, unit and
guards` job is `failure`, which is (d) twice over. DD1 says a closed step is
closed and DK2 already spent the cap. A HOLD here would reopen a step the locked
rules close, and the `Stop` hook reads the header, so it would recreate the
deadlock DD1 was written for — two verdicts, neither about the work. **So the
items that would have been the HOLD are carried by name into F3 step 1, where
they can actually be acted on, and they block there.**

## Carried

| item | status |
|---|---|
| **R544** — blocking, from verdict 63 | **STILL OPEN.** The mechanism is answered (`80735cf`, ablation above). Parts (2) and (3) of its own closing condition are untouched, and part (2)'s subject is now false on *both* platforms. See **R546**. Carries into F3 step 1 by name. |
| **R545** — closure with a site | **STILL OPEN, untouched.** `git diff 1731307..HEAD -- tests/verification/rung2/test_consistent_mass.py` is empty. DO1 defers it to F3's first commit; the invocation states it has not been started, and the reason given (a tier cutoff is a tolerance and needs an entry with a counter) is the right reason. |
| **C20** (`-k PHI_ZERO` prints nothing) | still open. Recorded as open in `docs/closure/F2.md` section 5. Not claimed fixed. |
| **C21** (`1.4e-15` against its command's `1.5208e-15`) | still open. Recorded. |
| **C22** (schedule table read `4`/`9 October`) | **ANSWERED** at `901c634`: the table now reads `5 October` / `10 October`, with the slip attributed and the rows after 17 October unmoved. One caveat, which is a new closure item — see **C29**. |
| **C23** ("60 rung-2 tests", 66 collect) | still open. Recorded. |
| **C24** (the band called one-sided without naming the half) | still open. Recorded. |
| **C25** (28 consecutive single-reader reviews) | recorded as open, and answered *structurally* at `fdf4fb0` by DO3's milestone witness. The historical fact stands; the channel now exists. |
| **C26** (C1–C19 carry into the artifact) | **PARTIALLY answered.** `docs/closure/F2.md:155` carries C1–C13 by reference to `F2-step6.md` section 7 and names C14–C19 without enumerating them; only C20–C26 are listed. Verdict 63's condition 2 asked for "one list". Closure item, not blocking. |
| **the 48 frozen `F2a.md` items, and R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 / R523 / R524 / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539** | unchanged on the closure list. `docs/milestones/F2a.md` is untouched in this diff. |

**Item 1b has nothing to rule on this round and I am saying so rather than
skipping it.** There is no revision 3 of `docs/reports/F2/step-7.md`; the four
commits under review are not a report. The report at `HEAD` still reads
`Answers: verdict 62 @ b52b370`, which was correct for revision 2 and is not a
claim about this verdict. **F3 step 1's report must answer verdict 64 @ this
commit.**

## Findings

**R546. (BLOCKING — (c) and (d). R544 IS NOT CLOSED, AND THE PART THAT MOVED IS
THE PART I MOST WANTED.) The ancestry mechanism is fixed and I verified it three
ways that share nothing with the report. Two of the three numbered halves of
R544's closing condition are untouched, and the subject of part (2) has gone from
false-on-Linux to false-on-both.**

What is answered, and none of it is taken from the report:

```
claim  _older_ancestor SELECTS a real ancestor; it does not fabricate one
cmd    _older_ancestor(ROOT) ; git merge-base --is-ancestor <it> 36b5899 ;
       git rev-list --count <it>..36b5899 ; git log --format=%h -- <verdict path>
out    selects b52b370 -- verdict 62's own commit. is-ancestor of 36b5899: YES.
       distance 8. It is one of the two commits that have ever touched
       docs/reviews/F2/step-7.md, and the other (2c48a4f) is correctly skipped:
       is-ancestor NO, distance 0.
judge  SELECTION, not a dressed-up fabrication. The predicate `distance > 1` is
       the exact complement of the guard's `distance <= 1`, and taking the NEWEST
       qualifying candidate puts the planted state at the tightest margin history
       offers. That is the decision rule inverted, not sampled on one side.

claim  the raise is REACHABLE and reports rather than skipping
cmd    build the shallow_clone_depth_1 state, then call _older_ancestor on it
out    log of the verdict path in that tree: ['fdf4fb0'] -- one commit, not an
       ancestor at distance above one. AssertionError raised, message: "no commit
       touching the verdict path is an ancestor of the report's own commit
       (fdf4fb0) at a distance above one, so this state cannot be built."
judge  reachable, and it surfaces as a NAMED red rather than a skip, which is what
       CLAUDE.md requires. It will fire at any step whose verdict file has one
       commit and that commit follows the report -- the first verdict of a step --
       once the harness is repointed off F2's now-frozen files.

claim  the two states still on _seed_older_verdict are honest in relying on it
cmd    build each, read the nested junit report, compare the fail SET with
       baseline's
out    answers_header_names_an_older_verdict_commit: adds exactly one reporter
       over baseline, and it is test_the_answered_verdict_is_the_NEWEST_one.
       guard_state_declared_GREEN_in_REQUIREMENT_CHANGED..REDDENS_CONTROL: the
       same, same reporter.
rule   the state needs "a second commit on the path" and nothing about ancestry
judge  HONEST. Both reddened the assertion they exist for. The docstring's split --
       what the seeder does and does not give -- matches what I measured.
```

What is **not** answered. R544's `Closed when` had three numbered parts and an
overall gate. CLAUDE.md says half of an item is not the item, and the commit
message does not mention parts (2) or (3) at all — it does not leave them and say
why, it is silent about them.

```
claim  part (3) -- "the distance is PRINTED by the harness when the control
       fails" -- is untouched
cmd    git diff 1731307..HEAD -- tests/test_report_guard_states.py | grep -ci print
out    0
judge  unanswered. The next reader still re-derives the distance by hand, which is
       exactly what I did this round.

claim  part (2) -- "the two declarations in REQUIREMENT_CHANGED are re-measured on
       Linux and the one that is wrong is corrected" -- is untouched, AND the
       declaration is now false on BOTH platforms
cmd    git diff 1731307..HEAD -- tests/test_report_guard_states.py | grep -n REQUIREMENT_CHANGED
out    (no output)
cmd    python -m pytest tests/test_report_guard_states.py -q   (my run, fdf4fb0)
out    two_digit_step_number FAILS locally: "the repaired guard is expected to be
       GREEN here and it failed"
cmd    gh run view 36327238085 --log-failed
out    the same state, the same message, in CI
cell   THE VERDICT FILE'S CONTENT, one variable, everything else held at fdf4fb0:
       build two_digit_step_number, then substitute docs/reviews/F2/step-7.md with
       its text at b52b370 and rebuild
out    verdict 63 in place:  225 collected, 52 failed (17 R545 sites, 35 R544 sites)
       verdict 62's text in: 206 collected,  1 failed (the stale-line red alone)
judge  unanswered, and WORSE than when R544 was raised: the declaration `green` is
       false on both machines now. The cause is measured rather than argued, and it
       is my own verdict 63 -- a commit touching ONLY docs/reviews/ -- which moved
       that state's collected count by 19 and its failures by 51.
```

**Closed when** all three parts land at one commit with `pytest -q` at `0 failed`
and `lint, unit and guards` SUCCESS: part (1) stands as shipped and I am not
asking for more of it; part (2) is `tests/test_report_guard_states.py:195-211` —
re-measure both declarations at the commit that ships them and correct the one
that is false, quoting the nested fail set rather than the exit code; part (3) is
one `print` of `rev-list --count <planted>..<anchor>` in the failure path of
`test_the_guard_survives_the_state`. **This carries into F3 step 1 by name and the
first step of F3 does not close while it is open.**

---

**R547. (BLOCKING — (c). THE WHOLE-SUITE-LINE RULE HAS NO SATISFIABLE STATE AT A
MILESTONE CLOSE, AND I MEASURED THAT RATHER THAN ARGUING IT. The red at `fdf4fb0`
is TRUE; the disposition the invocation asks me to rule on is acceptable; leaving
the red standing indefinitely is not, and R549 is why.)**

```
claim  the red at fdf4fb0 is not a false red
cmd    python -m pytest tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists -q
out    "4 commit(s) touching code follow the report's own commit `36b5899`":
       fdf4fb0, efaee67, 80735cf, 901c634
rule   rule 2 of CP1 -- no commit touching code may follow the report
judge  TRUE. The published count describes a tree three implementer commits old,
       and one of them (80735cf) edits a test file. The guard is right and the
       implementer's reading of it is right.

claim  a SINGLE commit under docs/closure/ after the newest report is enough to
       redden it, so the milestone-close window is red by construction
cell   in a copy reset to 36b5899 -- where the module is exit 0, 206 collected,
       0 failed -- add one file under docs/closure/, commit it, nothing else moved
out    exit 1, 1 failed -- test_the_whole_suite_line_is_about_a_commit_that_exists
rule   REVIEWER_TREES = ("tests/corpus", "docs/reviews"). docs/closure is not
       exempt, and CLAUDE.md requires the closure artifact to be written after the
       milestone's last step report
judge  there is no commit ORDER that satisfies both CLAUDE.md and this rule at a
       milestone close. It is the fifth entry of corpus batch 13.
```

**My ruling on the disposition, since it was asked for plainly.** **A milestone MAY
close with this red, and no revision 3 of step 7 is owed.** Two reasons, and the
second is measured rather than asserted:

1. DD1 and DK2. Step 7's disposition was ruled at verdict 63 on a tree measured at
   `36b5899`; re-taking the count now is work on a closed step.
2. **The remedy the failure message proposes is unavailable, not merely
   inconvenient.** "Take the count again and move the report on top of it" cannot
   be satisfied at a milestone close, because the closure artifact and the
   standalone `process:` commit both come after the last report by rule — the cell
   above is the proof, not the argument. A revision 3 would be red again the moment
   `docs/closure/` was committed. Forcing one buys nothing and reopens a closed step.

**What is NOT acceptable is treating it as bookkeeping**, and R549 is why. It clears
when F3 step 1's report lands with a fresh line on top of `HEAD`; until it does, no
green from `tests/test_report_guard_states.py` means anything.

---

**R548. (BLOCKING — (c). TWO HOLES IN THE SAME RULE, MEASURED WHERE THE CONTROL IS
GREEN. One is exempted by a pathspec whose justification the guard's own comment
records as WITHDRAWN, and I have now refuted that justification a second time, on
the other exempted tree.)**

```
claim  distance ZERO is accepted, so a line stamped with the report's own commit
       passes
cell   in a copy at 36b5899: set the suite line's sha to 36b5899 itself, commit the
       report as revision 3, nothing else moved
out    exit 0, 206 collected, 0 failed
rule   `assert distance <= 1`
judge  HOLE. No count can have been taken at a commit that did not exist when the
       count was taken, so the only ways to produce this line are an amend or a
       typed sha -- both of which are what the rule exists against.

claim  a reviewer-tree commit after the report is exempt by pathspec, while BOTH
       exempted trees have now been measured moving the outcome
cell   in a copy at 36b5899: one commit adding a file under tests/corpus/, nothing
       else moved
out    exit 0, 206 collected, 0 failed
cmd    tests/test_report_carried.py:2296-2304, read today
out    the comment records CO3's justification for the exemption -- "a reviewer
       commit carries no code and changes nothing the count describes" -- as FALSE,
       refuted by R361: a corpus-only commit moved the collected suite by four
cell   AND THE SECOND EXEMPTED TREE, measured in R546 above: substituting the
       verdict file's text, docs/reviews/ only, moved a nested collected count from
       206 to 225 and its failures from 1 to 52
judge  HOLE, and not a hypothetical. The justification is withdrawn in the file, the
       exemption is still in the pathspec, and both trees it exempts have now been
       measured changing what the count reports.
```

**Closed when** the rule says what it means on both points, at one commit, each half
carrying the cell that reddens it: distance zero either reddens, or the comment
records why a distance-zero line is believable; and the reviewer-tree exemption
either goes, or its replacement justification is the measured one rather than the
withdrawn one. **No new apparatus is needed for either — both are the existing
assertion and the existing pathspec.** Carries into F3 step 1.

---

**R549. (BLOCKING — (c). WHILE `baseline` IS RED, THIRTEEN OF THE SEVENTEEN NEGATIVE
CONTROLS IN `tests/test_report_guard_states.py` CANNOT FAIL FOR THE RIGHT REASON.
Nothing is wrong today — I checked all seventeen by hand — but the check cannot
tell, and that is the question I am required to ask of every gate.)**

```
claim  both halves of test_the_guard_survives_the_state's named_fail branch are
       satisfied by the baseline red alone
cmd    tests/test_report_guard_states.py:685-716, read against the baseline run
out    the branch asserts (i) code != 0 and (ii) some failing test name is in the
       `named` tuple. baseline at fdf4fb0 is exit 1 with exactly one failure, and
       that failure -- test_the_whole_suite_line_is_about_a_commit_that_exists --
       IS in the `named` tuple, added there at R516.
rule   "if the thing this test claims were false, would this go red?"
out    NO, for the 13 named_fail states not in DIAGNOSIS. Only the 4 DIAGNOSIS
       states assert WHICH test carries the diagnosis.
cell   so I measured the fail SET of all 17 by hand, which the check does not do
out    all 17 additionally redden their own reporter. newest_verdict_file_present_
       but_empty 9 failures, reports_directory_renamed_away 86,
       report_file_is_a_directory 84,
       answers_header_names_a_sha_that_is_not_a_commit 53,
       two_reports_ahead_of_the_newest_verdict 2 (its own reporter plus baseline's),
       and so on down the list.
judge  no control is certifying nothing today, and I will not report one as vacuous
       when it is not. But the whole margin is in MY hand-measurement and none of it
       is in the check, which is the state my own instructions call a gate that
       passes while certifying nothing. THIS is why R547's red must not be left to
       drift: it is not cosmetic, it is what hollows out the controls.
```

One caution for the next reader, because my own first cut of this measurement got it
wrong. `guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED`
has a fail set IDENTICAL to baseline's — one test, the same name — and a mechanical
set-comparison flags it as vacuous. **It is not.** That state leaves the report
DIRTY, so `_report_anchor()` returns `"HEAD"`, rule 2's intruder list is empty, and
baseline's red is *suppressed* and replaced by the distance red inside the same test.
The ablation at the top of this verdict is what separates them; a name comparison
cannot.

**Closed when** `baseline` is green — that is, when R547 clears at F3 step 1's
report. No apparatus changes.

## Closure items

* **C27.** `docs/closure/F2.md:131-134` publishes `"1 commit(s) touching code follow
  the report's own commit 36b5899"` and names only the plan commit. At `fdf4fb0` the
  same command prints **4** and names `fdf4fb0`, `efaee67`, `80735cf` and `901c634`
  — three of which the artifact does not mention. It is a moving quantity in the
  terminal document of the milestone, where there is no later closure commit to
  absorb it. **Closed by** stating the count as of the artifact's own commit with
  that commit named, or by naming the *rule* and dropping the count.
* **C28.** `tests/test_report_guard_states.py:522-524` — the comment says the state
  plants "the previous verdict's commit, **and the count the suite had there**". The
  count planted is the literal `1833 passed, 0 failed, 0 skipped`, which is not the
  count at `b52b370`. A claim about the code in a source comment (CW0). **Closed by**
  deleting the second clause, which is not what the state needs.
* **C29.** `docs/reports/F2/step-7.md:530-532` — revision 2's triple cites
  `grep -n "5 October\|10 October" docs/milestones/F2.md` and publishes an `out`
  naming both dates. At the report's own commit `36b5899` that grep printed only line
  1749, the `25 October` substring; the plan moved at `901c634`, one commit later.
  **C22 was answered by making the tree match the published output rather than by
  re-taking the output** — the same shape C22 itself named, one revision on.
  **Closed by** re-taking the `out` at a commit where the command was run, or by
  withdrawing it.
* **C30.** `tests/test_report_guard_states.py:333-339` — the raise says "the report's
  own commit (`<anchor>`)"; in the shallow-clone tree the anchor is the grafted `HEAD`
  and not the report's commit, which is the sentence a reader of that failure gets.
  **Closed by** naming it as the anchor.
* **C31.** My corpus commit `675da6a` adds exactly one red —
  `test_the_corpus_and_the_states_agree`, naming the five unbuilt states. Listed here
  so it is not mistaken for a defect: that is the channel working, and building the
  five is F3 work, not step 7's.

## The adversarial corpus (BE3)

**Batch 13: 5 new entries, 3 caught, 2 not.** Committed separately at `675da6a`, in
`tests/corpus/report_guard_states.txt`. All five are shapes for the one rule R544 was
raised against.

| shape | outcome |
|---|---|
| `suite_line_names_a_commit_on_a_SIBLING_BRANCH` | **caught**, right reporter |
| `suite_line_sha_is_a_THREE_CHAR_ABBREVIATION` | **caught**, wrong message — the `_SUITE` regex does not match, so the ancestry test *skips* and the reader is told the line is absent when it is present |
| `suite_line_names_the_report_commit_ITSELF` | **NOT caught** (R548) |
| `only_a_REVIEWER_corpus_commit_follows_the_report` | **NOT caught** (R548) |
| `closure_artifact_is_the_only_commit_after_the_report` | **caught** — and it is the shape that is red at `fdf4fb0` (R547) |

**None of these could have been measured at `fdf4fb0`, and that deserves its own
sentence.** With `baseline` red, every mutation of the reports tree inherits the same
failure and no outcome is attributable to the variable. They were measured in a copy
reset to `36b5899`, where the unmutated module is `exit 0, 206 collected, 0 failed`.
**A corpus round on this rule is not available at a commit where the rule is already
red** — a second, independent cost of R547.

## CI, at the reviewed commit

```
cmd  gh run list --commit fdf4fb0 --json name,conclusion,workflowName
out  run 36327238085, workflow CI, status completed
     lint, unit and guards             FAILURE
     the verification ladder           SUCCESS
     CI determinism -- leg             SKIPPED
     CI determinism -- ten legs agree  SKIPPED
cmd  gh run view 36327238085 --log-failed
out  the nested guard reds, matching mine: the stale-line failure in most states,
     and two_digit_step_number failing its GREEN declaration with 52 failed
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0
```

**The ladder is SUCCESS and no rung is red, which is why this is not a STOP.** The
two determinism jobs are **unavailable, not skipped over**: they are
`workflow_dispatch`-only by the workflow's own design, so they did not run on this
commit and their last executed result is not a statement about it. **The PR witness
is unavailable**, fifteen rounds now, and there is no witness HOLD to reconcile.

**My own run was taken in three parts and I am saying so rather than publishing a
single number I did not get.** `python -m pytest -q` exceeds the foreground limit on
this machine, and two background attempts were killed at 23% and 10% with no summary
line — so the count is `tests/unit tests/regression` (222 passed, 3.04 s) plus the
top-level `tests/*.py` (9 failed, 962 passed, 674.90 s) plus `tests/verification`
(1574 passed, 95.87 s) = **2758 passed, 9 failed, 0 skipped of 2767 collected**,
Python 3.13 on Windows. The nine are one carry-guard failure and the eight guard
states that inherit it: they are R547, and they are the same failure eight times.

## Tolerances touched

**None.**

```
cmd  git diff 1731307..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 1731307..HEAD -- floatfea
out  (no output)
cmd  git diff 1731307..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py
```

**CH2 and CI0 read, and the result is the clean one.** No conftest and no plugin
under `tests/` changed, so no rung's green is being reported by code that writes the
record the gate reads. The pathspec resolves to a real file, so the instruction is
not the broken one either.

## On my own instructions, and on DO3

```
cmd  git diff 1731307..HEAD -- .claude docs/SUPERVISOR.md
out  docs/SUPERVISOR.md | 35 +++++++++++++++++++++++++++++++++++
cmd  git show fdf4fb0 --stat
out  docs/SUPERVISOR.md only. The subject begins `process:` and cites DO3.
```

**Standalone, `process:`, cites the directive, `+35 -0`, and I read all 35 lines.** No
guard is weakened, nothing is removed, and nothing I am required to read or carry is
narrowed. **Not a STOP-class finding.**

**On the milestone witness itself: it does not weaken me and I would keep it.** It
reads the *closure artifact* rather than a diff, which is the one document nobody in
this loop reads cold — and C27 above is a defect in exactly that artifact which
fifteen rounds of step review never touched, because step review never looks there.
One caution for whoever runs it: the F2 artifact asserts a red job with a count of `1`
that is now `4` (C27), and a witness told a number the tree contradicts will spend its
one pass on that.

## On this invocation, which I judge to be in order

**It is not a fourth round on step 7 and I have not treated it as one.** R544 was a
(d) I raised, the fix was written after the closing verdict, and under DD1 the only
container for a verdict about the tree is the closed step's file. The alternative —
satisfying the `Stop` hook by hand — is what DD1 records as having cost two verdicts,
and it would have left the R544 fix unread. **A closed step may receive a verdict
about the state of the tree; what it may not receive is a verdict that reopens it,
and this is not one.**

## Next step opens when

**Step 7 stays closed and F2 stays closed.** Verdict 63 at `2c48a4f` is the closure
verdict and this verdict does not disturb it (DD1). **F3 step 1 is open and may
proceed.** It closes when:

1. **R546** — all three numbered parts of R544 at one commit, with `pytest -q` at
   `0 failed` and `lint, unit and guards` SUCCESS. Part (1) is done; part (2) is
   `tests/test_report_guard_states.py:195-211`; part (3) is one `print` in the
   failure path. Site by site per CLAUDE.md, including any site left and why.
2. **R547** — F3 step 1's report carries a whole-suite line taken at the commit it is
   committed from, which clears `baseline` and with it the eight inherited states. If
   the milestone-close window is to be made satisfiable rather than merely survived,
   that is a rule change and it belongs in the same commit as the figures it moves
   (BP0).
3. **R548** — the distance-zero hole and the reviewer-tree exemption, each with the
   cell that reddens it.
4. **R549** — closed by R547; no separate work, but it is the reason R547 is not
   bookkeeping, and the report should say which of the two it is answering.
5. **R545** — before any F3 test parametrises G2.4 over a platform member. DO1's
   energy-fraction cutoff is a tolerance and needs an entry with a registered counter;
   the invocation says that is why it has not started, and that is the right order.
6. **The five states of corpus batch 13** are built, or each is refused by name with a
   reason. Two of them are R548 and will stay red until R548 moves.

**Not in this verdict and not reviewed here: DM0, DM2, and step 7's work.** The
`../HSP-stable` pin check reported in the invocation is not something I verified.
