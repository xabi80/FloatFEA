# Review — F2 step 4
Reviewed commit: dac209ea7e60a11456d17a982db7b5b6780fa353
Verdict: HOLD
Tests: 860 passed, 0 failed, 0 skipped   (my run at `f8df590`, `python -m pytest -q`, 10.51s.
With my fourteenth-round corpus applied at `dac209e`: **2 failed, 895 passed**.)

**Reviewed code commit: `b42d834`; report `f8df590`.** The header stamp is
`dac209e`, my own corpus commit, made immediately before this verdict and
touching no code.

Fourteenth pass. Range `a8f36e5..f8df590`, four commits: `36ded5b` (`process:`,
`CLAUDE.md` only), `b690472` (plan, re-lock), `b42d834` (step) and `f8df590`
(report). `git diff a8f36e5..f8df590 -- .claude docs/SUPERVISOR.md` is **empty**;
`git log --oneline a8f36e5..f8df590 -- CLAUDE.md` returns `36ded5b` alone, whose
`--stat` is `CLAUDE.md | 25 +` and whose message opens `Directive: BP0.
Standalone process commit, touching no code and no test.` The guard change is in
the shape the guard requires, and it deletes nothing: 25 lines, all insertions. I
diffed my own instructions rather than inferring them from a green suite that
does not read them. No commit touches both `floatfea/` and `docs/reviews/`.

**And this is not a STOP, for the first time in three rounds. That is the
headline and I will not blur it.** The locked plan is right this round. BP0 is
the correct diagnosis of R117/R118/R120 and the correct level to fix them at.
BP1 is a real guard: I moved both constants and something reddens in every
direction that weakens the claim --

```
  COUNTER_DEFECT 2.3e-6   1 failed  test_the_counter_DEFECT_SIZE_cannot_be_raised
  COUNTER_DEFECT 1.0e-3   1 failed  same
  COUNTER_DEFECT 1.0e-7   481 passed        (a raise is caught; a lowering strengthens)
  HEADROOM       6.0e6    1 failed  test_the_counter_DEFECT_SIZE_cannot_be_raised
  HEADROOM       1.0e10   1 failed  test_a_RAISED_counter_defect_breaks_that
  HEADROOM       8.0e9    481 passed        (the 434x the entry names, bounded above)
```

`1.0e+6` no longer leaves the suite green; the twelve orders R115 found are now
2.27x. BP3's injection I verified against a textbook Euler-Bernoulli 4x4 written
in my own harness and not read from `beam.py`: the defective block equals it at
relative `0.0` in both planes, the clean block equals the Timoshenko form at
`2.2e-16`, and `K_defect - K_clean` is nonzero at exactly 32 entries, all inside
the two bending blocks -- Phi moves in both planes and nothing else moves. Every
figure in the report reproduces on my run, including all four defect minima and
the `PER-STATE` diagnostic line, and section 8 is the third round running where
the round's own errors are recorded first and were not extracted from me.

**The hold is on four things, and the first is the one this round was about.**
`test_corpus_configurations.py:805-827` -- the shipped file, not the plan --
still carries the withdrawn exclusion verbatim, with the stale figure, one line
above the tuple that now contains the defect:

```
claim   "A third, the dropped shear parameter, is undetectable on 22 of 63
         entries ... That is V2.2's defect, on a stubby member."
rule    the deleted 3.5e-05 response floor
cmd     sed -n 805,828p tests/verification/rung1/test_corpus_configurations.py
out     the sentence, at :825-827, immediately above
        INJECTED_DEFECTS = (..., "dropped_shear_parameter", ...)   :827-828
```

R118's closing condition said "in all three places". Two were done. This is the
site R118 named by path and line.

## Carried

Every item from the thirteenth verdict (`STOP @ de32be3`, committed `a8f36e5`),
traced through `a8f36e5..f8df590` and re-measured, plus the older carry.

