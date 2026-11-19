"""`floatfea export` — what it refuses before it spends 26 minutes, and what argv it builds.

GJ4 opened R2 step 1 and replaced `_cmd_export`'s honest refusal with the run. Four things
happen before any solve and each one refuses; this file is those four, plus the argv the
engine is handed and the environment it is handed it in.

**NOTHING HERE RUNS FLOATSIM, OPENS A BEM DATASET OR NEEDS A VENV.** The worktree, the
locked interpreter, the covered-heading query and the child process are each substituted,
so the file is green on a machine with no HSP checkout — which is CI, by design. What it
measures is the decision logic, which is the half a machine can hold; that the solve
reproduces the golden is `--check`'s job and takes half an hour.

**THE REFUSALS ARE TIMED, NOT JUST PRESENT.** A heading the dataset does not cover is
refused *before* the solve starts. R2 step 0 measured one D4 iteration at 26 minutes, so a
check that fires afterwards costs a working afternoon per typo, and a check that fires
after the file is WRITTEN publishes a file labelled with a heading nobody can produce.
`test_the_heading_refusal_fires_BEFORE_the_engine_is_invoked` is that assertion.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from floatfea import cli, determinism, floatsim_env, hsp_pin

# `cli.main` CATCHES `ConfigError`, prints `floatfea: <message>` to stderr and returns 2.
# These assertions go through `main` rather than calling `_cmd_export`, so what is measured
# is what a person at a terminal sees -- and the first version of this file used
# `pytest.raises(ConfigError)`, which passed on the exception and said nothing about
# whether the message ever reached anybody. Six of its ten tests were green on a refusal
# the user would never have seen.
REFUSED = 2


def _refusal(capsys) -> str:  # type: ignore[no-untyped-def]
    return capsys.readouterr().err


ROOT = Path(__file__).resolve().parents[2]
EXPORT_CFG = ROOT / "examples" / "platform12_export.yaml"
PLACEHOLDER_CFG = ROOT / "examples" / "platform12_placeholder.yaml"


class _Spy:
    """Stands in for `subprocess.run`, recording what it was asked to do."""

    def __init__(self, returncode: int = 0, stdout: str = "") -> None:
        self.calls: list[dict[str, object]] = []
        self._returncode = returncode
        self._stdout = stdout

    def __call__(self, argv, **kw):  # type: ignore[no-untyped-def]
        self.calls.append({"argv": list(argv), **kw})
        return subprocess.CompletedProcess(argv, self._returncode, stdout=self._stdout, stderr="")


@pytest.fixture
def no_hsp(monkeypatch: pytest.MonkeyPatch) -> None:
    """The worktree and the locked interpreter resolve, without either existing.

    Substituted at the names `cli` calls rather than by setting the env keys, because a
    key pointed at a path that is not a directory is a REFUSAL by design (R1214) -- so the
    env-var route cannot be used to fake a resolution, which is the point of that rule.
    """
    monkeypatch.setattr(hsp_pin, "worktree", lambda which, *a, **k: Path("/pinned/HSP-runs"))
    monkeypatch.setattr(floatsim_env, "interpreter", lambda *a, **k: Path("/locked/python"))


@pytest.fixture
def covered_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    """The pinned BEM database carries one heading, which is what R2 step 0 measured."""
    monkeypatch.setattr(cli, "_covered_headings", lambda *a, **k: (0.0,))


def _cfg(tmp_path: Path, replace: list[tuple[str, str]], name: str = "cfg.yaml") -> Path:
    """The export configuration with substitutions, written beside the real one.

    Written into `examples/` under a `tmp_` name rather than into `tmp_path`, because the
    configuration's paths are relative to its own directory and a copy somewhere else
    would fail validation on the deck before reaching the code under test.
    """
    text = EXPORT_CFG.read_text(encoding="utf-8")
    for old, new in replace:
        assert text.count(old) >= 1, f"the anchor {old!r} is not in the export config"
        text = text.replace(old, new)
    at = EXPORT_CFG.parent / f"tmp_{name}"
    at.write_text(text, encoding="utf-8")
    _WROTE.append(at)
    return at


_WROTE: list[Path] = []


@pytest.fixture(autouse=True)
def _sweep():  # type: ignore[no-untyped-def]
    """Remove the temporary configurations THIS FILE WROTE, and nothing else.

    **IT GLOBBED `tmp_*.yaml` AND DELETED SOMEBODY ELSE'S FILES.** `examples/` is a
    tracked, shared directory, and a sweep by pattern removes whatever matches it --
    including the two scratch configurations a 25-minute measurement was running against
    at the time. The measurement lost the half of its work that had not started yet, and
    nothing said why: the config was simply not there when the second command looked for
    it.

    A fixture that cleans up by PATTERN cleans up by guess. This one records what it
    wrote and removes exactly that, which is the same distinction `_is_tracked` draws in
    the engine: ask the question directly rather than infer it from a name.
    """
    del _WROTE[:]
    yield
    for stale in _WROTE:
        stale.unlink(missing_ok=True)
    del _WROTE[:]


# ---------------------------------------------------------------------------
# 1. A configuration that already has the file
# ---------------------------------------------------------------------------


def test_a_config_pointing_at_an_EXISTING_npz_is_refused(capsys) -> None:
    """`export` PRODUCES that file. The placeholder reads one, so it is the wrong input."""
    assert cli.main(["export", str(PLACEHOLDER_CFG)]) == REFUSED
    message = _refusal(capsys)
    assert "load_cases already points at" in message
    assert "declare `cases` instead" in message


# ---------------------------------------------------------------------------
# 2. The heading key R2 step 0 measured as absent everywhere
# ---------------------------------------------------------------------------


def test_an_ABSENT_heading_key_is_refused_and_the_message_names_the_covered_set(
    tmp_path: Path, no_hsp: None, covered_zero: None, capsys
) -> None:
    """§2b: no configuration in this repository declared a heading, so D4's "every heading
    in the R1 config" was unrepresentable and FL2(c)'s refusal had no input.

    `refuse_uncovered_headings((), covered)` returns WITHOUT raising, correctly -- for
    `floatfea run` an undeclared set means "do not check". `export` is the other case, so
    the empty set has to be refused here rather than relied on there.
    """
    cfg = _cfg(tmp_path, [("  headings: [0.0]\n", "")])
    assert cli.main(["export", str(cfg)]) == REFUSED
    message = _refusal(capsys)
    assert "load_cases.headings is not declared" in message
    assert "[0.0] deg" in message


def test_an_UNCOVERED_heading_is_refused_by_NAME_against_what_the_dataset_carries(
    tmp_path: Path, no_hsp: None, covered_zero: None, capsys
) -> None:
    """FL2(c)'s refusal, reachable for the first time since R1."""
    cfg = _cfg(
        tmp_path,
        [
            ("  headings: [0.0]\n", "  headings: [45.0]\n"),
            ("heading: 0.0,", "heading: 45.0,"),
        ],
    )
    assert cli.main(["export", str(cfg)]) == REFUSED
    message = _refusal(capsys)
    assert "[45.0] deg, which the BEM dataset does not cover" in message
    assert "It carries [0.0] deg" in message


