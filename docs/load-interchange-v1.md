# FloatSim → FloatFEA Load Interchange, v1.0

**Schema version:** `1.0` — **LOCKED 2026-08-10**
**File extension:** `.flr` (FloatSim Load Record)
**Container:** HDF5, metadata as a JSON document in the root attribute `meta`.
**Audited against:** `docs/findings/G1.0-floatsim-output-audit.md`, HSP tag
`floatfea-ref-1`

Locked as **1.0, not 0.9**. The first end-to-end run will probably break
something, and the answer to that is a 1.1 — which is the versioning scheme
working as designed. Hedging the version to make the bump feel cheaper only
makes the change invisible, which is the same reflex as widening a tolerance to
avoid a red test.

---

## 1. What this schema reflects

v1.0 is written *after* the G1.0 audit, not before it. Four channel groups in
the pre-audit draft described quantities FloatSim does not compute. They are
gone, and recorded in §7 rather than deleted silently.

The central design decision stands: **decompose by physical origin, because each
source distributes onto the structure by a different rule.** What changed is
which sources can actually be separated.

| source | distributes as | available as |
|---|---|---|
| Excitation (FK + diffraction, **combined**) | surface pressure | per-panel field + body resultant |
| Radiation | surface pressure | per-panel field + body resultant |
| Morison drag | line load along the member | per-strip, 10 per spar |
| Plate drag | pressure over the disc face | per-patch, polar quadrature |
| Joint reactions | point load | `lam`, per constraint row |

## 2. Structure

```
/meta                       (root attribute, JSON)
  schema_version            "1.0"
  floatsim_version, hsp_git_sha (40-char, dirty flag), run_id, created_utc
  units                     {length: m, mass: kg, time: s, force: N, angle: rad}
  gravity                   [gx, gy, gz]     -- 9.81 from FloatSim, not 9.80665
  water_density, water_depth
  scale                     "full" | "model" -- declared, never a factor to apply
  assumptions[]             free-text records of any fallback applied

/frames
  global                    origin, axes, z-up flag, still-water-level datum
  bodies/<id>               origin relative to the body REFERENCE POINT

/bodies/<id>
  name, mass
  cog[3]                          body frame, relative to reference_point
  inertia[3,3]
  inertia_reference_point         REQUIRED: "reference_point" | "cog"
  reference_point[3]

/time
  t[N], dt, n_samples

/kinematics/<body>
  position[N,3], velocity[N,3], acceleration[N,3]
  rotation[N,3], angular_velocity[N,3], angular_acceleration[N,3]
  rotation_parameterisation       REQUIRED -- see sec.3

/loads/<body>/<source>            source in {excitation, radiation,
                                             morison_drag, plate_drag}
  force[N,3], moment[N,3]         the body resultant FloatSim APPLIED
  application_point[3] or [N,3]
  frame, rotation_parameterisation REQUIRED
  time_alignment                  REQUIRED: "state_n" | "external_n_plus_1"

/loads/<body>/radiation
  mu[N,6]                         REQUIRED -- the convolution term; see sec.5
  (A_inf . xi_ddot is reconstructed from the hydro database and /kinematics)

/panels/<body>/<source>           source in {excitation, radiation}
  centroid[P,3], area[P], normal[P,3]    panel geometry, body frame
  pressure[K,P]                          complex per omega where harmonic
  window_index[K]

/loads/strips/<member>/<source>
  s[M], node_a, node_b
  f_per_length[K,M,3]
  window_index[K], frame, rotation_parameterisation

/loads/patches/<body>/plate
  centroid[P,3], area[P]
  f_normal[K,P]                   per-patch normal force, BEFORE summation

/joints/<id>
  type                            "yaw_locked" | "hinge"
  bodies                          [body_a, body_b]
  attach_a[3], attach_b[3], axis[3]   in respective body frames
  n_rows                          constraint rows (yaw_locked = 4)
  lam[N,n_rows]                   multipliers, dt-free, physical
  jacobian_evaluation             REQUIRED: "step_midpoint"

/mooring/<line>                   OPTIONAL -- absent in the 12-buoy platform
  fairlead_body, fairlead_point[3], tension[N,3], frame

/diagnostics                      OPTIONAL -- FloatSim computes no per-step
                                  residual today (G1.0 sec.3)
```

## 3. Rotation parameterisation is a required field

