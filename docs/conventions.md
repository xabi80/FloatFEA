# Conventions

**Status: LOCKED at F0, 2026-08-10.** Gate G0.2.

This document is authoritative. Where any other file, comment, or docstring
disagrees with it, this file wins. Changing it requires reopening the F0 gate,
not an inline edit.

Every entry is either **verified against FloatSim source** (file and line cited)
or explicitly marked **UNRESOLVED**. Nothing here is inferred and then presented
as settled. An UNRESOLVED entry is a question to answer, not a default to rely
on.

Filled from the G1.0 output audit (`docs/milestones/F1.md`), not from
assumption.

---

## The governing principle: reconstruct as produced, not as correct

**When FloatFEA reproduces any quantity FloatSim computed, it reproduces the
formulation FloatSim used — not the better one.**

Consistency with the source beats accuracy against the truth, because every
equilibrium and reconciliation gate in this project tests *self-consistency of
the load path*. An improvement applied on one side of a comparison shows up as a
residual, and it shows up looking like a mapping bug rather than like the
improvement it is. The place to fix upstream physics is upstream, under its own
gating — never silently, on the way past.

Three instances are already locked, which is why this is stated as a rule rather
than repeated as a special case:

| instance | reconstruct as | not as |
|---|---|---|
| Buoyancy for G4.6 | **mean** wetted surface, matching FloatSim's linearisation | instantaneous wetted surface |
| Rotations (below) | the parameterisation the **producing module** used | one globally "correct" parameterisation |
| Timestamps (below) | the index the force was **evaluated from** | the index it was applied at |

The rule decides the fourth case in advance. Departing from it in any specific
instance requires reopening this gate and recording why, in the milestone
closure artifact — it is not a judgement call to be made at the call site.

The rule is *not* a licence to propagate an upstream defect silently. Where the
source formulation is inconsistent with itself — as the rotation channels are —
that is escalated as a finding about FloatSim (see `docs/milestones/F1.md` §10
Q2), and the affected quantity is reconstructed per-producer *and* the resulting
inconsistency is quantified rather than absorbed.

---

## Units

SI throughout, internally, with no exceptions: metres, kilograms, seconds,
newtons, radians. Conversion happens only at the I/O boundary. A conversion
found inside the numerics is a defect.

| quantity | unit |
|---|---|
| Length | m |
| Mass | kg |
| Time | s |
| Force · Moment | N · N·m |
| Angle | rad |
| Stress | Pa |

**FloatSim agreement: confirmed, dimensional SI throughout.** FloatSim carries
no non-dimensionalisation and no unit-system switch; decks and results are SI.

**Gravity is 9.81, not 9.80665.** `studies/cluster-3buoy-rigid/cluster_common.py:26`
sets `G = 9.81`, passed into every deck as `Environment(gravity=...)`. FloatFEA
**must use 9.81 exactly**. The difference from standard gravity is 1.7e-5
relative — negligible as physics, and *not* negligible as a discrepancy, because
a gravity mismatch appears downstream as an unexplained mass error and would be
hunted in the wrong place. Water density is `RHO = 1025.0` kg/m³
(`cluster_common.py:25`).

**Scale.** FloatSim's committed studies are **model scale**; the device is
Froude-scaled at **λ = 50**. FloatFEA analyses at **full scale**, with FloatSim
re-run at full scale rather than model results scaled at the reader boundary —
Froude scaling is dimensionally inhomogeneous (a different exponent per
channel), so a wrong exponent is a silent factor-of-50 rather than an obviously
broken number. See `docs/milestones/F1.md` §3. Consequence: **no scale factor
appears anywhere in the schema or the numerics.**

## Machine-readable frame definitions

**`floatfea/io/frames.py` is the single source of truth.** The block below is
*generated* from it, and `tests/verification/rung3/test_conventions_are_generated.py`
fails if they diverge. **Edit the module, not this block.**

This inverts the direction G0.2 originally asked for. "Tested against" would
leave two hand-maintained artifacts held together by a comparison — which works
until someone edits one and updates the test to match, at which point the test
certifies the drift. "Generated from the document" would mean parsing prose,
where a formatting change silently alters a definition. With the data as source
and the prose as rendering, there is only one place a value can be stated, so
drift is impossible rather than merely detected.

