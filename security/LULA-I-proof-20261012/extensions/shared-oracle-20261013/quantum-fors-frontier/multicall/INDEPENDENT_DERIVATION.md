# Independent multi-message/full-row quantum contract

**PROVED (independence receipt).** Saved before opening `QUANTUM-COVERAGE-DRAFT.md` or any future peer multi-call proof. The first-call files are immutable. The primary AR theorem and independently derived coherent row lookup from that earlier lane are known. This document distinguishes a proved consequence of an explicit masked-IO contract from the still-to-be-checked source hop establishing that contract.

## 1. Minimal masked-IO/source contract

**ASSUMED (MC-IO).** Fixed nonzero S, single-root source, finite length-aware full256 raw oracle, classical atomic initiated signing calls and coherent adversarial raw queries. An already justified comparison game provides:

1. A memoized private namespace map V(m), unread by public raw queries before first Sign(m). At the first request for a new classical m, its unused full256 value is uniform independent of the complete prior prefix and outside base oracle functions. Adaptive selection among unused m preserves this law. A repeated m uses its existing R,U and row and generates no new latent draw.
2. Signed-message inner points may be publicly assigned their known U. A fresh final message has no such assignment: its transmitted R determines a base-inner point whose full value comes from the ordinary base inner restriction. That restriction is independent of the latent private namespace sequence before public querying. Inner assignments never read the base inner function to choose their U.
3. Eligible E points have U[16:32]!=S. They are disjoint from every inner input and from typed source graphs. A base eligible-outer restriction consists of iid full256 word outputs and is independent of the private maps and the other base functions.
4. Honest remaining source work uses private maps, fixed graph/metadata functions, the corresponding row and completed-call responses; it does not provide uncharged adversarial oracle access. Comparison bookkeeping and hash-oracle tables are global, not erased by Restore. Honest restored reference calls preserve the same functions. q bounds initiated requests globally, Q_q bounds coherent raw calls globally, and one final verification follows.
5. Noncompletion is absorbing/nonwinning. No successful-setup/NoBad normalization, coherent signing, timing, private-query/cache/fixture disclosure, compression access or corrupted cache is included.

**OPEN (source binding).** The distance from ordinary HJ to MC-IO is a preceding obligation, not assumed to be zero. Its exact definition and loss must be read and independently checked after this derivation is saved. This contract is not established by merely calling a private value fresh.

## 2. Guard coins and repeated namespaces

**PROVED (full-value decomposition).** Put N=2^128 and M=2^256-N. For every new message sample an independent guard coin with bad probability1/N; on a good coin draw U uniformly from G_S={u:u[16:32]!=S}, of size M. This reproduces a uniform full256 V(m) law before accounting for the bad branch. At most q new labels incur guard loss q/N. Repeated m reuses the stored guard and namespace; it creates no extra coin or entropy.

**PROVED (collision coupling).** Good draws with replacement can be coupled to draws without replacement, resampling only when a new namespace repeats an earlier namespace. Padding to q new labels gives mismatch probability <=binom(q,2)/M. This is a comparison loss, not a reliable-loss-detection API. It prevents later row programming from changing an earlier message's immutable row. A full raw U, not a bucket or a randomizer prefix, is the collision key.

**PROVED (fresh distribution after replacement).** In the distinct-namespace comparison, conditional on the entire prior prefix and the previous r-1 namespaces, the next good U is uniform over their complement in G_S. Its point-density maximum is exactly1/(M-r+1). Previously revealed namespaces can affect the adversary's message choice but cannot inspect an unused V(m) entry in MC-IO. Do not condition on all later success/NoBad events and then assert this density; the sampler is defined sequentially with those conditional distributions.

## 3. Full-row AR query contract

**PROVED (row-valued oracle).** Row(U) is the C=2^32 tuple of full256 images at U||BE32(c)||S. Its finite output register has256C=2^40 qubits. The one-query plus-state selected-slot construction exactly implements one coherent raw eligible-word query from one Row query, including coherent outside/dummy branches. Its work space is enormous; no efficient/PPT simulator is claimed.

