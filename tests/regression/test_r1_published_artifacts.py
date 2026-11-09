"""The PUBLISHED artifacts are read as files, not as a stub (R816, FO2).

**WHY THIS FILE EXISTS.** Verdict 2 measured that no test in `tests/` touched
`results/R1/example/`, `_write_report`, `_write_member_forces`, `_write_utilisations` or
`_cmd_run`. The header test asserted `_header_lines()` on a hand-built `RunResult`, which
checks the function and not the file: everything between that function and the bytes on
disk -- the `#` prefixing, the comma stripping, the writer's column list, the report's
section order -- was unexercised.

That is not hypothetical. R808 was a duplicated body prefix IN THE PUBLISHED REPORT that
survived a round because I verified the console line and not the file, and asserted the
fix in a commit message. A test over `_header_lines` would not have caught it either.

**THE ARTIFACTS ARE COMMITTED, SO THIS READS THEM RATHER THAN REGENERATING THEM.** A full
run is 67 s and `test_r1_example_golden.py` already pays it to check the NUMBERS.

**WHAT IS CHECKED HERE, NAMED RATHER THAN CALLED "THE PUBLISHED FORM" (C40).** That phrase
was broader than the file: the nine caveats and their count, the screen disclaimer `LABEL`,
the commented CSV header and its parseability, the clause limits, and the sensitivity
operating points. **NOT** checked against these three files: the provenance block and the
wave-basis line, which are per-run values rather than constants and are asserted at the
generator in `tests/unit/test_run_pipeline_refusals.py`. A docstring that claims a whole
category covers the next hole in it by accident.

**AND THE CLAIM THAT USED TO FOLLOW THAT SENTENCE WAS FALSE, WHICH R831 MEASURED.** It read
"reading the committed files also catches a regeneration that was never committed -- which a
test that regenerates cannot". It did not: the caveat gate's needle was the MARKER, and
`EX3` appears in the stale sentence as well as the repaired one, so all three deliverables
published the pre-R829 wording with 33 of 33 cases green. A needle that matches both sides
of the change it is meant to detect catches nothing. The needle is now the caveat TEXT, out
of `floatfea.cli.TABLE_CAVEATS`, so a reworded caveat reddens until the files are
regenerated.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from floatfea.cli import LABEL, TABLE_CAVEATS

ROOT = Path(__file__).resolve().parents[2]
PUBLISHED = ROOT / "results" / "R1" / "example"
REPORT = PUBLISHED / "report.md"
FORCES = PUBLISHED / "member_forces.csv"
UTILISATION = PUBLISHED / "utilisation.csv"

# **THE NEEDLE IS THE CAVEAT TEXT, NOT ITS MARKER (R831).** This was
# `CAVEAT_MARKERS = ("R739", "R740", ... "R743")` -- eleven markers for nine caveats,
# `EX3/R724` and `R741/R742` each naming two findings. The marker is present in a REWORDED
# caveat too, so when R829's repair changed `TABLE_CAVEATS[4]` in `cli.py` and the files
# were not regenerated afterwards, all 33 (file, marker) cases stayed green while all three
# deliverables published the sentence R829 had named false.
#
# Reading the source of truth makes the comparison one that can fail.


def _normalised(text: str) -> str:
    """`_write_header` writes `line.replace(",", ";")` so a CSV reader is safe.

    Both sides are normalised the same way, so one needle serves the markdown report and
    the two CSVs without a per-file branch that could pass for the wrong reason.
    """
    return text.replace(",", ";")


ARTIFACTS = (REPORT, FORCES, UTILISATION)


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_the_artifact_was_published_at_all(path: Path) -> None:
    """The file exists and is not empty. Everything below is vacuous without it."""
    assert path.is_file(), (
        f"{path.relative_to(ROOT)} is not committed. `floatfea run "
        f"examples/platform12_placeholder.yaml` produces it, and `results/` is tracked."
    )
    assert path.stat().st_size > 0, path


def test_R838_FO2s_NINE_caveats_are_still_NINE() -> None:
    """The count, because the membership check cannot see a DELETED caveat (R838).

    **EH4's WEAKENING DIRECTION, WHICH R831's REPAIR LEFT OPEN.** R831 made the needle the
    caveat TEXT, which closed the direction where a caveat is REWORDED. It did nothing for
    the direction where one is REMOVED: the parametrisation is over `TABLE_CAVEATS`, so
    deleting an element deletes its own three cases. Measured by cutting `R743` out of the
    tuple:

        baseline                            42 passed
        one caveat DELETED from the tuple   39 passed, 0 failed

    Three cases vanished and nothing went red. **And the next `floatfea run` would publish
    artifacts carrying eight caveats, with this gate green on all eight**, because the
    comparison is code-subset-of-artifact in both halves.

    FO2 asks for nine caveats in all three artifacts and for a test that reddens when one
    is removed. The membership cases are the first half; this is the second.

    The reason it is a result and not a wording question, under FR1: the caveats are what
    say the axial column is tension-positive (R739) and that a column is an envelope bound
    rather than a stress (R740). A published CSV missing one of those is a published number
    a reader takes with the wrong sign or the wrong meaning.
    """
    # **NINE DISTINCT, NON-BLANK (R846).** `len(...) == 9` is green when a caveat is a
    # DUPLICATE of another (`len 9, distinct 8`) and when one is the empty string, and the
    # per-caveat membership test is green on an empty needle too because `"" in text`
    # cannot fail. Each of those publishes artifacts missing a caveat while this gate
    # certifies nine of nine. Measured at `46 passed, 0 failed` for all three injections
    # before this line.
    assert len({c.strip() for c in TABLE_CAVEATS if c.strip()}) == 9, (
        f"FO2 requires NINE DISTINCT, non-blank caveats. `TABLE_CAVEATS` has "
        f"{len(TABLE_CAVEATS)} entries and "
        f"{len({c.strip() for c in TABLE_CAVEATS if c.strip()})} distinct non-blank ones, "
        f"so a duplicate or an emptied caveat is publishing in place of a real one."
    )
    assert len(TABLE_CAVEATS) == 9, (  # not-a-tolerance: FO2's own count
        f"FO2 requires NINE caveats and `floatfea.cli.TABLE_CAVEATS` has "
        f"{len(TABLE_CAVEATS)}. If a caveat was deliberately retired, FO2 is what changes "
        f"first -- and the three published artifacts are regenerated in the same commit "
        f"(CP3), because this gate compares the code against the FILES."
    )


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_R838_the_SCREEN_DISCLAIMER_reaches_every_artifact(path: Path) -> None:
    """`LABEL` is the sentence that stops a screen being read as a code case.

    The other half of R838. Measured by rewording it and leaving the files alone:

        LABEL reworded    42 passed, 0 failed

    so nothing in the tree asserted that the disclaimer the code emits is the disclaimer
    the published files carry. It is checked here the same way the caveats are, against the
    committed artifacts and comma-normalised for the CSV writer.
    """
    # AN EMPTY DISCLAIMER CANNOT FAIL EITHER (R846). `LABEL = ""` gave 46 passed.
    assert LABEL.strip(), "LABEL is blank, so the disclaimer check below is vacuous"
    text = _normalised(path.read_text(encoding="utf-8", errors="replace"))
    assert _normalised(LABEL) in text, (
        f"{path.name} does not carry the screen disclaimer VERBATIM. It is the one "
        f"sentence saying this is not a code case, so a stale or missing copy is a "
        f"published artifact misdescribing what it is. Missing: {LABEL[:120]}"
    )


@pytest.mark.parametrize("index", range(len(TABLE_CAVEATS)), ids=lambda i: f"caveat{i}")
@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_every_caveat_reaches_EVERY_published_artifact(path: Path, index: int) -> None:
    """All nine caveats, VERBATIM, in all three files, one case per (file, caveat).

    **R815 IS WHY THIS IS PARAMETRISED THIS WAY.** The previous gate asserted four markers
    in one `for` loop over a single stub, and the other five grepped `0 0 0` across the
    report and both CSVs while it passed. One case per pair means a missing caveat names
    both the file and the caveat.

    **R831 IS WHY THE NEEDLE IS THE TEXT.** With the marker as the needle this was green on
    three deliverables publishing the pre-R829 wording, because `EX3` is in both wordings.
    Measured at that commit:

        results/R1/example/report.md          caveats: 9   NOT PRESENT verbatim: [4]
        results/R1/example/member_forces.csv  caveats: 9   NOT PRESENT verbatim: [4]
        results/R1/example/utilisation.csv    caveats: 9   NOT PRESENT verbatim: [4]

    The counter is a rewording: change one element of `TABLE_CAVEATS` and leave the files
    alone, and this reddens on three cases rather than staying green on 33.
    """
    caveat = TABLE_CAVEATS[index]
    # AN EMPTY NEEDLE CANNOT FAIL (R846): `"" in text` is True for every file.
    assert caveat.strip(), f"caveat {index} is blank, so its membership check is vacuous"
    text = _normalised(path.read_text(encoding="utf-8", errors="replace"))
    assert _normalised(caveat) in text, (
        f"{path.name} does not carry caveat {index} VERBATIM. A caveat reworded in "
        f"`floatfea/cli.py` and not regenerated into the files is R831, and the fix is to "
        f"re-run `floatfea run` AFTER the last edit to `cli.py` (CP3). Missing: "
        f"{caveat[:160]}"
    )


@pytest.mark.parametrize("path", (FORCES, UTILISATION), ids=lambda p: p.name)
def test_the_csv_header_is_COMMENTED_and_the_data_is_parseable(path: Path) -> None:
    """The header must be `#` lines, and the rows must still read as a CSV.

    A header written without the comment prefix would make every consumer's first data row
    a label, and `csv.DictReader` would take it as the field names.
    """
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    head = [line for line in lines if line.startswith("#")]
    # C23: NO MAGIC COUNT. This read `len(head) >= 20` against 40 actual lines, so it
    # would have passed with half the header missing -- a floor with 2x slack is not a
    # check, and "20" was a number nothing derived.
    #
    # Every PROVENANCE KEY instead, taken from the schema rather than counted: the key set
    # comes from `RunConfig.provenance()`, so adding a provenance field extends this check
    # automatically and dropping one from the writer fails it by name.
    from floatfea.run.config import load_config

    expected_keys = sorted(
        load_config(ROOT / "examples" / "platform12_placeholder.yaml").provenance()
    )
    blob = "\n".join(head)
    missing = [key for key in expected_keys if key not in blob]
    assert not missing, (
        f"{path.name}'s header is missing provenance key(s) {missing}. The header is the "
        f"label, the provenance, the build's assumptions, its findings and the column "
        f"caveats; a reader who cannot see what was configured cannot audit the run "
        f"(R806)."
    )
    rows = list(csv.DictReader([line for line in lines if not line.startswith("#")]))
    assert rows, f"{path.name} has a header and no data rows"
    for field in ("body", "member", "station", "basis"):
        assert field in rows[0], (field, sorted(rows[0]))


def test_the_published_report_does_not_DOUBLE_PREFIX_the_member() -> None:
    """R808, as a property of the FILE this time.

    The member label already carries its body, so `platform:platform:hub4_arm` is the
    defect. It survived a round because the fix was claimed in a commit message and
    verified on the console line only.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    for body in ("platform", "hub1", "hub2", "hub3", "hub4"):
        doubled = f"{body}:{body}:"
        assert doubled not in text, (
            f"{REPORT.name} publishes `{doubled}...`: the member label already carries its "
            f"body, so prefixing it again doubles it (R808)."
        )