Anything still UNRESOLVED below stays in prose and is deliberately absent from
the module: a machine-readable file carrying a placeholder would let the
validator check records against a value nobody had decided.

<!-- GENERATED FROM floatfea/io/frames.py -- DO NOT EDIT BY HAND -->

| quantity | value |
|---|---|
| Gravity | (0.0, 0.0, -9.81) m/s^2 (magnitude 9.81, FloatSim's value, **not** 9.80665) |
| Water density | 1025.0 kg/m^3 |
| Global origin | platform geometric centre |
| Vertical datum | still_water_level, z up, right-handed |
| Heading 0 | propagates along +x, direction of travel |
| Body frame origin | body_reference_point (**not** the CoG) |
| Moment reference | body_reference_point |
| Rotation direction | body_to_global |
| Bodies / DOF | 17 bodies, 102 DOF, 16 joints x 4 rows, **38 free** |
| Hydro DOF | 72 (12 buoys x 6; hubs and platform are structural) |

Rotation parameterisation **per producing module**:

| producer | parameterisation |
|---|---|
| `morison_drag` | `zyx_intrinsic_euler` |
| `plate_drag` | `zyx_intrinsic_euler` |
| `strips` | `zyx_intrinsic_euler` |
| `patches` | `zyx_intrinsic_euler` |
| `joints` | `rotation_vector` |
| `hydrostatic_restoring` | `linearised` |

<!-- END GENERATED -->

## Global frame

- **Origin:** platform geometric centre. `platform_common.py:51-58` places
  cluster centres on a circle about `(0, 0)`.
- **z axis:** up positive. Vertical datum is the **still-water level**, `z = 0`
  — the hull mesh is an "eqdraft" mesh with `z = 0` at the free surface
  (`cluster_common.py:19-21`) and submergence is measured as `z < 0`
  (`platform_common.py:72-78`).
- **Handedness:** right-handed.
- **Water depth:** 200 m at model scale (`platform_common.py:184`) — deep water
  relative to the wavelengths in use.
- **x axis — RESOLVED 2026-08-11.** `heading_deg = 0` means waves **propagate
  along +X**, and the angle is direction-of-travel, not direction-of-origin.
  Verified in source: `waves/regular.py:56-59` — "Propagation heading in degrees
  measured from the inertial `+X`" — and `hydro/excitation.py:50` — "travelling
  in +X for heading 0".
- **Capytaine agrees, and the cross-check is closed.** The BEM datasets carry
  `wave_direction = 0.0` rad, and `readers/capytaine.py:191-194` converts it
  straight through as `heading_deg = rad2deg(wave_direction)` with no sign flip
  and no offset. Both sides put heading 0 on +X, so the 180° mismatch that would
  have reversed every excitation force while leaving drag pointing the other way
  **is not present**. Checked before the panel-pressure export was built, where
  it would have been far more expensive to find.
- **FloatSim agreement:** same frame, no transformation.

## Body frames

- **Origin: the body `reference_point`, NOT the centre of gravity.** Set per
  body in the deck (`platform_common.py:137, 157, 176`). For the buoys
  `Z_BUOY_REF = -1.1956674`, while the CoG sits at `-1.0163` in the eqdraft
  frame (`cluster_common.py:33`). These are different points and must not be
  conflated.
- **Axis orientation:** parallel to global at rest.
- **Moments are taken about the body reference point**, not the CoG
  (`morison.py:397-405, 430-432`). Every exported moment channel inherits this.
- **FloatSim agreement:** same, no transformation.

### The inertia tensor's reference point, and a defect it exposes

The record declares the inertia tensor **about the body reference point, in the
body frame**, matching the deck schema (`deck.py:88`). **The CoG offset must
travel with it.** FloatSim has no field for that offset, so FloatFEA cannot
recover it from the record and must take it from the model definition or the
mesh.

This matters because the two points are *not* coincident on this platform, and
FloatSim assumes they are:

| | value | source |
|---|---|---|
| Body reference point | `Z_BUOY_REF = −1.1956674` m | `platform_common.py:101` |
| CoG, global | `−1.0163 − 0.21638 = −1.23268` m | `cluster_common.py:33`, `platform_common.py:48` |
| **Offset** | **+37.0 mm** (CoG below the reference point) | |

`driver.py:222` passes `cog_offset_body=None`, which `mass_properties.py:62`
defines as *CoG at the reference point*, and `driver.py:208-209` states plainly
that the deck has "no explicit CoG-offset field... Phase 2 may add an off-CoG
reference-point field." Meanwhile `cluster_common.py:34` comments the values as
"at single-buoy CoM" — so the numbers are stated about one point and consumed
about another.

Consequences, at model scale:

- Parallel-axis term `m·d²` omitted: **0.039 kg·m², 0.164%** of `I_xx`. Small.
- **Translation–rotation coupling block `m·d = 1.061 kg·m` omitted entirely** —
  a **4.05%** coupling ratio against `√(m·I)`. This one is structural, not a
  magnitude error: the 6×6 mass matrix is block-diagonal where it should not be.

**G3.1a will not catch this**, because FloatFEA would compute its own tensor
about its own reference point and be internally consistent. Both sides would be
consistently wrong. The record must therefore state the tensor's reference point
explicitly, and the validator must reject a record that omits it.

**Candidate mechanism for KD-2, offered as a hypothesis rather than a claim.**
KD-2-revised attributes a +20.54% FloatSim-vs-OpenFAST pitch-period gap to a
"combined-deck mass-aggregation discrepancy". A missing CoG offset removes
exactly the translation–rotation coupling that sets a pitch period. Whether the
magnitudes account for the gap is not established here and should be tested by
whoever owns KD-2 — but the two descriptions name the same class of defect, and
that is worth someone's hour.

## Rotations

**This section records a finding, not a convention already in force.**

`xi[3:6]` is the rotational part of each body's state. **FloatSim interprets it
three different ways in three different modules**, and all three agree only to
first order in θ:

| module | interpretation | source |
|---|---|---|
| `floatsim/hydro/morison.py` | **ZYX-intrinsic Euler** `(roll, pitch, yaw)` via `quaternion_from_euler_zyx` | `_body_pose_from_xi`, morison.py:609-627 |
| `floatsim/bodies/joints.py` | **rotation vector (axis-angle)** via `Rotation.from_rotvec` | `_body_pose`, joints.py:169-174 |
| `floatsim/hydro/hydrostatics.py` | **linearised rotation vector**, folded into `C` | hydrostatics.py:25 |

`ARCHITECTURE.md:93` declares ZYX-intrinsic for input/output; `ARCHITECTURE.md:44`
calls `ξ` only "(surge, sway, heave, roll, pitch, yaw)", which does not
distinguish the two.

This has never surfaced because FloatSim is linearised throughout — all three
reduce to `I + [θ×]` at small θ, below the model's own accuracy. **At the
rotations actually measured it does not.** Divergence between the two live
interpretations, as maximum element difference in `R` and as position error at
the 1.4574 m spar lever:

| ‖θ‖ rad | deg | rotvec vs ZYX-Euler | position error at spar tip |
|---|---|---|---|
| 0.0390 | 2.23 | 3.2e-4 | 0.39 mm (0.027%) |
| 0.1000 | 5.73 | 2.1e-3 | 2.47 mm (0.170%) |
| **0.15657** | **8.97** | **5.3e-3** | **5.84 mm (0.401%)** |
| 0.3000 | 17.19 | 2.0e-2 | 19.31 mm (1.325%) |

0.15657 rad is the measured steady-state maximum at the rotational mode
(`docs/milestones/F1.md` §9).

### Rules for FloatFEA

1. **Reconstruct each channel the way the module that produced it did.** Not
   "the right way" — the *same* way. A load and the pose used to place it must
   come from one interpretation, or the pairing is inconsistent at O(θ²) and the
   discrepancy lands in the G4.1 residual looking like a mapping bug.

   | channel | reconstruct as |
   |---|---|
   | strip and patch drag loads, and their application points | ZYX-intrinsic Euler |
   | joint reactions (`lam`) and joint kinematics | rotation vector (axis-angle) |
   | hydrostatic restoring `C` comparison (G4.6) | linearised, about ξ = 0 |

2. **The `.flr` schema declares the interpretation per channel group.** It is
   not global, because upstream it is not global. A record that fails to declare
   it is rejected.

3. **Never apply the linearised map `I + [θ×]` to transform a load.** It is not
   orthogonal and stretches every transformed vector by `√(1+θ²)` — 1.5% at 10°,
   4.3% at 17° — silently magnifying magnitudes. Use the exact reconstruction
   for whichever parameterisation the channel declares.

4. **Rodrigues applies only to the axis-angle channels.** Applied to the
   ZYX-Euler channels it produces a *different rotation*, not a more accurate
   one.

- **Direction:** `R` maps **body → global**, `v_global = R @ v_body`
  (`rigid_body.py:121-128`). Stated explicitly because the representation alone
  is ambiguous.
- **No quaternion channel exists upstream** and none is carried. FloatSim has no
  finite-rotation state; synthesising a quaternion would advertise a validity
  the source does not have.
- **Validity bound — UNRESOLVED.** `multibody-conventions.md` Item 2 gives
  `|θ| < 0.1 rad` for the *connector attachment transform*'s O(θ²) error at
  0.5%. The integrator's global small-angle treatment of `xi[3:6]` is a
  **separate claim with no stated bound anywhere in the record**, and the
  measured 0.15657 rad exceeds the connector figure by 1.6×. Q2 in
  `docs/milestones/F1.md` §10 scopes the experiment that would supply a bound.
  Until it does this is unknown — not "probably fine".

## Timestamps within a single RHS

FloatSim evaluates different force terms at different times inside the same
right-hand side:

- `state_force` from `(t[n], xi_n, xi_dot_n)` — `newmark.py:409`
- `external_force` at `t[n+1]` — `newmark.py:401`

**Each exported force channel is written at the index of the state it was
evaluated from** — `state_force` at `n`, `external_force` at `n+1` — and the
schema declares the alignment per channel. Pairing a force with the wrong index
gives an equilibrium residual of order `ωΔt`, which at full scale is **3.2%** —
the magnitude `PLAN.md` §8 names as quiet and wrong. Guarded by **G4.5**
(convergence *rate* under Δt refinement), not by a tolerance.

This trap bites twice: once on export, and again on any channel later added by
analogy to an existing one.

## Sign conventions

- **Gravity vector:** `(0, 0, -9.81)` — see Units.
- **Cummins restoring:** `C·ξ = −δM_total` (`hydrostatics.py:38-40`). `C` is a
  restoring *derivative*, not a load. Gravity and buoyancy cancel inside it at
  `ξ = 0`, so neither can be extracted; both are reconstructed independently in
  FloatFEA (G4.6).
- **Lagrange multipliers:** `lam` is the physical constraint force, dt-free
  (`newmark.py:132-137`), expressed against the constraint Jacobian rows in the
  joint's own basis — **not** a force/moment 6-vector. The joint geometry must
  travel with it or it cannot be interpreted.

The following are **FloatFEA's own**; FloatSim has no counterpart, carrying no
structural members:

- Positive axial force: **tension positive**.
- Positive bending moment, shear, torque: right-hand rule about the member local
  axes, defined below.

### Member local axes — DECIDED 2026-08-10

Nothing upstream constrains this, so it is FloatFEA's own choice, and it is
fixed now rather than carried open: it is upstream of every element sign
convention, and retrofitting it after the element formulations exist means
re-deriving every sign.

```
local x  =  unit(node_B - node_A)          member axis, A to B
local z  =  unit(r - (r . x) x)            r = the member's orientation reference
local y  =  z  x  x                        right-handed
```

**The orientation node is a first-class REQUIRED field in the model-definition
YAML, not an optional override.** All twelve spars are vertical, so the
global-Z default path is the *exception* in this model, not the rule. A field
that is optional in the schema but mandatory in practice invites members to be
written without it, and each one fails at build time for a reason the author has
to rediscover. Required-by-default inverts that: the common case is stated, and
the rare horizontal member may omit it.

**There is no implicit default for a vertical member, because the spars are
vertical and the usual default is degenerate there.** The reference `r` is
supplied as either:

- an **orientation node** — a third point; local z lies in the plane of
  (A, B, orientation node), on the side of that point; or
- a **roll angle** about local x, measured from the global-Z reference.

Where no explicit orientation is given, `r = global Z`. **The model builder
raises when that default is used on a member too close to vertical** — it does
not silently fall back to global X. A silent axis switch is precisely the kind
of convention change that produces sign errors nobody can trace, and it would
fire on the most important members in this model.

The near-vertical guard is a degeneracy threshold and therefore a tolerance: it
lives in `floatfea/tolerances.py` as `MEMBER_ORIENTATION_DEGENERACY`, not here
and not at the call site.

Rationale for the guard rather than a fallback: local y is built from
`Ẑ × x̂`, whose *direction* error amplifies any perturbation in the member axis
by `1/|Ẑ × x̂|`. The construction is exactly singular at vertical and
ill-conditioned near it. A tubular section is axisymmetric, so this does not
move the stress *magnitude* — but it does move which circumferential recovery
point is which, and member identifiers and recovery points are what envelope
reports and golden files key on. It also stops being benign the moment a
non-circular section is introduced.

## Numbering and identifiers

- **Body names** match FloatSim exactly: `buoy1`…`buoy12`, `hub1`…`hub4`,
  `platform`.
- **Deck body index**, which is what indexes `xi`: each cluster occupies four
  slots as `[3 buoys, 1 hub]`, so buoy `k` (0-based) is at `4c + b` for
  `c, b = divmod(k, 3)`, hub `c` at `4c + 3`, and `platform` at **16**
  (`platform_rao_pilot.py:116-120, 336-338`). DOF `j` of body `i` is `6i + j`.
- **17 bodies × 6 = 102 DOF**, less 16 `yaw_locked` joints × 4 constraint rows =
  64, leaving the **38 DOF** quoted in `PLAN.md` §1.
- **Node and element numbering:** FloatFEA's own, assigned by the model builder
  from the YAML definition. **Member identifiers must be stable across model
  regeneration**, because envelope reports and golden files key on them.
- **Orientation nodes must be stable across model regeneration, on exactly the
  same footing as member identifiers.** Member forces are reported in *local*
  axes, so moving an orientation node rotates every stored force for that member
  **with no code change anywhere**. Every golden file keyed to it then fails, and
  it fails looking like a solver regression — the diff shows moments moving with
  no commit that could have moved them. This is the same failure mode as an
  unstable member identifier and is pinned in the same place so the two are
  reviewed together.
- **Joint identifiers:** 16 joints — 12 buoy→hub, 4 hub→platform, all
  `yaw_locked` with 4 constraint rows each. `lam` is ordered by joint as
  constructed in the deck.

## Machine-readable copy

G0.2 requires the frame definitions above to exist in a form the interchange
validator checks records against.

**UNRESOLVED — to be created during F1**, alongside the reader. The requirement
is that it is **generated from, or tested against, this document**, not
hand-maintained beside it: two hand-maintained copies of the same convention
will diverge, and the divergence will be found by a wrong answer rather than by
a failing test. Intended home is `floatfea/io/`, with a test that fails if the
two disagree.

## Reconciliation summary

| item | FloatFEA | FloatSim | transformation |
|---|---|---|---|
| Units | SI | SI | none |
| Gravity | 9.81 | 9.81 | none — **adopted from FloatSim, not standard gravity** |
| Global frame | origin platform centre, z up, SWL datum | same | none |
| Body frame origin | body reference point | body reference point | none |
| Moment reference | body reference point | body reference point | none |
| Rotation representation | per channel (see Rotations) | **inconsistent across modules** | reconstruct per producing module |
| Force timestamp | per channel, declared | `state_force` at n, `external_force` at n+1 | align at export |
| Scale | full scale (λ = 50) | full scale after re-run | none — no scale factor in the numerics |
| Axial sign | tension positive | n/a | n/a |

**This table is not "checked, no differences".** The rotation row is a genuine
divergence *inside FloatSim*, and it is the most likely source of a silent
O(θ²) error in the load path at the rotations this platform actually reaches.
