# FZ — standing rulings and escalation (reduce round trips)

*Recorded under FP0, verbatim, as the first commit of the turn that received it. Issued by
Xabier, 2026-10-31.*

## The directive, verbatim

```
DIRECTIVE FZ — standing rulings and escalation (reduce round trips)
Record: docs/directives/FZ.md, and link it from CLAUDE.md and
docs/SUPERVISOR.md so every session and the reviewer read it.

PURPOSE: decide covered questions yourself under the rulings below. Do not
stop to ask. Record each self-ruling in the active directive record as
"SR-<n>: question / ruling applied (FZ rule #) / why", then continue.

STANDING RULINGS (apply without asking)
 1. Blocking: FR1 only. A silently wrong published result blocks;
    everything else goes in the ledger, and is fixed in-cycle if cheap.
 2. Inputs: refuse rather than silently adjust. An exact, documented
    equivalence (e.g. 360 ≡ 0) is accepted on both the recorded and the
    declared side, so the two are never asymmetric.
 3. Every new numeric comparison gets a named tolerance in tolerances.py,
    with its justification and a counter-test showing a just-outside
    value is refused. Never widen an existing tolerance.
 4. Physics found wrong in the UNCONSERVATIVE direction: fix it, mark the
    affected published tables/figures SUPERSEDED with a dated note, give
    an old/new ratio table, and report it in the digest. Do not wait for
    approval. CONSERVATIVE-direction errors: ledger, fix if cheap.
 5. Self-found defects: fix, and add a named test row so they can't
    regress. No ruling needed.
 6. Provenance: derived or stand-in values are marked in human-readable
    outputs (report.md, user guide), never by adding keys to
    machine-readable outputs.
 7. Ambiguous directive wording: take the reading consistent with
    existing conventions and tests, record it as an SR, continue. If both
    readings give the same published numbers, pick the simpler one.
 8. Scope: never trim R1. Work outside R1 → ledger for R2.

ESCALATE (stop that item, keep working on others) ONLY for:
 a. Any change to FloatSim/HSP-stable, or running platform_bem.py.
 b. New physical inputs or design assumptions (masses, truss depth,
    materials, geometry).
 c. Changes to the code-check basis (API RP 2A parameters, Fy, K, C_m,
    allowable increases).
 d. Anything requiring a standing constraint to be broken (tolerance
    widened, test skipped/xfailed, force-push, hook bypass, writing to
    docs/reviews/ outside write_verdict.py).
 e. A forecast that R1 slips past 10 Nov.
 f. Two defensible readings that give DIFFERENT published numbers, where
    no convention or test picks one.

DIGEST (replaces per-item reports to the supervisor)
  Once per working day, or at each step completion if sooner, write
  docs/digests/<date>.md and print it. Contents:
    - done (commits, CI state)
    - SRs taken (one line each)
    - superseded published results (rule 4)
    - escalations (a–f), each with your recommended option first
    - next
  Keep it under one screen. Escalations are the only part needing a reply.

Continue the current queue under FZ: FY1/FY2/FY5 test rows and
docstring, golden check, FY3, the step-3 report revision 1, then FL3.
```

## What FZ changes about how this repository is worked

**It replaces asking with deciding, for everything its eight rulings cover**, and it
replaces the per-item report to the supervisor with a once-a-day digest. What it does not
change is the gate: `CLAUDE.md`'s step gating, the reviewer's verdicts and the ES0 revision
cap are untouched, and FZ (d) makes breaking any standing constraint an escalation rather
than a self-ruling.

**The three questions this session had already stopped to ask would now be decided, not
asked** — and recording that is the honest measure of what FZ costs and buys:

* **FX** (the Carried-table generator blocked by a hook) would still be an escalation,
  under FZ (d): a hook bypass is named there explicitly. Asking was right.
* **FY1's `[0, 360)`** would be decided under rule 2's second sentence, which settles the
  recorded/declared asymmetry directly — and would have reached FY5.1's answer without a
  round trip.
* **FY2's derived-height disclosure**, which the FY1/FY2 work named and declined to build,
  is rule 6 exactly: marked in `report.md`, never by a key in a machine-readable output.
  That is FY5.2's answer, reached without asking.

