"""AD1: is the A-term really 90 deg from the B-term?  AD3: broadband reconstruction."""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_H/"studies"/"platform-12buoy")); sys.path.insert(0, str(_H/"studies"/"cluster-3buoy-rigid"))
import platform_fin_fan as pff, platform_rao_pilot as prp
from floatsim.io.flr_export import recompute_mu
T_f=3.141; W=2*np.pi/T_f
d=np.load(Path(__file__).resolve().parent / "record_state.npz",allow_pickle=True); t,xid,xidd=d["t"],d["xi_dot"],d["xi_ddot"]
hdb=pff._hdb("0215"); prp._SPAR_CD=1.2
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); setup=pff._build(0.215,5.0,hdb)
w=np.asarray(hdb.omega); A=np.asarray(hdb.A); B=np.asarray(hdb.B); Ainf=np.asarray(hdb.A_inf)
lo=int(np.searchsorted(w,W)-1); hi=lo+1; f=(W-w[lo])/(w[hi]-w[lo])
Ai=A[:,:,lo]*(1-f)+A[:,:,hi]*f; Bi=B[:,:,lo]*(1-f)+B[:,:,hi]*f
mu,_=recompute_mu(setup.kernel,xid,from_run_start=True)
hy=prp._hydro_dof(prp._deck_with_drag()); sel=t>t[-1]-8*T_f
a=xidd[np.ix_(sel,hy)]; v=xid[np.ix_(sel,hy)]; R=mu[np.ix_(sel,hy)]
At=a@(Ai-Ainf).T; Bt=v@Bi.T
tt=t[sel]-t[sel][0]; M=np.column_stack([np.cos(W*tt),np.sin(W*tt)])
def ph(x):
    c,*_=np.linalg.lstsq(M,x-x.mean(),rcond=None); return complex(c[0],-c[1])
print("AD1 -- phase between the A-sum and the B-sum (90 deg is the bridge's premise)")
print(f"{'DOF':>4} {'|A-term|':>12} {'|B-term|':>12} {'arg(A)-arg(B) deg':>19}")
rows=[]
for j in range(72):
    Aj,Bj=ph(At[:,j]),ph(Bt[:,j])
    if abs(Aj)<1e-9 or abs(Bj)<1e-12: continue
    rows.append((abs(Aj),abs(Bj),np.degrees(np.angle(Aj/Bj)),j))
rows.sort(reverse=True)
for m,b,p,j in rows[:6]: print(f"{j:4d} {m:12.4e} {b:12.4e} {p:19.1f}")
ang=np.array([r[2] for r in rows])
print(f"  spread: min {ang.min():+.1f}  max {ang.max():+.1f}  "
      f"fraction within 10 deg of +/-90: {np.mean(np.abs(np.abs(ang)-90)<10):.2f}")
print("  -> if these are not ~90 deg, 'purely quadrature => error is in B' is INVALID\n")

print("AD3 -- broadband: apply A(w), B(w) frequency-by-frequency, not pointwise at w")
dt=float(t[1]-t[0]); n=v.shape[0]
fr=np.fft.rfftfreq(n,d=dt)*2*np.pi
V=np.fft.rfft(v,axis=0); Acc=np.fft.rfft(a,axis=0)
pred=np.zeros_like(V)
inb=(fr>=w[0])&(fr<=w[-1])
for i in np.where(inb)[0]:
    k=np.searchsorted(w,fr[i]); k=min(max(k,1),len(w)-1)
    g=(fr[i]-w[k-1])/(w[k]-w[k-1])
    Aw=A[:,:,k-1]*(1-g)+A[:,:,k]*g; Bw=B[:,:,k-1]*(1-g)+B[:,:,k]*g
    pred[i]=(Aw-Ainf)@Acc[i]+Bw@V[i]
Tb=np.fft.irfft(pred,n=n,axis=0)
Tp=At+Bt
def wnorm(X,Y):
    num=[];den=[]
    for j in range(72):
        Tj=ph(Y[:,j]); Rj=ph(X[:,j])
        if abs(Tj)<1e-9: continue
        num.append(abs(Tj)*abs(Rj-Tj)/abs(Tj)); den.append(abs(Tj))
    return sum(num)/sum(den)

def report(name,X,Y):
    """X3: a residual is a DIFFERENCE. |R-T|/|T| alone cannot tell a missing
    term from a phase rotation from a gain error. Report all three."""
    nu=de=0.0; rat=[]; pha=[]; wt=[]
    for j in range(72):
        Tj=ph(Y[:,j]); Rj=ph(X[:,j])
        if abs(Tj)<1e-9: continue
        nu+=abs(Tj)*abs(Rj-Tj)/abs(Tj); de+=abs(Tj)
        rat.append(abs(Rj)/abs(Tj)); pha.append(np.degrees(np.angle(Rj/Tj))); wt.append(abs(Tj))
    rat=np.array(rat); pha=np.array(pha); wt=np.array(wt)
    print(f"  {name:34s} |R-T|/|T| = {nu/de:7.4f}   "
          f"|R|/|T| = {np.sum(wt*rat)/np.sum(wt):6.4f}   "
          f"arg(R/T) = {np.sum(wt*pha)/np.sum(wt):+7.2f} deg")
    return nu/de

def tnorm(name,X,Y):
    """TIME DOMAIN, magnitude-weighted per DOF -- this is how the original 0.209
    was formed. The phasor version below projects onto the fundamental and would
    HIDE the very broadband content AD3 is testing for, so it cannot be the
    primary statistic here."""
    wt=np.linalg.norm(Y,axis=0)
    ok=wt>1e-9
    r=np.linalg.norm(X-Y,axis=0)[ok]/wt[ok]
    g=np.linalg.norm(X,axis=0)[ok]/wt[ok]
    print(f"  {name:34s} |R-T|/|T| = {np.sum(wt[ok]*r)/np.sum(wt[ok]):7.4f}   "
          f"|R|/|T| = {np.sum(wt[ok]*g)/np.sum(wt[ok]):6.4f}")
    return np.sum(wt[ok]*r)/np.sum(wt[ok])

print("  -- time domain (primary; matches how 0.209 was formed) --")
tp=tnorm("pointwise, single frequency",R,Tp)
tb=tnorm("broadband, frequency-by-frequency",R,Tb)
print(f"  collapse factor {tp/tb:.2f}x\n" if tb > 0 else "")
print("  -- phasor at the fundamental (secondary) --")
rp=report("pointwise, single frequency",R,Tp)
rb=report("broadband, frequency-by-frequency",R,Tb)
print(f"  collapse factor: {rp/rb:.2f}x" if rb > 0 else "")
print("  -> if the broadband residual collapses, the 0.209 was a single-frequency")
print("     harness applied to a broadband convolution, not a defect in anything.")
