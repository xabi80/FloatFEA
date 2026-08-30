"""AN3 -- re-run the mu-replay comparison against the CURRENT solver.

The '0 of 4806' figure predates 9fb5b33, which changed evaluate() from rectangular
to trapezoid. Both sides of the comparison call the same evaluate(), so the
structural argument says the result should still be 0 -- and that is an ARGUMENT.
This measures it.

Load-bearing because G1.6 CANNOT catch a broken export: both sides of that
comparison come from recompute_mu. This is the only check between the exported mu
and what the solver actually applied.

Runs on a throwaway instrumented branch. RAW OUTPUT ONLY.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
for sub in ("platform-12buoy", "cluster-3buoy-rigid"):
    sys.path.insert(0, str(_H/"studies"/sub))
warnings.simplefilter("ignore")

import platform_fin_fan as pff, platform_rao_pilot as prp
from floatsim.hydro.excitation import make_regular_wave_force
from floatsim.io.flr_export import recompute_mu
from floatsim.solver import newmark
from floatsim.solver.newmark import integrate_cummins
from floatsim.solver.ramp import HalfCosineRamp
from floatsim.waves.regular import RegularWave

assert hasattr(newmark, "_MU_TRACE"), (
    "newmark is NOT instrumented -- this must run on the throwaway branch, or the "
    "comparison is recompute_mu against itself and passes vacuously."
)

H, T, DT, RHO_INF, RAMP, DURATION = 0.04, 3.141, 0.01, 0.8, 20.0, 30.0
hdb = pff._hdb("0215"); prp._SPAR_CD = 1.2
setup = pff._build(0.215, 5.0, hdb)
deck = prp._deck_with_drag(); hydro_dof = prp._hydro_dof(deck)
wave = RegularWave(amplitude=0.5*H, omega=2.0*np.pi/T, heading_deg=0.0)
f72 = make_regular_wave_force(hdb=hdb, wave=wave, body_position=(0.0, 0.0, 0.0),
                              ramp=HalfCosineRamp(duration=RAMP))
n_dof = setup.lhs.n_dof

def ext(t):
    f = np.zeros(n_dof); f[hydro_dof] = f72(t); return f

res = integrate_cummins(lhs=setup.lhs, kernel=setup.kernel, xi0=setup.xi0,
                        xi_dot0=setup.xi_dot0, duration=DURATION, dt=DT,
                        rho_inf=RHO_INF, constraints=setup.constraints,
                        external_force=ext, state_force=setup.state_force,
                        projection_interval=1)

mu_solver = np.asarray(newmark._MU_TRACE)
mu_replay, valid_from = recompute_mu(setup.kernel, res.xi_dot, from_run_start=True)
print(f"samples {res.t.size}   n_dof {n_dof}   kernel lags {setup.kernel.K.shape[2]}")
print(f"solver trace {mu_solver.shape}   replay {mu_replay.shape}   valid_from {valid_from}")
assert mu_solver.shape == mu_replay.shape, "shape mismatch -- traces are not aligned"

diff = mu_replay != mu_solver
print(f"\n{diff.sum()} of {mu_solver.size} elements differ")
print(f"max |replay - solver| = {np.abs(mu_replay - mu_solver).max():.3e}")
print(f"max |mu|              = {np.abs(mu_solver).max():.6e}")

# A comparison of two all-zero arrays would also report 0 differing.
assert np.abs(mu_solver).max() > 0.0, "mu is identically zero -- nothing was compared"
print(f"\nnon-zero elements in the trace: {int((mu_solver != 0).sum())} "
      f"({(mu_solver != 0).mean()*100:.1f}%)")
print("PASS -- bit-identical" if diff.sum() == 0 else "FAIL -- replay has DIVERGED")
