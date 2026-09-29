# Review � F2 step 7
Reviewed commit: 02407b53875baa484b209338dce4a7bd64b5036a
Verdict: HOLD

**Reviewed commit: `4708cc2`.**
Tests: 2768 passed, 8 failed, 0 skipped   (my own run at `4708cc2`, `python -m pytest -q`, 591.03s)

**SEVENTY-FIRST verdict on F2/F3, and the FIRST of the new step. The count starts at one;
verdict 70 spent step 7's cap and closed it, and step 7 stays closed (DD1).** This verdict
is about the tree and about a plan, exactly as 70 was, and it is written into step 7's file
because that is the only report file every guard can see -- the reason is in R590 below and
the ruling is mine to give, not the implementer's.

**WHY HOLD AND NOT PASS.** All four carried items are genuinely answered and I re-measured
every one of them myself rather than reading the report -- DW1's six geometry figures
reproduce to the digit, the twelve-mutation ablation reproduces exactly, `--check` passes on
my reading of the tree. That is the best round of work this milestone has produced on the
platform. **But CI at `4708cc2` has conclusion `failure` and my own run is 8 red.** CA2 says
a red CI is a HOLD regardless of what a local run says, CZ0(d) says a red test at the
reviewed commit blocks, and verdict 70's own closing condition 4 pre-declared this exact
outcome as (d). The cause is one arbitrary floor in one meta-test and the fix is a deletion I
rule for below. Do not read this HOLD as a judgement on the work; read it as the one line in
the ladder that cannot be waived.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 4708cc2 --json name,conclusion,status,workflowName
out  []       -- the --commit filter still returns nothing while a run is in flight
cmd  gh run list --limit 6 --json headSha,databaseId,status,conclusion,event
out  36523001390  4708cc2  push  in_progress   -- the run EXISTS at the judged commit
cmd  gh run view 36523001390 --json status,conclusion   (polled to completion, 14 polls)
out  completed  FAILURE
cmd  gh run view 36523001390 --json jobs
out  the verification ladder            success  13 steps
     lint, unit and guards              FAILURE  14 steps  -- step "guards and meta-tests"
     CI determinism -- leg              skipped, 0 steps
     CI determinism -- ten legs agree   skipped, 0 steps
cmd  gh run view 36523001390 --log | grep run_rung
out  rung1 1276 / rung2 66 / rung3 164 / rung6 134 / rung4 127 collected, 0 failed,
     0 errored, 0 skipped in every rung; rung5 0 directories
cmd  gh run view 36523001390 --log-failed | grep -E "FAILED|failed,"
out  8 failed, 913 passed, 1 warning in 570.41s
     FAILED tests/test_report_carried.py::test_the_parse_found_something_to_check
     FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[7 states]
```

**THE LADDER IS GREEN AND THAT IS WHY THIS IS A HOLD AND NOT A STOP.** Every rung collected
and none failed, at the judged commit, on a machine neither of us controls. rung3 collected
164 including the rewritten G3.2 module. Nothing about the platform, the element or the deck
is red anywhere.

**CK2 DOES NOT APPLY AND I CHECKED RATHER THAN ASSUMED.** The failing job ran 14 steps for
ten minutes; it is a real failure, not an unstarted job. The two determinism jobs are
`skipped` with zero steps -- neither red nor green, and not CK2's allowance state either,
since every other job in the run executed and there is no billing annotation. Recorded as
unavailable on this run. The last run that executed them is `36455024518` at `2dc6a99`, and
`git diff 2dc6a99..HEAD -- .github` is empty, so nothing about the determinism configuration
has moved since.

**My own run agrees with CI on both the count and the names**, which is worth saying because
it is the first time this round that the two machines have been compared on a red rather than
on a green: 8 failed, 2768 passed at `4708cc2`, same eight test ids.

## Carried

Verdict 70 carried three blocking items -- R582, R583, R584 -- and closure items C10 to C16.
**The report's header is `Answers: verdict 70 @ 1b895db`, which names the LATEST verdict, so
instruction 1b is satisfied and I am not holding on it (see the ruling on C13 below).**
`python scripts/check_carried.py --verdict docs/reviews/F2/step-7.md --report
docs/reports/F2/step-7.md` prints `all 4 findings carried`, exit 0.

**I re-measured all four rather than reading the report on them. Every one is answered.**

* **R582 -- ANSWERED at `63046e5`, a standalone `plan:` commit, and DW1's condition holds on
  my own measurement.** I resolved every joint attach point through its body reference from
  the exported deck and got the plan's figures to the digit:

```
cmd    joint attach points resolved through each body reference, lambda = 50
out    16 of 16 joints: |a - b| = 0.000e+00; z spread max - min = 0.0 exactly
out    joint plane z = 0.4933695679797303 model = 24.668478398986515 m full = 24.6685
out    platform reference z = 0.7 model = 35.0 m full, 10.331521601013483 m above = 10.3315
out    hub1..4 reference z minus joint z = 0.0 exactly, all four
out    centre -> hub node: 50.000000 m full, dz 0.000e+00, on all four
out    hub node -> buoy joint: 25.000000 m full, dz 0.000e+00, on all twelve
out    platform MASS reference -> hub1 joint: 51.0562 m, 11.6747 deg
rule   a planar frame requires ONE joint elevation exactly, not approximately
judge  the frame IS planar at joint elevation, the 51.056 m inclined vector IS the
       platform end alone, and the hubs DO need no rigid link. All three of the
       implementer's readings are correct and I did not take any of them on trust.
