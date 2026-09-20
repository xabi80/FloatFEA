# Review � F2 step 5
Reviewed commit: a89f149066c746eda41c8a1689114c56e04cc3f3
Verdict: HOLD

**Reviewed commit: `d8ac843`.** Report revision 22, `Answers: verdict 47 @
b375cd0`. The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`a89f149` -- not the commit judged. That is R373, still open; read `d8ac843`.

Tests: **2480 passed, 0 failed, 0 skipped** at `d8ac843` (my run, clean tree,
`python -m pytest -q`, 521.99 s, Python 3.13.15 on Windows).

**AT MY OWN CORPUS COMMIT `a89f149`: 1 failed**, the figures guard doing its
job. `rigid_mode_corpus_frames` `114` to `126`, `rigid_mode_corpus_refused`
`29 of 114` to `33 of 126`, `retired_ratio_over_ceiling_on_corpus` `80 of 114`
to `91 of 126`, `rigid_mode_residual_worst_over_corpus` `1.1410e-16` to
`1.3502e-16`, `rigid_mode_largest_refused` `1.8800e+02` to `1.9951e+02`.
**None of my 12 new frames reddens the gate.**

**Item 1b.** Revision 22 at line 7873 reads `Answers: verdict 47 @ b375cd0`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`b375cd0bb194f3dfd4ab03e5fedfcdbe9e395891`. It is the latest. **Passes.**

**Commits judged: `b83d776`, `78970b7`, `d2a4666`, `fb5a5cf` (plan, RE-LOCKED),
`0a9d54d`, `0fe6f83`, `e1340dc`, `fd56d97`. Report `d8ac843`.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit d8ac843c165c0b082f898755e18d73b1090a3937
out  run 35482244521, event push, conclusion SUCCESS, status completed
cmd  gh run view 35482244521 --json jobs
out  "the verification ladder"       success, 13 steps, 01:46:14 -> 01:48:47
     "lint, unit and guards"         success, 14 steps, 01:46:14 -> 01:55:39
     "CI determinism -- leg"         skipped, 0 steps
     "CI determinism -- ten legs"    skipped, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING,
     with the single-constant gate in the ladder. Not CK2: both ran real
     steps for minutes. The determinism pair is dispatch-only here and is
     recorded as an UNAVAILABLE check at this commit rather than skipped over.
cmd  gh run view 35479925335 --json jobs   -- this round dispatch, at 0a9d54d
out  ten "CI determinism -- leg (n)" success, "ten legs agree" success,
     "the verification ladder" success, "lint, unit and guards" FAILURE
cmd  gh run view 35479925335 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  14 rows, every one a report-or-figure staleness guard at a commit where
     this revision did not yet exist. Nothing in floatfea/, nothing in rung 1.
cmd  git diff --stat 0a9d54d..HEAD -- tests/verification scripts .github
out  scripts/regen_figures.py, 16 insertions 5 deletions -- the `derived`
     marks on three figure rows. R383 advanced; the ten executed legs
     describe the tree under review except for those marks.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
judge R412 IS ANSWERED AND THE ANSWER IS BETTER THAN THE FINDING ASKED FOR.
     Both this round runs are named with their conclusions in the report 0a,
     the conclusion is in the section 0 heading, and two tests were added.
     The tests have holes -- R429, R430 -- but the omission does not recur.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff b375cd0..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction own expectation
cmd  git diff b375cd0..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung green is being written by code in its own directory.
cmd  git diff --stat b375cd0..HEAD -- floatfea
out  floatfea/tolerances.py | 251 ++++++----- -- ONE FILE
cmd  git show --stat on each of the eight commits
out  `fb5a5cf` touches docs/milestones/F2.md ALONE and says RE-LOCKED.
     `78970b7` touches tests/goldens/collected_tests.txt ALONE and its
     message names every moved line with a reason -- that is R409 rule,
     applied, and it is the best commit in the round.
     `b83d776` is the code commit; it touches no plan and no golden.
```

## Carried

Verdict 47 held on R415, R416, R417, R418, R405, R406 and R409, and recorded
R419 and R420. **R415, R416, R417, R418, R405, R406, R409 and R420 are all
answered at the sites their conditions named. R419 is correctly left open and
said so. What holds this step is eight NEW findings, every one of them a
sentence, and five of them written this round.**

- **R415 -- ANSWERED, AND IT IS THE RIGHT ANSWER.** The two constants are
  collapsed rather than justified, which is the first branch of the condition.

```
rule  lambda_7(K_hat) >= RIGID_MODE_BOUND * ||K_hat|| * eps
cmd   python -c "print(10.0*10**1.3)"
out   199.526231496888 -- the product, unchanged to the last digit
cmd   grep -rn "RIGID_MODE_FLOOR\|RIGID_MODE_GAP" --include=*.py . | grep -v tolerances.py
out   nine hits: three retired-record comments, two retired counter sizes
      `counter_response` still reports, and `_floor(..., "RIGID_MODE_GAP")`
      in regen_figures -- which is R428 below. NO ASSERTION READS EITHER.
