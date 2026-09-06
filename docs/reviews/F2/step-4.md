# Review — F2 step 4
Reviewed commit: 931d71da6dc94cceafc90db0760d26f0254d26e6
Verdict: STOP
Tests: 594 passed, 2 failed, 0 skipped   (my run at `36a3702`, `python -m pytest -q`, 3.51s.
With my eleventh-round corpus applied at `931d71d`: **3 failed, 607 passed**.)

**Reviewed code commit: `36a3702`.** The header stamp is `931d71d`, my own corpus
commit, made immediately before this verdict and touching no code.

Eleventh pass. Range `51fc886..36a3702`, two commits: one code commit `1f32c7f`
and the report `36a3702`. `git diff 51fc886..36a3702 -- .claude docs/SUPERVISOR.md`
is **empty** -- my own instructions were not touched, and I diffed them rather
than inferring it from a green suite that does not read them.

**Three of the four blocking items are genuinely answered and one of them is the
best-executed fix of this milestone.** R91's parser is right: I tried fourteen
`extra=` shapes against the new disambiguation rule and could not make one
resolve silently wrong; the per-entry assertion now reddens on a `hold` line the
module cannot build; `roll_and_aniso_together` moved from *unparseable* to
measured (`0.035x` ceiling, `1.1467e-11` detection). R93's four blocks reproduce
on my own harness -- blocks (i), (ii) and (iv) **to the digit**. Nothing was
widened; the `Final[` lines of `git diff -U0 -- floatfea/tolerances.py` are empty
in both directions. No test is skipped or `xfail`ed.

**And the verdict is STOP, on two independent grounds that the report itself
states.** A rung-1 verification test is red at HEAD, and the locked plan is wrong
in text that is load-bearing. `CLAUDE.md` sec. Step gating defines exactly this:
"`STOP` means the plan is wrong or a low rung is red: implementation halts and
the plan reopens." The report's own framing -- "R94 is a plan item awaiting
Xabier" -- is the definition of a STOP written in other words, and my instructions
forbid softening one into a HOLD. **This is not a criticism of `1f32c7f`, which
is good work; it is the routing the situation requires.** The work goes into a
`plan:` commit on `docs/milestones/F2.md`, not into step 5 and not into another
step commit.