So two of the three round trips this cycle spent were avoidable under FZ and one was not.

## Where self-rulings are recorded, and the first one

FZ says "the active directive record". **This file is that record for FZ-era rulings**, in
a running log below, rather than each SR going into whichever directive file happens to be
newest. The reading and the reason are themselves SR-1.

### SR log

**SR-1: where does an SR get written?**
*Ruling applied:* FZ rule 7 (ambiguous wording → the reading consistent with existing
conventions, recorded as an SR).
*Why:* "the active directive record" has two readings — this file, or the newest directive
file at the time of each ruling. The second scatters a running log across `FY.md`, `FZ.md`
and every later file, so a reader looking for "what did this session decide on its own"
would have to know the directive sequence first. `docs/directives/README.md` is already the
index of the record and points at one file per directive; one SR log in the file that
created the mechanism is the reading consistent with that. No published number depends on
either reading, so rule 7's tie-break — pick the simpler one — also selects this.

**SR-2: what is "per grid cell" for FY3's old/new ratio table, when the shipped example has
`truss_sizing` OFF and its `(h, b)` grid commented out?**
*Ruling applied:* FZ rule 7 (ambiguous wording → the reading consistent with existing
conventions and tests).
*Why:* two readings. (i) A probe load at a configuration where the inclined face governs,
which is what verdict 42 used to show the defect reaches the published column. (ii) The
example's own declared grid — `depths × widths × shapes` from the commented `truss:` block
— at the deck's own governing rows. **Taken: (ii).** FY3's phrase is "per grid cell" and
`truss_sizing.md` is published over that grid, so "cell" already denotes a row of that
table; a probe load would produce a table of a configuration no deliverable contains. The
probe is kept as well, as the absolute `h = 2, b = 8` cell FY3 separately requires, because
it is the configuration where the whole factor lands in the published column and the grid's
own rows mask it. Both readings are reported; neither replaces the other.

**SR-3: the triangle's torsion closure — against Bredt's identity, or against the module's
own wall forces?**
*Ruling applied:* FZ rule 1 (what blocks is a silently wrong published result) with rule 5
(self-found defects fixed, not ruled on).
*Why:* my first closure measurement computed the triangle's recovered `Mx/T` as
`2 · A_enc · q`, which is Bredt's identity and therefore `1.000000` whatever the module
does — a check that cannot fail, which is the R434 shape this repository has a guard for.
It was replaced before anything was claimed from it: the closure now sums the moments of
the module's OWN wall magnitudes about a point, with each wall's real lever, so a wrong
magnitude moves the answer. Worst `|closure − 1|` over the declared grid is `2.22e-16` on
`Vz` and exactly `0` on `Mx/T`. No ruling was needed on the physics; what needed recording
is that the first version of the evidence was vacuous and why.

**SR-4: does FY3's "mark the triangle tables SUPERSEDED" mean recompute them?**
*Ruling applied:* FZ rule 7 (ambiguous wording -> the reading consistent with existing
conventions), with rule 4 (unconservative physics: fix, mark SUPERSEDED, give a ratio table).
*Why:* two readings. (i) Fix `scripts/measure/f6b_truss_sizing.py` as well and regenerate
F6b's numbers. (ii) Leave the numbers as the record of what F6b published and mark them,
pointing at the corrected values. **Taken: (ii).** FY3's own words are "mark ... SUPERSEDED
with a dated note pointing to the corrected values" -- under (i) there would be nothing to
point at, and "superseded" would be the wrong word for a document that now agrees.
Recomputing would also destroy the evidence that the correction was needed, which is what
rule 4's ratio table exists to keep readable. The note carries no measured figure, because
that document's standing rule is that none is typed into it; it names which column moves
least and which most, and points at R1's `truss_sizing.md` and the step report.