```

  **And the two findings beyond the ruling are both correct.** Each hub carries exactly three
  cluster arms with angular gaps of `120.0, 120.0, 120.0` degrees on all four hubs -- four
  tripods, twelve cluster arms. `L/r` is `60.774830` and `30.387415`, so `60.77` and `30.39`
  as printed; the `60.78` is gone. Each buoy reference is `84.45185` m below its joint point,
  so the F2a return condition's `84.45 m` is right.

* **R583 -- ANSWERED at `b5602d6`, and the published ablation reproduces EXACTLY.** This is
  the invocation's question 1 and it deserves the detail.

```
cell   ONE VARIABLE: remove the CONTENT and BYTE digest gates from the check list,
       run the module's own twelve mutations through the SHIPPED functions
out    2 of 12 missed: every_mass_times_ten, re_emitted_with_sort_keys_True
judge  exactly the published figure, reproduced independently on my own harness.
       The counter is measuring those gates and not a copy of them. R583 is closed.
cell   the same twelve with ALL of the shipped checks
out    0 of 12 missed -- every one of the eleven the old gate missed now reddens
cell   the same twelve with all THREE digests removed, which the report does not run
out    3 of 12 missed -- two_bodies_swapped_in_order joins them
```

  **Then I ran thirty-three mutations the twelve-entry table does not contain, and that is
  where the coverage number moves.** Two are caught by nothing shipped -- see R589 and C18 --
  and the ablation goes from 2 of 12 to **17 of 33**. Both numbers are correct. One of them is
  about the gate and the other is about the table.

* **R584 -- ANSWERED at `b5602d6`, and I ran the procedure myself on a second reading of the
  tree rather than accepting a pasted output.**

```
cmd    python scripts/export_platform_deck.py --check
out    HSP floatfea-ref-1 @ 25de7ce / bodies 17 joints 16 /
       round trip: re-validated dump equals the source dump (9 top-level keys) /
       tests/goldens/platform_deck_digest.txt matches the deck /
       data/platform/platform12_deck.yaml matches the deck, HEADER INCLUDED   exit 0
cmd    git -C ../HSP-runs describe --tags --always ; rev-parse --short HEAD ;
       status --porcelain --untracked-files=no
out    floatfea-ref-1 / 25de7ce / (empty)
judge  both halves of R584 landed. The preflight refuses a dirty worktree at :89-97, and
       `comparable()` at :227-228 now excludes only `#   exported` by name rather than
       slicing the whole header. The committed YAML and the committed digest both
       reproduce a deck built from HSP at the pin, today, here. That is the strongest
       statement available about this file and it holds.
```

* **C10 / R585 -- ANSWERED at `475c224`**, and the fix is the one-line `is_dir()` branch the
  technical supervisor directed. The commit cites the direction and touches nothing else in
  the harness; the diff is 16 lines of which 12 are the reason. **It is a guard repair where
  DR1 permits only deletion, and it stands only on that direction** -- I record that rather
  than ruling it a STOP-class process breach, because the direction is named in the commit
  message and the change is confined to `tests/`. C11 is closed too, in passing: the
  `BODIES * 6 - JOINTS * JOINT_ROWS == 38` line is gone from the module.

* **R567 -- CARRIED, and the implementer is right about the mechanism.** See the ruling below.
  I have recorded the withdrawal in this verdict so the guard can do its job.

## Withdrawn in earlier rounds, recorded here so the record survives the round

**This file is OVERWRITTEN each round** -- `scripts/write_verdict.py:78` is
`out.write_text(header + body)`, not an append -- so it holds one round and every earlier
verdict exists only in git history. `test_no_status_claims_more_than_the_verdict_allows`
states its premise on its face as "the WHOLE review file, every round of it, because a
withdrawal ruled two verdicts ago is still a withdrawal", and that premise is false of a file
I replace. The implementer measured it: `83c7ba5` 397 lines / R567 x3, `4314118` 508 / x2,
`4ff1008` 508 / x2, `1b895db` 538 / **x0**. I reproduced the line counts.

**The guard is right about the rule and the defect is in MY output, not in the guard.** I am
not asking for the guard to change and the implementer was right not to touch it. The fix is
one standing section in the file I write, and this is it:

* **R567 -- WITHDRAWN by verdict 69.** Its site, the `two_digit_step_number` guard state, was
  deleted under DT2, which was one of the two DR1-compliant moves verdict 68 itself named.
  `docs/milestones/F2a.md:228` records the same withdrawal.

**A report may now write `withdrawn` for R567 without the guard reddening, and reporting
`carried` -- which is what revision 5 did -- remains correct and weaker.** This section will
be carried forward in every verdict from here.

## Findings

**R586. (d, blocking) Eight tests are red at the judged commit and CI at the judged commit
has conclusion `failure`. `tests/test_report_carried.py:454`.**

One cause, and the implementer named it correctly before I got here. I am ruling it rather
than leaving it open a second round.

```
cmd    python -m pytest -q          (mine, at 4708cc2)
out    8 failed, 2768 passed, 0 skipped in 591.03s
cmd    gh run view 36523001390 --json conclusion     (the push run AT 4708cc2)
out    failure -- job "lint, unit and guards", step "guards and meta-tests", 8 failed
rule   `assert len(EXPECTED) >= 5` -- a FLOOR on how many findings a verdict must carry
out    AssertionError: only ['R582','R583','R584','R585'] expected; assert 4 >= 5
judge  the parse did not fail. It found all four findings verdict 70 wrote, and four is
       the true count. Seven of the eight reds are guard states whose nested run includes
       this test, so eight reds are one assertion.
