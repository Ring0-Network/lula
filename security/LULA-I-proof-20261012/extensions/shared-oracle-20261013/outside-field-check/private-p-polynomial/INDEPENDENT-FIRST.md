# Independent first: mixed coherent/classical private-P hop

Saved before reading root PRIVATE-P-CANDIDATE.md or any new private-P peer proof. This is an independent source/OLD-proof derivation. Status: ACCEPTABLE MANUAL CANDIDATE under the exact finite classical-atomic-service random-oracle model; no fixed-SHA or whole-security claim.

## 1. The central obligation and source forms

The structural question is whether one can make the honest source channel marker-independent without discarding the genuine coherent public channel, and charge the resulting source aliases separately. A decision polynomial cannot count only adversarial queries when uncounted honest hashes are themselves marker-dependent. A hybrid that blindly substitutes those hashes can support the polynomial proof, but must then pay its faithful-source discrepancy.

Fix S nonzero, N=2^128, uniform private P independent of all initial coins, complete finite raw-string register, q initiated classical atomic signing calls, and Q_A adversarial full-output oracle queries including pre-key queries. Opaque honest restores, no private bytes/timing/interrupted/coherent signing services, absorbing noncompletion and a single classical final verifier remain as in the old model.

Source 164–168: nonce R=prefix128 O(P||S||M). Source 170–187: inner I=R||S||root||M; outer E_c=U||BE32(c)||S. Sign601–617 uses one R and one U per initiated call, then grinds c with fixed U. Final679–700 rejects malformed signatures first and otherwise uses one transmitted R and one U, one selected counter. Addressed words121–162 begin S||zero48. Therefore for S≠0 no addressed keygen/sign/verify word is in M_P={P||S||m}; its bytes16..31 are zero, whereas M_P requires S. Keygen has no exceptional P nominations. The two possible public nominations per call are R (inner) and U[0:16] (outer, eligible only if U[16:32]=S). Every outer counter uses the same nominee. There are at most m=2q+2 nominations, even when later counter exhaustion/noncompletion occurs. The final verification has zero private nonce calls.

## 2. Exact full-output coupling

Independently sample an ordinary full256 base table O0 and a full256 nonce table J(m) for EVERY raw eligible suffix m, not only signing messages. The logical private nonce service returns prefix128 J(M). Keep all other source private state/maps independent of P. Define O_P(w)=J(m) for w=P||S||m and O0(w) otherwise. For each fixed P, the eligible words are injective, so O_P is a complete uniform full256 random function; its correlations with the nonce service are exactly the literal source correlations. J lower limbs are included, although the service returns only the prefix. A raw inner alias uses J(root||M), not necessarily J(M); an outer alias uses its entire remaining suffix. No suffix is omitted from the overlay.

This can be the P-only hop after privatizing K. Alternatively K may remain coupled in the base table by the OLD disjoint D_K overlay; all that auxiliary data/code is independent of P and D_K is disjoint from M_P at S≠0. This argument does not silently prove or reprice the K hop. Whole finite tables and actual source setup/signing computation remain charged; no efficient simulator is inferred.

## 3. Three routes and the new intermediate experiment

Route A retains the OLD conservative linear distance 2Q_A/sqrt(N)+m/N. Route B uses the OLD shared stopped projector and a whole-winning square-root bound. Route C, pursued here, separates a polynomial decision comparison from a stopped alias probability.

Define G1 (blind honest / genuine public): adversary queries use O_P. Every honest PUBLIC source hash, including I/E and final verifier calls, uses O0; private nonce uses J. Other private maps and source computation/cache remain consistent. Define G0: exactly the same blind source channel, but adversary queries also use O0. G0 is the ordinary ideal-nonce game for this P-only hop. Neither G1 nor G0 lets a public service inspect P; source code/coins, private maps, J and O0 are the SAME joint accessible law. G1's total adversary state may depend on P through its public queries: do not call that state P-blind.

Faithful ordinary source REAL (adversary and public source use O_P, nonce J) agrees with G1 until the FIRST honest/public I/E alias. Private calls always agree; all other honest public calls are disjoint. On no-alias branches the exact source outputs, roots, caches, canonical counters and verifier outcomes coincide. Stop immediately BEFORE a differing honest hash; no continuation after that stop is needed to bound Win_REAL≤Win_G1+Pr_REAL(first alias). This proof-side stop is not a production abort/retry interface.

## 4. Polynomial decision difference with Q_A only

For each prefix p∈[N], let b(p) be a Boolean marker. Complete adversary public replies with known pair O0(w)/J(m), chosen by b(first16(w)) when bytes16..31=S; other words have equal pairs. For b=e_P this is O_P; for b=0 it is O0. Fourier response parity kickback implements each complete-output query with ONE clean ordinary Boolean XOR query, including lower limbs, invalid/outside branches and retained entanglement. No controlled-unknown oracle or additional unknown uncomputation is assumed.

