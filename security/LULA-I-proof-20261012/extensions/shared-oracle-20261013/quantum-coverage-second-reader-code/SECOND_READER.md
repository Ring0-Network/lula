# Source/game and adaptive-reprogramming second reading

Outcome: **ACCEPTED_MANUAL_SOURCE_AND_AR_STAGES; SUCCESSOR_WORDING_FIXES_REQUIRED; FULL_QROM_OPEN**.

Independent `INDEPENDENT-DERIVATION.md` was saved before root/peer multi-call reads. I reviewed the immutable root cut `QUANTUM-COVERAGE-DRAFT.md`, SHA256 **990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce**, directly against the source and the primary AR paper. I independently validated the clean one-row circuit on complex entangled states. No blocking source/AR mathematical defect was found in stages1–3 under the declared finite classical atomic HJ game. Search stages4–5 retain the separate search-reader gate and the wording corrections identified below; I do not promote a complete quantum total from this report.

## Exact subjects

* Release source: `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
* GHHM primary PDF: `9a5ea6adeba5dcdf6c80035057aaccdc704aa6ea2940af0320bcfd7eca0abc8d`.
* Root cut: `990aeb1067f9ac12235ef3982bc9d3d132cffeab5e704a7d0865a69d77e0c0ce`.

I extracted printed pages6–8 from that PDF myself with `pdftotext`; `PRIMARY-AR-PAGES.txt` records the read. Figure2 and Theorem1 Eq(2), not a guessed first-call extrapolation, are the primary anchors. The peer first-call document/circuit was read only after the independent source derivation.

## Stage-by-stage decision

| Item | Verdict | Reason / scope |
|---|---|---|
| Global nonce-inner sampler | ACCEPTED MANUAL | For each message m, I(R_m,m) is a distinct raw point even with repeated R values. Independent full256 U_m programming plus independent residual points gives the ordinary inner restriction conditional on J and the outside graph/root. Root is built in addressed domains and does not inspect inner outputs. |
| Nonzero-S language separation | VERIFIED SOURCE | Source164–187 and601–617 gives I=R16\|S16\|root16\|m and E=U32\|counter4\|S16. Addressed inputs have zero bytes16–31. E with U_lower!=S is outside all inner inputs; every E is52bytes. |
| Guard before outer access | REQUIRED / correctly placed | If U_lower=S, E may be an unknown nonce I point. Guarding only after an outer reply would break untouched-nonce independence. The root stops before the lookup. The stop preserves the original first-guard event and C-with-no-guard; it is not an implementation abort API. |
| Dynamic nonce overlay | ACCEPTED MANUAL | Before completion, the public ghost does not read that label's R or U. Both private classical services use U_m. A completed response reconciles R_m and U_m; repeats reuse them, including across snapshots. Earlier quantum memory is retained. Known is never rolled back. |
| Partial/completed/initiation convention | ACCEPTED MODEL | q counts initiated calls. No partial secret/R buffer is exposed. Absorbing noncompletion cannot produce a fresh final output. Do not replace q by a completed count while allowing unbounded retries. |
| Common packed-query comparison | ACCEPTED MANUAL | Remaining R values are unused in the continued guarded ghost, including after measured source calls. A raw word names one nonce coordinate and guessed R. Packed common service isometries give vector gap2Q/sqrt(N). Guard failure depends on U, not on another hidden R; it is checked before aliasing. |
| Guard probability | ACCEPTED MANUAL | New-label U is unused uniform256 before the request; repeats add no draw. Ghost guard probability <=q/N. A common stopped guard predicate then gives `(2Q+sqrt(q))^2/N` in ordinary HJ. This is an unconditional first-error argument, not conditioning the successful transcript. |
| Lazy-U equivalence | ACCEPTED MANUAL | In the masked ghost, unused per-label U entries have no public effect. A new classical label can take the next fresh U; old labels retain their assignments. Sampling a bad-half coin then conditional good U is the exact per-call law, with an explicit bad branch. |
| Entire-row AR | ACCEPTED PRIMARY INSTANTIATION | Input set G_S has M_good=N^2−N elements; output is a full tuple of2^32 independent256-bit words. Each new-label instruction supplies the uniform distribution on G_S, so max point probability is1/M_good. Source adaptive labels do not choose a preknown U point. |
| AR source callback reads | REQUIRED and counted | Figure2 returns input/side information, not the new row. One POST-instruction ROW query obtains the row. Earlier such reads appear in Qhat of later instructions. Client calls cost one row query each. The safe Q+q+1 bound retains both types and a conservative final endpoint read. |
| Namespace collision semantics | ACCEPTED with explicit cache wording below | A new-label U collision is still a new reprogramming instruction. AR pays the overwrite of that namespace; it must not be pretended absent. Each fresh programmed row has its own independent latent X_i. Repeats and collisions select from at mostq templates, so padded coverage dominates. |
| Full-output/failure law | ACCEPTED MANUAL | Program the complete counter row, not an accepted-conditioned digest. First acceptance selects on the independent omitted9-bit coordinate. Full256 suffixes are included. All-C failure remains absorbing noncompletion, and a latent X can still pad that unused template. No successful-completion normalization is inserted. |

## Primary AR constants and interface check

The inspected GHHM Theorem1 applies to finite input/output sets and adaptively supplied sampling distributions. Its Eq(2) is an event-probability distance bounded by

    sum_r [sqrt(Qhat_r*p_r) + (Qhat_r*p_r)/2],

with Qhat_r counting function queries before that instruction and p_r the expected maximum input probability. Root correctly uses p_r=1/M_good and at mostq instructions. Raw client queries plus up toq POST row reads plus one final selected-counter endpoint give total at mostQ+q+1, hence the displayed conservative

    Delta_row <= min(1,
      q*[sqrt((Q+q+1)/M_good)+(Q+q+1)/(2*M_good)]).

The first callback's POST read is after its own instruction but before later ones; it is not free. No2^32 counter multiplier arises. Variable instruction count <=q can be padded by unused post-output instructions without affecting the recorded event. The theorem is information-theoretic for finite registers; the2^40-qubit row response workspace makes no efficient/PPT claim possible.

## Direct one-query circuit verification

The preliminary independent derivation noted that the conventional **zero-ancilla** row-read/select/uncompute simulation costs two row queries. The peer/root circuit uses a different valid construction:

1. Every row output slot starts in the uniform plus state.
2. Coherently swap the real response register into the chosen counter slot, only on an eligible branch.
3. Apply one whole-row XOR query.
4. Swap back. Every other translated plus slot is unchanged; the selected slot receives the required word XOR; every ancillary slot returns to its original plus state.

This equality holds as a unitary identity on arbitrary entangled namespaces, counters, responses and work registers. An ineligible branch can route to a valid dummy U without any swap, so row XOR acts as identity there; its independent outside-table response can be compiled locally in this conceptual simulator.

Own `source_row_control.py` checks **256 complete two-row functions** on an arbitrary normalized complex state entangled across namespace, counter, response, eligibility and another ancilla. Every final amplitude equals the scalar raw-hash action tensored with exactly clean plus work. This independently confirms **one** row query per raw call. The enormous known nuisance/outside tables are independent of ROW initially; adaptive known-nonce overlays are generated by the controller and do not expose unknown future sampler U values before AR.

## Concrete controls and corrected details

The same script enumerates **16,384** message-labelled inner-programming worlds. For every fixed nonce assignment, all complete two-bit inner tables have equal probability, including repeated nonces.

A literal source-encoding counterexample confirms the need for the half guard: take `root=BE32(0)||S[:12]`, `m_other=S[12:]`, and `U=R_other||S`. Then

    E(U,0)=R_other||S||root||m_other=I(R_other,m_other)

as exactly52bytes. This is a syntactic model discriminator, not a real-source forgery.

A collision/repeat control uses two new messages with the same U but different fresh row templates. After reprogramming, an old label's actual current row has accepted X=3, while its obsolete per-label template has X=0. This confirms the controller must state which cache it uses and that a new collision's fresh row is read and stored. The checked preceding-source-read counts are0 then1 for the first two instructions.

## Exact successor wording corrections

1. **Stage3, cached-read sentence.** Replace the ambiguous claim that “known-row collisions” can be served without further reads with: “Each new-message reprogramming instruction, including a sampled collision with an old namespace, is followed by one whole-row read that updates the namespace-keyed cache. Later repeats use the latest cached row for their unchanged U and need no additional read.” This matches both the POST ledger and the later latest-row statement. It does not alter the conservative bound.
2. **Stage4, selected BASE response.** State that the **BASE function is independently sampled**, not that an adaptively selected final response is conditionally uniform. Earlier quantum queries can correlate the selected response with the state; the explicit marked-search reduction handles that correlation. The same correction applies to inner-target language. Root's independent-advice and challenge factorization are the correct mechanism.
3. **Keep advice cuts distinct.** Future U/template advice is an event-only enlargement after the AR hop. It cannot be supplied before the original reprogramming sampler and then still claim fresh-U entropy. Entire BASE inner-table advice is forbidden in the inner search, even if used as independent nuisance in the separate outer search. Adaptive assignment labels must remain controller-generated, never conditioned logs.

I find no new mathematical obstruction to the source/AR stages after these clarifications. The separate search reviewer should decide the exact marked-oracle constants and common-game final reduction. This report does not bypass that gate or promote full signature QUANTUM total from the immutable cut.

No source, manuscript, root/peer file, or frozen proof packet was edited. All outputs and controls remain in this second-reader directory.