cell  MY OWN COMPENSATED PAIR, re-run: there is nothing to compensate. One
      constant cannot be moved against itself.
judge THE SECOND HALF OF THE CONDITION IS ALSO MET, in a way I did not ask
      for and that is better. `largest_rigid_eigenvalue` is a figure now,
      floor-class BELOW `RIGID_MODE_BOUND`, so `regen_figures --check` --
      which `tests/test_plan_figures.py` runs inside the suite on every
      machine -- decides the Courant-Fischer composition and can fail.
cmd   my own sweep: 1980 configurations, 12 unit systems x 11 stretches x 5
      sections x 3 subdivisions, asking for DECIDED with the six NOT all
      under the bound -- the vacuous pass the composition rules out
out   ZERO. Closest approach rigid_max/bound = 7.32e-03, a 137x clearance.
      Plus all 114 committed frames and my 12 new ones: zero.
cmd   the tautology claim, checked over all 114 committed frames:
      (below_bound == 6) against (lambda_7 > bound and rigid_max < bound)
out   they disagree on ZERO frames, and they cannot: `below_bound == 6` is
      `w_6 <= bound < w_7` on a sorted spectrum, which is that conjunction
      written out. The claim is an identity and the departure rests on it.
judge THE COMPOSITION IS SOUND AND IT IS NOW ENFORCED. Closed.
```

- **R416 -- ANSWERED.** The clause is withdrawn by name at
  `floatfea/tolerances.py:449-455`, with the cross cell recorded and the
  surviving measurement kept -- a decade of widening takes the margin to
  `1.396`. No live entry claims a discrimination between two constants,
  because there is one. **Closed.**

- **R417 -- ANSWERED at both sites its condition named.**
  `floatfea/tolerances.py:491` now reads "FIVE TIMES stiffer than the floor
  counter at `2.0e-14` -- `0.7` of a decade, not the one and a half decades
  that stood here and in the test that injected it".
  `grep -rn "decade and a half\|one and a half decades" tests/ floatfea/
  docs/milestones/` returns nothing but that record. **Closed.**

- **R418 -- ANSWERED, and the mechanism rather than the row.**
  `as_ratio = floor_class().get(n, ("", None, False))[2]`, declared at the
  `rows.append`. Two guards, one of which injects a log-valued row named
  `a_log_row_named_anything` and checks BOTH classes on the same pair -- a
  real negative control, and I ran it. **Closed.** The comment beside the flag
  is R424.

- **R405 -- ANSWERED at all five sites.**
  `grep -rn "twenty-eight|fifty-six|Sixteen of the|a large minority"` over
  `floatfea/ tests/verification docs/milestones/` returns seven text hits and
  six are past-tense records of the refutation. The counts are `{{fig:...}}`
  wherever they are asserted and the corpus size is read from the file.
  **Closed.** The seventh hit is a typed count at a site the condition did not
  name, and it is R423.

- **R406 -- ANSWERED at the section its condition named.** `:1917` is headed
  `-- **THE RETIRED FORM**` with a block quote saying every present tense below
  is a past tense; the headroom column is `headroom it HAD`; the registry
  sentence is replaced by what `tests/test_counters_are_injected.py` says.
  **Closed.** The section EIGHT LINES ABOVE it is R422.

- **R409 -- ANSWERED at both sites its condition named.** `:1664` states the
  residual-and-bound form; `:1674` reads "V1.1 asserts on the RESIDUAL, not on
  the modes and no longer on the subspace"; "six numbers near zero" is
  withdrawn by name at `:1943`. The golden is its own commit with a
  line-by-line reason and it is the best commit in the round. **Closed.**
  Four sites the condition did NOT name still say the retired thing: R421.

- **R420 -- ANSWERED, and I checked that it can now fail.**
  `dim = zero_modes_under_the_bound(k)` is an independent count: `assert over
  < RIGID_MODE_BOUND` and `assert dim == RIGID + 1` can disagree, because the
  second also requires `lambda_8` above the bound. **Closed.** The docstring on
  the function it calls says nothing may assert against it, which is R425.

- **R419 -- OPEN, correctly, and not claimed.** The per-entry assertion moved
  from `np.isfinite(margin)` to `over > 0.0`, the same statement in the new
  quantity. The split is still asserted only as "both sides non-empty" and the
  `outcome=` field I ship is still unread. My Block A makes this sharper, not
  softer: three of my six window entries are refused and nothing in the rung
  would notice if all 126 were. 4a.

- **R412 -- ANSWERED as a rule.** See the CI block. The two tests it produced
  are R429 and R430.

- **R411 -- OPEN, SIXTH ROUND, OFF BY ONE NOW.** Revision 22 second line reads
  "Commits since the forty-seventh verdict, listed in §10"; §10 is `Carried`
  and the commit list is in §11 at line 8343. It is closer than it has been
  and it is still a pointer that does not resolve. 4a.

- **R410 -- DOES NOT RECUR IN ITS OWN SHAPE.** 4a.

- **R383 -- ADVANCED, NOT CLOSED.** Ten legs executed and agreed at `0a9d54d`;
  `scripts/regen_figures.py` has moved since, by the three `derived` marks.

- **R413, R414, R400, R401, R402, R390, R391, R392, R393 -- OPEN at 4a**,
  correctly listed.
- **R370, R371, R372, R373, R374 -- OPEN at 4a.** R373 bites again in this
  verdict header.
- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350 second
  half, R330, R331, R332 -- OPEN at 4a, correctly listed.**
- **R231, R244, R245, R275 -- OPEN, unblocked.** Step R has not run.
- **R230, R261 -- OPEN by instruction, correctly listed.**
- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a.**
- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement stays at 4a.
- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250, R251,
  R226, R227, R264 and R266 still have no row; R348 territory, unmoved.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394-R399, R403, R404, R407, R408, R388 -- closed earlier**,
  not reopened.

## Findings

**First, what is right, and it is again the larger part of this round.**

**THE GATE IS IN THE BEST SHAPE IT HAS BEEN IN AND I COULD NOT BREAK IT.** One
constant, one bound, one counter, and a departure from my own directive that
is correct. I attacked the composition the whole thing now rests on -- 1980
configurations asking for a DECIDED frame whose six are not all under the
bound, the vacuous pass -- and found none, closest approach 137x. The
tautology the departure rests on is an identity, not an empirical claim, and
it holds on all 114 frames. The 35-way re-expression of a real mechanism is
35 of 35 refused; I reproduced it. The counter detection edge is a linear
family and it is SOLVED, not sampled: `lambda_7 = 1.2445e15 * size`, so the
give-back at which the gate stops refusing is `1.6032e-13` and the shipped
counter at `1.0e-13` is `1.6033x` under it in DEFECT SIZE as well as in
response. **Deleting the second counter costs nothing** -- the two sat on one
line and the survivor is the harder of the two in both directions.

**And `78970b7` is the best commit this milestone has produced.** One file,
every moved golden line named, the reason for the deletion measured, and the
statement that the previous commit is red on it, said rather than hidden.

---

**R421. (BLOCKS -- the locked plan section 3 GATE REGISTER still defines G2.1
as the retired eigenvalue ratio, and three more sites still say the retired
thing. R409 fixed the two sites its condition named; these four it did not.)**
`docs/milestones/F2.md:51`, `:136`, `:212`, `:1505`.

```
code :51  "| **G2.1** | Six rigid-body modes at zero strain energy, tested as
          an eigenvalue *ratio* against the first flexible mode so it is
          mesh- and unit-independent | V1.1 |"
