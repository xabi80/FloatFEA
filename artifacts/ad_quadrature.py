"""The lag is the solver's own quadrature, measured with the solver's weights.

RadiationConvolution.evaluate() is a PLAIN RECTANGULAR sum:

    mu = dt * sum_k K[k] @ buffer[k]        weight dt on EVERY lag, k=0 included

AD2 used trapezoid, which weights the endpoints dt/2. The difference is
dt*K[0]/2, and K(0) is the LARGEST value in the kernel -- a purely real, positive
addition to the effective transfer function

    H(w) = B_eff(w) + i*w*[A_eff(w) - A_inf]

Adding to the REAL part while the imaginary part dominates rotates the phasor
toward the real axis (negative arg) and slightly increases its magnitude. Both
match the measured signs: arg(R/T) = -11.07 deg, |R|/|T| = 1.0223.

Measured here with the solver's exact weights. RAW OUTPUT ONLY.
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

W = 2*np.pi/3.141
hdb = pff._hdb("0215")
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); setup = pff._build(0.215, 5.0, hdb)
K = np.asarray(setup.kernel.K); tk = np.asarray(setup.kernel.t); dt = float(tk[1]-tk[0])
g = np.asarray(HYDRO_GLOBAL_DOF); Kh = K[np.ix_(g, g)]
w = np.asarray(hdb.omega); A = np.asarray(hdb.A); B = np.asarray(hdb.B); Ainf = np.asarray(hdb.A_inf)
k = int(np.clip(np.searchsorted(w, W), 1, w.size-1)); f = (W-w[k-1])/(w[k]-w[k-1])
At = A[:,:,k-1]*(1-f)+A[:,:,k]*f; Bt = B[:,:,k-1]*(1-f)+B[:,:,k]*f

e = np.exp(-1j*W*tk)
H_rect = dt*np.einsum("ijk,k->ij", Kh, e)                  # the solver's own sum
H_trap = np.trapezoid(Kh*e, tk, axis=2)                    # what AD2 used
H_tab  = Bt + 1j*W*(At-Ainf)                               # the tabulated target

print(f"dt {dt}   lags {tk.size}   omega {W:.4f}")
print(f"||K[0]||_F                 {np.linalg.norm(Kh[:,:,0]):12.4e}   <- largest lag")
print(f"dt*K[0]/2, the difference  {np.linalg.norm(dt*Kh[:,:,0]/2):12.4e}")
print(f"||B_tab||_F                {np.linalg.norm(Bt):12.4e}")
print(f"  -> the endpoint term is {np.linalg.norm(dt*Kh[:,:,0]/2)/np.linalg.norm(Bt):.2f}x the whole of B\n")

def cmp(name, H):
    r = np.array([abs(H[j,j])/abs(H_tab[j,j]) for j in range(72)])
    p = np.array([np.degrees(np.angle(H[j,j]/H_tab[j,j])) for j in range(72)])
    wt = np.abs(np.diag(H_tab))
    print(f"{name:28s} |H|/|H_tab| {np.sum(wt*r)/wt.sum():7.4f}   "
          f"arg {np.sum(wt*p)/wt.sum():+7.2f} deg   "
          f"||H-H_tab||_F/||H_tab||_F {np.linalg.norm(H-H_tab)/np.linalg.norm(H_tab):7.4f}")

print("effective transfer function against the tabulated coefficients:")
cmp("trapezoid (AD2's weights)", H_trap)
cmp("RECTANGULAR (the solver's)", H_rect)
print()
print(f"measured on the record:      |R|/|T| 1.0223   arg -11.07 deg   |R-T|/|T| 0.2085")
