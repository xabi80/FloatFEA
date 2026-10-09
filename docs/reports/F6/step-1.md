# F6 step 1 — API RP 2A-WSD tubular member checks

# Revision 1 — the six clauses, the first full pass, and FA2's answer

Answers: FA3 opens the step

**2026-10-09.**

## 1. The schedule, and what this revision is

**F6 step 1's working target is 22 October and it holds.** Today is 9 October. The
committed date is 28 October.

**The deliverable went first, per FA3 and EY0's ordering.** `docs/F6_utilisation.csv`
(256 rows) and `docs/F6_utilisation.md` were sent before any of this report's guard work
existed. What this revision records is what was built and what it measured; **G6.1's
documented hand calculations are not in it** and are named in § 6 as the step's remaining
work.

**The step marker moved in this commit and not in the one before it.** FA3 says "the marker
moves in its first commit"; `test_the_plan_names_the_step_under_execution` says it is
"advanced in the commit that adds the next step's report, never before it". That is C27's
unresolved conflict, and it has now been directed one way and enforced the other. Both are
satisfied here because this commit carries both — stated rather than left as a silent
choice. **C27 still needs ruling for the general case.**

## 2. What step 1 built

`floatfea/checks/api_wsd.py` — six closed-form clauses, one function each, SI throughout.

```
claim  every allowable reproduces hand arithmetic
cmd    python -c "from floatfea.checks.api_wsd import *; ..."
out    F_t = 0.6 Fy            = 213.00 MPa   (hand: 213.00)
out    F_b, D/t=13.9           = 266.25 MPa  branch=compact   (hand: 266.25, compact)
out    F_v = 0.4 Fy            = 142.00 MPa   (hand: 142.00)
out    C_c = sqrt(2 pi^2 E/Fy) = 108.059            (hand: 108.059)
out    F_a at KL/r=  60.8      =  161.05 MPa  branch=inelastic
out    F_a at KL/r= 121.5      =   73.25 MPa  branch=elastic
out    F_e at KL/r=121.5       = 73.25 MPa   (hand: 73.25)
rule   API RP 2A-WSD sections 3.2.1, 3.2.2, 3.2.3, 3.2.4
judge  spot checks, not G6.1. **G6.1 asks for each check against an INDEPENDENT hand
       calculation documented in `docs/verification/`, and that does not exist yet** (§ 6).
       These seven lines catch a gross error and nothing subtler.
```

**The SI coefficients are the ones that matter and they are named in the module.**
§ 3.2.3's branch limits are `10340/F_y` and `20680/F_y` with `F_y` in **MPa**; writing the
US forms against a pascal `F_y` would misplace every branch boundary by about `145x`. The
two conversions happen in one place each.

**`D/t > 300` is refused rather than extrapolated.** The clause's third branch is written
only that far; beyond it local buckling governs and a beam-level allowable would be an
invented clause.

## 3. FA1 — the allowable F4's table was comparing against was the wrong one

```
claim  the 213.0 MPa reference is generic 0.6 Fy, not the API bending allowable
cmd    python -c "Fy=355.0; print(10340/Fy, 20680/Fy, 0.75*Fy, 0.6*Fy)"
out    10340/Fy = 29.13   20680/Fy = 58.25
out    D/t = 13.9 <= 29.13  ->  section 3.2.3 first branch
out    F_b = 0.75 Fy = 266.25 MPa     against the generic 0.6 Fy = 213.00 MPa
rule   API RP 2A-WSD section 3.2.3
judge  the generic reference is **1.25x conservative on bending** for this section. F4's
       table, summary and closure artifact are relabelled -- a published-deliverable
       correction under EZ0, folded into issue 5 rather than resent for itself.
```

## 4. FA2 — and the answer is that the axial term contributes almost nothing

This is the finding of the pass and it was not what I expected when EZ4 locked `K = 2.0`.

```
claim  the K lock moves four members onto a different formula and barely moves a number
cmd    python scripts/measure/api_wsd_utilisation.py
out    axial branch over 256 rows : elastic 32; inelastic 96; tension 128
out    largest |U(K=2) - U(K=1)|  : 0.024114  at platform:hub1_arm TIP (elastic)
out    worst compression station  : U = 1.70984  with U(K=1) identical
out    at the worst station: u_axial = 0.0004  against  u_bending = 1.815
rule   API sections 3.3.1 and 3.3.2; EZ4 Q3's K = 2.0 with FA2's K = 1.0 column
judge  **both halves are true and the second is the one that matters.** At `K = 2.0` the
       50 m platform arms do cross `C_c = 108.06` into the elastic branch while the 25 m
       hub arms stay inelastic -- the branch split § 0 of the plan predicted. But bending
       governs by three orders of magnitude, so § 3.3's interaction is bending plus a
       rounding error, the `C_m / (1 - f_a/F_e')` amplification never bites, and on the
       compression rows the simple `0.6 F_y` form of § 3.3.2 governs over the amplified one
       -- which contains no `K` at all. **The choice that looked like the biggest modelling
       decision in the check changes the governing number by at most `0.024`.**
```

It would matter on a member carrying real axial load. None of these does, and a reader who
was told only "K is the biggest sensitivity" would have mis-weighted the whole check.

## 5. The result

```
claim  four member-stations exceed unity and the governing clause is the same for all four
cmd    python scripts/measure/api_wsd_utilisation.py
out    4 of 32 member-stations exceed U = 1.0, the worst at 1.815
out    1  platform:hub2_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.815
out    2  platform:hub4_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.814
out    3  platform:hub3_arm ROOT  T = 16.2 s  3.3.1 interaction  U = 1.202
out    4  platform:hub1_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.188
rule   EZ2's governing basis: T = 12.5, 14, 15, 16.2 s; ROOT and TIP only (FA3)
judge  all four are platform arm ROOTs, all § 3.3.1, all on bending, and three of the four
       are at `T = 12.5 s` -- the band's lower edge, which FA0 ruled stays and which
       governs because the response rises as `T` falls across the band.
```

**This is a finding about the section and the plan said so in advance.** The tube is a
stiffness equivalent for a truss of undecided depth, and F4 already had the static root at
`269.7 MPa` against a `213.0 MPa` reference under self-weight alone. `U = 1.815` on an
indicative screen of a stand-in section is the expected outcome, not news, and nothing was
tuned to bring it under unity.

## 6. What step 1 has NOT done

* **G6.1 is not met.** Each check needs an independent hand calculation documented in
  `docs/verification/api_wsd/`. § 2's seven lines are spot checks against arithmetic I did
  in the same sitting, which is not an independent path.
* **No counter-case per clause.** A check that cannot redden certifies nothing; each needs
  an injected input that pushes the utilisation past unity, with the injection size
  declared.
* **No tolerance is declared yet**, and none should be until the hand calculations measure
  what the closed forms agree to.
* **MID is excluded** (FA3) until R730's conditions are discharged — the closed-form
  midspan is a measured `4.0%` approximation on bending, unverified against a refined mesh.
  The exclusion is in the code, not in a note.
* **No circumferential stress recovery, no CalculiX cross-check, no VTK.** G6.2 and F7.

## 7. Carried

R730, R731 and R732 carry from F4's ledger, R730 and R731 blocking. C27 needs ruling for
the general case (§ 1). Nothing from F4's closure items is discharged here.