code :136 "| **V1.1** rigid-body modes | constructed | an eigenvalue *ratio*;
          no external reference needed |"
code :212 "**So G2.1 asserts on the SUBSPACE, not on the vectors:**"
code :1505 "| **5** | **V1.1 rigid-body modes** (subspace) | no spurious
           strain energy | **G2.1** |"
cmd  grep -rn "RIGID_BODY_MODE_RATIO\|RIGID_BODY_SUBSPACE_LOSS" --include=*.py
     floatfea tests | grep assert
out  nothing. Both are retired and `:1917` in this same file now says so at
     length, under a heading this round added.
judge THIS IS NOT PROSE PRECISION AND IT IS NOT 4a. Line 51 is the register
     of what the gate PROVES, in a plan RE-LOCKED at `fb5a5cf` whose commit
     message reads "G2.1 has ONE constant; the retired section says it is
     retired". A reader who opens the plan at section 3 is told G2.1 is an
     eigenvalue ratio; the form it actually asserts is 1600 lines later. The
     plan states BOTH forms in the present tense and nothing says which one
     is the gate.
```

  **Closed when** `:51` states the form `:1664` and `:1787` state, and `:136`,
  `:212` and `:1505` either carry the same or say at their head that they are
  the retired form -- the treatment `:1917` already got.

**R422. (BLOCKS -- the plan says the gap counter is a uniform elastic
foundation. No such injection exists anywhere in the repository, the code
comment that said the same thing was DELETED by this round, and the sentence
opens "Both counters" eight lines above the paragraph headed "ONE COUNTER".)**
`docs/milestones/F2.md:1902-1908`.

```
code :1902 "**Both counters are injected through `assembled`** ... The gap
     :1904  counter is a uniform elastic foundation: it lifts all six rigid
     :1905  modes together, so the residual is what degrades and lambda_7
     :1906  does not come down at all."
code :1910 "**ONE COUNTER, AT `1.0e-13` (CU0).**"   -- eight lines below
cmd  grep -rn "foundation" --include=*.py tests/ floatfea/
out  one hit, in test_closure_evidence_exists.py, about milestone F1
cmd  git show b83d776 -- tests/verification/rung1/test_rigid_body_modes.py
     | grep "^-.*uniform foundation"
out  "- # than by scaling one diagonal entry: a uniform foundation lifts all
      six rigid modes together, which is what degrades the gap without
      moving the count."   -- THE ROUND DELETED THE TWIN OF THIS SENTENCE
      FROM THE CODE AND LEFT IT STANDING IN THE PLAN.
