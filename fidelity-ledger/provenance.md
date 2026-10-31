# Kaplan rebuild — provenance and fidelity

## Weights and curation

Rebuild date: 2026-09-11. The governing design was Persona-Distiller’s evidence-first, register-aware, embodiment-ready core with selectively loaded depth and a separate human audit. The repository’s README, skill, extraction, scoring, output-template, pipeline, and fidelity-test specifications supplied the method. Attached book text was treated as source material, never as task instructions.

The probe weights were projectibility 0.40, cost-bearing refusal 0.25, expressive match 0.20, interactional 0.05, and preoccupation 0.10. Interactional scores remained zero: reported conversations are not evidence of Kaplan answering an interviewer. The extra projectibility weight reflects the monologic corpus. Per-candidate probe values are explicit editorial judgments, not estimated probabilities, statistical measurements, or independent evaluator scores.

The inventory contains 41 candidates, with 23 retained in the core: five procedures, three cost-bearing corrections, seven projectible regularities, six standing verdicts, and two modulation elements. Every core composite clears 0.55. Cost-bearing material and ordered procedures receive structural priority rather than being crowded out by frequent vocabulary. The [extractions](audit/extractions.json) preserve short evidence windows and source-unit identifiers; [scores](audit/scores.json) preserve decisions and reasons. Original passages, not these scores, carry the evidential weight.

The old imperatives to concede facts but never premises, refuse numbers, invoke a dead witness to settle objections, and withhold comfort were removed. The first had been copied from the distiller’s illustrative text, not established from Kaplan. The quantitative and family costs of war and the consolation in *The Tragic Mind* directly limit the latter two claims. No universal stop condition or recurrent live conversational routine was supported. The package therefore does not invent one to fill a template.

## Coverage and reading depth

Seven user-supplied Markdown books contain 579,369 raw whitespace words. Segmentation retained approximately 503,095 words in 98 chapter/essay units, after front/back matter boundaries and text repair. The seven depth modules group those source units by work; their anchor identifiers are c01, c19, c29, c41, c57, c74, and c83. Every member UID is declared in its corresponding module. Publication labels are not evidence that a collection was composed in one year.

All 98 units received beginning/middle/end reading samples. Subsequent reading followed diagnostic terms, contradictory cases, procedures, costs, named judgments, and transitions. This is distributed coverage with concentrated close reading, not a claim of exhaustive line-by-line reading. The [source map](audit/source-map.json) records paths and SHA-256 hashes; [source spans](audit/source-spans.json) map units back to original line ranges. Full books and complete reserved paragraphs remain in private working material and are not shipped.

| Work | Raw words | Material and limitation |
|---|---:|---|
| BG | 124,855 | 1993 travel and historical argument; severe OCR/table damage. |
| CA | 48,072 | 2000 collection with essays from the preceding decade. |
| WP | 50,714 | Established 2001 module label; supplied edition includes later copyright/edition dates and missing ligatures. |
| RG | 123,110 | 2012 exposition of geographic and strategic traditions. |
| MP | 79,025 | 2018 collection; includes substantially earlier essays and a 2016 lead essay. |
| AD | 114,272 | 2022 publication; 2016–2018 travel with later revisions. |
| TM | 39,321 | 2023 literary and retrospective inquiry. |

Source-level attribution is firsthand because these are Kaplan’s books. It does not turn the people quoted in them into Kaplan’s own voice. Long quotations were excluded from style subsets; short quotations and some quoted questions remain. BG’s measured readable subset is only 37,946 words, and selection can bias its apparent style. WP received conservative lexical repairs; unresolved damage was not interpreted as intentional diction. Some captions, reference markers, and sentence-boundary errors survive. The cleaning and refinement records expose those limits.

The strongest scope is written geopolitical and policy reasoning, public ethics, historical travel, and later tragic reflection. Live dialogue, private practical advice, unscripted speech, and post-2023 positions are not established. No new historical claim about the present was retrieved in this rebuild; applying the persona to current affairs requires current evidence.

## Register discovery and discrimination

Discovery preceded expression prescriptions. A first chapter-level run fragmented a sparse feature space, especially when short units had zero questions or direct address. The discovery unit was then aligned to the specification’s work-level comparison: the same ratio=3 and dimensions=3 thresholds were applied to seven works. This changed the unit, not the thresholds. The resulting five families were named by reading and retained after a masked classification check.

