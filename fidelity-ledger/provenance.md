# Provenance & fidelity ledger

The honesty lives here, never in `SKILL.md`. Every core element maps to its sources, its scores, and its gate status. Built by the `persona-distiller` pipeline (full-rigor mode) from seven single-authored books, ~562k words.

## Weight vector (adjusted for a monologic, dialogue-free corpus)

projectibility **0.34** · cost_refusal **0.25** · expressive_match **0.20** · interactional **0.11** · preoccupation **0.10**
*Adjustment:* dialogue_ratio 0.0 → interactional 0.15→0.11, projectibility 0.30→0.34 (auto-weight hook, `pipeline.md`).

## Core element ledger

| element | core section | source book(s) | clusters | composite | projection | cost-gate | note |
|---|---|---|---|---|---|---|---|
| C1 Iraq reversal | What I will not concede | Revenge, Tragic Mind, Marco Polo | 3 books | 0.785 | strong | high-signal, in core | anchor cost-move; "those like myself who supported the Iraq War" |
| R3/C2 order before freedom | How I read / will not concede | Coming Anarchy, Revenge, Tragic Mind | 3 books | 0.767 | strong | high-signal, in core | verbatim "order comes before freedom" ×3 |
| C3 pagan ethos | What I will not concede | Warrior Politics, Tragic Mind | 2 books | 0.732 | strong | high-signal, in core | results-over-intentions; public≠private virtue |
| R4 think tragically to avoid tragedy | How I read a question | Tragic Mind, Revenge | 2 books | 0.726 | strong | — | "anxious foresight to guard against hubris" |
| C5 withhold comfort | What I will not concede | Coming Anarchy, Tragic Mind | 2 books | 0.684 | strong | high-signal, in core | "inspire, not depress" — but refuses false comfort |
| C4 defend unfashionable theory | What I will not concede | Revenge, Coming Anarchy | 2 books | 0.652 | strong | high-signal, in core | defends the map "when it was unfashionable" |
| R7 traveler over theorist | How I read / How I move | Balkan Ghosts, Revenge, Marco Polo | 3 books | 0.645 | strong | — | "Huntington is correct"; ground truth |
| R2 partial determinism | How I read a question | Revenge, Adriatic, Marco Polo | 3 books | 0.644 | strong (hard-inference) | — | "many contradictory stories"; the assert-then-un-fatalize move |
| R5 anti-utopianism | How I read a question | Coming Anarchy, Warrior Politics | 2 books | 0.632 | strong | — | contra Fukuyama; "utopian streak… perilous" |
| R1 read the map first | How I read a question | Revenge, Marco Polo, Coming Anarchy, Adriatic | 4 books | 0.622 | strong | — | "forgotten, not conquered" |
| R6 elite/closed order | How I read a question | Adriatic, Warrior Politics | 2 books | 0.566 | strong | — | Venice as "closed elite" |
| I3 summon a witness from the dead | How I move / How I sound | all analytic + moral books | 4 books | 0.560 | — | interactional min-presence ✓ | Mackinder 261, Machiavelli 148, Hobbes 118 |
| M1 ground→map→moral modulation | How I sound | Balkan, Adriatic, Revenge, Marco Polo, Tragic Mind | 5 books | 0.521 (ELEVATED) | — | — | reserved-claim + sparsity protection; highest expressive_match (1.0) |

**Elevation note (M1):** raw composite (0.521) fell below the 0.55 cut, but `scoring.md` rules 2 (variation/modulation reserved claim) and 4 (sparsity protection) require retaining it — it is the single most individuating expression feature and would otherwise be crowded out by volume. Elevated to core and logged, per the rule.

**Demoted to references:** I1, I2 (interactional, reconstructed, 0.51–0.53); E1, P1 (embodied in core voice, detail in references). **Cut:** E2 (embodied not listed), X1 (bare style averages, 0.12 — generic).

## Gate & fidelity results (`fidelity.json`)

- **Projection gate (pre-assembly, seed 42, n=14):** overall **0.893**; **strong-domain 1.0**, **weak-domain 0.25**. PASS (≥0.70). The high overall is entirely home-turf; off home turf the persona degrades sharply — see caveats.
- **Cost gate:** 5/5 high-signal divergences in core (C1, C2=R3, C3, C4, C5). Presence assertion PASS. Interactional (I3) and modulation (M1) present.
- **Projection re-check (Stage 5, assembled core):** consistent with gate; home-turf strong, weak domains flagged.
- **Style-match (Stage 5):** modulation reproduced — generated geopolitical sample hedges ~1.76× the moral sample (14.9 vs 8.5/1k) and runs longer sentences (mean 22.3 vs 14.8), matching the originals' geo-hedged / moral-declarative split. Absolute hedge rates are elevated by short-sample density and are not directly comparable to book-length averages; the relative modulation is the decisive, passing check.

## Confidence caveats (carried into the coverage report, kept out of the core)

- **Strong / trust:** grand strategy; geography & the map; order-vs-freedom sequencing; tragic foresight; the moral philosophy of power; great-power competition; the Balkans/Adriatic borderlands.
- **Weak / distrust:** economics & finance; domestic US policy; granular dated forecasting; anything post-2023. The persona reframes these toward order/geography rather than holding a genuine attested position.
- **Softest dimension:** interactional moves are **reconstructed from monologic prose**, not observed in live exchange. The corpus contains zero interviews, debates, or decision records.
- **Temporal gaps:** 1994–1999, 2002–2011, 2013–2017 (between books) — the persona interpolates and should not be trusted to reproduce his exact stance *at* those dates.
- **Contested convictions** (order before freedom; a pagan ethos; partial determinism; support-then-repudiation of the Iraq War) are stated **as convictions** by fidelity requirement — attested positions, not endorsements. The skill is a thinking-style tool for analysis and ideation, not for forged attribution.
