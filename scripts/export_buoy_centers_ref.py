"""EO0: the pinned EB6 reference snapshot, generated from HSP-stable's SOURCE CODE.

WHY A SNAPSHOT AT ALL. EB6's expected side must come from FloatSim's own platform
definition, which DS0 keeps in a read-only worktree OUTSIDE this repository. A gate
reading it directly cannot run where that worktree is absent -- including CI -- and
`scripts/run_rung.sh` fails a rung on any skip, so the gate made ladder 4 red (R670).
Vendoring the four constants was the other option and is worse: it puts the expected
side where a deck-export permutation could reach it.

A SNAPSHOT IS NEITHER. It carries the VALUES plus the provenance needed to prove they
came from HSP-stable -- the source file's git blob sha and the pinned tag -- so a change
to that file makes the snapshot stale and `--check` says so. **ONE source file, and the
limits of that are stated at `BUOY_ANGLES_DEG` (C155) and at the `BUOY_RADIUS` parse
(C156): a value defined in `cluster-3buoy-rigid/cluster_common.py`, or taken from a
trailing comment, is NOT covered by this file's blob sha.** The deck export cannot
reach the snapshot, which is what EB6 is guarding against.

GENERATED FROM THE SOURCE CODE, NEVER FROM THE DECK EXPORT (EO0(a)). The four constants
are parsed out of `platform_common.py` rather than imported, because importing it drags
in FloatSim and the snapshot must be buildable from a checkout of the source alone.

    python scripts/export_buoy_centers_ref.py            # write the snapshot
    python scripts/export_buoy_centers_ref.py --check     # compare against HSP-stable
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from floatfea import hsp_pin  # noqa: E402

HSP_STABLE = ROOT.parent / "HSP-stable"
SOURCE_REL = "studies/platform-12buoy/platform_common.py"
SNAPSHOT = ROOT / "data" / "platform" / "buoy_centers_ref.json"

BUOY_ANGLES_DEG = (0.0, 120.0, 240.0)
"""`cc.BUOY_ANGLES_DEG`, cited at `platform_common.py:35`, defined at
`cluster-3buoy-rigid/cluster_common.py:47`.

**IT IS A LITERAL HERE AND `--check` DOES NOT COVER IT (C155).** The sentence that stood
here said it was "checked by `--check` like everything else", and that was false in both
halves: `check()` compares `build()` against the stored snapshot and `build()` reads this
same literal, so both sides move together; and the recorded blob sha is
`platform_common.py`'s, so a change in `cluster_common.py` moves neither side and
`--check` prints "current". The value is right today -- verified against
`cluster_common.py:47`, `np.array([0.0, 120.0, 240.0])`.

