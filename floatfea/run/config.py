"""The declared run configuration: schema, units, ranges, and refusal (FL1(a)).

A configuration says what to analyse. It does not say what the answer is, and it cannot
reach past the declared fields into the model -- there is no `eval`, no import hook and
no free-form override. Every field below carries its UNIT and its ADMISSIBLE RANGE, and
a value outside that range is REFUSED with a message naming the field, the value, the
range and the unit. `CLAUDE.md`: never let a validation failure degrade to a warning.

**THE RANGES ARE NOT TOLERANCES, AND THE DISTINCTION IS WORTH STATING ONCE.**
`CLAUDE.md` puts every tolerance in `floatfea/tolerances.py`, and extends that to
"anything that functions as a tolerance under another name: convergence thresholds,
comparison epsilons, 'small number' guards, tier cutoffs in screening, and any factor
introduced to make two numbers agree." A bound here is none of those. It is the declared
DOMAIN of an input: no result is compared against it, no two numbers are made to agree by
it, and widening one cannot turn a red into a green -- it can only admit a configuration
that was previously refused outright. They live here because FL3(a) requires the user
guide to document "every config field with its unit and range", and a schema's own
documentation is where a reader looks for a schema's domain.

They are deliberately WIDE. The job of a bound here is to catch a unit mistake or a typo
-- `E: 210` in GPa where Pa is meant, a wall thicker than its own radius, a period of
zero -- and not to express engineering judgement about what is sensible. A configuration
inside these bounds is not thereby endorsed; it is merely not obviously nonsense.

**WHAT IS NOT CONFIGURABLE, BY DESIGN.** Body totals, centre of gravity and inertia come
FROM THE DECK (FL1(a)), never from the configuration. A config that tries to set them is
refused rather than ignored, because a silently ignored mass would be the exact failure
this project exists to prevent. The residual between what the configuration's mass
distribution accounts for and what the deck declares is COMPUTED and REPORTED, not
assumed to be zero.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final

import yaml

__all__ = [
    "ConfigError",
    "RunConfig",
    "load_config",
]


class _NoDuplicateLoader(yaml.SafeLoader):
    """A YAML loader that REFUSES a duplicate mapping key (R811).

    `yaml.safe_load` is last-wins and silent, which is the worst of the three possible
    behaviours. Measured on this schema before the fix: `Fy` given twice took 275 MPa over
    355, `platform.f` took 0.30 over 0.75, and `K` took 3.0 over 2.0 -- each a different
    structure analysed under a value the reader can see with their own eyes in the file and
    did not get.

    It is exactly the failure mode `_reject_unknown` exists to prevent, arriving by a
    route that check cannot see: the key IS known, and there are simply two of it. A diff
    that adds a field without removing the old one is how it happens, and nothing about
    the file looks wrong afterwards.
    """


def _refuse_merge_keys(node: Any) -> None:
    """Refuse a YAML merge key (R823). The input language does not widen silently.

    `<<: *anchor` merges another mapping's keys in. **It went from a hard
    `ConstructorError` to WORKING between two commits of mine**, as a side effect of
    routing mapping construction through a custom constructor, and merged keys bypass the
    duplicate check entirely because `flatten_mapping` runs inside `construct_mapping`,
    after the loop. Measured through the real schema: an anchored `platform: {f: 0.75}`
    merged into `hub1` and overridden gave `hub1 f = 0.1`.

    That is not a defect in YAML -- explicit keys winning over merged ones is the spec --
    but it is an **undeclared widening of the accepted input language**, which nothing
    documented and nothing tested. A configuration schema whose accepted language grows as
    a side effect of an unrelated repair is one nobody can review.

    Refused rather than supported, because the schema has no use for it: every section is
    a flat declared field set, `_reject_unknown` refuses anything it does not name, and a
    reader who wants two bodies to share a distribution can write it twice and have the
    duplicate check confirm they match.
    """
    for key_node, _value_node in node.value:
        if getattr(key_node, "tag", None) == "tag:yaml.org,2002:merge":
            raise ConfigError(
                f"merge key `<<` at line {key_node.start_mark.line + 1} is not accepted. "
                f"A merged mapping bypasses the duplicate-key check -- YAML flattens it "
                f"after this check runs -- and an explicit key silently overrides a merged "
                f"one, so a field could take a value from either place with nothing in the "
                f"file saying which. Write the fields out."
            )


def _no_duplicates(loader: yaml.SafeLoader, node: Any, deep: bool = False) -> Any:
    """Refuse a duplicate key, comparing the keys PyYAML will actually build (R822).

    **TWO CHECKS, BECAUSE ONE QUESTION HAS TWO ANSWERS AND BOTH MATTER.**

    The TEXT check catches a key written twice the same way and can name it and its line,
    which is what a reader needs in order to fix the file.

    The COUNT check catches everything else: `len(mapping) != len(node.value)` means
    PyYAML collapsed two entries into one, whatever made them equal. That is the check
    that holds R811's guarantee rather than approximating it.

    **R822 IS WHY THE SECOND ONE EXISTS, AND IT WAS MY DEFECT.** Keying only on
    `ScalarNode.value` keys on the key's TEXT, and PyYAML builds the mapping from the
    key's CONSTRUCTED value. YAML 1.1 implicit typing makes those different functions, so
    five classes of duplicate were silently last-wins -- `no`/`No` both `False`,
    `yes`/`true` both `True`, `~`/`null` both `None`, `1`/`01` both `1`, `1.0`/`1.00` both
    `1.0` -- which is R811's exact stated failure mode in a narrower form. Reachable
    through a declared field: `line_masses: {1: 100.0, 01: 900.0}` loaded as
    `{'1': 900.0}`, the first value gone, and `str(g)` made the collapsed key look like a
    legitimate group name.

    It got there because the text check was a repair for a TYPE error -- the construct
    call needed a stub-conditional `type: ignore` -- and I replaced the comparison instead
    of the call. The count check needs no construct call of its own, so it is typed in the
    pinned stubs with no ignore.

    **AND MY OWN COMMAND COULD NOT REFUTE IT**: all three of R811's parametrisations are
    text-identical duplicates, so they are green under either keying. The gate was
    parametrised over mapping DEPTH and the change moved key IDENTITY.

    `flatten_mapping` runs FIRST so the counts are comparable, and that is also where R823
    is refused -- see `_refuse_merge_keys`.
    """
    _refuse_merge_keys(node)

    seen: set[str] = set()
    for key_node, _value_node in node.value:
        if not isinstance(key_node, yaml.ScalarNode):
            # Every non-scalar value `SafeLoader` constructs is unhashable, so PyYAML
            # refuses such a document downstream with a located `ConstructorError`. There
            # is nothing to compare and nothing is lost by passing it on.
            continue
        key = str(key_node.value)
        if key in seen:
            raise ConfigError(
                f"duplicate key {key!r} at line {key_node.start_mark.line + 1}. YAML's "
                f"default is last-wins and silent, so the run would have used the second "
                f"value while the first sits in the file looking authoritative. Remove "
                f"one."
            )
        seen.add(key)

    mapping = loader.construct_mapping(node, deep)
    if len(mapping) != len(node.value):
        # The keys that collapsed, named by the TEXT the reader wrote rather than by the
        # value YAML turned it into -- `no` and `No` are what is in the file; `False` is
        # not.
        texts = [str(k.value) for k, _v in node.value if isinstance(k, yaml.ScalarNode)]
        raise ConfigError(
            f"{len(node.value)} keys in this mapping became {len(mapping)} after YAML's "
            f"implicit typing, so at least two of {texts} are THE SAME KEY and one value "
            f"was silently discarded. YAML 1.1 reads `no`, `No`, `false` and `off` as the "
            f"same boolean, `~` and `null` as the same null, and `1`, `01` and `1.0` as "
            f"the same number. Quote the keys you mean as strings, or remove the "
            f"duplicate."
        )
    return mapping


_NoDuplicateLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


class ConfigError(ValueError):
    """A configuration this tool refuses to run.

    A distinct type so a caller can tell "your configuration is wrong" from "the solve
    failed". The CLI prints it without a traceback, because a traceback for a typo in a
    YAML file tells the reader nothing they can act on.
    """


# ---------------------------------------------------------------------------
# The declared domain. (field, unit, low, high) -- inclusive both ends.
# ---------------------------------------------------------------------------
Bound = tuple[str, float, float]

TUBE_DIAMETER: Final[Bound] = ("m", 0.05, 50.0)
TUBE_WALL: Final[Bound] = ("m", 0.001, 2.0)
YOUNGS_MODULUS: Final[Bound] = ("Pa", 1.0e9, 1.0e12)
SHEAR_MODULUS: Final[Bound] = ("Pa", 1.0e8, 1.0e12)
DENSITY: Final[Bound] = ("kg/m^3", 100.0, 25000.0)
YIELD_STRESS: Final[Bound] = ("Pa", 1.0e6, 2.0e9)
MASS_FRACTION: Final[Bound] = ("-", 0.0, 1.0)
HEADING: Final[Bound] = ("deg", 0.0, 360.0)
WAVE_HEIGHT: Final[Bound] = ("m", 0.0, 100.0)
WAVE_PERIOD: Final[Bound] = ("s", 1.0, 100.0)
EFFECTIVE_LENGTH_K: Final[Bound] = ("-", 0.5, 3.0)
MOMENT_REDUCTION_CM: Final[Bound] = ("-", 0.1, 2.0)
LINE_MASS: Final[Bound] = ("kg/m", 0.0, 1.0e7)
LUMPED_MASS: Final[Bound] = ("kg", 0.0, 1.0e9)
FROUDE_LAMBDA: Final[Bound] = ("-", 1.0, 1000.0)


def _checked(value: Any, name: str, bound: Bound) -> float:
    """One number, inside its declared range, or a refusal naming all four facts."""
    unit, low, high = bound
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ConfigError(
            f"{name}: expected a number in {unit}, got {value!r} "
            f"({type(value).__name__}). The admissible range is [{low:g}, {high:g}] {unit}."
        )
    got = float(value)
    if got != got:  # NaN, which every comparison below would silently pass
        raise ConfigError(
            f"{name}: NaN is not a value. The admissible range is " f"[{low:g}, {high:g}] {unit}."
        )
    if not (low <= got <= high):
        raise ConfigError(
            f"{name}: {got:g} {unit} is outside the admissible range "
            f"[{low:g}, {high:g}] {unit}. If that value is intended, the range is "
            f"declared in floatfea/run/config.py and changing it is a reviewed change, "
            f"not a local override."
        )
    return got


def _require(mapping: Any, key: str, where: str) -> Any:
    if not isinstance(mapping, dict):
        raise ConfigError(f"{where}: expected a mapping of fields, got {type(mapping).__name__}.")
    if key not in mapping:
        raise ConfigError(
            f"{where}: required field {key!r} is missing. Present: "
            f"{sorted(mapping) or 'nothing'}."
        )
    return mapping[key]


def _require_string(value: Any, where: str) -> str:
    """A declared NAME or provenance string IS a string, or it is refused (R834, FQ1's argument).

    **THE SCALAR HALF OF `_require_name_keys`, AND THE COERCION FQ1 ORDERED DELETED SURVIVED
    HERE.** FQ1's letter covers "a mapping whose keys are names", so `lumped[].label` was
    outside it -- the same defect one field across. Measured before this check, through the
    real `load_config` on the shipped example with two lumped masses labelled `true`
    (unquoted) and `"True"` (quoted):

        LOADED. lumped labels: ["True", "True"]
        two DECLARED labels, both arrive as: ["True"]

    `LumpedMass.label` is the only identifier a point mass has, so two masses the reader
    distinguished became two masses with one name -- and an explicit `lumped_0` can collide
    with the `lumped_{i}` default. Nothing consumes a lumped mass yet; FL2 wires it, which
    is why this is named now rather than after the consumer ships.

    **AND THE REVIEWER NAMED ONE SITE; THERE WERE THREE.** `tag` and `window_rule` coerce the
    same way and both reach PUBLISHED provenance, so `tag: no` would publish `False` as the
    FloatSim tag. The schema's discipline is refuse-not-coerce -- `_checked` rejects a `bool`
    by name for every declared NUMBER -- and these were the declared STRINGS that did not.
    """
    if not isinstance(value, str):
        raise ConfigError(
            f"{where}: {value!r} ({type(value).__name__}) is not a string. YAML reads bare "
            f"words like `no`, `yes`, `true`, `null` and `~` as booleans and nulls, and bare "
            f"digits as numbers, so a name written without quotes arrives as a different "
            f"type and can collide with a quoted one. **Quote the name.**"
        )
    return value


def _require_name_keys(mapping: dict[Any, Any], where: str) -> None:
    """Every key of a NAME-KEYED mapping is a string, or the mapping is refused (FQ1/R825).

    **THIS IS THE LAYER BELOW THE DUPLICATE CHECK, AND R822's REPAIR DID NOT REACH IT.**
    `_no_duplicates` compares the keys PyYAML will build, so it catches `no`/`No` (both
    `False`) and `1`/`01` (both `1`). It is correctly SILENT when YAML builds two DISTINCT
    keys -- and `{true: 100.0, 'True': 900.0}` is exactly that: the bool `True` and the
    string `'True'` are different keys and PyYAML keeps both.

    Then the schema coerced with `str(g)`, both became `'True'`, and one of two declared
    line masses was gone. Measured before this check:

        line_masses: {true: 100.0, 'True': 900.0}  ->  {'True': 900.0}
        line_masses: {~: 100.0, 'None': 900.0}     ->  {'None': 900.0}

    and the same at `sections.groups`, where two declared tubes became one.

    So the coercion was the defect, not the comparison. These keys are NAMES -- member
    groups, body names -- and a name is a string: `true` is a boolean the reader did not
    mean and `1` is a number. Refused with "quote the name", because that is the fix the
    reader applies.
    """
    offenders = [key for key in mapping if not isinstance(key, str)]
    if offenders:
        shown = ", ".join(f"{key!r} ({type(key).__name__})" for key in offenders)
        raise ConfigError(
            f"{where}: the key(s) {shown} are not strings. These keys are NAMES, and YAML "
            f"reads bare words like `no`, `yes`, `true`, `null` and `~` as booleans and "
            f"nulls, and bare digits as numbers -- so a name written without quotes can "
            f"arrive as a different type and collide with a quoted one. **Quote the "
            f"name.**"
        )


def _reject_unknown(mapping: dict[str, Any], known: tuple[str, ...], where: str) -> None:
    """An unrecognised field is REFUSED, not ignored.

    A silently ignored field is how a configuration comes to mean something other than
    what it says -- the reader sets `fy: 420`, the tool runs at 355, and the report
    carries a number nobody asked for. Spelling is part of the interface.
    """
    unknown = sorted(set(mapping) - set(known))
    if unknown:
        raise ConfigError(
            f"{where}: unrecognised field(s) {unknown}. Known fields are "
            f"{sorted(known)}. A field this tool does not understand is refused rather "
            f"than ignored, because an ignored field means the run is not the run the "
            f"configuration describes."
        )


# ---------------------------------------------------------------------------
# The sections
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class TubeSection:
    """A circular hollow section, by outer diameter and wall thickness. SI, metres."""

    d_outer: float
    wall: float

    def validate(self, where: str) -> None:
        if self.wall >= 0.5 * self.d_outer:
            raise ConfigError(
                f"{where}: wall {self.wall:g} m is at least half the outer diameter "
                f"{self.d_outer:g} m, so the bore is zero or negative. A solid or "
                f"inverted section is not a tube."
            )


@dataclass(frozen=True)
class Material:
    """E, G, rho, Fy. SI throughout -- Pa, Pa, kg/m^3, Pa."""

    e: float
    g: float
    rho: float
    fy: float


@dataclass(frozen=True)
class Sections:
    """Per member group, plus the material they share.

    `groups` is keyed by member group. A group the deck has and the config does not is
    refused at build time rather than defaulted, which is the same rule as
    `_reject_unknown` in the other direction.
    """

    groups: dict[str, TubeSection]
    material: Material


# ---------------------------------------------------------------------------
# The mass distribution
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class LumpedMass:
    """A point mass at a declared position, in the body's own frame. kg and m."""

    label: str
    mass: float
    position: tuple[float, float, float]


@dataclass(frozen=True)
class MassDistribution:
    """How a body's mass is split between its members and the remainder.

    Exactly one of the two modes, per FL1(a):

    `fraction`  -- `f`, with DY0's remainder rule. The remainder's position is FORCED by
                   the deck's own CoG, not chosen: `z_r(f) = (z_cog - f z_joint)/(1 - f)`.
                   The PSD / realisability result is reported, never assumed.
    `explicit`  -- line masses per member group plus lumped masses with positions. The
                   residual against the deck's body total is computed and reported.

    **BODY TOTALS, CoG AND INERTIA ARE NOT HERE.** They come from the deck (FL1(a)). This
    object says how a known mass is DISTRIBUTED, not how much there is.
    """

    mode: str
    fraction: float | None = None
    line_masses: dict[str, float] = field(default_factory=dict)
    lumped: tuple[LumpedMass, ...] = ()


# ---------------------------------------------------------------------------
# The load cases
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class WaveCase:
    """One regular wave: heading, height, period. Full scale, SI."""

    heading_deg: float
    height_m: float
    period_s: float


@dataclass(frozen=True)
class LoadCases:
    """Either a committed npz of dynamic inputs, or the FloatSim runs to produce one.

    `npz` is FL1's path: "or a path to an existing dynamic-inputs npz". It is what makes
    step 1 runnable "on existing data" with no HSP worktree.

    `governing_periods` is the set allowed to SET THE ENVELOPE (EZ2). A case outside it
    is still computed and still reported, as sensitivity, and cannot govern. It is
    declared rather than derived because EZ2's associated-period rule is a decision about
    which waves are admissible for a given height, and FL2(d) makes the check per case.
    """

    npz: Path | None = None
    cases: tuple[WaveCase, ...] = ()
    governing_periods: tuple[float, ...] = ()
    window_rule: str = ""


# ---------------------------------------------------------------------------
# The code check and the outputs
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class CodeCheck:
    """API RP 2A-WSD options (FL1(a)).

    `k` and `cm` are the clause's own parameters and `one_third_increase` is section
    3.1.2's allowable-stress increase. None of the three is a tolerance: they are
    declared options of the code being applied, and the report states which were used.
    """

    k: float = 2.0
    cm: float = 0.85
    one_third_increase: bool = False
    k_sensitivity: float | None = 1.0
    cm_sensitivity: float | None = 1.0


@dataclass(frozen=True)
class Outputs:
    """Where the run writes, and which optional analyses run (FL2(b)).

    The two sizing analyses are OFF by default, per FL2(b). Under FM0 they propose from
    fixed forces and then re-solve; neither is part of step 1.
    """

    directory: Path
    report: bool = True
    member_forces_csv: bool = True
    utilisation_csv: bool = True
    required_section: bool = False
    truss_sizing: bool = False


@dataclass(frozen=True)
class FloatsimRef:
    """The deck the model is built from, and the scale it is read at.

    `deck` is a path to the exported deck YAML. `tag` records WHICH HSP state it came
    from, for provenance (ER1's mechanism, generalised): it is recorded and reported,
    never used to fetch anything.
    """

    deck: Path
    tag: str = ""
    froude_lambda: float = 50.0


def _or_none(value: float | None) -> str:
    """A declared option's value, or `(none)` when the run reports no sensitivity."""
    return "(none)" if value is None else f"{value:g}"


@dataclass(frozen=True)
class RunConfig:
    """One validated run. Every field is declared; nothing is inferred at use time."""

    source: Path
    floatsim: FloatsimRef
    mass_distribution: dict[str, MassDistribution]
    sections: Sections
    load_cases: LoadCases
    code_check: CodeCheck
    outputs: Outputs
    study_only: bool = False
    """FN1. A STUDY configuration: one the tool will build but will not vouch for.

    The default is `False`, and that is the point. Before R1, `build_superstructure()`
    descended `MASS_FRACTION_LADDER` consulting `admissible()` at every rung, so a body
    with a non-PSD remainder was UNREACHABLE. A configuration handing `f` in bypasses
    that ladder, which made `f = 1.0` (the whole body mass on the members) and `f = 0.0`
    (massless members) reachable for the first time -- and R810 measured both running to
    completion and PUBLISHING.

    With this flag, such a run is permitted and every output it writes says
    `STUDY -- NOT FOR DESIGN` in its label and header. Without it, the run refuses. The
    flag cannot be inferred from anything in the tree: ES1's reasoning about the
    sensitivity entry point applies to the configuration too -- a build made this way
    must not be mistakable for one to ship.
    """

    raw: dict[str, Any] = field(default_factory=dict)

    def _relative(self, path: Path) -> str:
        """A path as the configuration writes it, not as this machine spells it.

        The provenance block is printed into `results/**`, which is tracked, so an
        absolute path would commit one machine's home directory into a shared repository
        and make the artifact unreproducible anywhere else. Anchored on the config file's
        own directory, which is what the YAML's relative paths already resolve against,
        and falls back to the absolute path when the target is somewhere else entirely.
        """
        try:
            return str(path.relative_to(self.source.parent)).replace("\\", "/")
        except ValueError:
            pass
        try:
            return str(path.relative_to(self.source.parent.parent)).replace("\\", "/")
        except ValueError:
            return str(path)

    def provenance(self) -> dict[str, Any]:
        """What this run was, in a form a report can print and a reader can audit."""
        return {
            "config": self._relative(self.source),
            "deck": self._relative(self.floatsim.deck),
            "hsp_tag": self.floatsim.tag or "(not declared)",
            "froude_lambda": self.floatsim.froude_lambda,
            "mass_distribution": {
                body: (
                    f"f = {spec.fraction:g}"
                    if spec.mode == "fraction"
                    else f"explicit ({len(spec.line_masses)} groups, {len(spec.lumped)} lumped)"
                )
                for body, spec in sorted(self.mass_distribution.items())
            },
            "sections": {
                name: f"D = {sec.d_outer:g} m, t = {sec.wall:g} m"
                for name, sec in sorted(self.sections.groups.items())
            },
            "material": (
                f"E = {self.sections.material.e:g} Pa, G = {self.sections.material.g:g} Pa, "
                f"rho = {self.sections.material.rho:g} kg/m^3, "
                f"Fy = {self.sections.material.fy:g} Pa"
            ),
            "load_cases": (
                f"npz {self._relative(self.load_cases.npz)}"
                if self.load_cases.npz is not None
                else f"{len(self.load_cases.cases)} declared wave case(s)"
            ),
            "governing_periods_s": list(self.load_cases.governing_periods),
            # R812: DECLARED AND CONSUMED. This field was accepted, stored and read by
            # nothing -- not the provenance, not an artifact, not a test -- so a reader
            # could state the window rule their npz was exported under and have it reach
            # no output at all. It is a fact about the dynamic inputs, so it belongs
            # wherever those are described.
            "window_rule": self.load_cases.window_rule or "(not declared)",
            "study_only": ("YES -- STUDY, NOT FOR DESIGN" if self.study_only else "no"),
            # R818: THE SENSITIVITY OPERATING POINTS, which reach two PUBLISHED columns
            # and reached no artifact. Run at a configuration the diff did not choose --
            # `K_sensitivity` equal to `K`, `Cm_sensitivity = 0.1` -- the two columns
            # collapse onto the base on 32 of 32 rows and the header differed from the
            # shipped run by ONE line, the config filename. A column whose operating point
            # is unpublished cannot be read, and that is also the half of R743 the
            # rewording dropped: the caveat delegates the direction to a column nobody can
            # locate.
            "code_check_sensitivities": (
                f"K_sensitivity = {_or_none(self.code_check.k_sensitivity)}, "
                f"Cm_sensitivity = {_or_none(self.code_check.cm_sensitivity)}"
            ),
            "code_check": (
                f"K = {self.code_check.k:g}, Cm = {self.code_check.cm:g}, "
                f"one-third increase {'ON' if self.code_check.one_third_increase else 'OFF'}"
            ),
        }


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
_TOP = (
    "floatsim",
    "mass_distribution",
    "sections",
    "load_cases",
    "code_check",
    "outputs",
    "study_only",
)


def _parse_floatsim(block: Any, base: Path) -> FloatsimRef:
    where = "floatsim"
    _reject_unknown(
        block if isinstance(block, dict) else {}, ("deck", "tag", "froude_lambda"), where
    )
    deck = Path(_require_string(_require(block, "deck", where), f"{where}.deck"))
    if not deck.is_absolute():
        deck = (base / deck).resolve()
    if not deck.is_file():
        raise ConfigError(
            f"{where}.deck: {deck} does not exist. The deck is the authority for every "
            f"coordinate, every body total, the CoG and the inertia, so there is no "
            f"default and nothing is built without it."
        )
    lam = block.get("froude_lambda", 50.0)
    return FloatsimRef(
        deck=deck,
        tag=_require_string(block.get("tag", ""), f"{where}.tag"),
        froude_lambda=_checked(lam, f"{where}.froude_lambda", FROUDE_LAMBDA),
    )


def _parse_mass(block: Any) -> dict[str, MassDistribution]:
    where = "mass_distribution"
    if not isinstance(block, dict) or not block:
        raise ConfigError(
            f"{where}: expected a mapping of body name to a distribution, got "
            f"{type(block).__name__}. Every body the deck declares needs one."
        )
    # The BODY names are name keys too, by the same argument: `mass_distribution: {no: ...}`
    # would arrive as `False` and match no body the deck declares.
    _require_name_keys(block, where)
    forbidden = ("mass", "total_mass", "cog", "centre_of_gravity", "inertia")
    out: dict[str, MassDistribution] = {}
    for body, spec in block.items():
        here = f"{where}.{body}"
        # FL1(a): body totals, CoG and inertia come FROM THE DECK. Refused rather than
        # ignored, because an ignored mass is the failure mode this project exists to
        # prevent.
        #
        # **CHECKED BEFORE `_reject_unknown`, AND THE ORDER IS THE POINT.** Either order
        # refuses the run, so this is not about safety -- it is about which sentence the
        # reader gets. With the generic check first, `mass: 2.4e6` came back as
        # "unrecognised field(s) ['mass']", which invites someone to look for the right
        # spelling of a field that does not and must not exist. The specific message says
        # why there is no such field.
        present = [k for k in forbidden if isinstance(spec, dict) and k in spec]
        if present:
            raise ConfigError(
                f"{here}: {present} may not be set in a configuration. A body's total "
                f"mass, centre of gravity and inertia come FROM THE DECK (FL1(a)); this "
                f"block says only how that mass is DISTRIBUTED. Change the deck, or the "
                f"run would report a mass the deck does not have."
            )
        _reject_unknown(
            spec if isinstance(spec, dict) else {},
            ("f", "line_masses", "lumped"),
            here,
        )
        has_f = isinstance(spec, dict) and "f" in spec
        has_explicit = isinstance(spec, dict) and ("line_masses" in spec or "lumped" in spec)
        if has_f and has_explicit:
            raise ConfigError(
                f"{here}: `f` and an explicit distribution are both given. They are two "
                f"different ways to say the same thing and the tool will not guess which "
                f"one you meant."
            )
        if has_f:
            out[body] = MassDistribution(
                mode="fraction",
                fraction=_checked(spec["f"], f"{here}.f", MASS_FRACTION),
            )
            continue
        if not has_explicit:
            raise ConfigError(
                f"{here}: needs either `f` (a member mass fraction, with DY0's remainder "
                f"rule) or an explicit `line_masses` / `lumped` distribution."
            )
        lines = spec.get("line_masses", {}) or {}
        if not isinstance(lines, dict):
            raise ConfigError(
                f"{here}.line_masses: expected a mapping of member group to kg/m, got "
                f"{type(lines).__name__}."
            )
        _require_name_keys(lines, f"{here}.line_masses")
        line_masses = {
            g: _checked(v, f"{here}.line_masses.{g}", LINE_MASS) for g, v in lines.items()
        }
        lumped_raw = spec.get("lumped", []) or []
        if not isinstance(lumped_raw, list):
            raise ConfigError(
                f"{here}.lumped: expected a list of point masses, got "
                f"{type(lumped_raw).__name__}."
            )
        lumped: list[LumpedMass] = []
        for i, item in enumerate(lumped_raw):
            at = f"{here}.lumped[{i}]"
            _reject_unknown(item if isinstance(item, dict) else {}, ("label", "mass", "at"), at)
            pos = _require(item, "at", at)
            if not isinstance(pos, list) or len(pos) != 3:
                raise ConfigError(
                    f"{at}.at: expected [x, y, z] in metres, got {pos!r}. A lumped mass "
                    f"without a position cannot be placed, and FL1(a) asks for positions."
                )
            lumped.append(
                LumpedMass(
                    label=_require_string(item.get("label", f"lumped_{i}"), f"{at}.label"),
                    mass=_checked(_require(item, "mass", at), f"{at}.mass", LUMPED_MASS),
                    position=tuple(  # type: ignore[arg-type]
                        _checked(c, f"{at}.at[{j}]", ("m", -1.0e4, 1.0e4))
                        for j, c in enumerate(pos)
                    ),
                )
            )
        out[body] = MassDistribution(mode="explicit", line_masses=line_masses, lumped=tuple(lumped))
    return out


def _parse_sections(block: Any) -> Sections:
    where = "sections"
    _reject_unknown(block if isinstance(block, dict) else {}, ("groups", "material"), where)
    groups_raw = _require(block, "groups", where)
    if not isinstance(groups_raw, dict) or not groups_raw:
        raise ConfigError(
            f"{where}.groups: expected a mapping of member group to a tube, got "
            f"{type(groups_raw).__name__}."
        )
    _require_name_keys(groups_raw, f"{where}.groups")
    groups: dict[str, TubeSection] = {}
    for name, spec in groups_raw.items():
        here = f"{where}.groups.{name}"
        _reject_unknown(spec if isinstance(spec, dict) else {}, ("d_outer", "wall"), here)
        sec = TubeSection(
            d_outer=_checked(_require(spec, "d_outer", here), f"{here}.d_outer", TUBE_DIAMETER),
            wall=_checked(_require(spec, "wall", here), f"{here}.wall", TUBE_WALL),
        )
        sec.validate(here)
        groups[name] = sec

    mat_where = f"{where}.material"
    mat = _require(block, "material", where)
    _reject_unknown(mat if isinstance(mat, dict) else {}, ("E", "G", "rho", "Fy"), mat_where)
    material = Material(
        e=_checked(_require(mat, "E", mat_where), f"{mat_where}.E", YOUNGS_MODULUS),
        g=_checked(_require(mat, "G", mat_where), f"{mat_where}.G", SHEAR_MODULUS),
        rho=_checked(_require(mat, "rho", mat_where), f"{mat_where}.rho", DENSITY),
        fy=_checked(_require(mat, "Fy", mat_where), f"{mat_where}.Fy", YIELD_STRESS),
    )
    return Sections(groups=groups, material=material)


def _parse_load_cases(block: Any, base: Path) -> LoadCases:
    where = "load_cases"
    _reject_unknown(
        block if isinstance(block, dict) else {},
        ("npz", "cases", "governing_periods", "window_rule"),
        where,
    )
    npz_raw = block.get("npz")
    cases_raw = block.get("cases")
    if (npz_raw is None) == (cases_raw is None):
        raise ConfigError(
            f"{where}: give exactly one of `npz` (an existing dynamic-inputs file) or "
            f"`cases` (the FloatSim runs to produce one). Both or neither is ambiguous."
        )
    npz: Path | None = None
    if npz_raw is not None:
        npz = Path(_require_string(npz_raw, f"{where}.npz"))
        if not npz.is_absolute():
            npz = (base / npz).resolve()
        if not npz.is_file():
            raise ConfigError(
                f"{where}.npz: {npz} does not exist. `floatfea export` produces it from "
                f"FloatSim runs; `floatfea run` does not invent dynamic inputs."
            )
    cases: list[WaveCase] = []
    for i, item in enumerate(cases_raw or []):
        at = f"{where}.cases[{i}]"
        _reject_unknown(item if isinstance(item, dict) else {}, ("heading", "H", "T"), at)
        cases.append(
            WaveCase(
                heading_deg=_checked(_require(item, "heading", at), f"{at}.heading", HEADING),
                height_m=_checked(_require(item, "H", at), f"{at}.H", WAVE_HEIGHT),
                period_s=_checked(_require(item, "T", at), f"{at}.T", WAVE_PERIOD),
            )
        )
    periods_raw = block.get("governing_periods", []) or []
    if not isinstance(periods_raw, list) or not periods_raw:
        raise ConfigError(
            f"{where}.governing_periods: expected a non-empty list of full-scale periods "
            f"in seconds. This is the set EZ2 allows to SET THE ENVELOPE; a case outside "
            f"it is still computed and reported, as sensitivity, and cannot govern. "
            f"Leaving it unset would let any case govern silently."
        )
    periods = tuple(
        _checked(p, f"{where}.governing_periods[{i}]", WAVE_PERIOD)
        for i, p in enumerate(periods_raw)
    )
    if len(set(periods)) != len(periods):
        raise ConfigError(
            f"{where}.governing_periods: {list(periods)} contains a repeat. A period "
            f"counted twice would weight one case twice in the envelope."
        )
    return LoadCases(
        npz=npz,
        cases=tuple(cases),
        governing_periods=periods,
        window_rule=_require_string(block.get("window_rule", ""), f"{where}.window_rule"),
    )


def _parse_code_check(block: Any) -> CodeCheck:
    where = "code_check"
    block = block or {}
    _reject_unknown(
        block if isinstance(block, dict) else {},
        ("K", "Cm", "one_third_increase", "K_sensitivity", "Cm_sensitivity"),
        where,
    )
    one_third = block.get("one_third_increase", False)
    if not isinstance(one_third, bool):
        raise ConfigError(
            f"{where}.one_third_increase: expected true or false, got {one_third!r}. "
            f"Section 3.1.2's increase is written for a declared extreme event; it is on "
            f"or off, not scaled."
        )
    k_sens = block.get("K_sensitivity", 1.0)
    cm_sens = block.get("Cm_sensitivity", 1.0)
    return CodeCheck(
        k=_checked(block.get("K", 2.0), f"{where}.K", EFFECTIVE_LENGTH_K),
        cm=_checked(block.get("Cm", 0.85), f"{where}.Cm", MOMENT_REDUCTION_CM),
        one_third_increase=one_third,
        k_sensitivity=(
            None
            if k_sens is None
            else _checked(k_sens, f"{where}.K_sensitivity", EFFECTIVE_LENGTH_K)
        ),
        cm_sensitivity=(
            None
            if cm_sens is None
            else _checked(cm_sens, f"{where}.Cm_sensitivity", MOMENT_REDUCTION_CM)
        ),
    )


def _parse_outputs(block: Any, base: Path) -> Outputs:
    where = "outputs"
    block = block or {}
    known = (
        "directory",
        "report",
        "member_forces_csv",
        "utilisation_csv",
        "required_section",
        "truss_sizing",
    )
    _reject_unknown(block if isinstance(block, dict) else {}, known, where)
    # **R837: THE FOURTH DECLARED STRING, AND THE ONE THE DELIVERABLES LAND IN.**
    # Measured through the real `load_config` before this check:
    #
    #     directory: no   ->  Path("False")    LOADED
    #     directory: 12   ->  Path("12")       LOADED
    #     directory: ~    ->  Path("None")     LOADED
    #
    # Four lines below, `known[1:]` refuses all five of its sibling flags by name --
    # `outputs.report: expected true or false, got 'no'` -- so `directory: no` was the
    # one key in this block that took a boolean silently.
    # The three EZ0 artifacts then land in a directory named `False`.
    #
    # **FIVE OF FIVE SIBLINGS ARE BOOLEANS IN THE SHIPPED EXAMPLE, NOT THREE (R844).** The
    # `three` was verdict 7's figure and I pasted it here without re-measuring:
    #
    #     report true   member_forces_csv true   utilisation_csv true
    #     required_section false   truss_sizing false
    #
    # All five are written and all five are bools, which makes the typo MORE inviting than
    # the wrong figure suggested, not less.
    # **AND THE EMPTY STRING IS REFUSED AT THIS SITE (R843), WHICH IS EH4's WEAKENING
    # DIRECTION.** `_require_string` admits `""`, and `base / Path("")` is `base`, so
    # `directory: ""` resolved to the CONFIG FILE's OWN directory -- `examples/` for the
    # shipped example, which is TRACKED. Measured before this check:
    #
    #     directory: ''     LOADED -> <repo>/examples
    #     directory: '   '  LOADED -> <repo>/examples
    #
    # so the three published deliverables would have been written into the source tree.
    # `tag` and `window_rule` legitimately default to empty and do NOT get this check: a
    # directory that names nothing is the one case where empty is a DESTINATION rather
    # than a default.
    raw_dir = _require_string(block.get("directory", "results/run"), f"{where}.directory")
    if not raw_dir.strip():
        raise ConfigError(
            f"{where}.directory: an empty directory name resolves to the configuration "
            f"file's own directory, so the published artifacts would be written beside "
            f"the config -- inside the tracked source tree for the shipped example. Name "
            f"the directory, or leave the key out to take the `results/run` default."
        )
    directory = Path(raw_dir)
    if not directory.is_absolute():
        directory = (base / directory).resolve()
    flags: dict[str, bool] = {}
    for name in known[1:]:
        value = block.get(name, name in ("report", "member_forces_csv", "utilisation_csv"))
        if not isinstance(value, bool):
            raise ConfigError(f"{where}.{name}: expected true or false, got {value!r}.")
        flags[name] = value
    return Outputs(directory=directory, **flags)


def load_config(path: Path | str) -> RunConfig:
    """Read, validate and freeze one run configuration, or refuse it.

    Relative paths inside the file resolve against the FILE'S OWN directory, not the
    working directory, so a configuration means the same thing wherever it is run from.
    """
    source = Path(path).resolve()
    if not source.is_file():
        raise ConfigError(f"{source} does not exist.")
    try:
        loaded = yaml.load(source.read_text(encoding="utf-8"), _NoDuplicateLoader)
    except yaml.YAMLError as exc:
        raise ConfigError(f"{source} is not valid YAML: {exc}") from exc
    if not isinstance(loaded, dict):
        raise ConfigError(
            f"{source}: expected a mapping at the top level, got "
            f"{type(loaded).__name__}. The known sections are {sorted(_TOP)}."
        )
    _reject_unknown(loaded, _TOP, str(source.name))
    base = source.parent
    for section in ("floatsim", "mass_distribution", "sections", "load_cases"):
        if section not in loaded:
            raise ConfigError(
                f"{source.name}: required section {section!r} is missing. Present: "
                f"{sorted(loaded)}."
            )
    study_only = loaded.get("study_only", False)
    if not isinstance(study_only, bool):
        raise ConfigError(
            f"{source.name}: study_only must be true or false, got {study_only!r}. It "
            f"governs whether an inadmissible mass distribution is permitted at all, so "
            f"it is not a value to be coerced."
        )
    return RunConfig(
        source=source,
        study_only=study_only,
        floatsim=_parse_floatsim(loaded["floatsim"], base),
        mass_distribution=_parse_mass(loaded["mass_distribution"]),
        sections=_parse_sections(loaded["sections"]),
        load_cases=_parse_load_cases(loaded["load_cases"], base),
        code_check=_parse_code_check(loaded.get("code_check")),
        outputs=_parse_outputs(loaded.get("outputs"), base),
        raw=loaded,
    )
