"""The locked environment every FloatSim invocation runs under (GJ1).

GJ1 ruled the FQ3 escalation: **restore the lock, do not re-base.** Its three clauses
are what this module implements.

* *"Build the FloatSim run environment from `HSP-runs/requirements-lock.txt` exactly
  (a separate venv is fine)."* — `venv()` resolves where that venv is and
  `interpreter()` the Python inside it, by the same decision table as
  `hsp_pin.worktree`.
* *"Every FloatSim invocation by FloatFEA uses that environment"* —
  `refuse_unless_locked()` is the preflight, run **inside** the invoking process, which
  refuses rather than correcting itself. See SR-76: a re-exec would mean the process
  reporting the result is not the process the user started, and a silently corrected
  environment is indistinguishable in its output from one that was right to begin with.
  That is the exact shape FQ3 exists against.
* *"FloatFEA records its path and lock hash in each run's provenance."* — `record()`.

**WHY A LOCKED ENVIRONMENT IS A CORRECTNESS CONCERN AND NOT HOUSEKEEPING.** The
committed `data/f4/dynamic_inputs.npz` stopped regenerating bit-identically when
`constraints-dev.txt` moved numpy `2.4.4 -> 2.5.4` and scipy `1.17.1 -> 1.18.1`
(`09d5bc9`): 36 of 100 arrays differed while all 64 INPUT arrays stayed bit-identical
and the HSP worktree stayed at `floatfea-ref-1`. FQ3's standing ruling is "if the golden
moves under these pins, STOP and report rather than re-baselining", so the gate was left
red and escalated. GJ1 is the answer to that escalation.

**AND THE SECOND THING THE VENV FIXES, WHICH THE ESCALATION HAD NOT SEEN.** The system
interpreter carries an *editable install* of `floatsim` pointing at a working checkout
121 commits past the pin. Its finder sits after `PathFinder` in `sys.meta_path`, so which
FloatSim answers an import depends on whether the pinned worktree was put on `sys.path`
first — call order, not any declaration. Nine source files differ between the two trees
and one of them is the radiation convolution. A venv built from the lock alone has no
`floatsim` at all, so there is no second tree for a call-order change to reach:
`refuse_unless_declared_worktree()` is what makes the remaining case loud.
`docs/milestones/R2.md` §7 carries the measurements.
"""

from __future__ import annotations

import hashlib
import importlib.metadata as md
import os
import re
import sys
from pathlib import Path
from typing import Final

from floatfea import hsp_pin

VENV_ENV: Final[str] = "FLOATFEA_FLOATSIM_VENV"
"""Where the locked venv is, if it is not the default below."""

DEFAULT_VENV: Final[str] = ".venv-floatsim"
"""The default, a sibling of this package inside the repository root.

Gitignored, exactly as the HSP worktrees are untracked: it is machine state built from a
tracked lock, so what belongs in the repository is the resolution and the record, not the
tree. `.gitignore` carries that sentence too.
"""

LOCK_NAME: Final[str] = "requirements-lock.txt"
"""The lock's name inside the pinned runs worktree. GJ1 names that file specifically.

It is read from the WORKTREE and never copied here. A copy is a second reader of the same
predicate, and it would go stale silently the moment HSP re-locked — which is R2 step 0's
one recurring defect shape, five times over.
"""

_PIN = re.compile(r"^(?P<name>[A-Za-z0-9._-]+)==(?P<version>[^\s;#]+)\s*$")
_EDITABLE = re.compile(r"^\s*-e\s")


def venv(declared: Path | str | None = None, *, require: bool = False) -> Path:
    """The locked venv's directory.

    Order, and the refusal rules, are `hsp_pin.resolve_declared_path`'s: a source that is
    set and wrong REFUSES rather than falling through (R1214), a relative value anchors
    to the repository root rather than the cwd (R1219), and only the implicit default
    falls through when `require` is false.

    `require=False` is the default for the same reason it is in `hsp_pin.worktree`: this
    is importable on a machine with no venv built — CI, by design — and an import that
    raises there takes the whole module with it (R670).
    """
    return hsp_pin.resolve_declared_path(
        what="FloatSim run environment",
        what_require="locked FloatSim run environment (GJ1)",
        declared=declared,
        declared_source="declared (floatsim.venv)",
        env_name=VENV_ENV,
        fallback=_repo_root() / DEFAULT_VENV,
        fallback_source=f"the default {DEFAULT_VENV} in the repository root",
        require=require,
        exists=Path.is_dir,
        noun="a directory",
        hint=(
            f"Build it from the pinned worktree's {LOCK_NAME} (GJ1), or set ${VENV_ENV} "
            f"to one that is already built."
        ),
    )


