"""The sentence a bit-exact refusal prints beside its count of differing arrays.

**WHY IT IS TESTED RATHER THAN TRUSTED.** It was written inline in `main()`, in the branch
that only runs when `--check` finds a difference -- a path that costs 25 minutes of FloatSim
to reach, so nothing would have exercised it before a reader did. Twenty-five lines of
message-building shipping unread is the shape `CLAUDE.md` calls prose that states a fact
about the code: a test, a triple, or deleted. This is the test.

**WHAT IT HAS TO SAY, AND WHY.** R2 step 1 measured two conditions that move the
comparison and neither is in the arrays being compared: the thread count and the library
versions. The committed sidecar records neither -- it predates R1225(ii)'s `environment`
block -- so the refusal has to distinguish "the file records them, go and compare" from
"the file records neither, so this difference cannot be attributed".
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "measure"))


@pytest.fixture
def note():  # type: ignore[no-untyped-def]
    """Imported late, because the module inserts paths at import time."""
    import export_f4_dynamic_inputs as ex

    return ex.sensitivity_note


def test_a_sidecar_WITHOUT_an_environment_block_is_named_as_recording_NEITHER(
    note, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The committed file's case, and the one a reader meets today."""
    at = tmp_path / "p.json"
    at.write_text(json.dumps({"hsp_tag": "floatfea-ref-1  (HSP-runs)"}), encoding="utf-8")
    monkeypatch.setenv("OMP_NUM_THREADS", "1")
    got = note(at)
    assert "RECORDS NEITHER" in got
    assert "'OMP_NUM_THREADS': '1'" in got
    assert "FQ3" in got


def test_a_sidecar_WITH_one_is_named_as_recording_them(note, tmp_path: Path) -> None:
    """The inverted direction. A file written since R1225(ii) carries the block, and the
    refusal should send a reader to it rather than telling them it is absent."""
    at = tmp_path / "p.json"
    at.write_text(
        json.dumps({"environment": {"threads": {"OMP_NUM_THREADS": "1"}}}), encoding="utf-8"
    )
    got = note(at)
    assert "RECORDS NEITHER" not in got
    assert "records an `environment` block" in got


def test_an_ABSENT_or_UNREADABLE_sidecar_does_not_raise(note, tmp_path: Path) -> None:
    """A refusal that raises while explaining a refusal is a traceback where a sentence
    should be -- FO1's defect, one file type over. Both shapes reach the same honest
    answer: nothing is recorded."""
    assert "RECORDS NEITHER" in note(tmp_path / "nothing-here.json")
    bad = tmp_path / "bad.json"
    bad.write_bytes(b"\xff\xfe not json at all")
    assert "RECORDS NEITHER" in note(bad)


