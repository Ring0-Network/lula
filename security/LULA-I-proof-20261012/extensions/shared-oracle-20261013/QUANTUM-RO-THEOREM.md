# Reviewed finite-QROM advantage theorem for the LULA I source game

**PROVED — manual finite-query source-model theorem, independently reviewed twice.** The immutable composition draft71d3f23a… and corrected coverage theorem24a03141… are preserved. `quantum-composition-numeric/ROOT_REVIEW.md` together with `CONDITIONAL-GATE-CLOSED.md`, and `quantum-composition-second-reader/SECOND_READER.md`, accept the complete common-HJ union, private hop, budgets, single seed and honest-cache transfer. Their source-first derivations precede the root composition read. The theorem is an unconditioned winning-probability upper bound in the declared partial atomic finite-query QROM experiment. No security category, efficient generic primitive reduction or fixed-SHA certificate follows.

## 1. Common experiment

**ASSUMED — explicit finite interface.** Use the pinned source library, independently uniform 128-bit K/P/S, one full256 XOR random oracle on a finite injectively framed register, a quantum query-bounded adversary, classical atomic Sign services, q initiated requests and Q coherent adversarial full-hash queries. A classical final signature is submitted for the exact root verifier. Honest cache handles are opaque, key-independent and consistent. No private bytes, timing, coherent signing, interruption or arbitrary corruption are supplied. Noncompletion is absorbing/nonwinning; neither setup nor campaign success is conditioned on. The adversary's measurements and retained quantum memory may determine its classical requests and forgery.

## 2. Pointwise accepting-verifier partition

**PROVED — deterministic classification — reviewed.** The structural proof in CLASSICAL-RO-THEOREM.md acts on a realized classical transcript, graph and final verifier trace; it does not assume the adversary's internal state or raw query history is classical. Quantum access changes how that transcript is produced, not the accepting verifier's byte-level dataflow.

Trace backward from the fixed top root on the route selected by final H_msg. A changed same-address Merkle path supplies G. A same WOTS leaf with changed endpoint vector or a position-labelled merger also supplies G. A genuine still-hidden predecessor or secret supplies H_final, including the unexposed canonical-key case because the sum is strictly below ell*(w-1). At an exposed key, genuine suffix access yields e>=x componentwise; fixed equal sums force e=x. A changed child or counter with equal digits supplies D7_final; equal pairs allow descent into the next lower fixed subtree. At the FORS root, a changed aggregate, path or leaf image supplies G; a genuine undisclosed secret supplies H_final; otherwise all seventeen final secrets/paths correspond to disclosed indices at that instance and the raw digest is COVER C. The forced eighteenth coordinate is only the zero filter, not an eighteenth secret.

Thus every accepting fresh-message signature lies in C union H_final union G_final union D7_final, even if it was prepared using coherent raw queries. No event meaning 'a quantum query ever hit a secret' is inserted. The partition is in ordinary HJ, never its blinded or reprogrammed comparison continuation.

## 3. Common-marginal probability projections

**PROVED — scoped event composition — reviewed.** Fix any nonzero S and let N=2^128. Private replacement compares the actual shared-RO game with ordinary JOINT-IDEAL HJ. Its normalized trace-distance bound already includes both potential public aliases in the final classical verifier. The event distance therefore obeys

    Pr_REAL[Win | S] <= delta + Pr_HJ[Win | S],
    delta = min(1, 2Q/sqrt(N)+(2q+2)/N).

Each event bound below refers to the SAME ordinary HJ marginal. G/D7 may reveal event-only full-graph advice, while H may reveal only its safe surface and suffix-closed disclosures. C uses separate inner/outer challenge views. These are separate upper-bound reductions; their secrets, BASE tables and adaptive logs are never combined into one enlarged forgery game.

**PROVED — independently reviewed component formulas.** Put M=N^2-N and p_F(q) equal to the independently checked exact-binomial raw-candidate coverage probability. With per-component caps at one,

    D = min(1, q*(sqrt((Q+q+1)/M)+(Q+q+1)/(2M))),
    A = min(1, D+8*(Q+2)^2*(p_F(q)+1/N+q/N^2)),
    c = min(1, (2Q+sqrt(q))^2/N
                 +(2*(Q+2)/sqrt(N)+sqrt(A))^2),
    h = min(1, (2Q+sqrt(3017))^2/N),
    g = min(1, 8*(Q+3218)^2/N),
    d7 = min(1, 8*(Q+6)^2/N).

The c formula is licensed by QUANTUM-COVERAGE-THEOREM.md and its source/AR/search review receipts. Honest row reads are included in its Q+q+1 ledger. Extra final evaluation counts inside c/g/d7 do not become additional original adversarial Q queries; they belong to the respective reductions. The H stopped examiner charges 3017 classical candidates instead of adding coherent slots.

## 4. Uniform public seed and reference theorem

**PROVED — arithmetic implication — reviewed.** All five component inequalities are uniform in fixed nonzero S. Assign winning probability at most one to S=zero[16], average the remaining seeds and drop the harmless factor 1-1/N. The accepted unconditional theorem is

    epsilon_QROM(q,Q) <= min(1, 1/N+delta+c+h+g+d7).

The seed-zero branch is paid exactly once. Do not use the unconditional private-hop expression with 2q+3 and add another 1/N. The theorem bounds the full verifier's winning probability in the declared finite-query experiment; it does not supply an efficient black-box generic primitive reduction, a checked Rust/channel refinement or a fixed-SHA theorem.

## 5. Honest cache transfer and completion

**PROVED — interface implication — reviewed.** Consistent recomputable cache restoration changes no serialized honest signature, random-oracle answer or classical service result. By coupling the same oracle/adversary coins and quantum operations, the actual adversary view remains identical for arbitrary adaptive branch restoration in the opaque honest-cache atomic interface. Therefore epsilon_cached <= epsilon_reference with zero probability and signing-query loss, and the accepted epsilon_QROM transfers unchanged within that interface. Time/space overhead and private cache disclosure are separate obligations. Arbitrary accepted-counter edits are excluded because source controls already refute universal transparency.

**PROVED — conditional completion arithmetic.** The theorem is unconditioned. For conditioning on the specific top-grinding completion event alone, division by its independently computed tau_top is valid; that event is not a substitute for arbitrary OS/time-limit completion. No total abort/retry API is invented.

## 6. Scope and remaining targets

**COMPUTED — target warning.** Already delta caps at one when Q=2^64; so the accepted sufficient sum is vacuous at that stipulated query budget. A vacuous sufficient upper bound is not an attack. No quantum q_max/category certificate follows. The per-candidate FORS exponents and a plain Grover square-root reading remain separate from this finite-QROM advantage expression.

**PROVED — independent review scope.** Both complete-composition readers accept the pointwise partition for quantum-produced classical transcripts, projection of each separate event to ordinary HJ, private-hop final handler, initiated calls, row reads, single seed-zero charge and honest-cache view equality. Component controls and all sixteen numerical rows are separately reproducible. This is a manually reviewed mathematical theorem; component Lean/EasyCrypt checks are not a mechanical verification of the full Rust implementation or quantum proof.

**OPEN — original level/category goal.** The theorem does not certify a classical/quantum signing capacity, category1, efficient generic PRF/PRE/SPR/TCR embeddings, actual SHA-256, physical leakage or broad corrupt-cache/total-failure APIs. The sufficient Q=2^64 bound is vacuous. A tighter event-specific private hop is separately proposed in QUANTUM-PRIVATE-RARE-EVENT-DRAFT.md; it does not alter this accepted conservative theorem. The complete-security goal remains active and its printable level/category assertion remains “not established.”
