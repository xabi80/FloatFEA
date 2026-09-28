"""Generate the SMALL writer-produced .flr that V2's round-trip runs against.

Why a checked-in file rather than importing the writer in the test
-----------------------------------------------------------------
`CLAUDE.md`: the two codebases meet **only at a versioned interchange file**. A
FloatFEA test that imports `floatsim` would make that false, and would make
FloatFEA's suite unrunnable without HSP installed at a matching state.

So the boundary object IS the fixture. This script runs under HSP, the resulting
`.flr` is committed to FloatFEA, and the test validates and round-trips it. It is
a golden file and carries a golden file's obligation: **regenerating it requires a
written explanation of why the bytes moved** (`CLAUDE.md` § Testing).

Deliberately tiny -- 2 bodies, 24 samples, 8 kernel lags -- because the point is
the writer's OUTPUT FORMAT, not any physics. The physics records are elsewhere.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
from floatsim.hydro.retardation import RetardationKernel
from floatsim.io.flr_export import Provenance, write_solve_state
from floatsim.solver.newmark import IntegrationResult

OUT = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\FLOATFEA\tests\fixtures\writer_output.flr")
N, NB, DT, NLAG = 24, 2, 0.05, 8
ndof = 6 * NB
t = np.arange(N + 1) * DT
# Deterministic, non-trivial, and DIFFERENT per channel and per DOF, so a channel
# swapped for another is a round-trip failure rather than an invisible one.
j = np.arange(ndof)[None, :]
# Rotations must sit INSIDE the declared rotation_validity_bound below, or the
# validator rejects the fixture -- as it did on the first attempt, correctly.
# Translations are unbounded; rotations are scaled to ~0.06 rad.
_rot = (np.arange(ndof) % 6) >= 3
xi = np.sin(1.7 * t[:, None] + 0.31 * j) * (1.0 + 0.05 * j)
xi[:, _rot] *= 0.02
xi_dot = np.cos(2.3 * t[:, None] - 0.17 * j) * (2.0 + 0.03 * j)
xi_ddot = np.sin(3.1 * t[:, None] + 0.09 * j) * (3.0 - 0.02 * j)
lam = np.cos(1.1 * t[:, None] + 0.5 * np.arange(4)[None, :])

tk = np.arange(NLAG) * DT
K = np.zeros((ndof, ndof, NLAG))
for a in range(ndof):
    for b in range(ndof):
        K[a, b] = (1.0 / (1 + abs(a - b))) * np.exp(-tk) * np.cos(0.4 * tk + 0.1 * (a + b))

write_solve_state(
    OUT,
    result=IntegrationResult(t=t, xi=xi, xi_dot=xi_dot, xi_ddot=xi_ddot, lam=lam),
    kernel=RetardationKernel(K=K, t=tk, dt=DT),
    body_name_to_index={"bodyA": 0, "bodyB": 1},
    provenance=Provenance(hsp_git_sha="b" * 40, hsp_dirty=False,
                          floatsim_version="0.1.0", run_id="fixture-0001"),
    rho_inf=0.9, gravity=9.81, water_density=1025.0, water_depth=200.0,
    scale="model", from_run_start=True, rotation_validity_bound=0.1,
    time_convention="exp_minus_i_omega_t",
)
print(f"wrote {OUT}  {OUT.stat().st_size/1e3:.1f} kB")
np.savez(OUT.with_suffix(".expected.npz"), t=t, xi=xi, xi_dot=xi_dot,
         xi_ddot=xi_ddot, lam=lam, K=K, tk=tk)
print("wrote expected-values sidecar")
