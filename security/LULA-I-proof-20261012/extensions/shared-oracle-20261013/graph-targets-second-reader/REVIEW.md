# Independent review of the typed honest-graph target term

**Verdict: PASS_SCOPED_GRAPH_TARGET_LEMMA.** The packet's statistical same-address target-hit result is valid under its explicit finite DAG, seed-independence and classical complete-hash RO hypotheses. No blocking counterexample to that scoped result was found. It must remain distinct from an efficient SPR/TCR challenge reduction, type-7 counter security and complete EUF-CMA security.

## Independence and reviewed cut

The actual release Rust source was read in full. `INDEPENDENT_DERIVATION.md` was saved before reading the target lane's derivation or controls. Then `graph-targets/DERIVATION.md`, `control.py` and `CONTROL-RESULTS.json` were read. Their inspected hashes are in `CHECKS.json`. All writes for this review are inside `graph-targets-second-reader`; the separately authorized FORS padding repair is in its existing extension directory and does not change this target lane or the earlier proof packet.

**COMPUTED:** release-source SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210` was independently checked. The reviewed target derivation SHA-256 is `3a61a88cbad28796c62ae94484d984ad3ed73320612f64469ad987c6e809346c`.

## Source graph audit

**PROVED (manual source derivation):** types0..4 have one designated honest payload per legitimate full address. Chain inputs depend on the preceding DIFFERENT position address, endpoint compressions depend on fixed full chains, Merkle payloads depend on lower-height nodes, FORS leaf payloads depend on outside private derivations, and FORS root compression depends on the17 real roots. Tree-global FORS indices and distinct heights prevent cross-tree address aliasing. WOTS endpoints do not depend on the child message they certify or on any canonical counter.

The graph is therefore own-domain-blind and acyclic. Its input rule uses only outside coins and predecessor designated images, not any non-designated response. Same node values at different addresses do not merge their hash domains. Target-search success compares an alternative payload with the honest image of THAT complete address, rather than every image in the forest.

**PROVED / PASS:** excluding type7 is essential. A source canonical counter is chosen by searching its own address restriction, with many `child||counter` payloads. One selected accepted value is not an independent DAG target. The packet correctly avoids importing its lemma there. The source's private types5/6 are outside selected target domains; their placement does not establish secrecy or make the full signer secure.

## Eager marginal and conditional residual audit

**PROVED / PASS:** sampling target full images in topological order, then independently completing every off-target table, has the ordinary-RO marginal. Its target point depends on predecessor restrictions but is independent of its own restriction. Full256-bit designated images must be retained for raw SHA replies even though subsequent nodes use only128-bit prefixes. The packet does this and does not overwrite preanswered oracle points.

**COMPUTED:** the independently arranged `control.py` generates targets and residuals first and compares the resulting completed-function distribution with directly enumerated ordinary functions. All64 finite worlds agree exactly, across8 graph views. Conditional on each graph, the3 residual bits have all8 possibilities with equal weight. Conditioning additionally on the entire OTHER domain's function leaves the target domain's residual uniform1/2. An adaptively chosen second fresh residual response remains1/2 conditional on graph, outside function and first reply; the two-query hit event is3/4.

**Boundary control, not a defect in the reviewed statement:** arbitrary adaptive outside-query TRANSCRIPTS are not independent side information. An adversary can query a residual, then encode its value in another domain's query input; that input reveals the old residual. The packet's hypothesis uses outside randomness/functions and honest graph dependencies, not an arbitrary post-query transcript. Keep that interpretation. Fresh-query probability is evaluated after conditioning on the actual preceding history; previously queried values are known and charged at their first occurrence.

**COMPUTED negative controls:** a cyclic target equation produces a nonuniform completed-function sampler (one ordinary binary function is absent), confirming that acyclicity/blindness is substantive. A two-counter first-accepted target at counter1 forces the earlier counter's result to be rejection, contradicting uniform residual independence for type7. The reviewed lane's separate8-world own-restriction counterexample is also correct: a three-cycle of binary outputs always has an equal adjacent pair, giving certain target collision after adversarial target selection.

## Prequeries, public seed and final verifier

**PROVED / PASS:** sample the ghost graph/function tables consistently at time zero and withhold disclosures until their real times, or reveal the graph earlier solely in the stronger TARGET-SEARCH experiment. Both treatments preserve earlier raw replies; later graph discovery does not justify resampling them. The source seed/coins must be chosen independently of selected-domain restrictions. A seed chosen after inspecting those restrictions is outside the claim.

**PROVED / PASS:** S!=0 is the explicit separation branch. The addressed prefix has zero bytes16..31, whereas unaddressed inner calls have S there; outer calls have length52 and cannot match an addressed header. Types distinguish type7 and private5/6. Charging the entire S=0 branch gives the packet's unconditional `(Q_public+3218)/2^128` bound. It is not a setup-success-normalized result. Shared seed-zero charges in later composition need the same care as other unconditional bad-event bounds.

**PROVED / COMPUTED:** the final verifier's altered-value/path schedule has at most3,217 target-family complete SHA calls and3,224 complete SHA calls overall. A changed sibling can make the next payload depend on the previous verification response, but a new off-target response is still uniform under the correct conditional history. A repeated old hit was already counted at its earlier adversarial query. All final addresses stay within the fixed honest graph's ranges; a path to an unobserved key still has a designated mathematical target. The verifier performs no counter search, so arbitrary counter fields do not increase the call cap.

Independent arithmetic rearrangement:

    targets = 17*10 + 1 + 3000 chain steps + 5 endpoint compressions + 41 path hashes
            = 3217.
    all complete calls = targets + 5 type7 digests + 2 message hashes = 3224.

For32-byte messages, multiblock operations add41 compressions, giving3,265 instrumented compressions and3,266 with prefix initialization. Neither number is the complete-RO query cap. Malformed signatures reject earlier and cannot increase the fixed maximum.

**COMPUTED:** the symbolic selected-domain total is39,339,469,515,522,047, matching the lane. The type2 internal-node count was independently obtained by telescoping across layer forests:2^41−1. The huge domain total is an inventory, not a query-loss multiplier or a promise of efficient construction.

## Security boundary

Giving the complete honest graph exposes chain starts and FORS secrets and can enable signing without an alternative-input collision. The packet explicitly states this. The graph-exposed experiment therefore cannot replace the actual EUF experiment or prove that every forgery causes the bounded target-hit event. Its statement is an information-theoretic ghost-graph event bound with at most one addressed target per fresh query, not a full security theorem or a QROM proof.

**Open obligations retained:** efficient challenge placement/graph simulation, exact full-signature classifier and other knowledge/encoding/inversion routes, type7 digest/first-acceptance analysis, secret/routing hybrids, full composition and quantum security. Full EUF-CMA and quantum fields remain null in this review's executable receipt.

**Executed receipt:** `python -I -B control.py` returned exit0, writing `CHECKS.json`. Only finite tables and source arithmetic were evaluated; no signatures, large graph, cache construction or timing measurements were run. No target-lane file, source or manuscript was edited.
