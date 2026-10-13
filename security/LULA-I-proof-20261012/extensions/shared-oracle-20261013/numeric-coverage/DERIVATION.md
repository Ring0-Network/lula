# Fresh-stream bridge for realized FORS coverage

Independent derivation saved before reading any other agent's new proof or reusing earlier numeric inputs. This document defines coverage experiments; none is a proof for the actual LULA I signer or a real forgery attack. Only this extension directory is written.

## 1. Transcript coverage and its expectation

**ASSUMED — exposure model.** There are B instance addresses, t leaves per real tree and K real trees. An exposure is X=(U,J_1,...,J_K), uniformly distributed on [B] x [t]^K. The q exposures are independent. An adversarial raw digest candidate is Y=(V,L_1,...,L_K,Z), uniformly distributed on [B] x [t]^(K+1), independently of the exposure transcript. Its omitted-coordinate filter is Z=0. There is no secret/tree associated with that omitted coordinate.

**PROVED — conditional exact counting.** For realized transcript T, define C_(b,j) as the set of exposed leaves at instance b in real tree j. A candidate is covered precisely when Z=0 and every L_j belongs to C_(V,j). Therefore

    p(T) = 1/(B*t) sum_b product_(j=1..K) |C_(b,j)|/t.

This is a deterministic function of T. It counts successful *coverage* of an independently sampled full digest. It does not certify that a corresponding complete signature can be forged.

**PROVED — exact expectation.** For a fixed instance b, its exposure count R has Binomial(q,1/B) distribution. Conditional on R=r, the K independent leaf-coordinate sequences are independent. The expected fraction covered in one real tree is 1-(1-1/t)^r. Hence

    E[p(T)] = 1/t E[(1-(1-1/t)^R)^K] =: p_fixed(q).

This is an equality for the stated exposure model, not an assertion that every realized transcript has coverage at most p_fixed. Symmetry over B buckets cancels the leading 1/B after expectation; a preselected target bucket still costs 1/B in each independent full-digest trial.

**PROVED — two exact arrangements.** One calculation sums p(T) over all q-tuples of exposures. Another conditions on occupancy R and sums its binomial law. The expectation can also be rearranged as

    p_fixed = 1/t sum_(j=0..K) (-1)^j binom(K,j)
                       (1-1/B+(1/B)(1-1/t)^j)^q.

The runnable check will independently implement exposure enumeration and occupancy expectation, with rational arithmetic for a small model.

## 2. Late-phase adaptive fresh queries

**ASSUMED — fresh-output interface.** After T is fixed, each distinct eligible query selected adaptively from the public history returns a new uniform Y independent of T and all previous fresh outputs. Eligibility concerns actual encoded oracle inputs, not just different source-level call labels. No prequeried output is classified as a fresh query.

**PROVED — exact late-phase search.** For a fixed budget M of eligible raw candidates, adaptive input names and stopping after success do not change fresh output distributions. A strategy that sees all M candidates and accepts any covered one has conditional probability

    P(success | T) = 1-(1-p(T))^M <= min(1,M*p(T)).

An arbitrary strategy that succeeds only when a candidate is covered has no greater probability. Taking expectation over independent honest exposures gives

    P(success) = E[1-(1-p(T))^M]
              <= 1-(1-p_fixed(q))^M <= min(1,M*p_fixed(q)).

The first inequality is Jensen's inequality for the concave function f(x)=1-(1-x)^M, M>=1. The second is the ordinary union bound. For M=0 all quantities are zero. These are model-conditional bounds; averaging p(T) alone is insufficient without the independence/freshness premise.

**PROVED — a previously unqueried final verification point.** If a purported forgery chooses an outer-hash input it never queried, the verifier's fresh evaluation is one further uniform opportunity. Upper bounding this route requires M+1 candidates rather than assuming every successful output was queried by the adversary. Whether the actual final point is fresh, an old honest point, or a shared-domain overlap is a source-bound classification obligation.

## 3. Extension to adaptive interleaving under a stronger interface

**ASSUMED — two independent streams.** Each new distinct-message signing exposure consumes the next value from an independent iid X stream. Each eligible adversarial fresh raw candidate consumes the next value from a separate iid Y stream. The adversary chooses when to request either stream, adaptively, and may stop early, but cannot preview X, direct its distribution, or cause either operation to reuse an already queried input from the other stream. At most q exposure draws and M candidate draws occur. Repeated signing messages add no new coverage and may be ignored.

**PROVED — padding/coupling lemma.** Presample q independent X values and M independent Y values. Any adaptive schedule reveals prefixes of these independent streams. Extend the actual exposure prefix to q values and the candidate prefix to M values. Coverage sets only grow when exposures are appended. Every actual covered candidate is therefore covered by the padded q-exposure transcript. This yields

    P(success under any such schedule) <= E[1-(1-p(T_q))^M]
                                      <= min(1,M*p_fixed(q)).