WHAT `--check` DOES COVER: `CLUSTER_ARM_RADIUS`, `CLUSTER_ANGLES_DEG`, `BUOY_RADIUS` and
`Z_HUB_REF`, all parsed from `platform_common.py`, plus that file's blob sha. A second
source file would need a second blob sha, which is a schema change to the snapshot and
belongs with the next thing that needs it.
"""


def _source() -> Path:
    path = HSP_STABLE / SOURCE_REL
    if not path.is_file():
        raise SystemExit(
            f"{path} is not a file. The snapshot is GENERATED from HSP-stable's source, "
            "so writing it needs that worktree; READING it does not, which is the "
            "whole point of EO0."
        )
    return path


def _blob_sha(path: Path) -> str:
    """The source file's git blob sha, from HSP-stable's own index."""
    out = subprocess.run(
        ["git", "rev-parse", f"HEAD:{SOURCE_REL}"],
        cwd=HSP_STABLE,
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        raise SystemExit(f"could not read the blob sha of {path}: {out.stderr.strip()}")
    return out.stdout.strip()


def _constants(text: str) -> tuple[float, list[float], float]:
    """`(CLUSTER_ARM_RADIUS, CLUSTER_ANGLES_DEG, BUOY_RADIUS)` parsed from the source."""
    arm = re.search(r"^CLUSTER_ARM_RADIUS = ([\d.]+)", text, re.MULTILINE)
    angles = re.search(r"^CLUSTER_ANGLES_DEG = np\.array\(\[([^\]]+)\]\)", text, re.MULTILINE)
    # C156: `BUOY_RADIUS` IS PARSED FROM THE TRAILING COMMENT, not from the constant.
    # `platform_common.py:36` reads `BUOY_RADIUS = cc.CLUSTER_RADIUS  # 0.5 m`, and the
    # value lives in `cluster-3buoy-rigid/cluster_common.py:44`. The comment and the
    # constant agree today (`CLUSTER_RADIUS = 0.5`, verified), and a comment that fell
    # out of step with its constant would become the expected side of two gates with
    # this file's blob sha unmoved. Reading the constant means a second source file and
    # a second blob sha in the snapshot; until that exists, the limitation is written
    # here and in the snapshot's own docstring rather than left for a reader to find.
    radius = re.search(r"^BUOY_RADIUS = cc\.CLUSTER_RADIUS\s*#\s*([\d.]+)", text, re.MULTILINE)
    if not (arm and angles and radius):
        raise SystemExit(
            "could not parse CLUSTER_ARM_RADIUS, CLUSTER_ANGLES_DEG or BUOY_RADIUS from "
            f"{SOURCE_REL}. The snapshot refuses rather than guessing: a wrong expected "
            "side is what EB6 exists to prevent."
        )
    return (
        float(arm.group(1)),
        [float(v) for v in angles.group(1).split(",")],
        float(radius.group(1)),
    )


def _hydro_labels(text: str) -> list[str]:
    """Every `hydro_body_label=` right-hand side in the source, verbatim.

    EK0(a)'s premise is structural: a body with no label has no excitation channel
    addressing its rows. The right-hand sides are recorded as WRITTEN rather than
    resolved, because resolving `f"buoy{k + 1}"` means re-implementing the study's loop
    bound here and a snapshot that re-implements its source is not independent of it.
    What the gate asserts is the thing that matters and that the text settles: no site
    can produce a name belonging to one of the five FE bodies.
    """
    found = [m.group(1).strip() for m in re.finditer(r"hydro_body_label\s*=\s*([^,\n)]+)", text)]
    if not found:
        raise SystemExit(
            f"no `hydro_body_label=` site found in {SOURCE_REL}. The premise EK0(a) rests "
            "on is that only buoys carry one; a parse that finds none would assert that "
            "vacuously, so the snapshot refuses instead."
        )
    return found


def _z_hub(text: str) -> float:
    m = re.search(r"^Z_HUB_REF = ([\d.]+)", text, re.MULTILINE)
    if not m:
        raise SystemExit(f"could not parse Z_HUB_REF from {SOURCE_REL}")
    return float(m.group(1))


def build() -> dict[str, Any]:
    """The snapshot's content, at MODEL scale -- the source's own units."""
    source = _source()
    text = source.read_text(encoding="utf-8")
    arm, cluster_angles, buoy_radius = _constants(text)
    z_hub = _z_hub(text)

    buoys: list[list[float]] = []
    hubs: list[list[float]] = []
    for pc in np.deg2rad(cluster_angles):
        cx, cy = arm * float(np.cos(pc)), arm * float(np.sin(pc))
        hubs.append([cx, cy, z_hub])
        for tb in np.deg2rad(BUOY_ANGLES_DEG):
            buoys.append(
                [cx + buoy_radius * float(np.cos(tb)), cy + buoy_radius * float(np.sin(tb))]
            )
    if len(buoys) != 12 or len(hubs) != 4:
        raise SystemExit(f"built {len(buoys)} buoys and {len(hubs)} hubs; expected 12 and 4")

    return {
        "schema": "floatfea/eb6-reference/1",
        "provenance": {
            "source": f"HSP-stable/{SOURCE_REL}",
            "lines": "CLUSTER_ARM_RADIUS :33, CLUSTER_ANGLES_DEG :34, "
            "BUOY_ANGLES_DEG :35, BUOY_RADIUS :36, Z_HUB_REF :102, "
            "buoy_centers() :51-58, the hub Body :157, hydro_body_label :140",
            "blob_sha": _blob_sha(source),
            "hsp_tag": hsp_pin.HSP_TAG,
            "generated_from": "the source code, never the deck export (EO0(a))",
        },
        "scale": "model",
        "buoy_centres_xy_m": buoys,
        "hub_positions_xyz_m": hubs,
        "hydro_body_label_sites": _hydro_labels(text),
    }


def check() -> int:
    """EO0(c): is the snapshot still what HSP-stable says? Not a pytest skip."""
    if not SNAPSHOT.is_file():
        print(f"EB6 reference: MISSING at {SNAPSHOT}", file=sys.stderr)
        return 1
    stored = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    if not (HSP_STABLE / SOURCE_REL).is_file():
        print(
            f"EB6 reference: HSP-stable absent, so the snapshot cannot be re-derived "
            f"here. It records blob {stored['provenance']['blob_sha'][:12]} at tag "
            f"{stored['provenance']['hsp_tag']}; verify it where that worktree exists."
        )
        return 0
    fresh = build()
    if stored.get("hydro_body_label_sites") != fresh["hydro_body_label_sites"]:
        print(
            "EB6 reference: STALE -- the `hydro_body_label` sites differ from HSP-stable. "
            f"stored {stored.get('hydro_body_label_sites')!r}, fresh "
            f"{fresh['hydro_body_label_sites']!r}. EK0(a)'s premise is about these sites, "
            "so regenerate and re-report the premise.",
            file=sys.stderr,
        )
        return 1
    for key in ("buoy_centres_xy_m", "hub_positions_xyz_m"):
        if not np.allclose(np.asarray(stored[key]), np.asarray(fresh[key]), atol=0.0, rtol=0.0):
            print(
                f"EB6 reference: STALE -- {key} differs from HSP-stable. Regenerate with "
                "`python scripts/export_buoy_centers_ref.py` and explain the move.",
                file=sys.stderr,
            )
            return 1
    if stored["provenance"]["blob_sha"] != fresh["provenance"]["blob_sha"]:
        print(
            "EB6 reference: the VALUES match but the source blob moved, "
            f"{stored['provenance']['blob_sha'][:12]} -> "
            f"{fresh['provenance']['blob_sha'][:12]}. Regenerate so the provenance is "
            "about the file that produced it.",
            file=sys.stderr,
        )
        return 1
    print(
        f"EB6 reference: current. blob {fresh['provenance']['blob_sha'][:12]}, "
        f"tag {fresh['provenance']['hsp_tag']}, 12 buoys and 4 hubs."
    )
    return 0


def main(argv: list[str]) -> int:
    if "--check" in argv:
        return check()
    data = build()
    SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    print(
        f"wrote {SNAPSHOT.relative_to(ROOT)}: 12 buoys, 4 hubs, blob "
        f"{data['provenance']['blob_sha'][:12]}, tag {data['provenance']['hsp_tag']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