```

**AND IT WILL STILL BE RED AFTER THIS VERDICT, WHICH IS WHAT DECIDES IT. I MEASURED THAT
RATHER THAN ASSUMING EITHER WAY.**

```
cmd    EXPECTED, recomputed against THIS verdict as `test_report_carried.py:270-273`
       computes it -- findings, union the R-numbers in the LAST `Carried` heading
out    ['R586', 'R587', 'R588', 'R589']   -- 4, so `assert 4 >= 5` again
judge  the last heading matching "Carried" in this file is `## Carried for the next
       step`, which names no item because this is a HOLD. There is no state of this
       verdict that satisfies the floor except padding it with findings I do not have.
```

R546 is the same shape and it is already on the record: *no satisfiable state at a milestone
close*. A guard that reddens because I wrote four findings and would green because I wrote six
is measuring the reviewer's verbosity. It has never measured a parse failure: the two assertions above it, `_FINDING.findall(VERDICT_TEXT)` non-empty and
`CARRIED.strip()` non-empty, are what stop a parse failure reading as a clean bill, and those
two are correct and must stay.

**Closed when** the single statement `assert len(EXPECTED) >= 5, (...)` at
`tests/test_report_carried.py:454-457` is **deleted**, with the reason recorded at the site
-- that a verdict is permitted to carry fewer than five findings, and that verdict 70 carried
four correctly. **This is a DELETION under DR1 and not a repair: do not replace the floor with
a smaller floor, and do not parametrise it.** The two assertions above it stay untouched. Then
CI at the answering commit is green. Nothing else in this HOLD depends on anything but that.

**R587. (plan, blocking) The re-locked plan says both that the twelve buoy bodies are in the
model and that they are out, and the difference is 85.6% of the deck mass.
`docs/milestones/F3.md:302` against `:323-324`.**

This is the invocation's question 4, and the answer is that scope was not widened -- it was
reduced, and the reduction is under-determined at the one number that decides what the first
result means.

```
claim  the plan says the remainder mass of EVERY body is attached
cmd    sed -n '302p;310,313p' docs/milestones/F3.md
out    :302  5. **attach each body's remainder mass by rigid link** (DW2, section 3.3)
out    :311  * **Remainder:** each body's remaining mass -- deck mass minus member mass
              -- goes on a lumped mass at the deck's reference point
claim  and the plan says the first result contains five of the seventeen bodies
cmd    sed -n '323,324p' docs/milestones/F3.md
out    The first result is **the platform body and the 4 hub bodies, 16 members.** The 12
       buoy spar columns are **deferred until after the member-force table**
cmd    the exported deck, body masses summed by class
out    12 buoys 344.04 kg model / 4 hubs 48.00 / platform 10.00 / total 402.04
rule   G3.1a asserts FE body mass, CoG and inertia against the deck PER BODY
judge  under one reading the model carries 402.04 kg and twelve 84.45 m rigid links nobody
       has mentioned; under the other it carries 58.00 kg, which is 14.4% of the deck, and
       G3.1a passes on 5 of 17 bodies while 85.6% of the mass is absent. The plan's
       executable list says the first; its scope section says the second.
```

**AND THE TWO READINGS GIVE MEMBER FORCES THAT DIFFER BY ORDERS OF MAGNITUDE IN THE ONE
MEMBER WHOSE SECTION IS A RECORDED NUMBER.** `docs/milestones/F3.md:101` sources the 25 m
cluster arm's `2.5 m x 180 mm` wall from `docs/milestones/F1.md:425-433`, where the demand is
`5.93 MN` at the rod tip over 25 m, `M = 148.2 MN.m`. If the buoy body is out, that tip
carries nothing but the arm's own steel, and the member-force table for the only member in the
model with a designed section is computed without the load that designed it. A utilisation
computed that way is not conservative and not unconservative -- it is about a different
structure.

**And a third thing follows from whichever reading is taken.** Sixteen members, four hub arms
and twelve cluster arms, with nothing joining adjacent hubs or adjacent buoy joints: in plan
the frame is a **tree**, four tripods on four radial spokes. Every joint plane member is
horizontal, z spread `0.000e+00` m, so a vertical load at a buoy joint has **no axial path at
all** and is carried entirely by bending and torsion of the cluster and hub arms. That may be
the right model. It is not a conclusion the plan states, and DW5 is written from this list.

**Closed when** section 3.2 item 5 and section 3.4 agree, in words, on whether the twelve buoy
bodies' mass and inertia are in the first result; if they are, the twelve `84.4519 m` rigid
links are named beside the platform's `10.3315 m` and the hubs' zero-length one; if they are
not, section 3.4 says so in those terms and G3.1a's row says which bodies it covers. A `plan:`
commit; DK0 applies and it buys no fresh three.

**R588. (c, blocking) The preflight that makes G3.2's "at the pin" true ignores untracked
files, and the comment beside it asserts that untracked files cannot matter.
`scripts/export_platform_deck.py:89` and `:95-96`, against `:103-104`.**

R584's first half landed and the tracked-file gap is closed. This is the residue, and it is a
finding because the code chose the narrower refusal and wrote a reason for the choice that one
reading refutes.

```
claim  untracked files cannot change what the study imports
cmd    the sentence at :95-96 -- "Untracked files are ignored -- they cannot change
       what the study imports."
