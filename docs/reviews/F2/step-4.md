# Review — F2 step 4
Reviewed commit: 1bc652a837c906fe9a36d139bdf6b3f27f076518
Verdict: HOLD
Tests: 1433 passed, 0 failed, 0 skipped   (my run at `fc30b71`, `python -m pytest -q`,
131.64 s. With my twenty-third-round corpus applied: **1463 passed, 1 failed**.)

**Reviewed code commit: `fc30b71`.** The header stamp is `1bc652a`, my own corpus
commit, made immediately before this verdict and touching no code.

Twenty-third pass, and a short one by design: range `eec7113..HEAD`, one commit,
two generated artifacts. Three of the four things I was asked to check are clean.
The fourth is not, and it is the one the round was about.

```
cmd  git diff eec7113..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched. Nothing added, nothing deleted.
cmd  git diff eec7113..HEAD -- floatfea/tolerances.py
out  (empty)  -- not a comment, not a value. The file is byte-identical.
cmd  git diff eec7113..HEAD -- floatfea/ tests/ --stat
out  tests/regression/g22_exempt_pair_responses.json | 3 +++   AND NOTHING ELSE.
     floatfea/ is untouched for an eighth consecutive round.
cmd  git diff eec7113..HEAD --stat
out  docs/milestones/F2_figures.md 36 (18 +, 18 -) ; the golden file 3 +
cmd  python scripts/regen_figures.py --check
out  regen_figures: up to date  -- exit 0
cmd  python -m pytest -q tests/test_plan_figures.py
out  31 passed
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md | tail -1 ; newest verdict
out  :3523 verdict 21 @ ec09ea6 ; newest verdict is 22 @ eec7113
```

**Item 1b, performed, and it does NOT trigger.** The report names verdict 21
while the newest is verdict 22 -- but no report revision landed in this range, and
verdict 22 is the PASS that judged the report *as it stands*. The report
legitimately predates the newest verdict and makes no `Carried` claim against it.
`tests/test_report_carried.py` is green at `fc30b71` and green under my corpus.
Not a HOLD on 1b.

**The ruling, first.** The regeneration itself is correct and I could not fault
it. The figures file is what a fresh run produces, no tolerance moved, no code
moved, and the golden change is three insertions with zero deletions and zero
moves from one new entry -- a corpus round, not a regeneration to match new
output. Every one of your four measurements reproduces at my run.

**And the claim I was asked to refute is refuted.** "R194's fix replaced the
retyped figures with names, so nothing went stale" is true of
`floatfea/tolerances.py:495-513` and false of the repository. R194's fix covered
one paragraph in one file. The locked plan carries a *different* paragraph, in
present tense, that justifies the same constant and retypes five of the figures
this commit moved -- including a **solved boundary that the shipped assertion now
contradicts at this commit**. That blocks under BP0, which says in terms that a
figure citing a rule that moved is regenerated or withdrawn *in the same commit*.

## Carried

Every item from the twenty-second verdict (`PASS @ 9d70483`, committed
`eec7113`), re-measured at `fc30b71`.

- **R205 -- ANSWERED, and it is what this commit is.** The corpus round is
  regenerated; `detection_edge` `3.9459e-14 -> 3.6425e-14` at
  `ch_edgemin_D0p0758_roll1p05_aniso9p4e5`, `counter_defect_over_edge`
  `2.534e+07x -> 2.745e+07x`, `counter_headroom_room` `2.37x -> 2.19x`. All three
  reproduce at my run to the published digits. `PATCH_TEST_COUNTER_HEADROOM =
  6.0e7` **holds**, and I re-solved rather than read it:

  ```
  cmd   the SHIPPED test_the_counter_DEFECT_SIZE_cannot_be_raised, CD varied,
        one variable moved, at fc30b71
  out   CD  2.00e-6 PASS  2.10e-6 PASS  2.18e-6 PASS  2.185e-6 PASS
            2.19e-6 FAIL  2.20e-6 FAIL  2.36e-6 FAIL  2.3675e-6 FAIL
  rule  ratio = CD / edge <= PATCH_TEST_COUNTER_HEADROOM
  out   edge 3.6425e-14 at ch_edgemin_D0p0758_roll1p05_aniso9p4e5;
        boundary = 6.0e7 x 3.6425e-14 = 2.185489e-06
  ```

  The constant holds with `2.19x` of room. The **plan sentence describing that
  same boundary does not** -- see R207.
