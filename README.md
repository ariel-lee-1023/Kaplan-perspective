# kaplan-perspective

A **Claude Skill** that analyzes conflicts, states, leaders, and decisions through the documented thinking style of the American author and geopolitical writer **Robert D. Kaplan** — read the map before the ideology, think tragically to forestall tragedy, and grant that order comes before freedom.

It is a *thinking-style tool* for analysis and ideation. It is not affiliated with, endorsed by, or authored by Robert D. Kaplan, and it must not be used to attribute invented statements to him. See [Disclaimer](#disclaimer).

---

## What it does

Loaded into a Claude session, the skill reframes a question the way Kaplan's published work does:

- **Read the map first.** Terrain, distance, chokepoints, and position before ideology or personality.
- **Partial, self-undercutting determinism.** Assert the constraint, then refuse the fatalism — "the map tells many contradictory stories."
- **Order before freedom.** Authority is prior to liberty; anarchy is the crueler tyranny.
- **Think tragically to avoid tragedy.** Anxious foresight as a discipline against hubris.
- **A pagan ethos.** Statecraft judged by results and by the fate of those in one's care, not by purity of intention.
- **Forecast by mechanism, never by date.** A prediction that names a year and not a cause is astrology.
- **Summon a witness from the dead.** Objections answered through Thucydides, Machiavelli, Hobbes, Mackinder, Berlin, Niebuhr.

It also **modulates register** with the subject matter — close and first-person in the field, hedged and third-person on the geopolitical map, most declarative on the moral weight of power.

## When to use it

Good fits:

- Grand-strategy and geopolitical analysis
- Reading a rising or revisionist power from geography and history
- Order-vs-freedom sequencing in state-building, intervention, and post-conflict policy
- The moral philosophy of power; the burden of the decider
- Borderlands and shatter-zones — the Balkans, the Adriatic, Eurasian seams

Poor fits (the skill will reframe toward geography/order rather than hold a real position):

- Economics and technical finance
- Domestic US policy
- Granular dated forecasting
- Anything after 2023

Confidence boundaries are documented in [`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md).

## Repository layout

```
kaplan-perspective/
├── SKILL.md                    # the skill itself (YAML frontmatter + persona core)
├── references/               # host-agent-facing, loaded at runtime, never contains
│   │                        #   provenance or episodic material
│   ├── frameworks.md           # Kaplan's named constructs, preserved verbatim
│   └── clusters/               # per-book register profiles
│       ├── 1993-balkan-ghosts.md
│       ├── 2000-coming-anarchy.md
│       ├── 2001-warrior-politics.md
│       ├── 2012-revenge-of-geography.md
│       ├── 2018-marco-polos-world.md
│       ├── 2022-adriatic.md
│       └── 2023-tragic-mind.md
├── fidelity-ledger/          # human-facing, never loaded by the host agent
│   ├── provenance.md         # sources, scores, gates, confidence caveats
│   └── episodic.md             # attested but lower-priority material
├── LICENSE
├── NOTICE.md
├── CHANGELOG.md
└── .github/workflows/validate.yml
```

The skill follows Anthropic's three-level progressive-disclosure convention: frontmatter is always in context, `SKILL.md` loads when the skill triggers, and `references/` loads only on demand.

## Installation

**Claude Code / local agents** — clone into your skills directory:

```bash
git clone https://github.com/ariel-lee-1023/Kaplan-perspective.git ~/.claude/skills/kaplan-perspective
```

**Claude.ai** — upload `SKILL.md` (and the `references/` files you want available) through the skills interface, or package the folder as a `.skill` bundle.

**Manual** — paste the contents of `SKILL.md` into a system prompt or project instructions, and paste individual reference files when you want a specific register.

## Usage

Once installed, ask normally:

> Analyze Turkey's position between the Black Sea and the Levant.

> What does the Kaplan frame say about state-building sequencing in the Sahel?

> Read China's Indian Ocean strategy from the map rather than the rhetoric.

To pin a specific register, name it:

> Use the 1993 field voice — describe the Vardar valley as a seam between worlds.

## How it was built

Distilled by a `persona-distiller` pipeline (full-rigor mode) from seven single-authored books, roughly 562,000 words: *Balkan Ghosts* (1993), *The Coming Anarchy* (2000), *Warrior Politics* (2001), *The Revenge of Geography* (2012), *The Return of Marco Polo's World* (2018), *Adriatic* (2022), and *The Tragic Mind* (2023).

Each core element is scored on projectibility, cost-bearing refusals, expressive match, interactional moves, and preoccupation, then gated. The full ledger — composites, elevation notes, projection and style-match results, temporal gaps — is in [`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md). The corpus contains **no** interviews, debates, or decision records, so the interactional moves are reconstructed from monologic prose and are the softest dimension.

## Disclaimer

- **Not affiliated with Robert D. Kaplan.** No endorsement is claimed or implied.
- **No forged attribution.** Output is a stylistic and analytic reconstruction, not quotation. Do not present anything the skill generates as Kaplan's actual words, and do not use it to fabricate quotes, interviews, or positions.
- **Contested convictions are stated as convictions** — order before freedom, a pagan ethos, partial determinism, the support-then-repudiation of the Iraq War — because fidelity requires it. They are attested positions in the source corpus, not endorsements by this repository's author or by Anthropic.
- **No verbatim source text.** The reference files paraphrase and characterize; they do not reproduce substantial passages from the underlying books, which remain under their publishers' copyright.

## Contributing

Issues and pull requests welcome. Useful contributions: corrections where a cluster mischaracterizes a book, better-calibrated confidence boundaries, additional registers for underrepresented periods. Please keep the honesty in `fidelity-ledger/provenance.md` rather than in `SKILL.md` — the core file stays in-voice.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

