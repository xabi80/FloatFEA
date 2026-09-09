# F2 step 5 — V1.1 rigid-body modes, gate G2.1

Answers: verdict 25 @ aae355a

**2026-09-09.** Three commits since step 4's PASS: `2f92c58` (figures), `7774e14`
(closure) and `b67163f` (`process:`), then `4a23232` (plan, re-locked) and
`d1fea41` (step).

## 0. What this step is, and one input it did not have

G2.1: an unconstrained assembly has exactly six zero-energy modes. The gate is
two assertions, four declared tolerances, two negative controls in opposite
directions, and two injected counters — all in the first commit, per BZ2.

**One thing is recorded before anything else, because it is a gap and not a
choice.** The directive names "AX3's shape" for this step's model. **`AX3` does
not exist in this repository.** A grep over every file finds it only in prose I
wrote in two revisions of the step-4 report, from which it entered the directive.
The plan's own case table says V1.1's reference is *constructed*, and the
verification README says only "an unconstrained model", so a constructed frame is
what the locked plan asks for and is what shipped. If `AX3` names a real platform
shape, the gate and both controls are unchanged and only `_frame()` moves — but
the geometry is not something I will invent a meaning for.

```
cmd    grep -rni "ax3" over the whole repository, excluding .git
out    two hits, both in docs/reports/F2/step-4.md, both mine, both prose
cmd    the plan's case table row for V1.1
out    "| V1.1 | constructed | 6 zero eigenvalues by ratio ... | G2.1 |"
```

## 1. The gate

```
cmd    python -m pytest tests/verification/rung1/test_rigid_body_modes.py -q
out    8 passed
       lambda_6 4.2634e-07  lambda_7 2.6631e+07  ratio 1.6009e-14 vs 1e-12
       worst analytic vector outside the computed span 5.3061e-15 vs 1e-13
rule   ratio <= RIGID_BODY_MODE_RATIO and loss <= RIGID_BODY_SUBSPACE_LOSS
```

**A ratio, because G2.1 says so and the reason is in the statement.** The
eigenvalues of a stiffness matrix carry units and scale with `E`, with the
section and with the mesh. A ceiling on them would be a ceiling on the model.

**The span assertion is the half AP3 calls the real content.** Inside the
six-fold degenerate zero eigenvalue the eigenvectors are an arbitrary basis —
non-unique *in principle*, not merely non-reproducible — so asserting mode shapes
asserts what the mathematics does not confer. What is invariant under every basis
choice in that block is that the six analytic rigid-body vectors lie in the
computed span. Measured on the **worst** of the six, never on a mean.

## 2. The controls, and the one that failed first

```
cmd    the pinned-DOF control, at every one of the 30 degrees of freedom
out    nullspace dimensions {5} -- not a chosen DOF, all of them
cmd    the torsional-release control
out    lambda_7 4.4889e-07  lambda_8 2.6884e+07  nullspace 7
```

**The release control read SIX on its first version, and it was right to.** The
frame put the released member off-axis. The assembled matrix is in global
coordinates, so cutting a global rotation is not cutting a member's torsion: no
mechanism was created and the control measured nothing while claiming to build a
seventh mode. The member is parallel to global x now, so its torsion **is** the
component being cut, and the control asserts that premise about its own geometry
before it measures anything.

That is the whole argument for having built it: the gate was green through both
versions, and only the control could tell the difference.

**The release is built by DOF mapping**, because `releases.py` is step 11 and
does not exist. The released member's rotation about its own axis is assembled
into one extra scalar degree of freedom instead of into the shared node's. The
extra mode is provable rather than measured — that member can twist rigidly about
its own axis at zero strain energy while nothing else moves — which is why the
control asserts an exact count rather than a threshold.

## 3. Four tolerances, each set from the first run

| name | value | clean | headroom | counter | response |
|---|---|---|---|---|---|
| `RIGID_BODY_MODE_RATIO` | `1e-12` | `{{fig:rigid_body_mode_ratio}}` | ~62x | `1.0e-12` | `{{fig:rigid_body_counter_ratio}}` |
| `RIGID_BODY_SUBSPACE_LOSS` | `1e-13` | `{{fig:rigid_body_subspace_loss}}` | ~19x | `1.0e-12` | `{{fig:rigid_body_counter_loss}}` |

