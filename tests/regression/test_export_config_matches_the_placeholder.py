"""`examples/platform12_export.yaml` is the placeholder with ONE block changed.

**WHY IT IS A TEST AND NOT A COMMENT.** GI5 step 1's acceptance is that exporting the
reference run *reproduces the golden dynamic-inputs file* -- bit-exactly, under Q8's rule
that there is no tolerance on that comparison. The golden was produced at the placeholder
configuration's inputs. If the export configuration drifts from it in any block the solve
reads, the comparison stops being a property of the code and becomes a coincidence of two
files that happen to agree.

The export header asserts the two files share everything but `load_cases` and `outputs`.
That is a claim about this repository written in prose, and CW0 gives prose three options:
a test, a triple, or deletion. This is the test.

**WHAT IT DOES NOT CLAIM.** It does not say the shared text is *correct* -- the placeholder
is a fixture, not a recommendation, and `tests/regression/test_r1_example_golden.py` is
what holds it to `U = 1.71167`. It says the two files cannot disagree without something
going red.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLACEHOLDER = ROOT / "examples" / "platform12_placeholder.yaml"
EXPORT = ROOT / "examples" / "platform12_export.yaml"

# The two blocks that are ALLOWED to differ, and nothing else. `load_cases` differs
# because `export` declares the runs to make rather than a file to read; `outputs`
# because the exported npz goes to the committed location and the FE artifacts are off.
MAY_DIFFER = ("load_cases:", "outputs:")


def _blocks(text: str) -> dict[str, str]:
    """Top-level `key:` blocks, in file order.

    A top-level key is one at column zero ending in `:`. Comment lines above a key belong
    to the block they introduce, which is why the split is on the key line itself and the
    preceding comments travel with it -- a comment that moved between two blocks would
    otherwise read as text deleted from one and added to the other.
    """
    out: dict[str, str] = {}
    current = "<preamble>"
    buf: list[str] = []
    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        is_key = (
            stripped and not stripped.startswith((" ", "\t", "#", "-")) and stripped.endswith(":")
        )
        if is_key:
            out[current] = "".join(buf)
            current = stripped
            buf = []
            continue
        buf.append(line)
    out[current] = "".join(buf)
    return out


def test_every_block_but_load_cases_and_outputs_is_BYTE_IDENTICAL() -> None:
    placeholder = _blocks(PLACEHOLDER.read_text(encoding="utf-8"))
    export = _blocks(EXPORT.read_text(encoding="utf-8"))
    shared = [k for k in placeholder if k not in ("<preamble>", *MAY_DIFFER)]
    assert shared, (
        "no shared block was found, so this test would pass on two unrelated files. "
        "The block splitter stopped matching the configuration's layout."
    )
    differing = [k for k in shared if export.get(k) != placeholder[k]]
    assert not differing, (
        f"{differing} differ between {EXPORT.name} and {PLACEHOLDER.name}. The export "
        f"must reproduce `data/f4/dynamic_inputs.npz` bit-exactly (GI5 step 1, Q8), and "
        f"the golden was produced at the placeholder's inputs -- so a difference in any "
        f"block the solve reads makes that comparison a coincidence. Change both files or "
        f"neither, and if the difference is deliberate, say so in MAY_DIFFER with the "
        f"reason."
    )


def test_the_SHARED_SET_IS_NOT_EMPTY_AND_NAMES_THE_BLOCKS_IT_HOLDS() -> None:
    """The control for the test above, which would otherwise pass vacuously.

    A splitter that returned one block per file would make `differing` empty and the
    assertion true about nothing -- AM5's rule that an empty parameter set is an error and
    not a skip, applied to a test's own subject. These are the blocks a reader expects to
    be held, named rather than counted, so a block that silently stopped being compared
    reddens here.
    """
    placeholder = _blocks(PLACEHOLDER.read_text(encoding="utf-8"))
    assert {"floatsim:", "sections:", "code_check:"} <= set(placeholder)
    assert set(MAY_DIFFER) <= set(placeholder)


def test_the_export_config_declares_CASES_and_the_placeholder_declares_NPZ() -> None:
    """The one block that differs, differing in the direction it is supposed to.

    `load_cases` must give exactly one of `npz` or `cases` -- both or neither is refused
    as ambiguous -- so this is the inverted half: it is not enough that the block differs,
    it has to differ by the export declaring runs and the placeholder declaring a file.
    """
    export = EXPORT.read_text(encoding="utf-8")
    placeholder = PLACEHOLDER.read_text(encoding="utf-8")
    assert "\n  cases:\n" in export and "\n  npz:" not in export
    assert "\n  npz:" in placeholder and "\n  cases:\n" not in placeholder
    assert "\n  headings: [0.0]\n" in export


def test_the_export_config_declares_the_SIX_PERIODS_THE_NPZ_CARRIES() -> None:
    """The export's cases against the committed file's own record.

    Not against a list retyped here: `periods_full_s` is an array IN the npz (R805 put the
    scale beside the data for the same reason), so the comparison is against the artifact
    the export has to reproduce. A seventh case, or a period moved, would change every
    array the file holds and `--check` would refuse -- but it would refuse after
    26 minutes, and this refuses in milliseconds.
    """
    import numpy as np

    npz = ROOT / "data" / "f4" / "dynamic_inputs.npz"
    if not npz.is_file():  # pragma: no cover - the committed file is tracked
        raise AssertionError(f"{npz} is tracked and must exist for this comparison")
    with np.load(npz, allow_pickle=False) as data:
        recorded = sorted(float(p) for p in data["periods_full_s"])
    text = EXPORT.read_text(encoding="utf-8")
    declared = sorted(
        float(line.split("T:")[1].strip().rstrip("}").strip())
        for line in text.splitlines()
        if line.strip().startswith("- {heading:")
    )
    assert declared == recorded, (
        f"the export configuration declares periods {declared} and the committed npz "
        f"records {recorded}. `--check` compares every array bit-exactly, so a period "
        f"that is not in the file cannot reproduce it."
    )
