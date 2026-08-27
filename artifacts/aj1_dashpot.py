"""AJ1 -- characterise the defect as a CONSTANT DASHPOT, not a magnitude error.

dt*K(0)/2 does not depend on omega. B(w) does, by orders of magnitude. So the
defect adds a frequency-INDEPENDENT damping on top of a frequency-DEPENDENT one,
and wherever the constant dominates, the model no longer has the property that
radiation damping varies with frequency.

Locates the crossover where the spurious term equals the physical one.
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
g = np.asarray(HYDRO_GLOBAL_DOF)
E = 0.5 * dt * K[np.ix_(g, g)][:, :, 0]
eF = np.linalg.norm(E)
w = np.asarray(hdb.omega); B = np.asarray(hdb.B)

W_OP = 2*np.pi/3.141
band = (w >= 0.5) & (w <= 8.0)
bF = np.array([np.linalg.norm(B[:,:,i]) for i in range(w.size)])

print(f"spurious term  ||dt*K(0)/2||_F = {eF:.4f}   CONSTANT at every omega")
print(f"physical term  ||B(w)||_F  ranges {bF[band].min():.4e} .. {bF[band].max():.4e}"
      f"   = {bF[band].max()/bF[band].min():.0f}x across 0.5 < w < 8\n")

def bnorm(omega):
    k = int(np.clip(np.searchsorted(w, omega), 1, w.size-1))
    f = (omega - w[k-1])/(w[k]-w[k-1])
    return np.linalg.norm(B[:,:,k-1]*(1-f) + B[:,:,k]*f)

lo, hi = 1.0, 8.0
for _ in range(80):
    mid = 0.5*(lo+hi)
    if bnorm(mid) < eF: lo = mid
    else: hi = mid
xover = 0.5*(lo+hi)
print(f"CROSSOVER (spurious == physical): w = {xover:.4f} rad/s   T = {2*np.pi/xover:.4f} s")
print(f"platform operating point:         w = {W_OP:.4f} rad/s   T = {2*np.pi/W_OP:.4f} s")
print(f"  -> operating point is {'INSIDE' if W_OP < xover else 'outside'} "
      f"the constant-dominated region, by {xover/W_OP:.2f}x in frequency\n")

print("effective damping the solver applied, against the physical B:")
print(f"{'omega':>7} {'T (s)':>7} {'|B(w)|_F':>11} {'|B+E|_F':>11} {'spurious frac':>14}")
for omega in (0.8, 1.2, 1.6, W_OP, 2.4, xover, 3.4, 4.5, 6.0):
    b = bnorm(omega)
    tag = "  <- operating" if abs(omega-W_OP) < 1e-6 else ("  <- crossover" if abs(omega-xover) < 1e-6 else "")
    print(f"{omega:7.4f} {2*np.pi/omega:7.3f} {b:11.4e} {b+eF:11.4e} "
          f"{eF/(b+eF)*100:13.1f}%{tag}")

print(f"\nacross the operating band w < {xover:.2f}, the applied damping is "
      f"{eF/(bnorm(1.0)+eF)*100:.0f}-{eF/(bnorm(xover)+eF)*100:.0f}% spurious")
print("=> a near-CONSTANT dashpot replaced a frequency-dependent B(w).")