def test_the_published_report_names_the_governing_station_in_full() -> None:
    """The governing row is NAMED, never summarised (`CLAUDE.md` forbids averaging).

    Member, station, period and clause, so an outlier cannot hide in a statistic.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## The governing utilisation" in text, text[:200]
    line = next(line for line in text.splitlines() if line.startswith("**U = "))
    for part in ("ROOT", "T_full", "basis", "governing clause"):
        assert part in line, (part, line)


def test_the_published_report_carries_the_mass_table_PER_BODY() -> None:
    """Five rows, one per body, with the residual formed from its own terms (G4.1)."""
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## Mass, per body" in text
    for body in ("platform", "hub1", "hub2", "hub3", "hub4"):
        assert f"| `{body}` |" in text, f"the mass table has no row for {body}"


def test_the_published_report_carries_the_BUILDS_OWN_findings() -> None:
    """R807: nine findings were computed and discarded. They are in the file now."""
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## Findings the build raised, per body" in text
    assert "MEASUREMENT" in text, (
        "five of the nine findings say the body is a MEASUREMENT and not one to ship; that "
        "is the half a reader of a published artifact most needs."
    )
    assert "11433" in text, "the equivalent densities must be reported (DZ5 / ER1(e))"


def test_a_NON_STUDY_run_carries_no_STUDY_label_anywhere() -> None:
    """The control for the study label: the shipped example is not a study.

    Without this, a generator that stamped every run would pass the study test and nobody
    would notice that the label had stopped meaning anything.
    """
    for path in ARTIFACTS:
        text = path.read_text(encoding="utf-8", errors="replace")
        assert "STUDY -- NOT FOR DESIGN" not in text, (
            f"{path.name} carries the study label and the example declares "
            f"`study_only: false`. A label on everything distinguishes nothing."
        )


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_R817_every_artifact_states_the_HEADING_and_the_WAVE_HEIGHT(path: Path) -> None:
    """The two facts the caveats are ABOUT (R817).

    The EX3/R724 caveat is about the heading and the EZ2/FA0 caveat is about the wave
    height's associated-period band, and neither value appeared in any artifact. The
    committed deliverables these replaced said "all cases are heading 0 degrees" and
    "H = 24.2 m" outright; the reworded caveat said "every case carries the heading its
    load cases declare", which in a file declaring no heading says nothing.

    Asserted per artifact, because carrying it in the report and not in the CSVs is the
    same defect one file over.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    assert "heading" in text.lower(), f"{path.name} does not state a heading"
    assert "0.0 deg" in text or "heading 0.0" in text, (
        f"{path.name} states no heading VALUE. The caveat about heading dependence is "
        f"unreadable without it."
    )
    assert "24.2" in text, (
        f"{path.name} states no wave height. EZ2's associated-period band is derived from "
        f"H, so a reader cannot check which periods may govern without it."
    )


