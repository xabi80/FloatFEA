# Review — F6a step 1
Reviewed commit: 2f72db8f86ee28354028974aaa860abcbafb171a
Verdict: PASS
Tests: not re-run -- `git diff --stat b04b124..HEAD -- floatfea tests` is empty and `pytest` does not execute this hook. The measurements are the controlled pairs below.

## R799's repair, reviewed. **PASS. The STOP is lifted. The deviation from my closing condition was CORRECT and the process you used to make it is the right one.**

**Reviewed commit: `2f72db8` (HEAD).** Range `b04b124..HEAD`: `60bb3f0` (the hook) and
`2f72db8` (artifact prose).

**Verified, not taken:**

```
cmd  git diff --stat b04b124..HEAD -- floatfea tests floatfea/tolerances.py
out  (empty)                                   -> EU1 does not arise
cmd  git show --stat 60bb3f0
out  .claude/hooks/require-verdict.sh | 75 +++++++  (1 file, +75 -0)
cmd  git log -1 --format=%B 60bb3f0 | head -3
out  process: R799 -- ... | Cites DIRECTIVE FH0 and answers the STOP in the FH2 hook
     diff. Touches only `.claude/hooks/require-verdict.sh`. No `floatfea/`, no `tests/`.
cmd  bash -n .claude/hooks/require-verdict.sh ; git status --porcelain
out  (no output) ; (clean)
judge **`+75 âˆ’0`. The repair deletes nothing, so the clause I ruled under last round --
      "a change that removes a guard is a STOP" -- cannot reach it.** That is the
      structural fact that settles the disposition before any behaviour is examined.
```

## Carried

| item | status | what I measured |
|---|---|---|
| R799 | **ANSWERED. The STOP is lifted.** | all three of its states now refuse -- below. |
| R793 | **still fixed** | the clean tree still ALLOWS, before and after every plant. |
| R798 | **withdrawn, unchanged.** | |
| R788, R789, R790, R791 | **on the ledger, unchanged** | `-- floatfea tests` is empty in this range. |

## R799's three states, re-measured on the real hook

```
claim  the regression's own states refuse, and the clean tree still allows
cmd    a throwaway clone at 2f72db8; the real hook, real stdin, every plant removed after
out    T0  clean tree                                        ALLOW
       S2b docs/reports/F6a/step-2.md, marker STALE at 1      BLOCK "these step reports
             have no supervisor verdict: docs/reports/F6a/step-2.md"
       S7  the SAME report, marker advanced to 2              BLOCK (the same message)
       S2  docs/reports/F7/step-1.md, marker still F6a 1      BLOCK (names that path)
       T   clean tree again                                   ALLOW
rule   the hook's line 2: "the implementer may not end its turn while the newest step
       report has no supervisor verdict"
judge  **the refusal no longer depends on the marker.** S2b and S7 now give the SAME
       answer, which is the whole of what the STOP asked for: the control and the attack
       are no longer distinguishable by the hook, because the marker is no longer in that
       decision.
```

**And two probes of the new code's own edges, neither of which you listed:**

```
claim  the step comparison is arithmetic, not lexical, and a malformed step name fails
       safe
cmd    plant docs/reports/F6a/step-10.md (gate_from = 1)
out    BLOCK, naming step-10.md
cmd    plant docs/reports/F6a/step-1-draft.md
out    BLOCK, naming step-1-draft.md
rule   `[ "$vs" -lt "$gate_from" ]` and `[ "$rep_step" -ge "$gate_from" ]` are `test`'s
       ARITHMETIC operators, so numeric by definition, and the `case ... *[!0-9]*`
       guards precede them so neither can be handed a non-number
judge  **both correct, and the second fails in the safe direction** -- an unparseable step
       name is added to the orphans rather than skipped, which is my own "empty parameter
       set is an error, not a skip" applied to a filename. One blemish, no number: the
       message then says that file "has no supervisor verdict" when what is wrong is its
       name. A refusal with a misdiagnosis is still a refusal.
```

## The deviation, ruled. **Your scope is right, your process was right, and no criterion question goes to Xabier.**

**First: my condition was wrong and your measurement is what shows it.** I verified the
orphans myself rather than taking the figure:

```
claim  docs/reports/F2/step-1..3 are real orphans, so the unscoped sweep I specified
       wedges the clean tree
cmd    two routes over the real tree: (a) `docs/reviews / p.parent.name / p.name`,
       (b) `p.as_posix().replace("docs/reports","docs/reviews",1)`
out    by parent/name  : ['docs/reports/F2/step-1.md','F2/step-2.md','F2/step-3.md']
       by as_posix swap: ['docs/reports/F2/step-1.md','F2/step-2.md','F2/step-3.md']
       agree: True   | total reports: 16
       docs/reviews/F2 holds: ['step-4.md','step-5.md','step-6.md','step-7.md']
judge  **three real orphans, confirmed by two routes that agree.** My closing condition
       would have replaced a guard that fails false in one direction with one that fails
       false in the other, on the first turn after it landed. **The condition was mine and
       it was wrong.**
```

**AND MY FIRST ATTEMPT AT THAT VERIFICATION WAS CORRUPTED BY THE SAME CLASS YOU REPORTED,
IN THE ACT OF CHECKING YOUR REPORT OF IT.** Route (b) was `str(p).replace("docs/reports",
...)`; on this platform `str(p)` is backslash-separated, so the pattern could not match, and
it returned `[]` against route (a)'s three. I printed `agree: False` and had to fix my own
route before the figure meant anything. **That is the fifth instance this session and the
second to reach a verification of the first** -- and it is why "two independent routes" is
only worth something when they agree and you say so when they do not.

**Second: the scope you implemented is right, and the reason is structural rather than
aesthetic.** `gate_from` is computed from `docs/reviews/F<m>/step-*.md` -- a directory
`protect-reviews.sh` denies the implementer. **So the exemption boundary is
reviewer-controlled: the implementer can add reports, which never lowers the gate, and
cannot add a verdict, which is the only thing that raises the exemption.** Adding a report
can only create an orphan. That is the property a scoped guard needs and it holds.

**Third: deviating was the right call and it needs no pre-agreement.** A closing condition
names *what must become true*, not the implementation. You did the one thing that makes a
deviation safe: **implemented my condition literally, ran it, measured it failing false, and
published the refutation** -- which is my own "convert arguments into measurements" aimed
back at me. Asking first would have cost a round and produced this same answer. **The rule
going forward, so it is written down once: a closing condition may be deviated from in the
commit, provided the commit carries the measurement that refutes it.** A deviation with an
argument instead of a measurement is the thing I would hold on.

## Findings

**R800. (apparatus, FF0 -- next commit, NOT the ledger) The hole you named is REAL and I
reached it: a milestone whose first verdict sits at a later step than an unreviewed earlier
report in the same milestone exempts that report, permanently and silently.**

```
claim  the state exists and the hook allows it
cmd    in the clone: docs/reports/F7/step-1.md (no verdict), plus
       docs/reports/F7/step-2.md AND docs/reviews/F7/step-2.md stamped at HEAD
out    ALLOW   (exit 0, no output)   -- gate_from = 2, so step-1 is below the gate
rule   "within ONE milestone, the lowest step that HAS a verdict is where gating began
       there. A report below it was never gated"
judge  **"I think it cannot arise" was the right thing to distrust.** Reachability,
       measured against the mechanism rather than asserted: in a NEW milestone with no
       verdicts, `gate_from` is empty and every report is gated, so step-1's report blocks
       the turn the moment it exists -- the ordinary sequence cannot produce this. What
       produces it is TWO reports created before any verdict and the reviewer invoked on
       the SECOND one: the turn blocks naming both, a verdict written for step 2 sets
       `gate_from = 2`, and step 1 is exempt from then on. **It needs a reviewer error, not
       an implementer action, and once reached it is permanent and silent.**
```

**Closed when** the historical exemption is DECLARED rather than inferred. There is exactly
one -- `docs/reports/F2/step-{1,2,3}.md`, because the discipline began at F2 step 4 -- and
it is now measured twice over in this file and in your commit message. Name those three
paths in the hook with the measurement beside them and gate every other report from step 1;
then there is no arithmetic over verdict sets at all and no state in which a verdict's
absence creates an exemption. **This is R694's own move:** a constant that was right at one
configuration was replaced by the closed form, with the constant demoted to a floor beneath
every configuration. Here an inference about history is replaced by the one fact it was
inferring.

**Why it is PASS and not another STOP.** `60bb3f0` is `+75 âˆ’0`: nothing is removed, the
guard is a large net strictness gain, and the residual state needs a reviewer mis-invocation
rather than ordinary implementer work -- where R799 was reachable by the implementer, in the
ordinary course, in the commit being guarded. FF0 routes it to the next commit; the ledger
is still the one home it may not have.

## Your three questions, answered

**(1) `block()` is still only moved, and I checked it rather than accepting it twice.**

```
cmd  awk '/^block\(\) \{/,/^\}/' .claude/hooks/require-verdict.sh | sha256sum
out  block() body now: 4 lines, sha 42ab11d92c8e7215
rule 31fe039 -- before FH0 -- gave 42ab11d92c8e7215 for the same extraction
cmd  git show 60bb3f0 -- .claude/hooks/require-verdict.sh | grep -E "^[-+].*(block\(\)|json.dumps)"
out  (no output)
judge **identical sha across three commits, and 60bb3f0 does not touch the function at
      all.** You have now asserted this twice and it has been true twice.
```

**(2) THE SWEEP IS NOT THE EXPENSIVE PART AND I MEASURED WHICH IS.** This answers the
question with a number instead of an opinion, and it corrects the premise:

```
claim  what the sweep costs, as a fraction of the hook
cmd    five runs of the whole hook, then three with the sweep's block excised, timed with
       `date +%s%N` on the real tree
out    whole hook   : 2831, 2704, 2645, 2657, 2630 ms
       without sweep: 2398, 2432, 2270 ms
       -> the sweep is roughly 0.2-0.4 s of ~2.7 s, about 10%
cmd    the shapes it iterates
out    16 reports globbed | 5 review dirs | 13 verdict files
rule   `[ -f "$sib" ] && continue` precedes the inner loop, so the per-milestone verdict
       scan runs ONLY for a report with no sibling -- three today
judge  **keep it where it is.** The dominant cost is `pick_reviewed`'s ancestry loop,
       which is O(n^2) `git merge-base --is-ancestor` calls over the eight shas in F6 step
       2's file -- up to 56 subprocesses -- and that is FH0's, not R799's. Neither is a
       defect: 2.7 s at a turn boundary is not a cost anyone notices, and correctness
       before speed is this repository's own rule.
```

**And it does NOT belong in `tests/test_report_carried.py`.** Two reasons, and the second
is the one that settles it. First, the `check_carried.py` comment's logic does not transfer:
carried-completeness is a property of two files' CONTENTS, which a test can assert, whereas
"a report exists with no verdict" is a property of the TREE AT A TURN BOUNDARY -- a test can
observe it but cannot refuse the turn, and refusing the turn is the entire function.
Second, **`CLAUDE.md` forbids it outright**: "No new apparatus through F6. No new guards,
scanners, meta-tests, detectors or report generators." A new test is new apparatus; a branch
restored to an existing hook under a directive is not. **Do not grow it and do not move it.**

**(3) The deviation disposition is ruled above and the answer is no, you do not need my
agreement first** -- a closing condition names what must become true, and a deviation that
arrives with the measurement refuting the condition is better than the condition was.
**Nothing here goes to Xabier as a criterion question.**

## Tolerances touched

**None.** `git diff --stat b04b124..HEAD -- floatfea tests floatfea/tolerances.py` is empty,
so no value, no counter, no injection: **EU1 does not arise** and I ran the command rather
than taking it. `tests/conftest.py` untouched. **I did not re-run the suite and the header
says so** -- `pytest` does not execute this hook, so a green suite would be evidence about
something else.

**My own instructions: this review is that diff.** `git log b04b124..HEAD -- .claude
docs/SUPERVISOR.md` gives one commit, `60bb3f0`, standalone, citing FH0, purely additive,
and I read all 75 lines.

## The corpus (EG4(e))

**Pause held; no batch, no entry.** The substitute was again the direction that weakens:
your ten replays are ten refusals, and both of this round's results came from the two states
nobody had run -- the F7 plant that ALLOWS (R800) and my own orphan recount that disagreed
with itself until I fixed my route. **Three rounds running, the finding has been in the
state the author did not choose.**

## Next step opens when

**Nothing opens. FH3 stops work and the STOP is lifted, so the tree is in a state where
work could resume rather than one where it must not.**

1. **R800 is fixed in one `process:` commit citing a directive**, under FF0's next-commit
   rule -- the three F2 paths declared, every other report gated from step 1, and no
   arithmetic over verdict sets.
2. **Everything in `60bb3f0` stays.** R799's three states refuse, the clean tree allows, the
   step comparison is arithmetic, a malformed step name fails safe, and `block()` is
   untouched. All measured here.
3. **The ledger stands at R788, R789, R790, R791.** R793, R798 and R799 are closed; R800 is
   routed, not ledgered.

## Disagreement with the criterion -- none

Last round I said this file has no comfortable middle, only PASS and STOP. That was right
about the *verdict* and incomplete about the *routing*: FF0 gives an apparatus finding a home
in the next commit without a HOLD, which is what R800 uses, and the asymmetry I described
bites only when a guard is actually removed. **A `+75 âˆ’0` commit cannot be that**, and
saying so is the correction to my own sentence rather than a complaint about the clause.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: 6caef39c3df933c33961f621d2fcf1c584b241e6
Verdict: STOP
Tests: not re-run -- no `floatfea/` or `tests/` change in the range (verified below). The hook is not exercised by `pytest`; it is exercised by the controlled pairs in this file.

## FH2 -- DIFF THE HOOK, of 2026-10-11. **STOP on ONE missing branch. FH0's substance is correct and must NOT be reverted.**

**Reviewed commit: `6caef39` (HEAD).** Range `31fe039..HEAD` is **four** commits, not two:
`52f33d7`, `a559a8c`, `4862f6e`, `6caef39`. The two the invocation did not name touch
`docs/closure/F6a.md` only, so the scope statement is right in substance -- one code file in
the range -- and I record the count because I checked it.

**Placement is compliant and I verified it rather than taking it.** `4862f6e` is a
standalone `process:` commit, one file, `+144 -42`, citing DIRECTIVE FH0.
`git diff --stat 31fe039..HEAD -- floatfea tests` is empty and so is
`-- floatfea/tolerances.py`. **So this is NOT the STOP-class finding my definition attaches
to a change mixed into a step commit.** It is the other clause in the same paragraph, and
that is the one I rule under.

## Why STOP, and the three dispositions I rejected first

**I found the state you asked for.** My definition's section on my own instructions ends:
*"a change that removes a guard is a STOP."* One branch of this hook's headline guard is
gone, measured in a controlled pair, and the three softer homes are each closed:

* **HOLD is not available.** Not CZ0 (a)-(d) -- not `floatfea/`, not a published
  deliverable, not a tolerance, not a test assertion, and no test is red. My definition
  forbids expressing a non-(a)-(d) finding as a HOLD and I will not.
* **The ledger is FORBIDDEN here, by `CLAUDE.md` and not by my preference.** FF0: *"A
  CLOSURE ITEM IN THE GATING APPARATUS IS NOT LEDGERED ... `.claude/hooks/` ... is fixed in
  the next commit."* Your offer to put anything outside (a)-(d) on the artifact is the one
  home this item may not have.
* **PASS would open increment 2 on a hook that lets a turn end with an unreviewed report in
  the tree**, which is the sentence this hook's own second line claims it prevents.

**STOP costs nothing operationally** -- FH3 stops work anyway -- so all it does is require
one `process:` commit before step work resumes. That is proportionate, and it is the
disposition my instructions name rather than one I reached for.

## Carried

| item | status | what I measured |
|---|---|---|
| R793 | **ANSWERED, and it is really fixed** | the wedge is gone: on the tree as committed OLD blocks on `bf5fdf0` and NEW allows (S1). Three interim checks' worth of refusals end here. **R799 is a different branch of the same rewrite, not R793 reopening.** |
| R798 | **WITHDRAWN, correctly, and I reproduced the measurement** | 8 distinct shas, file order starts `bf5fdf0`, ancestry pick `bf5fdf0`, the two agree -- so `-m1` took the newest. Ruled below. |
| R796 | **answered at verdict 127** and untouched by this range. |
| R797 | **answered at verdict 127** and untouched by this range. |
| R788, R789, R790, R791 | **on the ledger, unchanged** | `git diff --stat 31fe039..HEAD -- floatfea tests` is empty, so nothing in this range could have moved them. |

**Nothing else carries.** The one blocking item is new and is R799.

## Findings

**R799. (STOP) The no-verdict refusal now depends on the marker having been advanced, and
the marker is advanced by the implementer in the same commit it is supposed to guard.**

```
claim  a report with no verdict ends a turn, if the marker has not been advanced to it
cmd    a throwaway clone at 6caef39; OLD (31fe039:.claude/hooks/require-verdict.sh) and
       NEW run on the SAME tree with the same stdin, {"stop_hook_active": false}
out    S2b  docs/reports/F6a/step-2.md planted, marker still says 1
         OLD: BLOCK "Step report docs/reports/F6a/step-2.md has no supervisor verdict at
                     docs/reviews/F6a/step-2.md. Invoke the gating-supervisor subagent on
                     this step before ending the turn. Do not write the verdict yourself."
         NEW: ALLOW (exit 0, no output)
       S7   the SAME report, marker advanced to 2
         OLD: BLOCK (the no-verdict message)
         NEW: BLOCK (the same message, identical)
       S2   docs/reports/F7/step-1.md planted instead
         OLD: BLOCK "Step report docs/reports/F7/step-1.md has no supervisor verdict"
         NEW: ALLOW
cell   S2b against S7: one variable, the marker's number. Same tree, same report, same
       stdin, same two scripts. **S7 is the control and it is why this is a domain
       reduction rather than a broken guard** -- NEW's refusal works exactly when the
       convention is honoured.
rule   the hook's own line 2: "the implementer may not end its turn while **the newest
       step report** has no supervisor verdict"
judge  **"the newest step report" has been silently redefined as "the report the marker
       names".** FH0 was asked to stop the ranking colliding; it also moved the DOMAIN of
       the no-verdict sweep, and the comment it left states the replacement as a
       convention -- "The marker is advanced in the commit that adds the next step's
       report, never before it" -- where the hook used to depend on nothing.
```

**AND I CHECKED THAT OLD'S REFUSAL WAS A REAL CATCH AND NOT R793's WEDGE, because the exit
code alone would have misled me.** R793 makes OLD block on almost every state in this tree,
so "OLD refused and NEW allows" is nearly vacuous unless the message is read:

