"""DV0: export the 12-buoy platform deck from HSP to a YAML this repository reads.

WHY THIS EXISTS. F3's DJ1 originally sourced the layout from "HSP's model-definition
YAML". There is no such file -- the 12-buoy deck is built in Python, and verdict 69's
R576 STOPped F3 on it. DV0 re-locks the source as a GENERATED YAML, and this is the
generator.

WHAT THE PROPERTY WAS, AND WHY GENERATING IS STRONGER THAN FINDING. DJ1's rule is
"no coordinate is typed into this repository". A YAML checked in by hand satisfies
that rule on the day it is written and can drift from the deck silently ever after.
A file that only this script writes cannot: re-run it and any drift is a diff.

THE ROUND TRIP IS THE CHECK, and it runs here rather than only in a test, because a
file that does not reproduce its source must never be written in the first place.
`Deck.model_validate` on the emitted YAML must reproduce the source deck's dump
exactly, field for field. If it does not, this script writes nothing and says so.

WHAT IT DOES NOT DO. It does not scale. The deck is at MODEL scale and the YAML
says so on its face; `floatfea.io.froude` is the only thing that changes scale, at
the I/O boundary, and `floatfea.io.reader` refuses a model-scale record that has not
been through it.

    python scripts/export_platform_deck.py            # write the YAML
    python scripts/export_platform_deck.py --check    # verify, write nothing
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Final

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from floatfea import hsp_pin  # noqa: E402

HSP_RUNS = ROOT.parent / "HSP-runs"
STUDY = HSP_RUNS / "studies" / "platform-12buoy"
OUT = ROOT / "data" / "platform" / "platform12_deck.yaml"
_IMPORT_DIRS = (
    "studies/platform-12buoy",
    "studies/cluster-3buoy-rigid",
)
"""The directories `build_deck` puts on `sys.path`. Kept beside the preflight so
the refusal and the insertion cannot drift apart (R588)."""
DIGEST = ROOT / "tests" / "goldens" / "platform_deck_digest.txt"


def _git(*args: str, cwd: Path) -> str:
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed in {cwd}: {out.stderr.strip()}")
    return out.stdout.strip()


def _preflight() -> str:
    """Refuse to export from anything but the pinned tag, and never from HSP-stable.

    DS0: `../HSP-stable` is read-only from FloatFEA and runs happen in `../HSP-runs`.
    The pin exists so that a model exported today and a model exported next month
    are the same model; exporting from a moving worktree would make the YAML a
    snapshot of whatever HSP happened to be that afternoon.
    """
    if not HSP_RUNS.is_dir():
        raise SystemExit(f"{HSP_RUNS} is not a directory; the runs worktree is missing")
    resolved = HSP_RUNS.resolve()
    if resolved.name == "HSP-stable" or "HSP-stable" in resolved.parts:
        raise SystemExit("refusing to export from HSP-stable, which is read-only (DS0)")

    described = _git("describe", "--tags", "--always", cwd=HSP_RUNS)
    head = _git("rev-parse", "--short", "HEAD", cwd=HSP_RUNS)
    if not described.startswith(hsp_pin.HSP_TAG):
        raise SystemExit(
            f"{HSP_RUNS} is at {described!r} (HEAD {head}), not at the pinned tag "
            f"{hsp_pin.HSP_TAG!r}. A deck exported from an unpinned worktree is a "
            "model nobody can reproduce."
        )
    if not head.startswith(hsp_pin.HSP_COMMIT) and not hsp_pin.HSP_COMMIT.startswith(head):
        raise SystemExit(f"{HSP_RUNS} HEAD is {head}, the pin records {hsp_pin.HSP_COMMIT}")

    # R584. THE TAG AND THE COMMIT ARE NOT ENOUGH, and the gap was silent. A
    # worktree can sit exactly at the pin and have modified tracked files, in which
    # case the deck exported is NOT the deck at that tag -- and the header would name
    # the tag anyway, which is the worst of the three outcomes: a file that misstates
    # its own provenance. `--porcelain` is empty only when tracked files match HEAD
    # and nothing is staged.
    dirty = _git("status", "--porcelain", "--untracked-files=no", cwd=HSP_RUNS)
    if dirty:
        raise SystemExit(
            f"{HSP_RUNS} is at the pin but its worktree is DIRTY:\n{dirty}\n"
            "The deck built from it is not the deck at "
            f"{hsp_pin.HSP_TAG}, and the header would name that tag regardless. "
            "Commit, stash or revert there first."
        )

    # R588. THE SENTENCE THAT USED TO BE HERE SAID UNTRACKED FILES "cannot change
    # what the study imports", AND IT WAS FALSE. `build_deck` puts three directories
    # on `sys.path` and the study imports `platform_common` and `cluster_common` as
    # BARE NAMES, so an untracked `platform_common.py` in the directory inserted last
    # -- and therefore searched first -- is imported in preference to the tracked one,
    # with `--untracked-files=no` reporting a clean worktree throughout. The flag was
    # doing the work of a threshold, which is why this is a gate finding and not a
    # tidy-up.
    #
    # Untracked files ELSEWHERE still cannot affect the import, so the refusal is
    # scoped to the directories that go on `sys.path` and to `.py` files, rather than
    # refusing on any stray file in a large worktree.
    shadowing = [
        line
        for line in _git(
            "status", "--porcelain", "--untracked-files=all", cwd=HSP_RUNS
        ).splitlines()
        if line.startswith("??")
        and line.strip().endswith(".py")
        and any(part in line for part in _IMPORT_DIRS)
    ]
    if shadowing:
        listed = "\n".join(shadowing)
        raise SystemExit(
            f"{HSP_RUNS} is at the pin and tracked-clean, but carries UNTRACKED "
            f"Python modules on the import path:\n{listed}\n"
            "The study imports `platform_common` and `cluster_common` by bare name "
            "from these directories, so an untracked module of the same name is "
            "imported in preference to the tracked one and the deck exported is not "
            "the deck at the pin. Remove them or commit them."
        )
    return head


PLATFORM_OVERRIDE: Final[dict[str, Any]] = {
    "mass": 20.0,
    "inertia": {"Ixx": 20.0, "Iyy": 20.0, "Izz": 40.0},
}
"""ER0's platform mass and inertia, at MODEL scale, applied to the exported deck (ER1(a)).