**Was leaving the suite red the right call? Yes, unambiguously.** Every
alternative available inside the step was forbidden: deleting my entries (the
corpus is not the implementer's to edit), lowering `PATCH_TEST_EXACTNESS_COUNTER`
(weakens the control -- my own closing condition warned against it), `xfail`,
`skip`. `CLAUDE.md`: "Never widen a tolerance, skip a test, or mark a test
`xfail` to get a green build. Report the failure instead." That is what happened.
**Is "R94 is a plan item" a real distinction? Half of one.** It is right about
*where* the fix goes. It is not a category that lets a step close with a rung-1
red, and it is not the whole reason the item is open -- see R99.

**The finding of this round.** Revision 11 proposes bounding the model at member
`lambda <= 300` (F6 applying `200` in compression) so that the counter clears
everywhere admitted. **I measured that proposal and it does not hold.** The
runner's `member_lambda(entry)` rebuilds the section from `section=` and discards
`extra=I_y_over_I_z=`, so the `lambda` it prints is the *strong* axis, while the
`1/lambda^2` response follows the *governing* one:

```
  entry                            printed lam   min-I lam   x counter
  aniso_weak_lam154_undetectable       153.9        1539.0      0.214x   RED
  aniso_weak_lam154_pin                153.9         688.2      1.068x
  aniso_weak_lam102_detects            102.4         458.1      2.400x
  aniso_reversed_I_y_over_I_z          153.9         153.9     16.301x
```

An entry at printed `lambda 153.9` -- **half the proposed compression limit** --
holds at `0.044x` of the ceiling and responds to the 1e-6 defect at `0.214x` of
the counter. The gate holds there and cannot fail there. Two entries with the
**same printed lambda** sit `5x` apart in detection, and the fourth line is the
sign control: anisotropy the other way (`I_y/I_z = 100`) leaves the governing axis
at `153.9` and detection at `16.3x`, so this tracks the weak axis and not
`|I_y/I_z - 1|`. This is the ninth verdict's STOP species exactly -- a domain claim
sampled on one coordinate of the space it is asserted over -- and it arrives
*before* the bound is written, which is the cheapest moment for it to arrive.

## Carried

Every item from the tenth verdict (`HOLD @ 47d117e`, committed `51fc886`), traced
through `51fc886..36a3702` and re-measured. The four gated items first.

- **1. R91 (blocking) -- ANSWERED, and it is the best fix in this round.** Both
  halves. `_error_row` reads the reviewer's `expect` off the raw line with
  `_field` and no longer writes `"raise"` over it; a `hold` line the module
  cannot build now reddens with "the disagreement is the finding". I did not take
  the new test's word for it -- I drove `_error_row` and the per-entry assertion
  directly on five probe lines: `expect=hold` **RED**, `expect=breach` **RED**, no
  `expect` at all gives `"unrecorded"` **RED**, `expect=raise` green. And the
  capability: `extra=` now takes a sequence, and I attacked the disambiguation
  rule with fourteen shapes -- `roll` then `onode`, `onode` then `roll`, a
  two-component vector followed by a key, a key name used as a vector component,
  an empty value, empty components, leading and trailing commas, an inner `=`, an
  uppercase key, `none` followed by a key, `inf`, `1e400`. **Every ambiguous shape
  raises; not one resolves silently wrong.** My two adversarial refusal entries
  (`extra_key_repeated_with_onode`, `extra_onode_truncated`) are both refused by
  the shipped parser. `roll_and_aniso_together` is measured. Closing condition
  taken in full. One residual, small: **R104**.
- **2. R92 (blocking) -- ANSWERED at the site the condition named, and one more
  taken voluntarily.** The `L/D` sweep is out of `tolerances.py`; the entry keeps
  `1.14e-09` / `11371x` and points at revision 10 sec. 4, and I confirmed that
  section carries the sweep. The second removal (`RESULTANT_EXACTNESS_COUNTER`)
  was found without being asked for and is credited. But the exhaustiveness is
  not established -- **R100** -- and the second entry's pointer resolves to the
  withdrawn claim -- **R101**.
- **3. R93 (blocking) -- ANSWERED, and I re-derived all four blocks rather than
  reading them.** Blocks (i), (ii) and (iv) reproduce **to the digit** on my own
  harness:

  ```
  (i)  axial via field 1.0136e-13  via resultants 1.4498e-09   14302.8x
       twist          2.8348e-10                1.4498e-09        5.1x
  (ii) axial oob 2.8565e-02 ... twist 7.1889e-04 ... shear_xz 1.2401e-02
  (iv) S=1e-3 worst 1.4761e-16 (0.665 eps); S=1 and S=1e3 8.7042e-17 (0.392 eps)
       36 cells span 0.000132 .. 0.6648 eps; per-scale worst ratio 1.696
  ```

  Block (iii) reproduces in its ratio column and not quite in its percentages --
  **R102**. The blanket sentence is replaced by a per-block one, which is what the
  condition asked for.

  **On the withdrawal of "~150x weaker": it is honest, and the replacement is a
  better argument.** I bisected both shipped predicates myself, six states, and
  got `5.1x` to `14303x`. A single number cannot describe a three-order spread,
  and the entry now says why the spread is the reason to keep both channels
  rather than a reason to drop one: the field channel is `14000x` the sharper in
  axial and `5.1x` in twist, so they are not two measurements of one thing. That
  is a genuine improvement on the number it replaces, and it was reached by
  deleting a claim rather than by defending it.
- **4. R94 (blocking) -- NOT ANSWERED, correctly declared, and it is the STOP.**
  See R94 below. Two of the three closing conditions I offered needed nothing from
  Xabier and neither was taken (**R99**).
- **5. R95 (recordable) -- carried, open, and NOT in the report's `Carried`
  section.** The report records the `_direction` overflow in prose without its
  number and calls it "one new item"; it is R95, from the tenth verdict. Recording
  it rather than fixing it is the right call under the scope the directive set.
  The finding is broader than the report states -- **R95** below.
- **6. R96 (recordable) -- carried, OPEN, unmentioned, and it is load-bearing for
  R94.** `grep -n "second_moment" tests/` is still empty; `member_lambda(entry)`
  still reads `_section(entry["section"])`. That is not a cosmetic gap any more:
  it is the reason the proposed `lambda <= 300` bound does not bound the counter.
- **7. R97 (recordable) -- carried, OPEN, unmentioned.** `grep -rn "never
  asserted at a constant"` still returns `F2.md:506` and `F2.md:1208`, and
  `test_the_six_constant_strain_states_are_EXACT` still asserts `res_err <=
  RESULTANT_EXACTNESS` on the solved field at all 36 cells.
- **8. R98 (recordable) -- carried, OPEN, unmentioned.** `INADMISSIBLE` is still
  assigned at line 611 and read nowhere; `grep -rn "INADMISSIBLE" tests/ floatfea/`
  gives one assignment and three comments.
- **9. R65 -- WITHDRAWN by me at the tenth verdict.** Correctly recorded as
  withdrawn.
- **10. R63 -- carried, unanswered, correctly declared open.** `MATRIX_SYMMETRY`
  and `ROUNDOFF_IDENTITY` remain widenable in silence.
- **11. R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **12. R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 --
  still open**, correctly declared, routed to step 4a or later.
- **13. R77, R78, R81-R90 -- closed at the tenth verdict**, correctly recorded.
- **14. R68's standard -- BROKEN, fifth round.** Four rounds running, the report
  listed every open item by number. This one lists thirteen and omits four
  (**R99**), and one of the four turns out to decide the item the round is about.

## Findings

**R94. (STOP) The locked plan asserts a domain claim that is false at this
commit, a rung-1 test is red on it, and the answer proposed in revision 11 is
refuted by measurement before it is written.**
`docs/milestones/F2.md` sec. 5b Q6 (`:415`, `:457`) and sec. D7 item 7 (`:1189`,
`:1202`); `tests/verification/rung1/test_corpus_configurations.py:705`.

*The plan text, three claims, each checked:*

```
claim   "This dissolves the domain question rather than answering it. No
         boundary ... every corpus entry under one claim."   F2.md:457, :1202
command python -m pytest -q
output  2 failed, 594 passed -- lam900_skew_undetectable, lam900_axis_undetectable

claim   "it measures 0.13-0.49 eps across every configuration"   F2.md:1194
command the 36 shipped gate cells, and the corpus reporting test
output  gate cells 0.000132 .. 0.6648 eps; corpus floor 0.84 eps
        (nearly_solid_D_t_2p1); 1.018 eps at my new all_three_extras_free_dir
```

The second is the same withdrawn `0.13-0.49 eps` figure that R93(iv) found stale
in `test_patch_test.py`. The copy in the test file was regenerated this round.
**The identical figure in the locked plan was not, and in the plan it is the
support for "dissolved".** A number can be fixed in one file and left standing in
the file that decides.

*The proposed answer, measured.* Revision 11 sec. 3 proposes "model admission
limit member `lambda <= 300`, with F6 applying `200` to compression members". On
the `lambda` this repository computes, that admits a configuration the gate
cannot fail on:

```
  entry                            printed lam   min-I lam   x counter   x ceiling
  aniso_weak_lam154_undetectable       153.9        1539.0      0.214x     0.044x
  aniso_weak_lam154_pin                153.9         688.2      1.068x     0.019x
  aniso_weak_lam102_detects            102.4         458.1      2.400x     0.030x
  aniso_reversed_I_y_over_I_z          153.9         153.9     16.301x     0.014x
```

All four are `L/D` 35-53, ordinary members, not the `L/D 215-312` filaments the
tenth verdict's `lam900` entries were. `I_y/I_z = 0.01` is a plate-like member and
`0.05` is roughly a 4.5:1 rectangle -- both are shapes a platform carries.

*The engineering details the report flags, judged.* Both are real and there is a
third that decides.

* **Is the compression figure a User Note or a requirement?** In ANSI/AISC 360-16
  it is a **User Note** -- as is the tension `300` in sec. D1, which the report
  reads as the firmer of the two. Neither is a Specification requirement; sec. D1's
  own sentence is "There is no maximum slenderness limit for members in tension."
  **I record this as knowledge, not as verification.** I have no network in this
  environment, so I could not open sec. D1, Chapter E or API RP 2A-WSD sec. 3.2
  either. **The citation is not obtained and the block stands.** Refusing to write
  an unverified clause into a locked plan is the correct call and I endorse it
  without reservation -- it is "verify the reference" applied to a standard.
* **`KL/r` versus `L/r`.** Correct and material: the AISC `300` is on `L/r`
  (actual length) and the `200` is on `Lc/r` (effective). The corpus `lambda` is
  neither -- it is `L/r` on a single member with no `K`.
* **The third, which neither detail covers: `r` is `sqrt(I_min/A)`, and this
  repository's corpus computes it on the strong axis.**
  `floatfea/model/admissibility.py:135` already defaults to `min(I_y, I_z)`; the
  corpus `member_lambda` never passes it (**R96**). A limit written on the printed
  `lambda` admits `aniso_weak_lam154_undetectable`; the same limit written on
  `min(I_y, I_z)` refuses it at `1539`. **R96 is not a loose end -- it is the
  difference between a bound that works and one that does not.**

*And a causal claim with no cell (BG0).* "A member at `lambda = 900` is not a
structural member under the standard this project locked ... **so** the tool is
bounded at both ends by modelling and by code." A code serviceability
recommendation and a `1/lambda^2` detection floor are unrelated quantities; that
they might land near each other is a coincidence, not a derivation. The bound
that is *measured* is where the counter stops clearing on the governing axis. If
a code slenderness limit happens to sit inside it, that is a convenience worth
recording -- not the reason.

**Closed when** the plan reopens and sec. 5b Q6 / D7 item 7 say what was
measured: the *ceiling's* domain is dissolved (which I verified hard at the tenth
verdict and again here -- nothing I ran moved it above `0.05x`), the *counter's*
falls as `1/lambda^2` on `min(I_y, I_z)`, and the edge is at governing
`lambda ~ 630` with the corpus's own numbers beside it. Whether a code
slenderness limit is also adopted is a separate decision and needs Xabier;
**narrowing the plan's word from "dissolved" needs nobody**, and until it is
narrowed the plan states something the suite refutes at its own commit.
`0.13-0.49 eps` goes with it.