cmd    the three lines at :103-104 --
         for path in (HSP_RUNS, STUDY, STUDY.parent / "cluster-3buoy-rigid"):
             sys.path.insert(0, str(path))
cmd    grep -nE "^(import|from) " ../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py
out    :62  import cluster_common as cc
out    :63  import platform_common as pc
judge  both are BARE-NAME imports resolved off sys.path, and `insert(0, ...)` in a loop
       puts `cluster-3buoy-rigid` FIRST. An untracked `platform_common.py` dropped into
       that directory is imported in preference to the tracked one in
       `platform-12buoy`, and `git status --porcelain --untracked-files=no` reports
       nothing. The preflight passes, the header names the pin, and the deck is built
       from a file no commit contains -- which is the exact outcome the docstring at
       :62-64 says the pin exists to prevent.
rule   "a model exported today and a model exported next month are the same model"
```

**This is (c) and not prose because the flag IS the threshold.** `--untracked-files=no` versus
`all` is a decision about *which files a gate requires to match HEAD*, and `docs/verification/
README.md:97` makes this script half of G3.2. The false sentence is what makes it a finding
rather than an acceptable narrowing: a reader of the site is told the gap does not exist.

**Closed when** either the preflight refuses untracked files in the three directories it puts
on `sys.path` -- `--untracked-files=all` restricted to those paths, or a check that no
untracked `.py` exists in them -- **or** the sentence at `:95-96` is deleted and replaced by
the residual stated as a residual, in which case the gate's claim shrinks to match what it
checks. Either direction closes it; I am describing the predicate, not writing it.

**R589. (c, blocking) The digest that now carries G3.2 is named for the file's bytes and is not
over the file's bytes, and a line-ending rewrite passes all nine checks.
`tests/verification/rung3/test_platform_deck_export.py:221-247` and `:80`.**

This is the invocation's question 1, second half, and it is the one adversarial case that
passed when it should have failed.

```
cell   ONE VARIABLE: the committed YAML rewritten with CRLF, nothing else changed
out    all nine shipped checks GREEN -- CONTENT, ORDER, HEADER, FINITE, TOPOLOGY,
       AXIAL, COPLANAR, BYTE and REEMIT
cmd    the reader at :80 -- `DECK_YAML.read_text(encoding="utf-8")`
judge  `Path.read_text` opens in text mode with `newline=None`, so universal-newline
       translation turns every CRLF into LF before the hash sees it. The digest is over
       the newline-normalised decoded body, not over the bytes.
rule   the docstring at :221 -- "The file as emitted, hashed" -- and the failure message
       at :242-246 -- "the deck YAML's BYTES do not match the recorded digest"
```

**I am NOT asking for the behaviour to change and I want that on the record**, because the
normalisation is what makes the gate portable: with `core.autocrlf` on Windows the same commit
checks out with different bytes on two machines, and a true byte digest would redden in CI or
here depending on nobody's decision. The quantity it compares is the right quantity.

**What blocks is that the gate's own statement of which quantity it compares is wrong, and
that statement is now the only one there is.** `docs/verification/README.md` does not mention
the digests at all (C17), so these two sentences are the whole published description of what
G3.2 asserts, and they describe a stricter gate than the one that runs. Under CZ0 this is (c)
-- "what a gate claims, on which quantity" -- by the same reading my own instructions name: a
docstring that is the only statement of what a gate measures is the gate's assertion.

**Closed when** `:221` and `:242-246` say what is hashed -- the newline-normalised document
body as decoded, header excluded -- and say why, in one sentence, so a later reader does not
reach for `read_bytes()` and make the gate environment-dependent. One docstring and one
message. No behaviour change, no new apparatus.

## The rulings the invocation asked for

**IS A COMMITTED DIGEST A LEGITIMATE GATE, OR A GOLDEN THAT WILL SIMPLY BE REGENERATED?
It is a legitimate gate for exactly one property, and the property is the one DJ1 asked for.
Ruled, not left standing.**

The digest cannot detect a deck that changed *because HSP changed*: `main()` writes
`platform12_deck.yaml` and `platform_deck_digest.txt` in one invocation, so one re-run moves
both and the module goes green again. What it CAN detect, without a second repository and
therefore in CI, is that the committed file was written by something other than the generator
-- a hand edit, a merge resolution, an editor reformat, a partial revert. That is precisely
*"no coordinate is typed into this repository"*, and before this commit nothing in the tree
checked it at all.

**The defence against regenerate-to-match is the `git diff` and the reviewer, not a test, and
that is what a golden IS under `CLAUDE.md` § Testing.** It is the same boundary CJ0 draws for
conftest forgery: a gate that reads a record cannot outrank code that writes the record. The
digest docstring at `scripts/export_platform_deck.py:160-162` says this in the right words and
points at the rule. **So the split is coherent and I am ruling it sound:** the digest gates the
file against the tree, `--check` gates the tree against HSP, and neither pretends to be the
other. The residual I will name once: **a commit that moves the digest and the YAML together is
the one thing in this arrangement that only a reader can catch**, and it should be read as
carefully as a `tolerances.py` diff. That is not a new guard; it is a line in my own reading
list and I am putting it there.

**WHAT ELSE I WENT LOOKING FOR AND DID NOT FIND: A FOURTH GAP IN `--check`.** Three candidate
holes, measured:

```
cell   the header rewritten with `bodies 99` / `joints 99`
out    the suite half reddens (HEADER); `--check` reddens on the comparable lines. FIXED.
cell   a tracked file in ../HSP-runs modified while the worktree sits at the pin
out    the preflight refuses with the diff printed. FIXED.
cell   an untracked module on the import path
out    NOT refused -- that is R588, and it is the only one of the three still open.
cell   a line beginning `#   exported` carrying arbitrary text
out    invisible to `--check` (filtered by `comparable`) AND to the header test.
       A blind channel, recorded as C21 rather than blocking: nothing reads that line
       and the model cannot be changed through it.
