# DIRECTIVE FU — gravity, constants placement, the date

Received 27 October 2026. Verbatim, recorded before any of it is acted on (FP0).

```
DIRECTIVE FU — gravity, constants placement, the date

FU0 — ONE GRAVITY (R1004): the project uses FloatSim's value, 9.81 m/s²,
  everywhere, read from floatfea.io.frames.GRAVITY_MAGNITUDE (the single
  source). No other gravity literal anywhere in floatfea/ or scripts/.
  Half A (the steepness / band screen) in FT2.3's commit; half B
  (f6a_required_section.py) in FT2.4's, as you routed it. Regenerate the
  affected tracked deliverables in the same commits (BP0) and state in each
  cover note what moved and that no verdict or conclusion changed.
  A test: grep for 9.80665 in floatfea/ and scripts/ returns 0, and the
  screen's λ uses the frames value (a patched frames value moves it).
FU1 — The placement of √(6.5·H), √(11·H) and 1/7 in basis.py (cited code
  constants, not tolerances; R1 §4 stays "none expected") is accepted.
FU2 — FT3's DATE, NOW, before more building: the remaining items, each with an
  estimate, and a realistic R1 finish date. It goes in your next message to
  Xabier, not in a report. Then continue FT2.3 → FT2.7 → FL3 without stopping
  between items.
```

## What each clause settles

**FU0** answers R1004, which was found in the tree rather than in a diff and reported in
the message that this directive answers. It is FR1's second head — an input accepted and
used other than as declared — and the declaration is `floatfea/io/frames.py`'s own
published frames table, which says "magnitude 9.81, FloatSim's value, **not** 9.80665".
The directive resolves the one question that was genuinely the supervisor's: the screen
consumes FloatSim's gravity, so the screen and the loads describe one world.

**FU1** accepts the placement argued from `floatfea/basis.py`'s own docstring ("**Not
tolerances.** These are physical and code-derived constants") and from `R1.md` §4's last
paragraph. No plan reopen, and §4 stays "None expected, under FM0."

**FU2** is answered in the message, not here, and not in a report. It is the escalation
CLAUDE.md § Step gating requires when steps close carrying blocking items, asked for
again after FR0 answered the previous one with SLIP, NOT TRIM.