**FloatSim holds three interpretations of `xi[3:6]`** — ZYX-intrinsic Euler in
`morison.py`, axis-angle in `joints.py`, linearised in `hydrostatics.py`
(`docs/conventions.md` § Rotations). They agree only to first order, and at the
measured ‖θ‖ = 0.15657 rad they differ by 0.4% on the spar lever.

So `rotation_parameterisation` is **REQUIRED on every kinematics and load
channel group**, with values `zyx_intrinsic_euler`, `rotation_vector`, or
`linearised`. Per-group, not global — because upstream it is not global.

A record carrying the loads but not the interpretation carries half the
information. **The validator rejects absence** (§9, G1.2).

The consumer rule is `docs/conventions.md`'s governing principle: **reconstruct
as produced, not as correct.**

## 4. Time alignment is a required field

`state_force` is evaluated at `(t[n], xi_n, xi_dot_n)` and applied to the
step-(n+1) RHS; `external_force` is evaluated at `t[n+1]`
(`newmark.py:401, 409`) — two timestamps inside one RHS.

Each channel is written at **the index of the state it was evaluated from** and
declares which via `time_alignment`. Misalignment gives a residual of order
`ωΔt` — 3.2% at full scale, the magnitude `PLAN.md` §8 names as quiet and wrong.
Guarded by **G4.5** on convergence *rate*, not by a tolerance.

## 5. `mu[N,6]` — new required channel

The radiation force applied is `A_inf·ξ̈ + μ(t)`. `A_inf` is in the hydro
database and `ξ̈` is exported, so the first term is reconstructible. **`μ(t)` is
not** — it is a loop local in `newmark.py` (created `:391`, updated `:449`,
consumed `:421`) and appears in no return value.

**G1.6 compares a reconstructed radiation panel field against the body-level
radiation force FloatSim actually applied.** Without `μ` that comparison cannot
be made, and G1.6 is unenforceable for the largest of the BEM-sourced loads.
This is the cheapest addition on the list: one array, already computed every
step.

### `mu` carries its own validation, built with the export

In steady periodic motion at ω the total radiation force is
`A(ω)·ξ̈ + B(ω)·ξ̇`, and the Cummins split is `A_inf·ξ̈ + μ(t)`. Equating gives
an identity the exported channel must satisfy at the fundamental:

```
mu  =  [A(w) - A_inf] . xi_ddot  +  B(w) . xi_dot
```

`A(ω)` and `B(ω)` are already in the hydro database, so this needs **no new
data**. It is the best available check on the newest and most error-prone
channel in the schema, and it is **independent of G1.6**: this tests the export
and the convolution implementation, G1.6 tests the panel reconstruction. A fault
in either would otherwise be attributed to the other.

**Written as a test alongside the exporter, not as a one-off script after it.**
A validation that runs once during development validates nothing thereafter.

## 6. Two-pass generation

**Pass one** writes body-level channels — kinematics, per-source resultants,
`mu`, joint `lam`. This is what screening consumes.

**Pass two** writes `/panels/`, `/loads/strips/` and `/loads/patches/` for a
short window around each selected snapshot. A window rather than a bare instant,
so a peak can be confirmed as physical rather than a numerical spike.

Because every case is currently a **regular wave integrated to steady state**,
panel pressures reconstruct from the frequency-domain BEM field at the case
frequency.

**For radiation this reconstruction is not an approximation — it is exact.** The
retardation kernel `K(t)` and the damping `B(ω)` are a Fourier pair (Ogilvie),
and the convolution is linear, so a purely harmonic `ξ̇` at ω produces a
radiation force at ω and nowhere else. No harmonics are generated. Fundamental-
only reconstruction of radiation in steady periodic motion is therefore
*identically* the frequency-domain result.

This inverts an assumption carried through earlier drafts. **Radiation is the
cleanest of the four sources, not the riskiest.** Any G1.6 residual on the
radiation channel is harmonic content injected by the *nonlinear* sources — drag
and the joint constraints — reaching radiation through the motion, and is
**purely diagnostic**. It is not evidence that the radiation reconstruction is
insufficient and must not be read as a trigger for per-panel convolution.

The 2ω/3ω escalation signal therefore applies to **excitation only**, where the
reconstruction genuinely is a fundamental-only approximation of a field driven
by a not-quite-sinusoidal motion.

Note that the storage pressure which originally motivated deterministic replay
does not yet exist — there are no irregular seas and no RNG in the solve path
(G1.0 §7). Replay determinism is retained as a test, not a gate.

