# `scripts/measure/` — the scripts every report figure comes from

Adopted by directive **EV3**, which answers **C12**.

> every figure in a report comes from a script committed under `scripts/measure/` (plain
> scripts, outside the gate; not apparatus) and is cited by path and command. No
> scratchpad citations.

## Why this directory exists

Through F4 step 2 the measurements behind the reports' figures lived in the session
scratchpad. Every figure was reproducible *by me* and by nobody else: a `cmd` line reading
`python scratchpad/r710.py` names a file the reviewer does not have, which is the one thing
BF0's triple is supposed to prevent. The round-3 verdict reproduced all of them
independently and said so — which cost nothing *that* round, and was luck rather than a
property of the arrangement.

## What belongs here, and what does not

**Here:** a script whose output is a figure a report publishes. It measures; it asserts
nothing; it is not collected by `pytest` and no gate imports it.

**Not here:**

* **gates** — those are `tests/verification/`, and a gate's `# expected:` side is written
  in the test, not borrowed from a script (EA4);
* **apparatus** — guards, scanners, meta-tests, detectors and report generators are frozen
  through F6 by **DR1**. A plain measurement script is none of those, which is the
  distinction EV3 draws when it calls these "plain scripts, outside the gate";
* **anything that writes into `../HSP-stable`** — DS0. Runs happen in `../HSP-runs`.

## The rule for a report

A figure is cited by **path and command**:

```
cmd    python scripts/measure/<script>.py [args]
out    <the line that script printed>
```

Not `python scratchpad/...`, and not a remembered run (**CP3**: the paste is the last edit,
and an edit after it voids the paste).