code the shipped injection, `counter_response`, for "bound", "retired_floor"
     and "retired_gap" alike: `_assemble_with_torsional_release` then
     `kr[-1,-1] += size * max|kr|`. And `_nearly_released`: "A UNIFORM
     FOUNDATION WAS THE FIRST ATTEMPT AND IT DOES NOT WORK."
judge THE PLAN DESCRIBES A REJECTED APPROACH AS THE SHIPPED ONE, and BP0 says
     a rule change carries every sentence citing the old rule with it in the
     SAME commit. `fb5a5cf` rewrote the section below this one and walked
     past this paragraph.
```

  **Closed when** `:1902-1908` says what `counter_response` does, or is cut,
  and "Both counters" agrees with "ONE COUNTER" eight lines below it.

**R423. (BLOCKS -- two sentences written to say a number is NOT typed, each
refuted by one grep, and one of them is in the same file as the count it
denies.)** `docs/milestones/F2.md:1914-1915` and
`tests/verification/rung1/test_rigid_body_modes.py:30` against `:545`.

```
code F2.md:1914 "Both numbers are printed by the counter test rather than
     :1915       typed anywhere."                   -- ADDED THIS ROUND
cmd  grep -rn "1\.248\|6\.237" --include=*.py --include=*.md floatfea/ tests/
     docs/milestones/
out  floatfea/tolerances.py:408  `6.237x`
     floatfea/tolerances.py:414  `1.248x`
     floatfea/tolerances.py:446  `1.248x`
     docs/milestones/F2.md:1911  `1.248x`   -- three lines above the sentence
     docs/milestones/F2.md:1913  `6.237x`   -- two lines above the sentence
judge FOUR SITES PLUS THE PARAGRAPH THE SENTENCE IS IN. Both numbers are
     correct -- I measure 1.2479 and 6.2372 -- and the sentence about them
     is false. That is CP2 exactly: the prose written AROUND a repair
     inheriting none of the discipline applied TO it.
code test_rigid_body_modes.py:30 "NO COUNT IS WRITTEN HERE for the loss: its
     :31                          count is not machine-stable, which is why
     :32                          no figure publishes it"   -- ADDED THIS ROUND
code test_rigid_body_modes.py:545 "it breached at seventeen of the reviewer
     :546                          first twenty-eight clean frames against
     :547                          the ratio ten"
judge THE SAME FILE, 515 LINES APART, WRITES THE LOSS COUNT AND SAYS IT IS
     NOT WRITTEN. `seventeen` and `ten` are typed, unreproducible at this
     commit, and measured on a 28-frame corpus that is now 114.
```

  **Closed when** the F2.md sentence says where the two numbers are typed or
  the numbers move to the figure that carries them, and `:545` carries a
  figure, a bracket, or no count -- the treatment `:30` gave the same
  quantity twelve lines from the top of the same file.

**R424. (BLOCKS -- a comment added this round says no shipped row declares
`log=True`; two shipped rows declare it, one of them 409 lines above in the
same file and in the same commit, and a test added in the same commit asserts
that both do.)** `scripts/regen_figures.py:526-529`.

```
code :526 "No shipped row declares it at this commit -- the quantity that
     :527  needed it is a plain ratio under CU0 -- so the guard for it is an
     :528  injected pair in `tests/test_figure_local_check.py` rather than a
     :529  live row, and that is said here rather than left to be discovered."
cmd  grep -n "log=True" scripts/regen_figures.py
out  :118  _floor("rigid_mode_seventh_orders", "above", "RIGID_MODE_GAP", log=True)
     :180  log=True,     (rigid_mode_seventh_orders_smallest_decided)
code :111 of the SAME FILE, added in the SAME commit: "AND THEY ARE WHY
     `log=True` IS NOT A DEAD FLAG (CU1, R418). These are the repository
     log-valued rows"
code tests/test_figure_local_check.py, added in the same commit, asserts
     marked == the set of those two names, and is green
judge THREE STATEMENTS IN ONE COMMIT, TWO CORRECT AND ONE THE OPPOSITE, and
     the false one is the one a reader of the class vocabulary meets first.
     It is load-bearing too: it is the reason given for the guard being an
     injected pair rather than a live row.
```

  **Closed when** `:526-529` says what `grep -n "log=True"` prints.

**R425. (BLOCKS -- a docstring added this round says NOTHING ASSERTS AGAINST
THIS AND NOTHING MAY, and a test 388 lines below it in the same file, added
in the same commit, asserts against it. The report repeats the sentence.)**
`tests/verification/rung1/test_rigid_body_modes.py:273` against `:661`
and `:673`.

```
code :271 def zero_modes_under_the_bound(k) -> int:
     :273 "NOTHING ASSERTS AGAINST THIS AND NOTHING MAY (CU0)."
code :661 dim = zero_modes_under_the_bound(k)
     :673 assert dim == RIGID + 1, ...
code report section 2: "**below_bound stays printed and nothing asserts
     it**, which is what CU0 asked for"
cmd  grep -n zero_modes_under_the_bound tests/verification/rung1/test_rigid_body_modes.py
out  :270 def, :508 comment, :513 print, :659 comment, :661 A CALL FEEDING
     AN ASSERT AT :673