def test_R818_the_report_states_the_SENSITIVITY_OPERATING_POINTS() -> None:
    """Two published columns had no operating point anywhere (R818).

    `utilisation_K_sens` and `utilisation_Cm_sens` are published per station. Run at a
    configuration the diff did not choose -- `K_sensitivity` equal to `K`,
    `Cm_sensitivity = 0.1` -- the two columns collapse onto the base on 32 of 32 rows and
    the header differed from the shipped run by ONE line, the config filename. A column
    whose operating point is unpublished cannot be read, and R743's caveat delegates the
    Cm direction to exactly that column.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "K_sensitivity" in text, "the report states no K sensitivity operating point"
    assert "Cm_sensitivity" in text, "the report states no Cm sensitivity operating point"


def test_R819_FQ0_the_artifacts_state_the_FLAT_D_over_t_ceiling() -> None:
    """The clause limits as FQ0 rules them, in all three artifacts.

    **THIS GATE PINNED THE WRONG NUMBER AND IS THE REASON TO DISTRUST A GATE WRITTEN
    BESIDE ITS OWN REPAIR.** R819 said the artifacts misstated two things, and I corrected
    them to `0.75*Fy IS compact` (right) and `300000/Fy[MPa] = 845.1` (wrong), then wrote
    this test to assert the wrong one. The reviewer's bisection found the code's first
    refusal at `734.3`, which matched neither, and FQ0 then ruled the ceiling is a FLAT
    `300` and named `300000/Fy` as FB1's own error.

    So three figures were published for one limit -- `845.1`, `734.3`, `300` -- and the
    gate asserted the first. What it checks now is the ruling, and it checks the CODE's
    boundary too, so a caveat and a clause cannot drift apart again.
    """
    from floatfea.basis import FY_S355
    from floatfea.checks.api_wsd import BENDING_THIRD_BRANCH_MAX_D_OVER_T, allowable_bending

    for path in ARTIFACTS:
        text = path.read_text(encoding="utf-8", errors="replace")
        assert "D/t <= 300" in text, f"{path.name} does not state FQ0's flat D/t <= 300 ceiling."
        assert (
            "300000/Fy" not in text
        ), f"{path.name} still carries FB1's grade-dependent reading, which FQ0 overruled."
        assert "845.1" not in text, f"{path.name} still carries the 845.1 figure."
        assert (
            "first reduction below the compact branch" not in text
        ), f"{path.name} still calls 0.75*Fy a reduction below compact; it IS compact."

    # AND THE CODE AGREES WITH THE CAVEAT, at the boundary and on both sides of it.
    # not-a-tolerance: FQ0's flat clause ceiling. API RP 2A-WSD section 3.2.3's third
    # range ends at a D/t of 300 in the standard's own text, so this pins a CLAUSE
    # CONSTANT against the caveat the artifacts publish -- not a comparison epsilon.
    assert BENDING_THIRD_BRANCH_MAX_D_OVER_T == 300.0  # not-a-tolerance: a clause constant
    allowable_bending(d_outer=2.5, wall=2.5 / 300.0, fy=FY_S355)  # must not raise
    with pytest.raises(ValueError, match="the flat upper limit"):
        allowable_bending(d_outer=2.5, wall=2.5 / 300.01, fy=FY_S355)
    # FLAT: the ceiling does not move with grade, which is the whole content of FQ0.
    for fy in (235e6, 355e6, 460e6, 690e6):
        with pytest.raises(ValueError, match="the flat upper limit"):
            allowable_bending(d_outer=2.5, wall=2.5 / 300.01, fy=fy)


def test_R1156_the_Cm_caveat_names_the_CLAUSE_THE_TERM_IS_IN_and_the_CODE_AGREES() -> None:
    """R1156: the published caveat attributed `C_m`'s term to the wrong clause.

    **FOUND BY THE FL3 WITNESS, WHICH IS WHAT THE WITNESS IS FOR.** A fresh-context
    agent following only `docs/USER_GUIDE.md` changed `code_check.Cm` from `0.85` to
    `1.2`, found `U` rising `1.71167 -> 2.05621`, and then found that every row that
    moved reads `3.3.2 interaction` while all six rows reading `3.3.1 interaction` were
    bit-identical -- against a caveat, published in all three artifacts, saying `C_m`
    multiplies the bending term in "section 3.3.1's interaction".

    The two facts the old sentence ran together, and both are true:

    * the VALUE `0.85` is tabulated in § 3.3.1 case (a), members in frames subject to
      joint translation -- which is what `CM_JOINT_TRANSLATION`'s docstring is about;
    * the TERM it multiplies is in § 3.3.2's amplified interaction, `u_axial + cm *
      u_bending / (1 - f_a/F_e')`, which `check_member` evaluates in the compression
      branch ONLY.

    So this gate checks the published sentence AND the code's own behaviour, which is
    `test_R819_FQ0_the_artifacts_state_the_FLAT_D_over_t_ceiling`'s shape and for its
    reason: a caveat and a clause must not be able to
    drift apart again. R743 already corrected this sentence's DIRECTION once, in
    `api_wsd.py`, and left the clause number wrong in `cli.py`.
    """
    # ---- the SOURCE, which is what a revert of the repair moves ------------------
    #
    # **THE FIRST VERSION OF THIS GATE CHECKED ONLY THE ARTIFACTS AND SO COULD NOT GO
    # RED ON A REVERT.** Reverting `cli.py`'s caveat and re-running left it PASSING,
    # because the regenerated files on disk still carried the corrected sentence -- the
    # artifacts lag the source until someone runs the example. FZ rule 5 asks for a row
    # that fails when the repair ALONE is reverted, and that row has to read
    # `TABLE_CAVEATS`. Measured: with this block present a revert of `cli.py` reddens
    # here; without it, the revert was green.
    cm_caveats = [c for c in TABLE_CAVEATS if "C_m" in c]
    assert len(cm_caveats) == 1, (  # not-a-tolerance: FO2's nine caveats, one about C_m
        f"expected exactly one caveat about C_m in `floatfea.cli.TABLE_CAVEATS`, found "
        f"{len(cm_caveats)}. If a second was added, this gate no longer knows which one "
        f"carries the clause attribution."
    )
    source = cm_caveats[0]
    assert "section 3.3.2's AMPLIFIED interaction" in source, (
        "`floatfea.cli.TABLE_CAVEATS` does not attribute C_m's term to section 3.3.2. "
        "This is the source of the sentence published in all three artifacts, so it is "
        "what a revert of R1156 moves."
    )
    assert "section 3.3.1's interaction" not in source, (
        "`floatfea.cli.TABLE_CAVEATS` still says C_m multiplies the bending term in "
        "section 3.3.1's interaction. 3.3.1 is tension + bending and carries no C_m."
    )
    # R1162: the DIRECTION the same sentence states. It said a larger C_m "RAISES" the
    # compression utilisation, unconditionally; `u_combined = max(amplified, simple)`
    # makes it non-decreasing and flat below the overtake. The control is at the foot of
    # this test.
    assert "NEVER LOWERS" in source and "NON-DECREASING" in source, (
        "`floatfea.cli.TABLE_CAVEATS` states C_m's direction without the bound R1162 "
        "names. The column is `max(amplified, simple)`, so a larger C_m cannot lower it "
        "and does not always raise it."
    )
    # R1168: and the SECOND clause of the same sentence needed the same treatment.
    # "RAISES it wherever the amplified form governs" is false for a compression member
    # with no bending term: the amplified form governs and the column is flat, because
    # `cm * u_bending` is `cm * 0`. `docs/USER_GUIDE.md:260` already carried the
    # qualifier and the caveat did not, so the two deliverables disagreed. The control
    # is the zero-moment member at the foot of this test.
    # R1174: THE SECOND REPAIR WAS ALSO A COUNT, AND IT WAS ALSO WRONG. R1168's fix said
    # the response is "FLAT in two places" and named the overtake and the vanishing
    # bending term. There is a third and on the shipped table it is the DOMINANT one:
    # `utilisation` is the MAXIMUM over clauses and C_m enters only `3.3.2 interaction`,
    # so where shear governs AT THE PUBLISHED C_m the column does not move. Measured on
    # the shipped artifact: of 32 rows, 7 are `amplified` and all 7 are flat -- 5
    # governed by `3.2.4 beam shear` with `u_bending` up to 3.84e-3, and 2 with a
    # vanishing bending term.
    #
    # R1178: AND THE THIRD REPAIR STATED THAT THIRD CAUSE AS A UNIVERSAL, WHICH IS FALSE.
    # "a row governed by 3.2.4 shear is flat in C_m however large its bending term", with
    # the contrapositive "Anywhere else the published column is FLAT in C_m", published in
    # `floatfea/cli.py` and all three artifacts. Causes (i) and (iii) are BOTH overtakes
    # -- `max()` over clauses and `max(amplified, simple)` -- and a larger C_m undoes
    # either, though not necessarily one inside the declared bounds: the kink
    # `(B - a)/s` decides, and the shear fixture below has it at 3.04. So neither the
    # governing clause nor the interaction form is a property of the row. Re-measured at
    # each row's own state on the shipped
    # `utilisation.csv` the condition set was satisfied by 2 rows that are flat and
    # violated by all 10 that rise, the headline row among them.
    #
    # So the caveat now states the CLOSED FORM instead of a condition set over the row's
    # own columns, and what is pinned here is that form's own words, the retraction of
    # the universal, and -- at the foot of this test -- the two digits it publishes,
    # re-derived from the model. A needle can only test that a sentence is PRESENT; the
    # controls at the foot are what test whether it is TRUE.
    assert "THE LARGER OF B AND a + C_m*s" in source, (
        "`floatfea.cli.TABLE_CAVEATS` does not state the closed form the published "
        "column has in C_m. `utilisation` is `max()` over clauses and `u_combined` is "
        "`max(amplified, simple)`, so the column is exactly `max(B, a + C_m*s)` with B, "
        "a and s free of C_m -- a kink, not a condition set. R1178 is that a condition "
        "set over `governing_clause` and `interaction_form` is false in both directions."
    )
    assert "PREDICT" in source and "NOTHING ABOUT ANY OTHER C_m" in source, (
        "`floatfea.cli.TABLE_CAVEATS` has gone back to describing a row's C_m exposure "
        "from its `governing_clause` or `interaction_form` column. Those columns are the "
        "row AT THE C_m THIS RUN USED; the crossover control at the foot of this test is "
        "a row governed by a shear clause at 0.85 and by 3.3.2 at 2.00."
    )
    assert "NO COUNT OF" in source, (
        "`floatfea.cli.TABLE_CAVEATS` has gone back to counting the flat cases. R1168 "
        "said two, R1174 found a third; how many rows are flat is a property of the "
        "table, not of the clause, so the caveat states the closed form instead."
    )

    # ---- the published sentence, in every artifact -------------------------------
    for path in ARTIFACTS:
        text = _normalised(path.read_text(encoding="utf-8", errors="replace"))
        assert "section 3.3.2's AMPLIFIED interaction" in text, (
            f"{path.name} does not attribute C_m's term to section 3.3.2. R1156 is that "
            f"it said 3.3.1, which is the clause the VALUE comes from and not the clause "
            f"the TERM is in."
        )
        assert "section 3.3.1's interaction" not in text, (
            f"{path.name} still says C_m multiplies the bending term in section 3.3.1's "
            f"interaction. It does not: 3.3.1 is tension + bending and carries no C_m."
        )
        assert "section 3.3.1 case" in text, (
            f"{path.name} dropped where the VALUE 0.85 comes from. Correcting the clause "
            f"of the term must not delete the true fact the old sentence contained."
        )
        assert "NEVER LOWERS" in text and "NON-DECREASING" in text, (
            f"{path.name} states C_m's direction without R1162's bound. `u_combined` is "
            f"`max(amplified, simple)`, so C_m is FLAT below the value at which the "
            f"amplified form overtakes the simple one -- the control at the foot of this "
            f"test measures that band at its own member."
        )
        assert "THE LARGER OF B AND a + C_m*s" in text, (
            f"{path.name} does not carry the closed form the published column has in "
            f"C_m (R1178). It carried a condition set over `governing_clause` and "
            f"`interaction_form` instead, and that set is false in both directions: it "
            f"held on 2 rows of this file that are flat and failed on all 10 that rise."
        )
        assert "NOTHING ABOUT ANY OTHER C_m" in text, (
            f"{path.name} does not retract the prediction (R1178). A reader of these "
            f"columns has the row at ONE C_m, and both of the overtakes that can make a "
            f"row flat here are undone by a large enough C_m."
        )
        assert "NO COUNT OF" in text, (
            f"{path.name} counts the flat cases. R1168 said two and R1174 found a third; "
            f"a count over the author's own table is what went wrong twice here."
        )

    # ---- and the code, one variable moved ----------------------------------------
    from floatfea.checks.api_wsd import E_STEEL, FY_S355, check_member

    common: dict[str, float] = dict(
        shear_y_n=0.0,
        shear_z_n=0.0,
        torsion_nm=0.0,
        moment_y_nm=1.5e8,
        moment_z_nm=0.0,
        area_m2=1.3119290921390976,
        section_modulus_m3=0.7103833648114783,
        torsional_modulus_m3=1.4207667296229567,
        d_outer_m=2.5,
        wall_m=0.18,
        k_l_over_r=60.8,
        fy=FY_S355,
        e=E_STEEL,
    )

    # TENSION-POSITIVE (R739), so a positive axial is the 3.3.1 branch.
    tension_lo = check_member(axial_n=+6.0e6, cm=0.85, **common)  # type: ignore[arg-type]
    tension_hi = check_member(axial_n=+6.0e6, cm=1.20, **common)  # type: ignore[arg-type]
    compress_lo = check_member(axial_n=-6.0e6, cm=0.85, **common)  # type: ignore[arg-type]
    compress_hi = check_member(axial_n=-6.0e6, cm=1.20, **common)  # type: ignore[arg-type]

    assert "3.3.1" in tension_lo.governing, (
        f"the tension case does not reach a 3.3.1 clause -- it governs on "
        f"{tension_lo.governing!r}, so this control is not measuring the branch "
        f"it claims to."
    )
    assert "3.3.2" in compress_lo.governing, (
        f"the compression case does not reach a 3.3.2 clause -- it governs on "
        f"{compress_lo.governing!r}, so this control is not measuring the branch "
        f"it claims to."
    )
    # not-a-tolerance: EXACT equality. C_m does not enter 3.3.1's form at all, so the
    # tension utilisation is the same float, not a nearby one.
    assert tension_lo.utilisation == tension_hi.utilisation, (
        f"moving C_m from 0.85 to 1.20 moved the TENSION utilisation "
        f"{tension_lo.utilisation!r} -> {tension_hi.utilisation!r}. Section 3.3.1 carries "
        f"no C_m, so this would mean the caveat's clause attribution is wrong in the "
        f"other direction."
    )
    assert compress_hi.utilisation > compress_lo.utilisation, (
        f"moving C_m from 0.85 to 1.20 did not RAISE the compression utilisation "
        f"({compress_lo.utilisation!r} -> {compress_hi.utilisation!r}). R743's correction "
        f"was that a larger C_m gives a larger utilisation; if this fires, either the "
        f"direction or the branch has moved."
    )

    # ---- R1162: the response is NON-DECREASING, and the flat band is where ----------
    #
    # `u_combined = max(amplified, simple)` (`api_wsd.py:600-602`), so C_m is FLAT below
    # the value at which the amplified form overtakes the simple one, and the two
    # assertions above -- 0.85 against 1.20 -- step straight over that band without
    # measuring it. At THIS member the overtake is at `cm = 0.9757684714917533`
    # (bisected, 80 iterations, the reviewer's figure reproduced), so `0.90` is inside
    # the band and `1.20` is outside it. That is the published sentence as a control
    # rather than as prose, and it is the band R1163 recorded as unmeasured.
    compress_mid = check_member(axial_n=-6.0e6, cm=0.90, **common)  # type: ignore[arg-type]
    assert compress_mid.interaction_form == "simple", (
        f"at cm = 0.90 this member's interaction form is "
        f"{compress_mid.interaction_form!r}, not 'simple'. The flat band below the "
        f"overtake is what this control is about; if the member has moved so that the "
        f"amplified form already governs here, the band is elsewhere and this assertion "
        f"is measuring nothing."
    )
    # not-a-tolerance: EXACT equality. Below the overtake the simple form IS the column,
    # so the two are the same float and not nearby ones.
    assert compress_mid.utilisation == compress_lo.utilisation, (
        f"moving C_m from 0.85 to 0.90 moved the compression utilisation "
        f"{compress_lo.utilisation!r} -> {compress_mid.utilisation!r}, inside the band "
        f"where `max(amplified, simple)` returns `simple` at both. If this fires the "
        f"caveat's NON-DECREASING sentence is wrong in the strict direction."
    )

    # ---- R1168: FLAT WITH NOTHING TO MULTIPLY, WHICH IS THE OTHER CLAUSE -----------
    #
    # The band above is not the only place the column is flat, and the caveat's second
    # clause -- "RAISES it wherever the amplified form governs" -- was unconditional and
    # therefore false. A compression member with NO bending term reaches the AMPLIFIED
    # form, so the qualifier is not about which form governs: `cm * u_bending` is
    # `cm * 0` whatever C_m is. The reviewer found it by running a configuration the
    # repair had not chosen, which is R694's shape, and it is a zero-moment brace rather
    # than a degenerate case. C_m is swept to the top of its declared domain here --
    # `MOMENT_REDUCTION_CM = ("-", 0.1, 2.0)` -- so the row cannot pass by being narrow.
    no_bending: dict[str, float] = {**common, "moment_y_nm": 0.0}
    flat_lo = check_member(axial_n=-6.0e6, cm=0.85, **no_bending)  # type: ignore[arg-type]
    flat_hi = check_member(axial_n=-6.0e6, cm=2.00, **no_bending)  # type: ignore[arg-type]
    assert flat_lo.interaction_form == "amplified", (
        f"the zero-moment member's interaction form is {flat_lo.interaction_form!r}, "
        f"not 'amplified'. R1168 is that the AMPLIFIED form governs here and the column "
        f"is still flat; if the simple form governs instead, this row duplicates the "
        f"overtake band above and measures nothing new."
    )
    # not-a-tolerance: EXACT equality. `cm * 0.0` is `0.0` at every C_m, so these are
    # the same float and not nearby ones.
    assert flat_lo.utilisation == flat_hi.utilisation, (
        f"moving C_m from 0.85 to 2.00 moved the utilisation of a member with NO moment: "
        f"{flat_lo.utilisation!r} -> {flat_hi.utilisation!r}. There is no bending term "
        f"for C_m to multiply, so if this fires either the amplified form has acquired a "
        f"C_m-dependence outside the bending term or the moment is not actually zero."
    )

    # ---- R1174: FLAT BECAUSE ANOTHER CLAUSE GOVERNS, WHICH IS THE THIRD CAUSE --------
    #
    # This is the one the shipped table is actually full of, and the one two successive
    # repairs of this sentence missed: `utilisation` is `max()` over every clause and C_m
    # enters only `3.3.2 interaction`, so while another clause is the larger of the two
    # the published column does not move, whichever interaction form applies.
    #
    # The member below has a SUBSTANTIAL bending term and crosses the overtake inside the
    # swept range -- `simple` at 0.85, `amplified` from 1.00 -- so causes (ii) and (iii)
    # are both excluded by construction and only (i) can explain the flatness. Note the
    # two columns disagreeing: `u_combined` nearly doubles while `utilisation` is bit-exact.
    #
    # R1178: AND THIS ROW IS FLAT BY ITS TORSION MARGIN, NOT BY ANY UNIVERSAL. Bisected
    # at the reviewer's request: the `3.2.4` assertion below holds down to
    # `torsion_nm = 330811663.0070415` and the shipped fixture is `5.0e8`, a margin of
    # 1.51x. Just below it this member becomes the crossover control that follows. So
    # this row measures that the two COLUMNS can disagree; it is not evidence that a
    # shear-governed row cannot move, and the caveat no longer says that it is.
    shear_governed: dict[str, float] = {**common, "torsion_nm": 5.0e8}
    shear_lo = check_member(axial_n=-6.0e6, cm=0.85, **shear_governed)  # type: ignore[arg-type]
    shear_hi = check_member(axial_n=-6.0e6, cm=2.00, **shear_governed)  # type: ignore[arg-type]
    assert "3.2.4" in shear_lo.governing and "3.2.4" in shear_hi.governing, (
        f"this control needs a row governed by a SHEAR clause at both ends; it governs on "
        f"{shear_lo.governing!r} and {shear_hi.governing!r}. If 3.3.2 governs here the "
        f"row is measuring the overtake again instead of the max-over-clauses cause."
    )
    assert shear_lo.u_bending > 0.0 and shear_lo.interaction_form != shear_hi.interaction_form, (
        f"this control needs a real bending term and a crossing of the overtake, so that "
        f"neither of the other two causes can explain the flatness: u_bending="
        f"{shear_lo.u_bending!r}, forms {shear_lo.interaction_form!r} -> "
        f"{shear_hi.interaction_form!r}."
    )
    assert shear_hi.u_combined > shear_lo.u_combined, (
        f"C_m did not move `u_combined` on this member ({shear_lo.u_combined!r} -> "
        f"{shear_hi.u_combined!r}), so the row cannot show the two columns disagreeing, "
        f"which is the whole point of it."
    )
    # not-a-tolerance: EXACT equality. A clause C_m does not enter returns the identical
    # float at every C_m, so these are the same float and not nearby ones.
    assert shear_lo.utilisation == shear_hi.utilisation, (
        f"moving C_m from 0.85 to 2.00 moved the PUBLISHED utilisation of a row governed "
        f"by {shear_lo.governing!r}: {shear_lo.utilisation!r} -> {shear_hi.utilisation!r}. "
        f"C_m enters no clause but 3.3.2, and the column is the maximum over clauses, so "
        f"if this fires either C_m has reached another clause or the max is not taken."
    )
    # And flat across the DECLARED ENDS, which is what the caveat claims of this member:
    # `(B - a)/s exceeds 2.0`, measured at 3.04. A kink above the ceiling IS the statement
    # that the column does not move anywhere in `MOMENT_REDUCTION_CM`'s own 0.1 .. 2.0, so
    # the two ends are where it is checked. Without this, 0.85 and 2.00 leave the claim
    # unmeasured below 0.85 -- which is the shape R1163 recorded for the overtake band.
    shear_floor = check_member(axial_n=-6.0e6, cm=0.10, **shear_governed)  # type: ignore[arg-type]
    # not-a-tolerance: EXACT equality, for the reason above.
    assert shear_floor.utilisation == shear_hi.utilisation, (
        f"this member is NOT flat across C_m's declared domain: at cm = 0.10 it is "
        f"{shear_floor.utilisation!r} and at 2.00 it is {shear_hi.utilisation!r}. The "
        f"caveat publishes it as the row whose kink (B - a)/s is above the ceiling, so "
        f"if this fires that figure is stale and the published example is wrong."
    )

    # ---- R1178: AND NEITHER COLUMN IS A PROPERTY OF THE ROW -------------------------
    #
    # The R1174 repair stated the three causes above as a NECESSARY condition set and
    # then published the contrapositive: "Anywhere else the published column is FLAT in
    # C_m". Causes (i) and (iii) are both OVERTAKES, and a large enough C_m undoes
    # either, so a row whose `governing_clause` column reads a shear clause at the
    # published C_m can be governed by 3.3.2 at a larger one. Only cause (ii) -- the
    # vanishing bending term, the control above -- is flat at every C_m.
    #
    # THIS ROW REDDENS IF THE UNIVERSAL IS RESTORED, because it asserts that the
    # published utilisation RISES on a row governed by a shear clause at the low end. It
    # is the member the caveat now cites, inside `MOMENT_REDUCTION_CM`'s declared bounds
    # `("-", 0.1, 2.0)`, and `tests/corpus/cm_condition_set_necessity.txt` carries the
    # reviewer's ten entries on the same axis.
    crossover: dict[str, float] = {**common, "torsion_nm": 1.65125628e8}
    cross_lo = check_member(axial_n=-6.0e6, cm=0.85, **crossover)  # type: ignore[arg-type]
    cross_hi = check_member(axial_n=-6.0e6, cm=2.00, **crossover)  # type: ignore[arg-type]
    assert "3.2.4" in cross_lo.governing and cross_lo.interaction_form == "simple", (
        f"this control needs a row that reads as C_m-free in BOTH published columns at "
        f"the low end -- a shear clause and the simple form -- and it governs on "
        f"{cross_lo.governing!r} with form {cross_lo.interaction_form!r}. If 3.3.2 "
        f"already governs here the row cannot show that those columns predict nothing."
    )
    assert "3.3.2" in cross_hi.governing, (
        f"at cm = 2.00 this member governs on {cross_hi.governing!r}, not a 3.3.2 "
        f"clause. The whole point of the row is that the governing clause CHANGES "
        f"inside C_m's declared bounds, so if this fires the crossover has moved out of "
        f"range and the caveat's counter-example is no longer this member."
    )
    # not-a-tolerance: EXACT equality. The bending term carries no C_m, so these are the
    # same float and not nearby ones -- the rise below cannot be a larger moment.
    assert cross_lo.u_bending == cross_hi.u_bending, (
        f"the bending term moved with C_m on this member: {cross_lo.u_bending!r} -> "
        f"{cross_hi.u_bending!r}. C_m multiplies that term inside 3.3.2's amplified form "
        f"and is not part of the term itself, so if this fires the rise asserted below "
        f"is not the one this control claims to measure."
    )
    assert cross_hi.utilisation > cross_lo.utilisation, (
        f"moving C_m from 0.85 to 2.00 did NOT raise the published utilisation of this "
        f"member ({cross_lo.utilisation!r} -> {cross_hi.utilisation!r}), which governs "
        f"on {cross_lo.governing!r} at the low end. R1178 is that a condition set over "
        f"`governing_clause` and `interaction_form` is false in this direction: if this "
        f"assertion is green the universal the caveat used to publish is refuted, and "
        f"if it fires the universal is back."
    )
    # The caveat publishes these two digits in `floatfea/cli.py` and all three artifacts.
    # BP0: re-derived here, so a formulation change that moves them cannot leave the
    # published sentence describing a member this code no longer produces.
    for figure in (f"{cross_lo.utilisation:.6f}", f"{cross_hi.utilisation:.6f}"):
        assert figure in source, (
            f"`floatfea.cli.TABLE_CAVEATS` does not carry {figure}, which is this "
            f"member's published utilisation at one of the two C_m values the caveat "
            f"names. The sentence cites a measurement; this is the measurement."
        )
        for path in ARTIFACTS:
            text = _normalised(path.read_text(encoding="utf-8", errors="replace"))
            assert figure in text, (
                f"{path.name} does not carry {figure}. The caveat's counter-example is "
                f"published in every artifact, so a stale copy is a published figure "
                f"that no longer describes this code."
            )
    # And the direction over the WHOLE declared domain, exactly: `max(B, a + C_m*s)` with
    # s >= 0 is non-decreasing, which is the caveat's NON-DECREASING sentence as a
    # measurement rather than as a needle. No tolerance: `<=` on consecutive samples.
    swept = [
        check_member(  # type: ignore[arg-type]
            axial_n=-6.0e6, cm=0.1 + i * (1.9 / 190.0), **crossover
        ).utilisation
        for i in range(191)
    ]
    assert all(lo <= hi for lo, hi in zip(swept, swept[1:], strict=False)), (
        "the published utilisation FELL somewhere in C_m over the declared bounds "
        "0.1 .. 2.0 on the crossover member. The column is the larger of a C_m-free "
        "channel and a term affine and increasing in C_m, so it cannot fall; the first "
        "drop is at index "
        + str(next(i for i, (lo, hi) in enumerate(zip(swept, swept[1:], strict=False)) if lo > hi))
    )
    assert swept[0] < swept[-1], (
        f"the crossover member is FLAT across the whole declared C_m domain "
        f"({swept[0]!r} -> {swept[-1]!r}), so it is not the counter-example the caveat "
        f"cites and this control measures nothing."
    )
