"""`hsp_pin.worktree` — the two keys GI3(e)/R1208 introduced, and the three ways it
refused to behave until the reviewer ran it at configurations the diff did not choose.

**WHY THIS FILE EXISTS, AND IT IS R1220.** `worktree()` shipped with no test
exercising it at all. The import census over `tests/` that would have found that
looked for files importing `hsp_pin` and found two, both of which only read
`HSP_TAG` and `HSP_COMMIT`. So the resolver's whole decision table — three
sources, two keys, set-versus-unset, absolute-versus-relative — was unexercised,
and three defects sat inside it:

* **R1213** — a runs key pointed at the production `HSP-stable` passed the DS0
  check in `run_floatsim_design_waves.py`, because that check is an identity test
  against the other key rather than a name test. Held at its own call site below.
* **R1214** — a key that was SET AND WRONG was silently discarded and a different
  source used, so a caller opened a tree other than the one declared.
* **R1219** — a relative value resolved against the process's cwd, so one
  declaration named different worktrees depending on where it was started.

Each of the three is an *input accepted and used other than as declared*, which is
FR1's second head, and none is visible to `ruff`, `black`, `mypy`, the four root
guards or `tests/unit` as they stood.

**NOTHING HERE TOUCHES A REAL WORKTREE.** Every case builds its own directories
under `tmp_path`, so the file is green on a machine with no HSP checkout — which is
CI, by design, and is the whole reason `worktree()` has a non-refusing default.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from floatfea import hsp_pin


@pytest.fixture(autouse=True)
def _no_inherited_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    """Both keys unset unless a case sets one, so a developer's own environment
    cannot decide what these assertions measure."""
    monkeypatch.delenv(hsp_pin.HSP_RUNS_ENV, raising=False)
    monkeypatch.delenv(hsp_pin.HSP_STABLE_ENV, raising=False)


# ---------------------------------------------------------------------------
# The precedence table: declared, then env, then the legacy sibling.
# ---------------------------------------------------------------------------


def test_the_declared_key_wins_over_the_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    declared = tmp_path / "declared"
    env = tmp_path / "from_env"
    declared.mkdir()
    env.mkdir()
    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, str(env))
    assert hsp_pin.worktree("runs", declared) == declared.resolve()


def test_the_environment_is_used_when_nothing_is_declared(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    env = tmp_path / "from_env"
    env.mkdir()
    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, str(env))
    assert hsp_pin.worktree("runs") == env.resolve()


def test_the_two_keys_are_independent(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """R1208: one key for two worktrees is what made R1213 reachable. The stable
    key must not be answerable from the runs key or vice versa."""
    runs = tmp_path / "HSP-runs"
    stable = tmp_path / "HSP-stable"
    runs.mkdir()
    stable.mkdir()
    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, str(runs))
    monkeypatch.setenv(hsp_pin.HSP_STABLE_ENV, str(stable))
    assert hsp_pin.worktree("runs") == runs.resolve()
    assert hsp_pin.worktree("stable") == stable.resolve()
    assert hsp_pin.worktree("runs") != hsp_pin.worktree("stable")


# ---------------------------------------------------------------------------
# R1214. Set and wrong is a REFUSAL. Unset falls through.
# ---------------------------------------------------------------------------


def test_a_key_that_is_SET_AND_WRONG_refuses_rather_than_falling_through(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R1214, the direction that was broken.

    Reverting the `raise` in `hsp_pin.worktree` to the old `tried.append(...);
    continue` makes this test fail and nothing else in the suite move, which is
    the revert-red-restore cycle FT2 asks of a repair.
    """
    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, str(tmp_path / "does_not_exist"))
    with pytest.raises(SystemExit) as caught:
        hsp_pin.worktree("runs")
    message = str(caught.value)
    assert "declared and is not a directory" in message
    assert "does_not_exist" in message, "the refusal names the value it refused"
    assert hsp_pin.HSP_RUNS_ENV in message, "the refusal names WHICH source was wrong"


def test_a_declared_path_that_is_wrong_refuses_too(tmp_path: Path) -> None:
    """The config key, not just the environment variable."""
    with pytest.raises(SystemExit, match="declared and is not a directory"):
        hsp_pin.worktree("stable", tmp_path / "nope")