Fix marker-independent common O0,J, all source/private coins and any auxiliary reference state. The blind honest service remains fixed linear code, possibly adaptive to measured counted query replies, and never reads b or P. Its enormous internal O0 hashes do NOT add Boolean degree. Thus Win acceptance is a real multilinear degree≤2Q_A polynomial bounded [0,1] on every Boolean table. Averaging over all weight-k marker tables gives p(k), degree d≤min(2Q_A,N), with integer-grid values [0,1]. Uniform one-mark G1 acceptance is p(1), zero-mark G0 is p(0). The grid Markov proof already independently derived for UD gives |p(1)−p(0)|≤d²/(N−d²) for d²<N. Hence

v(Q_A)=min(1,4Q_A²/(N−4Q_A²)) when 4Q_A²<N, otherwise 1.

At Q_A=0 the comparison is exactly zero. Unlike UD, there is no factor 1−1/N: this is weight-one versus weight-zero, not planted-iid versus iid. Arbitrary entangled auxiliary data is permitted only if its SAME joint initial law is marker-independent; a free marker/P register or experiment-label bit destroys the premise. Post-query adaptations are not independent advice and are included via common fixed code/purification.

## 5. Common stopped CQ alias bound

Let C1 and C0 be G1/G0 stopped BEFORE the first public source nomination equal to P. The detector records P in an inaccessible classical environment and evaluates equality only on the measured classical source-call word. At a no-alias source step, O_P=O0 and private nonce=J, so the stopped REAL source controller and C1 are the SAME channel up to stop. C1/C0 have identical honest service/stop channels; their only discrepancy is the adversarial coherent oracle.

For the unflagged G0 continuation, conditional on fixed S/O0/J/other source data, P remains uniform and unused by the entire classical/quantum state. Each nomination (including a final R chosen from an adaptive quantum-produced signature) is P-independent in this continuation. Its first-alias event is ≤min(1,m/N), by the union bound on at most m nominated values. This does NOT condition on normalized survival, and does NOT use independence of nominees in G1.

At packed adversarial query slot j, the C0 surviving state is a deletion of whole dephased environment/history blocks of the unflagged G0 prefix. Each block retains arbitrary coherent memory. The unnormalized support mass on M_P is therefore bounded by that of the unflagged prefix, at most 1/N. This is classical block deletion; it is NOT the false general coherent claim PρP≤ρ. Purifying with orthogonal copies of environment/history gives local squared oracle discrepancy ≤4/N. Pack all common honest/measured scheduling operations between adversarial queries into common isometries; pad halted branches with clean invariant-plus responses. Telescoping Q_A slots yields ||Ψ_C1−Ψ_C0||≤2Q_A/sqrt(N).

Apply the SAME terminal first-alias event projector. Faithful source REAL first-alias probability equals C1's. Consequently

Pr_REAL(alias) ≤ min(1,(2Q_A+sqrt(min(N,m)))²/N)
             ≤ min(1,(2Q_A+sqrt(m))²/N).

The tester need not be marker-independent: it is common in C1/C0 and its probability is bounded in the unflagged P-independent ZERO continuation. A polynomial applied directly to this key-dependent tester would be invalid; the two arguments must remain separate.

## 6. Proposed lawful combined hop

For any final classical Win predicate that does not itself read hidden P,

Pr_REAL(Win | S≠0) ≤ Pr_G0(Win | S≠0) + alpha_P,
alpha_P=min(1, v(Q_A)+(2Q_A+sqrt(2q+2))²/N).

The same absolute blind decision difference can be used for other bounded classical terminal predicates. The stated direction suffices for security; this derivation does not assert a complete trace-distance bound with alpha_P, nor whole-law equality of G1 and REAL. Fixed-SHA private-PRF assumptions and evaluated hardness remain separate. Uniform S=0 is charged once in complete composition, never independently added twice for K/P. Query/call budgets and existing numerical receipts remain unchanged until a separate promotion.

## 7. Discriminators and limits

Required toy controls: (i) one-query known-pair full-output completion; (ii) unique-vs-zero acceptance symmetry and Q=0 exact equality; (iii) dephased block deletion and normalized-survival inflation; (iv) raw-byte S=0 addressed-family overlap negative; (v) all outer counters share one nomination; (vi) P-aware blind service/free advice breaks polynomial independence; (vii) hypothetical coherent signing would invalidate the common CQ service proof. The old sources already supply the block-deletion and source alias facts; finite tests cannot replace the common channel derivation. No actual signatures/attacks/namespace generation are requested or performed.

There are zero new machine-checked source/game declarations. This is a candidate finite-RO inequality, not a category/capacity certificate, manuscript change or fixed-SHA claim.
