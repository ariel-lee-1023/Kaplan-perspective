# Robert D. Kaplan — perspective

A persona skill rebuilt from seven supplied books using this project’s **Persona-Distiller** method. It joins geography, historical comparison, political order, travel, and literature in a working account of judgment. It is an interpretive tool, not writing authored or endorsed by Robert D. Kaplan.

The central question is what changes a recommendation: the successor authority after an intervention, the resources consumed elsewhere, the historical analogy that actually fits, and the person who must live with the consequences. The later reckoning with Iraq and *Balkan Ghosts* constrains the earlier confidence. Geography establishes pressures without abolishing choice; tragedy preserves responsibility without requiring despair.

## Start here

The persona lives directly in [SKILL.md](SKILL.md), with real files under [references/](references/), following the standalone layout of [Leopold-Kohr-perspective](https://github.com/ariel-lee-1023/Leopold-Kohr-perspective). There are no symbolic links or nested copies of the skill.

```text
Kaplan-perspective/
├── SKILL.md
├── references/
│   ├── frameworks.md
│   ├── voice.md
│   └── clusters/          # seven depth modules
├── fidelity-ledger/       # provenance, episodes, and test records
├── scripts/               # package validation
├── .github/workflows/     # automated validation
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md
└── README.md
```

For use as a file-based skill, copy `SKILL.md` and the complete `references/` directory into a directory named `kaplan-perspective` in the agent’s skill location. Alternatively, use the body of `SKILL.md` as a system prompt and load the referenced modules when needed. The audit files document the build and do not belong in the persona prompt.

Example requests:

- “Use $kaplan-perspective to assess the proposed intervention. Identify what would have to be true to justify it.”
- “Read this city description through the later Adriatic perspective, allowing the details to change the interpretation.”
- “Use the tragic frame to examine this leader’s decision. Preserve the legitimate obligation the choice sacrifices.”

The core handles short answers. It routes sustained writing to [voice.md](references/voice.md), extended reasoning to [frameworks.md](references/frameworks.md), and specialized questions to one relevant depth module. Contemporary applications require current evidence; invented travel memories, conversations, quotations, and attributed positions are excluded.

## Five writing modes

| Mode | Primary material | Function |
|---|---|---|
| Historical policy argument — default | *The Coming Anarchy*, *Warrior Politics*, *The Return of Marco Polo’s World* | Compare choices, instruments of power, and their costs. |
| Geographic exposition | *The Revenge of Geography* | Read terrain, routes, strategic reach, and changing constraints. |
| Early reported travel | *Balkan Ghosts* | Follow encounters, historical memory, and the pressure of place. |
| Late literary travel | *Adriatic* | Let art, reading, and overlapping identities revise the observer. |
| Tragic literary reflection | *The Tragic Mind* | Examine conscience, ambition, incompatible duties, and consolation. |

Seven depth modules retain the distinctions within each work. Their dates identify publications or the established module labels, not the composition date of every collected essay. The default understanding incorporates later corrections; an explicitly requested historical mode can recover an earlier stance with its limits.

## What changed in this rebuild

The previous package reduced Kaplan to a handful of geopolitical maxims and borrowed generic interaction rules from the distiller’s illustrative examples. The rebuild removes the unsupported refusal of numbers, permanent withholding of comfort, and use of dead authorities to settle objections. It restores actual discriminants, qualified standing judgments, literary attention, accountability, and measured differences among writing modes.

The core contains roughly 2,700 words. Depth is loaded selectively. The audit uses the distiller’s explicit heuristic token estimator rather than calling word counts or planning estimates model tokens.

## Evidence and limits

The seven local Markdown books were segmented into 98 chapter/essay units. All units received distributed reading samples, with deeper reading around diagnostic claims; this is not a claim of line-by-line close reading of seven pristine books. The *Balkan Ghosts* transcription is heavily damaged, and *Warrior Politics* requires text repair. Reported interviews do not provide evidence of Kaplan’s own live turn-taking.

Internal checks include reserved continuations, register discrimination, cost-bearing admissions, five prose samples, literal attestation, package structure, and calculated budgets. They exposed and corrected substantive errors. They are self-scored checks, not independent authentication of a simulated author. Late literary continuation remains less reliable, and short-sample hedge rates vary substantially.

The [rebuild audit](fidelity-ledger/provenance.md) preserves scores, misses, source hashes, the reading method, and the limits on each claim. The [episodic record](fidelity-ledger/episodic.md) separates concrete events from general traits. Audit files are separate from `SKILL.md` and `references/` and are not persona context. The superseded 2026-08-17 audit is retained as history, without inheriting its unverified claims.

## Validate

```sh
python3 scripts/validate.py
```

The validator checks canonical layout, reference resolution, frontmatter, retained cost-bearing material, budget arithmetic, artifact consistency, and runtime hashes. Full source texts are not distributed with this repository.

The [license](LICENSE) covers the repository’s original material; it does not grant rights to Kaplan’s books. Attribution and scope are described in [NOTICE.md](NOTICE.md).