```
claim  OLD's S2b refusal is the no-verdict check, which PRECEDES the dirty-tree check
cmd    the same plant, OLD's full `reason` parsed out of its JSON
out    Step report docs/reports/F6a/step-2.md has no supervisor verdict at
       docs/reviews/F6a/step-2.md. Invoke the gating-supervisor subagent on this step
       before ending the turn. Do not write the verdict yourself.
rule   R793's wedge produces "floatfea/, tests/, or docs/reports/F6/step-2.md changed
       since the verdict at bf5fdf0..." -- a different string, from a later check
judge  **a genuine catch, not the wedge.** Three of my seven states had OLD blocking for
       the wedge's reason and would have read as findings on the exit code alone. This is
       my own definition's "a residual destroys information", applied to a hook.
```

**AND THE REDUNDANCY THAT USED TO COVER THIS IS GONE, WHICH IS WHAT MAKES IT A STOP RATHER
THAN A GAP.** This is the half neither of us had looked at.

```
claim  every other resolver of the active step is ALSO the marker, and nothing anywhere
       checks that the marker names the newest report
cmd    grep -rn "step-under-execution\|_active_plan" tests/*.py
out    tests/test_report_carried.py:67,71,109
       tests/test_report_guard_states.py:42,45,77
       tests/test_report_numbers_are_sourced.py:50
cmd    grep -rn 'glob("docs/reports\|docs/reports/F\*' tests/*.py
out    (no sweep of docs/reports/F*/step-*.md for a missing verdict, in any file)
cmd    the guard FH0's comment cites, read in full
out    `test_the_plan_names_the_step_under_execution` asserts `len(carrying) == 1` --
       EXACTLY ONE PLAN CARRIES A MARKER. It says nothing about which report it names.
rule   FH0's own justification: "That is the resolver
       `tests/test_report_carried.py::_active_plan` uses, and
       `test_the_plan_names_the_step_under_execution` holds it to EXACTLY ONE plan"
judge  **that is true and it is not the property needed. One marker is not the right
       marker.** Before `4862f6e` the hook resolved the active step INDEPENDENTLY, by path
       ranking -- badly, which is R793 -- and that independence WAS the redundancy: when
       the marker was stale the hook and the guards disagreed, and the disagreement is
       what caught a stray report. **FH0 made the hook agree with the three guards it was
       the only thing able to contradict.** One marker line, in a prose file the
       implementer writes, is now the sole resolver for the entire gating apparatus.
```

**Closed when** the no-verdict sweep stops depending on the marker. The marker should stay
the anchor for *which verdict is read* -- that half of FH0 is right and R793 is really
fixed -- but "a report exists with no verdict" needs a domain that does not come from the
thing being guarded. The check I would describe rather than write: after the marker
resolves, refuse if any `docs/reports/F*/step-*.md` has no sibling under `docs/reviews/`,
naming the paths. That restores OLD's catch without restoring OLD's ranking -- no `sort`,
no `tail -1`, no numeric parse of a label -- so it cannot bring EC0 or R793 back with it.

### What is right, verified and not to be reverted

**FH0's four changes all work, and `block()` really was only moved.**

```
claim  `block()`'s body is byte-identical and only its position moved
cmd    awk '/^block\(\) \{/,/^\}/' on both versions, then sha256sum and diff
out    hook_old: 4 lines, sha 42ab11d92c8e7215
       hook_new: 4 lines, sha 42ab11d92c8e7215
       diff: (empty)
cmd    bash -n .claude/hooks/require-verdict.sh
out    (no output)
cmd    diff the `verdict=` tail of both versions
out    (empty -- the PASS/HOLD/STOP tail is unchanged)
rule   "'I only moved it' is exactly the claim a weakened guard would make"
judge  **verified.** And the move was necessary: the refusals FH0 adds run above the old
       definition point, bash resolves a function at call time, and with `set -u` and no
       `set -e` an unresolved `block` printed to stderr and the script ran on. Your own
       account of that is correct.
```

```
claim  the tie, the label and the ancestry pick each refuse where they should
cmd    the same clone, the real hook, real stdin
out    S5  zero live markers        -> BLOCK "0 plans carry a live step-under-execution
                                      marker. EXACTLY ONE must."
       S4  one sha, unresolvable    -> BLOCK "cannot choose the reviewed commit ... no
                                      single commit among [deadbeef...] has every other
                                      as an ancestor"
       S1  the tree as committed    -> ALLOW   (OLD: BLOCK on bf5fdf0 -- R793's wedge)
judge  **R793 is really fixed and the refusals are real.** S1 is the measurement that
       says so: OLD wedges on `bf5fdf0`, NEW allows a clean tree.
```

**Your attack point 4 is answered and your description of your own code is wrong in the
safe direction.** You wrote that "a file naming one commit that no longer exists still
resolves". It does not: with one sha and `git cat-file -e` failing, the `continue` leaves
`found` empty and `pick_reviewed` returns 1 with the "no single commit" reason, which
**blocks** -- S4 above. And where one bad sha sits among good ones, skipping it picks the
newest *resolvable* commit and the dirty-tree check still runs, whereas OLD's
`[ -n "$reviewed" ] && git cat-file -e "$reviewed"` would have skipped **both** checks
and fallen through to the verdict line. **The `continue` is strictly stricter than what it
replaced, which is the opposite of what you feared.**

**Attack point 1: `[0-9]+` is the right discriminator.** It is what separates the live
marker from the four retired `moved to F3 at step 1 (DY8c)` forms, and your stated failure
mode -- a future retirement written with a bare number, picking two and refusing -- is a
refusal, which is the direction a resolver must fail in. The thing that makes it safe is not
the regex, it is that a tie refuses rather than sorting; both are in place.

### R798's withdrawal is the right disposition, and I verified the measurement

```
claim  `grep -m1` returned the NEWEST reviewed commit, so R798's premise was false
cmd    my own script: list every `Reviewed commit:` of F6 step 2 in FILE order, then ask
       which one has every other as an ancestor (`git merge-base --is-ancestor`)
out    distinct: 8
       FILE order: bf5fdf0, af674e6, 6f3bd0d, c0e3165, 4bc359f, 9567893, ba1527e, 838e00e
       ancestry pick: ['bf5fdf0']
       file-first == ancestry pick: True
rule   `write_verdict.py` PREPENDS (DY6), which C105 already recorded as the reason
       `re.search` is correct for reading one
judge  **withdraw it, and the withdrawal is already written.** `-m1` took the newest, so
       "and therefore the oldest" did not follow from "the first". Your own account of the
       species is accurate and is the one this milestone is remembered for -- a sentence
       right about what it inspected and silent about the axis that decides it. **It
       changes nothing about R793**, which was a different defect in the same three lines
       and is really fixed; and replacing `-m1` with ancestry anyway is right for the
       reason given at the site -- file order is a convention one generator holds in
       place, and ancestry is not.
```

## Tolerances touched

**None, and no `floatfea/` or `tests/` line changed at all.**

```
cmd  git diff --stat 31fe039..HEAD -- floatfea tests floatfea/tolerances.py
out  (empty)
cmd  git show --stat 4862f6e
out  .claude/hooks/require-verdict.sh | 186 +++++++++++------  (1 file, +144 -42)
cmd  git diff --stat 31fe039..HEAD
out  .claude/hooks/require-verdict.sh | 186 ++++++++++---
     docs/closure/F6a.md              | 141 +++++++++-
```

**EU1 does not arise** and I did not take it: no tolerance value, no counter, no
`Final[float]`. `tests/conftest.py` is untouched. **I did not re-run the suite and I say so
in the header rather than omitting it** -- `pytest` does not execute this hook, so a green
suite would be evidence about something else, and the measurements that bear on the change
are the controlled pairs above.

**My own instructions: this review IS that diff.** `git log 31fe039..HEAD -- .claude
docs/SUPERVISOR.md` gives one commit, `4862f6e`, standalone, citing FH0, and I read all 186
changed lines rather than the hunk headers.

## The corpus (EG4(e))

**The pause held; no batch, no entry.** The substitute this round was the thing the pause's
clause exists for: **the repair measured from the side that WEAKENS it.** FH1 asked for four
replays and all four are refusals the new hook makes. I ran three more in the other
direction -- S2, S2b, S7 -- and the finding is in those three and in nothing else. Corpus
batch 31's recorded fault, which is why EH4 exists, is exactly this: *every boundary solved
from the side that makes a gate look strong.* **Your own instinct in the invocation was
right and your cases 5-7 were still all refusals.** The direction that matters is the one
where the new hook says yes.

## Next step opens when

**Nothing opens, and the STOP is narrow. Do not revert `4862f6e`.**

1. **R799 is fixed in one `process:` commit citing a directive**, under FF0's
   next-commit rule and under the standalone-commit rule, before any step work resumes. The
   repair is additive -- a sweep that does not read the marker -- and it must not reintroduce
   a ranking.
2. **The ranking fix, the tie refusal, the label regex, the ancestry pick and the `block()`
   move all stay.** Each is verified above. R793 is really fixed: a clean tree now allows,
   and that is measured, not argued.
3. **R798 stays withdrawn.** The withdrawal in `docs/closure/F6a.md` is correct and I
   reproduced its measurement independently.
4. **Nothing from this review goes on the ledger**, because FF0 forbids this class there
   and the one finding is a STOP.

## Disagreement with the criterion -- none, and one note on the instrument

I ruled under my own definition's clause on changes to my instructions, because CZ0's four
heads do not reach a hook and FF0 forbids the ledger -- so for an item in this file the only
dispositions available are PASS and STOP, and that is a sharp edge rather than a complaint.
**I am not asking for it to be changed**: the asymmetry is deliberate, a file that gates the
gate should have no comfortable middle, and this is the first time in the milestone it has
had to bite. The thing worth recording is that **you invited the check, named the criterion
it should be judged by, and the criterion found something** -- which is the second time in
three rounds that attacking a repair has outperformed the scan the hook was asking for.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: 365fe3fc0e278e0d24fa401ea98d1cc0fcbb4c4d
Verdict: PASS
Tests: 3346 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q -p no:randomly`)

## THIRD INTERIM CHECK (ES0) of 2026-10-11 -- no new report revision, so this counts against NO round. **PASS, and no fourth check is needed.**

**Reviewed commit: `365fe3f` (HEAD).** Scanned `2457ef3..HEAD` -- `24282fa`, `365fe3f`.
Light scope, one target. **Nothing is (a)-(d).**

**Verified, not taken -- all six:**

```
cmd  git diff --stat 2457ef3..HEAD -- floatfea/tolerances.py
     git diff 2457ef3..HEAD | grep -nE "^[-+].*(_COUNTER|Final\[float\])"
     git log --oneline 2457ef3..HEAD -- .claude .claude/hooks docs/SUPERVISOR.md
     git diff --stat 2457ef3..HEAD -- tests/conftest.py 'tests/**/conftest.py'
     git log --oneline 2457ef3..HEAD -- docs/reports
out  (empty) x 5
cmd  git diff 2457ef3..HEAD -- floatfea/ | grep -E "^[-+]" | grep -vE "^[-+]{3}" | grep -vE "^[-+]\s*#"
out  (empty -- so the `floatfea/` change is comment text only, as you said)
judge **EU1 does not arise**, no STOP-class finding, no conftest, EK3 holds, and neither
      EG3 boundary state exists.
```

## Carried

| item | status | what I measured |
|---|---|---|
| R793 | **still open and still not yours** | `.claude/hooks/` untouched by both commits. |
| R796 | **answered, and the case is sound at the level that was missing** -- ruled below | |
| R797 | **answered at both sites, and the form is now right** -- ruled below | |

## The one target: R796's case. It holds, and all three of your attacks fail.

**(1) `monkeypatch.setitem(globals(), ...)` reaches the dictionary the guard reads, and the
case carries its OWN positive control.** You said the mutation was your only evidence. It
is not -- there are two more, and one of them is inside the case.

```
claim  the dict the case writes is the dict the guard reads, by identity
cmd    import the module; compare
       `test_R796_....__globals__` with `test_a_report_does_not_say_CLOSED.__globals__`
out    R796.__globals__  is  guard.__globals__ : True
                   ...  is  module.__dict__   : True
       CARRIED and EXPECTED live there        : (True, True)
rule   `globals()` inside a function in this module IS the module `__dict__`, and a
       function defined in the same module resolves its free names through that same
       object -- so `setattr(module, ...)` and `setitem(globals(), ...)` write to one
       dictionary here, and no import is needed to reach it
cmd    POSITIVE CONTROL: delete the two `setitem` lines, keep everything else
out    E  +  where [('R781', '**answered** ...'), ... 5 rows] = _status_cells()
       tests/test_report_carried.py:878: AssertionError
       FAILED ...::test_R796_the_GUARD_actually_CALLS_the_exemption_predicate
judge  **the case cannot be vacuous in the way you feared, and it tells you so itself.**
       Without the monkeypatch it goes RED at its own `assert not _status_cells()` --
       which prints the real five rows -- rather than reaching `pytest.raises`. And the
       third independent argument: if the patch did not reach the guard, the guard would
       read the real `CARRIED`, return normally, and `pytest.raises(AssertionError)`
       would fail. **Green-as-shipped is itself proof the patch lands.**
```

**And it survives the ordering you did not mention.** `monkeypatch` undoes at teardown, so
I measured the leak rather than assuming it:

```
cmd    python -m pytest tests/test_report_carried.py -q     (DEFAULT order, pytest-randomly
       enabled, three times)
out    133 passed in 1.66s / 133 passed in 1.74s / 133 passed in 1.83s
judge  stable across three random orderings, and `test_a_report_does_not_say_CLOSED` is
       collected and run separately on the real globals in every one of them. No leak.
```

**(2) The needle is `assert cells`'s and no other assertion's. Checked mechanically, which
is the only way this one can be settled.**

```
claim  "no status cell parsed" belongs to `assert cells` and to nothing else, and no
       assertion can fire before it