judge  the fourth gap you asked about is R588. The `exported` channel is a fifth and it
       is cosmetic. I found no path by which a WRONG MODEL reaches the file with
       `--check` green on a clean pinned worktree.
```

**THE `Answers:` SHA NAMES THE COMMIT THE VERDICT TEXT IS FINAL AT, NOT THE COMMIT JUDGED.
Ruled, and C13 is closed by this ruling.** `VERDICT_TEXT = _verdict_text_at(ANSWERED)` reads
the verdict file *at that commit*, and this file is overwritten each round, so naming the
judged commit makes every generator read the PREVIOUS round's verdict. That cost three rebuilds
and it will cost three more every time. **My last two hand-backs proposed the judged commit and
they were wrong.** The convention from here: `Answers: verdict <n> @ <the commit that verdict
was committed at>`, and the judged commit is stated in prose in the report's own §1. This
verdict's closing instructions say it as a command.

**THE THIRD PASTED UNRUN NUMBER -- RECORDED, NOT A FINDING, AND THE PROCEDURAL CHANGE IS THE
FIRST ONE THAT IS A PROCEDURE.** `902301b` (three counts), `b958083` (one), `b5602d6` (108
where it is 107). All three amended before pushing; nothing in the tree reads a commit message,
so no guard could have caught any of them and none reached a reader. **What is different this
time is that the fix is not a resolution.** The lint line is now produced by capturing the
command's output into the message text, which removes the hand from the loop instead of asking
it to be more careful -- and the `L/r = 60.78` slip in the plan was fixed by computing the
table in place rather than by re-typing it. That is the right shape and it is the first time in
three occurrences that the answer has been mechanical. I verified the number it lands on:
`L/r` is `60.774830`, so `60.77`.

**`measure_platform_joints.py` and `export_platform_deck.py` are still not apparatus under the
freeze**, unchanged from verdict 70's ruling. Nothing was added to either class this round.

## Closure items

None of these blocks. Fix the list once, in the closure commit, and do not re-review them
item by item (CZ0). **C10, C11, C13, C15 and C16 from verdict 70 are closed** -- C10 at
`475c224`, C11 by the rewrite, C13 by the ruling above, C15 and C16 by the plan rewrite at
`63046e5`, both of which I re-measured. **C12 and C14 are still open and carry forward.**

* **C17. `docs/verification/README.md:93-96` still describes the RETIRED assertion as gate
  G3.2's always-run half, and does not mention the digests at all.** It reads "*asserts,
  everywhere and always, that the committed file round-trips through a parse-and-re-emit
  cycle*" -- which is the assertion R583 ruled vacuous, which no longer carries the gate id,
  and which is now named `test_the_file_PARSES_and_re_emits_stably`. `git diff 1b895db..HEAD --
  docs/verification/README.md` is empty. This is BP0 exactly: the decision rule moved and the
  document citing it did not move in the same commit. **It is the first item on this list and
  it is the one I would fix first**, because the ladder document is where a reader who is not
  the author goes to find out what G3.2 claims. **Closed when** the bullet names the three
  digest lines and the four structural assertions, and the parse-and-re-emit sentence is gone
  or is labelled as the assertion that does not carry the gate.
* **C18. `tests/verification/rung3/test_platform_deck_export.py:320-322` says the twelve
  mutations are "the reviewer's eleven, plus the coplanarity case".** They are eight of the
  eleven plus four new ones. Absent: every body z negated, a buoy moved onto the diagonal, a
  duplicated `name` key. I measured all three and all three are caught by the digests, so the
  table is weaker than it says and the gate is not. **Closed when** the docstring counts what
  is there, or the three are added.
* **C19. `tests/test_report_guard_states.py:507-510` asserts "CI is unaffected ... guards were
  1000 passed at the reviewed commit", with no triple, and it is already stale.** At `4708cc2`
  the same job is 8 failed / 913 passed. CW0: a claim about this repository written in a
  comment is a test, a triple, or deleted. **Closed when** the sentence states the mechanism
  (`actions/checkout` produces a directory) without the count, or carries the count as a
  triple that something regenerates.
* **C20. The header's `source` line is unguarded by the always-run half of G3.2.** Measured:
  `platform_rao_pilot.py` changed to `other_thing.py`, all nine checks green. `--check` does
  compare it, so R584's condition is met and this is the residue. **Closed when** the header
  test asserts the source line, or the docstring's "declares its provenance" is narrowed to
  the four things it actually reads.
* **C21. Any line beginning `#   exported` is invisible to both halves of G3.2.**
  `scripts/export_platform_deck.py:227-228` filters the prefix from both sides, and the header
  test does not read it. Arbitrary text can live there. **Closed when** the filter matches the
  generated line's full shape rather than its prefix, or the blind channel is named at the site.