def test_an_UNSET_key_falls_through_without_refusing() -> None:
    """The other direction (EH4), and the reason `require=False` is the default.

    These are module-level constants in six scripts, three of which `tests/` and
    `scripts/export_f4_dynamic_inputs.py` import. Refusing here would turn "this
    machine has no worktree" -- true of CI by design -- into an ImportError that
    takes the whole module with it, which is R670's shape.
    """
    got = hsp_pin.worktree("runs")
    assert got.name == "HSP-runs"
    # `assert not got.is_absolute() or True` stood here. `X or True` is True for every
    # X, so it was a check that could not fail -- eleven lines below a docstring saying
    # exactly that (CW0). Deleted rather than repaired: the line above is the real
    # check, and whether the fallback path is absolute is not a property this test is
    # about. THIRD instance of this shape in one session; the other two were a source-text
    # assertion for R1213 and a wait condition that could not see its own process.


def test_require_True_refuses_and_names_every_candidate_it_tried() -> None:
    with pytest.raises(SystemExit) as caught:
        hsp_pin.worktree("runs", require=True)
    message = str(caught.value)
    assert "cannot locate the pinned HSP runs worktree" in message
    for expected in ("declared (floatsim.worktree_runs)", hsp_pin.HSP_RUNS_ENV, "legacy sibling"):
        assert expected in message, f"the refusal does not name {expected!r}"
    assert hsp_pin.HSP_TAG in message, "the refusal names the tag it wanted"


# ---------------------------------------------------------------------------
# R1219. A relative value is anchored to the repository, not the caller's shell.
# ---------------------------------------------------------------------------


def test_a_RELATIVE_value_resolves_against_the_repo_root_not_the_cwd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R1219. One declaration must name one worktree.

    Measured by moving the cwd and nothing else: the resolved path is the same.
    """
    # NOTHING IS CREATED IN THE REPOSITORY. An earlier version made and removed
    # `HSP-runs-r1219-probe` in the repo root to have something a relative path could
    # reach; a test that writes into the tree it is testing is one interrupted run away
    # from leaving litter behind. The relative value here is `tmp_path` expressed
    # relative to the root, which exercises the same anchor with no side effect.
    root = Path(hsp_pin.__file__).resolve().parents[1]
    target = tmp_path / "HSP-runs"
    target.mkdir()
    relative = os.path.relpath(target, root)
    assert not Path(relative).is_absolute(), "the probe value must be relative to mean anything"

    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, relative)
    here = hsp_pin.worktree("runs")
    monkeypatch.chdir(tmp_path)
    there = hsp_pin.worktree("runs")
    assert here == there == target.resolve(), (
        "a relative key resolved differently from two working directories, so one "
        "declaration named two trees (R1219)"
    )


def test_an_unknown_key_name_is_a_programming_error_not_a_path() -> None:
    with pytest.raises(ValueError, match="must be 'runs' or 'stable'"):
        hsp_pin.worktree("production")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# R1213. The DS0 refusal at its own CALL SITE, which is what FT2 asks for.
# ---------------------------------------------------------------------------


def test_the_DS0_refusal_fires_when_the_RUNS_key_names_the_STABLE_tree(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R1213, held at the call site rather than at the helper.

    `run_floatsim_design_waves.preflight()` checked `RUNS.resolve() ==
    STABLE.resolve()` -- an identity test against the other key. That could not be
    tripped while both were literals; GI3(e) made it reachable, and then a runs key
    pointed at the real `HSP-stable` passed the check while `main()` went on to
    write six case files into the read-only production worktree.

    THIS DRIVES `preflight()` ITSELF AND NOT THE SOURCE TEXT. The first version of
    this test asserted that the predicate's source line was present, and the
    revert-red-restore cycle exposed it immediately: disabling the test with
    `if False and ...` left the string in the file, so the test passed with the
    repair reverted. A check that cannot fail is not a check (CW0). What follows
    calls the function and requires the refusal.

    `preflight()` is reachable without a worktree because the name test precedes
    every `subprocess` call in it, and the module's own imports of
    `platform_rao_pilot` are inside `main()`.
    """
    monkeypatch.syspath_prepend(str(Path(hsp_pin.__file__).resolve().parents[1] / "scripts"))
    import run_floatsim_design_waves as module

    stable_like = tmp_path / "buoy" / "HSP-stable"
    stable_like.mkdir(parents=True)
    elsewhere = tmp_path / "other" / "HSP-stable-decoy"
    elsewhere.mkdir(parents=True)

    monkeypatch.setattr(module, "RUNS", stable_like)
    monkeypatch.setattr(module, "STABLE", elsewhere)

    # The identity test ALONE does not catch this -- the two keys differ, which is
    # exactly the input GI3(e) made reachable and the identity test cannot see.
    assert stable_like.resolve() != elsewhere.resolve()

    with pytest.raises(SystemExit) as caught:
        module.preflight()
    message = str(caught.value)
    assert "HSP-stable" in message and "DS0" in message, (
        "preflight() must refuse by NAME and not only by identity with the stable key "
        f"(R1213). Got: {message!r}"
    )