def interpreter(declared: Path | str | None = None, *, require: bool = False) -> Path:
    """The Python inside the locked venv.

    **THE LAYOUT IS BRANCHED ON `os.name`, NOT ON WHICH FILE HAPPENS TO EXIST.** Probing
    for `Scripts/python.exe` and falling back to `bin/python` would silently pick the
    wrong one in a tree that has both — a venv copied between platforms, which is exactly
    the state a lock is supposed to make detectable. A declared venv that does not carry
    the interpreter for THIS platform is a refusal under `require`, not a different
    interpreter.
    """
    root = venv(declared, require=require)
    got = (
        root
        / ("Scripts" if os.name == "nt" else "bin")
        / ("python.exe" if os.name == "nt" else "python")
    )
    if require and not got.is_file():
        raise SystemExit(
            f"REFUSED: the FloatSim run environment at {root} carries no interpreter for "
            f"this platform.\n"
            f"  looked for {got}\n"
            f"GJ1 asks for a venv built from the pinned worktree's {LOCK_NAME}. A "
            f"directory that is not one is not silently substituted."
        )
    return got


def lock_path(runs_worktree: Path | None = None) -> Path:
    """The lock GJ1 names, inside the pinned runs worktree."""
    runs = runs_worktree if runs_worktree is not None else hsp_pin.worktree("runs")
    return runs / LOCK_NAME