- **R206 -- OPEN, and no longer only about a past tense.**
  `floatfea/tolerances.py:511` still retypes `2.534e+07`; the live figure is now
  `2.745e+07x`. Tensed as history, so still true as history, and I am not
  re-raising it as blocking. It stays 4a with its closing condition unchanged.
  But it is now the *third* retyped figure in this file, and R208 below is the
  one that is not tensed as history.
- **R200, R201, R202, R203, R204 -- OPEN at 4a, correctly.** Nothing in this
  commit touches them and nothing was expected to.
- **R198, R199 -- 4a, accepted, unchanged.**
- **R181, R189, R190, the R170/R171 remainder, R172, R159, R162, R151, R152 --
  4a, unchanged from my endorsement.**
- **R134, R135, R137 -- OPEN, UNTOUCHED**, eighteenth round.
- **R129, R131, R132, R136, R138, R139, R148 -- as declared.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Recorded as a disagreement.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or
  later.
- **R68 standard -- MET, seventh round.**
- **The witness channel -- STILL UNAVAILABLE.** `git remote -v` is empty. Twenty-
  three consecutive reviews by one reader. Unchanged, and still not a pass.

## Findings

**R207. (BLOCKING) The locked plan retypes five figures this commit moved, in
present tense, in the paragraph that justifies `PATCH_TEST_COUNTER_HEADROOM =
6.0e7` -- and one of them is a SOLVED boundary that the shipped assertion now
contradicts. `2.36e-6` is published as passing; measured at this commit it
FAILS.** `docs/milestones/F2.md:579-591`.

```
code  :579-581 "Measured by the shipped runner: the smallest edge is `3.9459e-14`
      at `band_edge_isotropic_bracing`, and the shipped `1e-6` sits `2.534e+07x`
      above it. `PATCH_TEST_COUNTER_HEADROOM = 6.0e7`, so the shipped value has
      `2.37x` of room."
      :582-583 "The boundary is SOLVED rather than quoted: `2.36e-6` passes and
      `2.38e-6` fails, against `6.0e7 x 3.9459e-14 = 2.3675e-6`."
      :591 "`2.37x` is the room that leaves for one."
cmd   python scripts/regen_figures.py --check ; the generated table at fc30b71
out   detection_edge 3.6425e-14   detection_edge_at
      ch_edgemin_D0p0758_roll1p05_aniso9p4e5   counter_defect_over_edge
      2.745e+07x   counter_headroom_room 2.19x
rule  the shipped assertion, run with CD varied one variable at a time
out   2.36e-6 -> FAIL. The boundary is 2.185e-6 < CD <= 2.19e-6, i.e.
      6.0e7 x 3.6425e-14 = 2.185489e-06, NOT 2.3675e-6.
judge FIVE numbers in thirteen lines, every one of them false at this commit:
      3.9459e-14 (twice), band_edge_isotropic_bracing, 2.534e+07x, 2.37x
      (twice), and the solved pair 2.36e-6 / 2.3675e-6. The entry name is the
      interesting one -- `detection_edge_at` has been `aaa_band_edge_twin` since
      the figures file was created at ba4c21a and is `ch_edgemin_...` now; it has
      NEVER been `band_edge_isotropic_bracing`, which is `clean_worst_entry`, a
      different figure.
```

