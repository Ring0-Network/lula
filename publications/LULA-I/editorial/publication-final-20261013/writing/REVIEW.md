# Writing Review Report

## Overall assessment

The article presents a coherent mechanism paper: construction, honest-cache transparency, a conditional rollback simulation, explicit costs and selected performance observations. The manuscript no longer reads as an operational research ledger. No critical or major writing defect was identified; three local, nonblocking clarity improvements were recommended on the frozen baseline. Root applied all three during this review, and their exact current successor has been rechecked. A wholesale rewrite is not justified.

**Scope:** Complete LULA-I.tex and its recursive operating-model, stability-results and comparison-results includes, including all statements, algorithms, proofs, tables, diagrams/captions, appendix and final Note. Bibliography entries and ACADEMIC_STRUCTURE.md were read. This is a prose/claim-scope review, not independent validation of the formal mathematics, experiment data, external bibliography destinations or publication acceptance. No manuscript or PDF was edited or rebuilt by this reviewer.

**Baseline:** LULA-I.tex SHA256a33849e5eccf0d1895a3a035bd6a45de312bf783db200d986d0e5cd55699c6c1. All locators below refer to that frozen source and the include hashes in READ-SCOPE.json.

## Frozen-baseline scores

| Dimension | Score | Summary |
|---|---:|---|
| Cohesion |4/5|Referents and cross-references are clear; one introductory resource-state sentence can be more precise.|
| Coherence |5/5|The stated mechanism question is answered through construction, transparency, transfer, costs and limits.|
| Cadence |4/5|Technical qualifications are readable; some dense cost/recovery prose is necessary and remains justified.|
| Lexical quality |4/5|Terminology is stable; one awkward compound and one cross-metric comparison merit local edits.|
| Argumentation |5/5|Writing consistently distinguishes conditional proof, component models and measured observations; this score does not certify their mathematical truth.|
| Academic register |4/5|The technical body is professional; the explicitly requested personal Note is a deliberate exception and is retained.|
| Section compliance |5/5|Concise abstract, numbered contributions, motivated construction, results context, limitations and appendix have distinct functions.|
| Grammar and errors |5/5|No consequential mechanical grammar error was identified; source references and citation keys resolve in the reviewed include closure.|
| **Overall** |**4/5**|Minor local revision only; no structural rewrite is needed.|

Scores are editorial judgments within this scope, not detector results, scientific certificates or predictions of venue acceptance.

## Critical issues

No critical issues found within the prose-review scope.

## Major issues

No major issues found within the prose-review scope.

## Minor issues

### W01 — Make the restored local view explicit

- **Dimension:** Cohesion and lexical precision.
- **Severity:** MINOR; nonblocking.
- **Location:** LULA-I.tex:51, Introduction.
- **Exact quote:** “A resource that appears unused in every restored execution may nevertheless have been exposed in another branch.”
- **Problem:** “Every restored execution” invites an unnecessarily global reading while the surrounding argument concerns the apparent state after restoration. The reader can recover the intended distinction, but must supply that temporal scope.
- **Minimal English rewrite:** “A resource that appears unused after restoration may already have been exposed in another branch.”
- **Conditions to preserve:** The resource only appears unused; earlier exposure is possible, not asserted for every resource; the adversary retains observations across branches. Do not add a public resource-status API or a new consumption mechanism.
- **Counterinterpretation considered:** The original can mean each branch's restored starting view. That reading is legitimate; the rewrite simply makes it direct, without weakening the restoration problem.
- **Alternatives:** Local rewrite recommended; a new explanatory paragraph is unnecessary; retaining the original is acceptable if the editor prefers its emphasis.

### W02 — Replace an awkward temporal compound

- **Dimension:** Lexical quality and register.
- **Severity:** MINOR; optional polish.
- **Location:** LULA-I.tex:55, Introduction.
- **Exact quote:** “The intended use objective is $2^{40}$ signing queries across all branches, conditional on a still-unestablished full reference-signer bound.”
- **Problem:** “Still-unestablished” compresses the qualification into an awkward compound. The full sentence is already scientifically qualified and requires no substantive change.
- **Minimal English rewrite:** “The intended use objective is $2^{40}$ signing queries across all branches, conditional on a full reference-signer bound that has not yet been established.”
- **Conditions to preserve:** The value is a use objective, not a proven limit or certified capacity; queries aggregate across branches; the full reference bound remains unestablished. Do not substitute the FORS-only exponent as that bound.
- **Counterinterpretation considered:** The compound is understandable and may be retained. This suggestion is local register polish, not a defect in the technical claim.
- **Alternatives:** Local rewrite if desired; no structural move or author question is warranted.

### W03 — State the latency/byte distinction directly

