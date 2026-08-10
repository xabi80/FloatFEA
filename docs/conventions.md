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
- **x axis — UNRESOLVED.** Wave heading is passed as `heading_deg=0.0`
  (`platform_rao_pilot.py:262`) and the platform is four-fold symmetric, so no
  committed result distinguishes the heading-zero direction. Whether 0°
  propagates along `+x`, and whether the angle is direction-of-travel or
  direction-of-origin, must be read out of `floatsim/waves/regular.py` and
  `make_regular_wave_force` before any directional load case is built. It does
  not affect the symmetric cases run so far — which is exactly why it has never
  been forced to declare itself.
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
  axes.
- **UNRESOLVED:** the local-axis triad (which reference vector orients local *y*
  for a vertical member) is not yet fixed. It must be settled in F2 before any
  member force is reported, because envelope reports and golden files key on the
  sign.

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