This is not a prose blemish. It is the derivation a reader consults when they ask
why `6.0e7` is the right number; it is stated as a **solved** boundary, the one
form this repository treats as stronger than a quoted one; and the solution
published is wrong by 8% in the unsafe direction -- it claims `2.36e-6` is
admissible when the shipped test rejects it.

**The mechanism, and it is the finding underneath the finding.** `git blame` puts
these lines at `d920a8d` (BR), which is *before* BT0 created the generated
figures at `ba4c21a`. BT0 converted the sections at `F2.md:507-556` and
`:654-750` to `{{fig:...}}` -- 29 references -- and left this section retyped. Its
own docstring says so: "SCOPE, and it is deliberately narrow: the figures that
move, not the whole plan." The one section BT0 skipped is the one that justifies
a shipped tolerance, and this commit is the second consecutive round in which a
reviewer corpus moves every number in it.

**Closed when** `F2.md:579-591` cites `{{fig:detection_edge}}`,
`{{fig:detection_edge_at}}`, `{{fig:counter_defect_over_edge}}` and
`{{fig:counter_headroom_room}}` by name, and the solved-boundary sentence either
carries the boundary re-solved at the current edge (`2.185e-6` passes, `2.19e-6`
fails) or is rewritten so that it does not quote an absolute value that moves
with the corpus. Half of this item is not the item: **all five sites**, or a
statement of which was left and why.

**R208. (BLOCKING) `floatfea/tolerances.py` states the margin of
`PATCH_TEST_EXACTNESS = 5e-15` twice in present tense, and both numbers are now
wrong -- one of them by 2.6x.** `floatfea/tolerances.py:405` and `:413`.

```
code  :413 "Worst clean value over the corpus: 0.0887x of this ceiling."
cmd   the generated table at fc30b71
out   clean_worst_ratio 0.0982x  at ch_edgemin_D0p391_rollm0p73_aniso1p4e5
judge stale as of THIS commit, and stale in the paragraph that says, two lines
      earlier, that the figures are generated into docs/milestones/F2_figures.md.
      `clean_worst_ratio` exists; it is not cited.

code  :405 "5e-15 is the geometric centre of the band, 4.47e-15 rounded up:
      26.8x above the worst clean corpus entry and 21.5x below the smallest
      defect response."
cmd   the shipped runner own printed line at fc30b71
out   "CEILING 5.000e-15  worst clean 4.9119e-16 (2.21 eps,
      ch_edgemin_D0p391_rollm0p73_aniso1p4e5) = 0.0982x"
judge 5e-15 / 4.9119e-16 = 10.18x, not 26.8x. At the previously published
      0.0887x it was 11.27x -- so 26.8x has not described this repository for
      many rounds, and nothing re-took it. Present tense throughout.
cell  and my corpus round moves it again, one variable moved (7 entries added,
      no code): clean_worst_ratio 0.0982x -> 0.1142x at
      ci_plateau_D0p0689_roll1p017_aniso9p6e5, i.e. 8.75x.
```

**The ceiling itself holds** -- 8.75x of margin is not a small number and I am not
asking for `5e-15` to move. What is wrong is that a reader deciding whether
`5e-15` is defensible is told the margin is `26.8x` when it is `10.2x` and
falling, and told the worst entry sits at `0.0887x` when it sits at `0.0982x`.
This blocks under the truth-of-a-published-figure clause and under the tolerance
clause: it is the justification located for a shipped accuracy tolerance.

**Closed when** `:413` cites `clean_worst_ratio` by name, as `:495-498` already
does for the headroom entry, and `:405` either drops `26.8x` or states the margin
as the generated figure at this commit with the derivation-time value marked as
history. Both sites.

**R209. (BLOCKING) The Reason paragraph for `PATCH_TEST_COUNTER_HEADROOM` ships a
directional claim that the locked plan records as WITHDRAWN, that is impossible
by the selection rule own construction, and that this round own data refutes in
the opposite direction.** `floatfea/tolerances.py:498-501` against
`docs/milestones/F2.md:586-590`.