def test_the_note_reports_THIS_process_rather_than_a_remembered_configuration(
    note, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The whole point is attribution, so the line has to describe the run that printed
    it. Two environments, two different lines, nothing else moved."""
    at = tmp_path / "p.json"
    at.write_text("{}", encoding="utf-8")
    monkeypatch.setenv("OMP_NUM_THREADS", "1")
    monkeypatch.setenv("OPENBLAS_CORETYPE", "Haswell")
    pinned = note(at)
    monkeypatch.delenv("OMP_NUM_THREADS")
    monkeypatch.delenv("OPENBLAS_CORETYPE")
    unpinned = note(at)
    assert pinned != unpinned
    assert "'OMP_NUM_THREADS': None" in unpinned
    assert "OPENBLAS_CORETYPE None" in unpinned


# ---------------------------------------------------------------------------
# What the written file calls itself in its own sidecar
# ---------------------------------------------------------------------------


@pytest.fixture
def recorded():  # type: ignore[no-untyped-def]
    import export_f4_dynamic_inputs as ex

    return ex._recorded_path


def test_a_file_UNDER_the_repository_root_names_itself_relatively(recorded) -> None:
    """The committed sidecar's own field, which must not move: it has always read
    `data/f4/dynamic_inputs.npz` and a repository-relative POSIX path is what produces
    it."""
    assert recorded(ROOT / "data" / "f4" / "dynamic_inputs.npz") == ("data/f4/dynamic_inputs.npz")


def test_a_file_OUTSIDE_it_names_itself_absolutely(recorded, tmp_path: Path) -> None:
    """R2 step 1's `--out` made the destination configurable, and this field was a
    LITERAL `"data/f4/dynamic_inputs.npz"` -- true for as long as that was the only
    place the script could write. An export anywhere else would have shipped a sidecar
    naming a file it is not beside: a record saying something other than what happened,
    which is FR1's second head inside the provenance itself.

    The inverted direction matters as much as the forward one: a relative path computed
    against a root the file is not under is not a path to anything, so the absolute one
    is the only honest answer."""
    at = tmp_path / "elsewhere" / "dynamic_inputs.npz"
    at.parent.mkdir()
    at.write_bytes(b"")
    got = recorded(at)
    assert got == str(at.resolve())
    assert not got.startswith("data/f4")


# ---------------------------------------------------------------------------
# A committed golden is not overwritten without saying so
# ---------------------------------------------------------------------------


@pytest.fixture
def tracked():  # type: ignore[no-untyped-def]
    import export_f4_dynamic_inputs as ex

    return ex._is_tracked


def test_the_COMMITTED_golden_reads_as_tracked(tracked) -> None:
    """The file the refusal exists for. `floatfea export` on the shipped export
    configuration targets the committed location -- that is what makes `--check` compare
    against the golden -- so without the refusal, leaving off `--check` silently
    re-baselines the file FQ3 has a live escalation about."""
    assert tracked(ROOT / "data" / "f4" / "dynamic_inputs.npz") is True


def test_a_path_OUTSIDE_the_repository_does_not(tracked, tmp_path: Path) -> None:
    """A scratch export must not be refused: the question is "is this committed", not
    "is this called dynamic_inputs.npz"."""
    at = tmp_path / "dynamic_inputs.npz"
    at.write_bytes(b"")
    assert tracked(at) is False


def test_an_UNTRACKED_file_INSIDE_the_repository_does_not_either(tracked, tmp_path: Path) -> None:
    """The case a path-shaped guess would get wrong. A new destination under the
    repository root is untracked until somebody commits it, and exporting into one is
    ordinary work -- so the check is `git ls-files --error-unmatch` and not a prefix
    test on `data/`."""
    at = ROOT / "tmp_untracked_probe.npz"
    at.write_bytes(b"")
    try:
        assert tracked(at) is False
    finally:
        at.unlink()


# ---------------------------------------------------------------------------
# The write path, with an out-of-tree `--out`
# ---------------------------------------------------------------------------


def test_an_OUT_OF_TREE_out_writes_BOTH_files_and_records_the_real_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """**THE CRASH `--out` SHIPPED WITH, AND NO UNIT TEST REACHED IT.**

    `--out` was added in R2 step 1 and the npz-written line still read
    `target.relative_to(ROOT)`, which RAISES for a path outside the repository. Measured by
    running the real command: a 26-minute export into a scratch directory wrote the npz,
    raised on that line, and never reached the provenance -- so `floatfea run` on the result
    published "wave basis: NOT RECORDED" in both CSVs and in the report. The arrays were
    fine and the record beside them did not exist, which is the worse of the two failures.

    The flag's other tests stop at the argv the engine is HANDED. This one drives the
    engine's own write path with the solve replaced, which is the only part that has to be
    fast; everything after `export_case` is exercised for real, including the provenance.
    """
    import export_f4_dynamic_inputs as ex
    import numpy as np

    case = {
        "period_full_s": 10.0,
        "times": np.zeros(2),
        "base": np.zeros((2, 3)),
        "dt": 0.01,
    }
    monkeypatch.setattr(ex, "export_case", lambda period, dt: dict(case))
    monkeypatch.setattr(ex, "_hsp_tag", lambda: "floatfea-ref-1  (test)")
    monkeypatch.setattr(ex, "_import_closure_shas", dict)
    monkeypatch.setattr(ex.floatsim_env, "lock_path", lambda *a, **k: tmp_path / "lock.txt")
    monkeypatch.setattr(ex.floatsim_env, "refuse_unless_locked", lambda *a, **k: {"numpy": "0"})
    monkeypatch.setattr(ex.floatsim_env, "record", lambda **k: {"interpreter": "test"})
    monkeypatch.setitem(sys.modules, "floatsim", type("m", (), {"__file__": __file__}))

    out = tmp_path / "elsewhere"
    assert ex.main(["--out", str(out), "--period", "10"]) == 0

    npz = out / "dynamic_inputs.npz"
    prov = out / "dynamic_inputs.provenance.json"
    assert npz.is_file(), "the arrays were not written"
    assert prov.is_file(), (
        "the npz was written and the PROVENANCE was not. That is the shape this test "
        "exists for: a run whose arrays are fine and whose record beside them is absent "
        "publishes 'wave basis: NOT RECORDED' downstream."
    )
    recorded = json.loads(prov.read_text(encoding="utf-8"))["npz"]["path"]
    assert recorded == str(npz.resolve()), (
        "the sidecar must name the file it is beside. A literal `data/f4/...` here would "
        "name a file this one is not beside, which is FR1's second head in the provenance."
    )