- **R115 (STOP) -- CLOSED, and closed with a guard that fires.** The six-cell
  table above is my own run, not the report's. `PATCH_TEST_COUNTER_HEADROOM` is
  bounded from below by the guard passing (`8.686e+06`) and from above by its own
  counter (`8.686e+09`), so the constant that had twelve orders of unguarded room
  now has 2.27x and its guard has 434x. The residual -- that `HEADROOM` itself
  may be raised 434x green -- is disclosed in the entry and in the report as
  `434.3x`. I accept that: moving it is a `tolerances.py` edit under the standing
  rule. What is not closed is the *published boundary* -- **R124**.
- **R116 (STOP) -- CLOSED by removal, and the removal is right.** The per-state
  assertion asserted a `min`-over-states universal the gate never decides on.
  `grep -rn "test_EVERY_STATE_detects_the_small_defect" tests/` is empty; the
  numbers survive as the `PER-STATE` diagnostic, which prints `minimum 0.804x at
  plan_headline_lam2885; 3 of 74 entries below 1.0` on my run -- the exact edge I
  brought last round, now visible instead of asserted.
- **R117 (STOP) -- CLOSED.** `grep -n "red-on-defect check IS the sensitivity"
  docs/milestones/F2.md` is empty; `F2.md:548-555` withdraws the sentence and
  puts the band's removal back on the band's own `1.01x` vacuity. The `5x` claim
  is recorded as `2 of 69` and `none of the 52`, which are my figures and are
  cited as mine.
- **R118 (STOP) -- HALF CLOSED, and the half left is the one R118 named.** The
  substance is answered: the exclusion is withdrawn, `dropped_shear_parameter` is
  in `INJECTED_DEFECTS`, and `0 of 74 / minimum 1739x at plan_headline_lam2885`
  reproduces exactly on my run. The plan and the report say so. The shipped test
  file does not -- **R122**. And the defect arrives with no domain -- **R123**.
- **R119 (blocking) -- CLOSED at three of four named sites, and I withdraw the
  fourth.** The range refuses `1e-300` and my four reds went green, one by
  raising. `:426` and `:526` still construct the section by the bypass route, but
  the guard now states which invariant it is standing in for, which is the
  alternative my own condition offered, so the site is answered. The comment no
  longer calls `Section.__post_init__` "the only guard" while restoring half of
  it. What is left is the range's *justification* -- **R128** -- and BP5's own
  predicate -- **R126**.
- **R120 (recordable) -- CLOSED at two copies of three, and the correction
  over-corrects at one.** `F2.md:640-645` and `test_patch_test.py:966-975` are
  corrected; `test_corpus_configurations.py:819-822` is not, and sits 17 lines
  above its own correction in the same file (**R122**). The corrected text
  itself: **R127**.
- **R121 -- credit, correctly recorded as such.**
- **R113 -- carried, OPEN, correctly declared.** `grep -n "_section(entry"
  tests/verification/rung1/test_corpus_configurations.py` still returns `:656`
  inside `_inadmissible`.
- **R95 -- carried, OPEN, correctly declared.** `pytest.raises(ValueError)` with
  no `match` at `:721`.
- **R97 -- carried, OPEN, correctly declared.** `grep -n "never asserted at a
  constant" docs/milestones/F2.md` returns `:697` and `:1412`.
- **R98 -- carried, OPEN, correctly declared.** `INADMISSIBLE` assigned at
  `:662`, four occurrences, none an assertion.
- **R100 -- carried, OPEN, and it took on weight this round.** `ls scripts/` is
  still `write_verdict.py` alone. Three of the five figures in the new
  `PATCH_TEST_COUNTER_HEADROOM` entry are printed by the shipped test and
  regenerate; two are not, and one of those two is wrong -- see **R124**. That is
  BI3's stated failure mode arriving in the entry written the same week BI3 was.
- **R101, R102, R103 -- carried, OPEN, correctly declared.** `grep -n "revision
  1" floatfea/tolerances.py` returns `:189` and `:616`, both "revision 10".
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Correctly recorded.
- **R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 -- still
  open**, correctly declared, routed to step 4a or later.