```
code  tolerances.py:498-501 "The margin is eaten from BOTH sides -- a harder
      corpus entry raises the minimum edge and loosens this, but a formulation
      change that IMPROVES sensitivity anywhere lowers it and tightens it"
code  F2.md:586-588 "**The reason for `6.0e7` is the improvement side only, and
      the sentence claiming otherwise is withdrawn.** It read 'a harder corpus
      entry raises the edge and loosens the guard'; under a MINIMUM selection
      that cannot happen"
cmd   git blame -L 496,502 floatfea/tolerances.py ; git blame -L 586,590 F2.md
out   tolerances.py:499-501 = f1b226b (2026-09-08); F2.md:586-590 = d920a8d
      (2026-09-07). The withdrawn sentence was RE-INTRODUCED into the tolerance
      comment, with the word "minimum" added, the day after the plan withdrew it.
code  the selection: `edges = sorted(...); smallest = edges[0][0]`
      (test_corpus_configurations.py:1335-1336) -- a minimum over a growing set
      is monotone non-increasing. "Raises" is impossible by construction.
cell  and measured, one variable moved -- 7 corpus entries added at 5554f0d, no
      code change (git diff eec7113..HEAD -- floatfea/ is empty):
out   detection_edge 3.9459e-14 -> 3.6425e-14, counter_headroom_room 2.37x ->
      2.19x. The corpus grew and the margin TIGHTENED.
cell  repeated with my own 7 entries at 1bc652a, same control:
out   3.6425e-14 -> 3.6275e-14, room 2.19x -> 2.18x. Tightened again.
judge Two rounds, two corpus additions, two tightenings, zero loosenings, and a
      construction that permits nothing else. "Eaten from BOTH sides" is a causal
      claim about why 6.0e7 is the value it is (BG0), and the cell that isolates
      it says one side.
```

I flagged the phrase at the twenty-second verdict as something to re-read in step
5 and did not measure it. This round is the measurement, and it goes the other
way. It blocks because it is the Reason paragraph of a shipped tolerance, because
CLAUDE.md is explicit that such a paragraph is a causal claim, and because the
plan and `tolerances.py` now disagree in writing about the same constant.

**Closed when** `tolerances.py:498-501` states the one direction that is
measurable -- a corpus round can only lower the minimum edge and tighten this,
and a sensitivity-improving formulation change does the same -- or the plan
withdrawal at `F2.md:586-588` is itself reopened with a construction that permits
the other direction. Not both sentences standing.

**R210. (recordable, 4a) The commit message "Nine figures move" is not what its
own pasted `cmd` prints: eighteen rows moved.** `fc30b71` commit body.

```
code  "Nine figures move; every tolerance comment that would once have gone stale
      with them now cites them by name" / "cmd  diff of docs/milestones/
      F2_figures.md"
cmd   git diff eec7113..HEAD -- docs/milestones/F2_figures.md | grep -c "^-|"
out   18
judge The `out` block enumerates eight lines covering nine figures and omits nine
      more that the named command prints: below_ceiling_dropped_flip,
      below_ceiling_wrong_dof_index, below_ceiling_dropped_shear_parameter,
      below_ceiling_one_element_scaled (all four denominators 132 -> 139),
      exempt_total 58 of 528 -> 61 of 556, exempt_by_defect 11/31/16 ->
      12/32/17, and boundary_margin_bases 127 -> 134. The count is inherited from
      my own verdict 22, which said "reddens on nine rows" and was also counting
      the interesting subset rather than the diff. UNDER-claimed, not
      over-claimed, and the substance is right -- but the second half of the
      sentence is the claim R207 and R208 refute, and it sits beside a count that
      does not reproduce.
```

**Closed when** the count is what the named command prints, or the sentence says
which subset it is counting.

## Tolerances touched

**None. The file is byte-identical.**

