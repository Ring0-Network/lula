# Independent shared-SHA secret-input derivation

**Scope and independence.** This derivation was saved before reading the root proof or other agents' new extension reports. The original user attachment was read in full, then the pinned actual release library was inspected. No source, manuscript, earlier proof packet or benchmark file is changed. This addresses one classical shared-oracle privatization step, not complete signature security.

## 1. Source binding and model

**COMPUTED.** Release library `publications/LULA-I/release/code/lula1/src/lib.rs` has SHA-256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Source anchors below refer to that file. `N=16`; `Ctx` stores private `sk_seed` and `sk_prf` at 104–105; keygen splits the 48 caller-supplied bytes at 498–506.

**ASSUMED.** The key distribution is independent uniform K=`SK.seed`, P=`SK.prf`, S=`PK.seed`, each 128 bits. S becomes public; K and P remain private. Seed length 384 bits does not make either secret's guess entropy 384 bits. Benchmark fixture seeds do not have this distribution.

**ASSUMED.** Model complete SHA-256 evaluations as one shared random oracle O from finite byte strings to 256 bits. The adversary makes at most Q_H classical raw queries, including any pre-key or pre-signature queries. Pre-key queries can be represented by sampling the private coins at time zero and withholding their disclosure. Direct access to the SHA compression function, quantum superposition queries, timing, instrumentation, cache bytes, secret-bearing benchmark fixtures and private signer objects are not interfaces of this lemma. Prepared compression state in `Ctx::th` merely computes the ordinary SHA input in this model; this is not a standard-model theorem about actual SHA-256.

**PROVED (source).** Reference signing emits only completed signatures in the ordinary single-root interface, uses `sign(...,false)` (601–668), and verification uses the root-equality wrapper 672–674. Counter searches are partial: no exhaustion response is added. At most q initiated signing calls and one final challenger verification are considered. Local adversarial verification computations consume their raw O queries from Q_H. The final verification may consume extra oracle work, counted separately below. Setup completion is not silently conditioned away.

## 2. Exact hidden input sets and observable labels

**PROVED (encoding).** Let B=S||0^48 and A be the 22-byte address at 69–95. Its type byte is at offset 9 within A. All address integers are big-endian. The secret-derivation points are

    D_K = { B || A || K : A has type 5 or 6 in the fixed source namespace }.

Every point has length 102 bytes. Type 5 is WOTS chain-start derivation (248–250); type 6 is FORS leaf-secret derivation (348–350 and 391). The family label A is public. The same label must give the same value on all repeat calls. Derivation returns the first 16 bytes of O at that point (161–163).

**PROVED (encoding).** The message-randomizer points are

    M_P = { P || S || m : m is any finite byte string }.

Their minimum length is 32 bytes; label m is raw bytes, without a context or prehash wrapper. `prf_msg` (164–168) returns the first 16 bytes. The set includes messages not yet queried to the signing oracle: this is necessary to handle prequeries and future adaptive requests.

**PROVED (source).** Every other addressed operation starts with B but uses type 0,1,2,3,4 or 7: chains, endpoint compression, Merkle/FORS nodes, root compression, and WOTS message/counter digests (60–67, 216–220, 239–245, 251–256, 291–330, 348–409). Their inputs cannot be in D_K because the type differs. Repeated or adversarially selected node values do not change that type byte.

**PROVED (source).** The unaddressed public operations are

    I(R,m) = R || S || root || m            [170–172]
    E(U,c) = U || BE32(c) || S              [174–187]

Signing uses R from the private message-randomizer and U=O(I(R,m)); every FORS outer grinding trial uses the same U (603–610). Verification uses adversarial R and c (697–700). The WOTS counter search is addressed type 7 and adds no new unaddressed input family.