cmd    grep -n "no status cell parsed" tests/test_report_carried.py
out    789:        "no status cell parsed from the newest revision's Carried table, ..."
       891:    assert "no status cell parsed" in str(caught.value), (
cmd    sed -n '788,800p' tests/test_report_carried.py
out    788: assert cells, (
       789:     "no status cell parsed from the newest revision's Carried table, and the
              section "
       ...
       796: assert not guilty, (
       797:     f"{[g[0] for g in guilty]} are recorded with a word only a verdict may use.
rule   your worry: "if the guard ever fails earlier for an unrelated reason, this case
       would read that as success"
judge  **it cannot.** Line 789 is the only occurrence besides the case's own grep at 891,
       `assert cells` is the FIRST assertion in the guard -- what precedes it is
       `cells = _status_cells()` and the exemption's `return`, neither of which asserts
       -- and the next assertion's message shares no phrase with it ("a word only a
       verdict may use"). So the needle is both unique and first. **Your replacement is
       right, and the capital-`T` failure was the construct working**: a vacuity check
       that fails in the safe direction is a vacuity check.
```

**(3) Calling another test function directly is a new pattern in this repository, nothing
forbids it, and its failure mode is loud.**

```
claim  the pattern is used once and only here
cmd    grep -rn "    test_[a-zA-Z_]*(" tests/*.py
out    tests/test_report_carried.py:886:        test_a_report_does_not_say_CLOSED(capsys)
rule   `CLAUDE.md` and `docs/SUPERVISOR.md` prohibit no such thing; `tests/conftest.py` is
       unchanged and adds no collection rule that would interact with it
judge  **no finding.** The two interactions worth naming are both safe: pytest also
       collects the callee and runs it on the real globals -- measured above, three
       random orderings -- and if the callee ever gains a fixture the caller does not
       request, the call raises `TypeError` rather than silently skipping, which is a red
       test naming the right line. The one thing I would not do is let this spread; as a
       single case reaching a guard that reads module globals, it is the only level at
       which "the guard calls this predicate" is a measurement rather than a reading, and
       that is exactly what it is for.
```

**And the thing you found that I did not ask for is the best part of the commit.** R795's
`contradictory` section cannot serve for this case, because its row parses, so `cells` is
non-empty, so `not cells` is false and the two-clause form refuses the exemption there too
-- a case both forms treat alike pins neither. The discriminating input is the one where
`cells` is empty and `EXPECTED` is not. **That reasoning is the whole of what makes a
counter-case a counter-case**, it is recorded in the docstring, and nobody asked for it.

## R797 -- the form is right now, and the quotation is not a problem. Ruled, so there is no fifth.

```
claim  the live pointer carries no inventory, at either site
cmd    grep -n 'docs/closure/F6a.md` records' floatfea/model/platform.py
       tests/verification/rung3/test_platform_skeleton.py
out    floatfea/model/platform.py:798:    # ... `docs/closure/F6a.md` records what was
         measured once.
       tests/verification/rung3/test_platform_skeleton.py:807:
         `docs/closure/F6a.md` records them.
cmd    grep -n 'It used to' (both files)
out    platform.py:800: ... (R797).** It used to add "with its ...
       test_platform_skeleton.py:809: ... (R797).** It used to
judge  **bare at both sites, which is the form I ruled for, and the single remaining grep
       hit is inside a past-tense attribution.**
```

**Quoting a withdrawn false clause in order to explain it is NOT a CW0 problem.** CW0
prohibits prose that *claims* something about this repository. A clause quoted in the past
tense with its refutation in the same sentence is a record of a retraction, not a claim --
and it is the device by which the defect cannot come back, which this repository uses
everywhere (`"BY A MARGIN ASSERTED IN" IS WHAT THIS SAID`). The test to apply is one
question: *can a reader mistake it for a live claim?* Here the refutation is eight words
later. No. **The form is right and I have no further ask on this sentence.**

**One residual, stated once and deliberately given NO number.** The paragraph that explains
the deletion makes two checkable claims about `docs/closure/F6a.md` -- that it carries no
date, and that its `cmd` field cites a verdict rather than giving a runnable line -- and it
carries its command inline for the first. **Both are true and I checked both this round**,
so the record holds them:

```
cmd  sed -n '380,412p' docs/closure/F6a.md | grep -cE "2026|October"
out  0
cmd  sed -n '389,391p' docs/closure/F6a.md
out  claim  the admissibility margin by body, over the span the gate asserts
     cmd    the reviewer's own 210-build sweep, reported in verdict 123
judge CW0's second option is "a triple", and in substance this is one -- claim, command,
      asserted result. It is not in the form `tests/test_tree_prose_consistent.py` parses,
      so nothing in the tree re-checks it. **I am recording it rather than numbering it,
      because a sentence about where a measurement lives has now been rewritten four
      times and a fifth finding from me would be the defect rather than the cure.** The
      verification above is the answer: the claims are true at this commit and a reviewer
      checked them, which is what the fourth iteration was for.
```

## Findings

**NONE NEW, and that is a ruling rather than an empty section.** Three attacks on R796's
case and all three fail; R797's form is right at both sites; the one residual above is
verified true at this commit rather than left open. **I numbered nothing deliberately:** a
sentence about where a measurement lives has been rewritten four times in these two files,
each rewrite answering my previous finding, and a fifth finding from me would be the defect
rather than the cure. What the record needs from this check is the verification, and it is
in the two blocks above with its commands.

## Tolerances touched

**None.** Both commands are in the verified block at the top: `floatfea/tolerances.py`
untouched, and the diff contains no `_COUNTER` or `Final[float]` line at all. **EU1 does not
arise**, and your reason is right -- the `floatfea/` change is comment text only, which I
confirmed by filtering comment lines out of the diff and getting nothing back.

## The suite, lint and CI at the reviewed commit (CA2, CK2)

```
cmd  python -m pytest -q -p no:randomly          (mine, at 365fe3f, tree clean)
out  3346 passed, 2 warnings in 679.68s (0:11:19)
cmd  python -m ruff check floatfea tests scripts
     python -m black --check floatfea tests scripts
     python -m mypy floatfea
out  All checks passed! / 135 files would be left unchanged. /
     Success: no issues found in 37 source files
cmd  gh api .../runs/38121064579 --jq status,conclusion   then its /jobs   (head 365fe3f)
out  run 38121064579 head 365fe3f: status=completed conclusion=success
       the verification ladder   success   runner "GitHub Actions 1000001668"
       lint, unit and guards     success   runner "GitHub Actions 1000001669"
       CI determinism -- leg / ten legs agree   skipped  runner null
cmd  the same at 24282fa (run 38120436492)
out  status=completed conclusion=success ; both jobs success
```

**`3346` is `3345` plus exactly one, and the one is R796's case** -- counted from my own
runs at both commits, not by differencing yours. **I waited for HEAD's run a third time**:
`365fe3f` was `in_progress` with `lint, unit and guards` at `conclusion: null` while the
ladder had already gone green, which is exactly the state that would have read as a pass
from the job list alone. CK2 does not apply: no job in either run has `runner_name: ""`
with a payment annotation, and the two determinism jobs are `skipped` by their
`workflow_dispatch` condition.

## Next step opens when

**Nothing opens, and NO FOURTH CHECK IS NEEDED. Stated plainly, because you asked.**

**The reason is not that the tree is green -- it is that there is nothing left for a check
to read.** An interim check's substance under ES0 is the CZ0 (a)-(d) scan of the diff, and
you have committed that no further commit will touch `floatfea/` or `tests/`. A check whose
diff can only contain `docs/closure/F6a.md` is a check of prose that EQ0 already exempts
from review. **If one is forced anyway, it has no content, and saying so now is cheaper
than discovering it in a fourth verdict.**

1. **R793 is the only thing that ends the loop and it is with Xabier.** For the record, so
   the directive request carries its full cost: **three interim checks have now been forced
   by a `%03d` format string**, every one of them PASS, and the two findings they produced
   (R796, R797) came from attacking the repairs rather than from the scan the hook was
   asking for. The hook asked the right question three times for the wrong reason.
2. **R796 and R797 are answered. Nothing from this check goes on the ledger**, because the
   one residual above is verified rather than open, and I have numbered nothing new.
3. **The ledger stands at R788, R789, R790, R791** -- plus R793 pending its directive.

## Disagreement with the criterion -- none

Three attacks on R796's case and all three fail, which is the right outcome for a case
written to answer a finding about assertion level. The thing I would record about this
increment, if it is recorded anywhere, is that its last four findings were each in the
repair of the one before, and each was found by running the thing rather than reading it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: a522ae42e45f30f85ed509ae60a341f561abb2ae
Verdict: PASS
Tests: 3345 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q -p no:randomly`, 676.58s)

## SECOND INTERIM CHECK (ES0) of 2026-10-11 -- no new report revision, so this counts against NO round. **PASS.**

**Reviewed commit: `a522ae4` (HEAD).** Scanned `803c640..HEAD` -- `5485ed0`, `a522ae4`.
Light scope per ES0: the suite and CI at the commit, plus a CZ0 (a)-(d) scan. No corpus
batch, no closure list. **Nothing is (a)-(d).**

**Verified rather than taken, all five:**

```
cmd  git diff --stat 803c640..HEAD -- floatfea/tolerances.py
     git diff 803c640..HEAD | grep -nE "^[-+].*(_COUNTER|Final\[float\])"
out  (empty) ; (empty)
cmd  git log --oneline 803c640..HEAD -- .claude .claude/hooks docs/SUPERVISOR.md
     git diff --stat 803c640..HEAD -- tests/conftest.py 'tests/**/conftest.py'
     git log --oneline 803c640..HEAD -- docs/reports
out  (empty) ; (empty) ; (empty)
cmd  grep -cn "393\.9x\|442x\|4\.4x\|89x" floatfea/model/platform.py
     tests/verification/rung3/test_platform_skeleton.py
out  floatfea/model/platform.py:0
     tests/verification/rung3/test_platform_skeleton.py:0
judge **EU1 does not arise**: no value moves, no counter is declared or moved, and R794 is
      a deletion -- the grep is `0` at both sites, run by me. No STOP-class finding; no
      conftest, so no rung's green is read through new in-tree code; and no step report
      touched, so EK3 holds and neither EG3 boundary state exists.
```

## Carried

| item | status | what I measured |
|---|---|---|
| R793 | **still open, correctly, and not yours to close** | `.claude/hooks/` is untouched by both commits, which is the right action. It needs the directive. |
| R794 | **answered at both sites** | the figures are gone (`0` and `0` above) and what replaced them is the shape of the fact. The pointer that replaced them is R797. |
| R795 | **answered, and the case is non-vacuous -- I reproduced your measurement exactly** | `1 failed, 131 passed` with clause (1) deleted, and **R795's case is the only id that fires**. R796 is the level question you raised. |

## The two things you asked me to attack

**(1) THE LEVEL IS THE WRONG ONE, AND IT IS WORSE THAN YOU PUT IT -- R796 BELOW.** Not
because asserting on the predicate is wrong; because **nothing asserts that the guard calls
it.**

**(2) YOUR SECOND WORRY IS WRONG, IN THE SAFE DIRECTION. The construct is correct and I
measured it.** You wrote that if `_ROW` stops parsing that row shape "the case degrades into
a third test of clause (3) ... but it would still pass". It would not: it goes **red**.

```
claim  breaking `_ROW` makes R795's case FAIL, not pass
cmd    replace line 666 with `_ROW = re.compile(r"^XXNEVERMATCHESXX$", re.MULTILINE)`,
       then run `-k R795`
out    E       assert []
       tests/test_report_carried.py:869: AssertionError
       FAILED ...::test_R795_the_FIRST_CLAUSE_refuses_the_exemption_when_a_TABLE_PARSED
       1 failed, 127 deselected
rule   `assert cells, "this case depends on the row PARSING; if `_ROW` misses it the case
       is about clause (3) again and clause (1) is still unexercised"`
judge  **`assert cells` is an assertion, not a branch, so the double duty is exactly what
       a vacuity guard must do** -- it fails loudly and its message names the parser
       rather than the clause. There is nothing to repair here, and the worry is the
       right one to have had: a vacuity guard written as an `if ... return` instead of an
       `assert` is the defect you were describing, and this is not that.
```

## Findings

**Two. Neither is (a)-(d), and per FG6 both join R788/R789/R790/R791 in the artifact.**

**R796. (apparatus, FF0 class) All four cases pin `_is_the_sanctioned_empty_carry`, and
NOTHING pins the guard's use of it -- so R784's original defect is reintroducible with the
whole suite green.** This is your level question, measured.

```
claim  rewire the GUARD to the two-clause form R784 was raised about, leave the predicate
       completely intact, and nothing reddens
cmd    in `test_a_report_does_not_say_CLOSED`, replace
         `if _is_the_sanctioned_empty_carry(CARRIED, cells, EXPECTED):`
       with
         `if not cells and nothing_carried():`
       then the whole guard file, then the other guard file
out    132 passed in 1.60s          (tests/test_report_carried.py)
       25 passed in 0.03s           (tests/test_report_numbers_are_sourced.py)
cmd    grep -n "_is_the_sanctioned_empty_carry" tests/test_report_carried.py
out    731:def _is_the_sanctioned_empty_carry(       <- the definition
       786:        # The three clauses are ...       <- a COMMENT, not a call
       832, 840, 874, 902:                          <- the four counter-case assertions
rule   my own recorded guard: "Provenance, not existence. A pass/fail cannot show where a
       value came from ... asserted structurally, not inferred from a passing test."
judge  **`132 passed` with the guard carrying exactly the defect R784 named.** The three
       counter-cases certify a function the guard need not call, and the grep shows the
       predicate has ONE production call site and four assertion sites -- nothing between
       them. **No present defect**: the guard does call it, which is why my mutation had
       to change that line. But the cases' own domain excludes the thing they protect,
       which is assertion domain blindness at the level you suspected.
       **The test I would describe rather than write:** one case that reaches
       `test_a_report_does_not_say_CLOSED` itself with `CARRIED` and `EXPECTED`
       monkeypatched to the `contradictory` section and `[]`, asserting the guard goes
       red. That is a case in an existing gate, not new apparatus -- the same standing
       R795's case has. It is the only level at which "the exemption reaches the guard
       through this predicate" is a measurement.
```

**R797. (closure) Both pointers R794 installed claim `docs/closure/F6a.md` holds the
measurement "with its date", and that section carries no date.** Your own question about the
pointer, answered -- and the answer has a measurement under it.

```
claim  the referent resolves for the figures and the command, and NOT for the date
cmd    sed -n '384,412p' docs/closure/F6a.md
out    claim  the admissibility margin by body, over the span the gate asserts
       cmd    the reviewer's own 210-build sweep, reported in verdict 123
       out    platform   ... margin 393.9x
              hub1..4    ... margin   4.4x
cmd    sed -n '380,412p' docs/closure/F6a.md | grep -nE "2026|October|date"
out    (empty)
cmd    grep -n "docs/closure/F6a.md" floatfea/model/platform.py
       tests/verification/rung3/test_platform_skeleton.py
out    floatfea/model/platform.py:798:    # ... records what was measured once,
         with its date and its command
       tests/verification/rung3/test_platform_skeleton.py:807:
         `docs/closure/F6a.md` holds the measurement with its command and its date
rule   "Every citation resolves ... checked mechanically"
judge  **the figures and the triple are there; the date is not, at either pointer.** And
       the `cmd` field is "the reviewer's own 210-build sweep, reported in verdict 123" --
       a CITATION, not a one-line check a reader can run -- so "with its command"
       overstates what is there as well, more mildly. **This is the fourth iteration of
       one sentence in these two files** (R787 -> R794 -> this), each time a claim about
       where a measurement lives, and each time one command refutes it.
```

**My ruling on the pointer, which is what you asked for.** A **bare** pointer from
`floatfea/` to a closure artifact is NOT a CW0 claim I cannot check -- it is a path, it
resolves or it does not, and checking it is one grep I ran. **A pointer that inventories its
referent's contents IS one**, and that is what was written: "records what was measured once"
resolves; "with its date and its command" adds two properties of the referent and one of
them is false. **So the form is the pointer alone, with no inventory.** And I am not asking
for the figures back: moving a measurement out of `floatfea/` into a document that is
regenerated by rule is the right direction, and R794's repair is correct in direction and
wrong only in the clause it added on the way out.

**One residual, stated and not listed:** nothing mechanically ties either pointer to that
section of `docs/closure/F6a.md`, so if the section is ever edited the comment becomes a
false claim with nothing red. That is the same class as R790 and it has the same answer --
apparatus, frozen, F2a -- so I am recording it here rather than giving it a number.

## Tolerances touched

**None.** The two commands are in the verified block at the top: `floatfea/tolerances.py`
is untouched and the diff contains no `_COUNTER` or `Final[float]` line at all. **EU1 does
not arise**, and your reason is the right one -- R794 deletes two prose figures rather than
moving a value, so there is no configuration axis for an adversarial case to range over. I
checked the one thing a deletion could have been hiding: the figures are not re-stated
anywhere in `floatfea/` or `tests/` under a different spelling (`grep -cn` over both files
gives `0`, and `grep -rn "remainder_inertia" tests/` still finds only the mass-properties
helper at line 168 -- no test computes a margin, which is what makes the deletion the
correct repair rather than a loss).

## The suite, lint and CI at the reviewed commit (CA2, CK2)

```
cmd  python -m pytest -q -p no:randomly          (mine, at a522ae4, tree clean)
out  3345 passed, 2 warnings in 676.58s (0:11:16)
cmd  python -m ruff check floatfea tests scripts
     python -m black --check floatfea tests scripts
     python -m mypy floatfea
out  All checks passed! / 135 files would be left unchanged. /
     Success: no issues found in 37 source files
cmd  gh api .../runs/38118717740 --jq status,conclusion   then its /jobs   (head a522ae4)
out  status=completed conclusion=success
       lint, unit and guards     success   runner "GitHub Actions 1000001664"  14 steps
       the verification ladder   success   runner "GitHub Actions 1000001665"  13 steps
       CI determinism -- leg / ten legs agree   skipped  runner null  0 steps
cmd  the same at 5485ed0 (run 38118207969)
out  status=completed conclusion=success ; both jobs success
```

**`3345` is `3344` plus exactly one, and the one is R795's case** -- I ran both commits'
worth myself rather than differencing your numbers. **And I waited for HEAD's run again**:
`a522ae4` was `in_progress` with both jobs at `conclusion: null` when I first polled, so I
polled until `completed`. **Your correction took** -- reading the run-level `status` as well
as the job list is what the artifact now does, and it is the right fix. CK2 does not apply:
no job in either run has `runner_name: ""` with a payment annotation, and the two
determinism jobs are `skipped` under `if: github.event_name == 'workflow_dispatch'`, not run
by design.

## Next step opens when

**Nothing opens. FG6 stops work and this check exists because R793's hook demanded it.**

1. **R793 is with Xabier and is the only thing that ends this loop.** Both commits leave
   `.claude/hooks/` untouched, which is correct, and I confirmed it rather than taking it.
2. **R796 and R797 join R788/R789/R790/R791 in `docs/closure/F6a.md`**, per your own note
   that there is no next increment commit. R797 is one clause deleted from each of two
   comments. R796 is one case, and if it is never written the thing to record is the
   measurement: `132 passed` with the guard carrying R784's defect.
3. **R794 and R795 are answered.** R795's case is non-vacuous and fires alone; R794's
   deletion is complete at both sites and is the right direction.

## Disagreement with the criterion -- none

Both questions you raised were worth asking and the answers went opposite ways: the vacuity
guard needed no repair and the assertion level needed the finding you suspected. I have
nothing for Xabier beyond R793, which is already with him.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: 683f91012e45b0261faf2fc80662ecd06f444e1a
Verdict: PASS
Tests: 3344 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q -p no:randomly`, 672.51s, exit 0)

## INTERIM CHECK (ES0) of 2026-10-11 -- no new report revision, so this counts against NO round. **PASS.**

**Reviewed commit: `683f910` (HEAD).** Scanned: `810e979..HEAD` -- `7e94440`, `683f910`.

**Which clause I ruled under.** `CLAUDE.md` Â§ "Step gating": **ES0**, light scope -- the
suite and CI at the commit plus a CZ0 (a)-(d) scan of the diff since verdict 123. No corpus
batch and no closure list, per ES0's own words. **EU1 does not arise and I verified it
rather than taking it** (below). CA2/CK2 for the CI reading. EG3/FC1 for the boundary states
-- there are none. FF0 for the apparatus items. CW0 for the margin sentence, which is where
the one new finding in `floatfea/` comes from.

**Nothing is (a)-(d).** The suite is green with no exclusion, CI is green in both jobs at
HEAD, `floatfea/tolerances.py` is untouched, no gate assertion is weakened -- both are
measurably stronger -- and the two figures now in `floatfea/model/platform.py` are correct,
re-measured at HEAD rather than carried from the commit I took them at.

## Carried

**Verdict 123's seven items.**

| item | status | what I measured, not what the commit says |
|---|---|---|
| R786 | **answered, and verified by my own mutation at HEAD** | the failure branch now fails on its own `AssertionError`. **Both limbs of the `or` report, which the commit does not claim**: injecting a section term into `member_mass` gives `platform at D=2.0 t=5mm f 0.75 -> 0.75, member_mass 1.899599e+06 -> 1.875588e+06` (the mass limb), and raising `admissible()`'s floor to `3.5e7` -- between the hub span's `3.148e7` and `3.857e7` -- gives `hub1 at D=5.0 t=5mm f 0.75 -> 0.5, member_mass 1.125000e+06 -> 7.500000e+05` (the fraction limb). No `AttributeError` in either. |
| R787 | **answered in substance; its repair produced R794** | "by a margin asserted in" is gone from `floatfea/model/platform.py` and from the docstring, and `8.054e-05` is withdrawn for `7.994e-05` in `docs/closure/F6a.md:406-407`. What replaced the sentence is two figures with no mechanism behind them, which is R794. |
| R788 | **ledgered** | `docs/closure/F6a.md:416`. |
| R789 | **ledgered** | `docs/closure/F6a.md:417`. |
| R790 | **routed, and the entry is accurate** | `docs/milestones/F2a.md:287-310`, with the grep as its own `claim/cmd/out/rule` and labelled "a missing gate rather than a present defect", which is what I ruled. |
| R791 | **ledgered** | `docs/closure/F6a.md:418`, and it carries the two numbers that make the point (`1.405275e-04` against `1.405473e-04`). |
| R792 | **answered, and both my mutations still refute** | measured below. |

### The three things you asked me to look hardest at, ruled

**(1) R786's repair did NOT make the span assertion vacuous, and `len(sections) == 42`
still measures the span it claims.** I mutated it rather than reading it.

```
claim  the span assertion still bites after the tuple refactor
cmd    drop `0.600` from the wall tuple, then run the one test
out    >       assert len(sections) == 42, "the span this is asserted over is part of
                  the claim"
       E       AssertionError: the span this is asserted over is part of the claim
       FAILED ...::test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION
rule   a gate carries its own failure
judge  **not vacuous.** 6 diameters x 7 walls, none removed by `wall < 0.5 * d` (the
       largest wall is 0.600 against the smallest half-diameter 1.0), so 42 is the
       product and the assertion fires on any change to either tuple. The docstring's
       "walls from 5 mm to 600 mm, diameters from 2 m to 6 m" still describes it.
       And `Section`'s field list in the new docstring is EXACT, which I checked
       because I thought it was one short: `dataclasses.fields` gives
       `['A','I_y','I_z','J','shape']` and `kappa` is a method, not a field.
```

**(2) R792's repair did not weaken either case. Both mutations still refute, through the
production parser.**

```
claim  the two counter-cases still fail on the two mutations I ran in verdict 123, now
       that they call `_status_cells(section)` instead of a copy
cmd    baseline, as shipped
out    6 passed, 125 deselected      (and `5 status cells parsed, 0 say closed`)
cmd    MUTATION A: `return not outstanding` -> `return True`
out    FAILED ...::test_R784_the_SANCTIONED_SENTENCE_does_not_exempt_a_BROKEN_table
       1 failed, 5 passed
cmd    MUTATION B: `return not _LOOSE_MENTION.findall(section)` (my own rejected clause)
out    FAILED ...::test_R784_the_SANCTIONED_SENTENCE_does_not_exempt_a_BROKEN_table
       FAILED ...::test_R784_the_THIRD_CLAUSE_does_not_refuse_a_DECLARATION_THAT_NAMES_ITEMS
       2 failed, 4 passed
rule   the same two mutations, the same two ids, the same counts as at `09559f8`
judge  **identical to before: A reddens one case, B reddens both.** Routing through the
       real parser did not weaken either, and the reason it could not is that
       `_ROW.findall` is the only thing either case depends on and both helpers always
       called the same regex -- the risk R792 named was drift in the FUTURE, not a
       difference today. The default argument is the right repair: one parser, and
       `CARRIED if section is None else section` leaves the production call
       byte-identical in behaviour. **I also checked the one way this could have gone
       wrong -- `_status_cells("")` returns `[]`, as `_ROW_CELLS("")` did.**
```

**But one clause of the three has no counter-case, and that is new (R795).**

**(3) The margin sentence. YOUR QUESTION'S ANSWER IS YES -- IT IS NONE OF THE THREE -- AND
NO, NOT RE-DERIVING THEM WAS THE WRONG CALL, SO I DID IT.** Both halves measured.

```
claim  the two figures now in `floatfea/model/platform.py` are correct AT THE COMMIT THAT
       PUBLISHES THEM, not at the commit I took them at (CP3)
cmd    my own scratch script re-run at HEAD: 42 sections x 5 bodies = 210 builds, min
       eigenvalue of the symmetrised remainder inertia against
       `-MASS_PROPERTY_AGREEMENT * scale`
out    platform  min eig 4.655562287e+09 .. 4.667381836e+09  effect 1.181955e+07  margin 393.9x
       hub1..4   min eig 3.148139570e+07 .. 3.857312500e+07  effect 7.091729e+06  margin   4.4x
       smallest min-eigenvalue anywhere in the span: 3.148139570e+07 at D=6.0 t=0.005 (hub4)
rule   the comment's own claim: "`393.9x` on the platform and `4.4x` on the hub bodies,
       minimum at `D = 6.0 m, t = 5 mm` -- FG3's own corner"
judge  **correct, to every digit, at HEAD.** `7e94440` changes `build_superstructure` in a
       comment only, so nothing could have moved -- but that is an argument and this is
       the measurement, and CP3's whole point is that a figure correct when taken can
       describe a tree that has moved. You should have run it; it costs 40 seconds. R794
       is not that the figures are wrong.
```

## Findings

**Three. None is (a)-(d), and I say under each why.**

**R793. (apparatus, FF0 class, BUT IT NEEDS A DIRECTIVE AND YOU WERE RIGHT NOT TO TOUCH IT)
-- `.claude/hooks/require-verdict.sh:56` ranks `F6a` as `F6`, so the hook is anchored on F6
step 2's verdict and will refuse every turn that touches `floatfea/` or `tests/` for the
rest of this repository's life.** You reported the symptom; here is the mechanism, measured,
so whoever writes the `process:` commit has a diagnosis.

```
claim  which report the hook's own ranking picks, and why
cmd    the awk block from require-verdict.sh:56-65, run verbatim over
       `ls docs/reports/F*/step-*.md`
out    004 003 docs/reports/F4/step-3.md
       006 001 docs/reports/F6/step-1.md
       006 001 docs/reports/F6a/step-1.md      <-- F6a COLLIDES with F6 step 1
       006 002 docs/reports/F6/step-2.md       <-- and loses to F6 step 2 on `2 > 1`
cmd    the same pipeline's `sort | tail -1`, then the derived review and its stamp
out    report=docs/reports/F6/step-2.md
       review=docs/reviews/F6/step-2.md
       Reviewed commit: bf5fdf0adca9bfc46b477cec10f0a50132a495d4
cmd    printf 'docs/reports/F6a/step-1.md' | awk -F'[/-]' '{m=$3; sub(/^F/,"",m);
       printf "m=%s starts-with-digit=%s m+0=%d\n", m, (m ~ /^[0-9]/ ? "yes":"no"), m+0}'
out    m=6a  starts-with-digit=yes  m+0=6
rule   the hook's own comment at lines 50-56: "`F2a` and the like rank on their integer
       part, which is what `m+0` takes" -- stated as intended behaviour, and it is the
       defect
judge  **TWO sub-findings, and the second is the one that will outlive this.**
       **(i) A suffixed milestone COLLIDES with its base rather than sorting after it.**
       `F6a` and `F6` both rank `006`, so `F6/step-1` and `F6a/step-1` TIE EXACTLY at
       `006 001` and `sort | tail -1` would resolve that tie by path string. Even with no
       F6 step 2 the hook would pick between them by alphabetical accident.
       **(ii) EC0's loud-failure guard CANNOT SEE THIS.** The guard is
       `if (m !~ /^[0-9]/)` -- it checks that the field STARTS with a digit, and `6a`
       does. The defect is that the field is not ONLY a digit. That is assertion domain
       blindness: the collection the check inspects cannot contain the failure. EC0's own
       comment says "printing `000` for it is what let the defect survive: the ranking
       stayed plausible" -- and `006` for `F6a` is the same thing one notch less visible.
```

**And that it cannot be cleared, which is the half that makes it worth a directive:**

```
claim  no F6a verdict can clear the refusal, because the hook does not read one
cmd    git diff --quiet bf5fdf0 -- docs/reports/F6/step-2.md floatfea tests
       ':(exclude)tests/corpus'   (the hook's exact pathspec, at HEAD)
out    DIFFERS -> BLOCKS
       floatfea/model/platform.py                          |  52 ++++++-
       tests/test_report_carried.py                        | 153 +++++++++++++++-
       tests/verification/rung3/test_platform_skeleton.py  |  75 ++++++++++
rule   require-verdict.sh:166-170 blocks on that pathspec, and it runs BEFORE the
       `case $verdict in PASS) exit 0` branch -- so F6 step 2's PASS does not exempt it
judge  **the only thing that would clear it is reverting F6a's work**, which is EC0's
       recorded cost word for word: "this hook spent all of F3 anchored on F2 step 7's
       verdict ... the condition it blocks on -- 'changed since the verdict' -- could
       only be cleared by reverting F3's work." **That paragraph describes the state the
       repository is in right now**, with F6 for F2 and F6a for F3. The refusal also
       names `docs/reports/F6/step-2.md`, a report closed by a PASS two milestones' worth
       of verdicts ago, which is how a reader can tell at a glance that it is misaimed.
```

**You were right not to fix it, and FF0 does not override that -- I am ruling, not
agreeing out of politeness.** `CLAUDE.md` Â§ "The reviewer's own instructions are not edited
inside a step" puts `.claude/hooks/` behind "a standalone `process:` commit that cites the
directive asking for the change", and says a change inside a commit that also touches
`floatfea/` or `tests/` is **STOP-class**. `7e94440` touches both. There is no directive
asking for this change, so there was no permitted route, and you identified that correctly.
**Where FF0's "fixed in the next commit" meets the standalone-commit rule, the
standalone-commit rule is the specific one and it names its own consequence.** FF0 governs
*when* an apparatus item is fixed; it is not an authorisation to edit the one class of file
`CLAUDE.md` places behind a directive. **This needs a directive from Xabier, and R793 is the
number for it.** What that directive has to authorise is narrow: make the ranking sort a
suffixed milestone AFTER its base and refuse a tie, and make EC0's guard reject a field that
is not wholly numeric rather than one that merely does not start with a digit.

**Why it is not (a)-(d).** It is not in `floatfea/`, not a published deliverable, not a
tolerance, and not a gate assertion -- a hook is not a test. No test is red at HEAD. So it
does not block this check, and I am not manufacturing a HOLD out of something outside the
four heads. **It will block work mechanically until the directive lands, which is a
statement about the hook and not a verdict about the tree.**


**R794. (closure) `floatfea/model/platform.py:792-793` now carries `393.9x` and `4.4x`, and
under CW0 that is none of the three things a claim about this repository may be.** Your own
question, answered: **yes, it is none of the three.**

```
claim  the two figures are asserted by no test, sit in no triple the tree runs, and are
       derivable only from a verdict nothing reads
cmd    grep -rn "393\.9\|4\.4x\|442x" floatfea/ tests/ scripts/
out    floatfea/model/platform.py:792:    # (R787).** The margin is also not one number: it is `393.9x` on the platform and
       floatfea/model/platform.py:793:    # `4.4x` on the hub bodies, minimum at `D = 6.0 m, t = 5 mm` -- FG3's own corner. A
       tests/verification/rung3/test_platform_skeleton.py:796:    not to publish a margin here is a measurement: the reviewer's `442x` was the
       tests/verification/rung3/test_platform_skeleton.py:798:    `4.4x`, minimum at `D = 6.0 m, t = 5 mm` -- FG3's own corner. A figure in a
       (two corpus files match `4.4x` and `0442x` on unrelated numbers)
cmd    grep -rn "remainder_inertia" tests/ --include=*.py
out    tests/verification/rung3/test_platform_skeleton.py:168:    parts.append((body.remainder_mass, body.remainder_point, body.remainder_inertia))
rule   CW0: "A claim about this repository written in a comment, a docstring or a plan is
       one of three things: a test, a triple (`claim:`/`cmd:`/`out:`, run by
       `tests/test_tree_prose_consistent.py`), or deleted."
judge  **none of the three, and at TWO sites rather than one.** The grep is the finding:
       `test_platform_skeleton.py:796-798` is the docstring that says "A figure in a
       docstring is a report nothing regenerates" and it carries `442x` and `4.4x`
       itself, three lines later. Line 168 is a mass-properties helper; **no test
       computes an eigenvalue margin over a section span anywhere.**
       The figures are CORRECT -- I re-measured them at HEAD above -- and that is not
       the finding. The finding is BI3's own reasoning landing on this comment a third
       time: "A comment that carries measurements is a report that never gets
       regenerated unless something regenerates it." The sentence that stood here
       over-claimed a margin; the sentence replacing it publishes two margins whose only
       derivation is `docs/reviews/F6a/step-1.md`. Either they go and the comment says
       only what the test asserts -- that the outcome holds over the span -- or they
       become a triple. **R787 asked for the false sentence to go; it did not ask for
       these to be published.**
```

**And I nearly wrote this triple's `out` from memory and had it wrong by one file.** My
draft said "the comment itself, and nothing else". Running it found the docstring too. CP3's
ordering is why this one is right, and the species is the one this milestone keeps producing.

**R795. (apparatus, FF0 class) One of `_is_the_sanctioned_empty_carry`'s three clauses has
no counter-case: deleting `if cells: return False` reddens nothing.** It predates this diff
-- it is `35de6cb`'s, which I passed in verdict 123 without measuring this clause -- and I
found it only because you asked whether routing through the production parser weakened
anything.

```
claim  clause (1) of the three is unguarded
cmd    delete `if cells: return False` from `_is_the_sanctioned_empty_carry`, then run
       the whole file
out     tests/test_report_carried.py | 2 --
        131 passed in 1.59s
rule   a gate carries its own failure; R784's own two counter-cases pin clauses (2) and
       (3) and I measured both, twice
judge  **no present defect.** With `EXPECTED` non-empty, clause (3) refuses the exemption
       whatever clause (1) says, so clause (1) is load-bearing only when the verdict
       names no finding -- a milestone's first revision -- and in that state there is no
       item for a report to wrongly close. So it is defence in depth, not a hole. **But
       it is one third of a condition that has never been exercised, and the direction it
       fails in is the weakening one** (more reports exempt). This is R784's own shape one
       level down: a clause that reads green on the state it exists for. One case, the
       mirror of the existing pair -- real parsed cells plus the sentence plus an empty
       `outstanding` -- would pin it.
```

## Tolerances touched

**None, and EU1 is verified rather than taken -- which is what you asked.**

```
cmd  git diff --stat 810e979..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff 810e979..HEAD | grep -nE "^[-+].*(_COUNTER|COUNTER|Final\[float\]|tolerance)"
out  15:-verdict 122's item 6 reasoned that the closure commit would change no gate and no tolerance
     29:+122's item 6 reasoned that the closure commit would change no gate and no tolerance and
     46:+rule   EQ0: a closure commit that changes a gate or a tolerance is reviewed
     247:+    # R792: THE PARAMETER IS HOW A COUNTER-CASE REACHES THIS PARSE. R784's cases need
rule  EU1: an interim check whose diff moves a tolerance VALUE or a declared counter
      includes the adversarial case
judge **no value moves and no counter is declared or moved.** All four hits are the WORD
      in prose -- three in `docs/closure/F6a.md` quoting EQ0, one the word `COUNTER-CASE`
      in a new comment. So EU1 does not arise, and your reason for saying so is the right
      one: with no tolerance in the diff there is no configuration axis for an adversarial
      case to range over. **I ran the ladder-adjacent case anyway, for a different
      reason** -- `MASS_PROPERTY_AGREEMENT` is the constant R794's figures are measured
      against, and raising its effective floor to `3.5e7` is what exercised the
      `mass_fraction` limb under R786. That is a probe, not a tolerance change; the file
      is untouched and the tree was restored.
```

**And the three diffs my own definition asks for separately:**

```
cmd  git log --oneline 810e979..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
     git diff --stat 810e979..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py ; (empty)
cmd  git log --oneline 810e979..HEAD -- docs/reports
out  (empty)
```

**No STOP-class finding.** Neither commit touches a line of my instructions -- which is
exactly what R793 is about and why reporting it instead of repairing it was correct. No
conftest change, so no rung's green is read through new in-tree code (CH2/CI0/CJ0). **No
step report is touched, so EK3 is satisfied and neither EG3 boundary state exists** -- which
is why the suite below is green with nothing waived.

## The suite, lint and CI at the reviewed commit (CA2, CK2)

```
cmd  python -m pytest -q -p no:randomly          (mine, at 683f910, tree clean)
out  3344 passed, 2 warnings in 672.51s (0:11:12)
cmd  python -m ruff check floatfea tests scripts
     python -m black --check floatfea tests scripts
     python -m mypy floatfea
out  All checks passed!
     135 files would be left unchanged.
     Success: no issues found in 37 source files
cmd  gh api repos/:owner/:repo/actions/runs/38116312029 --jq '.status, .conclusion'
     gh api repos/:owner/:repo/actions/runs/38116312029/jobs
out  completed / success                                   (head 683f910)
     the verification ladder    success   runner "GitHub Actions 1000001661"
     lint, unit and guards      success   runner "GitHub Actions 1000001660"
     CI determinism -- leg               skipped  runner null  0 steps
     CI determinism -- ten legs agree    skipped  runner null  0 steps
cmd  the same, at 7e94440 (run 38115644910)
out  the verification ladder success ; lint, unit and guards success
```

**I WAITED FOR THE RUN AT HEAD RATHER THAN RECORDING AN UNFINISHED ONE AS A PASS.** When I
first polled it, `683f910`'s `lint, unit and guards` job had `conclusion: null` and the run
was `in_progress`; my own definition says a run that has not finished is not a pass, so I
polled until `completed`. It is green. The two determinism jobs are `skipped` under
`if: github.event_name == 'workflow_dispatch'` -- not run by design, which is neither red
nor CK2's third state: no job in either run has `runner_name: ""` with a payment
annotation. **`3344 passed, 0 failed, 0 skipped` is the whole suite with no exclusion and
nothing waived**, the three report-guard files included, and the two warnings are
`orient_norm_overflow`'s own designed overflow.

## The corpus (EG4(e))

**Not applicable: ES0 says an interim check runs no corpus batch, and I ran none.**
`git log 810e979..HEAD -- tests/corpus` is empty from both sides. The two exceptions the
pause keeps open -- F4's load-mapping gate and EB6's label-provenance gate -- are not
touched by either commit.

## Next step opens when

**There is no next step: FG6 stops work and this check exists because the hook demanded it,
not because there is increment work left.** The list, in the order I would act on it:

1. **R793 goes to Xabier as a directive request**, and the number is for whoever writes the
   `process:` commit. You have already put it to him; the diagnosis above is what that
   commit needs -- sort a suffixed milestone AFTER its base, refuse a tie rather than
   resolving it by path string, and make EC0's guard reject a field that is not wholly
   numeric instead of one that merely does not start with a digit. **Until it lands the
   hook refuses every turn touching `floatfea/` or `tests/`, and no F6a verdict can clear
   it.**
2. **R794 and R795 are FF0's class and go in the next commit if there is one** -- R794 is
   two lines of comment and one docstring paragraph, R795 is one counter-case. If FG6 means
   there is no next commit, both join R790 on `docs/milestones/F2a.md`.
3. **Nothing else.** Verdict 123's other five items are repaired, ledgered or routed, and I
   checked each at its named site rather than reading the commit message.

## Disagreement with the criterion -- none, and I am ruling FOR you on the one you raised

**You asked whether you should have fixed the hook under FF0 despite the standalone-commit
rule. No.** The reasoning is in R793 and it is a ruling, not a courtesy: FF0 governs *when*
an apparatus item is fixed, and `CLAUDE.md` Â§ "The reviewer's own instructions are not
edited inside a step" governs *who may touch that one class of file and in what commit*. The
second is the specific rule, it names its own consequence -- STOP-class -- and `7e94440`
touches `floatfea/` and `tests/`, so there was no permitted route. **Reporting it was the
only correct action available and you took it.** I have nothing for Xabier about the
criterion; R793 is about the apparatus and it goes to him as a directive request, which is
the channel `CLAUDE.md` already provides for it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: 09559f8f0afcc3ba1731de4ce92172140a901c3f
Verdict: PASS
Tests: 3344 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q -p no:randomly`, 667.64s, exit 0)

## Round of 2026-10-10 -- F6a, the EQ0 closure review. **PASS. The increment closes.**

**Reviewed commit: `09559f8` (HEAD).** The range is `1d2be7b..HEAD`: `35de6cb`, `740221d`,
`15bb18f`, `09559f8`.

**Which clause I ruled under.** `CLAUDE.md` Â§ "Step gating": **EQ0**, because `35de6cb`
changes a gate assertion and adds one, so this commit is reviewed; **EB4**, so it counts
against no step's rounds and FG1's one reviewed revision is intact. CZ0 (a)-(d) as amended
by EZ0, with FG1's restatement that a wrong figure in `results/F6a/` or in the script
producing it blocks. CA2 and CK2 for the CI reading (stated in my own definition, because
`CLAUDE.md` does not carry them). EG3/EH1/EJ2/FC1 for the boundary reds in the range.
EH4 for the boundaries. EG4(e) for the corpus. FF0 for the apparatus items. **ES0/EU1 do
not arise: no tolerance value and no declared counter moved anywhere in the range.**

**The implementer was right and verdict 122's item 6 was wrong.** Item 6 reasoned the
closure commit would change no gate. `35de6cb` changes
`test_a_report_does_not_say_CLOSED`'s exemption condition and adds
`test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION`. EQ0 applies on its own
terms. **Item 6 is withdrawn**, and the asking was worth it: this review found the items
below, two of them in the repair of a repair, and one of them a correction to a figure I
published myself.

## Carried

**Every open item of verdict 122, with its status. Five findings and five closure items.**

| item | status | where, and what I measured |
|---|---|---|
| R781 | **answered** | report Â§ 2. The provenance sentence now reads "No MEASURED figure is typed into this document or its generator -- what is written literally is the declared inputs and the clause's own constants". I audited the enumeration rather than taking it: all 20 digit-bearing string literals in `scripts/measure/f6a_report.py` are a path, a column header, a clause number (`3.2.2(b)`, `3.2.3`, `3.3.1`, `3.3.2`), a declared input (FG3's `2.5 m`/`180 mm`, heading `0Â°`, `K = 2.0`, `F_y = 355 MPa`, `0.75 F_y`), a decision threshold (`1.0`, `max U = 1`) or a label. **The claim holds as scoped.** The three premise figures are now in `results/F6a/premise_check.json` and read from it. |
| R782 | **answered, and with more than I asked for** | `dynamic_half` at `scripts/measure/f6a_premise_check.py:156` re-solves the increment at both sections, runs at all three searches x two groups, and the docstring states what the file does. Its `max U` is taken over **every step** of the governing periods, which is verdict 122's own adversarial case, now in the repository and reproducing my figures to the digit. R788 is the residual. |
| R783 | **answered** | The continuum requirement `W_req = 1.215739 mÂ³` and the bending fraction `99.98595%` are published; the six-figure agreement is named as `4.2e-04` of one grid step. **And my own `8.054e-05` is withdrawn** -- see R787(b). |
| R784 | **answered, and my own closing condition is refuted** | The substitution is right and I measured it in both directions. Ruling below. R792 is the residual. |
| R785 | **answered** | `--milestone` takes a label. `_milestone` accepts `6`, `6a`, `F6a`, refuses anything else, `re` is imported, and the value becomes the path segment at lines 99/103/105. **I wrote this file with `--milestone 6a` and nothing patched.** |
| C98 | **fixed** (`35de6cb`) | and checked against my own recomputation of the sweep, not against the report's. |
| C99 | **fixed** (`35de6cb`) | the claim moved from a comment into a test, which is CW0's own route. R786 and R787(a) are the residuals. |
| C100 | **fixed** | the fence count is 38 and the fences balance. |
| C101 | **fixed** | `EIGHTEENTH` became `SEVENTEENTH` at line 270. |
| C102 | **fixed** | the restated column is gone from the document I read; the grep count is 0. |
| HOLD item 4 | **UNVERIFIABLE BY ME, and recorded as such** | "the corrected deliverable is re-sent to Xabier". `docs/closure/F6a.md:115-116` states it -- "Sent to Xabier twice: the first version on 10 October, the corrected version the same day, with a PDF rendered outside the repository." Nothing in this repository can refute that. It is the one item of the HOLD I am taking on the implementer's word, and I am saying so rather than counting it answered. |
| HOLD item 6 | **withdrawn, by me** | its premise was false. See above. |

**On my own instruction 1b.** The newest revision's header is `Answers: verdict 122 @
1d2be7b` and verdict 122 at `1d2be7b` is the latest verdict. One comparison, correct.

## Findings

**Nothing blocks. Every one is a closure item, an apparatus item, or one line for F2a's
frozen list, and I say under each why it is not (a)-(d) rather than leaving the class
implied.**

**R786. (closure) `tests/verification/rung3/test_platform_skeleton.py:813` -- the new gate's
ONLY failure branch raises before its assertion.** The assertion is sound and the gate does
detect the defect. What it cannot do is say what it caught.

```
claim  break the property the gate claims and the gate reddens -- but not through its
       assertion
cmd    inject a section term into `_build_body`:
         member_mass = fraction * deck_mass * (1.0 + 0.01 * section.A)
       then run the one test
out    E   AttributeError: 'Section' object has no attribute 'd_outer'
       tests/verification/rung3/test_platform_skeleton.py:813: AttributeError
       FAILED ...::test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION
cmd    python -c "from floatfea.model.material import Section; print([f for f in
       dir(Section.circular_tube(2.5,0.18)) if f[0]!='_'])"
