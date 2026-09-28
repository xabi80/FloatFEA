#!/usr/bin/env python
"""The CI paragraph of a review invocation, generated (CX0, R449).

    python scripts/review_invocation.py

WHY THIS EXISTS. R449 was a `cancelled` run published in a step report as
`FAILURE`, with its cancelled ladder published as green. The verdict recorded
one more thing about it: **it propagated**. The invocation handed to the
reviewer repeated the report's wording, so the same wrong fact would have
entered the verdict, and the reviewer caught it only by running the command
itself.

The report's CI sections are generated. The invocation was not, and it is the
same sentence twice, so it is generated from the same functions here. Nothing
in this file asks `gh` a question `scripts/ci_section.py` does not already
ask, and nothing reformats an answer: `outcome()` is imported, not
reimplemented, so the two cannot disagree.

WHAT IT DOES NOT DO. It writes the CI paragraph and nothing else. The rest of
an invocation -- what to attack, what is claimed, what is left undone -- is
the implementer's and is a judgement, not a record.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ci_section import (  # noqa: E402
    _anchor,
    full_sha,
    outcome,
    rounds_runs,
    run_for,
)


def paragraph() -> str:
    number, sha = _anchor()
    sha = full_sha(sha)
    judged = run_for(sha)
    lines = [
        "CI, from `python scripts/review_invocation.py` -- the same functions "
        "that write the report's sections 0 and 0a, so the invocation and the "
        "report cannot disagree about a run (CX0, R449).",
        "",
        f"- At the commit verdict {number} judged, `{sha[:7]}`: run "
        f"`{judged['databaseId']}`, event {judged['event']}, {outcome(judged)}.",
    ]
    runs = rounds_runs(sha)
    if not runs:
        lines.append("- No run at any commit in this round.")
    for r in runs:
        lines.append(
            f"- This round, `{r['headSha'][:7]}`: run `{r['databaseId']}`, "
            f"event {r['event']}, {outcome(r)}."
        )
    lines += [
        "",
        "A run whose status is not `completed` has **no result**: it reached no "
        "verdict on anything, so no reason is attributed to it.",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) > 1:
        print(__doc__)
        return 2
    sys.stdout.write(paragraph())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