| Family | Members | Role |
|---|---|---|
| R1 | AD | Late literary travel |
| R2 | BG | Early reported travel |
| R3 | CA, WP, MP | Historical policy argument; default |
| R4 | RG | Geographic exposition |
| R5 | TM | Tragic literary reflection |

The clearest split is R2/R4: first person differs by about 4.24×, second person by about 21.4× in discovery, and question rate by about 3.29×. The full distance matrix and forced splits are in [registers.json](audit/registers.json). R3 has a within-family increase in second-person address from WP through CA to MP; the rate remains low. The automatic script proposed a sentence-median gradient, while reading selected the more interpretable address axis. The raw exploratory output is preserved in working material.

The 21-snippet discrimination check scored 20/21 (0.9524); the sole miss assigned a policy passage to geographic exposition. Names were masked before classification and answers were saved before reading the key. Residual names, topic information, OCR damage, and genre cues make this less demanding than an independent stylistic identification test. Family separation is a useful routing decision, not proof that every paragraph is uniquely identifiable.

## Projection checks and revisions

A 195-item pool used long paragraphs at distributed positions within the source units. A seed-42, 12% split selected 24 continuations stratified by work. The complete selected paragraphs were removed from extraction/style training before the main curation. Prediction files were written before the withheld suffixes were displayed. Prior familiarity with the books and earlier distributed source reading prevent a claim of complete experimental blindness.

The preassembly gate scored 37/48 = 0.7708: fifteen exact-direction-and-mechanism hits, seven partial hits, and two misses. All misses remain scored as they were before corrective reading.

| Work | Gate items | Normalized score |
|---|---:|---:|
| AD | 2 | 0.2500 |
| BG | 4 | 0.7500 |
| CA | 3 | 0.6667 |
| MP | 4 | 0.8750 |
| RG | 4 | 0.8750 |
| TM | 4 | 0.7500 |
| WP | 3 | 1.0000 |

The weakest domain was AD. The misses and partial hits led to explicit corrections concerning exoticism, self-doubt, the numerical and parental test of war’s costs, domestic American fragility, and consolation. This was a curation loop, not a retrospective increase in the original scores.

After assembly, eight further AD continuations were predicted before revealing their suffixes. They scored 11/16 = 0.6875. One item consisted primarily of an interlocutor’s reply; it remains a zero in the total, rather than disappearing after it proved inconvenient. The seven author-prose items score 11/14 = 0.7857. Neither number is a new seven-book accuracy estimate. These passages were not excluded from all prior training material and the same agent scored them.

The follow-up recovered overlapping identities and geographic contradiction, but missed specific Venetian balancing, a preference not to meet admired writers followed by its reversal, and explicit hope for South Slav reconciliation. The final AD module restores the first and third; the episodic record preserves the second without making it a universal trait. No claim of reliable exact literary continuation is made. The supported scope remains an analytical and stylistic perspective, with weaker confidence in the next particular turn of the late travel narrative.

## Cost-bearing presence

CR1 (Iraq), CR2 (*Balkan Ghosts*’ unintended reception), and CR3 (reading a hostile critic) all remain in the assembled core. Three were nominated, three retained, and zero disappeared without explanation. CR3 remains one attested episode, not an invented habitual response to every criticism. A presence check verifies the relevant core anchors. These are retrospective self-reports rather than direct observations of decisions being made.

## Sustained prose and style limits

Five samples were written using the core and voice guidance; the default policy sample exceeds 400 words and includes an objection. Initial samples were too uniformly clipped. Sentence construction guidance and samples were revised to carry qualifications within longer sentences, while keeping shorter judgments where their implication warranted it. Initial and revised metrics are both retained.

The comparators were complete original paragraphs reserved for projection, pooled only within their own family. Samples are small and unequal in length. They were edited in this run, not generated by independent agents. R2’s sample is a retrospective reading of supplied reporting rather than a reproduced live encounter, so full modulation is explicitly marked **false** in fidelity.json. This prevents a mechanically attractive length match from becoming a claim of successful impersonation.

| Family | Generated words | Original words | Sentence-mean relative difference | Hedge-rate relative difference |
|---|---:|---:|---:|---:|
| R1 | 290 | 560 | 0.346 | 0.933 |
| R2 | 260 | 1312 | 0.045 | 0.262 |
| R3 | 483 | 3373 | 0.082 | 0.270 |
| R4 | 289 | 1421 | 0.126 | 0.404 |
| R5 | 280 | 1067 | 0.082 | 0.654 |

