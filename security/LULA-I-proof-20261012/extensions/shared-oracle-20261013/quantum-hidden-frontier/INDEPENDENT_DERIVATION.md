# Quantum hidden-value frontier: static lemma, dynamic FORS candidate, and obstruction

**Independent first save.** No future peer hidden-quantum proof was read. Source semantics and primary literature were inspected directly. This document distinguishes a static mathematical lemma, an explicit failed static-to-dynamic shortcut, and a manually derived dynamic candidate requiring independent source/game review. No complete QROM security claim follows.

## 1. Primary O2H statement and receipts

Ambainis–Hamburg–Unruh's [author page](https://kodu.ut.ee/~unruh/publications/semiclassical.html) identifies the semi-classical O2H result and its oracle/input-distribution scope. The ePrint2018/904 and official CRYPTO2019 PDF endpoints returned403. I therefore do not claim to have directly inspected the original AHU PDF. The exact theorem used here was read in the primary full version by Joseph Jaeger, [Nonadaptive One-Way to Hiding Implies Adaptive Quantum Reprogramming](https://arxiv.org/html/2511.16009v1), Theorems2.1–2.2 and Figure3. The latter explicitly restates AHU Theorem3; the former gives the fixed-permutation version needed below. The downloaded primary PDF has SHA-256 `95609e630baf7fd7572591e5cdf2e4693d768dab51c8d2a095b9d120922d8965`.

For fixed permutations P0,P1, a distinguisher D with at most q permutation queries, and e in {1,1/2}, the primary statement is

```
|p0^e-p1^e| <= 2q sqrt(mu).
```

Here mu is the probability that measuring the input to a uniformly chosen query during a P0 execution gives an input on which P0/P1 differ. Use the ghost permutation as P0. The measured-query experiment halts there; it is not a simultaneous classical log of all quantum queries. Padding to q calls is permitted and only gives a conservative cap. State-augmented permutation queries can include private game tables and disclosure state, which the distinguisher controls while the original adversary sees only its public interface.

## 2. Exact static single-leaf lemma

Fix a valid source FORS leaf address A. Let Z be a uniform128-bit ideal private-map leaf secret; put M=2^128. Let X_A(z) be the injective raw type3/height0 input `S||zero48||Addr22(A)||z16`. Sample an independent uniform full256 image W and a uniform full256 base oracle G. Define H to equal G except H(X_A(Z))=W. Its complete-table marginal is exactly an ordinary uniform random function conditional on Z. Give the adversary the public leaf prefix Y=first128(W), or even W, and Z-independent auxiliary data/graph derived from W and independent outside functions. Do not give it Z or a function of Z beyond the planted public relation. Other honest interfaces must not reveal Z.

In the ghost experiment G,Y and all query-generation state are independent of Z. At any measured raw query, X_A's framing admits at most one literal z candidate. The measured-hit probability is therefore at most1/M, regardless of the coherent query amplitudes. O2H gives

```
|p_H^e-p_G^e| <= min(1,2Q/sqrt(M)), e=1 or1/2.
```

If the terminal predicate is exact output recovery `z_hat=Z`, the ghost success is1/M. The controller can check that predicate after the last query without revealing Z beforehand. Thus

```
Pr_H(z_hat=Z) <= min(1,(2Q+1)^2/M).
```

This concerns exact secret recovery, not arbitrary alternative preimages or the full forgery event. The explicit planted full256 value preserves suffix answers; merely replacing a public128-bit prefix would be an incomplete oracle model.

## 3. Exact obstruction to retaining a static ghost after disclosure

The source `FORS::sign` reveals the selected private leaf secret. If the ghost still returns G at X_A(Z) after revealing Z, one classical query at that point distinguishes it from H using Y: real matches with probability1; ghost matches with probability1/M. The advantage is1-1/M. Under O2H the measured-hit probability after disclosure is1, not1/M, so the theorem remains valid but the static numerical substitution does not.

