# Adaptive coverage bridge: scope and results

**PROVED — model progress.** The extension closes the exact identity E[p(T)]=p_fixed(q), a late-phase adaptive fresh-query bound, and an arbitrary-scheduling/early-stopping bound in a precisely defined two-independent-stream model. The last result includes a candidate queried early and retained until a later exposure covers it. It does not require testing coverage only at the candidate's query time.

**OPEN — actual signer.** No source-bound Bad-event probability or complete LULA I security bound is supplied. The actual reference signer must be coupled to the fresh-stream model with explicit treatment of prequeried points, shared input languages, fresh-message R/inner hashes, deliberate repeat queries and finite first-acceptance searches. Existing proof packet, source, manuscript and earlier results were not changed. No peer's new proof was read, and no earlier numeric input/output was reused before or after the new derivation.

## Exact checks

**COMPUTED.** `python -I -B coverage_checks.py` completed with exit code 0 using the standard library. The small coverage model has B=2 instances, t=2 leaves, K=2 real trees, q=2 exposures and M=2 raw candidate draws.

| Quantity | Exact rational | Decimal |
|---|---:|---:|
| E[p(T)] | 17/128 | 0.1328125 |
| E[1-(1-p(T))^2] | 503/2048 | 0.24560546875 |
| Jensen bound 1-(1-E[p(T)])^2 | 4063/16384 | 0.24798583984375 |
| Union bound 2 E[p(T)] | 17/64 | 0.265625 |

**COMPUTED.** Four independently arranged expectation calculations agree exactly: complete exposure-transcript enumeration, coverage-state dynamic programming with integer multiplicities, binomial occupancy, and finite alternating moments. The late-phase probability agrees between a direct enumeration of all 16,384 exposure/candidate assignments and the coverage-state dynamic program. Direct enumeration checks candidate filtering and coverage membership rather than assuming the probability formula.

**COMPUTED.** Exhaustively checking 65,536 length-four raw counter streams verifies the first-accepted-counter/accepted-tuple factorization. The failure probability is 1/16 and the accepted tuple is uniform conditional on success. This is a toy counter search, not a full counter loop in the real implementation.

## Discriminating failures outside the model

**COMPUTED.** With q=1 and L=2 exposure previews, selecting a matching exposure after seeing a candidate has success 15/128, versus the independent-exposure value 1/16. The final exposure is selected rather than independently drawn. The previews have a resource cost; this does not refute a bound that correctly charges every such oracle opportunity.

**COMPUTED.** A stronger countermodel sets the honest exposure X to the tuple of a previously queried raw candidate Y. X still has a uniform marginal distribution; E[p(T)] is still exactly 1/16. But the correlated candidate is covered with probability 1/2, eight times that expectation. Thus merely reproducing the binomial marginal occupancy model does not justify a bound for the joint adaptive experiment. This is an oracle-point-reuse control, not a construction of a fresh-message forgery against LULA I.

## Bounded Monte Carlo checks

**COMPUTED.** The fixed seed is 20261013017. Each model uses 30,000 trials. The confidence intervals below are individual 99.9% Wilson intervals; no simultaneous-confidence or cryptographic-security interpretation is assigned.

| Model | Successes | Observed probability | Exact probability | 99.9% interval |
|---|---:|---:|---:|---|
| Independent late-phase search | 7,246 | 0.2415333333 | 503/2048 | [0.2334961874, 0.2497569829] |
| Adaptively interleaved independent streams | 7,246 | 0.2415333333 | 503/2048 | [0.2334961874, 0.2497569829] |
| Preview-selected exposure | 3,525 | 0.1175 | 15/128 | [0.1115199486, 0.1237560547] |
| Correlated reused point | 15,133 | 0.5044333333 | 1/2 | [0.4949348883, 0.5139285794] |

**COMPUTED.** The interleaved and late-phase experiments use the same presampled independent streams. Their coverage-success flags agree on every trial, not just in their totals. Adaptive input/reveal order and early success stopping are exercised; 3,684 successful trials stop before consuming both padded budgets. The code keeps earlier candidates and retests them when coverage grows. These controls discriminate scheduling from output dependence without invoking any real signing API.

## Conditional bound ready for source-level integration

**PROVED under stated premises.** If the source-bound simulator couples its coverage route to independent fresh streams until a charged bad event, with at most q exposure draws and Q_outer raw adversarial outer-digest draws, then

    P(covered-leaf route) <= P(Bad)
                         + min(1,(Q_outer+1)*p_fixed(q)).

The extra one covers a fresh final verification input not previously queried. The ideal padding experiment is unconditional; do not condition on avoiding Bad and assume its distribution remains iid. The bound concerns the covered-leaf route only. Other component attacks still require extraction and separate reductions.

**PROVED conditional counter-search component.** Fresh independent counter outputs give no-success probability at most 2^(-2^23) for C=2^32, t=512. Across at most 2^40 new messages this is at most 2^(-8388568), a conservative analytic bound. The source has no explicit exhaustion-return contract; the fresh-output premise and source interface remain obligations.

**Smallest remaining lemma:** implement and prove the actual shared-oracle simulator's good-prefix coupling, classify every old/prequeried point in fresh-message verification, and provide a concrete Pr(Bad) bound covering input overlap, secret-R/inner-point prequeries and collision/exhaustion events. The isolated combinatorial scheduling step no longer needs to remain OPEN once these premises are supplied.

**Outcome:** MODEL_ADAPTIVE_COVERAGE_BRIDGE_PROVED; SOURCE_BOUND_BRIDGE_OPEN; FULL_EUF_CMA_NOT_ESTABLISHED.
