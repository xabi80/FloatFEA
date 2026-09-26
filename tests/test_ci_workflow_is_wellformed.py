"""The workflow says what the commit that changed it claimed (CM2, R334).

CK0 made seven claims about `.github/workflows/ci.yml` and no test read any of
them. One was false: two `if:` keys on one job, where YAML keeps the last and
reports nothing, so the `workflow_dispatch` gate was discarded and ten
determinism legs kept running on every push. The run at the commit that shipped
it produced **no jobs at all**.

`yaml.safe_load` cannot see that -- it is the tool that silently keeps the last
key. This file loads with a duplicate-REJECTING loader, and then asserts each
of CK0's claims as a property of the parsed document rather than as a sentence
in a commit message.

`actionlint` runs in CI beside `ruff` and `mypy` and catches a wider class than
this. It needs a binary; this does not, so it runs wherever the suite runs --
which is where the claim was made.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"


class _NoDuplicates(yaml.SafeLoader):
    """A loader that refuses a mapping with a repeated key."""


def _no_duplicate_keys(loader: yaml.Loader, node: yaml.MappingNode, deep: bool = False) -> dict:
    seen: dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"duplicate key {key!r} at line {key_node.start_mark.line + 1}",
                key_node.start_mark,
            )
        seen[key] = loader.construct_object(value_node, deep=deep)
    return seen


_NoDuplicates.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicate_keys)


def _doc() -> dict:
    return yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=_NoDuplicates)


def test_the_workflow_has_no_duplicate_key() -> None:
    """The finding itself, as a test.

    `yaml.safe_load` keeps the last of two identical keys and says nothing,
    so the file parsed, the workflow ran, and the gate was gone. A loader
    that refuses the shape is the only reading that would have caught it.
    """
    try:
        _doc()
    except yaml.constructor.ConstructorError as exc:
        pytest.fail(
            f"{WORKFLOW.name} has a repeated key: {exc.problem}. YAML keeps "
            "the last one, so whichever of the two you meant may be the one "
            "discarded -- and nothing else in this repository reads it."
        )


def test_the_determinism_jobs_run_only_by_hand() -> None:
    """CK0's claim, and the one that was false."""
    jobs = _doc()["jobs"]
    for name in ("determinism", "determinism_verdict"):
        condition = str(jobs[name].get("if", ""))
        assert "workflow_dispatch" in condition, (
            f"`{name}` does not gate on `workflow_dispatch`: {condition!r}. "
            "Ten legs are twenty-two minutes of a push that did not move the "
            "render, the kernel pin or the environment."
        )


def test_a_push_does_not_run_twice() -> None:
    """Every commit in a pull request is also a push to the branch."""
    on = _doc()["on"] if "on" in _doc() else _doc()[True]
    assert "pull_request" not in on, (
        "the `pull_request` trigger is back, so every push measures the same " "tree twice."
    )
    assert "push" in on, "nothing triggers on a push, so nothing runs at all"


def test_a_documentation_commit_runs_no_job() -> None:
    on = _doc().get("on") or _doc()[True]
    ignored = on["push"].get("paths-ignore") or []
    for path in ("docs/reports/**", "docs/reviews/**"):
        assert path in ignored, f"{path} is not ignored; a report revision runs the suite"
    # R342: THIS SAID THE OPPOSITE OF WHAT IT MEANT. `all(... not in ...)`
    # passes on the shipped list -- where nothing mentions the render -- and
    # REDDENS on the carve-out it was written to require. Measured both ways
    # below rather than re-read.
    #
    # What is meant: `docs/milestones/**` holds the canonical render, and Q8
    # makes CI the only machine that may produce it. Ignoring that tree
    # wholesale means a commit that lands a render runs no job, so the
    # byte-identity assertion the next run is supposed to make never happens.
    # Either the tree is not ignored, or the render is carved back in.
    if "docs/milestones/**" in ignored:
        assert any("F2_figures" in x for x in ignored), (
            "`docs/milestones/**` is ignored and nothing carves the canonical "
            "render back in, so the commit that lands a render runs no job "
            "and the byte-identity check never fires. Add a `!` carve-out for "
            "`docs/milestones/F2_figures.md`."
        )


def test_a_superseded_run_is_cancelled() -> None:
    concurrency = _doc().get("concurrency") or {}
    assert concurrency.get("cancel-in-progress") is True, (
        "a superseded run finishes, which is minutes spent on a tree nobody " "will read."
    )


def test_the_ladder_is_not_chained_behind_the_guards() -> None:
    """R335. They are independent evidence and the last real run proves it.

    At run `34546580003` the guards job failed and all six ladder jobs
    passed. Chained, the ladder would have been skipped and this step's
    central result -- ladder 4 green on the canonical machine -- could not
    have been produced.
    """
    ladder = _doc()["jobs"]["ladder"]
    assert not ladder.get("needs"), (
        f"the ladder needs {ladder['needs']}. A lint error would then hide "
        "every rung, and a red guards job would hide the ladder's own green."
    )


def test_every_job_caches_its_wheels() -> None:
    for name, job in _doc()["jobs"].items():
        setups = [
            s for s in job["steps"] if str(s.get("uses", "")).startswith("actions/setup-python")
        ]
        installs = any("pip install" in str(s.get("run", "")) for s in job["steps"])
        if not setups:
            # A job that installs nothing needs no cache. `determinism_verdict`
            # downloads ten artifacts and reads them with the runner's own
            # python; requiring a setup step there would be requiring the
            # shape rather than the saving.
            assert not installs, f"`{name}` installs without setting up python"
            continue
        for step in setups:
            assert (step.get("with") or {}).get(
                "cache"
            ) == "pip", f"`{name}` installs numpy and scipy without a cache"


def test_actionlint_runs_in_CI() -> None:
    """The wider class this file cannot reach without a binary."""
    steps = _doc()["jobs"]["checks"]["steps"]
    assert any(
        "actionlint" in str(s.get("uses", "")) or s.get("name") == "actionlint" for s in steps
    ), (
        "nothing lints the workflow in CI. This file catches a duplicate key; "
        "actionlint catches the rest of the class."
    )
