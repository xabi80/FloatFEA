"""`floatfea.floatsim_env` — GJ1's locked environment, and what it refuses.

GJ1 ruled FQ3: restore the lock, do not re-base. Three clauses, each with a test below:
build from `requirements-lock.txt` exactly, every FloatSim invocation under that
environment, and its path and lock hash recorded in the provenance.

**WHY THE FILE IS WRITTEN BEFORE THE CALL SITE.** `hsp_pin.worktree` shipped in R2 step 0
with no test exercising it, and three defects sat in its decision table — R1213, R1214 and
R1219, each an *input accepted and used other than as declared*, none visible to `ruff`,
`black`, `mypy` or any guard (R1220). This module resolves by the same table, so it gets
the same coverage on the way in rather than after a reviewer runs it at a configuration
the diff did not choose.

**EVERY BOUNDARY IS SOLVED IN BOTH DIRECTIONS (EH4)**, including the direction that
weakens the check: for each refusal there is a case that passes it and a case that trips
it, and for `refuse_unless_locked` the passing case is built by *satisfying* the lock
rather than by emptying it.

**NOTHING HERE TOUCHES A REAL VENV OR A REAL WORKTREE.** Every case builds its own
directories under `tmp_path`, so the file is green on a machine with neither — which is
CI, by design.
"""

from __future__ import annotations

import importlib.metadata as md
import os
from pathlib import Path

import pytest

from floatfea import floatsim_env as fse
from floatfea import hsp_pin

ROOT = Path(__file__).resolve().parents[2]

# The lock's real shape, including the editable line SR-75 does not install. Trimmed to
# five pins; the three names are chosen because they are the ones PEP 503 normalisation
# actually matters for.
LOCK_TEXT = """\
annotated-types==0.7.0
-e git+https://github.com/xabi80/HSP.git@928ae47473ccfab3e34ab318816582ae42ae2eec#egg=floatsim
numpy==2.4.4
scipy==1.17.1
types-PyYAML==6.0.12.20260408
typing_extensions==4.15.0
"""


@pytest.fixture(autouse=True)
def _no_inherited_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """The venv key unset unless a case sets it, so a developer's own environment cannot
    decide what these assertions measure."""
    monkeypatch.delenv(fse.VENV_ENV, raising=False)


def _venv(at: Path) -> Path:
    """A venv-shaped directory with this platform's interpreter inside it."""
    sub = at / ("Scripts" if os.name == "nt" else "bin")
    sub.mkdir(parents=True)
    exe = sub / ("python.exe" if os.name == "nt" else "python")
    exe.write_bytes(b"")
    return at


# ---------------------------------------------------------------------------
# The precedence table, which is `hsp_pin.resolve_declared_path`'s
# ---------------------------------------------------------------------------


def test_the_declared_key_wins_over_the_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    declared = _venv(tmp_path / "declared")
    monkeypatch.setenv(fse.VENV_ENV, str(_venv(tmp_path / "from_env")))
    assert fse.venv(declared) == declared.resolve()