A record may legitimately contain no strip or panel data — a screening-only
record. **The reader accepts it and the solver refuses to build load cases from
it**, rather than the reader accepting it silently and the solver inventing a
distribution.

## 7. Deliberately absent

**These are not oversights. Each is a locked decision, and re-adding one in a
future version would silently reverse it.**

| absent | why | locked at |
|---|---|---|
| `gravity` load channel | Computed in FloatFEA from the FE mass distribution — the one load source FloatFEA knows better than FloatSim, which carries a lumped placeholder. | F1 §3 |
| `hydrostatic` load channel | Gravity and buoyancy cancel inside `C` at ξ=0 upstream. `C` is a restoring *derivative*, not a load, so there is no pressure field in it to extract. Recomputed in FloatFEA from hull geometry, **on the MEAN wetted surface**, matching FloatSim's linearisation. | Q1, **G4.6** |
| `froude_krylov` / `diffraction` separately | BEM produces one combined `F_exc(ω)`; not separable at source. | G1.0 §3 |
| Structural properties (sections, materials, thicknesses) | FloatSim has none and never will. They live in the F3 model-definition YAML. | F1 §8 |
| `quaternion` kinematics channel | FloatSim has no finite-rotation state; synthesising one would advertise a validity the source lacks. | conventions |

**Anyone proposing to add one of these in v1.1 must first reopen the decision
that removed it.** Adding a `hydrostatic` pressure channel breaks G4.6's
mean-wetted-surface constraint; adding `gravity` reintroduces a lumped
placeholder in place of a computed distribution. Both would read as improvements
to someone who had not read this table — which is why the table exists.

## 8. Screening metrics (re-derived post-audit)

Fixed here because they constrain the channel set. Two changes from the
pre-audit list, both from the final channel walk:

| metric | status |
|---|---|
| Per-joint reaction force and moment | from `lam` + joint geometry |
| Per-cluster interface resultant | derived from hub→platform joint rows |
| **Platform-interface resultant** | **replaces "global base shear and overturning moment"** — a floating platform has no base; that framing was inherited from fixed jackets |
| Platform pitch and roll extremes | from `/kinematics` |
| Vertical acceleration per body | from `/kinematics` |
| ~~Mooring line tension~~ | **STRUCK — the 12-buoy platform has no mooring** (`connections = 0`) |
| Relative motion between adjacent buoys | from `/kinematics` |

Every retained metric is exported directly or derivable from exported channels.
A metric added later that is neither increments the schema version.

**None of the retained metrics depends on separable Froude-Krylov, diffraction,
or hydrostatic force** — checked explicitly, because a metric list that quietly
assumed them would put a requirement back into the schema that the audit
removed.

## 9. Validation rules

The reader **rejects** — never warns and continues. G1.2 tests that each
rejection fires with a specific message.

Carried from the pre-audit draft: unknown or future `schema_version`; missing or
partial `units`; a frame referenced but not declared; NaN or inf in any channel;
an inertia tensor that is not symmetric positive definite; a body referenced in
`/loads` or `/joints` but absent from `/bodies`; non-monotonic or non-uniform
`t` without an explicit flag; missing `hsp_git_sha` or `run_id`, since a record
without provenance is not analysable.

Added at v1.0:

- **Missing `rotation_parameterisation`** on any kinematics or load group (§3).
- **Missing `time_alignment`** on any load group (§4).
- **Missing `inertia_reference_point`** on any body — G3.1a cannot catch a wrong
  reference point, because both sides would be internally consistent and
  consistently wrong.
- **Missing `jacobian_evaluation`** on any joint carrying `lam`.
- **Rotation exceeding the declared validity bound**, once Q2 supplies one.
- Strip `window_index` that does not resolve into `/time`; strip stations `s`
  non-monotonic or not spanning the member.
- **Strips or panels that do not integrate back to the body resultant** for the
  same source and timestep — the numerical half of the old G1.4, promoted to
  **G1.6**, reported per body and per source with its spectral content.

## 10. Versioning

Semantic. A patch increment adds optional groups only. A minor increment adds
required groups, with the previous minor supported behind an explicit
compatibility flag. A major increment breaks the reader. **The reader never
guesses at an unknown version** — the failure is loud and immediate, because the
alternative is silently analysing a structure under misinterpreted loads.