judge AND THE INTERESTING PART IS THAT THE CODE IS RIGHT AND THE SENTENCE IS
     WRONG. R420 needed the second assertion to be an independent
     measurement, and counting the spectrum is the right one -- I confirmed
     it can fail while the first passes, since it also requires lambda_8
     above the bound. CU0 asked that the count never become a second name
     for the gate decision. BOTH ARE SATISFIED, and the distinction between
     them -- not asserted BY THE GATE, asserted BY A CONTROL -- is what
     neither the docstring nor the report records. A later reader who takes
     the docstring at its word deletes `:673`.
```

  **Closed when** `:273` says which assertions may read it and which may not,
  and the report sentence says the same.

**R426. (BLOCKS -- "The binding side is the SIX THEMSELVES" compares two
numbers 1.06x apart, taken on different machines, and the side it dismisses
is the one nothing enforces.)** `floatfea/tolerances.py:363-374`.

```
code :363 "below  A GENUINE SEVENTH ZERO MODE is refused at all 35
     :367  re-expressions ... The binding side is the SIX THEMSELVES"
cell the 35-way cell, reproduced: one torsional release, 7 unit systems from
     1e-6 to 1e6 crossed with 5 spans, nothing else moved
out  35 of 35 refused; the highest lambda_7 any of them reaches is 1.3750
     units of ||K_hat||*eps
cmd  the corpus max of rigid_max, same machine, same commit
out  1.4614 units -- so on THIS machine the six do bind, by 1.0628x
cmd  the published figure, from the canonical runner
out  rigid_mode_largest_rigid_eigenvalue = 1.2727, which is BELOW the 1.3750
     the mechanism reaches here
judge SO THE TWO CANDIDATE LOWER LIMITS SIT INSIDE FIGURE_FLOOR_CLASS_SPREAD
     OF EACH OTHER, and the published pair is measured on two machines with
     the ordering reversed between them. Eight lines below, the same entry
     applies exactly this test to the UPPER side and declares the result a
     limitation. The lower side gets no such test, and it is the side that
     matters more: only the six are enforced, as a floor-class row, while
     the mechanism ceiling is enforced by nothing and is not a figure. The
     bound is 145x above both, so no decision moves -- what is wrong is the
     sentence saying which measurement brackets the constant.
```

  **Closed when** the entry says the two lower limits are within the declared
  spread of each other and reports both, or the mechanism ceiling becomes a
  figure so the comparison is between two numbers from one render.

**R427. (BLOCKS -- `rigid_mode_corpus_refused` is published as an EXACT row,
its own entry says it is not platform-stable, and the mechanism named as the
one that would catch it moving cannot: ten legs of one canonical environment
do not measure a second machine. The generator withholds another count six
lines away for precisely this reason.)** `floatfea/tolerances.py:392-400`
and `scripts/regen_figures.py:203-213`.

```
code tolerances.py:398 "what is not platform-stable is the published count
     :400              of refusals. CI is canonical for that figure (Q8) and
                       the determinism legs are what would catch it moving."
cmd  grep -n "runs-on\|OPENBLAS_CORETYPE\|leg: \[" .github/workflows/ci.yml
out  every leg runs-on ubuntu-latest with OPENBLAS_CORETYPE Haswell; the
     matrix is leg 1..10 -- ten runs of ONE pinned environment
judge THE LEGS MEASURE RUN-TO-RUN DETERMINISM ON THE CANONICAL MACHINE. The
     machine on which this count would move is a NON-canonical one, and
     there the path is compare(), where this row is not floor-class:
code regen_figures.py:664 "Not a floor-class figure: Q8 requires these to
                           agree EXACTLY on every machine, so this is
                           staleness rather than platform."
code regen_figures.py:203-213, SIX LINES ABOVE the row: "THE LOSS COUNT IS
     NOT MACHINE-STABLE AND IS NOT PUBLISHED ... An exact row that disagrees
     between machines is staleness by Q8 rule, and it is not floor-class
     either -- a count is not a measurement against a tolerance. It is left
     out."
judge ONE GENERATOR, TWO POLICIES, SIX LINES APART, AND THE ROUND WROTE THE
     REASON FOR ONE OF THEM DOWN WHILE PUBLISHING THE OTHER.
cell  AND I MADE IT MEASURABLE RATHER THAN ARGUED. Block A puts six frames
     in the window; rb_window_l7_200 renders at 1.9951e+02 against a bound
     of 199.526 -- it becomes rigid_mode_largest_refused and it is 1.00008x
     from flipping, four orders inside the declared 1.5x spread. The
     refusal count is now one round-off away from 32 or 33.
```

  **Closed when** `rigid_mode_corpus_refused` is floor-class or withdrawn the
  way the loss count was, or the entry names a check that would actually see
  the count move. Deleting the corpus entry is not one of the three.

**R428. (BLOCKS -- a figure row is decided against a ceiling this round
retired.)** `scripts/regen_figures.py:117-118`.

```
code _floor("rigid_mode_seventh_orders", "above", "RIGID_MODE_GAP", log=True)
cmd  the class vocabulary at :514 on this kind
out  "above <ceiling>   a counter: it must stay over the ceiling it defends"
code tolerances.py:460 "CLASS: ACCURACY -- and RETIRED at CU0/R415 ... NOT A
     GATE, for the same reason as the floor above"