def test_the_heading_refusal_fires_BEFORE_the_engine_is_invoked(
    tmp_path: Path, no_hsp: None, covered_zero: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The timing assertion, and it is the one with a cost attached.

    One D4 iteration is 26 minutes (R2 step 0 (b)). A heading check that ran after the
    solve would charge a working afternoon for a typo; one that ran after the WRITE would
    publish a file labelled with a heading nobody can produce.
    """
    spy = _Spy()
    monkeypatch.setattr(cli.subprocess, "run", spy)
    cfg = _cfg(
        tmp_path,
        [
            ("  headings: [0.0]\n", "  headings: [45.0]\n"),
            ("heading: 0.0,", "heading: 45.0,"),
        ],
    )
    assert cli.main(["export", str(cfg)]) == REFUSED
    assert spy.calls == [], (
        "the engine was invoked although the heading is uncovered. The refusal has to "
        "come first: the solve is 26 minutes and the write is irreversible."
    )


# ---------------------------------------------------------------------------
# 3. Two keys describing one quantity
# ---------------------------------------------------------------------------


def test_headings_that_DISAGREE_with_the_declared_cases_are_refused(
    tmp_path: Path, no_hsp: None, monkeypatch: pytest.MonkeyPatch, capsys
) -> None:
    """One predicate, two readers -- the shape R2 step 0 paid five rounds for, here in a
    configuration rather than in a guard. `headings: [0]` beside cases at 45 deg would
    export at 45 and label the file 0."""
    monkeypatch.setattr(cli, "_covered_headings", lambda *a, **k: (0.0, 45.0))
    cfg = _cfg(tmp_path, [("heading: 0.0,", "heading: 45.0,")])
    assert cli.main(["export", str(cfg)]) == REFUSED
    message = _refusal(capsys)
    assert "load_cases.headings is [0.0] deg but the declared cases sit at [45.0] deg" in message
    assert "false label on a published file" in message


def test_an_EMPTY_case_list_is_refused_rather_than_exporting_nothing(
    tmp_path: Path, no_hsp: None, covered_zero: None, capsys
) -> None:
    text = EXPORT_CFG.read_text(encoding="utf-8")
    head, _, tail = text.partition("  cases:\n")
    rest = tail.split("  headings:", 1)[1]
    at = EXPORT_CFG.parent / "tmp_empty.yaml"
    at.write_text(f"{head}  cases: []\n  headings:{rest}", encoding="utf-8")
    _WROTE.append(at)
    assert cli.main(["export", str(at)]) == REFUSED
    message = _refusal(capsys)
    assert "there is nothing to export" in message
    assert "an error and not a skip" in message


# ---------------------------------------------------------------------------
# 4. What the engine is handed
# ---------------------------------------------------------------------------


def test_the_engine_gets_the_LOCKED_interpreter_and_one_period_per_declared_case(
    no_hsp: None, covered_zero: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    spy = _Spy()
    monkeypatch.setattr(cli.subprocess, "run", spy)
    assert cli.main(["export", str(EXPORT_CFG)]) == 0
    argv = spy.calls[0]["argv"]
    assert argv[0] == str(Path("/locked/python"))
    assert argv[1].endswith(str(cli.EXPORT_ENGINE))
    periods = [argv[i + 1] for i, a in enumerate(argv) if a == "--period"]
    assert sorted(float(p) for p in periods) == [10.0, 12.5, 14.0, 15.0, 16.2, 20.0]
    assert "--check" not in argv


def test_check_is_passed_through_and_the_exit_code_is_the_ENGINE_S(
    no_hsp: None, covered_zero: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A refusal inside the engine -- `--check` finding one array different -- must reach
    the caller's exit status. Swallowing it would make a failed bit-exactness comparison
    look like a successful export, which is Q8's whole subject."""
    spy = _Spy(returncode=1)
    monkeypatch.setattr(cli.subprocess, "run", spy)
    assert cli.main(["export", str(EXPORT_CFG), "--check"]) == 1
    assert "--check" in spy.calls[0]["argv"]


def test_the_child_environment_PINS_the_threads_and_the_BLAS_kernel() -> None:
    """Reduction order varies with thread count, so a float sum is not bit-reproducible
    unless the count is fixed -- and GI5 step 2's zero-change test is a bit-identical
    comparison. A child that inherited an unpinned count would be a different computation
    from the one that made the golden, and the only symptom would be a `--check` refusal
    nobody could explain."""
    env = cli._child_env()
    assert [env[v] for v in determinism.THREAD_ENV] == ["1"] * len(determinism.THREAD_ENV)
    assert env["OPENBLAS_CORETYPE"] == determinism.CANONICAL_CORETYPE


def test_an_INHERITED_coretype_is_NOT_overridden(monkeypatch: pytest.MonkeyPatch) -> None:
    """`setdefault`, not assignment, and the inverted direction says why it matters: CI
    sets `OPENBLAS_CORETYPE` at the workflow's top level for every job, and a child that
    overwrote it would run at a kernel the workflow did not choose. The thread counts ARE
    assigned, because an inherited `OMP_NUM_THREADS=8` is not a choice anyone made for
    this comparison."""
    monkeypatch.setenv("OPENBLAS_CORETYPE", "Zen")
    monkeypatch.setenv("OMP_NUM_THREADS", "8")
    env = cli._child_env()
    assert env["OPENBLAS_CORETYPE"] == "Zen"
    assert env["OMP_NUM_THREADS"] == "1"


# ---------------------------------------------------------------------------
# 5. The declared keys GI3(e) asked for, which this command is the first to pass
# ---------------------------------------------------------------------------


def test_a_DECLARED_worktree_wins_over_the_environment_variable(
    monkeypatch: pytest.MonkeyPatch, covered_zero: None
) -> None:
    """GI3(e): *"Make it a config key with an env-var fallback."*

    R2 step 0 built the env-var half and the default. The key itself did not exist, and
    `hsp_pin.worktree`'s docstring named it anyway -- so the first arm of its decision
    table was reachable only from `tests/`. This is the production caller that makes the
    docstring true.
    """
    seen: list[object] = []
    monkeypatch.setattr(
        hsp_pin,
        "worktree",
        lambda which, declared=None, **k: seen.append(declared) or Path("/pinned"),
    )
    monkeypatch.setattr(floatsim_env, "interpreter", lambda *a, **k: Path("/locked/python"))
    monkeypatch.setattr(cli.subprocess, "run", _Spy())
    cfg = _cfg(
        tmp_path=Path("."),
        replace=[
            (
                "  deck: ../data/platform",
                "  worktree_runs: /declared/HSP-runs\n  deck: ../data/platform",
            )
        ],
        name="declared.yaml",
    )
    assert cli.main(["export", str(cfg)]) == 0
    assert seen == [Path("/declared/HSP-runs")]


def test_an_EMPTY_declared_key_is_refused_rather_than_falling_through(capsys) -> None:
    """R1214, at the configuration boundary. `worktree_runs: ""` is something somebody
    typed, and an empty value that fell through to the environment variable would open a
    different tree from the one the file declares -- which is FR1's second head."""
    cfg = _cfg(
        tmp_path=Path("."),
        replace=[("  deck: ../data/platform", '  worktree_runs: ""\n  deck: ../data/platform')],
        name="empty_key.yaml",
    )
    assert cli.main(["export", str(cfg)]) == REFUSED
    message = _refusal(capsys)
    assert "floatsim.worktree_runs is declared EMPTY" in message
    assert "absent is not the same" in message or "not the same as an" in message


def test_an_UNKNOWN_key_in_the_floatsim_block_is_still_refused(capsys) -> None:
    """The inverted direction for widening a schema: three keys were added, so the test
    that matters is that a FOURTH is still refused. A block that accepted anything would
    turn a typo -- `worktree_run` -- into a silent fall-through to the environment."""
    cfg = _cfg(
        tmp_path=Path("."),
        replace=[("  deck: ../data/platform", "  worktree_run: /typo\n  deck: ../data/platform")],
        name="typo.yaml",
    )
    assert cli.main(["export", str(cfg)]) == REFUSED
    assert "worktree_run" in _refusal(capsys)


def test_the_RESOLVED_worktree_and_venv_REACH_THE_CHILD(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, covered_zero: None
) -> None:
    """A config key reaches the parent and nothing else unless it is passed down.

    The child resolves both paths again for itself -- `floatsim_env.lock_path()` asks
    `hsp_pin.worktree("runs")`, and `report_joint_reactions.HSP_RUNS` is evaluated at the
    child's import, before any configuration is read. So a configuration that declared a
    worktree and set no environment variable had the child fall through to the default:
    a refusal on a machine without one, and on a machine WITH one, a different tree from
    the one the configuration names. That second case is FR1's second head and it is
    silent.

    **THE DECLARED VENV IS A REAL DIRECTORY AND `floatsim_env.venv` IS NOT SUBSTITUTED**,
    which the first version of this test got wrong in a useful way: it declared
    `/declared/venv`, which does not exist, and the real resolver REFUSED it under R1214 --
    a key that is set and wrong does not fall through. The refusal was right and the test
    was asserting past it, so the directory is created here and the resolver runs.
    """
    monkeypatch.delenv(hsp_pin.HSP_RUNS_ENV, raising=False)
    monkeypatch.delenv(floatsim_env.VENV_ENV, raising=False)
    monkeypatch.setattr(hsp_pin, "worktree", lambda which, *a, **k: Path("/pinned/HSP-runs"))
    monkeypatch.setattr(floatsim_env, "interpreter", lambda *a, **k: Path("/locked/python"))
    declared_venv = tmp_path / "declared-venv"
    declared_venv.mkdir()
    spy = _Spy()
    monkeypatch.setattr(cli.subprocess, "run", spy)
    cfg = _cfg(
        tmp_path=tmp_path,
        replace=[
            (
                "  deck: ../data/platform",
                f"  worktree_runs: /declared/HSP-runs\n  venv: {declared_venv.as_posix()}\n"
                "  deck: ../data/platform",
            )
        ],
        name="passdown.yaml",
    )
    assert cli.main(["export", str(cfg)]) == 0
    child = spy.calls[-1]["env"]
    assert child[hsp_pin.HSP_RUNS_ENV] == str(Path("/pinned/HSP-runs")), (
        "the worktree the PARENT resolved must reach the child, not the key it resolved "
        "it from: the parent is the one that applied the precedence table."
    )
    assert child[floatsim_env.VENV_ENV] == str(declared_venv.resolve())


def test_an_INHERITED_worktree_variable_is_OVERRIDDEN_by_the_resolved_one(
    monkeypatch: pytest.MonkeyPatch, covered_zero: None
) -> None:
    """`setdefault` would be wrong here, and this is the inverted direction that says so.

    The coretype is `setdefault` because CI sets it deliberately for every job. The
    worktree is ASSIGNED, because an inherited variable naming a different tree than the
    configuration declares is exactly the disagreement the pass-down exists to prevent --
    and the parent, not the environment, is what applied the precedence table.
    """
    monkeypatch.setenv(hsp_pin.HSP_RUNS_ENV, r"C:\stale\HSP-runs")
    monkeypatch.setattr(hsp_pin, "worktree", lambda which, *a, **k: Path("/pinned/HSP-runs"))
    monkeypatch.setattr(floatsim_env, "interpreter", lambda *a, **k: Path("/locked/python"))
    spy = _Spy()
    monkeypatch.setattr(cli.subprocess, "run", spy)
    assert cli.main(["export", str(EXPORT_CFG)]) == 0
    assert spy.calls[-1]["env"][hsp_pin.HSP_RUNS_ENV] == str(Path("/pinned/HSP-runs"))


def test_the_sweep_does_NOT_remove_a_tmp_FILE_THIS_FILE_DID_NOT_WRITE(
    no_hsp: None, covered_zero: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The inverted direction for the cleanup fixture, and it is the defect it was
    written after.

    The fixture globbed `tmp_*.yaml` in `examples/` -- a tracked, shared directory -- and
    deleted two scratch configurations a 25-minute measurement was running against. The
    measurement lost the half of its work that had not started, and nothing said why: the
    file was simply absent when the second command looked for it.

    A decoy with a matching name is created here and must survive the test that writes
    beside it. `_sweep` removes what it RECORDED writing, so a glob regression reddens
    this immediately rather than in whatever else happens to be using the directory.
    """
    decoy = EXPORT_CFG.parent / "tmp_not_mine.yaml"
    decoy.write_text("# somebody else's file\n", encoding="utf-8")
    try:
        monkeypatch.setattr(cli.subprocess, "run", _Spy())
        assert cli.main(["export", str(_cfg(Path("."), [], name="decoy.yaml"))]) == 0
        assert decoy.is_file(), (
            "the cleanup removed a file this test file did not write. A fixture that "
            "cleans up by PATTERN cleans up by guess."
        )
    finally:
        decoy.unlink(missing_ok=True)