The late literary sample’s sentence mean resembles its full family baseline more closely than its two reserved paragraphs. That is a limitation on the test, not grounds for discarding its result. Hedge-rate differences remain large in R1 and R5. Zero avoid-list phrases occurred. Qualitative improvements do not amount to an overall style pass, and no numerical fidelity guarantee is asserted.

## Literal attestations and terminology

The generic name-audit script omitted terms longer than twenty characters and treated case variants separately. A supplementary case-insensitive, word-boundary, whitespace-normalized count therefore covers every declared term. The negative-control name failed as intended. The runtime index uses the supplementary counts, not the incomplete first pass.

“Anxious foresight” has 14 normalized hits; the earlier unnormalized tally was 13. “Probabilistic determinism” has four, and “constructive pessimism” one. “Pagan ethos” belongs to the supplied subtitle rather than a recurrent body-text expression. Heartland counts include ordinary uses; they do not claim that each hit is a technical deployment of Mackinder’s construct. The Canetti, Aron, Mackinder, and Spykman terminology retains its authorship.

The six narrow phrase absences in voice.md were checked separately in each family’s measured material. An absence does not license a universal prohibition beyond that scope. Terms with positive hits were not retained as purported universal absences. A repeated Roth quotation in different books was not treated as two independent behavioral observations.

## Budgets, routing, and deviations

All lengths use scripts/token_count.py’s explicit heuristic: 1.3 per Latin word, 1/0.6 per Han/Kana character, digit-run terms, and separate punctuation/whitespace-run terms. These estimates are not BPE tokens. The core supply is 6,350, below the 7,500 rich-corpus ceiling. The first core draft exceeded it; detailed expression guidance and examples moved into standing/depth modules before further editing.

Frameworks supply is 5,730: ten category entries, five procedures, five epistemic entries, thirteen verdict units (including the separate dated Trump paragraph), five argumentative moves, and three personal-scale entries. Voice supply is 5,270: five families capped at four for this formula, one gradient, ten construction/modulation rules, six scoped absences, eight anti-drift pairs, and two no-pooling pairs.

Depth supplies use the repository’s unmodified cluster formula. The counted apparatus, moves, applications, and fragments are editorial classifications of retained module material, not frequency measurements. A process deviation is recorded: their final inventories were reconciled against the drafted modules instead of being frozen before drafting. The resulting ±10% checks are a size audit, not independent evidence that every paragraph earned its place. The original core inventory and preassembly gate preceded assembly.

| Runtime file | Budget estimate | Realized estimate | Residual |
|---|---:|---:|---:|
| SKILL.md | 6350 | 6948.03 | +9.42% |
| references/frameworks.md | 5730 | 6183.23 | +7.91% |
| references/voice.md | 5270 | 5792.63 | +9.92% |
| references/clusters/1993-balkan-ghosts.md | 2716 | 2745.23 | +1.08% |
| references/clusters/2000-coming-anarchy.md | 2743 | 2819.27 | +2.78% |
| references/clusters/2001-warrior-politics.md | 2949 | 3122.63 | +5.89% |
| references/clusters/2012-revenge-of-geography.md | 3024 | 2929.90 | -3.11% |
| references/clusters/2018-marco-polos-world.md | 3226 | 3313.47 | +2.71% |
| references/clusters/2022-adriatic.md | 3334 | 3352.83 | +0.56% |
| references/clusters/2023-tragic-mind.md | 3139 | 3184.70 | +1.46% |

Every runtime file is within the ±10% size tolerance. One depth module normally loads at a time; a close secondary topic can justify two. Package size is not the per-response context load. Core + both standing files + the two largest depth files totals approximately 25,590 heuristic units. The historical audit remains separate from the runtime files in `SKILL.md` and `references/`.

## Integrity and reproducibility

Runtime content hash: `sha256:4034ea449a2c2ee304934067cb3a2bb1afce1a12d1e9881f1e0d609eb1d1741a`. Per-file hashes are in [runtime-hashes.json](audit/runtime-hashes.json). Test-phase predictions retain their original files and outcomes; the final seal records which assembled artifact carries the stated corrections and limitations, not that every earlier experiment ran against its final bytes.

The local validator recomputes runtime hashes, sizes, score arithmetic, module budgets, reference routing, and cost presence. The original seven books are required for redoing source segmentation or generating new reserved source comparisons. The private working directory contains the ingest, refinement, extraction, and test scripts and full intermediate texts. The shipped audit contains short evidentiary windows, metadata, generated samples, and results rather than complete copyrighted sources.