out    ['A', 'I_y', 'I_z', 'J', 'circular_tube', 'kappa', 'shape']
cmd    grep -rn "[.]d_outer" floatfea/ tests/ scripts/ --include=*.py | grep -v "d_outer_m|d_outer="
out    tests/verification/rung3/test_platform_skeleton.py:813
       scripts/measure/f6a_required_section.py:68,69,73,74,78,82,90,346,371
rule   my own recorded guard: "A gate carries its own failure: break the claimed property
       and confirm the assertion goes red." It goes red; the assertion does not run.
judge  `d_outer` is `f6a_required_section.py`'s own `Candidate` attribute, not
       `floatfea`'s `Section` -- the diagnostic was written against the wrong class.
       **And it cannot be fixed by renaming**: `Section` does not record `D` or `t` at
       all, so the repair is to carry `(d, t)` from the loop. The failure mode is
       specific: a real mass-basis change presents in rung 3 as an `AttributeError`,
       which under the ladder's own discipline reads as a stale test, and the natural
       repair makes the red disappear into a message nobody reads. **The assertion
       message -- "the chosen mass fraction or the member mass moved with the measurement
       section" -- has never been printed and cannot be.** Nobody broke the property and
       watched it go red, which is the whole of why this is here.
```

**Why it is not (c).** CZ0 (c) is "a gate assertion -- what a gate claims, on which
quantity, at what threshold", and all three are intact: `assert not moved`, on the chosen
fraction and the member mass, at exact equality. What is broken is the path to it. CZ0 puts
guards and apparatus in the closure list and I am not smuggling this one past that. **I did
consider blocking** -- my definition's carve-out covers "a generator whose output *is* a
gate's assertion" -- and an f-string inside a failure branch is not that.

**And two sentences around it, one of them in `floatfea/`:**

```
claim  the docstring says the eigenvalue margin is printed, and nothing prints it
cmd    python -m pytest ".../test_platform_skeleton.py::test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION" -q -s
out      42 sections x 5 bodies: 0 mass changes
       1 passed in 3.09s