**SR-5: the F6b generator wrote the deliverable and then exited 1.**
*Ruling applied:* FZ rule 1 (not blocking under FR1, fixed in-cycle because cheap) with
rule 5 (self-found defect: fix and add a named row).
*Why:* `args.out.relative_to(ROOT)` on the final log line raises `ValueError` for any
`--out` not under the repository root. The write had already happened, so the artifact was
on disk at 17516 bytes and the process exited 1 -- a caller checking the exit code concludes
the file was not produced; one that does not gets a traceback beside a correct artifact. No
number is wrong, so FR1 does not make it blocking; it is one line, so it is fixed now rather
than ledgered. **And it had already cost something before it was found:** my first
verification of the supersession printed "REGENERATES BYTE-IDENTICAL" from a `cmp` of two
files written by crashed runs, because a `&&` chain hides a non-zero exit whenever the next
command succeeds on the wreckage. That claim was withdrawn and re-measured with exit codes
checked.

**SR-6: FY2's derived height was computed from a lambda nothing had reconciled.**
*Ruling applied:* FZ rule 1 (FR1: a silently wrong published number blocks, so it is fixed
ahead of everything else) with rule 5 (self-found defect: fix and add a named row) and
EH4 (the boundary solved in both directions, including the two that weaken the check).
*Why:* FY2 made `_resolve_height_pair` derive the missing height from `run.lambda`. The
sidecar's `run.lambda` and the npz's `froude_lambda` are two records of ONE fact, and the
comparison between them lived inside `validated_export_scale` -- the door a deliverable
resolves its SCALE through, not the door `run()` resolves the BASIS through.
`exported_wave_basis` went straight to `wave_basis_from_sidecar`. Measured on the shipped
pair with `run.lambda` edited to 25.0 against an npz key of 50.0:

    model 0.484 only  ->  full published as 12.1 m    EXIT 0   (24.2 m is the truth)
    full 24.2 only    ->  model published as 0.968 m  EXIT 0   (0.484 m is the truth)

Wrong by exactly the ratio of the two records, in `report.md` and in both CSV headers, and
in the breaking band: at `governing_periods: [12.5]` the same recorded period came out
`too short for this height` at 24.2 m and `too long for this height` at 12.1 m, both at
exit 0. That is the sentence FR1 asks for -- a wrong number and a wrong verdict in a
published deliverable, with nothing saying so.

**AND MY FIRST ACCOUNT OF IT WAS TOO NARROW, WHICH IS WORTH RECORDING BECAUSE THE
CORRECTION WIDENED THE DEFECT.** I wrote -- in the commit message and in the docstring --
that the pair check already refused a lambda disagreement whenever both heights were
recorded. That holds for one of the two ways both heights can be recorded. A sidecar
belonging to a DIFFERENT export carries heights consistent with its OWN lambda, and then
`0.968 * 25 == 24.2` exactly, so FY2's check has nothing to complain about and `25.0` is
inside `FROUDE_LAMBDA`. Driven through the basis door alone: **ACCEPTED**, publishing
`lambda = 25.0` and `wave_height_model_m = 0.968` where `24.2/50 = 0.484` is the truth. A
published scale and a published model height, each wrong by the ratio of the two records,
with every check that existed green. Three shapes; that one fired nothing, and it is the
one a real mismatched pair would have.

**It was found by a red test whose outcome was right.** `test_R933_a_DISAGREEING_scale_is
_refused_by_both` refused the disagreeing pair with a message naming the two HEIGHTS,
which at that input are the two numbers that are correct; the record that is wrong is the
lambda. Exit code and "wrote nothing" were both right, and only the assertion on the
message saw it. Under FR1 that half is a ledger item, not a block -- the derivation half
is the block.

*The repair:* the comparison is extracted to `refuse_separated_scale_records`, one
decision at one site, called by `validated_export_scale` as before AND by
`exported_wave_basis` before it resolves a basis against the sidecar's lambda. Both
generators resolve the scale before the basis, so their refusal names the record that has
to be repaired. `pipeline.py` had itself described that call order as a thing that
"happens to" hold; that comment is now a stated dependency, and the regression cell that
went red is what holds it.