judge compare() COMPUTES A MARGIN FOR THIS ROW AGAINST A RETIRED CONSTANT
     and fails the build if it falls under FIGURE_FLOOR_CLASS_SPREAD. It
     never will -- the margin is 10**11.08 -- so nothing breaks today. The
     form is what is wrong. R399, which verdict 47 closed, asked for "no
     `_floor(...)` mark against a retired ceiling"; this round retired the
     ceiling and left the mark. The mark was correct when it was written,
     which is the whole of BP0. The row beside it got `derived` for a
     weaker reason.
```

  **Closed when** the row is `derived` like the other retired parametrisation
  beside it, or the ceiling it names is not a retired constant.

---

**Recorded, and lock items for step 4a (BU0). None of these touches the gate
assertion, a tolerance, or the truth of a published figure.**

**R429. The run-id guard CU3 asked for misses the most ordinary way of
writing a run id, and I measured it.** `tests/test_report_carried.py`,
`_RUN_ID`. The right-hand lookahead rejects a trailing DOT as well as a
digit, so a run id at the end of a sentence is never seen. Seven unseen
shapes in `tests/corpus/report_ci_section.txt`, each applied to the newest
revision in a scratch clone at `d8ac843` and run through the shipped tests:
**2 of 7 refused, 5 allowed.** The misses are a trailing full stop, a full
stop in a list item, a 13-digit id, thousands separators, and -- the R412
shape itself -- a paragraph whose only "conclusion" is the word inside
`gh run view <id> --json conclusion status`, which satisfies the conclusion
regex without anyone pasting what the run did.

**R430. The second CU3 guard has no negative control and is vacuous on this
report.** `test_a_GREEN_JOB_TABLE_does_not_stand_under_a_FAILED_run` returns
early when every conclusion in `_ci_section()` is success or skipped, which
is the case at `d8ac843`; the runs that DID conclude failure are in section
0a, which `_ci_section()` does not return. There is no state for it in
`tests/test_report_guard_states.py`. A gate carries its own failure.

**R431. `scripts/suite_count.py` excludes three files and a fourth grows
with the revision.**
`tests/test_plan_figures.py::test_every_figure_reference_anywhere_resolves`
is parametrised over every figure reference ANYWHERE, including the step
report: 105 parameters at `fd56d97`, 110 at `d8ac843`. So the published
"2107 passed ... excluding 309 tests in 3 files parametrised over this
report" does not reconcile with my run -- 2480 collected at `d8ac843`, 368
excluded, 2112 left, five more than 2107, and `d8ac843` touches only two
docs files. I confirmed 2416 / 309 / 2107 at `fd56d97` in a scratch
worktree, so the number is right for what it counts; the sentence about what
it counts is not, and R323 is the reason that line exists at all.

**R432. A local literal duplicates `WIDEN` in the counter test.**
`tests/verification/rung1/test_rigid_body_modes.py:760` reads
`widened = RIGID_MODE_BOUND / 10.0`, three lines under a comment that says
"the meta-test widens the bound by `WIDEN`". `WIDEN = 10.0` lives at
`tests/test_counters_are_injected.py:68`. It feeds a print and not an
assertion, but the print is where `6.237x` and `1.248x` come from, and
`1.248x` is the stated justification for deleting a counter.

**R433. Seven machine-dependent measurements are typed into
`floatfea/tolerances.py` rather than rendered.** `124.45`, `1.603x`,
`6.237x`, `24.90`, `1.248x`, `4.3707e+05` and `199.5625`. I reproduce every
one to four digits -- 124.4494, 1.6033, 6.2372, 24.8989, 1.2479, 4.3716e+05,
199.538 -- so they are right at this commit. They are also eigenvalue-derived,
which is the round own argument for why two figure rows had to become
`derived`, and `rigid_mode_counter_seventh` already publishes the first of
them. BI3 territory; the mechanism is 4a.

## Tolerances touched

**One file, `floatfea/tolerances.py`, `+166 -85`, all in `b83d776` and
`0a9d54d`. One constant created at the product of two retired ones, one
counter created at the size of a retired one, two constants and two counters
retired. NO VALUE MOVED.**

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| `RIGID_MODE_BOUND` | -- | `199.526231496888` | NEW. Dimensionless, in units of `\|\|K_hat\|\| * eps`; the assertion is `lambda_7(K_hat) >= BOUND * \|\|K_hat\|\| * eps`. Exactly `RIGID_MODE_FLOOR * 10**RIGID_MODE_GAP`, so the decision is bit-unchanged | `RIGID_MODE_BOUND_COUNTER_DEFECT` at `1.0e-13`, nearly-released connection injected through `assembled`, pinned by `match="UNDECIDABLE"` | `:329-401`. **R415 closed: one degree of freedom, one constant.** Counter margin `1.6033x` under the bound and `6.2372x` over the widened bound -- I reproduce both, and I SOLVED the edge: the give-back at which the gate stops refusing is `1.6032e-13`, so the counter is `1.6033x` under it in defect size too. Window: R426 on the lower side, R427 on the upper. |
| `RIGID_MODE_BOUND_COUNTER_DEFECT` | -- | `1.0e-13` | NEW, at the size the retired gap counter carried. Relative stiffness given back on the released twist DOF | n/a | `:404-418`. The response is linear in the give-back, `lambda_7 = 1.2445e15 * size`, so this is a detection threshold and not one perturbation. R433 on the typed numbers beside it. |
| `RIGID_MODE_FLOOR` | `10.0` | `10.0` | **RETIRED.** Value unchanged; nothing asserts against it | retired with it | `:420-439`. Entry rewritten to the past tense, window moved to the figure where it decides. **R399 discipline applied here and missed one file over: R428.** |
| `RIGID_MODE_FLOOR_COUNTER_DEFECT` | `2.0e-14` | `2.0e-14` | **RETIRED.** Still computed by `counter_response("retired_floor")` and printed; asserted nowhere | n/a | `:441-458`. **R416 closed** -- the discrimination clause is withdrawn by name with the cross cell recorded. |
| `RIGID_MODE_GAP` | `1.3` | `1.3` | **RETIRED.** Value unchanged; nothing asserts against it | retired with it | `:460-485`. **R418 closed** at the mechanism. R428: `regen_figures` still decides a row against this constant. |
| `RIGID_MODE_GAP_COUNTER_DEFECT` | `1.0e-13` | `1.0e-13` | **RETIRED**, its size carried forward unchanged into the new counter | n/a | `:487-498`. **R417 closed** -- `FIVE TIMES stiffer`, `0.7` of a decade, at both sites. |
| `RIGID_BODY_MODE_RATIO`, `RIGID_BODY_SUBSPACE_LOSS` and their counters | unchanged | unchanged | retired earlier, still nothing asserts | -- | `:500-610`. **R405 closed** at all five sites. |

```
judge NO VALUE WAS WIDENED AND NO VALUE MOVED AT ALL. `RIGID_MODE_BOUND` is
     the arithmetic product of the two constants it replaces, to the last
     digit of a double, and I checked it: 10.0*10**1.3 is exactly
     199.526231496888. The gate decides the same thing on the same frames.
