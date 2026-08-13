# FloatSim → FloatFEA Load Interchange, v1.2

**Schema version:** `1.2` — **LOCKED 2026-08-11**
*(1.0 locked 2026-08-10. 1.1 split excitation into Froude-Krylov and diffraction,
§7.1. 1.2 adds the integrator block, §4.1 — both minor increments, both adding
required groups.)*
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
| **Froude-Krylov** | incident pressure on the wetted surface | per-panel field (v1.1) |
| **Diffraction** | scattered field | per-panel field (v1.1) |
| Excitation (their sum) | — | body resultant, as applied |
| Radiation | surface pressure | per-panel field + body resultant |
| Morison drag | line load along the member | per-strip, 10 per spar |
| Plate drag | pressure over the disc face | per-patch, polar quadrature |
| Joint reactions | point load | `lam`, per constraint row |

## 2. Structure

```
/meta                       (root attribute, JSON)
  schema_version            "1.2"
  floatsim_version, hsp_git_sha (40-char, dirty flag), run_id, created_utc
  units                     {length: m, mass: kg, time: s, force: N, angle: rad}
  gravity                   [gx, gy, gz]     -- 9.81 from FloatSim, not 9.80665
  water_density, water_depth
  scale                     "full" | "model" -- declared, never a factor to apply
  assumptions[]             free-text records of any fallback applied
  integrator                REQUIRED -- v1.2, see sec.4.1
    scheme                  "generalized_alpha"
    rho_inf, alpha_m, alpha_f, beta, gamma
    dt
    mu_treatment            "lagged_unblended"    -- see sec.4.1

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

/panels/<body>/<source>           source in {froude_krylov, diffraction,
                                             radiation}          -- v1.1
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

### 4.1 The integrator block — v1.2, and why blending is done reader-side

`time_alignment` (§4) is a two-value **index** enum. It cannot carry numeric
integrator parameters, so this is a **new required field and a version bump**,
not a clarification. Checked rather than assumed, and far cheaper now than after
the exporter exists.

**The problem §4 does not solve.** Generalized-alpha does not form its balance at
a timestep. It forms it at *alpha-weighted* states (`newmark.py:415-422`):

```
(1-alpha_m) M a_{n+1} + alpha_m M a_n
  + (1-alpha_f) C x_{n+1} + alpha_f C x_n
  + mu_n                                       <- LAGGED, NOT BLENDED
  = (1-alpha_f) F_{n+1} + alpha_f F_n
