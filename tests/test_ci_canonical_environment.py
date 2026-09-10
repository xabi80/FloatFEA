"""Q8's canonical environment is held by a machine, not by a paragraph (R295).

Q8 makes CI canonical for the golden files, for every platform-dependent
tolerance, and for `docs/milestones/F2_figures.md`. The plan states the
condition that makes that defensible: the same BLAS kernel on every runner.
It was measured -- ten legs at one commit split exactly by CPU vendor, two
different renders, and the 2.6e9 ULP breach on the three Intel legs and nowhere
else -- and then pinned with one `env:` line.

**One line, and deleting it left the entire guard suite green.** The reviewer
ran that ablation twice, a round apart, and both times `463 passed, 0 failed`.
A condition three canonical artifacts rest on could be removed in silence, and
the round after the removal would look exactly like the round before it, except
that the goldens would start alternating by vendor again.

This file is the machine. It asserts the pin exists, that it is set once for
every job rather than per job, that the plan and the workflow name the SAME
kernel, and that each determinism leg records the kernel it actually ran under
so the verdict job can compare them. Delete the `env:` line and the first test
is red; change it in one place only and the third is.

WHAT IT DOES NOT DO, so it is not trusted past its reach: it reads the
workflow, not the runner. That the kernel is what OpenBLAS actually selected is
measured on CI by the determinism legs -- `leg/coretype.txt` -- and asserted
across legs by `determinism_verdict`. This file makes the declaration
undeletable; the legs make it true.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"
PLAN = ROOT / "docs" / "milestones" / "F2.md"

# The variable OpenBLAS reads to choose its kernel. Named once here so the
# three tests below cannot drift apart from each other.
PIN = "OPENBLAS_CORETYPE"


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def test_the_workflow_pins_the_BLAS_kernel() -> None:
    """The ablation the reviewer ran twice, as a test."""
    env = _workflow().get("env") or {}
    assert PIN in env, (
        f"`{PIN}` is not in the workflow's top-level `env:`. Q8 makes CI "
        "canonical for the goldens, the platform-dependent tolerances and "
        "`F2_figures.md`; without this pin the kernel is whatever CPU the job "
        "draws, and the same commit rendered two different files on the same "
        "day. The measurement is in `docs/milestones/F2.md`, Q8."
    )
    assert str(env[PIN]).strip(), f"`{PIN}` is declared empty, which is not a pin."


def test_the_pin_is_set_once_for_EVERY_job() -> None:
    """A per-job pin is a pin with holes in it.

    The quantity being controlled is a comparison BETWEEN jobs -- the
    determinism legs against each other, and the regression rung against the
    goldens some other job rendered. A kernel pinned on nine jobs of ten makes
    the tenth the odd one out and nothing says so.
    """
    doc = _workflow()
    assert PIN in (doc.get("env") or {}), (
        f"`{PIN}` must be set at the workflow's top level, where it reaches " "every job."
    )
    per_job = [
        name for name, job in (doc.get("jobs") or {}).items() if PIN in (job.get("env") or {})
    ]
    assert not per_job, (
        f"{per_job} set `{PIN}` for themselves. A second declaration is a "
        "second answer: the top-level one then holds for every job except "
        "these, and a cross-job comparison cannot see the difference."
    )


def test_the_plan_and_the_workflow_name_THE_SAME_kernel() -> None:
    """Q8 is a plan answer; the workflow is its implementation.

    If the workflow moves to a different kernel, every figure and tolerance
    taken under the old one is stale and the plan says otherwise. This is the
    BP0 rule with a machine behind it: when the rule beneath a figure moves,
    the figure is regenerated or withdrawn -- and here the move is one word.
    """
    env = _workflow()["env"]
    kernel = str(env[PIN]).strip().strip("\"'")
    plan = PLAN.read_text(encoding="utf-8", errors="replace")
    assert PIN in plan, (
        f"`{PIN}` appears nowhere in {PLAN.name}. R285: a lockfile does not "
        "pin the kernel, so the condition belongs in the locked plan and not "
        "only in the workflow."
    )
    assert re.search(rf"\b{re.escape(kernel)}\b", plan), (
        f"the workflow pins `{kernel}` and {PLAN.name} does not name it. One "
        "of the two moved. Every platform-dependent number in this repository "
        "is measured under the kernel the workflow sets, and Q8 is the "
        "sentence that says which one that is."
    )


def test_each_determinism_leg_records_the_kernel_it_RAN_under() -> None:
    """The declaration is not the measurement, and the leg is.

    `env:` says what the job asked for. `leg/coretype.txt` says what the
    process saw, and `determinism_verdict` requires the ten to agree and to be
    something other than `unset`. Without the recording step the ten legs could
    agree on a hash while running three different kernels, which is the
    coincidence the pin exists to remove.
    """
    text = WORKFLOW.read_text(encoding="utf-8")
    legs = text[text.index("  determinism:") :]
    assert "coretype.txt" in legs, (
        "no determinism leg writes `coretype.txt`. The kernel each leg ran "
        "under is then unrecorded, and the ten-leg comparison is a comparison "
        "of hashes with no environment attached to them."
    )
    verdict = text[text.index("  determinism_verdict:") :]
    assert "coretype.txt" in verdict and "unset" in verdict, (
        "`determinism_verdict` does not read the recorded core types, or does "
        "not reject `unset`. Ten legs agreeing while the pin is absent is the "
        "state this whole item is about."
    )
