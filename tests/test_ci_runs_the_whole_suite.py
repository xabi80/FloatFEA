"""Every test in this repository is executed by a named CI job (R235).

`.github/workflows/ci.yml` names eight paths across its jobs. Between them they
collected **1296** of the suite's **1589** tests, and the 293 that were missing
were every top-level `tests/test_*.py` -- which is where the guards live: the
tolerance-literal scanner, the carry guard, the counter meta-test, the plan and
figure checks, and the two corpora added at CB0 and CB1.

**So two published sentences were false in the same commit that wrote them.**
The step report said the reviewer's layouts run "in the suite, so in CI" and
`ci.yml` said "which means in CI"; neither file was ever collected by any job,
and the scanner that keeps every tolerance in `floatfea/tolerances.py` had never
run on a machine neither agent controls.

This file makes the claim mechanical instead of repeating it. It parses the
workflow, collects what each job actually names, and requires the union to be
the whole suite. A test added to a directory no job runs fails HERE, at the
commit that adds it, rather than being noticed the next time somebody reads the
YAML.

WHAT IT DOES NOT CHECK, stated so it is not trusted past its reach: that the
jobs are ordered correctly, that they run at all, or that a job's `needs:` chain
is intact. `tests/test_ci_ladder_gating.py` covers what each rung job does with
what it finds; this one covers only that nothing is left out.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"


def _invocations() -> list[list[str]]:
    """Each run step that collects tests, as the pytest arguments it implies.

    THE FLAGS ARE CARRIED, NOT JUST THE PATHS. The first version of this file
    kept only tokens beginning `tests`, so the guards job's
    `pytest tests --ignore=... --ignore=...` contributed the bare token `tests`
    and the union was the whole suite BY CONSTRUCTION -- a coverage check that
    could not fail, which is the same defect it was written to find.
    """
    text = WORKFLOW.read_text(encoding="utf-8")
    out: list[list[str]] = []
    # BOTH STEP FORMS. CK0 collapsed nine jobs into two and gave every step a
    # `name:`, so the command moved from `- run:` to a bare `run:` on the next
    # line. A parser that reads one form finds five steps where there are
    # eleven, and the union it compares is then a union of what it happened to
    # match -- the exact shape of the defect this file exists to catch.
    for step in re.findall(r"^\s*-? ?run: (.+)$", text, re.MULTILINE):
        tokens = step.split()
        if tokens[:2] == ["sh", "scripts/run_rung.sh"]:
            # Only `full:` directories are executed; `empty:` ones are asserted
            # to collect nothing, which is not coverage.
            out.append([t.split(":", 1)[1] for t in tokens[2:] if t.startswith("full:")])
        elif "pytest" in tokens:
            args = tokens[tokens.index("pytest") + 1 :]
            out.append([a for a in args if a != "-q"])
    return [args for args in out if any(a.startswith("tests") for a in args)]


def _collected(paths: list[str]) -> set[str]:
    """The node ids pytest collects for `paths`, as `file::name`."""
    if not paths:
        return set()
    out = subprocess.run(
        [sys.executable, "-m", "pytest", *paths, "-q", "--collect-only"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    ids: set[str] = set()
    for line in out.stdout.splitlines():
        if "::" in line and not line.startswith(" "):
            ids.add(line.strip().replace("\\", "/"))
    return ids


def test_the_workflow_names_paths_at_all() -> None:
    """Meta-test: a workflow this cannot parse would make the check vacuous."""
    steps = _invocations()
    assert steps, (
        f"no test-collecting run step parsed out of {WORKFLOW}. Either the "
        "workflow stopped naming them or the pattern broke, and both make the "
        "comparison below a comparison of two empty sets."
    )
    assert len(steps) >= 5, f"only {steps} parsed; the workflow names more"


def test_every_test_in_the_suite_is_run_by_some_ci_job() -> None:
    """The union of what CI runs is the suite. Measured, not read off the YAML."""
    everything = _collected(["tests"])
    covered: set[str] = set()
    for args in _invocations():
        covered |= _collected(args)
    missing = sorted(everything - covered)
    assert not missing, (
        f"{len(missing)} of {len(everything)} collected tests are run by no CI "
        f"job. First few: {missing[:5]}. Add a job that names them, or the "
        "sentence 'it runs in the suite, so it runs in CI' is false for them -- "
        "which it was for all 293 top-level guard tests until R235."
    )