**Both counters are one defect**, and that is content rather than economy: a
diagonal stiffness resisting a rigid translation must lift a zero eigenvalue
**and** remove that translation from the span. One defect, both halves.

**Every figure above is a generated name from this gate's first commit.** R194's
remedy is applied at the start here rather than five rounds into it, which is the
one thing step 4 would have wanted done differently.

```
cmd    the defect sweep, one variable moved, at this commit
out    size    1e-14      1e-12      1e-08
       ratio   3.03e-13   3.06e-11   3.06e-07
       loss    7.59e-14   7.47e-12   7.47e-08
judge  linear over eight decades, so the ceiling is crossed by a defect between
       1e-14 and 1e-13 of the largest entry. The counter sits one decade above
       that crossing deliberately: a counter on its own detection edge tests the
       edge rather than the gate.
```

## 4. Both counters are registered, and pass both cells

```
cmd    python -m pytest tests/test_counters_are_injected.py -q
out    14 passed  (5 registered x 2 cells + 3 controls + the registry test)
```

They inject through `assembled`, the one function both gates read, so the
**shipped** gate computes the defective number and decides on it. A counter that
builds a defective matrix itself and compares the result with the ceiling never
runs the assertion it defends — R163's defect, three times in step 4.

**Their widened ceilings are measured, not typed.** The injection is a defect
*size*, so how far it lifts the quantity is a property of the frame;
`counter_response` returns it at the commit that runs. A literal there would be
stale the first time the frame moved.

## 5. The `v0` pin, and where I departed from the directive's wording

BZ2 says "`v0` pinned". **The gate is a dense symmetric eigensolve and has no
starting vector**, so pinning one would be vacuous, and choosing ARPACK for the
gate in order to have a pin to point at would be choosing a less accurate method
to satisfy a guard. What AP3's pin actually buys is that the ARPACK path is
reproducible, and that is asserted directly:

```
cmd    two ARPACK runs from determinism.deterministic_v0
out    max |difference| 0.000e+00, bit-identical
cmd    two runs from an UNPINNED random start
out    they differ, max |difference| 1.490e-07
judge  the second is the control. If two unpinned runs ever agreed, the pinned
       assertion would pass with the pin removed, and it fails rather than skips.
```

This is a departure from the literal wording and it is flagged rather than
buried. If the ruling is that the gate itself must run ARPACK under the pin, that
is a plan change and it comes back to the supervisor.

## 6. Carried

| item | status |
|---|---|
| step 4's twenty-fifth verdict | **PASS** at `4ccd166`. Its corpus round is regenerated in `2f92c58`, its closure artifact is `7774e14` |
| R200–R204, R206, R210, R215–R220, R222 | **open at 4a**, unchanged by this step and untouched by it |
| R221 — the ceiling margin is defended by a corpus that samples the interior | **open at 4a, and named first.** One round of searching the admissible corners halved it, `7.93x -> 3.62x` |
| R218 — a step report that states no suite count | **answered here**: `1578 passed, 0 failed, 0 skipped` |
| every earlier item | **as declared in the step-4 closure artifact**, `docs/closure/F2-step4.md` |

**Nothing from step 4 is carried as unanswered into this step**, because step 4
closed on a PASS. The 4a list is in the closure artifact by name, which is half
of R220's condition; the other half is `docs/milestones/F2a.md` carrying it with
the verdict each item came from, and that is 4a lock work.

## 7. What I am asking for

**A PASS**, or a **HOLD naming the item.** Two things I would rather have ruled
on than left:

1. **`AX3`.** The frame is constructed, which is what the locked plan asks for.
   If a specific platform shape was meant, say so and only `_frame()` moves.
2. **The dense eigensolver**, §5. The directive says the pin; the gate has
   nothing to pin, and the pin is exercised on the path that has one.

## 8. Witness

**The channel is open for the first time this milestone**: `xabi80/FloatFEA`,
private, PR #1, `F2 -> master`. Steps 1 to 4 have no witness comment and never
will — twenty-five consecutive reviews of step 4 were written by one reader, and
opening the channel now does not change that. **Step 5 is the first step that can
carry one.** There is no `[witness ...]` comment yet, which is an unavailable
check rather than a pass.
