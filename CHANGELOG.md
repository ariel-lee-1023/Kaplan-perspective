# Changelog

## Activation entry (2026-09-17)

- Require full reading of the core, voice and frameworks before the first substantive
  response, including short answers, with module roles and context recovery rules.
- Align current loading instructions and usage documentation; retain conditional
  topic and work modules. This changes runtime loading only. No recognition or fidelity
  evaluation was rerun; prior results retain their original input scope.

## 2026-09-12 — default project persona

Added the existing local `AGENTS.md` to the repository and clarified selective reference loading. Project conversations default to the root Kaplan persona, while explicit mode changes and repository maintenance remain available. Documented the standard filename and project usage in README.

## 2026-09-12 — standalone root layout

Moved the existing `SKILL.md` and `references/` contents to real files and directories at the repository root, following Leopold-Kohr-perspective. Removed the nested `.agents/skills/` package and both root symbolic links. Updated usage paths and validators. Runtime content and its fidelity hash are unchanged.

## 2026-09-11 — corpus rebuild

Rebuilt the persona from seven local books using Persona-Distiller’s evidence, curation, register, and modular-loading design. Added five measured writing modes, ordered decision procedures, qualified standing judgments, accountability for Iraq and the reception of *Balkan Ghosts*, and substantial literary and travel depth. Removed unsupported generic interaction rules. Replaced the recursive skill symlink with a canonical lowercase runtime directory and compatible root links. Added reproducible structural and artifact checks, disclosed failed and limited fidelity checks, and preserved the previous audit as superseded history.

All notable changes to this skill are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **`provenance.md` moved out of `references/` into a new top-level `fidelity-ledger/` folder.**
  `references/` is loaded by the host agent at runtime, so the fidelity ledger now lives at
  `fidelity-ledger/provenance.md`, a sibling of `references/` rather than a member of it —
  structurally out of reach during embodiment, not just documented as off-limits. Content
  unchanged; only the path moved. `SKILL.md`, `README.md` (including the repository-layout tree,
  which now also lists `NOTICE.md`), and `.github/workflows/validate.yml` (the required-file check)
  updated to point at the new location.
- **`episodic.md` moved out of `references/` into `fidelity-ledger/`, alongside `provenance.md`.**
  Lower-priority attested material is not reasoning the host agent should load mid-embodiment, so
  it belongs with the fidelity ledger rather than the host-agent-facing package. Content unchanged;
  only the path moved, to `fidelity-ledger/episodic.md`. `SKILL.md`, `README.md`'s layout tree, and
  `.github/workflows/validate.yml`'s required-file check updated to point at the new location.
- **Loading depth now states a real-world-retrieval rule, distinct from the corpus-internal
  lookup.** `references/` and `fidelity-ledger/` answer questions about his own frame and voice,
  corpus-internal by design; they were never meant to stand in for a fact about the world — who
  holds power where today, a current conflict's state, a country's present alignment — especially
  given this persona's subject is contemporary great-power geography and the essays run only
  through 2023. `SKILL.md` now says so explicitly: retrieve such a fact before running it through
  the frame, and do not treat the corpus as either currently accurate or as the limit of what the
  frame can be turned on.

### Planned
- Registers for the temporal gaps (1994–1999, 2002–2011, 2013–2017), if source material supports them
- Sharper confidence boundaries for economics and domestic-policy questions, where the persona currently extrapolates
- Live-exchange material, if any becomes available, to firm up the reconstructed interactional moves

## [1.0.0] — 2026-07-22

Initial public release.

### Added
- `SKILL.md` — persona core: how I read a question, what I will not concede, how I move in an exchange, how I sound, what I keep returning to
- `references/frameworks.md` — Kaplan's named constructs (the revenge of geography, the coming anarchy, a pagan ethos, thinking tragically, order before freedom, constructive pessimism, Heartland/Rimland/shatter-zones, a concert of civilizations, the map tells many contradictory stories) plus the recurring chorus of authorities
- `references/episodic.md` — attested but lower-priority material: reconstructed interactional moves, demoted expression features, expanded preoccupations, and an explicit list of what was cut
- `references/provenance.md` — full fidelity ledger: weight vector, core element scores, gate results, style-match modulation check, and confidence caveats
- `references/clusters/` — seven per-book register profiles covering 1993 through 2023
- Repository scaffolding: `README.md`, `LICENSE`, `.gitignore`, `CHANGELOG.md`, and a structure-validation workflow

### Notes
- Distilled from seven single-authored books (~562k words) via a `persona-distiller` pipeline in full-rigor mode
- Projection gate: 0.893 overall, 1.0 on strong domains, 0.25 on weak domains — the persona degrades sharply off home turf, and this is documented rather than hidden
- Cost gate: 5/5 high-signal divergences retained in the core
- M1 (ground → map → moral modulation) was elevated to the core below the 0.55 composite cut under the variation and sparsity-protection rules; the elevation is logged in `provenance.md`
- Interactional moves are reconstructed from monologic prose; the corpus contains no interviews, debates, or decision records

[Unreleased]: https://github.com/ariel-lee-1023/Kaplan-perspective/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ariel-lee-1023/Kaplan-perspective/releases/tag/v1.0.0
