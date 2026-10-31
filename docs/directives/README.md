# The directive record (FP0)

Every directive from Xabier is committed here **verbatim**, one file per directive, as the
**first commit of the turn that receives it** — a standalone `plan:` commit. Plans and
reports cite these files rather than paraphrasing them.

**Why this exists, and it is C25.** Directives were being implemented and cited as the
governing rule without their text existing anywhere in the repository. Measured at the
interim check on R1 step 1: `FO0`, `FO1` and `FO2` were cited as the governing rule in five
shipped files, and `grep -c "FO0\|FO1\|FO2\|FO3" docs/milestones/R1.md` was **0**. FM0 had
got a plan section, FN2 and FN3 had got `process:` commits, FO had got neither — and a
blocking finding's repair condition was "what FO0 actually requires", which no file said.

A rule cited by five files and recorded in none is a rule nobody can check a repair
against.

## Provenance, stated per file

Each file records where its text came from. **This is not uniform and the record says so:**

* `FM.md`, `FN.md`, `FO.md`, `FP.md`, `FQ.md`, `FR.md`, `FS.md`, `FT.md`, `FU.md`,
  `FV.md`, `FW.md` — **verbatim** from the directive message.
* `FY.md` — **verbatim** from the directive message. Issued by Xabier, 2026-10-31.
* `FX.md` — **verbatim, but the directive arrived as a SELECTION rather than as a message.**
  Xabier was asked a question with three options and chose one; what is reproduced
  word-for-word is the question and all three options, including the two not taken, so a
  later reader can see what the ruling was chosen *against*. There is no free-text
  instruction to quote and the file says so rather than inventing one. **This is the first
  directive in this record with that provenance**, and it is distinguished here because
  "verbatim from the directive message" would be false of it.
* `FL.md` — **reconstructed from the session summary.** FL arrived before a context
  compaction, so the implementer no longer had the original message when the record was
  backfilled. The summary's rendering is faithful in substance and is not guaranteed
  word-for-word; the original is in the session transcript named in that file.

Earlier directives (through FK) are not backfilled here. They were implemented and are
recorded where they were adopted — `CLAUDE.md`'s own clauses quote most of them verbatim,
which is why the gap only became visible at FO.