* **C22. Revision 5 carries no `--check` triple, and the README says the procedure's output
  goes in the step report.** The cells are in the commit message at `b5602d6` instead. **I ran
  it myself and it passes -- the output is in the Carried section above -- so nothing about the
  deck is in doubt; what is missing is the record at the commit.** Closed when the report
  carries the `--check` output at its own commit, per `docs/verification/README.md:97-99`.
* **C23. The report's own suite figure does not describe the commit it is published at.**
  §5 reads "*Whole suite at `475c224`: 2573 passed, 2 failed*" plus 10 in the excluded set; at
  `4708cc2` my run is 2768 passed / 8 failed and neither of the two vocabulary-corpus reds it
  names still exists. The measurement is structurally taken one commit early because the report
  is inside what it measures, which is a known seam -- but the line as written asserts a state
  the judged tree is not in. **Closed when** the line names the commit it was taken at *and*
  says that the report commit that follows it may move the count, or the figure moves to the
  closure artifact.
* **C24. Revision 5 has a duplicated heading and a duplicated clause.** `## 0. CI, for the
  commit under review` immediately above `## 0. CI at 2e24459 ...`, and "*The escalation was
  answered by scope, not by slipping the date — and the escalation was answered by scope, not
  by slipping the date (DW0)*". Generator seams, not content. **Closed when** each appears once.
* **C25. `DW0`, `DW4` and `DW5` are directive ids that nothing in the repository defines.**
  `grep -rn "DW5" docs/` is empty; `DW0` appears only as a parenthesis on `docs/milestones/
  F3.md:321` and a row in `F2a.md:229`; `DW4` appears nowhere. DW5 is described to me as "the
  whole of" the next work and the plan's §3.2 list is what it will be written from. **Closed
  when** the DW directives are transcribed into F3 §0 beside DJ and DV, verbatim, in the way
  DV0-DV2 already are -- a plan whose executable list cites an id no reader can look up is the
  condition R576 and R582 were both about.
* **C12 (carried).** `floatfea/io/froude.py::_refuse_uncovered` refuses a genuinely scalar 2-D
  array of trailing width 4, 5 or 6; the docstring documents the 1-D residual and not this.
* **C14 (carried).** `docs/reports/F2/step-7.md:1087` still says F3 closes 10 October, in
  revision 4's paragraph; the plan has said 13 October since `772f01e`. Revisions are
  append-only, so BP0's "regenerated or withdrawn in the same commit" needs the withdrawal
  written in place.

## Tolerances touched

**None.**

```
cmd  git diff 1b895db..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 1b895db..HEAD -- floatfea
out  (no output)   -- nothing under floatfea/ moved at all this round
cmd  git diff 1b895db..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff 1b895db..HEAD -- .github
out  (no output)
cmd  git diff 1b895db..HEAD --name-status
out  10 files: the plan, F2a, the report and its answers json, the deck YAML (one date
     line), the export script, two goldens, the guard-state harness, the rung-3 module
```

**No conftest and no plugin was added or changed, so CH2's reading has nothing new to read**,
and the one existing conftest is byte-identical across this round. I checked the rung-3 module
for the six forgery channels by hand anyway, because it is the module whose green I am relying
on: it defines no `pytest_` hook of any kind, and its only pytest surface is one
`@pytest.mark.parametrize` and one `importorskip`.

**The rung-3 module reads `ROUNDOFF_IDENTITY` at FOUR sites now (`:268`, `:275`, `:291`,
`:296`), two more than last round.** All four are relative and dimensionless --
`min(|x|,|y|)/radius`, `(max-min)/max` over the four arm radii, `dist(a,b)/max(1,|a|)` on the
joint coincidence, and `(max z - min z)/max|z|` on the joint plane -- which is the entry's
declared form. **I measured the margin on the two new ones:** every joint gap is `0.000e+00`
against a threshold of `1e-14`, and the defect it exists to catch, a 1 mm offset at model
scale, reads `1e-3` relative -- `1e11` times the threshold. The `z`-spread assertion is the
one to watch: it is `(max - min) <= ROUNDOFF_IDENTITY * max|z|`, measured `0.000e+00` against
`4.934e-15`, and **its counter-case is an assertion-domain hole rather than a margin** -- see
the `named` rows in the corpus, where a uniformly lifted plane is coplanar and invisible to it.
No value was added, none was changed, nothing was widened.

