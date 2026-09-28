"""X3 pays off: the residual is dominantly a PHASE LAG, not a missing term.

arg(R/T) = -11.07 deg and |R|/|T| = 1.0224. Test directly whether a pure time
shift of the tabulated prediction collapses the residual -- and if so, what dt
that shift corresponds to in the integrator's own units.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_H/"studies"/"platform-12buoy")); sys.path.insert(0, str(_H/"studies"/"cluster-3buoy-rigid"))
import platform_fin_fan as pff, platform_rao_pilot as prp
from floatsim.io.flr_export import recompute_mu
T_f=3.141; W=2*np.pi/T_f
d=np.load(Path(__file__).resolve().parent/"record_state.npz",allow_pickle=True)
t,xid,xidd=d["t"],d["xi_dot"],d["xi_ddot"]
hdb=pff._hdb("0215"); prp._SPAR_CD=1.2
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); setup=pff._build(0.215,5.0,hdb)
w=np.asarray(hdb.omega); A=np.asarray(hdb.A); B=np.asarray(hdb.B); Ainf=np.asarray(hdb.A_inf)
k=int(np.clip(np.searchsorted(w,W),1,w.size-1)); f=(W-w[k-1])/(w[k]-w[k-1])
Ai=A[:,:,k-1]*(1-f)+A[:,:,k]*f; Bi=B[:,:,k-1]*(1-f)+B[:,:,k]*f
mu,_=recompute_mu(setup.kernel,xid,from_run_start=True)
hy=prp._hydro_dof(prp._deck_with_drag()); sel=t>t[-1]-8*T_f
a=xidd[np.ix_(sel,hy)]; v=xid[np.ix_(sel,hy)]; R=mu[np.ix_(sel,hy)]
tt=t[sel]-t[sel][0]; M=np.column_stack([np.cos(W*tt),np.sin(W*tt)])
def ph(x):
    c,*_=np.linalg.lstsq(M,x-x.mean(),rcond=None); return complex(c[0],-c[1])
def stats(X,Y):
    wt=np.array([abs(ph(Y[:,j])) for j in range(72)]); ok=wt>1e-9
    r=np.array([abs(ph(X[:,j])-ph(Y[:,j]))/abs(ph(Y[:,j])) for j in range(72)])[ok]
    g=np.array([abs(ph(X[:,j]))/abs(ph(Y[:,j])) for j in range(72)])[ok]
    p=np.array([np.degrees(np.angle(ph(X[:,j])/ph(Y[:,j]))) for j in range(72)])[ok]
    W_=wt[ok]; return (np.sum(W_*r)/W_.sum(), np.sum(W_*g)/W_.sum(), np.sum(W_*p)/W_.sum())

T0=a@(Ai-Ainf).T + v@Bi.T
r0,g0,p0=stats(R,T0)
print(f"baseline               |R-T|/|T| {r0:.4f}   |R|/|T| {g0:.4f}   arg {p0:+.2f} deg")
print(f"pure-rotation model    a rotation of {p0:+.2f} deg alone gives "
      f"{abs(np.exp(1j*np.radians(p0))-1):.4f}")
print(f"rotation + gain model  {abs(g0*np.exp(1j*np.radians(p0))-1):.4f}   "
      f"-> explains {abs(g0*np.exp(1j*np.radians(p0))-1)/r0*100:.0f}% of the residual\n")

dt=float(t[1]-t[0])
print(f"the lag as a time shift  {np.radians(abs(p0))/W:.5f} s = {np.radians(abs(p0))/W/dt:.2f} dt   (dt={dt})")
rho=0.8; af=rho/(1+rho); am=(2*rho-1)/(rho+1)
for name,shift in [("one step (mu lagged_unblended)",dt),("alpha_f*dt",af*dt),
                   ("alpha_m*dt",am*dt),("dt/2 (left-endpoint quadrature)",dt/2)]:
    print(f"  {name:34s} {shift:.5f} s = {np.degrees(shift*W):.2f} deg")

# Is the -11.07 deg a COHERENT lag shared by every DOF, or per-DOF scatter that
# happens to average to -11? Fit ONE global complex factor to all 72 phasors at
# once -- that is exactly a time shift plus a gain -- and see what is left.
Rp=np.array([ph(R[:,j]) for j in range(72)])
Tp=np.array([ph(T0[:,j]) for j in range(72)])
ok=np.abs(Tp)>1e-9
Rp,Tp=Rp[ok],Tp[ok]
c=np.vdot(Tp,Rp)/np.vdot(Tp,Tp)
base=np.linalg.norm(Rp-Tp)/np.linalg.norm(Tp)
res=np.linalg.norm(Rp-c*Tp)/np.linalg.norm(Tp)
print(f"\nsingle global factor   c = {abs(c):.4f} * exp({np.degrees(np.angle(c)):+.2f} deg)")
print(f"                       equivalent time shift {np.angle(c)/W:+.5f} s "
      f"= {np.angle(c)/W/dt:+.2f} dt")
print(f"residual, unweighted   {base:.4f}  ->  {res:.4f} after removing it")
print(f"collapse               {base/res:.2f}x")
d_=np.degrees(np.angle(Rp/Tp))
print(f"per-DOF phase spread   min {d_.min():+.2f}  max {d_.max():+.2f}  std {d_.std():.2f} deg")