**PROVED (observable labels).** The adversary sees S, root, the messages it queried, each returned R, selected route/indices derivable from public hashing, revealed FORS values, WOTS values/counters and authentication paths. It chooses its raw oracle strings and all final signature fields. It does not see K/P themselves, all internal PRF results, a typed private signer `Ctx`, elapsed timing or the private snapshot header. The signature may reveal an F(A) output, but that is not the suffix key K. Calling the public Rust method `Ctx::prf` on the actual private context is key access, not an extra oracle allowed in this game.

## 3. Structural separation sufficient for a joint replacement

**PROVED.** On the event S≠0^16, D_K and M_P are disjoint for every K and P. A D_K point's bytes 16–31 are zero; an M_P point's bytes 16–31 equal nonzero S. The same observation shows that every nonsecret addressed input is outside M_P. No probability assumption about node values is needed.

**PROVED.** On S≠0^16, an I input cannot lie in D_K: its bytes 16–31 equal S while D_K requires zero. An E input has length 52, so cannot lie in D_K. Thus only the adversary's raw queries can hit D_K; honest addressed computations and the two unaddressed public families cannot hit it.

**PROVED.** Every raw query can be eligible for at most one of D_K and M_P on S≠0^16. For D_K it contains one literal K candidate in its last 16 bytes; for M_P it contains one literal P candidate in its first 16 bytes. This means one raw query should not be charged as two independent key guesses. A huge derivation-address namespace does not multiply this literal-guess count.

**PROVED.** I(R,m) is in M_P exactly when R=P; its message label is `root||m`. E(U,c) is in M_P exactly when `U[0:16]=P` and `U[16:32]=S`; its message label is `BE32(c)||S`. All E trials for the same U therefore offer the same possible P candidate. Changing a 32-bit grinding counter does not create 2^32 different P-prefix guesses.

**ASSUMED / charged degeneracy.** Uniform S has probability 2^-128 of being all zero. Rather than alter key generation or pretend separation always holds, charge that entire event as bad. This is conservative: actual overlap can require additional equalities. No seed rejection is introduced.

## 4. Joint real/ideal games and coupling

**PROVED (game definition).** REAL uses O for all source operations, including private points D_K and M_P. IDEAL uses an independent memoized 256-bit map F indexed by A and an independent memoized 256-bit map J indexed by raw m for those two private derivations. Their first 16 bytes replace the source PRF/randomizer outputs. IDEAL uses one common independent raw oracle O_pub for every other honest and adversarial hash input. K and P are retained as independent unused coins for analysis. All source address selection, tree construction, first-counter searches, signature parsing and public verification otherwise remain unchanged.

**PROVED (full images).** Although source private calls consume only 16 bytes, sample full 256-bit F/J images. If a public query later reaches a private point, the real oracle returns all 32 bytes; a coupling that sampled only prefixes would omit this consistency obligation. Repeat labels return the same full image.

**PROVED (coupling construction on S≠0).** Sample K,P,S,F,J,O_pub together. Define the coupled real oracle by

    O_real(x) = F(A)       if x=B||A||K is in D_K;
                J(m)       if x=P||S||m is in M_P;
                O_pub(x)   otherwise.

The hidden sets are disjoint, their label-to-input encodings injective, and all full images independent uniform. Conditional on K,P,S, O_real is exactly a random oracle; its distribution does not become a different function family. In REAL, source private derivations use F/J. In IDEAL they also use F/J, while public evaluations use O_pub. The two executions therefore agree at every step until a public evaluation hits D_K or M_P. This includes prequeries: the bad event refers to the complete hidden sets, not only points previously queried by honest signing. No later overwrite of a prequeried raw table entry is permitted.

**PROVED (zero-seed branch and correct REAL marginal).** When S=0^16, declare Bad immediately and sample an ordinary shared random oracle for REAL. Every real private and public evaluation uses that oracle, including overlapping inputs; do not use inconsistent independent F/J images at overlapping real points. Continue IDEAL with its independently defined F/J/O_pub tables. The two executions may be coupled arbitrarily after immediate Bad. This completes the global coupling while preserving each marginal and the charged probability 2^-128; the good-event construction is not applied to the degenerate branch.