rule   the test's own docstring: "The eigenvalue margin is printed so a future reader can
       see how much room the answer has rather than taking the word 'cannot'."
cmd    sed -n '783,785p' floatfea/model/platform.py
out    # **The section reaches the mass decision.** It does not change it, by a margin
       # asserted in `tests/verification/rung3/test_platform_skeleton.py`, by
       # `test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION`
judge  **no margin is printed and no margin is asserted anywhere.** Both sentences are
       CW0-class claims about the code, one of them in `floatfea/`, in the repair of a
       CW0 finding (C99) that was itself in that comment. Per CW0 each is a test, a
       triple, or deleted. The quantity they promise is R787.
```

**R787. (a) A CORRECTION TO VERDICT 122, MEASURED -- MY OWN `442x` IS WRONG BY TWO ORDERS
OF MAGNITUDE ON THE BINDING BODY; AND (b) MY `8.054e-05` IS WITHDRAWN.** This is the item I
would most want read, and it is about my record rather than the implementer's.

**(a) The margin.** Verdict 122's C99 cell printed "the platform remainder-inertia
eigenvalues" and concluded "the margin is 4.6558e+09 against a 1.0523e+07 section effect --
**442x** -- so the behaviour is safe by a wide measured margin". I swept one body of five.

```
claim  admissible()'s margin on EVERY body, over the test's own 42-section span
cmd    my own scratch script: 42 sections x 5 bodies = 210 builds of the superstructure;
       at each, the min eigenvalue of the symmetrised remainder inertia against the
       boundary `-MASS_PROPERTY_AGREEMENT * scale` that `admissible()` tests
out    body       min eig range                   section effect  dist-to-boundary  margin
       platform   4.655562e+09 .. 4.667382e+09    1.181955e+07    4.655562e+09      393.9x
       hub1       3.148140e+07 .. 3.857313e+07    7.091729e+06    3.148140e+07        4.4x
       hub2       3.148140e+07 .. 3.857313e+07    7.091729e+06    3.148140e+07        4.4x
       hub3       3.148140e+07 .. 3.857313e+07    7.091729e+06    3.148140e+07        4.4x
       hub4       3.148140e+07 .. 3.857313e+07    7.091729e+06    3.148140e+07        4.4x
       smallest min-eigenvalue anywhere in the span: 3.148140e+07 at D=6.0 t=0.005 (hub4)
rule   `admissible()`: `m_r >= 0` and `min eig(J_r) >= -MASS_PROPERTY_AGREEMENT * scale`,
       with `MASS_PROPERTY_AGREEMENT = 1e-13`, so the boundary is -3.125e-05 and the
       margin is the distance to zero divided by the span's full excursion
judge  **4.4x, not 442x.** The platform is the loosest body by a hundredfold and it is the
       one I measured. **Nothing flips anywhere in the span, so no F6a answer moves** --
       and the sentence a future caller would have read was two orders of magnitude
       optimistic about how much room there is. This is R755, this milestone's first
       blocking finding, in my own verdict one round later: a figure right about the axis
       its author swept and silent about the four with the answer on them.
cell   one variable moved: which body the eigenvalue is read from. Same 42 sections, same
       builds, same boundary.
```

**So the implementer's choice -- assert the outcome, not the margin -- was the right one,
and for a reason stronger than the report gives.** C99 offered "state the measured margin
(442x)" as the first of two options. **Taking that option would have published a figure
wrong by 89x on the governing body**, in `floatfea/`, under my own name. The implementer
took the option that did not inherit my error. The answer to the invocation's question is
therefore: asserting the outcome is correct, and the only thing missing is that the comment
and the docstring still promise a margin (R786).

**And the span is the right span, checked rather than assumed.** The test's corner is
`D = 6.0 m, t = 5 mm`, which is exactly the corner of FG3's own grid, and it is the corner
that minimises the hub eigenvalue -- so the 4.4x is measured where the span is tightest and
not at a convenient interior point. Outside the span nothing is reachable: at `D = 20 m`
`check_limits` refuses at `L/D = 1.250` before `admissible()` is consulted at all.

**(b) `8.054e-05` is withdrawn in favour of `7.994e-05`.** The report attributes the
difference to "the bisections differ in their last digits". It is simpler than that, and it
is mine.

```
claim  the exact spread, recomputed from the two W* the deliverable publishes
cmd    my own scratch script: abs(1.2159102795078853 - 1.2160074798261564)
       / 1.2159102795078853
out    7.994037052670982e-05   -- the published figure, to every digit
rule   their bisection endpoints and mine are the same number: `t* = 406.49845 mm`,
       `D* = 3.193772 m`. With the same endpoints the spread cannot differ.
judge  **`7.994e-05` is derivable from the published pair and `8.054e-05` is not.** It was
       a normalisation slip in verdict 122, not a bisection difference, and the
       deliverable carries the right one. Nothing downstream moves: the conclusion is the
       same at either and it is still 31x the grid agreement.
```

**R788. (closure) `results/F6a/required_section.md` Â§ (vi): the dynamic block's "worst
component rel" does not name its quantity, and the quantity the search actually reads moves
by `6.9e-01`.** Ruling on the invocation's item 7: **a real distinction, not a narrowing.**

```
claim  what `worst_component_relative_change` is a change IN
cmd    sed -n '200,215p' scripts/measure/f6a_premise_check.py
out    store[key] = (total if prev is None
                     else np.where(np.abs(total) > np.abs(prev), total, prev))
       ...
       rel, where, abso, _ = _worst_change(stores["shipped"], stores["sized"])
rule   `store[key]` is the componentwise max-abs over every step, so its components may
       come from different instants. It is a per-component ENVELOPE.
judge  mine (`6.860008e-01`) is the change in the GOVERNING ROW when the instant selection
       is re-run; theirs is the change in the envelope under a fixed selection rule. Two
       different quantities, and the report's Â§ 2 says so in exactly those words. **The
       deliverable does not**, and the deliverable is the file Xabier has: a reader of
       "the forces do move ... worst component rel 5.692647e-05" has no way to know that
       the row the search reads moves four orders of magnitude further.
```

**Why it is not (a).** The figure is correct for what it measures, and the load-bearing
claim beside it -- `max U` -- is both the right quantity and published on the right basis.
**The right basis is stronger than the search's own:**

```
claim  the script's `max U` is taken over EVERY step, not at the stored sigma-peak instant
cmd    sed -n '208,212p' scripts/measure/f6a_premise_check.py
out      u = _u_of(cands[group], total, lengths[member.label])
         if u > best.get(group, -1.0): best[group] = u
rule   verdict 122's adversarial case was precisely this: the stored basis keeps one row
       per station where `sigma` peaks, and `sigma` is not `U`
out    the deliverable now publishes, at answer (i), `platform 0.995702`, `hubs 0.989907`
       -- identical to the figures I measured over 4081 steps x 5 bodies x 16 members x 3
       stations in verdict 122; and at (iii) `hubs 0.991135 -> 0.991139`, also identical
judge  **my adversarial case is now in the repository and it reproduces to the digit.**
       That is the strongest statement anyone has made about these six answers and it is
       no longer only in a verdict. The missing sentence is one line.
```

**R789. (closure) Measured figures typed in `scripts/measure/f6a_required_section.py`, which
is inside EZ0's phrase -- R781's species, one file upstream.** No defect today; nothing ties
them.

```
claim  the search's answers are typed into the script that computes two published figures
cmd    sed -n '429,434p' scripts/measure/f6a_required_section.py
out    "published_spread_relative": abs(
           Candidate(2.5, 0.410).section_modulus - Candidate(3.2, 0.180).section_modulus)
           / Candidate(2.5, 0.410).section_modulus,
       "grid_step_W_at_D_2.5": Candidate(2.5, 0.410).section_modulus
           - Candidate(2.5, 0.405).section_modulus,
cmd    my own scratch script: W from my own tube algebra at (2.5,0.410) and (3.2,0.180),
       compared bit-for-bit with the two published `W_m3`
out    (2.5,0.410) W = 1.2211589864838892  matches answer (i)  : True
       (3.2,0.180) W = 1.2211621186517647  matches answer (ii) : True
rule   `t = 0.410` and `D = 3.2` are the ANSWERS of searches (i) and (ii), not declared
       inputs. `2.5` and `0.180` are FG3's.
judge  correct today and correct to the last bit, which is why it is a closure item and
       not (a). But if an answer moved, `2.565e-06` and `4.2e-04` would be published as
       "the two GRID answers" about a section that is not an answer, and the sentence
       would be false with nothing red. One line: read `t_m` and `D_m` from `found`.