**R99. (blocking) The report's `Carried` section omits R95, R96, R97 and R98,
against an explicit condition of the tenth verdict -- and one of the four decides
R94.** `docs/reports/F2/step-4.md` sec. 4.

The tenth verdict's closing text: "R95 through R98, together with R63, R76, R79,
R80, ... may be answered in the next report `Carried` section, **and that section
must list every one of them, open or answered.**" Section 4 lists R94, R63, R76,
R79, R80, R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62, R65, and "R77,
R78, R81-R93 closed or dissolved". The range stops at 93. R95 appears as prose
under "one new item" without its number; R96, R97 and R98 do not appear at all.

This is the guard the whole arrangement exists for, and it failed on the one
species it was written against: **the omitted item is the one the round needed.**
R96 says `member_lambda` reads the strong axis and that no test exercises the
weak-axis argument; R94's proposed fix is a limit on `lambda`; the two were never
put side by side because one of them was not on the list. The tenth verdict's own
header warned that a step had once been "executed cleanly on top of three
unanswered items" -- this is that shape again, with the dependency present in the
repository and absent from the list.

**Closed when** the next report's `Carried` section lists R94, R95, R96, R97,
R98, R99, R100, R101, R102, R103, R104, R63, R76, R79, R80, R6, R16, R25, R30,
R31, R32, R33, R36, R50, R52 and R62 -- each by number, each with a status.