**SR-7: `np.load`'s exception handler was marked `# pragma: no cover` and was wrong for
three of six malformed npz shapes.**
*Ruling applied:* FZ rule 1 (ledger under FR1 -- no number is wrong, the run dies with a
traceback instead of a named refusal) with rule 5 (self-found defect: fix in-cycle, add a
named row).
*Why:* `exported_froude_lambda` caught `(OSError, ValueError)` behind
`# pragma: no cover - unreadable npz`. Measured:

    empty file       EOFError            NOT caught -- derives straight from Exception
    text file        ValueError          caught
    truncated npz    zipfile.BadZipFile  NOT caught -- derives straight from Exception
    a directory      PermissionError     caught (OSError)
    missing          FileNotFoundError   caught (OSError)
    zip magic only   zipfile.BadZipFile  NOT caught

So `floatfea run` on an empty or truncated npz gave an uncaught traceback where the code's
own intent is the named refusal "the npz could not be read". **A `# pragma: no cover` on an
exception handler is a statement that nothing ever measured it**, and this one was wrong
for half the shapes it names.

**It was found because I copied it.** `_npz_scale_key`, written for SR-6's repair, took
that handler verbatim and inherited the hole; `test_R877_the_READER_ITSELF_validates_not
_only_the_helper` -- which writes its npz as `b""` on purpose -- went red with `EOFError`
raised out of my new function. The repair is one shared `UNREADABLE_NPZ` tuple rather than
a second corrected copy, which is R983's rule and is exactly what the copy demonstrated.
Six shapes, six rows, in
`test_SR6_every_UNREADABLE_npz_shape_reaches_the_NAMED_refusal`.

**SR-8: the same defect one file type over -- `(OSError, json.JSONDecodeError)` at four
sites, none of them catching `UnicodeDecodeError`.**
*Ruling applied:* FZ rule 1 (ledger under FR1 -- no number is wrong; the run dies with a
traceback where a named refusal is intended) with rule 5 (self-found: fix in-cycle, named
row).
*Why:* a provenance sidecar that exists and is not UTF-8 raises out of
`read_text(encoding="utf-8")`, before `json.loads` is reached. `UnicodeDecodeError` is a
`ValueError` subclass and `json.JSONDecodeError` is a *different* `ValueError` subclass,
so naming the second does not catch the first. Measured: both
`refuse_separated_scale_records` and `wave_basis_from_sidecar` raised
`UnicodeDecodeError` on `b"\xff\xfe\x00binary garbage not utf8"`.

The site that matters is `wave_basis_from_sidecar`, whose refusal text is *"exists and
cannot be read as JSON"* -- exactly this case, bypassed. **R1007's distinction is what
this protects**: an UNREADABLE sidecar is not an ABSENT one, and a traceback is not that
distinction either; it is the third outcome, where the run dies without naming the file.

*Why it is in this commit and not ledgered, stated so the gate can rule on the
judgement rather than infer it:* **it was found by asking SR-7's question at the next
reader**, and the census is over `json.JSONDecodeError` in the whole module rather than
over the two sites this repair happened to touch -- four found, four fixed, one shared
`UNREADABLE_JSON`. Having just fixed one instance of "a handler that names two classes
and misses a third", leaving three known instances of it standing is the narrow-census
failure FR1 lists as a non-blocking class and which has cost this milestone three rounds
elsewhere. If the reviewer rules it scope creep in an FF0 commit, the repair is sound and
only its placement is wrong.

**And SR-7 had a second half, in code this commit WROTE.** `_npz_scale_key` kept the
`np.load` inside the handler and the conversion after it, so
`np.asarray(recorded).reshape(()).item()` sat outside. `is_recorded_number` is **True**
for a multi-element array, so `froude_lambda = np.array([50.0, 25.0])` raised
`ValueError` as a bare traceback out of `exported_wave_basis` -- while
`exported_froude_lambda`, which has the identical conversion INSIDE its own `try`,
answered `the npz could not be read (cannot reshape array of size 2 into shape ())`. Two
readers, one input, one crash and one named reason. Three shapes measured (two elements,
empty array, 2x2); all three behaved that way, and all three are rows in
`test_SR7_a_MULTI_ELEMENT_scale_key_reaches_the_NAMED_refusal`.