```

**Same species, two lines further on:** `continuum["grid_t_step_m"] = 0.005` and
`grid_D_step_m = 0.1` at lines 521-522 are typed, while `grid_D_max_m = max(D_STEPS)` and
`grid_D_min_m = min(D_STEPS)` on the two lines **above** are derived. The grid steps are two
of the figures the deliverable now reads from the JSON per the invocation's item 6, so they
reached the document from a literal that must agree with `_frange(0.005, 0.600, 0.005)` and
`_frange(2.0, 6.0, 0.1)` and nothing checks that it does.

**R790. (one line for `docs/milestones/F2a.md`, and NOT a request for new apparatus)
`results/F6a/` is under no regeneration gate, and F6's is -- which is the gate that caught
the one stale figure this increment shipped.**

```
claim  F6's deliverable has a regeneration gate and F6a's has none
cmd    grep -rn "required_section|F6a" tests/regression/*.py
out    (empty)
cmd    grep -rln "F6a" tests/ --include=*.py
out    tests/test_report_carried.py
       tests/verification/rung3/test_platform_skeleton.py
rule   `tests/regression/test_f6_deliverable_agrees_with_itself.py::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`
       is what reddened the ladder at `35de6cb` and nothing else did
cmd    python scripts/measure/f6a_required_section.py && python scripts/measure/f6a_report.py
       && git diff --stat -- results/F6a/ && git status --porcelain
out    (empty, both) -- CRLF warnings only; no tracked content differs
judge  **there is no defect today: the deliverable regenerates byte-identically at HEAD,
       and I ran it rather than reading the report's claim of it.** The finding is the
       asymmetry. A figure in F6's report going stale is caught by CI; the same class of
       staleness in F6a's own deliverable, which is the increment's entire output and is
       in Xabier's hands, is caught by nothing. `CLAUDE.md` forbids me asking for the
       apparatus -- "No new apparatus through F6 ... a finding that needs one goes onto
       [F2a's] list" -- so this is a line on that list and not a condition. I checked:
       `grep -n "F6a|regeneration|R756" docs/milestones/F2a.md` is empty, so it is new.
```

**R791. (closure, low) The continuum block publishes three numbers for the same requirement
and recommends the smallest without saying why they differ -- though the number that
explains it is already on the line above.**

```
claim  the gap between the pure-bending requirement and the exact inversion IS the
       published bending fraction, and the document never says so
cmd    python -c "from the JSON: (exact_W_at_D_2.5 - W_req_continuum)/W_req_continuum,
       and 1 - bending_fraction_of_U"
out    gap                    = 1.405473e-04
       1 - bending fraction   = 1.405275e-04
rule   R783's closing condition: "the deliverable publishes the continuum requirement and
       the bending fraction -- the two numbers that ARE the mechanism"
judge  **the pair R783 asked for is complete and exact to four figures, which is better
       than the condition required** -- `W_req = 1.215739` ignores the axial term and
       `99.98595%` is precisely the size of what it ignores. Only the sentence joining
       them is absent, so a reader sees `1.215739`, `1.21591028` and `1.21600748` for one
       quantity and is told to transfer the lowest. Nothing is wrong; one clause is
       missing.
```

**R792. (apparatus, FF0 -- fixed in the next commit, not ledgered) `_ROW_CELLS` is a
byte-for-byte duplicate of `_status_cells`'s body and nothing keeps the two in sync.**

```
claim  the two parsers are the same code twice
cmd    diff the body of `_status_cells` (tests/test_report_carried.py:710-724) against
       `_ROW_CELLS` (727-741)
out    identical but for `CARRIED` -> `section` and
       `cells = [c for c in rest.split("|")]` -> `cells = list(rest.split("|"))`
rule   the invocation asked: "check it is not a second parser that can drift from
       `_status_cells`"
judge  it is one, and it can. If `_status_cells` changes -- it has changed at least twice,
       per its own docstring on the third column and CH4 -- the two R784 counter-cases
       keep measuring a parser the production path no longer uses, and they would stay
       green while doing it. **The repair is `_status_cells(section: str | None = None)`
       defaulting to `CARRIED`**, which is a repair and not an extension (EK2). The
       counter-cases' own non-vacuity asserts (`not _ROW.findall(broken)`,
       `_LOOSE_MENTION.findall(honest)`) are good and do not cover this.
       **If FG6 means there is no next commit, this goes on F2a's list with R790.**
```

### The things the invocation asked me to attack, ruled

**(1) R784's third clause. THE SUBSTITUTION IS RIGHT AND MY OWN CLOSING CONDITION IS
REFUTED BY BOTH COUNTER-CASES, IN TWO DIRECTIONS.** I did not take this from the report; I
mutated the function.

```
claim  the counter-cases are not vacuous -- revert the repair and the case reddens
cmd    MUTATION A: `return not outstanding` -> `return True` (the two-clause version R784
       named), then the two R784 ids plus `test_a_report_does_not_say_CLOSED`
out    E  AssertionError: the exemption fired with a finding outstanding, on a section
          carrying three rows the parser cannot read, one of them saying CLOSED.
       FAILED ...::test_R784_the_SANCTIONED_SENTENCE_does_not_exempt_a_BROKEN_table
       1 failed, 5 passed
rule   a gate carries its own failure
judge  non-vacuous, and it reddens on state B of verdict 122's own cell.
```

```
claim  MY condition -- "no finding mentioned in the section at all" -- is worse, and
       measurably
cmd    MUTATION B: `return not _LOOSE_MENTION.findall(section)`, the clause verdict 122's
       `Closed when` asked for
out    FAILED ...::test_R784_the_SANCTIONED_SENTENCE_does_not_exempt_a_BROKEN_table
       FAILED ...::test_R784_the_THIRD_CLAUSE_does_not_refuse_a_DECLARATION_THAT_NAMES_ITEMS
       2 failed, 3 passed
rule   EH4: every boundary is solved in BOTH directions, including the ones that weaken
judge  **my clause fails BOTH cases, in opposite directions.** It refuses the honest
       declaration that names what it is not carrying -- which is the shipped revision 1,
       and which the implementer measured before adopting anything -- AND it refuses the
       flip-back half of the first case. `CLAUDE.md` says a guard that fails false is
       fixed or deleted rather than lived with; mine would have failed false on the first
       input it met. **The implementer was right to substitute and right to say so.**
```

**And the weakening direction of the new clause, converted from an argument into a
measurement, because the report argues it.** The report's case for `not EXPECTED` is that
the verdict is hook-protected and prose is not. That is true and it is the right reason. But
the exemption is reachable by emptying `EXPECTED` instead of emptying `cells`, so I checked
whether an empty `EXPECTED` is itself caught:

```
claim  can a report reach the exemption with something outstanding, through EXPECTED?
cmd    my own scratch script: import the module, call `_is_the_sanctioned_empty_carry` on
       a broken section with EXPECTED real and with EXPECTED forced to []; then plant a
       verdict text with no `**R<n>.` heading and call
       `test_the_parse_found_something_to_check`
out    live tree:  EXPECTED = ['R781','R782','R783','R784','R785'];  cells = 5
                   exemption fires on the SHIPPED report: False
       broken section, real EXPECTED      : False
       broken section, EXPECTED = []      : True   <-- reachable this way
       planted verdict with no heading    -> EXPECTED would be []
       test_the_parse_found_something_to_check: RED -- "no `**R<n>.` finding heading
         parsed from the verdict -- the format changed and every assertion below would
         pass on anything"
rule   EH4, the direction that weakens the gate
judge  **the composition holds and it is now measured.** The only route to the exemption
       with something outstanding requires making a different, non-vacuous guard red. The
       production path is live at this commit -- 5 cells parsed, 0 saying `closed`,
       exemption not fired -- so the exemption is not silently swallowing this report.
       One recorded dependency, pre-existing and not this round's: a genuinely
       zero-finding verdict would redden `test_the_parse_found_something_to_check` on a
       legitimate state, which is R586's shape. It has not occurred and I am not asking
       for it to be changed.
```

**(2) C99's test. `admissible()` IS consulted on all 42 builds, the test is non-vacuous as
a regression guard, and no flipping section is reachable in the span.** Ruled in R786/R787.

```
claim  the measurement section reaches `admissible()` rather than being swapped in after
       the fraction is chosen
cmd    sed -n '837,849p' floatfea/model/platform.py
out    for fraction in MASS_FRACTION_LADDER:
           candidate = _build_body(name, geometry[name], bodies[name], fraction,
                                   (measurement_sections or {}).get(name, section), ...)
           if admissible(candidate): built.append(candidate); break
rule   the invocation's question: "whether `admissible()` is actually consulted on those
       builds"
judge  **it is -- the section goes into `_build_body` INSIDE the ladder loop**, so every
       rung is tested at the measurement section, and the comment's new mechanism
       sentence is true. 42 is the right span: `len(sections) == 42` is asserted, and the
       corner `D = 6.0, t = 5 mm` is both FG3's own corner and the hub eigenvalue's
       minimum. A flipping section is NOT reachable in the span -- margin 4.4x at the
       tightest body -- nor outside it, where `check_limits` refuses at `L/D = 1.250`
       before `admissible()` runs. **The gate is a regression guard on the shipped
       behaviour and a good one; mutation A above shows it detects. R786 is that it
       cannot report.**
```

**(3) C98's boundary sweep and the monotonicity sentence. The replacement sentence is
right, the crossing claim is EXACTLY right, and I checked both against the sweep rather than
against the report.**

```
claim  every shape and crossing figure the deliverable publishes, recomputed from the
       sweep rows
cmd    my own scratch script over `boundary_sweep`, both groups
out    platform: steps 36 (theirs 36) | rises 9 (9) | largest rise 2.378121% (2.378121%)
                 fall 0.665533 (0.665533)
       hubs    : steps 40 (40) | rises 18 (18) | largest rise 3.316750% (3.316750%)
                 fall 0.628115 (0.628115)
       platform: max D with ratio>1 = 4.9 ; min D with ratio<=1 = 5.0
                 SINGLE CROSSING: all D>4.9 are <=1 -> True ; all D<5.0 are >1 -> True
       both    : min-A-at-or-below-the-bound monotone non-increasing -> True
rule   `max U <= 1.0` with `refused == 0`, the search's own rule
judge  **"above 1.0 up to and including D = 4.9 and at or below it from D = 5.0" is true
       of every one of the 37 passing rows, not just of the two extremes** -- I checked
       the whole range in both directions because the two JSON fields the sentence is
       built from (`largest_D_with_ratio_above_1`, `smallest_D_with_ratio_below_1`) would
       print a self-contradictory sentence on a double crossing and nothing asserts there
       is only one. There is only one. **My own (f) ruling said "between D = 4 and D = 5"
       and 4.9 is the sharper answer; 4.9 supersedes it.** And the two sequences are
       correctly distinguished: the per-D sequence is not monotone (9 of 36, 18 of 40)
       and the min-at-or-below-the-bound sequence is, which is exactly what the
       replacement paragraph claims and not what the first one did. **The implementer
       caught its own instance of this milestone's recurring species, in its own repair,
       by running the check the sentence implied.** That is the right reflex and it is
       worth saying so.
```

**(4) R756's red. The record in the repository is right; THE INVOCATION'S SUMMARY TO ME IS
NOT, and the ladder red is on the other commit.**

```
claim  which commit shipped the ladder red
cmd    gh run list --limit 20 --json headSha,databaseId,conclusion ; then
       gh api repos/:owner/:repo/actions/runs/<id>/jobs for each
out    35de6cb  lint, unit and guards FAILURE | the verification ladder FAILURE
       740221d  lint, unit and guards FAILURE | the verification ladder SUCCESS
       15bb18f  both SUCCESS
       09559f8  both SUCCESS
rule   the invocation says "At `740221d` CI was red in two jobs: 13 boundary ids in
       `lint, unit and guards`, and one in `the verification ladder` which was R756's
       gate"
judge  **the ladder was red at `35de6cb` and green at `740221d`**, which is the correct
       chronology: `35de6cb` added the test and made the count stale, `740221d` repaired
       it. `docs/reports/F6a/step-1.md` Â§ 0a lists `test_R756_...` under run
       `38110136837` at `35de6cb`, and Â§ 7 and `docs/closure/F6a.md` Â§ 0 both say "RED
       one commit earlier" / "RED at the previous commit". **The artifacts are right and
       the invocation merged the two commits.** Recorded because my definition says a
       claim I cannot locate in the diff or the test output is recorded -- here I located
       its refutation, and the refutation exonerates the record.
```

```
claim  nothing but the count moved in F6's deliverable, and the CSVs are byte-identical
cmd    git diff --stat 35de6cb..740221d -- results/F6/
       git diff 35de6cb..740221d -- results/F6/floatfea_results_report.md
out    results/F6/floatfea_results_report.md | 2 +-   (one file, one line)
       -  G3.1a            53 passed
       +  G3.1a            54 passed
cmd    python -m pytest tests/verification/rung3/test_platform_skeleton.py -q -p no:randomly
out    54 passed in 3.27s
rule   the G3.1a row of `scripts/measure/f6_results_report.py:95-100` counts the WHOLE
       file `tests/verification/rung3/test_platform_skeleton.py`
judge  **confirmed, both halves.** One file, one line, one count, and `54` is pytest's own
       number at this tree. No engineering figure moved and no CSV was touched at all --
       the `--stat` names one file, so byte-identity of the CSVs is not a claim I have to
       take on anyone's word.
```

**(5) The deliverable's new content. Every figure reproduces, several from my own algebra,
and the published sentence uses the denominator it names.**

```
claim  the continuum block, recomputed independently of the search
cmd    my own scratch script: tube properties from A = pi/4(D^2 - di^2) and
       W = (pi/64)(D^4 - di^4)/(D/2), with no import of f6a_required_section
out    quantity                      mine                     published
       published_spread_relative     2.564914077671898e-06    2.565e-06   (identical)
       grid_step_W_at_D_2.5          0.00751490364838614      0.007515    (identical)
         as a fraction of the answer 0.006153910941624376
         spread / that step          4.1679e-04               "4.2e-04"
       exact_spread_relative         7.994037052670982e-05    7.994e-05   (identical)
       W_req = M_res / F_b           1.215739410615924        1.215739
       0.75 * 355 MPa                266250000.0              266.25 MPa
       bending_fraction_of_U         0.9998594724505246       99.98595%
rule   the sentence names its denominator: "one grid step in W at D = 2.5 m is
       0.007515 m^3, so that agreement is 4.2e-04 of ONE step"
judge  **it is the denominator the sentence names.** And I found the draft's error the
       invocation asked about: dividing the same spread by the `t = 180 mm` search's
       D-step in W (`0.08144670`) gives `3.845665589633503e-05`, which is the `3.85e-05`
       the closure artifact records as corrected. One grid, one step, the right one.
       `M_res = 3.236906e+08` is `hypot(My, Mz)` at the row I measured independently in
       verdict 122 (`My = 1.8018e+08`, `Mz = 2.6890e+08` -> `3.2369e+08`).
```

**(6) R781's enumeration.** Audited above and recorded in `Carried`. Two notes inside the
sentence's own carve-out and not against it: `F_y = 355 MPa` is typed at
`f6a_report.py:399` while line 72 reads `FY_S355`, and `K = 2.0` is typed at line 73 beside
`CM_JOINT_TRANSLATION` read from `floatfea.checks.api_wsd`. Both are declared inputs and the
sentence permits those literally. `K` is not a named constant anywhere in `floatfea`, so
typing it is the only option; `F_y` is, and reading it twice from one place would cost one
character.

**(7) R782's dynamic half.** Ruled in R788: a real distinction, not a narrowing, and the
basis published is stronger than the search's own.

## Tolerances touched

**None, across the whole increment, and I checked it as its own diff rather than taking the
report's statement.**

```
cmd  git diff --stat ca611e3..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 1d2be7b..HEAD -- tests/conftest.py 'tests/**/conftest.py'
     git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  (empty) ; tests/conftest.py
cmd  git log --oneline ca611e3..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)
```

**No tolerance value, no form, no counter, no injection -- so EU1 does not arise and
neither does the adversarial-ladder requirement it attaches.** Â§ 7 of the plan and Â§ 6 of
the report agree, and I agree with the reason: `max U <= 1.0` is the clause's own threshold,
the grid steps are FG3's and declared, and `MASS_PROPERTY_AGREEMENT` is read and not moved
-- it is what R787's margin is measured against.

**`tests/conftest.py` is unchanged**, so no rung's green is read through new in-tree code
(CH2/CI0/CJ0). The one conftest in the repository is at depth one and the glob pair finds
it, as my definition says it must.

**My own instructions: `git log ca611e3..HEAD -- .claude docs/SUPERVISOR.md` is EMPTY.** The
invocation predicted one commit, `4013d61`; `git show --stat 4013d61` touches `CLAUDE.md`
only, 24 insertions, and nothing under `.claude/` or `docs/SUPERVISOR.md`. The conclusion is
therefore stronger than the one offered: **not one of the four commits, and not `4013d61`
either, touches a line of my own instructions.** No STOP-class finding. `docs/reviews/` and
`tests/corpus/` are untouched by the range (`git log 1d2be7b..HEAD -- docs/reviews
tests/corpus` is empty).

## The suite, lint and CI at the reviewed commit (CA2, CK2)

```
cmd  python -m pytest -q -p no:randomly          (mine, at 09559f8, clean tree)
out  3344 passed, 2 warnings in 667.64s (0:11:07)   [exited with code 0]
cmd  python -m ruff check floatfea tests scripts
     python -m black --check floatfea tests scripts
     python -m mypy floatfea
out  All checks passed!
     135 files would be left unchanged.
     Success: no issues found in 37 source files
cmd  gh api repos/:owner/:repo/actions/runs/38112961531/jobs     (head 09559f8)
out  the verification ladder    success   runner "GitHub Actions 1000001656"  13 steps
     lint, unit and guards      success   runner "GitHub Actions 1000001657"  14 steps
     CI determinism -- leg               skipped  runner null  0 steps
     CI determinism -- ten legs agree    skipped  runner null  0 steps
```

**Nothing is red, locally or in CI, and there is no boundary state to waive.** `3344
passed, 0 failed, 0 skipped` is the whole suite with no exclusion -- it reconciles exactly
with the report's split, `3165 + 179 = 3344` -- so **the increment's final state is green in
a way no commit in its own record could claim**, which is FC1's control working as designed:
a closure commit creates neither boundary state.

**A note on the command my own definition prescribes.** `gh run list --commit <sha> --json
name,conclusion,workflowName` returns `[]` for every one of these four shas on this machine
while the runs plainly exist; `gh run list --limit 20 --json headSha,databaseId,conclusion`
finds all four. **An empty result from `--commit` here is a broken flag, not an unavailable
check**, and recording it as CK2's third state would have been wrong. CK2 does not apply:
no job in any of the four runs has `runner_name: ""` with a payment annotation. The two
determinism jobs are `skipped` under `if: github.event_name == 'workflow_dispatch'` -- not
run by design, which is neither red nor unavailable.

**The two intermediate reds, traced by name, both self-clearing (EG3, EH1, EJ2, FC1).**
`35de6cb`: 13 ids in `lint, unit and guards`, all in the two report-guard files and all
state-boundary, **plus one in the ladder that is NOT a boundary red** --
`test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`, CZ1 (iv), named as
such in the report and in the closure artifact, repaired at `740221d` with the ladder's
green there as the measurement. `740221d`: the boundary set alone. `15bb18f` and `09559f8`:
green in both jobs. **The one red in the range that was not designed was found by CI and not
by the implementer, the implementer says so in those words, and the trace is individual
rather than by family -- which is EG3(i) doing its job.**

**CZ1's four outputs exist and I verified the ones that matter.** `docs/closure/F6a.md` Â§ 0
carries (ii) and (iii) at `740221d` and (iv) at `15bb18f`; `09559f8` adds the green
follow-on. I re-ran (ii) myself at HEAD, above, and read (iii) from `gh` rather than from
the artifact. **CZ1 is satisfied and `09559f8`'s own pushed run is green too**, which the
artifact could not state for the reason CZ1 itself gives.

## The corpus (EG4(e))

**The pause held. No corpus file was added by the implementer or by me, and no batch ran.**
`git log 1d2be7b..HEAD -- tests/corpus` is empty, so there are **0 new entries and no
coverage measurement to report** -- the pause's intended consequence, not an omission. The
two exceptions EG4(e) keeps open -- mutation work on F4's load-mapping gate and EB6's
label-provenance gate -- are not touched: nothing in the range goes near either surface.

**What I ran instead, which is the recorded substitute, both halves:**

* **A continuum grid over the parameter space the decision rules guard.** The whole boundary
  sweep recomputed from my own tube algebra (77 D-rows across two groups), every continuum
  figure re-derived, the `rho A / mu = 1.0` crossing solved in **both** directions over all
  37 passing platform rows, and `admissible()`'s margin measured over the new test's full
  42-section span on **all five bodies** rather than one. **R787 came out of the fifth body
  and nothing else**; the 4.9/5.0 sharpening of my own (f) ruling came out of the full range
  rather than the five rows I sampled last round.
* **A regeneration check on the published deliverables.** `results/F6a/` regenerates
  byte-identically at HEAD (`git status --porcelain` clean after both generators);
  `results/F6/` diffs to one count line across `35de6cb..740221d` and to nothing else.
* **And mutation, three cells, on the two gates the commit moves**: the R784 repair reverted
  to its two-clause form and then to my own rejected clause, and a section term injected
  into `_build_body`. **The first refuted my closing condition and the third produced R786.**

## Try to break it

The case I built is the one the invocation pointed me at, and it is where the round's value
came from: **the new gate's own failure.** Verdict 122 could not test a gate that did not
exist; this round could, and the result is R786 -- the assertion is right, it detects the
defect, and it raises an `AttributeError` on the way to saying so. **The adversarial case
did not break the engineering; it broke the instrument's voice.**

The second case was my own figure. Asking *which bodies did I sweep* of a margin I had
published as "safe by a wide measured margin" turned `442x` into `4.4x` on the body that
binds. The engineering survives -- nothing flips, no answer moves -- and the record did not.

Everything else held. Six required sections, verified independently last round and unmoved;
a crossing claim exact over 37 rows and not just at its two endpoints; a spread, a grid step
and a denominator each reproduced from first principles; a premise whose dynamic half now
carries my own adversarial case to the digit. **FG1 asked for the numbers and the numbers
are right, twice over.**

## Next step opens when

**There is no next step. FG6 stops work after this verdict and the increment is closed by
this PASS.** What remains is a list, not a condition:

1. **R786 and R792 are the two items that should not wait, and they are the two that
   `CLAUDE.md` says do not.** R792 is a report guard and so FF0's class -- fixed in the next
   commit, not ledgered -- and R786 is the failure branch of a gate that is live in the
   ladder today. If FG6 means there is no next commit, both go on `docs/milestones/F2a.md`
   with R790.
2. **R788, R789, R791 and R787(a)'s two sentences go to `docs/closure/F6a.md`'s ledger**, by
   name, with their files and lines, and are not re-reviewed item by item.
3. **R790 is one line on `docs/milestones/F2a.md`**, and explicitly not a request to build
   anything before the apparatus freeze lifts.
4. **R787 is a correction to `docs/reviews/F6a/step-1.md` and it is in this file**, which is
   the only place it can be. `442x` is withdrawn; `393.9x` on the platform and `4.4x` on
   each hub supersede it, and `8.054e-05` is withdrawn in favour of `7.994e-05`. Anything
   downstream quoting either of my two numbers quotes a withdrawn figure; nothing in the
   repository does, which I checked.
5. **Increment 2 inherits the contradiction, not a question about it.** `rho A / mu` of
   `2.254` and `1.430` on the platform arms, two of three platform answers implying more
   static root moment than the whole static case carries (`1.752x` and `1.258x`), and the
   boundary now stated with its direction and its turning point. That is a closed finding
   handed over, which is what FG4 asked for.

## Disagreement with the criterion -- none this round, and one observation about EQ0

I ruled under CZ0 (a)-(d) as amended by EZ0 and under EQ0, and EQ0 earned its invocation
here. **The best finding of this round is in the repair of a repair** -- the failure branch
of the gate written to answer C99 -- and the second best is a figure I published myself that
nobody else could have corrected, because it is in a verdict and the verdict is the one
document the implementer may not touch. A green suite saw neither: `3344 passed`, both CI
jobs, `ruff`, `black` and `mypy` are green on all of it. That is EQ0's own stated reason,
observed once more.

**I have nothing for Xabier that is about the criterion rather than about the work.** FF0
did what it was adopted for again -- R792 routes to a commit instead of onto a ledger that
would outlive the milestone. The one procedural thing worth recording is not a disagreement:
**the invocation's summary of the CI reds was wrong about which commit carried the ladder
failure, and the repository's own record was right.** Reading the artifacts last, as my
definition requires, is what made that difference visible.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6a step 1
Reviewed commit: 8c1493133d2ee67351f44b7f4fe1542eedbbd01d
Verdict: HOLD
Reviewed commit: 8c1493133d2ee67351f44b7f4fe1542eedbbd01d
Tests: 3279 passed, 36 failed, 0 skipped   (my run, `python -m pytest -q -p no:randomly`, 641.86s)

## Round of 2026-10-10 -- F6a step 1, revision 1. **HOLD on three items, none of them a wrong number.**

**Reviewed commit: `8c14931`.**

**Which clause I ruled under.** `CLAUDE.md` Â§ "Step gating": CZ0 (a)-(d) **as amended by
EZ0**, with FG1's restatement that a wrong figure in `results/F6a/` or in the script that
produces it blocks; CA2 and CK2 for the CI reading (stated in my own definition, because
`CLAUDE.md` does not carry them); EG3/EH1/EJ2/FC1 for the boundary red; DD1 for F6's
disposition; EG4(e) for the corpus; EH4 for the boundaries; FF0 for the two gating-apparatus
items, which are **not ledgered**. My definition's citations resolve.

**FG1 asked me to recompute the governing required section by an independent route, and I
did. All six answers reproduce exactly** -- independent clause transcription, independent
section-property algebra, independent brute-force search with no area pruning, member
lengths set from the deck geometry rather than read from the search's own helper. Every
published `D`, `t`, `D/t`, `A`, `W`, `max U` and `rho A / mu` matched the digits published.

```
claim  the six answers, recomputed from the API clauses and the forces CSV with no import
       of floatfea.checks.api_wsd and no reuse of the search