**`tests/goldens/platform_deck_digest.txt` is new and it is a golden, not a tolerance.** Three
hashes, two counts, two order strings; no threshold, exact comparison. It is the right shape
for what it is and the ruling above says why.

## What I built to break it

Everything ran from the session scratch directory outside the repository. Nothing was written
into the tree except this verdict and the corpus.

1. **An independent geometry probe over the exported deck**, resolving all 16 joint attach
   points through both bodies. It reproduced every one of DW1's six figures to the digit, plus
   the 120-degree tripod, the `84.45185` m buoy offset, and the `51.0562 m / 11.6747 deg`
   platform-reference vector. This is the measurement DW1 made the plan conditional on and I
   did not take it from the report.
2. **Thirty-three mutations of the committed YAML against the SHIPPED check functions**, called
   directly with `DECK_YAML` repointed, which is the same mechanism the module's own counter
   uses. **Two are caught by nothing: a CRLF rewrite (R589) and a falsified `source` header line
   (C20).** A clean-file control ran first and all nine checks passed on it, so the harness can
   tell green from red.
3. **The published ablation, reproduced, and then run three more ways.** 2 of 12 with
   CONTENT+BYTE removed -- exactly the figure. 3 of 12 with all three digests removed. 17 of 33
   and 20 of 33 on the unseen set. 6 of 33 with only the digests, all six header edits.
4. **`--check` on my own reading of the tree**, with `../HSP-runs` at `floatfea-ref-1` @
   `25de7ce` and `git status --porcelain --untracked-files=no` empty. Exit 0, header included.
5. **The untracked-shadow reading on the preflight** (R588), traced through
   `sys.path.insert(0, ...)` and the study's two bare-name imports. I did not write into
   `../HSP-runs` to demonstrate it; the mechanism is the two lines and the two imports.
6. **The CI run at the judged commit, polled to completion**, which is what turned a PASS into
   a HOLD. Fourteen polls over seven minutes.

**The adversarial case that passed when it should have failed is the CRLF rewrite** -- all nine
checks green on a file whose every line ending changed -- and the reason it is R589 rather than
a demand to change the behaviour is that the normalisation is correct and only the words are
wrong. **The finding that outranks everything in the report is R587**, which is not adversarial
at all: I added the body masses up.

## Corpus this round (BE3)

**`tests/corpus/platform_model_skeleton.txt`, batch 19, committed separately at `02407b5`,
before this verdict.** Fifty-five entries, none seen by the implementer, in four sections: the
twenty-nine mutations the module's twelve-entry table does not contain, the ablation run four
ways, the model F3 section 3 now describes, and the generator after R584.

**In scope under DE2** -- "from F3 -- the platform model" -- so it is not an apparatus corpus,
DR1 does not defer it to `docs/milestones/F2a.md`, and nothing is transcribed. It is a separate
file from batch 18 because batch 18 is about the committed FILE and this is about the MODEL.

**THE COVERAGE MEASUREMENT: 33 of the 55 entries assert that a defect must be caught by
something shipped. 26 are caught. 7 are not.** That number replaces the module's own, and the
comparison is the point of the round:

```
cmd  the module's own twelve, all shipped checks
out  0 of 12 missed
cmd  thirty-three mutations the module's table does not contain, all shipped checks
out  2 missed -- CRLF line endings, and a falsified `source` header line
cmd  the same thirty-three with the CONTENT and BYTE digests ablated
out  17 of 33 missed, against 2 of 12 on the author's own table
judge  the gate is much stronger than it was and the PUBLISHED COVERAGE FIGURE IS STILL A
       PROPERTY OF THE TWELVE-ENTRY TABLE. Nothing is wrong with the ablation; it is that
       "exactly two" is a statement about what twelve mutations happen to contain.
```

**The seven missed, named, because a count without its members is not a measurement:** the CRLF
rewrite (R589); the falsified `source` line (C20); a uniformly lifted joint plane, invisible to
every *named* assertion because the coplanarity test asserts a spread and not a datum; an
untracked module on the study's import path (R588); the `#   exported` blind channel (C21); the
absence of a `--check` record at the judged commit (C22); and the README still describing the
retired gate (C17).

**Thirteen entries are questions rather than mutations** (`expect=explain`) and they are the
half I would read first, because the frame has not been built: whether the buoy mass is in the
model, what is at the tip of a twelve-cantilever tripod, whether the one designed section in the
model is loaded by what designed it, the three rigid-link lengths, and the fact that a planar
frame gives a vertical load at a buoy joint no axial path at all. **Two of them became R587.**

**The standing measurement.** `cmd grep -h "^id=" tests/corpus/*.txt | wc -l`; `out` 1253
entries across 20 files. Of the apparatus corpus, the untranscribed count stays where DR1 put
it and is reported by the corpus-agreement test rather than written down here.

## My own instructions (4b)

```
cmd  git diff 1b895db..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git log --format="%h %s" 1b895db..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git log --format="%h" 1b895db..HEAD -- docs/reviews
out  (no output)
```