def lock_sha256(path: Path) -> str:
    """The lock's `sha256`, which is what GJ1 asks be recorded in the provenance.

    Read as BYTES. A text read would normalise line endings, so the same lock would hash
    differently on two platforms and the recorded hash would stop identifying the file.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_lock(text: str) -> dict[str, str]:
    """`name -> version` for every `name==version` line. Editables are not included.

    The canonical-name key is lower-cased with runs of `[-_.]` collapsed to `-`, which is
    PEP 503 normalisation. Without it `types-PyYAML` and `typing_extensions` would not
    match what `importlib.metadata` reports, and the comparison would read two spurious
    mismatches on a correct environment — a check that cries wolf gets deleted.
    """
    out: dict[str, str] = {}
    for line in text.splitlines():
        found = _PIN.match(line.strip())
        if found:
            out[canonical(found["name"])] = found["version"]
    return out


def editables(text: str) -> list[str]:
    """Every `-e ...` line of the lock, verbatim.

    They are reported rather than installed, and SR-75 is why: the lock's one editable is
    `-e git+https://github.com/xabi80/HSP.git@928ae474...#egg=floatsim`, and `928ae474` is
    an ANCESTOR of the pin `25de7ce`. Installing it as written would put FloatSim at a
    state that is not the pin, from the network, in a fourth checkout — breaking the GI1
    constraint the environment exists to serve. FloatSim comes from the pinned worktree on
    `sys.path` instead. No version is substituted: the same package, at a strictly more
    pinned state.
    """
    return [line.strip() for line in text.splitlines() if _EDITABLE.match(line)]


def canonical(name: str) -> str:
    """PEP 503 normalisation, so `types-PyYAML` and `types_pyyaml` are one key."""
    return re.sub(r"[-_.]+", "-", name).lower()


def installed(names: list[str] | None = None) -> dict[str, str | None]:
    """What THIS interpreter has, for each requested distribution.

    In-process on purpose. The preflight runs inside the process that is about to import
    FloatSim, so the only environment whose answer matters is its own; asking a
    subprocess would measure a different one.
    """
    want = names if names is not None else []
    out: dict[str, str | None] = {}
    for name in want:
        try:
            out[name] = md.version(name)
        except md.PackageNotFoundError:
            out[name] = None
    return out


def mismatches(lock: dict[str, str]) -> list[tuple[str, str, str | None]]:
    """`(name, wanted, got)` for every pin this interpreter does not satisfy.

    `got` is `None` for a distribution that is absent, and the two cases are kept apart in
    the message rather than merged into "wrong": a missing package and a wrong version
    have different repairs.
    """
    have = installed(sorted(lock))
    return [
        (name, wanted, have.get(name))
        for name, wanted in sorted(lock.items())
        if have.get(name) != wanted
    ]


def refuse_unless_locked(lock_file: Path, *, doing: str) -> dict[str, str]:
    """Refuse unless THIS interpreter satisfies every pin in `lock_file`.

    Returns the parsed lock so the caller can record it. `doing` names the action in the
    message, because a refusal that does not say what it stopped is a refusal someone
    works around.

    **IT REFUSES; IT DOES NOT RE-EXEC (SR-76).** GJ1 requires every FloatSim invocation to
    use the locked environment, and two mechanisms satisfy that sentence. A re-exec is the
    more convenient and the less honest: the process reporting the result would not be the
    process the user started, and a run whose environment was silently corrected is
    indistinguishable in its output from one that was right to begin with.

    **AND IT COMPARES THE INSTALLED SET, NOT THE LOCK'S HASH.** A hash says the file on
    disk has not changed; it says nothing about the interpreter that is running. The
    defect FQ3 was adopted for was exactly an interpreter that had drifted from a lock
    nobody re-read, so the check that matters is `version(x) == lock[x]`, distribution by
    distribution.
    """
    if not lock_file.is_file():
        raise SystemExit(
            f"REFUSED: cannot {doing} -- the lock {lock_file} does not exist.\n"
            f"GJ1 builds the FloatSim run environment from the pinned worktree's "
            f"{LOCK_NAME}, so without it there is nothing to check this interpreter "
            f"against, and an unchecked environment is what FQ3 was adopted against."
        )
    lock = parse_lock(lock_file.read_text(encoding="utf-8", errors="replace"))
    if not lock:
        raise SystemExit(
            f"REFUSED: cannot {doing} -- {lock_file} parsed to ZERO pins.\n"
            f"An empty lock would make this check pass on any environment at all, which "
            f"is worse than no check. The file exists, so its FORMAT changed."
        )
    bad = mismatches(lock)
    if bad:
        lines = "".join(
            f"  {name}: lock {wanted}, this interpreter " f"{'ABSENT' if got is None else got}\n"
            for name, wanted, got in bad
        )
        raise SystemExit(
            f"REFUSED: cannot {doing} -- this interpreter does not satisfy "
            f"{len(bad)} of the lock's {len(lock)} pins.\n"
            f"{lines}"
            f"  interpreter {sys.executable}\n"
            f"  lock        {lock_file}\n"
            f"GJ1: every FloatSim invocation by FloatFEA runs under an environment built "
            f"from that lock exactly. This is a refusal and not a correction (SR-76): a "
            f"run whose environment was silently fixed up reads exactly like one that was "
            f"right to begin with. Build the venv from the lock and re-run under "
            f"{interpreter()}."
        )
    return lock


def refuse_unless_declared_worktree(module_file: Path | str, *, declared: Path) -> None:
    """Refuse unless the imported `floatsim` came from the worktree that was declared.

    **THIS IS THE DEFECT MADE LOUD, NOT A BELT-AND-BRACES CHECK.** Measured in the system
    interpreter: a bare `import floatsim` resolves to a checkout 121 commits past the pin,
    and the same import with the pinned worktree on `sys.path` first resolves to the pin.
    The editable install's finder sits AFTER `PathFinder` in `sys.meta_path`, so the
    answer is a property of call order. Nine source files differ between the two trees,
    one of them the radiation convolution, which the npz path imports directly.

    No published number came from the wrong tree, because in every real run the solve
    imports first. **A guarantee that holds by call order is FR1's second head: an input
    accepted and used other than as declared.** This turns it into a refusal.
    """
    got = Path(module_file).resolve()
    want = Path(declared).resolve()
    if want not in got.parents:
        raise SystemExit(
            f"REFUSED: `floatsim` was imported from outside the declared worktree.\n"
            f"  imported from {got}\n"
            f"  declared      {want}  (tag {hsp_pin.HSP_TAG}, {hsp_pin.HSP_COMMIT})\n"
            f"GI1 authorises running FloatSim from the PINNED worktree. Which tree answers "
            f"an import depends on whether that worktree was put on `sys.path` before the "
            f"first import, so this is checked rather than assumed. A locked venv built "
            f"from {LOCK_NAME} alone carries no `floatsim`, which removes the fallback "
            f"this refusal exists to catch."
        )


def record(
    *,
    lock_file: Path,
    lock: dict[str, str],
    floatsim_file: Path | str | None = None,
) -> dict[str, object]:
    """The provenance block GJ1 asks for: the environment's path and the lock's hash.

    Recorded, and separately asserted by `refuse_unless_locked`. R1225 is why both: a
    bit-exactness gate was deciding whether an artifact is believed while the conditions
    its answer depends on appeared nowhere in the artifact. Recording without asserting
    repeats that; asserting without recording leaves a reader unable to see what was
    asserted.
    """
    out: dict[str, object] = {
        "interpreter": str(Path(sys.executable).resolve()),
        "venv": str(venv()),
        "lock": {
            "path": str(lock_file),
            "sha256": lock_sha256(lock_file),
            "pins": len(lock),
            "editables_not_installed": editables(
                lock_file.read_text(encoding="utf-8", errors="replace")
            ),
        },
        "pins_satisfied": not mismatches(lock),
    }
    if floatsim_file is not None:
        out["floatsim"] = str(Path(floatsim_file).resolve())
    return out


def _repo_root() -> Path:
    """This repository's root, from this file's own location."""
    return Path(__file__).resolve().parents[1]