This is a counterexample to a proof shortcut, not a LULA I forgery. A source-consistent dynamic ghost must reconcile disclosed canonical points before returning the signature, or use an appropriate state-augmented/oracle-reprogramming argument. A classical claim that no hidden literal guess was logged cannot substitute for that argument.

## 4. Source-specific dynamic FORS model

Pinned `release/code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Lines344–364 construct FORS leaves and parents; lines383–391 disclose one secret per real tree. There are17 real trees with512 leaves. Every valid leaf has a distinct actual compressed type3/height0 address, including its instance/keypair and global leaf index. One raw point can therefore identify at most one leaf label i and one proposed secret z.

Work first in the declared ideal-F/private-start model with independent uniform Zi at every FORS type6 label. The real-source quantum replacement of its keyed derivation by this ideal map is **not proved here**. Sample independent full256 Wi for leaf images and an independent full256 base G. Program H(X_i(Zi))=Wi for every valid leaf i. Different leaf domains are disjoint. Conditional on all Zi, this preserves the complete public random-function marginal; internal FORS hashes are ordinary G at distinct height>0 domains. Authentication trees/roots computed from Wi prefixes and outside G are independent of the private Zi. Repeated secret values at different leaves do not collapse their raw input domains.

The ghost may disclose this output-labelled tree skeleton but cannot disclose canonical raw leaf inputs, which contain Zi. It may use G/outside functions and Wi privately. Giving an entire canonical-input graph would trivially reveal the very secrets this event is intended to protect.

Let R be a permanent set of leaf labels disclosed by completed honest signatures across every restored branch. A snapshot never erases R. Before emitting a signature, its message-derived leaf choices are computed from public roots, other private maps, and outside-domain hashes. On nonzero S the message inputs cannot equal the type3 leaf domains. Its FORS paths and certified root are functions of Wi/outside G, rather than Zi. Only the selected leaf values are then read and emitted, after their labels enter R.

Atomicity permits this rearrangement of the private computation for transcript purposes: a failed/nonterminating attempt emits no partial secret. The controller's other returned fields must depend only on outside functions, the output-labelled graph, and already disclosed/private variables independent of the undisclosed FORS Zi. The source data flow supports this for honest caches: subsequent WOTS signing certifies the FORS root, not a separate function of the selected secret bytes. This manual source-to-controller refinement remains subject to independent review; timing, arbitrary fault responses or cache-byte access are excluded.

## 5. Fixed permutations with reveal reconciliation

Store G, Z, W and R in game registers. Define response permutations on `(x,y:G,Z,W,R)`, leaving all game registers unchanged:

```
P_real:
  if x=X_i(Zi) for some valid i: y ^= Wi
  else: y ^= G(x)

P_ghost:
  if x parses a valid leaf label i AND i in R AND x=X_i(Zi): y ^= Wi
  else: y ^= G(x)