judge THE ONE COVERAGE REDUCTION IS DEFENSIBLE AND I MEASURED IT. Deleting
     the `2.0e-14` counter removes a sample from a LINEAR family whose edge
     is solved; the survivor is harder in both directions (1.6033x under
     the bound against 8.0135x, 6.2372x over the widened bound against
     1.2479x). One counter for one constant is right.
judge NO OTHER NUMBER IN THE EIGHT COMMITS FUNCTIONS AS A TOLERANCE. `RIGID`
     is still a kinematic constant; `EPS` is `np.finfo(float).eps`; the
     `10.0` at test_rigid_body_modes.py:760 is a duplicate of a declared
     not-a-tolerance and feeds a print (R432).
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2480 passed at d8ac843 -- no undeclared literal entered tests/ this
     round and nothing was added to `tolerance_marker_exemptions.txt`.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**The departure from CU0 is CORRECT and it is not a STOP.** I asked for the
transition at `stretch ~ 1.95e6` as the lower side of the window and the
implementer refused it as a tautology. He is right, and it is an identity
rather than an empirical claim: `below_bound == 6` is `w_6 <= bound < w_7`
on a sorted spectrum, which is exactly "lambda_7 above the bound AND the six
under it". I confirmed zero disagreements on all 114 frames and I re-solved
the crossing myself -- `4.3716e+05`, where `lambda_7` is `199.538` units,
the bound restating itself. My `1.95e6` was a real bracket for the retired
floor of 10 and it died with that constant. The departure was declared in the
commit message, in the tolerance entry and in two report sections, which is
what `CLAUDE.md` asks of a reviewer directive that execution shows to be
wrong. **A directive I wrote is not the locked plan and a measured refusal of
one is the process working.**

**What holds is eight items and every one of them is a sentence.** Not one is
an element defect; not one moves a threshold; the gate decides the same thing
on the same frames before and after every repair I am asking for.

1. **R421 -- the plan gate register still defines G2.1 as the retired
   eigenvalue ratio**, at `:51`, with `:136`, `:212` and `:1505` behind it.
   The plan was RE-LOCKED this round on the claim that the retired section
   says it is retired; four sites outside that section do not.
2. **R422 -- the plan says the gap counter is a uniform elastic foundation.**
   No such injection exists; the same commit deleted the twin of that sentence
   from the code; and it opens "Both counters" eight lines above "ONE
   COUNTER".
3. **R423 -- two sentences saying a number is not typed**, both refuted by
   one grep, one of them two lines below the number it denies.
4. **R424 -- "No shipped row declares `log=True` at this commit"**, with two
   shipped rows declaring it, one 409 lines above in the same file and in the
   same commit, and a test asserting exactly that set.