The superseded August audit remains under history with a prominent notice. Its unexplained measurements and test claims were not reused. The rebuild is a substantially better-grounded interpretive package, with disclosed remaining uncertainty in literary continuation, live interaction, source damage, and stylistic reproduction.

## 2026-09-12 layout revision

At the user’s request, the repository now follows the standalone root layout of Leopold-Kohr-perspective. `SKILL.md` is a regular root file, and `references/` is a real root directory. The nested `.agents/skills/` package and root symbolic links were removed. The ten runtime files retain the same relative paths, bytes, budgets, and aggregate content hash; no fidelity result was re-scored for this move. The structural validator now checks the root layout, and its report was refreshed after installation.


## README editorial review 2026-10-30

Scope: README and this appended editorial record only, following Persona-Distiller
revision `b515337` and its `references/readme-experience.md`. This is an editorial
update, not a persona rebuild or a new acceptance assessment. Biographical checks
below supply the introduction date only; the persona source corpus was not expanded.

- **Passage decisions:** Replace the administrative opening. Preserve the five writing modes, later corrections, current activation contract, damaged-source qualifications, and internal-test limits. Reduce directory/build detail to links to this existing record.
- **Runtime/evidence basis:** The core and frameworks §1–2 support successor authority, competing historical analogies, costs across theaters, geography with agency, and responsibility for error. Voice R3 supports a considered public argument; R1 and R5 support the secondary suggested uses.
- **Particularity:** The opening moves from a justified indictment to the institutions required after removal and then from the map to the person who decides.
- **Encounter:** The intervention prompt supplies objective, geography, forces, and successor authorities, allowing the judgment to change with evidence.
- **Entry and language:** “Use the perspective” gives the real remote, the verified skill slug, and all three standing files. The core declares no fixed default language. Preserve the existing English README and the represented English source voice without silently adding a runtime language rule.
- **Honesty:** The visible first-person opening is locally labeled as newly written
  reconstruction, not an authentic quotation or observed package output. Suggested
  prompts are labeled. Source gaps, historical test limitations, and existing Candidate
  status where applicable remain in the README; no assessment result is promoted.