**R95. (recordable, carried and now broader) `expect=raise` certifies that
*something* raised, not that the named thing was refused.**
`tests/verification/rung1/test_corpus_configurations.py:206-211` and `:672-675`.

The tenth verdict's instance stands unchanged: `_direction` tests the norm of the
input, so `1e308,1e308,0` overflows to `inf`, `v / inf` is the zero vector, and
the function returns what its docstring says it refuses; the RuntimeWarning is in
my suite output at this commit. The report records it accurately and declines to
fix it, which is correct under the scope the directive set.

**What the report does not record is that the mechanism is general.** The
parseable-refusal branch is

```python
if expect == "raise":
    with pytest.raises(ValueError):
        _build(entry)
    return
```

-- no `match`, where the inadmissible branch twenty lines above uses
`match="admission limit"`. So every `expect=raise` entry in the corpus passes on
any `ValueError` raised anywhere in `_build`, including the wrong one. That is
why `orient_norm_overflow` reads green: it is caught by the `Node` constructor's
"node_a and node_b must be distinct", a refusal about a different thing.

**Closed when** `_direction` refuses a non-finite norm and a zero result, the
normalisation test's parametrisation contains an overflowing input, and the
`expect=raise` branch asserts *which* refusal fired -- a `match`, or a per-entry
`refuses=` field the reviewer writes.