def test_the_environment_is_used_when_nothing_is_declared(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from_env = _venv(tmp_path / "from_env")
    monkeypatch.setenv(fse.VENV_ENV, str(from_env))
    assert fse.venv() == from_env.resolve()


def test_a_key_that_is_SET_AND_WRONG_refuses_rather_than_falling_through(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R1214, in the second place the table is read.

    The default `.venv-floatsim` may well exist on the machine running this, which is
    exactly the condition under which a silent fall-through is invisible: the caller gets
    a working venv that is not the one declared.
    """
    monkeypatch.setenv(fse.VENV_ENV, str(tmp_path / "nope"))
    with pytest.raises(SystemExit) as caught:
        fse.venv()
    message = str(caught.value)
    assert "was declared and is not a directory" in message
    assert "nope" in message
    assert "R1214" in message


def test_a_RELATIVE_value_resolves_against_the_repo_root_not_the_cwd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """R1219. The control is that the cwd is moved and the answer does not."""
    monkeypatch.setenv(fse.VENV_ENV, ".venv-floatsim")
    monkeypatch.chdir(tmp_path)
    if not (ROOT / fse.DEFAULT_VENV).is_dir():
        pytest.skip(f"{fse.DEFAULT_VENV} is not built here, so there is nothing to anchor")
    assert fse.venv() == (ROOT / fse.DEFAULT_VENV).resolve()


def test_an_UNSET_key_falls_through_to_the_default_without_refusing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The default is not a source anybody SET, so its absence is the ordinary state of a
    machine that has not built it -- true of CI -- and `require=False` must not raise."""
    got = fse.venv()
    assert got == ROOT / fse.DEFAULT_VENV


def test_require_True_refuses_and_names_every_candidate_it_tried(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(fse, "_repo_root", lambda: tmp_path)
    monkeypatch.setattr(hsp_pin, "_repo_root", lambda: tmp_path)
    with pytest.raises(SystemExit) as caught:
        fse.venv(require=True)
    message = str(caught.value)
    assert "cannot locate the locked FloatSim run environment (GJ1)" in message
    assert "declared (floatsim.venv): not set" in message
    assert f"${fse.VENV_ENV}: not set" in message
    assert fse.DEFAULT_VENV in message


# ---------------------------------------------------------------------------
# The interpreter inside it
# ---------------------------------------------------------------------------


def test_the_interpreter_is_this_platforms_and_is_not_probed_for(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The layout is branched on `os.name`, so a venv carrying BOTH layouts -- one copied
    between platforms, which is the state a lock exists to make detectable -- still yields
    this platform's interpreter rather than whichever file is found first."""
    both = tmp_path / "both"
    _venv(both)
    other = both / ("bin" if os.name == "nt" else "Scripts")
    other.mkdir()
    (other / ("python" if os.name == "nt" else "python.exe")).write_bytes(b"")
    got = fse.interpreter(both, require=True)
    assert got.parent.name == ("Scripts" if os.name == "nt" else "bin")
    assert got.name == ("python.exe" if os.name == "nt" else "python")


def test_a_directory_that_is_not_a_venv_refuses_under_require(tmp_path: Path) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(SystemExit) as caught:
        fse.interpreter(empty, require=True)
    assert "carries no interpreter for this platform" in str(caught.value)


def test_the_same_directory_does_NOT_refuse_without_require(tmp_path: Path) -> None:
    """The inverted direction. `require=False` is the import-time default and must return
    a candidate rather than raising (R670)."""
    empty = tmp_path / "empty"
    empty.mkdir()
    assert fse.interpreter(empty).parent.parent == empty.resolve()


# ---------------------------------------------------------------------------
# Parsing the lock
# ---------------------------------------------------------------------------


def test_the_lock_parses_to_its_pins_and_the_editable_is_NOT_one_of_them() -> None:
    lock = fse.parse_lock(LOCK_TEXT)
    assert lock == {
        "annotated-types": "0.7.0",
        "numpy": "2.4.4",
        "scipy": "1.17.1",
        "types-pyyaml": "6.0.12.20260408",
        "typing-extensions": "4.15.0",
    }
    assert "floatsim" not in lock


def test_the_editable_line_is_REPORTED_verbatim_rather_than_dropped() -> None:
    """SR-75 records a deviation from the lock, and a deviation nobody can see is not a
    record. The provenance carries this line so a reader can check the claim that
    `928ae474` is an ancestor of the pin."""
    got = fse.editables(LOCK_TEXT)
    assert len(got) == 1
    assert got[0].startswith("-e git+https://github.com/xabi80/HSP.git@928ae474")


def test_PEP_503_normalisation_is_what_makes_the_comparison_work() -> None:
    """Without it `types-PyYAML` and `typing_extensions` read as two mismatches on a
    CORRECT environment, because `importlib.metadata` answers to the normalised name. A
    check that cries wolf on a good tree is a check that gets deleted."""
    assert fse.canonical("types-PyYAML") == "types-pyyaml"
    assert fse.canonical("typing_extensions") == "typing-extensions"
    assert fse.canonical("zope.interface") == "zope-interface"


def test_a_sha256_is_taken_over_BYTES_so_line_endings_do_not_change_it(
    tmp_path: Path,
) -> None:
    """The control for a text read: the same pins with CRLF endings must hash DIFFERENTLY,
    because the recorded hash identifies a file and a text read would make two files
    identical. If this ever reads equal, `lock_sha256` has started normalising."""
    lf = tmp_path / "lf.txt"
    crlf = tmp_path / "crlf.txt"
    lf.write_bytes(LOCK_TEXT.encode("utf-8"))
    crlf.write_bytes(LOCK_TEXT.replace("\n", "\r\n").encode("utf-8"))
    assert fse.parse_lock(lf.read_text()) == fse.parse_lock(crlf.read_text())
    assert fse.lock_sha256(lf) != fse.lock_sha256(crlf)


# ---------------------------------------------------------------------------
# The preflight: SR-76's refusal
# ---------------------------------------------------------------------------


def _satisfied_lock(tmp_path: Path) -> Path:
    """A lock this very interpreter satisfies, built FROM what is installed.

    EH4's passing direction, and it is built this way on purpose: a lock trimmed to
    nothing would also pass, and would prove only that the check can be made vacuous.
    """
    names = ["pytest", "numpy"]
    lines = [f"{n}=={md.version(n)}" for n in names]
    at = tmp_path / "satisfied.txt"
    at.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return at


def test_an_interpreter_that_SATISFIES_the_lock_passes_and_returns_the_pins(
    tmp_path: Path,
) -> None:
    lock = fse.refuse_unless_locked(_satisfied_lock(tmp_path), doing="export")
    assert lock["numpy"] == md.version("numpy")
    assert fse.mismatches(lock) == []


def test_ONE_WRONG_VERSION_IS_ENOUGH_TO_REFUSE_and_the_message_names_both(
    tmp_path: Path,
) -> None:
    """The direction that matters: FQ3's defect was numpy `2.4.4 -> 2.5.4`, one pin."""
    at = tmp_path / "one-wrong.txt"
    at.write_text(f"numpy==0.0.1\npytest=={md.version('pytest')}\n", encoding="utf-8")
    with pytest.raises(SystemExit) as caught:
        fse.refuse_unless_locked(at, doing="export the dynamic inputs")
    message = str(caught.value)
    assert "does not satisfy 1 of the lock's 2 pins" in message
    assert f"numpy: lock 0.0.1, this interpreter {md.version('numpy')}" in message
    assert "export the dynamic inputs" in message
    assert "SR-76" in message


def test_an_ABSENT_distribution_reads_ABSENT_and_not_as_a_wrong_version(
    tmp_path: Path,
) -> None:
    """A missing package and a wrong version have different repairs, so they are not
    merged into one word."""
    at = tmp_path / "absent.txt"
    at.write_text("floatfea-no-such-dist==1.0\n", encoding="utf-8")
    with pytest.raises(SystemExit) as caught:
        fse.refuse_unless_locked(at, doing="export")
    assert "this interpreter ABSENT" in str(caught.value)


def test_a_MISSING_lock_refuses_rather_than_passing_vacuously(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as caught:
        fse.refuse_unless_locked(tmp_path / "nothing-here.txt", doing="export")
    assert "does not exist" in str(caught.value)


def test_a_lock_that_parses_to_ZERO_pins_refuses_rather_than_passing(
    tmp_path: Path,
) -> None:
    """The one that would otherwise be silent. An empty or reformatted lock makes the
    comparison true on any environment at all, which is worse than no check -- and it is
    the exact shape `check_carried`'s own zero-findings guard exists for."""
    at = tmp_path / "comments-only.txt"
    at.write_text("# nothing but a comment\n\n", encoding="utf-8")
    with pytest.raises(SystemExit) as caught:
        fse.refuse_unless_locked(at, doing="export")
    message = str(caught.value)
    assert "parsed to ZERO pins" in message
    assert "worse than no check" in message


# ---------------------------------------------------------------------------
# The worktree the import actually came from
# ---------------------------------------------------------------------------


def test_a_floatsim_inside_the_declared_worktree_is_accepted(tmp_path: Path) -> None:
    declared = tmp_path / "HSP-runs"
    (declared / "floatsim").mkdir(parents=True)
    (declared / "floatsim" / "__init__.py").write_text("", encoding="utf-8")
    fse.refuse_unless_declared_worktree(declared / "floatsim" / "__init__.py", declared=declared)


def test_a_floatsim_from_ANOTHER_checkout_refuses_and_names_both_trees(
    tmp_path: Path,
) -> None:
    """The measured case, in its real shape: two sibling checkouts of the same repository,
    one pinned and one a working tree, and an editable install pointing at the second."""
    declared = tmp_path / "HSP-runs"
    other = tmp_path / "HSP_code"
    for at in (declared, other):
        (at / "floatsim").mkdir(parents=True)
        (at / "floatsim" / "__init__.py").write_text("", encoding="utf-8")
    with pytest.raises(SystemExit) as caught:
        fse.refuse_unless_declared_worktree(other / "floatsim" / "__init__.py", declared=declared)
    message = str(caught.value)
    assert "imported from outside the declared worktree" in message
    assert "HSP_code" in message
    assert "HSP-runs" in message
    assert hsp_pin.HSP_TAG in message


def test_the_check_is_on_CONTAINMENT_and_not_on_a_name(tmp_path: Path) -> None:
    """A sibling whose path merely STARTS with the declared one -- `HSP-runs-old` beside
    `HSP-runs` -- is outside it. A `str.startswith` check would accept it, which is why
    the implementation asks whether the declared root is among the file's parents."""
    declared = tmp_path / "HSP-runs"
    lookalike = tmp_path / "HSP-runs-old"
    for at in (declared, lookalike):
        (at / "floatsim").mkdir(parents=True)
        (at / "floatsim" / "__init__.py").write_text("", encoding="utf-8")
    with pytest.raises(SystemExit):
        fse.refuse_unless_declared_worktree(
            lookalike / "floatsim" / "__init__.py", declared=declared
        )


# ---------------------------------------------------------------------------
# What reaches the provenance
# ---------------------------------------------------------------------------


def test_the_record_carries_the_path_and_the_lock_hash_GJ1_asks_for(
    tmp_path: Path,
) -> None:
    at = tmp_path / "lock.txt"
    at.write_bytes(LOCK_TEXT.encode("utf-8"))
    lock = fse.parse_lock(LOCK_TEXT)
    got = fse.record(lock_file=at, lock=lock, floatsim_file=tmp_path / "f" / "__init__.py")
    assert got["interpreter"].endswith(("python.exe", "python"))  # type: ignore[union-attr]
    assert got["lock"] == {  # type: ignore[comparison-overlap]
        "path": str(at),
        "sha256": fse.lock_sha256(at),
        "pins": 5,
        "editables_not_installed": fse.editables(LOCK_TEXT),
    }
    # **AND THIS ASSERTION IS MADE DETERMINISTIC RATHER THAN LEFT TO THE INTERPRETER.**
    # The first version asserted `False` against `LOCK_TEXT` with the comment "numpy 2.4.4
    # is not what THIS one has" -- which is true in the dev venv and FALSE in the locked
    # one GJ1 builds, where every pin above is satisfied. A test whose answer depends on
    # which of this repository's two environments runs it measures the environment, not the
    # code, and the pair of them would have disagreed the first time CI ran under the lock.
    unsatisfiable = tmp_path / "unsatisfiable.txt"
    unsatisfiable.write_text("floatfea-no-such-dist==1.0\n", encoding="utf-8")
    assert (
        fse.record(
            lock_file=unsatisfiable,
            lock=fse.parse_lock(unsatisfiable.read_text(encoding="utf-8")),
        )["pins_satisfied"]
        is False
    )
    assert "floatsim" in got


def test_pins_satisfied_is_a_MEASUREMENT_and_not_a_constant(tmp_path: Path) -> None:
    """The inverted direction for the field above: on a lock this interpreter satisfies it
    must read True, or the field is decoration."""
    at = _satisfied_lock(tmp_path)
    lock = fse.parse_lock(at.read_text(encoding="utf-8"))
    assert fse.record(lock_file=at, lock=lock)["pins_satisfied"] is True