**PROVED (bad definition).** Bad is S=0, or a raw adversarial query/honest-public call/final-verifier call entering D_K or M_P. Bad is a private analytical flag; it does not change IDEAL outputs or send an extra response. Before Bad, all completed public transcripts, signature bytes, setup/signing completion behavior and the winning event are coupled identically. For any bounded public event E,

    |Pr_REAL[E] − Pr_IDEAL[E]| ≤ Pr_coupling[Bad].

For a nonterminating source search, consider finite interaction prefixes; its unaddressed prefix candidate is fixed, and repeated counters add no guesses. The same partial computation persists while no Bad occurs. No theorem of total termination is being claimed.

## 5. Posterior independence: what is proved, and what is not

**PROVED (IDEAL noninterference).** On fixed nonzero S, the unflagged entire IDEAL execution never uses the values K or P: it uses F/J indexed by public labels, the raw public oracle, adversarial coins, and the fixed source procedure. Therefore its public transcript and adaptive public-query schedule are independent of K,P. This is an exact property of the *joint ideal game*, established by induction on its calls, not an assertion about the actual real posterior after observing a signature.

**ASSUMED (explicit snapshot interface).** If honest snapshot commands are included, initialize handle 0, assign the next sequential integer on each Snapshot, and check Restore validity solely by membership/range in the set of assigned handles. No label, validity bit or request-acceptance decision may hash or inspect K/P or a secret serialization. The coupled mathematical interface uses these same key-blind responses in both games; honest restoration preserves the declared fixed signing function. This is a model stipulation, not an implementation theorem for the seed-bearing benchmark snapshot codec. Under this rule, the preceding noninterference induction includes handles and restoration responses; mere use of the word “opaque” would not specify it sufficiently.

**PROVED (adaptive finite guessing lemma).** Let an unused uniform key take M=2^128 possible values. A candidate list of length at most g may depend adaptively on any key-independent unflagged execution. Conditional on that execution, the list is fixed and contains at most g distinct values. Hence the probability the key occurs in it is at most g/M. The same union argument applies to two independently unused keys, allocating candidates to their respective families.

**PROVED (survival posterior).** Conditioning additionally on a hidden “no earlier hit” event removes tested keys. Given a transcript and distinct earlier guesses G, a surviving key is uniform on the complement, not on all M keys. A fresh surviving conditional guess can therefore have probability `1/(M−|G|)`, which is larger than 1/M. This does not invalidate the unconditional g/M bound proved from the unflagged ideal execution. It does invalidate an argument that assumes the unchanged 1/M posterior after conditioning on all prior failures.

**OPEN / false generic premise.** Independent uniform key generation alone does not make a key posterior independent of arbitrary outputs of a real keyed algorithm. An algorithm that reveals one key bit doubles a one-guess success probability in a small exact control. For this step the justified independence is IDEAL noninterference, followed by coupling; one may not assume the same property for REAL to prove the coupling circularly. Likewise a separate secret-derivation-only hybrid that leaves PRF_msg real needs its own consistency analysis. The joint replacement avoids claiming an unproved intermediate independence premise.

## 6. Source-bound candidate accounting

**PROVED.** On S≠0, the Q_H raw adversarial queries contribute at most Q_H total candidate keys across D_K/M_P, because eligibility is disjoint. Each initiated signing message contributes at most one I prefix R and one E prefix U[0:16], hence at most 2q additional P candidates. First-acceptance grinding can be long or wrap, but all its E points keep the same U. Other honest hashing, including potentially billions of tree/chain operations and type-7 WOTS grinding, contributes no private-point candidates by the domain checks in §3. Setup uses addressed operations only (498–573), so does not contribute these unaddressed candidates.