5. **R425 -- "NOTHING ASSERTS AGAINST THIS AND NOTHING MAY"**, with an assert
   on it 388 lines below in the same file and in the same commit. The code is
   right; the sentence and the report sentence are not.
6. **R426 -- "The binding side is the SIX THEMSELVES"**, a comparison of
   `1.2727` from the canonical runner with `1.3750` from the laptop, 1.06x
   apart, and the side it dismisses is the one nothing enforces.
7. **R427 -- the published refusal count is an exact row that the entry says
   is not platform-stable**, with the determinism legs named as the check
   that would catch it and ten legs of one pinned environment unable to. The
   same generator withholds the loss count six lines away for that reason.
8. **R428 -- a figure row still decided against `RIGID_MODE_GAP`**, retired
   this round.

**One observation about the shape of these eight, because it is the finding
behind the findings.** Five were written in the round that fixed the same
species elsewhere. `b83d776` deleted the uniform-foundation sentence from the
code and left it in the plan; wrote a correct comment about `log=True` at
line 111 and its negation at line 526; wrote a docstring saying nothing may
assert a quantity and an assert on it in the same file; and `fb5a5cf`
rewrote the retired section while walking past the paragraph eight lines
above it. CP2 already names this -- the prose written AROUND a repair
inheriting none of the discipline applied TO it -- and the mechanical guard
`tests/test_report_numbers_are_sourced.py` reaches the report and stops at the
source tree. **Every one of these eight is refuted by a grep over files the
commit itself touched.** That is worth a directive rather than eight repairs.

**Adversarial corpus (BE3): 19 new entries across two files, all unseen by the
implementer, committed separately at `a89f149`.**

**`tests/corpus/g21_rigid_body_frames.txt`, 114 to 126. Twelve frames, and
the shipped gate reddens at NONE.** Nine decided, three refused, residual
holds at all twelve with a new corpus worst of `1.3502e-16` against `1e-15`,
and `below_bound` is six at every decided one. Block A occupies the window
the entry describes as a limitation -- six stretches solved so `lambda_7`
lands at 215, 205, 200, 195, 188 and 180 units either side of `199.53` -- and
`rb_window_l7_200` becomes `rigid_mode_largest_refused` at `1.9951e+02`,
`1.00008x` from the bound. That is R427 turned from an argument into a
number. Block B aims at the only side of the window anything enforces and
does not move it: the highest `rigid_max` the six reach is `1.3295` against
the file existing `1.4614`, which is the result rather than a reason to leave
them out. **And I applied BP0 to my own file**: my block header from the
forty-seventh verdict said the margin reaches zero at `stretch ~1.95e6`, true
against the retired floor and not against the bound, and the new header says
so.

**`tests/corpus/report_ci_section.txt`, 4 to 11. Seven CI-section shapes, and
the implementer check caught 2.** That is the coverage measurement for the
CU3 guard, and it is not the planted-shape count: **2 of 7 refused, 5
allowed**, with the misses listed at R429. The one that matters is the fifth:
a paragraph naming a run and showing `gh run view <id> --json conclusion
status` without pasting the result satisfies the guard, and that is R412
itself.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
       tests/test_plan_figures.py -q        (at a89f149)
out  1 failed, 292 passed
     tests/test_plan_figures.py::test_the_generated_figures_are_not_stale
```

* **The one red at my commit is the figures guard and it is correct.**
  `rigid_mode_corpus_frames` `114` to `126`, `rigid_mode_corpus_refused`
  `29 of 114` to `33 of 126`, `retired_ratio_over_ceiling_on_corpus`
  `80 of 114` to `91 of 126`, `rigid_mode_residual_worst_over_corpus`
  `1.1410e-16` to `1.3502e-16`, `rigid_mode_largest_refused` `1.8800e+02`
  to `1.9951e+02`. **The next report regenerates them and names them.**

**Not gates on step 5, into the next report Carried section:** R429, R430,
R431, R432, R433, R419, R410, R411, R413, R414, R400, R401, R402, R390,
R391, R392, R393, R383, R370, R371, R372, R373, R374, R362, R363, R364,
R354, R355, R356, R357, R347, R348, R349, R350 second half, R330, R331,
R332, the section 9 status-versus-subject disagreement, R321, R322, R300,
R291, R292, R281, R231, R244, R245, R275, R230, R261, the underlying gap in
R276, R277, R262, R264, R266, the two R248 residues, R249-R252, R225-R228,
R232, R233, and everything already at 4a. **R415, R416, R417, R418, R405,
R406, R409 and R420 are closed.** R411 advanced to off-by-one and stays
open. R412 is answered as a rule and reopens as R429 and R430.

**Forty-eight rounds have found no element defect and this round found none
either.** Every one of the 126 frames is the same defect-free element; the
residual half holds at all of them; 1980 further configurations produced no
vacuous pass; 35 re-expressions of a real mechanism were all refused. It
still means "not yet contradicted": ladder 5 has printed
`OK -- 0 directories ran` every time it has run, and V5.1 against CalculiX is
the witness that has not spoken.