- **R77, R78, R81-R94, R96, R99, R104-R112, R114 -- closed** at earlier verdicts,
  correctly recorded.
- **R68's standard -- HELD.** Eight rounds of seven. Section 7 names every item
  by number and section 8 puts the round's own three errors first, one of which
  ("I inherited a figure without asking its rule, in the commit that changed the
  rule") is the sharpest sentence in the report.

## Findings

**R122. (blocking) The withdrawn exclusion is still in the shipped file, with
its stale figure, one line above the tuple that refutes it -- and two further
figures in the same file were measured on a corpus that no longer exists.**
`tests/verification/rung1/test_corpus_configurations.py:808`, `:819-822`,
`:825-827`, `:904-909`.

Four stale statements, all in the one module this step edited:

```
:808     "`dropped_flip` and `wrong_dof_index` are injected into
          `local_stiffness`"                      -- three are, since :763
:819-822 "on 2 further near-axis entries the injected difference leaves the
          balance below the ceiling"              -- R120's third copy, uncorrected,
          17 lines above its own correction at :838-842
:825-827 "A third, the dropped shear parameter, is undetectable on 22 of 63
          entries ... That is V2.2's defect"      -- R118's exact site, and the
          defect is in INJECTED_DEFECTS at :827
:904-909 "Measured minima of response/ceiling over every solved entry:
            dropped flip             5.150e+09x  at L/r_min 2332
            one wrong DOF index      5.227e+09x  at L/r_min 1058"
```

The last is not merely incomplete (three rows where four defects ship); it is
**refuted by the report's own regenerated table at the same commit**, which the
runner and I both reproduce:

```
rule  worst state against PATCH_TEST_EXACTNESS, over the 74 solved entries
cmd   python -m pytest -q -s tests/verification/rung1/test_corpus_configurations.py -k REPORTED
out   dropped_flip     2.530e+09x at every_state_edge_thickwall_L50 (L/r_min 3331.5)
      wrong_dof_index  7.087e+08x at plan_headline_lam2885          (L/r_min 2885.5)
```

A factor of 2.0 and 7.4, and different entries. Those docstring figures were
measured on the 69-entry corpus; the corpus went to 74 solved at `b0bf881`, which
is *before* this step's first commit. Nobody edited them and they are wrong,
which is the sentence BP0 was written to make impossible -- and BP0 shipped in
this range. `docs/reports/F2/step-4.md:2104` and `:2109` carry the same two
sentences, but that document is append-only over fourteen revisions and revision
14 supersedes them in text; I do not count those two.

**Closed when** each of the four sites is answered site by site: `:808`
enumerates what is injected, `:819-822` says what was measured or defers to
`:838-842`, `:825-827` goes with the exclusion it justified, and `:904-909` is
regenerated at its commit or replaced by a pointer to the line the runner prints.
`CLAUDE.md` sec. Step gating, "A closing condition that names sites is closed
site by site".

**R123. (blocking) The fourth defect is asserted over every solved entry with no
stated domain, its edge is at `L/r_min ~ 1.9e4` on a plain circular tube, and the
mechanism published with it puts that edge 6.4x further away than it is.**
`tests/verification/rung1/test_corpus_configurations.py:828`, `:887-935`;
`docs/milestones/F2.md:535-544`; report sec. 2.

The plan's own sentence is correctly scoped -- "it does not take it below the
ceiling **anywhere in the corpus**" -- and that is true and reproduces. The
assertion is not scoped, and the mechanism attached to it is:

```
claim  "`Phi ~ 1/lambda^2` does shrink the shear defect on a slender member"
rule   worst state against PATCH_TEST_EXACTNESS
cell   D=0.600 t=0.01200 axis, L the ONLY variable moved
out    L        600     2000     6000
       L/r     2886     9618    28860
       x       1739    14.09   0.1739     -- margin falls as lambda^-4.0, not ^-2
```

The defect itself does shrink as `Phi ~ 1/lambda^2`; measured at
`plan_headline_lam2885`, `Phi = 7.337e-05` and the bending block moves by
`5.503e-05` relative. The *margin* falls at twice that exponent. Under
`lambda^-2` the edge is at `L/r_min ~ 1.2e5`; solved, it is at `~1.9e4`. That is
the difference between a number no corpus will reach and one 5.6x past the
corpus's most slender entry -- which my fourteenth-round corpus now reaches, on
two section families:

```
  shear_edge_iso_L4000   D=0.600 t=0.01200 axis L=4000  L/r 1.924e+04  0.8806x  RED
  shear_edge_thin_L400   D=0.050 t=0.00100 axis L= 400  L/r 2.308e+04  0.4247x  RED
  shear_edge_iso_L3000   same family, L=3000            L/r 1.443e+04  2.783x   green
  shear_edge_thin_L200   same family, L= 200            L/r 1.154e+04  6.795x   green
  shear_edge_iso_L4000_skew  same GEOMETRY, skew        L/r 1.924e+04  1.069x   green
```

Both reds are plain circular tubes, no extras, no synthetic anisotropy, clean
field at `0.0000x` and `0.0098x` -- the element is fine at both and only the
control loses. The skew entry is the one that matters for the shape of the
answer: at identical geometry, orientation moves the margin by `1.21x` and puts
it on the other side, so the edge is a surface and `L/r_min` alone does not
locate it. The defect responds in the `shear` and `shear_xz` states only, which
is right.

This is R116's species arriving on the defect that replaced it, one commit later.
The difference, and it is a real one: R116's edge was inside the corpus at the
commit that shipped it; this one I had to write two entries to reach.

**Closed when** the assertion states the sample it is asserted over and the
solved edge, or the measured exponent replaces `lambda^-2` in the plan, the
report and the `_defective_stiffness` comment. Either is fine; a corpus-wide
assertion whose published mechanism is 6.4x optimistic about its own domain is
what is not.

**R124. (blocking) "Any raise of `2.31x` or more fails the build" is refuted by
the runner: `2.30x` fails, and the solved boundary is `2.26x .. 2.28x`. The
arithmetic assumes the detection edge is independent of the constant it bounds,
and `_hardest_entry` selects using that constant.**
`floatfea/tolerances.py:487-489`; `docs/milestones/F2.md:557-560`; report sec. 3.

*Invert the decision rule and solve*, which the entry does by arithmetic instead:

```
rule  ratio = COUNTER_DEFECT / _detection_edge(_hardest_entry())  <=  2.0e7
cmd   COUNTER_DEFECT moved, everything else held, one test run each
out   1.00e-6  pass  edge 1.1513e-13 at slender_axis_L_r_189       2.30x of room
      2.20e-6  pass  edge 1.1491e-13 at posed_axis                 1.04x
      2.26e-6  pass  edge 1.1380e-13 at straddle_above_lam61_axis
      2.28e-6  FAIL  edge 1.1380e-13 at every_state_edge_iso_L90
      2.30e-6  FAIL  edge 1.1491e-13 at tier2_in_plane_y_lam70
```

The named entry changes five times across that sweep. `_hardest_entry`
(`:968-976`) selects on `max` over states of `_oob_with_injected(...,
one_element_scaled)`, which is evaluated at `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`
-- so the edge is a function of the constant the guard bounds, and `edge x 2.0e7`
is not the boundary. The error is in the safe direction: the guard is ~2% tighter
than advertised, not looser. It is still a published measured boundary that the
file's own runner refutes, in `tolerances.py`, in the round about figures
republished under a rule that moved. `1.15x` and `1.16x` in the same paragraph
are the same arithmetic; that direction (a sensitivity improvement, with
`COUNTER_DEFECT` held) does not move the selection, so those two survive as
reasoning -- unmeasured, but not refuted.

**Closed when** the two sentences state the solved boundary, or the entry says
the boundary is solved by the shipped test and carries the one number the test
prints, per BI3's second option.

**R125. (recordable) "The entry with the least margin" is a two-way exact tie
broken by corpus file order, and the winner is named as a measurement in two
files.** `tests/verification/rung1/test_corpus_configurations.py:968-976`;
`floatfea/tolerances.py:487`; `docs/milestones/F2.md:557`.

```
cmd   count SOLVED entries whose max-over-states one_element_scaled response
      equals the minimum exactly
out   2 of 74 -- slender_axis_L_r_189, slender_in_plane_y_L_r_94
      (8 entries tie at 8.701e+06x to four digits)
```

`min()` returns the first. `slender_axis_L_r_189` is a fact about line order in
`g22_model_configurations.txt`, published as a fact about which configuration is
hardest to detect. The bisected edges differ by 0.2% across the tied set, so
nothing numerical turns on it; the sentence does.

**Closed when** the entry says the minimum is tied and the selection is
order-dependent, or `_hardest_entry` breaks the tie deterministically on
something stated.

**R126. (blocking) BP5 asserts "a defect that changes nothing is not a pass" with
a predicate that calls a `3.5e-301` change a pass, and it is green on the
configuration R119 named as the vacuous one.**
`tests/verification/rung1/test_corpus_configurations.py:832-869`, `:914-926`,
`:938-960`.

```
cell  D=0.600 t=0.01200 stations=9.67 axis, I_y_over_I_z swept, range guard
      bypassed for measurement only
out   ratio    injected_delta(dropped_flip)   worst-state response / ceiling
      1e-6            3.497e-07                        1.072e+07x
      1e-14           3.497e-15                          0.1072x   dead
      1e-30           3.497e-31                          0.0162x   = the CLEAN value
      1e-300          3.497e-301                         0.0162x   = the CLEAN value
```

At `1e-300` the guard reads `delta = 3.497e-301 > 0.0` and passes, while the
defect produces exactly the clean response -- a control certifying nothing, which
is BP5's own definition of the thing it exists to catch. `> 0.0` is a "small
number" guard in `CLAUDE.md`'s sense, it is a local literal outside
`tolerances.py`, and it has no scale.

Three further properties of the same guard:

* It **cannot fire on any of the four shipped defects.** For
  `one_element_scaled` the delta is `CD * max|to_global(k,R)| / max|K|`, positive
  by construction; for the three `local_stiffness` defects it is positive for any
  section with positive `I_y`, `I_z`, `J`, `A`. All 296 pairs are live and the
  aggregate test's `dead` list is empty by construction, not by luck.
* It ships **without a negative control**, in the round whose sibling guard BP1
  ships with one. Nothing in the suite demonstrates that `injected_delta`
  returning zero turns anything red.
* Its motivating case **cannot be expressed in it**: the transposed transform is
  not in `INJECTED_DEFECTS` and `_defective_stiffness` has no branch for it, so
  `injected_delta(entry, "transposed_transform")` returns `0.0` -- as does
  `injected_delta(entry, "typo_defect")`, because `_defective_stiffness` builds
  the *clean* matrix for any name it does not recognise rather than raising.
  ("An unsupported case raises, it never defaults.")

For `one_element_scaled` the function also does not observe the path under test:
it reconstructs `element_global_stiffness(m, els[1])` inline (`:846-856`) rather
than calling it, so it is a parallel implementation of the injection, not a
measurement of it. Today the two agree exactly; if the real path in `_measure`
(`:509-518`) broke, this guard would still read positive and the red-on-defect
assertion would be the one to catch it.

**Closed when** the guard's threshold is a stated scale rather than `> 0.0` and
lives where thresholds live, or the report states that `delta > 0` is a
structural non-emptiness check that cannot fire on the shipped defects and names
what would. Either is honest; "controls that cannot be vacuous" as a section
title is what is not, while the control is vacuous.

**R127. (recordable) R120's correction over-corrects: the difference is present
on the second entry, and "in both" is the word that makes it wrong.**
`tests/verification/rung1/test_patch_test.py:970-974`.

```
claim  "In both the difference is ABSENT from the assembled matrix, not present
        and too small to see."
rule   max|to_global(k, R.T) - to_global(k, R)| on the injected element
cmd    build els[1] on each entry, compare the two transforms
out    onode_just_outside         |R-R.T|=2.0000  diff = 0.0000e+00  exactly zero
       straddle_above_lam61_axis  |R-R.T|=1.1969  diff = 1.8264e-12  rel 3.0873e-18
```

`1.83e-12` is present. It is round-off, and "present and too small to see" is
precisely what it is. My own thirteenth verdict wrote `3.09e-18 (round-off)` and
the correction generalised the first entry's *exactly zero* over both. Third
round in three where the number is right and the mechanism sentence attached to
it is not -- this time in the correction of the previous one. `F2.md:640-645` and
`:838-842` in the corpus module generalise from the same single measurement but
do not say "both", so they are weaker rather than wrong.

**Closed when** the sentence separates the two entries, or measures the second.

**R128. (recordable) The declared range's stated reason is in the quantity BP2
deleted in the same commit, and the derived boundary exists, is seven orders
away, and was not taken.**
`tests/verification/rung1/test_corpus_configurations.py:172-188`, `:365-375`.

The declaration is honest -- "The range is declared rather than derived, and it
is deliberately generous" is the right sentence and I credit it. The *reason*
clause is not: "a denormal ratio builds one whose **weakest-state** response to a
defect is exactly `0.0`, which is a control that certifies nothing". That is true
(I reproduce `0.0` exactly at `1e-300`, `orient=axis`) and it is measured in the
per-state quantity `test_EVERY_STATE_detects_the_small_defect` asserted -- which
BP2 removed, 500 lines away, in the same commit. Under the rule that ships, what
actually breaks at small ratio is `dropped_flip`:

```
rule  worst state against PATCH_TEST_EXACTNESS
cmd   bisect the ratio at which dropped_flip stops exceeding the ceiling
      (skew, D=0.600 t=0.01200 stations=9.67)
out   ~7.897e-14 -- the declared floor 1e-6 is 1.27e+07x above it
```

So the guard is right, conservative, and justified by a deleted assertion instead
of by the live one. Four corpus entries this round pin the declared boundaries:
`1e-6` and `1e6` are admissible and green everywhere, `9e-7` and `1.1e6` are
refused.

A consequence worth naming rather than treating as a defect: the implementer's
parser now declares which corpus entries are admissible, and the declared floor
sits seven orders above the measured edge of a shipped assertion, so the region
where `dropped_flip` degrades from `1.07e+07x` to `1.07x` cannot be written as an
`expect=hold` entry at all. The disagreement is still reportable -- such a line
reddens `test_the_corpus_entry_behaves_as_the_reviewer_recorded` -- so the
mechanism holds. It is the second guard to narrow the corpus's reach and the
first whose bound is declared rather than physical.

**Closed when** the reason clause names the live quantity, or states that the
floor is declared conservative against a measured edge of `~1e-13`.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` | -- | `2.0e7` **new** | relative, dimensionless -- a bound on the ratio of a defect size to the solved detection edge | `test_a_RAISED_counter_defect_breaks_that`, in the defect quantity: `x1e3` gives `8.686e+09x` the edge, `434.3x` past. Verified by moving the constant: reddens below `8.686e+06`, its counter reddens above `8.686e+09` | `tolerances.py:467-495`, `F2.md:545-573`, report sec. 3 -- **and its `2.31x` boundary is refuted (R124)** |
| `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` | `1.0e-6` | `1.0e-6` unchanged | -- | -- | now bounded above; R115 closed |
| `PATCH_TEST_EXACTNESS` | `5e-15` | `5e-15` unchanged | -- | -- | untouched |

`I_Y_OVER_I_Z_RANGE = (1.0e-6, 1.0e6)` is a new constant in the **test module**,
not in `tolerances.py`. It is a corpus-admission bound on a synthetic field, not
a comparison threshold, and I accept it where it sits -- but it decides what a
control may be measured on, which is why R128 asks for its reason and not for its
value. `delta > 0.0` at `:919` is a threshold under another name and it is a
local literal (R126).

`git diff a8f36e5..f8df590 -- floatfea/tolerances.py` is `+31 -0`: one addition,
nothing moved, nothing removed. `grep -rn "xfail|pytest.skip" tests/` returns
nothing. `git diff --stat a8f36e5..f8df590 -- tests/regression tests/corpus` is
empty -- no golden file moved and no `expect` on any corpus line was touched.

I re-derived every published figure independently. `1.1513e-13`, `8.686e+06x`,
`434.3x`, `1739x`, `2.530e+09x`, `7.087e+08x`, `8.701e+06x`, `0.804x`,
`3 of 74`, `0.0887x`, `|R-R.T| = 2.000` and `1.197`, `Phi = 7.337e-05` -- **all
reproduce**. Every number the report publishes is right. Two sentences built on
them are not, one guard is green where its own section title says it must be red,
and four sentences in the shipped module were true under a corpus and a rule that
no longer hold.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: the
locked plan is right, the element is not implicated in anything here, the suite
at `f8df590` is green on my run, and both reds at `dac209e` are mine. `F2.md`
does not need to reopen; one step commit answers all of this.

1. **R122 -- four stale sites in one shipped module**, one of them R118's own
   named site standing as the reason for an exclusion that the line below it
   withdraws. Cheapest of the four and the least defensible to leave, and it is
   BP0's rule broken inside the BP0 commit.
2. **R123 -- the fourth defect's domain.** State the sample and the solved edge
   (`L/r_min ~ 1.9e4`), or replace `lambda^-2` with the measured `lambda^-4.0`.
   Two of my new entries are red on it.
3. **R126 -- BP5's predicate.** `> 0.0` passes at `3.5e-301` on R119's own
   configuration. Either give it a scale or say plainly that it is a structural
   non-emptiness check that cannot fire on the four shipped defects.
4. **R124 -- the published boundary.** `2.30x` fails; solve it, or point at the
   line the runner prints.
5. **R125, R127, R128 -- recordable**, answerable in prose.
6. **R113, R95, R97, R98, R100-R103 -- carried, unchanged**, answerable in the
   next report's `Carried` section.

**Adversarial corpus (BE3): 9 new entries committed, all unseen by the
implementer; 2 red at `f8df590`, 7 green as predicted.**
`tests/corpus/g22_model_configurations.txt`, now **105**, committed separately at
`dac209e` immediately before this verdict and touching no code. Full suite with
the corpus applied: **2 failed, 895 passed**. Every outcome was measured before
the line was written.

The coverage measurement, stated plainly: **two entries cross the undeclared edge
of the assertion this step added, on two different section families and on plain
circular tubes with no extras; one shows that at identical geometry the
orientation moves that margin across the edge; two bracket it from inside; and
four pin the declared anisotropy range at both of its boundaries.** The
implementer's own count -- 74 solved entries, four injected defects, 296 live
pairs -- is what it is, and BP5's `dead` list is empty by construction rather
than by measurement (R126).

**Fourteen consecutive rounds have found no element defect**, and the guard's
reading is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other
side. What changed this round is that the errors got smaller and moved. BP0 is
the right mechanism and it worked where it was applied: every figure the *report*
publishes was re-taken at this commit and every one reproduces. What it did not
reach is the shipped source file, where four sentences were left describing a
corpus of 63 entries and a tuple of three defects. The rule says "every figure
citing the old rule is regenerated or withdrawn in the same commit"; the commit
regenerated the report and edited the code twenty lines below the comments that
needed it. **A rule applied to the document that is regenerated by rule, and not
to the file that is regenerated by nobody, is applied backwards.**

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Fourteen consecutive reviews by one reader, and the standing consequence is
unchanged.

**The standing question for the next round:** for every sentence in the shipped
`floatfea/` and `tests/` sources -- not the report, which is regenerated by rule
-- **what is the command that checks it, and when was it last run?** The report
is the document this project has taught itself to regenerate. The comments are
the document it reads.
