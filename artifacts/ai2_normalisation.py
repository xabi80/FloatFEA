"""AI2 -- reconcile FloatSim's 6.73x pitch excess against FloatFEA's 43.51x.

Two independent measurements of one quantity, 6.5x apart, both now in permanent
records. The suspicion is normalisation. This computes every reduction of the
SAME underlying quantity -- the removed endpoint dt*K(0)/2 against B -- so the
two can be matched to their definitions instead of argued about.

RAW OUTPUT ONLY.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_H/"studies"/"platform-12buoy")); sys.path.insert(0, str(_H/"studies"/"cluster-3buoy-rigid"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import platform_fin_fan as pff
from floatfea.io.frames import HYDRO_GLOBAL_DOF

hdb = pff._hdb("0215")
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); setup = pff._build(0.215, 5.0, hdb)
K = np.asarray(setup.kernel.K); tk = np.asarray(setup.kernel.t); dt = float(tk[1]-tk[0])
g = np.asarray(HYDRO_GLOBAL_DOF); K0 = K[np.ix_(g, g)][:, :, 0]
w = np.asarray(hdb.omega); B = np.asarray(hdb.B)
E = 0.5 * dt * K0                                   # the removed endpoint

pitch = [6*b + 4 for b in range(12)]
allx  = list(range(72))

def at(omega):
    k = int(np.clip(np.searchsorted(w, omega), 1, w.size-1))
    f = (omega - w[k-1])/(w[k]-w[k-1])
    return B[:,:,k-1]*(1-f) + B[:,:,k]*f

print(f"dt {dt}   endpoint = dt*K(0)/2")
print(f"{'omega':>7} {'whole-F':>9} {'pitchblk-F':>11} {'pitch-diag':>11} "
      f"{'pitch-diag(1)':>14} {'|B|_F':>10}")
for omega in (1.0, 1.5, 2.0004, 2.5, 3.0, 4.0):
    Bt = at(omega)
    whole = np.linalg.norm(E)/np.linalg.norm(Bt)
    pb    = np.linalg.norm(E[np.ix_(pitch,pitch)])/np.linalg.norm(Bt[np.ix_(pitch,pitch)])
    pdm   = float(np.mean([E[j,j]/Bt[j,j] for j in pitch]))
    pd1   = E[pitch[0],pitch[0]]/Bt[pitch[0],pitch[0]]
    print(f"{omega:7.4f} {whole:9.2f} {pb:11.2f} {pdm:11.2f} {pd1:14.2f} "
          f"{np.linalg.norm(Bt):10.3e}")

print("\nFloatFEA's published 43.51x is the MEAN PITCH DIAGONAL at w=2.0004.")
print("FloatSim's note for 9fb5b33 says '~7x ||B|| in Frobenius' -- a WHOLE-MATRIX")
print("reduction, which is a different definition, not a different result.")
Bt = at(2.0004)
print(f"\nat w=2.0004:  whole-matrix Frobenius {np.linalg.norm(E)/np.linalg.norm(Bt):.2f}x")
print(f"              mean pitch diagonal     {np.mean([E[j,j]/Bt[j,j] for j in pitch]):.2f}x")
print(f"              ratio between them      "
      f"{np.mean([E[j,j]/Bt[j,j] for j in pitch])/(np.linalg.norm(E)/np.linalg.norm(Bt)):.2f}x")
