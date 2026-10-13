# Stress test of the manual privatization lemma

**PROVED / OPEN scope.** This supplement checks the five obligations requested after `DERIVATION.md` was independently saved. It does not read or revise the existing proof packet. The result is a classical event-distance argument in a specified idealized interface, not an efficient complete-signature reduction or a machine-checked Rust refinement.

## 1. Continue IDEAL after Bad

**PROVED.** IDEAL must run its entire program without using K/P, except to evaluate a private analytical Bad flag. The flag cannot alter answers, terminate the ideal experiment early, select a branch, or disclose itself. F/J are maps on public labels, and O_pub is one independent full public oracle. Setup, all signing attempts, later adversarial requests and final verification therefore remain functions of independent F/J/O_pub tables, S and public/adversarial coins even after Bad. This is the independence used to bound the complete candidate lists. It is stronger than claiming a uniform key conditional on no earlier hit.

**PROVED.** Given the continued key-independent ideal execution and fixed S≠0, let G_K and G_P be the full distinct candidate sets. They depend on that execution, not K/P. Conditional on that execution, `Pr[K in G_K or P in G_P] <= (|G_K|+|G_P|)/2^128`. A stopping convention based on Bad would invalidate this proof structure unless a separate stopped-process lemma were supplied. The current coupling instead stops *agreement* at Bad while continuing IDEAL's outputs normally.

**COMPUTED.** `control.py` checks the exact unused-key list probability 2/16, the conditioned-on-failure next-guess probability 1/15 rather than 1/16, and the one-bit-leak negative control. These establish that the posterior distinction matters; they are finite illustrations, not the proof itself.

## 2. Final verification is not free for this event

**PROVED.** Final `verify_root` receives transmitted R/counter, computes I and E once each at 697–700, then uses public addressed types only. On S≠0:

| Final-verifier input | Hidden-family eligibility | Candidate |
|---|---|---|
| `R*||S||root||m*` | M_P iff R*=P; never D_K | R* |
| `U*||BE32(c*)||S` | M_P iff first half U*=P and second half U*=S; length excludes D_K | U*[0:16], only if eligible |
| FORS leaf/internal/root hashes | type 3/4; neither hidden family | none |
| WOTS digest/chain/PK hashes | type 7/0/1; neither hidden family | none |
| Hypertree path hashes | type 2; neither hidden family | none |

At most two candidate P values are added. A local verification performed by A already consumes its raw oracle budget. If a different game grants v uncharged verifier calls, its bound adds 2v rather than silently using the present final-verification constant.

## 3. Full responses and prequery consistency

**PROVED.** F(A) and J(m) are full uniform 32-byte images. Source private calls use their prefixes, but the coupled real raw oracle at a hidden point returns that exact full image. The remaining 16 bytes are sampled once and retained, not sampled independently each time a raw query arrives. Public O_pub at such a point is an independent full image, and the executions can differ there after Bad; no attempt is made to overwrite an earlier O_pub response to preserve a false no-Bad invariant.

**PROVED.** Using the complete hidden sets catches a raw prequery to a future private point even if F(A) or J(m) has not yet been requested by honest computation. Static coupling is a mathematical construction on independent tables. A lazy implementation can instantiate the full hidden image on first use. This does not allow programming an already returned raw image without declaring Bad.

## 4. Precisely choose the signing/setup experiment

**PROVED (request-bounded form).** `DERIVATION.md` defines q as a bound on *initiated* atomic signing requests, incremented before evaluation. A nonterminating request is absorbing and offers no subsequent public interaction. It uses unconditioned setup; unsuccessful setup has no winning completion. In this experiment the conservative bound is `(Q_H+2q+3)/2^128`, capped at one.

**PROVED (completed-call variant with one pending request).** If q instead bounds completed calls and the interface permits one additional request to begin before an absorbing nontermination, use the number N_I of initiated requests explicitly. For every finite interaction prefix N_I≤q+1, hence a safe bound is

    min(1, (Q_H + 2(q+1) + 3)/2^128)
      = min(1, (Q_H + 2q + 5)/2^128).

If the oracle refuses a further request once q completions have been returned, N_I≤q and the smaller request-bounded formula applies. Do not switch between the two budget conventions without declaring which rule is implemented. The bound based on q+1 covers a currently pending call rather than presuming all initiated requests completed.