**PROVED (honest read counts).** Reprogram returns U, not the programmed row Y. Therefore the source simulator must query Row(U) once after each new-message instruction to obtain the entire row for its private classical computation. It caches that row and simulates the source's first-zero search and any repeated-message request locally. The extra read is one oracle query before the next instruction. It cannot be dropped because it is an honest source call. It need not be multiplied by C because it reads the row-valued output at once.

The private read preserves the ordinary fixed-function source law: unused words are never disclosed to the adversary, and future raw calls still evaluate that same function. A completed signature depends only on the ordinary source's selected prefix and other fixed functions. If the row has no accepted counter, the simulator gives no further public response; recognizing failure from its private row does not create an abort oracle. The interface has classical function tables, and privately caching their values supplies no extra public quantum measurement interface.

**PROVED (prefix cap).** Before the r-th instruction there are at most Q_q adversarial row calls and r-1 previous private full-row reads, so

    Qhat_r <= Q_q+r-1.

Repeated messages cause no instruction and no new row read because the cached value is unchanged. A final verification is after all instructions and cannot contribute to Qhat_r of an earlier instruction. Adversarial local verification is already in Q_q. Unused instructions can be padded after termination without exposing any response or changing the output bit; their entropy remains the complement-size entropy.

**PROVED / CITED (primary loss).** The checked primary AR theorem gives the contract consequence

    delta_ROW(q,Q_q)
      <= min(1, sum_{r=1}^q [ sqrt((Q_q+r-1)/(M-r+1))
                              +(Q_q+r-1)/(2(M-r+1)) ]).

This is a distance between the unmodified-row MC-IO game and the fresh-row comparison. It uses finite sets, fresh full row images, adaptive uniform available namespaces and all preceding helper queries. Reprogramming an already externally fixed U with a point-mass instruction would not have this entropy. Its placement must instead be reordered within the atomic call so that the sampler selects U before the common inner assignment, as in the first-call proof. Exact multi-call equivalence of that reordering is an independent-review obligation.

## 4. Latent first-zero coordinates and completion

**PROVED (row disintegration).** Independently sample q latent route vectors X_i uniform on [B]x[t]^17, B=2^41,t=512. For each row independently sample its omitted-coordinate sequence and first accepted counter or failure; on success set the accepted route coordinates to X_i and sample all rejected/later other coordinates independently. On failure all omitted coordinates are nonzero and X_i is unused. Full unused hash bits and tails are sampled consistently. Each row has exactly the iid full-word marginal, with failure probability(511/512)^(2^32). The X_i remain independent of failure and each other.

**PROVED (padding exposures).** A new label consumes one row/latent X. Repetition consumes none. Atomic completion may fail after route selection and may depend on X via the WOTS metadata at that route. Actual publicly exposed sets are subsets of the q padded latent exposures, so adding every X_i only increases coverage. No uniformity or independence is asserted for the subset of completed signatures after conditioning on completion. Retaining failed rows as nonwinning requires no extra always-success loss or global canonical-counter existence premise.

## 5. Final fresh message and old namespace

**PROVED under MC-IO (old assignments excluded).** Let m* be fresh and R*,c* arbitrary. Its inner point I(R*,m*) cannot equal a signed-message inner assignment by message framing. The final U* comes from the base inner restriction, not a previously signed assignment. If U* has lower half S, eligible outer reduction does not apply. If U* equals any previously used namespace, an old row could be used. Both must be separate extraction events rather than silently declared impossible.

**PROVED candidate target-search reduction.** Pre-sample all q distinct eligible latent namespaces T. They are independent of the base inner function. Give T and independent outside tables/maps to a stronger helper, and simulate public assigned inner points by their known values. At a fresh final message, the selected point is not an override. The base full256 image is bad when it belongs to T or has lower half S. These image sets are disjoint, with exact marked probability

    lambda_I = (N+q)/2^256 = 2^-128+q*2^-256.