```

Both are fixed finite XOR permutations on the combined register universe. The controller updates R between queries; their definitions do not change. Disclosure reconciles that canonical point in the ghost before returning Zi, so later queries at the disclosed point are answered consistently in both games. P_real has the same static H oracle at all stages.

In P_ghost, if i is not in R, the response function does not depend on Zi at all. Its private disclosure scheduler does not read Zi until it decides to add i to R. Thus conditioned on any classical disclosure history `(R,Z_R)`, the joint adversary quantum state is independent of the undisclosed Zi, which remain independent uniform values. This is a classical-quantum unused-variable invariant, not a claim that the real queried values remain uniform after arbitrary survival conditioning. The ghost neither signals a hidden hit nor branches on such a flag.

At a measured permutation query, a raw x either is outside a valid leaf domain, has i already disclosed, or names one undisclosed i. Only the last case can make the permutations differ, and matching Zi has probability1/M in the ghost. The additional condition G(x)!=Wi only reduces that probability. Therefore

```
mu <= 1/M.
```

There is no multiplier for the number of leaf labels: each raw input fixes its own leaf address. There is also no direct signing-query factor here because the disclosure controller uses no differing-oracle query. This does not make its work efficient or remove the separate FORS coverage dependence on how many leaves have been disclosed.

The primary fixed-permutation O2H theorem then yields `|p_real^e-p_ghost^e|<=2q/sqrt(M)` for this explicitly state-augmented controller. Coherent pre-key queries are included in q and use the same G/Z/W tables fixed from the beginning. They are not measured or logged in the actual game. Registers have finite injective length/content encodings and the selected actual address fields are valid; no undefined infinite-register construction is used.

## 6. Small terminal events and final-verifier budget

For terminal output `(i,z_hat)` with i not in R, the ghost exact-secret recovery probability is at most1/M, even if i is chosen adaptively from the public transcript. The unused-variable invariant is needed for that assertion. With q=Q adversarial queries and no final source-verifier query, the dynamic candidate is

```
Pr_real(i notin R AND z_hat=Zi) <= min(1,(2Q+1)^2/M).
```

For a classical final signature, define E_secret as an actual accepted verification with at least one of its at most17 FORS secret fields equal to the canonical Zi at a leaf not previously disclosed. The ghost probability is at most17/M by a terminal union bound, ignoring acceptance. Selecting the leaf list may use message hash answers but not hidden Zi; its terminal equality test reads Zi only after all queries.

The actual verifier makes17 type3/height0 leaf calls. Its remaining hashes are outside this protected input class and can be computed from G; disclosed canonical calls are also consistent. A conservative state-permutation budget is q<=Q+17, leading to the **proposed manually derived scoped bound**

```
Pr_real(E_secret | fixed nonzero S, ideal private starts)
 <= min(1,(2(Q+17)+sqrt(17))^2 / 2^128).
```

The primary theorem supplies factor2, while17 counts source leaf fields/final leaf queries. This is the exact-canonical-unexposed-secret branch only. The new fresh-message signature could instead use all previously exposed leaves, or alternative preimages/node collisions; those are distinct branches. No bound for total forgery is claimed. Independent review is required before promoting this dynamic candidate.

## 7. WOTS predecessor obstruction and suffix closure

`WotsC::sign` at264–266 emits C(e), and verification completes the suffix via distinct position-labelled hashes at269–275. Emitting C(e) also makes every later chain position C(p), p>=e, computationally derivable. A reveal set that marks only the emitted node is therefore wrong.

For example, reveal C(1) on a chain with a public endpoint C(3), and reconcile only the position1 hash. One query yields C(2); a second ghost query at position2 returns an unrelated G output, while the real chain returns C(3). Prefix comparison distinguishes with advantage1-1/M. All suffix positions must be reconciled, not just the directly serialized position.

A possible extension samples a chain's nodes/full edge outputs in topological order, reveals endpoints initially, and updates per-chain disclosed cutoffs to include the entire suffix when C(e) is emitted. But edge Wi contains its successor node, so an outside-function/graph disclosure that includes hidden edge outputs would reveal hidden predecessors. The exact classical-quantum invariant for all chain cutoffs, source canonical digest selection, aliases and adaptive multi-key paths must be proved. That WOTS extension remains **OPEN** in this file; the FORS proof above cannot be cited as its proof.

## 8. Remaining boundaries

No original AHU PDF theorem was silently claimed read: its exact fixed-permutation formulation is taken from the verified Jaeger primary theorem, and its AHU antecedent is explicitly attributed. No standard source reduction is applied to fixed SHA-256. Quantum ideal-private-map replacement, WOTS suffix/controller refinement, security of adaptive FORS route selection/coverage, full final-forgery classification, efficient simulation/extraction and full QROM composition remain open. The public interfaces omit timing, crash leakage, partial-signature release, arbitrary cache corruption and mid-call restoration. A seed-zero branch needs its own charge if composing beyond fixed nonzero S.