**R100. (recordable) `tolerances.py` still carries at least three tables with no
generator, and the command offered as evidence does not establish otherwise.**
`floatfea/tolerances.py:469-475`, `:531-533`, `:641-644`;
`docs/reports/F2/step-4.md` sec. 2.

The report's evidence for the sweep is
`git grep -n "157.9x\|9.1808e-12\|150x WEAKER" -- floatfea tests` returning
nothing. That command proves the two *named* tables are gone. It cannot say a
third does not exist, and three do:

```
:469-475  SOLVE_BACKWARD_ERROR_FACTOR    6 rows x 5 columns
:531-533  RESULTANT_EXACTNESS            3 rows x 3 columns
:641-644  rotation deviation vs angle    4 rows x 3 columns
```

`ls scripts/` is still `write_verdict.py` alone. **I regenerated two of the three
and both reproduce exactly** -- `S=1e-3 axial r/f 3.5385e-16 bwd 6.1713e-17` and
the rest of that block, and `RESULTANT_EXACTNESS` worst `4.5578e-11` at `S=1e-3`
skew, `21.9x` -- so nothing here is stale today, and this is a recordable rather
than a blocker. BI3's point is the mechanism, not the current values: "a comment
that carries measurements is a report that never gets regenerated unless
something regenerates it."

**Closed when** the report's claim is stated as what its command shows (the two
named tables are gone), and the three remaining are either listed as a known
carry-over with a route, or moved, or `scripts/` gains the generator. A grep that
finds tables by *shape* rather than by content is the honest command:
`grep -nE "^#   [A-Za-z_].*[0-9][.][0-9]+e[-+][0-9]" floatfea/tolerances.py`.

**R101. (recordable) `RESULTANT_EXACTNESS_COUNTER`'s pointer resolves to the
claim the entry has just withdrawn.** `floatfea/tolerances.py:566-568`.

The entry says the regenerated table is "in `tests/verification/rung1/
test_patch_test.py` beside `RESULTANT_DETECTION_THRESHOLD` ... and in
`docs/reports/F2/step-4.md` revision 10." The first resolves. The second does not:

```
command grep -n "157.9\|150x weaker\|14302\|14303" docs/reports/F2/step-4.md
output  1005: **~150x weaker as a gate**, reproducing the verdict's table to
        1753: the predicates that ship the ratio spans 5.1x ... 14303x
        1757:   axial           1.0136e-13      1.4498e-09   14302.8x
```

Line 1005 is revision 10; lines 1753-1757 are revision **11**. A reader following
the entry's own pointer lands on "~150x weaker as a gate", which is the sentence
the entry three lines earlier declares withdrawn. Every citation resolves -- this
one resolves to the wrong side of a withdrawal.

Second, smaller: BI3's two routes are "a committed script produces the table" or
"the table belongs in the step report". Moving a table from `tolerances.py` into
`test_patch_test.py` is neither. It is defensible -- the table now sits beside the
dict it describes, which is better placement -- but it puts the table back in the
file where R93 found four stale blocks, with no generator, so the mechanism BI3
names is unchanged for it.

**Closed when** the pointer names revision 11, and the entry says which of BI3's
routes the test-file placement claims, or that it claims neither.

**R102. (recordable) `WHAT THE BAND BUYS` reproduces in its ratio column and not
in its percentages, and the summary sentence is 0.06 pp optimistic.**
`tests/verification/rung1/test_patch_test.py:674-680`.

Bisecting the shipped predicate myself -- `_run(state, SKEW, 1 + f*eps)`, ratio
against `PATCH_TEST_EXACTNESS`, `assert_close(ratio, 1.0, 0.05, floor=eps)` --
the `ratio at f=1` column reproduces exactly, all six. The other two do not:

```
  state          ratio at f=1     shipped          mine
  axial              0.996385   +5.44 / -4.92   +5.42 / -4.92
  curvature          0.999760   +5.34 / -5.02   +5.29 / -4.98
  twist              0.998301   +5.49 / -4.88   +5.44 / -4.84
  shear              0.999578   +5.28 / -4.97   +5.28 / -4.95
  curvature_xz       0.999695   +5.34 / -5.02   +5.29 / -4.97
  shear_xz           0.999133   +5.39 / -4.92   +5.35 / -4.93