cmd    my own /tmp script: brute force over D in [2.0,6.0]x0.1 and t in [0.005,0.600]x0.005
out    platform  (i)   t=410mm D/t=   6.10 A=2.6920 W=1.221159 maxU=0.9957 rhoA/mu=2.254
       platform  (ii)  D=3.2  D/t=  17.78 A=1.7078 W=1.221162 maxU=0.9958 rhoA/mu=1.430
       platform  (iii) D=6.0 t=55mm D/t=109.09 A=1.0272 W=1.512844 maxU=0.9835 rhoA/mu=0.860
       hubs      (i)   t=140mm D/t=  17.86 A=1.0380 W=0.580149 maxU=0.9899 rhoA/mu=0.543
       hubs      (ii)  D=2.3  D/t=  12.78 A=1.1988 W=0.589877 maxU=0.9726 rhoA/mu=0.627
       hubs      (iii) D=6.0 t=30mm D/t=200.00 A=0.5627 W=0.835591 maxU=0.9911 rhoA/mu=0.294
rule   `max U <= 1.0` over every governing per-instant row, every candidate outside the
       clause's own range refused -- and I used the STRICTER of the two readings FB1
       declares (`D/t <= 300` on section 3.2.3, not `300000/F_y = 845.1`). **The answers do
       not move under it**, so FB1's open discrepancy reaches none of the six.
judge  the numbers are right. Everything below is about what is said around them.
```

**And F6's stand-in reproduces too**: `U = 1.71167` on the platform group at
`D = 2.5 m, t = 180 mm`, `0.80821` on the hubs -- so the figure the deliverable cites for
comparison is correct, which matters for R781.

## Carried

**Checked, nothing carried.** `docs/reviews/F6a/` had no file before this one; this is the
milestone's first verdict. I checked the one thing that could carry in by name:

```
claim  F6's last verdict is PASS with no blocking item open, so nothing travels into F6a
cmd    head -8 docs/reviews/F6/step-2.md
out    Verdict: PASS ... "Four closure items, none blocking, one of which is the
       milestone's first finding happening one last time."
rule   CZ0: "A blocking item still open at that point carries by name into the next step's
       `Carried` section." There is none. F6's four closure items stay on
       `docs/closure/F6.md` and FG1 scopes this increment away from them.
judge  the report's declaration is true by fact and not by omission, and Â§ 7 is right that
       the parser could not read it until this revision fixed it.
```

**On my own instruction 1b (the `Answers:` header).** The report's header reads
`Answers: FG opens the step` and names no verdict, because for this milestone there is none.
That is the correct state, not a superseded one: the comparison 1b asks for -- does the
header name the LATEST verdict of this milestone -- has an empty right-hand side.

## Findings

**R781. (a, blocking) `results/F6a/required_section.md:5` says "no figure is typed" and four
figures in it are string literals in the generator.** The sentence is false of the document
it is in, and it is the one sentence that tells a reader these figures cannot go stale.

```
claim  the typed figures, located in the generator rather than inferred from the document
cmd    grep -nE 'w\("[^"]*[0-9]' scripts/measure/f6a_report.py
out    64:    w("at which the worst station reaches `U = 1.71167`.")
       182:   w("outside `D <= 6.0 m`, and the search cannot say, because FG3 fixed the range.")
       222:   w("`1.608328e-15` -- round-off. And `U <= 1.0` holds on the rebuilt forces too:")
       223:   w("`0.581954` on the platform group, `0.821927` on the hubs, on the static basis.")
rule   `results/F6a/required_section.md:5` -- "Generated by `scripts/measure/f6a_report.py`
       from `scripts/measure/f6a_required_section.py`'s own output -- no figure is typed",
       and the generator's own docstring, "Nothing is typed into the document"
judge  **every one of the four is CORRECT today** -- I reproduced `1.71167` independently and
       ran `f6a_premise_check.py` myself for `1.608328e-15`, `0.581954` and `0.821927`. That
       is not the finding. The finding is that `f6a_premise_check.py` **writes no file**, so
       three of these cannot be read from anything, and the deliverable asserts a provenance
       property it does not have. This is BP0's recorded species exactly: figures republished
       after the rule beneath them moved, each correct when taken. These two sentences tell a
       reader not to check -- which is what makes a stale figure survive.
```

**Closed when** either the premise check emits its three figures to a file the generator
reads (no new guard and no meta-test -- a `json.dump`, which DR1 and FG1 do not touch), or
the two provenance sentences are struck and each typed figure carries the command it came
from at the point of use. **And the four figures are re-taken at the commit that publishes
them (CP3), because a paste that precedes an edit is void.**

**R782. (a, blocking) `scripts/measure/f6a_premise_check.py`'s docstring says it compares "on
BOTH the static and the dynamic cases". It compares the static case twice and nothing else.**
The script produces three figures published in the deliverable, so it is inside EZ0's phrase.

```
claim  the dynamic comparison the docstring claims is not in the file
cmd    grep -n "_static_rows\|_net_field\|solve_inertia_relief" scripts/measure/f6a_premise_check.py
out    183:    before = MFT._static_rows(shipped)
       184:    after = MFT._static_rows(sized)
       (no other line)
rule   the module docstring, lines 14-16: "this rebuilds the model at the required section of
       each group and compares every force component at every member-station, on BOTH the
       static and the dynamic cases, and reports the maximum relative change"
judge  false in two ways at once: the dynamic case is never solved, and "the required section
       of each group" is one search per invocation -- as shipped, `iii_min_area`, so two of
       the six answers. **I did both halves myself and the premise HOLDS, which is why this
       is a false sentence and not a wrong answer.**
```

**I ran the static half at all six answers** (`--search` is already there):

```
claim  the premise's static half at the four answers the report did not check
cmd    python scripts/measure/f6a_premise_check.py --search i_min_wall_at_D_2.5
       python scripts/measure/f6a_premise_check.py --search ii_min_diameter_at_t_180mm
out    i   worst RELATIVE change 1.206246e-15   (worst ABSOLUTE 1.341105e-07 N.m)
       ii  worst RELATIVE change 1.742356e-15   (worst ABSOLUTE 3.278255e-07 N.m)
       iii worst RELATIVE change 1.608328e-15   (the published figure, reproduced)
judge  round-off at every answer, over area changes from 1.7078 to 2.6920 m^2 -- a 2.62x span
       of `A` and a 2.79x span of `r`. The premise's static half is verified for all six.
```

**And I rebuilt the DYNAMIC increment, which is the half nobody had measured.** The argument
in the script's closing paragraph -- "the dynamic increment is built from those multipliers
and each body's own d'Alembert field, and the field reads `mu`, held above" -- is **not
sufficient**, and this is the mechanism: the field is an acceleration, and what turns it into
a load is `element_equivalent_load` = `M_e @ a_e` with the CONSISTENT element mass matrix,
whose rotary terms are `rho_eq * I = mu * r^2`. `r` moves with the section even though `mu`
does not. Measured over the four governing periods, 4081 steps, five bodies:

```
claim  the per-instant governing rows, rebuilt at the shipped and at the sized section
cmd    my own /tmp script: the member_forces_table loop at both sections, 4 periods
out    iii_min_area : governing INSTANT moved on 26 of 48 stations;
                      worst relative change in the governing rows 6.860008e-01
                      (platform:hub3_arm ROOT N: 5.390660e+05 -> 6.845148e+06)
       i_min_wall   : governing INSTANT moved on 3 of 48;
                      worst relative change 7.948013e-03
rule   the stored `total_instant` row is the step where `sigma = f_a + f_b` PEAKS, and
       `sigma` is computed with the member's own section -- so WHICH instant governs is a
       function of the section even though the forces at a given instant are not
judge  this is the one way the published answer could have been undersized, and it is not in
       FG2. **It survives**: re-selecting the instant at the sized section moves `max U` by
       4e-06 at worst.
```

```
claim  max U at the published section, with the governing instant re-selected AT that section
cmd    the same two runs, max U over the re-selected rows
out    iii platform 0.983516 -> 0.983516     hubs 0.991135 -> 0.991139
       i   platform 0.995702 -> 0.995702     hubs 0.989907 -> 0.989907
rule   `max U <= 1.0`; the margin at the tightest answer is 4.3e-03 and the motion is 4e-06,
       1075x inside it
judge  the answers stand. The sentence does not.
```

**Closed when** the docstring says what the file does -- the static case, at the answer named
by `--search` -- or the dynamic comparison is in the file. Either; not a widening of the claim
to cover what I measured, because my measurement is not in this repository.

**R783. (a, blocking) The deliverable publishes a grid coincidence as a property of the
structure.** `results/F6a/required_section.md:108`, and the block beneath it: "THE TWO CONSTRAINED PLATFORM ANSWERS
LAND ON THE SAME SECTION MODULUS, and that is the table's explanation rather than a
coincidence", with "the same W to six figures" in the block beneath it.

**The mechanism is real and I verified it.** The binding condition at the governing station is
bending alone, and both constrained answers sit in the same compact branch, so `F_b` is
identically `0.75 F_y` and the required `W` is the same quantity in both searches:

```
claim  how much of U is bending at the governing station, and why F_b is shared
cmd    my own /tmp script, at the governing row platform:hub2_arm ROOT, T = 12.5 s
out    D=2.5 t=410: N=-8.0025e+04  My=1.8018e+08  Mz=2.6890e+08
                    u_bending=0.99556  u_axial(simple)=0.00014  U=0.995702
       D=3.2 t=180: the same row;  u_bending=0.99556  u_axial(simple)=0.00022  U=0.995779
       D/t = 6.10 and 17.78, both under 10340/F_y = 29.13 -> F_b = 0.75 F_y = 266.25 MPa both
judge  **"W binds, not A" is a measurement and it is correct.** The axial term is 1.4e-04 of
       the utilisation. Nothing here is being disputed.
```

**What is false is the precision.** Invert the decision rule instead of sampling the grid:

```
claim  the EXACT required W in each search, by bisecting maxU = 1 in the free variable
cmd    my own /tmp script: 200-step bisection on t at D=2.5, and on D at t=180mm
out    D = 2.5 m fixed : t* = 406.4985 mm  ->  W* = 1.21591028  A* = 2.673511
       t = 180 mm fixed: D* = 3.193772 m   ->  W* = 1.21600748  A* = 1.704248
       the two exact requirements differ by 8.054e-05 relative
       grid W step at D=2.5 : 0.007515 m^3 = 0.62% of the answer
       grid W step at t=180 : 0.028259 m^3 = 2.31% of the answer
       the two PUBLISHED grid answers differ by 2.5e-06 relative
rule   BP0/BG0: a figure carries the rule it was measured against, and a causal sentence
       carries the cell that isolates it
judge  **the mechanism is good to 8.1e-05; the published agreement is 2.5e-06, which is
       4e-04 of one grid step.** Two independent grids landing that close is luck at about
       one part in three thousand, and "rather than a coincidence" sits directly above it. A
       reader transferring `1.221159` to a truss on the strength of six figures is
       over-trusting the measurement by three orders of magnitude. **The number that actually
       transfers is `W_req = M_res / F_b = 3.2368e+08 / 2.6625e+08 = 1.2157 m^3` (continuum),
       and the grid answer sits 0.45% above it.**
cell   one variable moved: grid vs continuum. Same clauses, same row, same allowable.
```

**Closed when** the deliverable publishes the continuum requirement and the bending fraction
-- the two numbers that ARE the mechanism -- and the six-figure agreement is either dropped or
named as what it is. `W` is also not shared with answer (iii) (`1.5128`, because `D/t = 109`
reduces `F_b` to `217.63 MPa`), so "this is the number that transfers" needs to say which
allowable it is tied to.

### The things the invocation asked me to attack, ruled

**(a) The premise.** Ruled in R782. Static half: verified at all six answers by me, not two.
Dynamic half: verified by me for the first time, and the stated argument is insufficient for
the reason given there. **FG2(b)'s "single vertical redundancy" is true of the model**, and
measured rather than read off the directive: the platform has four tip joints against three
out-of-plane rigid modes, which is one redundancy, and the four arms are geometrically
identical -- `My = 1.916016e+08` on all four at ROOT static, to the digit -- so the redundant
force splits equally whatever the section is. That is why a 2.62x change in `A` moves the
static forces by 1.6e-15 instead of redistributing them.

**(b) The normalisation. The third measure is not hiding anything, and the reason is stronger
than the report's.** There is no component that is small-but-not-noise:

```
claim  per-component own-max relative change, which is what a shared denominator could hide
cmd    my own /tmp script over the same two static builds
out    comp   own global max     worst |delta|    delta/own max   delta/kind max
       N      0.000000e+00       0.000000e+00     --              0.000e+00
       Vy     0.000000e+00       0.000000e+00     --              0.000e+00
       Vz     6.948750e+06       1.117587e-08     1.608e-15       1.608e-15
       T      3.050995e-08       4.028382e-08     1.320e+00       2.102e-16
       My     1.916016e+08       1.639128e-07     8.555e-16       8.555e-16
       Mz     0.000000e+00       0.000000e+00     --              0.000e+00
judge  for EVERY component that is not round-off, the per-component figure and the per-kind
       figure are the SAME -- 1.608e-15 and 8.555e-16. Only `T` differs, and `T`'s own
       maximum is 3.05e-08 N.m. Three components are identically zero in both builds. So the
       shared moment denominator cannot be hiding a real change in a small component, because
       in the static set there is no such component. The report's 1.320350e+00 for the second
       measure is reproduced here as T's own-max figure, 1.320e+00.
rule   G4.1's "the denominators are sums of magnitudes" is the right analogy, but the
       load-bearing fact is the per-component table above, not the analogy
```

Caveat for the record: this is a property of the STATIC set only. In the dynamic set every
component is live, and there the shared denominator would be doing real work -- which is where
I used it (R782), and the 6.9e-01 figure there comes from the instant moving, not from the
denominator.

**(c) `W = 1.221159` vs `1.221162`.** Ruled in R783. Measurement in the mechanism, coincidence
in the digits. **The hub control is good**: the hubs are in tension at all three answers
(`3.3.1`, branch `tension`) so `A` binds and their three `W` are `0.5801`, `0.5899`, `0.8356`
-- they share nothing, which is the right control and it does its job.

**(d) FG4's arm-weight moment. It is sound to publish, and the `35%` sentence UNDERSTATES it
rather than overstating it.** This is the opposite of what the invocation expected, and it is
a measurement:

```
claim  the model's OWN static root moment as a function of the arm line mass and the
       remainder mass, so the closed form can be checked against it
cmd    my own /tmp script: the static solve at measurement_fraction = 1.0 (m_rem = 0),
       0.75 and 0.5, then M_root = a*mu + b*m_rem
out    f=1.00  mu=12500  m_rem=0        max|My| ROOT = 1.532813e+08
       f=0.75  mu= 9375  m_rem=625000   max|My| ROOT = 1.916016e+08
       f=0.50  mu= 6250  m_rem=1250000  max|My| ROOT = 2.299219e+08
       a = 1.226250e+04 per (kg/m)      b = 1.226250e+02 per kg
       the closed form's coefficient g L^2 / 2 = 1.225831e+04  ->  0.034% apart
rule   the solve is linear in the mass distribution, so `a` is measured with m_rem = 0 and
       `b` follows from the shipped configuration's own remainder point
judge  **`mu g L^2 / 2` IS the model's arm-weight term, to 0.034%.** The idealisation
       objection does not land: the four tip reactions and the cantilever form give the same
       number here because `R L = mu g L^2` exactly when the whole weight is on the arms. So
       the closed form is the model's own quantity and the "lower bound" label is right.
```

```
claim  how much the lower bound gives away, which is the number the deliverable does not carry
cmd    the same script, a*mu_req + b*m_rem with m_rem = 625000 held
out    (i)   mu_req=21132  MODEL 3.357772e+08  published 2.590481e+08   1.752x vs 1.352x
       (ii)  mu_req=13406  MODEL 2.410317e+08  published 1.643348e+08   1.258x vs 0.858x
       (iii) mu_req= 8064  MODEL 1.755217e+08  published 9.884729e+07   0.916x vs 0.516x
rule   against the published static root 1.916016e+08 N.m, the same denominator the
       deliverable uses
judge  the comparison is sound and **conservative by about 30%**. The finding is stronger than
       published: at answer (ii)'s required section the implied root moment ALSO exceeds the
       present total (1.258x), which the deliverable's table shows as 0.858 and therefore as
       not exceeding. "35%" is `75%` on the model's own quantity. I am not asking for the
       number to be replaced by mine -- I am recording that the bound's slack is 30%, it is
       one run away, and the conclusion survives either way.