**Nothing touched them this round, and no commit in this round touches both `floatfea/` (or
`tests/`) and `docs/reviews/`.** I read the four commits' file lists individually rather than
taking the aggregate: `63046e5` is plan and ledger only, `b5602d6` is the script, the module and
two goldens, `475c224` is the harness alone, `4708cc2` is the report and the deck's date line.
**I have complied with both DU1 rules:** the judged commit is restated bolded and backticked at
the top, and every blocking finding heads `**R<n>. (<class>, blocking) ...**` with the status
inside the parentheses, which is the shape `scripts/check_carried.py`'s `^\*\*(R\d+)\.` and
`test_report_carried.py`'s `_blocking()` both parse.

## On the criterion, and two things that leave the loop

**CZ0 is right and it paid again.** Nine closure items from verdict 70 landed in one commit, five
of them are closed, and the round went to the deck, the gate and the plan. Three of my four
findings are one deletion, one plan paragraph and two docstrings between them.

**WHERE I AM STRETCHING CZ0, SAID ONCE AND NOT ARGUED.** R587 is a plan finding and R582 was.
Neither is literally one of (a)-(d). I am classing it `(plan, blocking)` on verdict 70's
precedent and for its reason: a plan that says two different things about 85.6% of the model's
mass makes DW5's first instruction ambiguous, and DW5 is the whole of the next work. **I am not
asking for a ruling and this does not become another round.** If the technical supervisor
prefers it as a closure item, say so and it becomes one.

**TWO THINGS THAT GO TO XABIER THROUGH THE IMPLEMENTER, not into another round.**

**One: F3's step reports have nowhere to go that any guard can see, and the interim answer is
ugly.** `tests/test_report_carried.py:67-68` hardcodes `docs/reviews/F2` and
`docs/reports/F2`; `scripts/write_verdict.py` refuses a step with no report under the milestone
it is given; `docs/milestones/F2.md:10` carries the only `step-under-execution` marker. **Nothing
goes RED when F3 opens -- the guards simply go on reading F2 step 7 forever, which is the
assertion-domain failure in its purest form: green while checking nothing.** DR1 permits only
deletion, and R564 already named this exact shape as one of the four findings the carry rule
produced against itself. **My interim ruling, so the implementer is not blocked: keep writing
into `docs/reports/F2/step-7.md` and `docs/reviews/F2/step-7.md` as revisions, exactly as
revisions 5 and verdicts 54, 55, 70 and this one do, with DD1 as the precedent.** It is wrong and
it works. The durable choice -- re-point two path constants, or delete the carry apparatus and
let `tests/test_collected_set_golden.py` carry what remains -- is above me and above the
implementer, and I would take the deletion.

**Two: the escalation condition fired again and the answer has already been given once.** DW0
answered the last one by reducing scope and holding 13 October, and the reduction is real work.
This round ends carrying blocking items for the third consecutive time. **I am not asking for
another scope cut** -- the remaining three items are a deletion, a plan paragraph and two
docstrings, and none of them costs a day. What I will say plainly is that **nothing has yet
touched the platform MODEL.** The deck is exported, measured and gated; that is the input. The
frame, the sections, the rigid links and G3.1a are all still ahead of 13 October, and R587 is
the reason the first line of that work cannot be written today.

## Carried for the next step

Nothing carries yet -- **this is a HOLD, not a close.** The four findings above are answered
before anything else and the step does not advance. If a third verdict on this step arrives with
any of them open, they carry by name then.

## Next step opens when

**This step stays open. Four things, and three of them are small.**

1. **R586: delete `assert len(EXPECTED) >= 5, (...)` at `tests/test_report_carried.py:454-457`**,
   with the reason at the site -- a verdict may carry fewer than five findings and verdict 70
   carried four correctly. A DELETION under DR1: no smaller floor, no parametrisation. The two
   assertions above it stay. **Then CI at the answering commit is green**, and 8 failed / 913
   passed becomes 0. Anything less than green CI at the answering commit is (d) again.
2. **R587: one `plan:` commit** making section 3.2 item 5 and section 3.4 agree on whether the
   twelve buoy bodies' mass is in the first result, and naming the rigid-link lengths that
   follow. DK0 applies: it buys no fresh three.
3. **R588 and R589: one predicate and two docstrings.** R588 either refuses untracked files on
   the three `sys.path` directories or deletes the sentence that says they cannot matter. R589
   says what the digest hashes. Neither needs new apparatus and neither changes behaviour.
4. **C17 to C25 plus C12 and C14 land in one closure commit** and are not re-reviewed
   individually. C17 first: the ladder document still describes G3.2 as the assertion R583
   retired.
5. **The next report's header is `Answers: verdict 71 @ <the commit THIS verdict is committed
   at>`** -- not `4708cc2`, not `02407b5`. The generators read `VERDICT_TEXT` at the commit the
   header names and this file is overwritten each round, so naming the judged commit makes every
   generator read verdict 70. That is C13's ruling and this is it as a command. State the judged
   commit in the report's own prose instead.
6. **Push, wait for the run to complete, then ask for the verdict.** The run at `4708cc2` was
   `in_progress` when this review began and it is the reason this is a HOLD rather than a PASS
   written on a local green. A run that has not finished is not a pass.