**SR-9: the refusal message computed a ratio, which divided by zero on one input and
published nonsense on another. A defect this commit INTRODUCED.**
*Ruling applied:* FZ rule 5 (self-found: fix in-cycle, named row). Under FR1 a crash is
not a wrong number, so it does not block -- but it is mine and it is one line.
*Why:* the message read `wrong by {ratio}x` with
`ratio = max(key, beside) / min(key, beside)`. `is_recorded_number(0.0)` is **True**, and
`exported_wave_basis` reaches this comparison BEFORE any domain check --
`validated_export_scale` range-checks against `FROUDE_LAMBDA`, but that is the other
door. Driven through `exported_wave_basis` with the npz key at 50.0:

    run.lambda = 0.0     ZeroDivisionError: float division by zero
    run.lambda = -50.0   refused, and its own text read `wrong by -1x`
    run.lambda = 25.0    refused, `wrong by 2x`   <- the only case I had checked

So: a crash on the main `run()` path, and a nonsense figure inside a refusal, from a
quotient that existed only to decorate a message.

*The repair is removal, not a guard.* The message already states both recorded values,
so the quotient is the reader's to take, and a division that crashes on one input and
lies on another is not worth keeping for prose. **A decorative figure is still a
figure**, and this one was measured at exactly one input -- the same shape as EU1's
lesson about a constant that is right at the configuration its author chose.

*How it was found, because that is the transferable part:* not by a test and not by
review, but by reading my own diff with the comments stripped and asking what every
computed expression does at its boundaries. `ratio` was the only arithmetic in the
function. Three rows pin it, including `-0.0`, where the sign is invisible in the text
and the division would still have failed.

**SR-10: the F6b sizing generator wrote both deliverables and then exited 1.**
*Ruling applied:* FZ rule 1 (not blocking under FR1) with rule 5 (self-found defect:
fix and add a named row).
*Why:* recorded here because SR-1 rules that this file is the record and SR-10 reached
only `docs/digests/2026-11-02.md`. It is SR-5's defect in a second generator:
`args.out.relative_to(ROOT)` on the closing log line raises `ValueError` for any `--out`
outside the repository root, after both the CSV and the JSON are on disk. A caller
reading the exit code concludes nothing was produced. The repair is a `_shown()` helper
that falls back to the absolute path, and
`test_SR10_the_SIZING_generator_also_does_not_crash_AFTER_writing`. **Four sites still
carry the bare form** under `scripts/measure/` — `api_wsd_utilisation.py`,
`f6a_premise_check.py`, `f6a_report.py`, `f6a_required_section.py` — recorded at
`member_forces_table.py:486` before I found this one, so the family is a known deferral
and not a discovery of mine.

**SR-11: 1905 report-guard reds whose test ids each name a site of the newest verdict —
boundary reds under FS1's first limb, or CZ1 (iv)?**
*Ruling applied:* FZ rule 7 (ambiguous wording → the reading consistent with existing
conventions), with rule 5 (self-found defect: fixed, named row).
*Why:* two readings, and the literal one is wrong. FS1's predicate is "every red names a
finding or a site of the newest verdict". All 1905 ids of
`test_every_named_site_is_touched_or_declared` do exactly that, so read as a pattern
match on the id, every one is waived. **Taken: they are not boundary reds.** EG3 names
two states and both are self-clearing — state (1) is cleared by the verdict, state (2)
**by the answering report and not by time**, which is the eighty-third verdict's own
sharpening. Here the verdict exists *and* the answering report exists, so neither state
obtains; a red that survives both is not at a boundary, it is a defect in the report.
And it was: the revision omitted the generated declaration block entirely. Step 2's own
report carries **367** `no change` lines; the draft of this one carried **0**.

The reading matters beyond this instance, so it is stated as a rule rather than as an
outcome: **FS1's limbs are tests of the CAUSE of a red, not patterns over its id.** A
waiver read as a pattern over ids would have passed 1905 unanswered sites into a
reviewed revision, which is the `R29` shape — half of an item is not the item — at a
scale no reviewer could be expected to notice by reading.

*The repair:* `python scripts/untouched_sites.py` generates §8b, and the reason column
is keyed on the same pointer file §8's table is generated from. All 1905 rows fall in
one class, `later`, because the diff reaches every site of `R1106`, `R1107` and `R1108`
and every other row belongs to a finding §7 carries unswept.

