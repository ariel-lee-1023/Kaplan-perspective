# Changelog

All notable changes to this skill are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