```

Aligning each force to the index of the state it was evaluated from is
necessary and **not sufficient**: the force the integrator actually applied over
a step is a two-term blend, and no single index represents it.

**Decision: export `F_n` per source, plus the blend parameters. Do NOT export the
blended `F_alpha`.**

- Blending **destroys the per-source decomposition G1.6 depends on** — a blended
  sum cannot be taken apart again.
- Blending *per source* stores exactly the information `F_n` already carries,
  with extra steps.
- Reader-side blending is a two-term weighted sum with **constant** weights.
  Nothing is lost, and the convention is **declared rather than baked in** —
  consistent with `rotation_parameterisation`, `time_alignment`,
  `inertia_reference_point` and `jacobian_evaluation`.

**Export `alpha_m` as well as `alpha_f`.** The inertia term blends with a
*different* parameter. At the default `rho_inf = 0.9`:

```
alpha_m = 0.42105     alpha_f = 0.47368     difference 0.05263
gamma   = 0.55263     beta    = 0.27701
```

Exporting only `alpha_f` would let FloatFEA form the right *force* blend against
the wrong *acceleration* blend, **and that residual would look exactly like an FE
mapping error** — the failure this schema exists to prevent. `beta`, `gamma` and
`rho_inf` cost nothing and make the record self-describing.

**`mu` is lagged, not blended.** The convolution enters as `mu_n` — the previous
step's value — not as `mu_{n+1-alpha_f}` (`newmark.py:391, 421, 459`; the
docstring at `:48` states the approximation). A reader that blended `mu` like the
other terms would introduce an error while trying to remove one, so
`mu_treatment` is declared explicitly.

### 4.1.1 The reader MUST branch on `mu_treatment`

**A uniform alpha blend across all terms silently reintroduces the floor §4.2
removes.**

The exact-discrete-equilibrium claim holds only if *every* term's declared
treatment is honoured, and `mu`'s differs from the rest: forces and stiffness
blend with `alpha_f`, inertia with `alpha_m`, and **`mu` is lagged and not
blended at all**. A reader that applied `alpha_f` uniformly — the natural
implementation, and the one a careless reading of §4.1 invites — would introduce
an error of the same order as the one it was correcting, while appearing to
implement the fix.

So `mu_treatment` is not documentation. It is a **branch condition**, and the
reader is required to dispatch on it rather than assume `"lagged_unblended"`.
A record declaring an unrecognised value is rejected, not defaulted.

### 4.2 What this buys: G4.1 loses its floor entirely

This is not damage limitation. Reconstructing the same blends means FloatFEA
reproduces the **exact discrete equilibrium** the integrator solved, rather than
approximating a continuous one. The balance then holds to **Newton tolerance**,
and whatever residual remains is genuinely **FloatFEA's load distribution onto
the FE mesh** — which is precisely what G4.1 was always meant to measure and,
until now, never could.

Both previously recorded floors are removed by construction, not budgeted for:
the `omega*dt` lag (§4) and the alpha-state misalignment (§4.1). **G4.1 finally
means what it says.**

*Do not merge the two scales when quoting this.* `alpha_f * omega * dt = 0.91%`
is an **instantaneous** misalignment, ~0.90 N on a 95 N swing. The 0.014 N figure
is a **mean** residual, 1.6% of that instantaneous scale — dimensionally
consistent with a second-order mean, which *supports* the alpha hypothesis but
does not prove it. Quoting them interchangeably would make an inference read as a
result.

### 4.3 Consequences elsewhere

**F5: a screened snapshot is an alpha-state, not a timestep.** Equilibrium holds
*between* n and n+1, so selecting a snapshot at index n defines a load case at an
instant where the balance does not hold. F5 must define the load case against the
alpha-state explicitly, or F4 and F5 refer to different instants and the mismatch
appears as an unexplained residual in whichever runs second.

**G4.5 is superseded for this term, not deleted.** A convergence-*rate* guard was
the right instrument while the best available treatment was an approximation. An
exact identity is stronger than any rate. G4.5 should be restated to cover what
remains — the `state_force` / `external_force` index alignment, where a
regression is still possible — rather than removed, since the two protections
answer different questions.

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

### 5.0 Reading a G1.6 failure — written before the first one

The panel field reaches FloatFEA through a **different extraction path** than
the body force DR2 validated, and carries its own phase convention along it. A
mismatch is therefore possible even though DR2 passed, and G1.6 catches it by
construction. Writing the diagnosis down now means the first failure is *read*
rather than investigated from scratch — and the spectral reporting G1.6 already
requires is what distinguishes the causes:

| signature | cause |
|---|---|
| Large residual, **coherent at the fundamental** | phase-convention error in the panel extraction |
| **Broadband**, or **spatially localised** on the hull | extraction error — geometry, panel ordering, normals |

The two demand opposite responses. A coherent fundamental residual means the
field is right and its *sign or phase* is wrong, which is a one-line fix in the
extraction and a convention to declare. A broadband or localised residual means
the field itself is wrong somewhere, and no convention change will help.

Note this is only diagnosable because G1.6 reports **spectral content per body
per source** rather than a single number. A scalar residual would show the same
magnitude for both causes.

### 5.0.1 Radiation reconstruction sums over ALL radiating DOF — 72, not 6

The database is a genuine 12-body coupled solve (G1.0 §4.3), so the radiation
pressure field on body *i* depends on the motion of **every** body.
**Reconstructing body *i*'s field from body *i*'s own motion alone silently drops
the interaction** — measured at 2.7% of own-body added mass at the rotational
mode.

G1.6 would catch it, since 2.7% sits comfortably above any sensible tolerance.
But catching it costs a debugging cycle that building it right does not, so it is
stated here as a requirement rather than left to be discovered.

**The count is 72, not 102.** The global state vector is 102 DOF (17 bodies), but
only the **12 buoys carry hydrodynamics** — the four hubs and the platform are
`structural=True` with no hydro database. `radiating_dof` and `influenced_dof`
each have exactly 72 entries, `buoy1__Surge … buoy12__Yaw`. An implementation
that summed over 102 would index past the end of the BEM data or, worse, pick up
structural DOF that have no radiation field at all. `_hydro_dof(deck)` is the map
between the two.

### 5.0.2 Storage: export complex coefficients, reconstruct on read

Sized before writing, because the windowing that made strip export cheap does
**not** carry over — strips are ~20 per member, panels are three orders more.
Measured counts: **1488** panels per hull, **17,856** for the 12-hull platform
mesh; 72 radiating DOF; 81 frequencies in the swept database, 13 in the reduced
grid the platform runs use.

At 40 snapshots × a 101-sample window = 4040 samples:

| option | arithmetic | volume |
|---|---|---|
| Time-domain, 3 fields, full platform mesh | 17,856 × 4040 × 8 B × 3 | **1.73 GB** |
| Time-domain, single hull reused | 1488 × 4040 × 8 B × 3 | 0.14 GB |
| **Complex coefficients**, FK + diffraction, 13 ω | 17,856 × 13 × 16 B × 2 | 7 MB |
| **Complex coefficients**, radiation, 13 ω × 72 DOF | 17,856 × 72 × 13 × 16 B | 267 MB |
| **Coefficient total at the case frequencies** | ~11 distinct ω in the fan | **~232 MB** |

**Decision: store the complex field plus the motion, and reconstruct on read.**

- **It loses nothing.** `K(t)` and `B(ω)` are a Fourier pair and the convolution
  is linear, so in steady periodic motion the reconstruction is *exact at the
  fundamental*, not approximate (§6). Storing coefficients rather than samples
  discards no information the time-domain export would have carried.
- **It collapses the volume by the window length** — 4040 samples become ~11
  frequencies — for a net **~7× reduction**, 1.73 GB to ~232 MB.
- **The motion is already exported.** `/kinematics/` carries what the
  reconstruction needs, so the coefficient form adds no second data source that
  could disagree with the first.
- Radiation dominates the remainder because of its 72-DOF dimension. If that
  becomes binding, the lever is the number of distinct case frequencies, not the
  window — which is the opposite of where one would look by default, and the
  reason for recording the arithmetic rather than the conclusion.

The alternatives, rejected: narrower windows and fewer panel-carrying snapshots
both trade away screening coverage to solve a problem that the coefficient form
removes outright.

### 5.1 Panel-field validity — required of module 3, decided before it is written

The BEM computes the panel field for a hull **at its reference position**, and
linear theory assumes small motion about that position. The platform translates
**~2.3 spar diameters** over a run, so the field becomes progressively less
applicable to where the hull actually is.

This is the same validity-window logic as the `mu` warm-up (§5) and the
stored-window rule, in its third application — see
`docs/instrumentation.md` § "The general pattern".

Required in `/panels/`:

```
/panels/<body>/<source>
  reference_pose[7]         REQUIRED -- position + rotation the BEM assumed
  body_pose[K,7]            REQUIRED -- actual pose at every exported instant
  validity_bound            REQUIRED -- max admissible displacement from
                                        reference, WITH its basis stated here