```

Eight of the twelve cells differ by 0.03-0.05 pp, consistently in one direction,
so the generator differs from the shipped predicate in some small way rather than
drifting. The conclusion survives -- "+5.5% or -5.0% caught in every state" is
true on my numbers too (worst `+5.44`, `-4.98`) -- but the tightest is quoted as
`+5.3% / -4.9%` where I measure `+5.28% / -4.84%`, and `-4.84` is not `-4.9`.
The closed form for the band, `f_above = 1/(0.95 r0)`, matches my bisection in
four states and not in axial, which is the state where the response is least
linear.

**Closed when** the block states the perturbation the percentages were bisected
on (the multiplier applied to `DETECTION_THRESHOLD[state]`, or something else),
so the table is reproducible from its own description, and the tightest figure is
the measured `-4.84%`.

**R103. (recordable) The BM0 headroom table's second row is labelled as a
different quantity from the one it reports, and its `lambda <= 300` rows are
statements about 57 corpus entries presented as properties of a limit.**
`docs/reports/F2/step-4.md` sec. 1.

The numbers themselves all reproduce, and I checked every one against the shipped
reporting test at this commit:

```
  worst residual, whole corpus       1.8641e-16 = 0.0373x ceiling            OK
                                     nearly_solid_D_t_2p1, lam 64.4, 0.84 eps
  most slender with lam <= 300       slender_L_r_99, lam 293.7, 4.53x        OK
  weakest detection, lam <= 300      slender_in_plane_y_L_r_94, 4.30x        OK
  the same at lam <= 200             slender_L_r_63 11.25x; aniso_free_dir_weak 6.68x OK
  the same at lam <= 630             lam620_counter_pin 1.0187e-13 = 1.02x   OK
```

Two things about them:

* Row 2 is labelled "counter / ceiling at the most slender entry". `4.53x` is
  *response / counter*. Counter over ceiling is `20x` for every row and does not
  vary. Row 2 reports the same quantity as row 3, at a different entry.
* The weakest `lambda <= 200` entry is `aniso_free_dir_weak` at
  **`lambda = 46.5`**, `6.68x`. The report prints that number without remarking
  that the binding entry under a slenderness cap is the *least slender* one in the
  group. That is the whole of R94 visible in the report's own table, one column
  from being read: detection is not monotone in the printed `lambda`, so bounding
  the printed `lambda` does not bound detection. The sentence "the proposed
  admission limit is not a restatement of the detection edge, it is comfortably
  inside it" is true of these 57 entries and false of the domain `lambda <= 300`.

**Closed when** row 2 is labelled with the quantity it reports, and the
`lambda <= 300` claim is stated over the corpus it was measured on rather than
over the limit -- or re-measured on `min(I_y, I_z)`, where it becomes a claim
about a domain.

**R104. (recordable) `_field` takes the first matching token where `_parse_line`
treats a duplicate as fatal, so one shape of unexecutable line is still green.**
`tests/verification/rung1/test_corpus_configurations.py:250-257`.

Driven directly:

```
  ... extra=bogus=1 expect=raise expect=hold   ->  row expect='raise'  per-entry GREEN
  ... extra=bogus=1 expect=hold expect=raise   ->  row expect='hold'   per-entry RED