**PROVED.** One final challenger verification adds at most two P candidates, for its I and E calls; all subsequent verification hashes are addressed public types. Local adversarial hashing/verification is already charged to Q_H. If the interface gave V additional uncharged verifier-oracle calls instead, replace this final contribution with 2V; that is a different interface. Repeated candidates can only reduce the bound.

**PROVED (classical joint-privatization lemma under §1's model).** With uniform independent seed components, q initiated signing queries, Q_H raw classical adversarial queries and one final verification,

    Δ_joint ≤ min(1, 2^-128 + (Q_H + 2q + 2)/2^128)
            = min(1, (Q_H + 2q + 3)/2^128).

This is a conservative distinguishing/event-probability loss for replacing the two hidden-input families jointly. It does not include a factor equal to the number of private addresses or secret derivations. It does not make public hash domains independent of one another. An alternative proof which blindly charges every internal SHA invocation would be much looser; the source input inventory justifies the narrower candidate bound.

**PROVED (budget qualification).** Here q bounds initiated requests. If q bounds completed calls and one additional pending request is permitted before absorbing nontermination, use `min(1,(Q_H+2q+5)/2^128)` instead. `STRESS-TEST.md` states the exact variants, continued-after-Bad noninterference, final-verifier accounting, setup conditioning and efficient-simulator boundary.

**PROVED (completion scope).** The bound is for the unconditioned partial game, treating noncompletion as no winning completion. A separately normalized experiment conditioned on successful setup must relate its conditioning probabilities; dividing or renormalizing without such an argument is not licensed here. IDEAL setup itself does not depend on unused K/P, but the coupled REAL setup may diverge on Bad. An interface revealing timing, hash-compression counters, cache serialization or secret-bearing fixtures also requires a new candidate/noninterference analysis.

## 7. Missing bridges to complete security

**OPEN — source-to-model validation.** The input-domain argument and classical coupling above are manually derived from the pinned source. Independent checking should verify every honest hash site and the raw-query interface; no proof assistant has checked the Rust refinement. Actual fixed SHA-256 is modeled, not proved random. This is not a decisional-PRF theorem in the standard model and is not HMAC.

**OPEN — full ideal-game security.** Bounding the difference to IDEAL says nothing yet about IDEAL's forgery probability. Public H_inner/H_outer remain the *same* oracle and can collide/alias; the forced-bit and route sampling distributions must still be handled adaptively. FORS coverage, same-fixed-child WOTS digest/chain binding, endpoint/Merkle extraction and the composition reductions remain necessary. In particular, setting these terms to zero because private keys are idealized would be false.

**OPEN — tightness/target interpretation.** This conservative privatization loss may already exceed a demanded tiny advantage at large q. It is not a demonstrated forgery strategy or proof that the parameter set fails a work-factor target. A tighter event-to-forgery analysis may be possible; no full signing capacity or 128-bit total claim follows by merely inserting this loss into the still-open table.

**OPEN — QROM.** A classical raw query specifies one candidate key; a quantum superposition query does not. The union/counting argument cannot be reused as a QROM lemma or replaced casually by a square root.

**PROVED / COMPUTED useful progress.** The next posterior-independence obligation can be proved in a *joint* ideal game with unused keys and a shared public oracle. It need not be assumed for the real transcript. The exact remaining bridge is to prove the ideal signer's security and validate any extra exposed interfaces, not to assert complete security from key-guess counting. The small control accompanying this derivation checks the survival-posterior and leakage distinctions and literal source-format overlaps; it is not a cryptographic experiment.

**COMPUTED (control receipt).** `python -I -B control.py` returned exit 0, producing `CONTROL-RESULTS.json`. It verifies the live source hash, exact finite guess/survival/leakage examples, nonzero/zero public-seed encoding cases, deduplication of 256 outer trials to one prefix candidate, continued ideal outputs independent of the hidden Bad flag, and consistent full 32-byte hidden responses. No signatures or full cache were generated.