```
cmd  git diff eec7113..HEAD -- floatfea/tolerances.py
out  (empty)  -- not one line, comment or value
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` `:515` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | the raised-defect counter, injected and registered in both cells | `tolerances.py:491-514` and `F2.md:561-599`. **HOLDS** -- I re-solved the boundary at the new edge: `2.185e-6` passes, `2.19e-6` fails, `2.19x` of room. The tolerances-file half is clean; the plan half is **R207** and the direction sentence is **R209**. |
| `PATCH_TEST_EXACTNESS` `:430` | `5e-15` | `5e-15` (unchanged) | relative field error, dimensionless | `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, injected | `tolerances.py:396-429`. **HOLDS** at `10.18x` above the worst clean entry, `8.75x` under my corpus. The two numbers stating that margin are **R208**. |
| `DELTA_CALIBRATION_ULP` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `DELTA_CALIBRATION_ULP_COUNTER = 5.0`, injected | `calibration_ulp_worst` is `2.000 ULP` at this commit and `2.000 ULP` under my corpus; the histogram gains three entries at 0/1/2 and nothing above. The `2x` headroom is not threatened. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:626` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected | unchanged; the golden file grew by three keys and the drift gate is green on all 54. |

**The golden file, checked as its own question (CLAUDE.md, section Testing).**
Three insertions, zero deletions, zero moved values -- I diffed it rather than
reading the claim.

```
cmd  git diff eec7113..HEAD -- tests/regression/g22_exempt_pair_responses.json
out  +3 lines, all "ch_edgefloor_D0p068_L387_skew|{dropped_flip,
     dropped_shear_parameter,wrong_dof_index}". No line removed, no value
     changed.
cmd  python -c "json.load(...)" -- key count and split
out  54 keys; dropped_shear_parameter 25, wrong_dof_index 17, dropped_flip 12.
     54 = `exempt_detected`; 12+25+17 reconciles against `exempt_by_defect`
     12/32/17 with 7 of the 32 shear pairs exempt-and-undetected.
judge a corpus round, not a regeneration to match new output. The written
     explanation is in the commit body. It is NOT in a step report, because no
     report revision landed in this range -- see "Next step opens when".
```

**What held.** These reproduce at my run: `1433 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` exit 0; `tests/test_plan_figures.py` 31 passed;
`floatfea/` byte-identical; `tolerances.py` byte-identical; my instructions
byte-identical; the golden diff exactly as stated; all three figures named in the
task, to the published digits; the counter-defect boundary re-solved at
`2.185e-6`. These do **not**: the plan boundary sentence (R207), the two
`PATCH_TEST_EXACTNESS` margin figures (R208), the both-sides direction claim
(R209), the commit body figure count (R210).

## Next step opens when

**Not now. Step 4 re-opens on R207, R208 and R209; step 5 does not begin.**

The BU0 head, named as asked: **R207 is the head**, and the reason it is not
apparatus is one measurement. `docs/milestones/F2.md:582-583` publishes a
**solved** boundary -- `2.36e-6` passes -- and the shipped assertion at this
commit rejects `2.36e-6`. That is a claim measurement refutes, about the decision
rule of a shipped tolerance, in the locked plan. It is not a parser reach and not
a docstring precision about its own machinery. R208 and R209 attach to the same
head: R208 because the margin of `PATCH_TEST_EXACTNESS` is misstated by 2.6x in
the file that owns it, R209 because a Reason paragraph asserts a direction its own
selection rule forbids and two consecutive corpus rounds have measured going the
other way. R210 is apparatus and goes to 4a with the six already there.

**The three conditions, site by site.** `F2.md:579-591`: four `{{fig:}}`
references and the boundary sentence re-solved or rewritten -- five sites, each
listed with its hunk or stated as left and why. `tolerances.py:405` and `:413`:
both, not one. `tolerances.py:498-501`: the direction reduced to what is
measurable, or the plan withdrawal reopened.