```

`_parse_line` refuses a duplicated field precisely because "taking the last
silently runs a configuration nobody wrote"; `_field` then takes the first and the
per-entry test agrees with it. The reviewer wrote a contradiction, so no
expectation is being overwritten -- this is much smaller than R91 -- but it is the
one line I could build that is unexecutable and reads green, and the fix is the
rule `_parse_line` already applies one function away.

**Closed when** `_field` refuses a key that appears more than once, so a
duplicated `expect` reaches the per-entry assertion as a disagreement.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| -- | -- | -- | -- | -- | **None.** The `Final[` lines of `git diff 51fc886..36a3702 -U0 -- floatfea/tolerances.py` are **empty in both directions**. Every change to that file this round is comment text: two tables removed under R92, and prose. No value moved, none was widened, none was tightened, and nothing was moved to rescue a red -- the red is still red. |

`BEAM_ADMISSION_L_OVER_D` (`2.0`) and `PATCH_TEST_EXACTNESS_COUNTER` (`1.0e-13`)
are the two entries whose *comments* changed. I re-read both against the
measurements: `1.14e-09` at the limit and `11371x` the counter reproduce (I
measured all six columns of the withdrawn sweep at the tenth verdict), and the
`1/lambda^2` statement in the counter's entry is the one thing in this repository
that predicts my `aniso_weak_lam154_undetectable` correctly. **The entry is right
and the plan is wrong**, which is an unusual and welcome direction for that
disagreement to run.

No golden file moved -- `git diff --stat 51fc886..36a3702 -- tests/regression` is
empty. `grep -rn "xfail\|pytest.skip" tests/` returns nothing. The two red tests
are red, named in the report, and not accommodated anywhere -- which is the
correct handling of a failure and is why this STOP is about the plan and not
about the commit.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin, and **neither does another step
commit**. This is a STOP: `docs/milestones/F2.md` reopens.

1. **R94 -- the plan.** Sec. 5b Q6 and sec. D7 item 7 say what was measured. The
   *ceiling's* domain is dissolved, and I could not break it in two consecutive
   rounds on five axes; the *counter's* is not, it falls as `1/lambda^2`, and the
   axis it falls along is `min(I_y, I_z)` and not the `lambda` the runner prints.
   `0.13-0.49 eps` goes with the sentence it supports. **This part needs nobody
   and blocks on nothing.** Whether a code slenderness limit is *also* adopted is
   a separate decision, still blocked on the clause, and correctly so.
2. **R99 -- the list.** The next report's `Carried` section carries R94 through
   R104 and the older items, by number, each with a status. R96 in particular is
   answered *before* any bound is written on `lambda`, because it decides whether
   the bound bounds anything.
3. **R100, R101 -- the two loose ends of R92**, both one-line.
4. **R102, R103, R104, R95 -- recordable**, answerable in the next report's
   `Carried` section.

I want to be exact about what I am not saying. **`1f32c7f` is the cleanest step
commit of this milestone.** Three blocking items answered, two of them at the
level the condition asked for rather than at the level that would have closed it;
a capability added because the reviewer could not express a case; a second stale
table found without being asked; a claim withdrawn rather than defended; a red
left red and named. Every figure I checked in it reproduced, most to the digit.
The STOP is because the *plan* now contradicts the suite at its own commit, and
because a plan is the one artifact a step commit may not fix.

**Adversarial corpus (BE3): 8 new entries committed, all unseen by the
implementer; 7 scored exactly as recorded, 1 red.**
`tests/corpus/g22_model_configurations.txt`, now **82**, committed separately at
`931d71d` immediately before this verdict and touching no code. Full suite with
the corpus applied: **3 failed, 607 passed**.

Four measure the `lambda` proposal on the coordinate it does not sample, and one
of them is the finding of this round. Four attack the new sequence parser in
shapes the implementer's twelve tests omit: `onode + aniso` (the five accepted
shapes cover `roll`, `roll + aniso`, `onode`, `onode + roll`, `none`), all three
keys on a free direction, a key repeated *across* a vector value, and a vector
truncated so the following key is swallowed as its third component. **Both
refusal shapes are refused by the shipped parser** -- that is the coverage
measurement for R91, and it is a pass: the seven planted refusals generalise to
two the author did not plant. `all_three_extras_free_dir` is now the corpus's
worst clean value at `2.2595e-16` = **1.018 eps**, the first entry above one eps
and `7.8x` the plan's quoted range, at `0.045x` of the ceiling.

**Twelve consecutive rounds have found no element defect.** Per the guard, that
still means "not yet contradicted", and it stays that way until V5.1 puts
CalculiX on the other side. What twelve rounds *have* found is a consistent
pattern, and this round names it precisely: **the element has been right every
time and the sentences around it have not.** Eleven of the last fifteen findings
were a figure, a docstring, a pointer or a plan word describing the repository as
it was one commit ago.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Eleven consecutive reviews by one reader, and the standing consequence is
unchanged: nothing here has been read by anyone who does not share this
repository's assumptions.

**The standing question for the next round**, narrower than the tenth's: **for
every claim in this diff that is a statement about a *space* rather than about a
*list*, which coordinate of that space was varied?** `lambda <= 300` was measured
over 57 entries and asserted over a domain, and the coordinate that broke it --
section anisotropy -- was already in the corpus, already in the signature of
`admissibility.member_lambda`, and already an open finding.