**SR-12: `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` is one of the two tests FT1's
limb two exists for. It was red. Is it waived?**
*Ruling applied:* FZ rule 7, and `CLAUDE.md`'s own sentence that both limbs are reasons
and neither is a list of names.
*Why:* **no.** FT1 names that test because *no run exists for a commit before it is
pushed* — that is the reason, and the two names are illustrations of it. This red had a
different cause: the revision carried no `## 0a` table at all, because the assembler ran
`scripts/ci_section.py` and never `--rounds`. A waiver claimed on the name would have
hidden a missing generated section behind a rule written for a missing CI run.

This is the same error as SR-11 in the opposite direction — there a red was waived by
matching an id, here one would be waived by matching a name — and it is why the
enumerated lists went in the first place. **A red is ruled on by its cause.** With §0a
present the test passes, which is the control: one variable moved.

**SR-13: a published figure of mine was stale by eleven lines.**
*Ruling applied:* FZ rule 5 (self-found defect: fixed, stated rather than quietly
corrected).
*Why:* §7 cited `NODE_COINCIDENCE_DECIMALS` at `floatfea/tolerances.py:1793`. That was
the line when I measured it; `325fd2e` then added eleven lines above the declaration and
the line became **1804**. Nothing re-takes a measurement when the file beneath it moves.
**This is the fourth figure of mine in two days voided by the same ordering**, which is
what CP3 exists for — the paste is the LAST edit — and the fourth instance is the reason
it is recorded as a ruling rather than as a typo. The report states the correction in the
`judge` field of the triple that carries the new figure, so a reader who remembers `1793`
is told what happened to it.

**SR-14: the reviewer and I both allocated `R1117`, to different findings.**
*Ruling applied:* FZ rule 7 (ambiguous wording → the reading consistent with existing
conventions), with rule 5.
*Why:* I took `R1117` for the finding-anchor defect, found while building the Carried
table, at a moment when the verdict file's highest id was `R1116`. The reviewer
concurrently took `R1117` for a finding against itself in the addendum `6f14aba` — it
removed its own worktree while a two-hour measurement was still reading it, and 33 of
that run's reds were that. **Taken: the reviewer's allocation is canonical and mine
moves to `R1118`.** `docs/reviews/` is written only by `scripts/write_verdict.py` and
the implementer never writes a verdict, so the ledger's numbering is the reviewer's to
allocate; there is no competing convention and nothing to escalate under rule 6.

It is not a cosmetic clash. `scripts/carried_table.py` generates a row for `R1117` from
the verdict, and the report's §5 was titled `R1117`: **a carried row resolving to a
section about a different finding is a wrong pointer in a published deliverable**, which
is what FR1's first head covers. The report now carries `R1118` in §5 and the addendum's
`R1117` in §5a.

**What cannot be corrected is three commit messages** — `31bae09`, `3861fa0` and
`64af726` — which call the anchor defect `R1117`. History here is linear and force-push
is forbidden. §5a is the record, and it says which of the log's four `R1117` hits is
whose, because a reader grepping the log would otherwise find a contradiction with no
resolution in the repository.

**SR-15: the first commit of revision 1 answered the wrong verdict, and every generated
section inherited it.**
*Ruling applied:* FZ rule 5 (self-found defect: fixed, named test row).
*Why:* the `Answers:` line named `ea92019`, verdict 43. The addendum `6f14aba` is a
newer verdict entry, written after `3861fa0` published revision 1. Every generated
section anchors on that sha — `scripts/ci_section.py` walks `Answers:` → the verdict's
own header → the judged commit — so §0, §0a, §8 and §8b were all produced against the
verdict file **as it stood before the addendum existed**. The repair is one line of
header and a full regeneration, not an edit.

**The reusable half, and it is the second instance in this step:** a generator given a
stale anchor does not fail. It succeeds, against the wrong input, and emits a complete
and plausible section. The first instance was anchoring on `a2c3f5c` earlier in this
step, which produced a §0 about verdict 42 that read perfectly. Neither was caught by
reading; both were caught by `test_the_answered_verdict_is_the_NEWEST_one`, which fired
only once the report commit existed — CZ1's reusable half, since the comparison is
between the report's commit and the verdict's.
