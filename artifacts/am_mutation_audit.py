"""AM1-AM3 -- answer question (b) by MUTATION, not by re-reading.

Question (b) -- "does this evidence test what the row claims?" -- was answered by
me reading my own rows, which is the weakest form of the check: a reviewer
re-forms the judgement the author already formed. A mutation is a measurement.

Each mutation is derived from the ROW'S CLAIM TEXT, never from the test (AM2).
Break exactly what the row asserts; the gate must go RED. Needing to read the test
to invent the mutation is itself the tell that row and test have drifted.

Mutations are applied in-tree and reverted with `git checkout --` immediately.
Run only on a clean working tree.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

FEA = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\FLOATFEA")
HSP = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
PY = HSP / ".venv" / "Scripts" / "python.exe"


def _run(repo: Path, args: list[str]) -> tuple[int, str]:
    p = subprocess.run([str(PY), "-m", "pytest", *args, "-q", "--no-header", "-x"],
                       cwd=repo, capture_output=True, text=True, timeout=1800)
    return p.returncode, (p.stdout + p.stderr)[-400:]


def _restore(repo: Path, rel: str) -> None:
    subprocess.run(["git", "checkout", "--", rel], cwd=repo, check=True)


def _edit(path: Path, old: str, new: str) -> None:
    s = path.read_text(encoding="utf-8")
    if old not in s:
        raise SystemExit(f"anchor not found in {path.name}: {old[:60]!r}")
    path.write_text(s.replace(old, new, 1), encoding="utf-8")


def mutate_g10():
    """Row: cites docs/findings/G1.0-floatsim-output-audit.md as the finding."""
    f = FEA / "docs/findings/G1.0-floatsim-output-audit.md"
    body = f.read_text(encoding="utf-8")
    f.unlink()
    try:
        return _run(FEA, ["tests/verification/rung3/test_closure_evidence_exists.py"])
    finally:
        f.write_text(body, encoding="utf-8")


def mutate_g11():
    """Row: round-trip BIT-EXACT against a writer-produced fixture."""
    import h5py
    fx = FEA / "tests/fixtures/writer_output.flr"
    raw = fx.read_bytes()
    with h5py.File(fx, "r+") as h:
        d = h["kinematics/bodyA/position"]
        v = d[...]
        v[3, 1] += 1e-12          # one value, one ulp-ish: bit-exact must catch it
        d[...] = v
    try:
        return _run(FEA, ["tests/verification/rung4/test_writer_round_trip.py"])
    finally:
        fx.write_bytes(raw)


def mutate_g12():
    """Row: rejects each fault with a SPECIFIC message."""
    r = FEA / "floatfea/io/reader.py"
    _edit(r, 'MU_WARMUP = "record lies inside the mu warm-up region"',
          'MU_WARMUP = "missing hsp_git_sha or run_id"')   # collide with PROVENANCE
    try:
        return _run(FEA, ["tests/verification/rung4/test_validator_matrix.py"])
    finally:
        _restore(FEA, "floatfea/io/reader.py")


def mutate_g13():
    """Row: a record without hsp_git_sha OR run_id is rejected."""
    r = FEA / "floatfea/io/reader.py"
    _edit(r, 'if not meta.get("hsp_git_sha") or not meta.get("run_id"):',
          'if not meta.get("run_id"):')                     # drop the sha half
    try:
        return _run(FEA, ["tests/verification/rung4/test_validator_matrix.py"])
    finally:
        _restore(FEA, "floatfea/io/reader.py")


def mutate_g14():
    """Row (corrected): determinism is a HARNESS CONFIGURATION, NOT a test.

    A GREEN result here CONFIRMS the corrected row. If breaking determinism turns
    something red, the row is wrong again and determinism really is tested.
    """
    c = HSP / "tests/conftest.py"
    s = c.read_text(encoding="utf-8")
    if "derandomize=True" in s:
        _edit(c, "derandomize=True", "derandomize=False")
    elif "derandomize = True" in s:
        _edit(c, "derandomize = True", "derandomize = False")
    else:
        return -1, "no derandomize flag found -- inspect manually"
    try:
        return _run(HSP, ["tests/unit/test_flr_export_mu.py",
                          "tests/unit/test_export_is_additive.py"])
    finally:
        _restore(HSP, "tests/conftest.py")


def mutate_g15():
    """Row: fails if anything in floatsim/ imports the export modules."""
    t = HSP / "floatsim/solver/newmark.py"
    s = t.read_text(encoding="utf-8")
    t.write_text("import floatsim.io.flr_export  # MUTATION\n" + s, encoding="utf-8")
    try:
        return _run(HSP, ["tests/unit/test_export_is_additive.py"])
    finally:
        _restore(HSP, "floatsim/solver/newmark.py")


CASES = [
    ("G1.0 finding exists", mutate_g10, "RED"),
    ("G1.1 round-trip is bit-exact", mutate_g11, "RED"),
    ("G1.2 each fault has its own message", mutate_g12, "RED"),
    ("G1.3 hsp_git_sha half is enforced", mutate_g13, "RED"),
    ("G1.4 determinism is NOT a test", mutate_g14, "GREEN"),
    ("G1.5 additive-only is structural", mutate_g15, "RED"),
]

if __name__ == "__main__":
    print(f"{'row':38s} {'expect':>7} {'got':>7}  verdict")
    bad = 0
    for name, fn, expect in CASES:
        try:
            code, tail = fn()
        except Exception as e:  # noqa: BLE001 - report, do not mask
            print(f"{name:38s} {expect:>7} {'ERROR':>7}  {e}")
            bad += 1
            continue
        got = "GREEN" if code == 0 else "RED"
        ok = got == expect
        bad += not ok
        print(f"{name:38s} {expect:>7} {got:>7}  {'ok' if ok else 'MISMATCH'}")
        if not ok:
            print(f"    {tail.strip()[-300:]}")
    print(f"\n{len(CASES) - bad}/{len(CASES)} rows behaved as the claim text predicts")
    sys.exit(1 if bad else 0)