**IT IS DECLARED HERE AND STATED ON THE DECK'S FACE**, so the generated file says what it
is and `--check` compares HSP-stable's own deck PLUS this override against what is on
disk. Setting it to `{}` exports HSP's deck unmodified.

WHAT IT OVERRIDES: `platform_common.py:177-178`, `mass=PLATFORM_MASS` and
`Inertia(Ixx=10.0, Iyy=10.0, Izz=20.0)`.

WHY AN OVERRIDE AT ALL. ER0 is Xabier's input for this platform and HSP is not forked:
HSP-stable stays read-only at the pinned tag (DS0), FloatSim's own study keeps its own
numbers, and the change belongs where this repository assembles its input. The replay
driver applies the same override in memory (`scripts/report_joint_reactions.py`), so the
FE side and the FloatSim runs see one basis.

ER0(a) records that the inertia scaling is an ASSUMPTION Xabier marked overridable:
`20, 20, 40` is `10, 10, 20` scaled with the mass. ER0(b) leaves the reference point
alone.

not-a-tolerance: a mass and three inertias, the physical inputs ER0 sets. Nothing is
compared against them.
"""


def apply_override(deck: Any) -> list[str]:
    """Apply `PLATFORM_OVERRIDE` in place. Returns one line per value that moved."""
    if not PLATFORM_OVERRIDE:
        return []
    body = next(b for b in deck.bodies if b.name == "platform")
    moved: list[str] = []
    before_mass = body.mass
    body.mass = float(PLATFORM_OVERRIDE["mass"])
    moved.append(f"platform mass {before_mass:g} -> {body.mass:g} kg (model)")
    for axis, value in PLATFORM_OVERRIDE["inertia"].items():
        before = getattr(body.inertia, axis)
        setattr(body.inertia, axis, float(value))
        moved.append(f"platform {axis} {before:g} -> {float(value):g} kg*m^2 (model)")
    return moved


def build_deck() -> Any:
    """Import the pinned study, apply the declared override, return its Deck.

    Read-only on HSP: the override is applied to the Deck OBJECT this function returns,
    never to anything under `../HSP-stable` or `../HSP-runs`.
    """
    for path in (HSP_RUNS, STUDY, STUDY.parent / "cluster-3buoy-rigid"):
        sys.path.insert(0, str(path))
    import platform_rao_pilot as prp

    deck = prp._deck_with_drag()
    apply_override(deck)
    return deck


def dump_and_verify(deck: Any) -> tuple[str, dict[str, Any]]:
    """Serialise, re-validate, and compare. Returns the YAML text and the dump."""
    from floatsim.io.deck import Deck

    source = deck.model_dump(mode="json")
    text = yaml.safe_dump(source, sort_keys=False, default_flow_style=False)
    back = Deck.model_validate(yaml.safe_load(text)).model_dump(mode="json")
    if back != source:
        differing = sorted(k for k in set(source) | set(back) if source.get(k) != back.get(k))
        raise SystemExit(
            "THE ROUND TRIP DOES NOT REPRODUCE THE DECK and nothing is written. "
            f"Top-level keys that differ: {differing}. A YAML that does not "
            "re-validate to its source is not a model definition, it is a lossy "
            "copy of one."
        )
    return text, source


def digest(raw: dict[str, Any], body: str = "") -> str:
    """The committed fingerprint of the deck's CONTENT and its ORDER (R583).

    Two lines, because neither implies the other:

    * `content_sha256` over canonical JSON (`sort_keys=True`) catches any changed
      VALUE -- a moved coordinate, a scaled mass, a `.nan` -- and is blind to
      reordering by construction, which is exactly why the second line exists.
    * `body_order` and `joint_order` are the sequences as the FILE carries them, so
      a dropped or swapped body reddens by name rather than as an opaque hash.
    * `body_sha256` is over the document's text with **newlines normalised to LF**,
      and it is the only line that can see a mapping re-emitted with
      `sort_keys=True`. It does NOT see a line-ending change: `Path.read_text`
      translates CRLF to LF on the way in, so a file rewritten with CRLF hashes
      identically (R589). That is deliberate rather than a gap -- `core.autocrlf`
      rewrites line endings on checkout, and a digest that noticed would fail on
      every Windows clone -- but the first version of this sentence said "AS
      EMITTED" and the assertion's message said "bytes", and a reader would have
      believed both. Two earlier attempts at the ordering case could not see it
      either:
      the content hash is order-blind by construction, and a test that re-emits the
      file's OWN parsed content always reproduces it, because `safe_load` hands the
      keys back in the order the file listed them. A RECORDED hash is the only side
      of that comparison the file cannot supply itself.

    THIS EXISTS BECAUSE THE GATE IT REPLACES CERTIFIED NOTHING. G3.2's
    environment-independent half was a parse-and-re-emit comparison, which is green
    on any file that parses -- measured green on 11 of 11 injected mutations,
    including the reordering its own docstring claimed to catch. A round trip of a
    file against itself is a statement about the YAML library.

    Written by the generator rather than by a test, so the figures are produced at
    the commit that publishes them (BI3).
    """
    canonical = json.dumps(raw, sort_keys=True, separators=(",", ":"))
    bodies = [b["name"] for b in raw["bodies"]]
    joints = [f"{j['body_a']}>{j['body_b']}" for j in raw["joints"]]
    return (
        "# GENERATED BY scripts/export_platform_deck.py -- DO NOT HAND-EDIT.\n"
        "#\n"
        "# A golden under CLAUDE.md section Testing: changing these figures requires a\n"
        "# written explanation of why the deck moved. Regenerating it to match new\n"
        "# output without that explanation is the same error as widening a tolerance.\n"
        f"content_sha256={hashlib.sha256(canonical.encode()).hexdigest()}\n"
        f"body_sha256={hashlib.sha256(body.encode()).hexdigest()}\n"
        f"canonical_bytes={len(canonical)}\n"
        f"bodies={len(bodies)}\n"
        f"joints={len(joints)}\n"
        f"body_order={','.join(bodies)}\n"
        f"joint_order={','.join(joints)}\n"
    )


def _override_lines() -> list[str]:
    """`PLATFORM_OVERRIDE` as the header prints it, without needing a deck."""
    if not PLATFORM_OVERRIDE:
        return []
    out = [f"platform mass -> {float(PLATFORM_OVERRIDE['mass']):g} kg (model)"]
    out += [
        f"platform {axis} -> {float(value):g} kg*m^2 (model)"
        for axis, value in PLATFORM_OVERRIDE["inertia"].items()
    ]
    return out


def header(head: str, deck: Any) -> str:
    """The provenance the file carries on its face."""
    return (
        "# GENERATED BY scripts/export_platform_deck.py -- DO NOT HAND-EDIT.\n"
        "#\n"
        "# Every coordinate in this file came from HSP's own deck builder. Editing it\n"
        "# by hand breaks the one property DJ1 asked for: that no coordinate is typed\n"
        "# into this repository. Re-run the generator instead; a real difference will\n"
        "# show up as a diff.\n"
        "#\n"
        f"#   HSP tag        {hsp_pin.HSP_TAG}\n"
        f"#   HSP commit     {head}\n"
        f"#   source         studies/platform-12buoy/platform_rao_pilot.py\n"
        f"#   bodies         {len(deck.bodies)}\n"
        f"#   joints         {len(deck.joints)}\n"
        f"#   exported       {_dt.datetime.now(_dt.UTC).strftime('%Y-%m-%d')}\n"
        + (
            "#\n"
            "#   OVERRIDE       this deck is HSP's deck PLUS a declared override, and\n"
            "#                  the override is part of what `--check` compares (ER1(a)):\n"
            + "".join(f"#                    {line}\n" for line in _override_lines())
            + "#                  source: directive ER0 (Xabier, 6 Oct). The inertia\n"
            "#                  scaling is ER0(a)'s assumption, marked overridable.\n"
            if PLATFORM_OVERRIDE
            else ""
        )
        + "#\n"
        "# SCALE: this deck is at MODEL scale. Nothing here is full scale and nothing\n"
        "# in this file applies a factor. floatfea.io.froude converts at the I/O\n"
        "# boundary and floatfea.io.reader refuses a model-scale record that has not\n"
        "# been through it.\n"
        "#\n"
        "# The round trip is checked by the generator before it writes: this YAML\n"
        "# re-validates through Deck.model_validate to a dump equal to the source.\n"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = ap.parse_args(argv)

    head = _preflight()
    deck = build_deck()
    text, source = dump_and_verify(deck)
    content = header(head, deck) + text

    print(f"HSP {hsp_pin.HSP_TAG} @ {head}")
    print(f"bodies {len(deck.bodies)}  joints {len(deck.joints)}")
    print(f"round trip: re-validated dump equals the source dump ({len(source)} top-level keys)")

    if args.check:
        if not OUT.is_file():
            print(f"{OUT.relative_to(ROOT)} does not exist")
            return 1

        # R584. THIS SLICED THE HEADER OFF BOTH SIDES, so tag, commit and counts were
        # compared with nothing -- the one part of the file a reader trusts to state
        # where the model came from was the one part `--check` could not see. The
        # EXPORTED date is the only line that legitimately differs between two
        # correct exports, so it is the only line excluded, by name.
        on_disk = OUT.read_text(encoding="utf-8").splitlines()
        expected = content.splitlines()

        def comparable(lines: list[str]) -> list[str]:
            return [ln for ln in lines if not ln.startswith("#   exported")]

        if comparable(on_disk) != comparable(expected):
            print(f"{OUT.relative_to(ROOT)} DIFFERS from the deck it claims to record")
            for i, (a, b) in enumerate(
                zip(comparable(on_disk), comparable(expected), strict=False)
            ):
                if a != b:
                    print(f"  first difference at comparable line {i}:")
                    print(f"    on disk  {a[:100]}")
                    print(f"    expected {b[:100]}")
                    break
            else:
                print(
                    f"  the files agree line for line but differ in length: "
                    f"{len(comparable(on_disk))} on disk, {len(comparable(expected))} expected"
                )
            return 1

        if DIGEST.is_file():
            recorded = DIGEST.read_text(encoding="utf-8")
            if recorded != digest(yaml.safe_load(text), body=text):
                print(f"{DIGEST.relative_to(ROOT)} DIFFERS from the deck it records")
                return 1
            print(f"{DIGEST.relative_to(ROOT)} matches the deck")
        else:
            print(f"{DIGEST.relative_to(ROOT)} does not exist")
            return 1

        print(f"{OUT.relative_to(ROOT)} matches the deck, header included")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(content.splitlines())} lines)")

    DIGEST.parent.mkdir(parents=True, exist_ok=True)
    DIGEST.write_text(digest(yaml.safe_load(text), body=text), encoding="utf-8", newline=chr(10))
    print(f"wrote {DIGEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