Conditional on T, base-inner marked bits are iid. Split full images into uniform marked/unmarked sets and use the one-Boolean-query full-word simulation from the already derived graph search lane. All outside functions and override data are independent of that mark table. The final raw I point is computable from the adversary's classical output before evaluating its mark; HRS average search therefore suggests

    delta_final_namespace <= min(1,8 lambda_I (Q_q+1)^2).

This is a candidate application of the already checked iid average-search theorem and requires a separate reader to validate the simulation/extraction. Counting a separate selected final evaluation as an internal query would give the weaker but safe(Q_q+2)^2 variant. The q namespaces include unused padded ones; this only strengthens the bad event. Source free operations in the fresh-row MC-IO game do not evaluate base-inner residuals.

## 6. Candidate quantum coverage event

**PROVED (realized coverage density).** For the padded X transcript let C_bj be exposed indices in bucketb, real treej. A raw digest covers it iff its omitted digit is0 and every chosen real index is in its bucket's sets. Its density is

    lambda_X = [1/(B*t)] sum_b product_{j=1}^{17} (|C_bj|/t).

Independent q latent X draws imply

    E lambda_X = p_F(q)
      = (1/t) E[(1-(1-1/t)^L)^17], L~Binomial(q,1/B).

The forced omitted coordinate is retained. This is a realized full-transcript quantity, not a best-bucket average or a fresh digest conditional on successful verification.

**PROVED candidate search game.** Conditional on all X_i, namespace T_i, complete fresh row images W_i and outside functions/maps, the base eligible-E words remain iid full256. Define their Boolean mark by coverage of the padded transcript. Each mark is iid with probabilitylambda_X. Full-word images can be independently split into marked/unmarked samplers and simulated with one Boolean query per coherent raw call. Before a future T_i activates, its base word is used; after activation, the known W_i row is returned locally. Giving all latent advice early does not merge these two histories or overwrite a base response in the helper. The helper uses dynamic override bookkeeping matching the comparison game. It does not give full secret-graph advice to a hidden-value game.

If final U* is eligible and outside every padded namespace, its current E point is a base point, so actual covered-route success implies a mark at the computed outputx*=(U*,c*). The helper computes U* using known outside/base-inner data and source overrides; this requires no coverage-mark query. The average-search theorem thus suggests

    Pr[covered route and final namespace good]
      <= min(1,8(Q_q+1)^2 E lambda_X)
      = min(1,8(Q_q+1)^2 p_F(q)).

This is a quantum search reduction, not a classical(Q_H+1) candidate stream, and no classical padding argument is used. Honest row words are already fresh independent advice in this comparison and require no base-Boolean queries here. Their one read per new label was paid in the preceding ROW AR comparison, a different game.

## 7. Candidate source-contract ledger and outstanding gates

**PROVED conditional combination, pending the marked-query gates.** If the source masked-IO contract and both proposed marked-search projections are validated, a sufficient conditional coverage-route bound is

    epsilon_C <= min(1,
       q/2^128 + binom(q,2)/(2^256-2^128)
       +delta_ROW(q,Q_q)
       +8(2^-128+q*2^-256)(Q_q+1)^2
       +8(Q_q+1)^2 p_F(q)).

The ordinary HJ bound additionally pays the independently established masked-IO distance and any separately counted zero-seed event; these are not set to zero. No full QROM signature total is claimed. All entries remain candidate contract bounds until reviews identify exactly which projections are valid.

**OPEN smallest gates.** Establish/check MC-IO on the same HJ probability space; prove the atomic reordering for all new labels and without-replacement coupling; validate the two Boolean full-word/extraction simulations including free source information; bind all Qhat/read counts to the helper; and compose with the other QROM events. The first-call packet remains immutable. This save precedes reading the root draft.

**Status: INDEPENDENT_MULTICALL_CONTRACT_AND_CANDIDATE_SEARCH_PROJECTIONS_SAVED.**