This closes adaptive *scheduling* of fresh independent exposures and candidates. It includes candidates retained until later exposures cover them, not only candidates tested against coverage at their query time. It does not close adaptively selected/prequeried exposure outputs or overlapping oracle inputs. A balanced or quiet host is irrelevant to these probabilistic premises.

**PROVED — why no postselection of the honest stream is allowed.** If the signer may choose, after seeing a candidate, one of L previously revealed uniform exposure vectors and expose a matching one, with q=1, coverage success is

    (1/t) * (1-(1-1/(B*t^K))^L),

provided the signer can choose any matching vector and the candidate's filter is independent. For L>1 this exceeds p_fixed(1)=1/(B*t^(K+1)). The final transcript is selected, not iid independent of the candidate. This toy counterexample disproves a q-only independence argument. It is NOT a violation of a fully accounted Q_H bound: the L preview queries must be charged to whichever oracle-resource model allows them.

## 4. First accepted counters and their limits

**ASSUMED — fresh independent raw counter outputs.** For one new signing message, let successive raw digests Y_c be independent uniform values, and accept the smallest c whose Z_c=0. Acceptance depends only on the omitted coordinate; the instance and K real leaf coordinates are disjoint from it.

**PROVED — no selection bias from fresh first acceptance.** Conditional on successful search within C counters, the accepted X is uniform on [B] x [t]^K and independent of the accepted counter number and all rejected prefix outputs. Explicitly,

    P(c_first=c, X=x) = (1-1/t)^c * (1/t) * 1/(B*t^K).

Summing c=0..C-1 gives failure probability (1-1/t)^C and preserves the accepted X's uniform law. Revealing rejected outputs after signing does not retrospectively change this factorization. Every rejected output fails Z=0 and therefore is not a valid coverage candidate in this model.

**PROVED — rejection-cost bookkeeping.** An adversary's raw candidates also must satisfy Z=0. Treating an already accepted candidate as one raw query and then multiplying by p_fixed improperly charges the filter twice or ignores the work spent rejecting other trials. Conditional on Z=0, the coverage probability is t*p(T); its query budget must separately include the raw trials. M in the preceding theorems counts RAW eligible outer-digest opportunities, including rejection trials.

**OPEN — exact LULA interface bridge.** The source returns R and the first accepted FORS counter. Before signature completion, a future outer input may have been publicly queried, may coincide with another internal call's input language, or may inherit an inner-hash collision. For repeated messages the input is deliberately old. A source-bound proof must classify those cases, couple the good case to the fresh streams, and bound the probability/resource cost of the bad cases. Merely checking that the last nine digest bits are zero does not establish this coupling. Finite 32-bit counter exhaustion must also be charged if a total signing interface is claimed.

**PROVED — conditional full-counter failure bound.** Under the fresh-counter premise, C=2^32 and t=512 give one search's no-success probability (1-1/t)^C <= exp(-C/t) <= 2^(-2^23). For at most 2^40 new signing messages, the union bound is at most 2^(-8388568). This is an exact conservative inequality in the model, not an empirical result or a statement that the Rust implementation aborts after exhausting counters. The unchecked source may loop after wrapping, and a checked build may panic. The failure event can be charged in a completion-based reduction only after the fresh-counter coupling is established.

## 5. Smallest remaining lemma and verdict

**OPEN — source-bound lemma needed.** Construct a simulator with a stopping bad event Bad such that, before Bad, every new signing-message accepted routing/leaf tuple and every eligible forged raw digest candidate can be coupled to the two independent streams; no old/prequeried or overlapping point is silently treated as fresh. Prove the actual forgery's covered-leaf route lies in the padded candidate event, with at most Q_outer+1 raw opportunities, and bound Pr(Bad) using the exact shared-oracle encodings, secret-R/inner-point guesses, collision events, and finite first-acceptance search. Under that lemma the coverage route would satisfy

    P(covered-leaf route) <= Pr(Bad)
                         + min(1,(Q_outer+1)*p_fixed(q)).

The inequality is conditional on the stated coupling, not a current theorem about the source. Other PRF, WOTS certification, tree extraction, message binding and quantum terms remain separate and OPEN. The progress here is an exact transcript-to-occupancy identity, exact late-phase bound, and an adaptive scheduling bridge in a specified fresh-stream model, with an explicit counterexample outside that model.

**PROVED — conditioning precaution.** The proof must use an unconditional joint coupling that agrees until Bad and charge the stopping bad event. Conditioning the entire transcript on 'Bad never occurs' and then asserting the streams remain iid is not justified: avoiding Bad can itself bias their joint distribution. The padding upper bound is applied to the unconditional ideal streams in the coupling, not to a retrospectively conditioned distribution.