- **Dimension:** Lexical precision and claim presentation.
- **Severity:** MINOR; nonblocking.
- **Location:** stability-results.tex:23, Latency consequences of caching.
- **Exact quote:** “Cache availability has a larger effect on first-use latency than on signature size.”
- **Problem:** “Larger effect” compares unlike metrics without stating a normalization. The actual mechanism result is sharper: honest cache availability affects computation, while returned serialized signature size is invariant.
- **Minimal English rewrite:** “Under the honest-cache model, cache availability affects first-use latency but leaves serialized signature size unchanged.”
- **Conditions to preserve:** Honest supported cache states and terminating returned signatures; no claim about arbitrary corruption; no universal recovery distribution or guaranteed runtime. Keep all restart, cache-loss and key-generation values and their individual-observation qualifications unchanged.
- **Counterinterpretation considered:** A qualitative comparison with zero change in signature bytes is intelligible. Stating the invariant directly removes the need to infer that cross-metric comparison.
- **Alternatives:** Local rewrite recommended; restructuring the recovery paragraph or adding a new comparison measure is unnecessary.

## Priority fix list

1. Apply W03 to express the established byte invariant directly, leaving all observations untouched.
2. Apply W01 to clarify the local view after restoration.
3. Optionally apply W02; do not otherwise rewrite the abstract, mathematical exposition or conclusion.

## Material deliberately retained

- **Abstract:** Retain the current94-word abstract. It names LULA as Ring0 Labs' research family; identifies the deterministic cache mechanism; preserves successful-key, honest-cache, termination and conditional-reference qualifications; reports signature/cache sizes and the large cold cost. It neither claims a complete security proof nor generalizes three cold observations into a distribution.
- **Use objective:** Retain the conditional2^40 objective in the Introduction, component subsection and latency captions. The132.6 value is explicitly FORS-only and per candidate.
- **Necessary repeated limits:** The abstract, model, theorem and conclusion serve different reading functions. Their reference-bound/atomic/honest-cache qualifications are not filler. No deletion is recommended merely because a technical term or warning recurs.
- **Results:** Retain the host/back-end/core-isolation limitations, pooled-block/two-key explanation, two failed verification repeatability cells, three individual cache-loss observations and the absence of guaranteed worst-case runtimes. These are scientific interpretation limits, not execution logs.
- **Comparison:** Retain separate compact/SHRINCS observations, their unnormalized assumptions, non-author implementations and explicit statement that no real-SHRINCS forgery was run. Neither table is framed as a normalized security ranking.
- **Note:** Retain exactly the requested “Note:” and its sentence. The user's explicit choice takes precedence over a generic register preference; no new humor is added elsewhere.
- **Article structure:** Retain the current reader order. The supplied Li Crypto2025 example was consulted for title/introduction/contributions, section hierarchy and its compact efficiency treatment, not as a theorem or formatting authority. Its complete mathematics was not independently reviewed here.

## Research-informed safeguards

The live primary text of [Reinhart et al., *Do LLMs write like humans?*](https://arxiv.org/html/2410.16107v2) was consulted for its abstract and opening methods/results. It reports structural differences in the tested parallel corpora; that licenses inspecting noun stacks, referents and genre fit, not diagnosing this paper's authorship. The abstract and selected grammar-editing passages of the [Abdulhai et al. March2026 preprint](https://arxiv.org/html/2603.18161v1) were consulted for reported meaning/stance changes under editing instructions. That motivates checking every proposed rewrite against its original claim; it does not prove that every edit distorts meaning. Neither source is inserted into the scientific manuscript.

No AI-authorship inference, detector-evasion objective, AI-writing score, lexical-density score or punctuation-based defect classification was used. The32-pattern catalog is an editorial procedure, not a validated classifier. Each recommendation above is justified by its specific textual effect and has a preservation condition.

## Validation and handoff

All95 writing-skill reference nodes, its SKILL.md and seven assets were read; all24 phd-paper-review reference nodes and its SKILL.md were read. Exact file paths and hashes appear in COVERAGE.json. All three PhD MOCs, cadence/register, scoring, output and their linked criteria were applied. The paper's full recursive include closure was read; empty replay-results.tex was inspected as an inactive empty file. The bibliography source was read, but URL availability and cited-work factual adequacy are separate reviews.

A source scan checks the94-word abstract, recursive include closure, citation keys and cross-reference targets, plus absence of the retired operational/placeholder vocabulary. This reviewer performs no compile, rendered-page review, benchmark rerun or new proof validation. “Manual model review; no automated model checking performed.”

Root is the sole manuscript editor. This reviewer applied no prose patch. During the pass root applied W01–W03 exactly, named the reconstructed verifier value $P_j$ explicitly and clarified the dependency-diagram box as “FORS, lower trees, and chain signing.” The verifier edit connects an existing computed public-key value to RootFromPath; it introduces no new cryptographic step. The diagram edit includes the top chain signing that remains online. These presentation edits were inspected and the current main/stability hashes are pinned in REVIEW-RECEIPT.json.

An exact replacement allowlist reconstructs the current files from the frozen originals. Numeric-string sequences and all table, lemma, theorem, proof, equation and align environments are identical; the94-word abstract and final Note are identical. Only the explicitly notified algorithm variable binding and diagram wording differ outside the three prose fixes. Other included sources, bibliography and ACADEMIC_STRUCTURE.md are unchanged. Root will compile/package separately; no build result from another reviewer is claimed here. There are no remaining in-scope writing recommendations or open author questions.

**Outcome: COMPLETE_WITHIN_SCOPE — read-only whole-paper prose review and exact root-successor recheck completed; three baseline minor recommendations resolved, no remaining critical, major or minor writing issue identified.** The publication's deliberately conditional security scope remains unchanged.