```

The validator **rejects or flags** any screened snapshot whose displacement from
the reference exceeds `validity_bound`. The bound and its justification live in
this schema, not in a code comment — a threshold whose reasoning is a comment is
a number nobody can re-check.

### 5.2 Module 3 carry-forward, so nothing is lost

- **FK and diffraction are exported separately** (§7.1, v1.1).
- **The G1.6 gate is on their SUM** against FloatSim's combined applied
  excitation. The per-field comparison against Capytaine's own resultants is a
  **different check** — panel extraction, not simulation agreement — and is
  labelled as such (§7.2).
- **The panel → FE mapping is G4.4, in F4, not this module's job.** Module 3
  exports the field; F4 maps it. Keeping that boundary clean is what makes G1.6
  and G4.4 independent failure modes rather than one blurred one.

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
*(The v1.0 entry merging Froude-Krylov and diffraction has been **struck** — its
justification was factually wrong. See §7.1.)*

### 7.1 Froude-Krylov and diffraction are split — v1.1

The v1.0 justification, "BEM produces one combined `F_exc(ω)`; not separable at
source", **was false.** Capytaine's datasets carry `Froude_Krylov_force` **and**
`diffraction_force` as separate variables alongside `excitation_force`. They are
separable at source; only FloatSim's *reader* merges them.

Split, for four reasons:

1. **Free at source** — no new computation, no new BEM run.
2. **Physically distinct distributions.** FK is the incident-wave pressure on the
   wetted surface; diffraction is the scattered field. They do not distribute
   alike, and the whole premise of §1 is that sources distributing differently
   must arrive separately.
3. **Retrofitting costs a re-run**, and the panel-pressure module is about to be
   written.
4. **It future-proofs the decision most likely to be revisited.** If G4.6's
   mean-wetted-surface constraint is ever reopened, **FK is the term that would
   move to the instantaneous surface** — it is the incident pressure, defined
   wherever the hull actually is — while diffraction stays on the mean. Merged,
   that change would be impossible without a schema break.

`/loads/<body>/excitation` is **retained** as the combined body resultant, because
that is what FloatSim actually applied. The split lives in `/panels/`.

### 7.2 Two guards, two purposes — do not conflate them

**(a) The G1.6 gate.** The **sum** of the two panel fields, integrated over the
hull, against **FloatSim's combined applied excitation**.

> This must **not** be satisfiable by checking the halves separately.
> **FloatSim never applied the halves to anything** — it applied their sum, and
> only the sum has a counterpart in the simulation.

**(b) A panel-extraction check.** Each field against **Capytaine's own** FK and
diffraction resultants. Useful, and it is what catches an error in the pressure
extraction itself.

But (b) tests *agreement with Capytaine*, not *agreement with the simulation*.
Conflating them would let a panel extraction that matches Capytaine perfectly
pass while disagreeing with what the simulator actually applied — which is
precisely the failure G1.6 exists to catch. Only (a) is the gate; (b) is a
diagnostic and is labelled as one.
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
- **A case screened inside the `mu` warm-up region.** Records carry
  `mu_valid_from`; `mu` before that index saw a zero-padded convolution buffer
  the solver did not, and is **invalid rather than approximate**. A record whose
  entire history lies inside the warm-up is rejected outright.
- **An unrecognised `mu_treatment`** — the reader branches on it (§4.1.1) and
  must not default.
- **Missing or incomplete `/meta/integrator`** — all of `alpha_m`, `alpha_f`,
  `beta`, `gamma`, `dt` and `mu_treatment` (§4.1). A partial block is rejected:
  a reader with `alpha_f` but not `alpha_m` would silently blend the inertia term
  wrongly.
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