```

**(f) The boundary answers. Saying so is enough, and I solved the boundary in both directions
(EH4) to establish that** -- which is more than the deliverable does:

```
claim  the minimum area per diameter across the declared range, both groups
cmd    my own /tmp script, minimum passing A at each D
out    platform  D=3.0 1.8811 | 4.0 1.3443 | 5.0 1.1604 | 5.5 1.1098 | 5.9 1.1008 | 6.0 1.0272
                 (D=2.0: nothing in the grid passes)
       hubs      D=2.0 1.5130 | 3.0 0.8670 | 4.0 0.7427 | 5.0 0.6233 | 5.5 0.6009 |
                 5.9 0.6449 | 6.0 0.5627
rule   `max U <= 1.0` with refused == 0, the search's own rule
judge  **the direction that WEAKENS the published conclusion is the one that matters, and it
       is far away.** Raising the bound makes `A` smaller and `rho A / mu` smaller, so
       "(iii) is the only mass-consistent answer" only gets safer. Lowering it breaks the
       conclusion: `rho A / mu` is 0.860 at D=6.0, 0.972 at D=5.0 and **1.126 at D=4.0** --
       so the mass-consistency verdict for (iii) flips between D = 4 and D = 5, and had FG3
       written `D <= 4.0` the deliverable's finding (iii) would have read the other way. The
       hub column is not monotone on the grid (0.6009 at 5.5, 0.6449 at 5.9) because the 5 mm
       wall step quantises it; the trend is.
```

So: a boundary answer may be published as a grid minimum when it is labelled as one, and it
is. **C98 below is the one sentence missing.**

**(e) The `floatfea/` change. The code is right and the comment's reason is wrong.** The
comment at `floatfea/model/platform.py:777-783` says: "IT DOES NOT MOVE THE MASS, AND THAT IS
NOT THIS PARAMETER BEING CAREFUL -- IT IS `_build_body`'s arithmetic. `member_mass = fraction
* deck_mass` carries no section term". The cited arithmetic does not establish it, because
`fraction` is not a constant -- it is chosen by `admissible()`, and `admissible()` reads a
quantity the section moves:

```
claim  the section reaches admissible() through the element mass matrix's rotary inertia
cmd    build at four sections and print the platform remainder-inertia eigenvalues
out    D=2.5 t=0.180  r=0.8227  min eig = 4.666293820e+09
       D=6.0 t=0.055  r=2.1020  min eig = 4.655771115e+09
       D=2.5 t=0.410  r=0.7530  min eig = 4.666602703e+09
       D=6.0 t=0.300  r=2.0180  min eig = 4.656743554e+09
rule   `remainder_inertia = deck_inertia - inertia_member - parallel`, and `inertia_member`
       comes from `assemble_mass_dense`, whose rotary term is `rho_eq * I = mu * r^2` -- the
       DY2 comment inside `_build_body` says so in its own words
judge  the eigenvalue `admissible()` tests moves by 1.0523e+07 with the section, 0.23%. So
       the section DOES reach the mass decision; the quoted two lines cannot be the reason it
       does not move the mass.
```

```
claim  and it does not move it, measured over the whole FG3 grid rather than argued
cmd    build with measurement_sections at 42 (D,t) pairs spanning D in {2,2.5,3,4,5,6} and
       t in {5,10,30,55,180,410,600} mm, all five bodies, and compare f and member_mass
out    built 42 sections; mass moved on: []   (f = 0.75 and member_mass identical on all five
       bodies at every one; zero refusals, so no L/D or L/r limit is reached either)
rule   `admissible()`: `m_r >= 0` and no eigenvalue of `J_r` below -tol
judge  the margin is 4.6558e+09 against a 1.0523e+07 section effect -- **442x** -- so the
       behaviour is safe by a wide measured margin and the parameter is what it says it is.
       The refusal on an unknown body name works and I checked it. **What is wrong is one
       sentence**, and it is wrong in the direction that invites a future caller to stop
       looking: a section outside the grid that flipped the eigenvalue would silently change
       the mass fraction, and the comment says that cannot happen.
```

C99 below.

## Closure items

**C98. `results/F6a/required_section.md:100-103` -- the boundary caveat has no direction and
no rate.** It says the true minimum may lie outside `D <= 6.0 m`; it does not say that `A`
falls monotonically toward the bound, nor that the mass-consistency verdict for (iii) flips
between `D = 4` and `D = 5`. My table under (f) is the sentence. The figure `D <= 6.0 m` is
also typed in the generator (R781).

**C99. `floatfea/model/platform.py:777-783` -- the comment's mechanism is wrong (CW0).** The
claim is true, the cited arithmetic does not entail it, and the entailment runs through
`admissible()`. Either state the measured margin (442x) or delete the "and that is ...
`_build_body`'s arithmetic" half and keep the fact. Per CW0 this is a test, a triple, or
deleted.

**C100. `docs/reports/F6a/step-1.md` -- a code fence is missing and the file renders wrong
from line 307.** Counting fences over the file gives 37: the triple at lines 308-314 is
OUTSIDE a block, the paragraph at 317-321 is INSIDE one, and the fence opened at 371 never
closes. One missing fence after line 306.

**C101. `docs/reports/F6a/step-1.md:270` says "THE EIGHTEENTH" for the test line 254 calls
"the seventeenth".** There are 17 failures in that file and the `R507` case is the
seventeenth. The commit message has it right; the report does not.

**C102. `results/F6a/required_section.md:61-64` -- the "x the mu-basis term" column is the
mass-ratio column restated.** `implied/assumed = (rho A_req g L^2/2)/(mu g L^2/2) = rho A/mu`
identically, so 2.254 and 1.430 appear twice in the document as different-looking quantities.
The column that would carry information is the one in (d) above.

## The two gating-apparatus items, FIXED IN THE NEXT COMMIT AND NOT LEDGERED (FF0)

**Neither of these holds the step.** Their headings read `(apparatus, FF0)` and not the
phrase a reader would expect, deliberately: `_blocking()` in `tests/test_report_carried.py`
matches the substring `block` anywhere inside the parentheses, so negating the word there
would be parsed as the opposite of what it says. DU1 tells the reviewer to put the class
inside the parentheses; this is the one class that cannot be spelled with that word.
Recorded so the next reviewer does not find it the slow way.

**R784. (apparatus, FF0) The `_status_cells()` repair reads green on a broken table when
the sanctioned sentence is also present.** The repair is right in substance -- one more state,
exact sentence only, `assert cells` kept -- but the early return is keyed on
`nothing_carried()` alone, so the half the assertion exists for is reachable past it. Three
cells, one variable moved:

```
claim  the sanctioned sentence plus item rows the parser cannot read, one of them saying CLOSED
cmd    import tests/test_report_carried.py, set CARRIED to each of three bodies, call
       test_a_report_does_not_say_CLOSED
out    A  this commit's real section     nothing_carried=True  cells=0  -> PASS (correct)
       B  sentence + unreadable rows saying "CLOSED"
                                         nothing_carried=True  cells=0  -> PASS  <-- green
       C  the same rows, sentence removed nothing_carried=False cells=0  -> red (correct)
rule   `test_a_report_does_not_say_CLOSED`: "no status cell parsed ... the table format
       changed and every check below passes on anything"
judge  B is the state the kept `assert cells` is supposed to catch, and the commit message
       claims it is kept for exactly that. The condition needs the third clause the docstring
       already implies -- no finding mentioned in the section at all -- not a wider early
       return. **Fixed, not extended (EK2).**
```

**R785. (apparatus, FF0) `scripts/write_verdict.py --milestone` is typed `int`, so the
one sanctioned path into `docs/reviews/` cannot express this milestone.** `--milestone 6a`
raises in argparse, and `--milestone 6` writes into the F6 review directory's step-1
file, prepending a round onto a CLOSED step's verdict. I wrote this file by running the script with that one
argument's type widened in a wrapper -- all four refusals and the whole accumulation path ran
unchanged -- and I am recording it because the tool that enforces the reviewer's write path
could not reach the milestone it was asked to review. `--milestone` should take a string;
nothing downstream of it does arithmetic.

## The boundary red, traced by name (EG3, EH1, EJ2, FC1)

**EG3 state (1), generalised: `docs/reviews/F6a/` had no file at the reviewed commit.** Not
"no verdict for this step" -- no verdict for the MILESTONE, so every verdict-reading guard is
reading an empty string. I measured it rather than taking it.

```
claim  the whole suite at the reviewed commit, and the same split the report claims
cmd    python -m pytest -q -p no:randomly
out    36 failed, 3279 passed, 2 warnings in 641.86s
       all 36 are in tests/test_report_carried.py (17) and test_report_guard_states.py (19)
       outside those two: 3279 - 97 - 4 - 21 = 3157 passed, 36 - 36 = 0 failed
       tests/test_report_numbers_are_sourced.py: 21 passed  <-- the control, and it holds
rule   EG3(i): the waiver is conditional on the trace, and a red that does not match the
       state's own list is CZ1 (iv) unchanged
judge  the report's per-file counts are exact -- 17/97, 19/4, 21/0 -- and its 3157 for the
       non-report-guard suite is reproduced here as an arithmetic consequence of my own run at
       a DIFFERENT commit, which is a stronger check than matching the number it quoted.
```

**The seventeenth is what the report says it is, and I checked it instead of taking the
trace.** One variable moved:

```
claim  test_the_R507_cases_rule_as_measured[frames.txt] fails through the documented
       permissive fallback on absent input, not through a change to the rule
cmd    import the module, read the chain, then substitute a non-empty tracked set
out    VERDICT_TEXT length: 0
       _reviewed_commit(VERDICT_TEXT): ''
       _tracked_paths_at_reviewed() size: 0
       _is_a_site('frames.txt'): True      (the control expects False)
       with a non-empty tracked set -> _is_a_site('frames.txt'): False
rule   `_tracked_at_reviewed`: "if not known: return True  # nothing to check against; do not
       silently drop sites"
judge  **not R629's shape.** R629 was a real defect inside a group ruled by class; this one is
       ruled by its own two-line chain, the direction is PERMISSIVE (it counts more things as
       sites, not fewer), and the diff of this revision's 30-line edit touches neither
       `_is_a_site` nor `_R507_CONTROLS` -- I read it. It clears when a verdict exists.
```

**The nineteen are the planted cascade off a red baseline (EH1).** `[baseline]` is red, and
each of the other eighteen carries its own failure line naming the absent
`docs/reviews/F6a/step-0.md`, `step-1.md` or `step-2.md` fixture, or the absent directory
itself (`reviews_directory_renamed_away` raises `FileNotFoundError` on `docs/reviews/F6a`).
Identified by the baseline and by each one's own line, not by name.

## CI, for the reviewed commit (CA2, CK2)

```
cmd  gh run list --commit 8c1493133d2ee67351f44b7f4fe1542eedbbd01d --json name,conclusion,workflowName
out  [{"conclusion":"failure","databaseId":38101883833,"name":"CI","workflowName":"CI"}]
cmd  gh api repos/:owner/:repo/actions/runs/38101883833/jobs
out  lint, unit and guards     failure   runner "GitHub Actions 1000001648"
                               the ONLY failing step is `guards and meta-tests`
     the verification ladder   success   runner "GitHub Actions 1000001649"
     CI determinism -- leg               skipped  (if: github.event_name == 'workflow_dispatch')
     CI determinism -- ten legs agree    skipped  (same condition)
cmd  gh run view 38101883833 --log-failed | grep -E "failed,"
out  36 failed, 970 passed, 1 warning in 598.43s
```

**CI is RED and it does not HOLD, under EG3 and nothing else.** The reason is stated rather
than assumed: the failing set in CI is the SAME 36 ids as my local run, by name, all inside
the two report-guard files; the lint, format, mypy and unit steps of that job all SUCCEEDED,
so the `guards and meta-tests` step is seen to have RUN rather than been skipped behind an
earlier red (CZ1 (iii)'s own concern); and the ladder job is green on a second runner. **CA2
is satisfied because nothing outside the boundary set is red, not because a local run said
so.** The two determinism jobs are **not run by design** -- `workflow_dispatch` only -- which
is neither red nor CK2's third state: no job in this run has `runner_name: ""` with a payment
annotation.

**EG3(ii): I measured state (1) clearing at this verdict's own commit, rather than asserting
it.** With this file in the tree and nothing else moved:

```
claim  the four ids that are state (1) and NOT state (2) go green the moment a verdict exists
cmd    python -m pytest tests/test_report_carried.py -q -p no:randomly, then the four ids
out    whole file  17 failed, 97 passed   ->   23 failed, 102 passed
       test_the_guard_reads_the_step_being_worked_on        PASS
       test_the_parse_found_something_to_check              PASS
       test_a_blocking_item_is_not_routed_to_4a             PASS
       test_the_R507_cases_rule_as_measured (all 3 cases)   PASS
rule   EG3's two states: (1) clears at the verdict, (2) clears at the answering report
judge  **state (1) has cleared and what is left is state (2)** -- 23 ids, every one naming a
       finding or a site of THIS verdict, which the closure commit's record answers. The
       R507 case passing here is the other half of its trace: it was the permissive fallback
       on an absent verdict, and a verdict is what cleared it. The count rose from 17 to 23
       because the state changed, not because something broke.
```

## The corpus (EG4(e))

**The pause held. I added no corpus file and ran no batch.** `tests/corpus/` is untouched by
this round -- 0 new entries, so there is no coverage measurement to report, which is the
pause's intended consequence and not an omission.

**What I ran instead, which is the recorded substitute**, both halves:

* **A continuum grid over the parameter space the decision rule guards.** The full (D, t)
  grid recomputed independently, plus the decision rule `max U = 1.0` INVERTED by bisection
  in each free variable (`t* = 406.4985 mm` at `D = 2.5`; `D* = 3.193772 m` at `t = 180 mm`),
  plus the minimum passing area at seven diameters in each group. **R783 came out of the
  inversion and the (f) ruling came out of the per-diameter table** -- neither is visible from
  the grid the search chose.
* **A regeneration check on the published deliverable.**

```
claim  the deliverable regenerates from its own scripts at this commit
cmd    python scripts/measure/f6a_required_section.py && python scripts/measure/f6a_report.py
       && git diff --numstat results/F6a/
out    (empty -- CRLF normalisation only; no tracked content differs)
judge  the generators are deterministic and the shipped document is the one they produce. F6
       step 2's third round found a non-deterministic deliverable this way; this one is clean.
```

## Try to break it -- the adversarial case, and it held

The case I built is the one the method's own structure makes available: **the stored
per-instant basis keeps ONE row per station, chosen where `sigma` peaks, and `sigma` is not
`U`.** A step with less `sigma` and more shear, torsion or axial could carry a larger `U`, and
the search would never see it -- which would make the published section undersized in the one
direction that matters.

```
claim  max U at the tightest answer over EVERY step of the four governing periods and every
       station, not only at the sigma-peak instant
cmd    my own /tmp script: the full dynamic loop at the i_min_wall_at_D_2.5 section, 4081
       steps x 5 bodies x 16 members x 3 stations, U from my own clause code
out    i_min_wall_at_D_2.5: max U over EVERY step, refused=0
         platform  max U = 0.995702  at platform:hub4_arm ROOT  T=12.5  step=13
         hub       max U = 0.989907  at hub3:buoy9_arm  ROOT    T=12.5  step=563
rule   `max U <= 1.0`, and the published per-instant figures are 0.9957 and 0.9899
judge  **identical to the published figures.** The sigma-peak instant IS the U-peak instant at
       this answer, so the basis the search reads loses nothing here, and `refused = 0` over
       195888 station-evaluations says no candidate silently left the clause's range. The
       adversarial case did not break it. That is the strongest single statement anyone has
       made about these six answers and it is not in the report.
```

## Tolerances touched

**None.** `git diff 950b916..8c14931 -- floatfea/tolerances.py` is empty, and I checked it as
its own diff. Â§ 7 of the plan and Â§ 6 of the report both state that none is needed, and I
agree with the reason: `max U <= 1.0` is the clause's own threshold, the grid steps are FG3's
and declared, and `1.608328e-15` is reported against round-off rather than against a ceiling.
No counter is declared or moved, so EU1 does not arise. `tests/conftest.py` is unchanged
(`git ls-files -- tests/conftest.py 'tests/**/conftest.py'` -> `tests/conftest.py`, diff
empty), so no rung's green is read through new in-tree code (CH2/CI0/CJ0).

**My own instructions**: `git log 950b916..HEAD -- .claude docs/SUPERVISOR.md` gives one
commit, `e53675e`, a standalone `process:` commit citing R777, touching only
`.claude/agents/gating-supervisor.md`, additive, removing no guard -- I read it line by line.
No step commit touches them. No STOP-class finding.

## Next step opens when

**There is no next step: FG6 stops work after this and FG1 allowed one reviewed revision.** So
the HOLD's force is on the deliverable rather than on a gate, and it is this:

1. **R781** -- the deliverable no longer claims a provenance it does not have: either the
   premise check emits its figures and the generator reads them, or the two sentences go and
   each typed figure carries its command at the point of use. Re-taken at the publishing
   commit (CP3).
2. **R782** -- `f6a_premise_check.py`'s docstring describes what the file does.
3. **R783** -- the continuum requirement (`W_req = 1.2157 m^3`) and the bending fraction
   (`u_bending = 0.99556` of `U = 0.995702`) are published, and the six-figure agreement is
   dropped or named as a grid coincidence.
4. **The corrected deliverable is re-sent to Xabier**, because the uncorrected one is already
   with him. That is the item; a corrected file sitting in `results/` is not it.
5. **R784 and R785** are fixed in the next commit under FF0 and are not ledgered. C98-C102 are
   ledgered and fixed once, in the closure commit, and are not re-reviewed item by item.
6. **CZ1's four outputs** at the closure commit, in its own record: `ruff`, `black`, `mypy`,
   `pytest -q`, then the pushed `gh run list --commit <sha>` with job-level conclusions. Under
   EQ0 that commit changes no gate and no tolerance if it is confined to the above, so **it is
   not reviewed** -- which means items 1-4 are answered on the implementer's record, with the
   triples, and nobody checks them. Say that plainly in the closure artifact rather than
   implying a review that will not happen.

**And what this HOLD is not about.** The engineering is sound and I could not break it. Six
required sections reproduced exactly by an independent route; the premise verified at all six
answers and, for the first time, in the dynamic increment; the governing-instant selection
shown to be section-dependent and shown not to matter (4e-06 against a 4.3e-03 margin); the
boundary solved in both directions; the mass contradiction real, and understated by about 30%
rather than overstated. **FG1 asked for the numbers and the numbers are right.** The three
blocking items are three sentences published around them, and EZ0 is the clause that says a
sentence in a deliverable already in Xabier's hands is not free.

## Disagreement with the criterion -- none this round

I ruled under CZ0 (a) as amended by EZ0 and I think it is the right instrument here: every one
of R781-R783 is a sentence in `results/F6a/` or in the `scripts/measure/` script that produced
a figure in it, and none of them is a report section. FF0 did exactly what it was adopted for
-- two apparatus items found in one round, both routed to the next commit instead of onto a
ledger that would have outlived the milestone. I have nothing for Xabier that is about the
criterion rather than about the work.