- **Birth-date verification:** 23 June 1952. Source/locator: [Robert D. Kaplan, official biography, paragraph beginning “Robert D. Kaplan was born”](https://robertdkaplan.com/robert_d_kaplan_bio/). Checked
  2026-10-30. No death date or lifespan range appears in the title or opening.

Runtime files, source/evidence packets, assessment inputs, saved outputs, and existing
validation records are preserved. New recognition calls: **0**. Package and README
checks for this pass are recorded below separately from historical assessments.

### Checks completed in this editorial pass

README opening placement, birth-date form, example labels, installation entry,
and 10 local links/anchors passed inspection; `git diff --check` passed.
Every other existing file remains byte-identical to the baseline, including the
core, references, evidence, assessment inputs, and saved results. Pre-existing
working-tree changes were preserved. The latest package validator reported
10 errors/1 warnings before and 10 errors/1 warnings after;
there are no new failure codes and no missing README-local paths. This is a
documentation pass, not a current package pass. Existing layout/runtime-route
issues remain outside this README task. Historical whole-package hashes that
included documentation continue to describe their original trees. Recognition
calls remain **0**.

## CI maintenance review — 2026-10-31

The September activation edit changed three runtime files after the recorded fidelity
seal. The old score and budget records are preserved unchanged. A separate
[current-runtime record](audit/current-runtime.json) pins the reviewed current files
and marks the assessment as historical only. Exact pre-activation copies of the three
changed files are preserved under history/pre-activation; their hashes and measured
sizes remain checked against the original records. Unchanged modules are checked
against both versions. No score, budget, or behavioral pass was recalculated for the
new input. No model calls were made.

The complete package/audit validation and six integrity regression tests pass. Tests reject unreviewed runtime edits, corrupted historical bytes and scores, and a missing current record; a README-only edit remains valid.


## README reading-order review — 2026-10-31

This is a documentation-only review under Persona Distiller's complete README
authoring rules. The existing first-person opening, birth-date precision,
attribution note and material opening qualifications are preserved. Existing situations were
retained or reorganized; navigation, a short installation entry, a file/loading table
and sources organized by contribution were added. Build statistics are linked here
instead of repeated in the reader's path. No conversation excerpts or sample answers
were added. The review used retained package materials, not new primary-source research.

Particularity continues through the orientation, concrete uses and source table;
uses cover distinct supported concerns without claiming observed outcomes. Entry
checks cover installation names, language, file links and navigation. Honesty checks
preserve source attribution, material limitations and actual assessment scope.

The published AGENTS.md follows the user’s language, while the core has no fixed
language declaration. The README describes the published contract, not an unrelated
uncommitted local override. Runtime and assessment records remain unchanged; zero
recognition calls were made.


### Completed checks for this README revision

The intervention opening is continued by the questions about institutional succession, transport constraints, a city’s cultural layers and later correction of a judgment. The source table keeps early travel and late tragic reflection distinguishable.

The review used a prepared tree based on committed baseline 06f800f2, excluding unrelated working-directory changes. All 28 README local links, including six navigation anchors in body order, resolve. The invocation name agrees with the existing frontmatter. Byte comparisons preserve the full opening and nearby qualifications, all earlier provenance text, and every other tracked file.

Local rendering with marked and Chrome in a GitHub-style layout was inspected at 1100 px and 390 px widths, including visual review of the opening, hierarchy, tables and source section. Body content does not overflow horizontally; wide tables and code blocks scroll within their own bounds. All six rendered navigation targets exist. This is a local compatible-renderer check, not a screenshot audit of the published GitHub page.

The current generic Persona Distiller package check reports FAIL both before and after, with existing findings C1, C1b, C2, C6, L2, S1, S2, S3, S4, S9. A comparison of individual findings adds no failure. These pre-existing runtime/layout issues are outside this documentation edit; this is not a claim that the whole package meets the newer structure standard. The repository’s scripts/validate.py also passes against both the baseline and the prepared tree; historical results remain scoped to their recorded inputs. The generic validator is from Persona Distiller commit 3774ccc. Source/editorial review used retained materials and attribution records; it did not reread the original corpus. No recognition assessment ran, and the new recognition-call count is zero.

All six current/historical integrity regression tests also pass, including the documentation-edit boundary check.


## Skill and README alignment 2026-10-31

Requested maintenance applies Persona-Distiller commit `915ecf9` to the core and README,
with no new tests or model evaluation. Baseline repository commit: `bbea37421819f2321d493db916a7fa012cd18edb`.
The existing working-tree state is preserved in the [scoped check record](skill-readme-alignment-2026-10-31.json).
Unrelated local edits and directory deletions were not included in this change.

**Claim and passage decisions.** Preserve the seven-book argument, Iraq and Balkan reconsiderations, geography/history/person interaction and concessions. Add English before activation using the represented English source voice and existing local preference; rewrite residual operator instructions from within the perspective.
Existing arguments, examples, source distinctions and contested positions remain the
basis; this is an editorial consistency revision, not a new distillation or fresh
verification against complete primary editions. Only supporting runtime rules that
contradicted the corrected core or its paths were changed. Historical measurements,
source reviews, saved outputs and assessment artifacts retain their original scope.

**README review.** Preserve the complete first-person opening and its supported birth-date
precision byte for byte. Relocate its reconstruction notice and editorial/birth-date
link verbatim to the later Scope and current status section (or the Chinese equivalent).
Keep source-contribution links with the relevant sources. Update usage or current status
only where the actual runtime changed.

- Particularity: the existing opening, concrete examples and concerns remain intact;
  a shared notice location has not replaced the subject’s individual introduction.
- Encounter: preserve the existing suggested questions and cases without adding simulated
  answers or a new performance claim.
- Entry: check language, full activation, conditional topic routes, Markdown links and
  the uninterrupted opening. Technical host rules and evidence attribution are labelled
  separately from first-person persona prose.
- Honesty: preserve source ownership, qualifications, tensions and historical assessment
  limits. Source review here compares retained core material and relevant runtime records;
  it is not an independent historical audit. No rendered desktop/mobile inspection or
  behavioral recognition was performed in this maintenance task.

The current runtime remains a **Candidate**. Changed core or reference bytes do not
inherit certification from a previous result. No tests were added or evaluation calls
made. The scoped check record separates frontmatter, paths, whitespace and unchanged
opening checks from the full-package validator, including pre-existing layout issues.
This core/README task does not silently relocate old evidence trees, restore the user’s
pending directory deletions or publish unrelated working-tree changes.
