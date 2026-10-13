# Independent component derivation (saved before peer reports)

Author: independent numeric checker. Scope: original implementation and original model scripts, not the first proof or another agent's derivation. Every result below is component-scoped; a complete EUF-CMA reduction is OPEN.

## FORS coverage

**PROVED (idealized fixed-instance distribution).** Let B=2^h, t=2^a and K=k-1. Under independent uniform honest instance selection and independent uniform leaf selections within each real tree, the occupancy of an independently selected target instance is R~Binomial(q,1/B). Its average coverage of an independent digest is

    p_fixed(q) = t^-1 E[(1-(1-t^-1)^R)^K].

The leading t^-1 is the public forced-zero digest filter. The code builds only K real trees. There is no last-tree secret or authentication path; therefore the instruction that a signature 'reveals leaf 0 of the last tree' is false for this implementation. Filtering the last digest coordinate to zero is the actual mechanism.

**PROVED (finite exact moment identity).** Expanding the K-th power gives

    p_fixed = t^-1 sum(j=0..K) (-1)^j binom(K,j) (1-p+p(1-t^-1)^j)^q,

where p=1/B. Its Poisson analogue replaces the final factor by exp(mu*((1-t^-1)^j-1)), mu=q/B. These are independently implemented alongside positive occupancy summation. Finite precision stability is checked at two precisions. The positive sum's omitted mass is upper-bounded by a Chernoff tail, not silently discarded. For huge occupancy, concentration and coverage bounds give a tight saturation interval without millions of iterations.

**OPEN (adaptive EUF upper bound).** This is a fixed random-instance average, not automatically the best adaptive adversary's success probability. Actual signed transcripts expose covered sets C_(b,j); after a transcript, a uniformly sampled full digest has exact conditional success

    p_T = 1/(B*t) sum_b product(j=1..K) |C_(b,j)|/t.

An average over independent honest transcripts recovers p_fixed. Adaptive message selection, public prequeries, selective signing, chosen forged R and ctr, and full hash-query budget need a reduction controlling p_T and transcript dependence. Multiplying an *unconditional average* by Q_H without that argument does not supply it. Targeting a particular preselected bucket must pay probability 1/B per full-digest trial; best-bucket statistics and average-bucket statistics must not be conflated.

**PROVED (budget arithmetic only).** If a conditional per-query upper bound p applies, the classical union bound is min(1,Q_H*p), and its advantage exponent is max(0,-log2(p)-log2(Q_H)). A 132.6-bit *work factor* does not give advantage 2^-128 after 2^128 queries; the resulting FORS component exponent is approximately 4.6 bits. To demand advantage <=2^-128 with that query budget requires p<=2^-256. No such claim follows here.

## Target-sum encodings

**PROVED.** For x,y in [0,w-1]^ell with sum x=sum y=S, y>=x coordinatewise implies x=y. Forward evaluation alone after one signature reaches one point on this slice.

**PROVED.** Given signature positions x^(1),...,x^(j), set m_i=min_t x_i^(t), and put D=S-sum m_i, u_i=w-1-m_i. The inclusive number of reachable accepted encodings is the coefficient

    N(m) = [z^D] product_i (1+z+...+z^u_i)
         = sum_(J subset coordinates) (-1)^|J| binom(D-sum_(i in J)(u_i+1)+ell-1,ell-1),

with terms of negative remaining degree zero. A prefix-sum integer DP computes the same coefficient in O(ell*D) operations. Subtract only the number of DISTINCT observed vectors if reporting a distinct-encoding statistic. Inclusive coverage per raw encoding hash is N(m)/w^ell; conditional slice coverage is N(m)/|slice|. For LULA I both digest widths are 128 bits. After one encoding, N=1 and inclusive success is 2^-128. It is not zero: a fresh message/counter input may hash to the same encoding. Antichain reasoning alone does not prove EUF-CMA.

**PROVED (reference code, semantic invariant).** A full WOTS address is (layer,tree,leaf), not the leaf index alone. At layer zero it always signs the public key of the same FORS instance (independent of the chosen revealed FORS leaves). At every higher layer it always signs the root of the uniquely addressed child subtree. Each reference counter is the first accepted counter for that fixed child value; repeated reference use reveals the same digest vector. Thus every reference WOTS address sees at most ONE distinct signed child value and ONE distinct encoding, regardless of q. Honest occupancy does not create the two-different-message reuse described in the requested formula. Corruption that substitutes another accepted counter is a separate adversarial cache model, not reference signing.

**OPEN.** Reachability counting is not a reduction for inversion, alternative chain values, endpoint compression collisions, or arbitrary roots. Those need separate chain and tree lemmas with oracle budgets. The objective's product 'probability some leaf reused * two-signature forgeability' is not a justified security term and its per-layer local 2^h' occupancy ignores the tree coordinate.

## Address inventories

**COMPUTED (not a security loss theorem).** Let below_i=sum_(j<i)h_j and above_i=41-below_i-h_i. Layer i has 2^above_i subtrees, 2^(41-below_i) WOTS key addresses, and 2^above_i*(2^(h_i+1)-1) Merkle node positions including WOTS public-key leaves. These counts distinguish total universe, signer touched addresses, and adversary oracle queries. Cache and grind work are not bounded by the number of secret derivations; grind loops may test many counters and finite u32 overflow behavior requires an explicit failure convention.

## Verdict

FORS fixed-instance component: COMPUTED under stated idealized distribution. Target-sum counts and semantic one-message-per-reference-address invariant: PROVED / COMPUTED. Total EUF-CMA bound and signing limit: **not established**. No number for total security, quantum reduction, or cache transfer premise is inferred from component work factors. Toy Monte Carlo checks coverage/counting models only, not a full EUF oracle experiment or an attack on real SHRINCS.