**And the regeneration will have to happen again**, because my corpus round moves
the same figures a third time: `detection_edge` `3.6425e-14 -> 3.6275e-14`,
`clean_worst_ratio` `0.0982x -> 0.1142x`, `counter_headroom_room` `2.19x ->
2.18x`, thirteen rows in all. **That is the argument for R207 stated as a schedule
rather than as a principle.** These numbers have moved in each of the last two
rounds and will move in the next; a paragraph that retypes them is wrong within
one commit of being written, every time, and the mechanism that fixes it --
`{{fig:}}` -- already exists, ships, is tested, and is used 29 times in the same
file.

**A process note, recorded and not blocking.** `fc30b71` changes a file under
`tests/` and landed with no revision of `docs/reports/F2/step-4.md`; the written
explanation the golden-file rule requires is in the commit body instead. I asked
for the regeneration at R205 and called it "the next report's work", so the
routing is on me as much as on the implementer. Doing it as a standalone commit
with the triples in the message is defensible and I am not holding on it. When
step 4 closes, the report revision answering R207-R209 should carry the
golden-file explanation too, so that it is somewhere a reader looks.

**Adversarial corpus (BE3): 7 new entries committed, all unseen by the
implementer; every field measured at `fc30b71` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **170** entries, 145 solved,
committed separately at `1bc652a` and touching no code. Full suite with the
corpus applied: **1463 passed, 1 failed** --
`test_the_generated_figures_are_not_stale`, and only that.

The coverage measurement, stated plainly: **0 of my 7 new entries produce a new
exempt-and-detected pair, so BS2 golden file is untouched and caught 0.** BT0
reddens on thirteen rows. What the entries measure:

* **The detection edge is a plateau, not a descent, and it is scale-free.** 1100
  candidates over two independent seeds through the shipped `_detection_edge`:
  500 broad reached `4.0721e-14`, 600 perturbed around the shipped minimum
  reached `3.6275e-14` -- **0.4% below the published edge after 600 tries in the
  region that produced it**. Four entries span `D` `0.069 m` to `0.787 m`, an 11x
  range of diameter, inside a 12% band of edge.
* **`PATCH_TEST_COUNTER_HEADROOM = 6.0e7` holds, second round running against a
  reviewer trying to break it.** Breaking it needs an edge below `1.6667e-14`;
  1100 candidates got to `3.6275e-14`, a factor of 2.2 short.
* **A symmetry the model has and the residual does not.** For `I_y = I_z` a roll
  about the member axis is a symmetry of the section. Measured: `roll=0`,
  `roll=2pi`, `I_y/I_z=1` with no roll, and `extra=none` give a **bit-identical**
  worst residual `8.051599e-17` and edge `1.013201e-13`; with `roll=1.05` and
  `I_y/I_z=1` the worst residual is `1.207740e-16`, **1.50x**. A path difference
  at `0.016x` vs `0.024x` of the ceiling, not a defect -- and it bounds any future
  roll-invariance claim to a bound at 1.5x, never an identity. Two entries carry
  both halves.
* **The degeneracy guard refuses at every scale.** Directions `1e-9`, `1e-15` and
  `1e-17` off global Z all raise `DegenerateMemberOrientation` against the `0.05`
  rad floor; none falls through to a default construction. The `1e-17` case is
  pinned, because it is the one an underflow in a normalisation turns into an
  exact global-Z member.

**Twenty-three consecutive rounds have found no element defect**, and the reading
is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side.
The element did not move under my input this round either. What moved, again, is
prose about the element instruments.

**The standing question, sharpened.** Verdict 22 asked what deletes the sentences
a round makes stale, and answered it by hand at four sites. This round the answer
is mechanical and already in the repository: `{{fig:}}`, used 29 times in
`F2.md`, absent from exactly the one section that justifies a tolerance. BT0 own
docstring calls its scope "deliberately narrow" and hands the rest to the
claim-carries-its-command rule -- which is a rule nothing runs. Two rounds in a
row, the numbers it hands over have been the ones that moved.
