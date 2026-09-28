"""Generate a real .flr record (DURABLE: writes into artifacts/, not a scratchpad): the first end-to-end exercise of the chain.

Runs the drift case (S3) with the FULL history retained -- run_case returns only
its final window, and the mu warm-up (I2) needs one kernel memory of real
history, so the exporter is driven from integrate_cummins directly.

RAW OUTPUT ONLY (docs/instrumentation.md). Ratios and residuals are derived in
the write-up.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np

_HSP = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_HSP / "studies" / "platform-12buoy"))
sys.path.insert(0, str(_HSP / "studies" / "cluster-3buoy-rigid"))

import platform_fin_fan as pff  # noqa: E402
import platform_rao_pilot as prp  # noqa: E402
from floatsim.hydro.excitation import make_regular_wave_force  # noqa: E402
from floatsim.io.flr_export import Provenance, write_solve_state  # noqa: E402
from floatsim.solver.newmark import integrate_cummins  # noqa: E402
from floatsim.solver.ramp import HalfCosineRamp  # noqa: E402
from floatsim.waves.regular import RegularWave  # noqa: E402

TAG, PLATE_R, CD_N = "0215", 0.215, 5.0
H, T, DT, RHO_INF = 0.04, 3.141, 0.01, 0.8      # rho_inf = 0.8, per run_case
RAMP, DURATION = 20.0, 120.0
# Q2 is open; 0.1 rad is the stated small-angle bound the record DECLARES.
# The run has measured max|theta| = 8.97 deg = 0.157 rad against it.
ROT_BOUND = 0.1
_HERE = Path(__file__).resolve().parent
OUT = _HERE / "platform_drift.flr"

hdb = pff._hdb(TAG)
prp._SPAR_CD = 1.2
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    setup = pff._build(PLATE_R, CD_N, hdb)
    deck = prp._deck_with_drag()
    hydro_dof = prp._hydro_dof(deck)

wave = RegularWave(amplitude=0.5 * H, omega=2.0 * np.pi / T, heading_deg=0.0)
f72 = make_regular_wave_force(
    hdb=hdb, wave=wave, body_position=(0.0, 0.0, 0.0), ramp=HalfCosineRamp(duration=RAMP)
)
n_dof = setup.lhs.n_dof


def ext(t: float) -> np.ndarray:
    f = np.zeros(n_dof, dtype=np.float64)
    f[hydro_dof] = f72(t)
    return f


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    res = integrate_cummins(
        lhs=setup.lhs, kernel=setup.kernel, xi0=setup.xi0, xi_dot0=setup.xi_dot0,
        duration=DURATION, dt=DT, rho_inf=RHO_INF, constraints=setup.constraints,
        external_force=ext, state_force=setup.state_force, projection_interval=1,
    )

print(f"samples                {res.t.size}")
print(f"duration               {res.t[-1]:.2f} s")
print(f"kernel lags            {setup.kernel.K.shape[2]}")
print(f"n_dof                  {n_dof}")
print(f"lam rows               {0 if res.lam is None else res.lam.shape[1]}")

np.savez_compressed(_HERE / "record_state.npz", t=res.t, xi=res.xi, xi_dot=res.xi_dot,
                    xi_ddot=res.xi_ddot, lam=res.lam)
print("wrote record_state.npz  -- BEFORE the .flr write, so the 20 min integration")
print("  is not at the mercy of a downstream signature change. The previous run")
print("  lost exactly this way: it completed, then threw on write_solve_state.")

write_solve_state(
    OUT,
    result=res,
    kernel=setup.kernel,
    body_name_to_index=setup.body_name_to_index,
    provenance=Provenance(
        hsp_git_sha="e" * 40, hsp_dirty=False, floatsim_version="0.1.0",
        run_id="platform-drift-0001",
    ),
    rho_inf=RHO_INF,
    gravity=9.81,
    water_density=1025.0,
    water_depth=200.0,
    scale="model",
    from_run_start=True,
    rotation_validity_bound=ROT_BOUND,
    time_convention="exp_minus_i_omega_t",
)
size_mb = OUT.stat().st_size / 1e6
print(f"wrote {OUT}          {size_mb:.2f} MB")

plat = prp._buoy_body_index_platform()
sx = res.xi[:, 6 * plat]
print(f"platform surge start   {sx[0]:+.6f} m")
print(f"platform surge end     {sx[-1]:+.6f} m")
print(f"max |theta| any body   "
      f"{max(np.linalg.norm(res.xi[:, 6*b+3:6*b+6], axis=1).max() for b in range(n_dof//6)):.6f} rad")