**OPEN (other failure interfaces).** This accounting relies on the atomic interface's absorbing nontermination. Explicit aborts followed by retries, interrupted calls, resumed execution frames, different failure responses or arbitrary cache faults can permit more initiated requests and observables. In such a game, use a bound on attempts and re-audit noninterference; completed-call count alone is insufficient.

**PROVED / OPEN (conditioning).** Unconditioned setup is essential to the displayed joint probability comparison. For S=0 the full event is charged at 2^-128. A separate setup-success-conditioned distribution requires control of both normalization probabilities; the unconditional event distance does not automatically become the same bound after conditioning. Neither the source caller's fixed benchmark seed nor a silently rejected public seed is the stated uniform setup distribution.

## 5. Deduplicate and charge public-seed degeneracy separately

**PROVED.** The candidate list counts literal values, not hash invocations. Repeated signing messages reuse the same J value and inner U, adding no new candidates. Repeated outer counters keep the same U prefix. Type-7 WOTS grinding adds no eligible secret point on nonzero S. Repeated raw guesses also add no distinct value. The use of 2N_I is only a conservative cap; it need not be attained.

**COMPUTED.** The control uses 256 distinct outer counter inputs and finds one distinct possible P prefix. It also shows the structural overlap when S=0. This event is charged before applying the nonzero-S parser separation, rather than being discarded by an unstated key filter.

**PROVED (REAL marginal on the charged branch).** On S=0, start with immediate Bad and continue REAL with one ordinary shared random oracle for all real inputs. Independent F/J values must not replace real evaluations at overlapping points on that branch. IDEAL retains its defined independent maps and shared public oracle. Coupling agreement is no longer required after immediate Bad, but both correct marginals are required. This explicit completion adopts the second reader's clarification without changing the bound.

## 6. Exact exposure restrictions and simulator resources

**ASSUMED (exposure).** The public transcript consists of the public key, chosen raw messages, completed signatures, raw public-oracle queries/responses, opaque honest snapshot handles and restoration validity responses. It does not contain K/P, the seed-bearing persisted fixture, private Ctx access, timing, compression-call counts, in-flight values or cache bytes. Honest snapshots restore one fixed key; handles do not disclose serialized state. Adding the actual fixture's 48-byte seed header trivially defeats the unused-key independence premise. Exposure of a smaller derived cache payload would require a newly specified game and its own security analysis; no such claim is obtained merely from this lemma.

**ASSUMED / PROVED under the stipulated interface (handle independence).** “Opaque” alone does not constrain how labels are generated. Specify sequential integer handles beginning with 0 and restoration-validity responses determined only by previously assigned handles, without inspecting or hashing K/P or their serialization. Make that same rule part of REAL and IDEAL. It is then key-blind and preserves continued ideal noninterference, including after the hidden Bad flag. No source claim about concrete persisted-fixture handles is inferred from this abstract interface.

**PROVED (resource distinction).** Static infinite tables make the coupling easy to state, but need not be materialized: F/J/O_pub may be lazy maps indexed by their exact strings/labels. This saves the complete 19-quadrillion-address namespace from becoming a required allocation. Nevertheless constructing the honest public key and answering a signature through the actual source flow still requires its real tree/chain work. Cache setup, cold signing and counter searches are not free local reduction computation merely because their source inputs cannot guess K/P.

**OPEN (efficient reduction).** The coupling establishes event distance without promising a polynomial worst-case sampler or an efficient black-box reduction at budget T. Source searches are partial and their worst-case execution contract is absent. A concrete distinguisher/reduction must charge its actual setup, private-function oracle queries, public oracle-internal work, memory and bookkeeping, and explicitly handle noncompletion. The classical adversarial query count Q_H is not the sum of every honest source hash call, but honest calls still have execution cost. This distinction cannot be used to manufacture an efficient algorithm from the statistical argument.

**OPEN (remaining complete-game bridge).** Even accepting this manually derived joint-privatization step leaves the ideal scheme's adaptive inner/outer hashing, source routing/coverage bridge, WOTS certification, tree extraction and composition security open. Any independent adaptive-coverage result must be connected to these actual shared inputs and private-R generation. This lemma deliberately leaves public H_inner/H_outer on a common oracle rather than declaring them independent. It also gives no QROM key-guess lemma.

**Final status.** Posterior independence is proved for the *continued unflagged joint ideal execution* under the explicit exposure/model assumptions. Exact source-model refinement and efficient complete-signature security remain OPEN. The conservative loss is available in both initiated-call and completed-plus-one-pending conventions; neither is a full 128-bit forgery bound.
