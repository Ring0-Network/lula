# Probabilistic review of the dependency-safe successor

**PASS_CONDITIONAL_PROBABILITY_AND_ABSTRACT_AMPLIFICATION; SOURCE_BINDING_OUTSIDE_AUDIT.** Reviewed only the probability laws, conditional assumptions, union bookkeeping and abstract query/amplification arithmetic in root-preimage-criterion/DEPENDENCY_SUCCESSOR.md, SHA256 `b403d39ccf66455acb6c5dc6776a98fdca397ec6e087ac80578d0049cd3b7249`.

My independent sampler/union/rotation derivation and exact controls were saved before opening that successor. No source-forgery implementation, signature/payload construction, real SHA search or protected edit was performed. This report does **not** validate its source-level forgery claim, query inventory or asserted absence of residual-H dependencies. A failed source review cannot be replaced by this mathematical acceptance.

## 1. Conditioned count law (§2)

Accepted **under the stated exact generative disintegration**. P* is selected outside residual H; its complete image Y is planted independently; all other complete images are iid uniform conditional on Sigma. The row has N distinct points and depends only on Sigma. Conditional on any positive-probability Sigma block, excluded P* gives Bin(N,1/N), included P* gives1+Bin(N-1,1/N). If membership is random, the unconditional distribution is a mixture rather than necessarily either single binomial law.

Both cases nevertheless give exactly

    Pr(M=1 | Sigma)=(1-1/N)^(N-1)>1/3.

The successor uses this correct shared singleton probability and does not require one unconditional binomial law. If T/A are Sigma-measurable as asserted, additionally conditioning on their true values cannot change it. Dependence of row choice on the designated Y is harmless; dependence on residual values is not. Full256 tails remain part of the function law. “No direct query” alone would be insufficient if purported outside information carried residual-derived data.

The exact sampler control enumerates68256 finite full-image worlds for N=2,3,4, checks36 conditional Sigma distributions, mixed membership, and singleton/Sigma-event factorization. A duplicate-row control invalidates binomial counting, and an outside-information control with residual-derived match bits gives singleton probability3/8 rather than1/2. These delimit the hypothesis rather than auditing a source construction.

## 2. Prerequisite bookkeeping (§1)

Accepted given the two **unconditioned, same-space** marginal estimates. From Pr(T)>31/32 and Pr(A)>31/32, only Pr(T and A)>15/16 is universally guaranteed. The successor correctly avoids the unjustified product. Its latent continuation is an explicit modelling hypothesis whose source correctness is not established here.

The stagewise A estimate additionally requires conditional row-blindness at each reached stage. The T product requires its declared independent top-row law. Under these hypotheses, the primitive uniform-digit target-sum probabilities exceed1/1024: exact inclusion-exclusion and an independently arranged sliding-window DP agree for(32,16,240) and(16,256,2040). This proves combinatorial probabilities for independent uniform digits; it does not prove that any actual selected source row has that law.

With L=2^20,C=2^32, the coarse failure bounds6exp(-L/1024) and2^21 exp(-C/1024) are both less than1/32. Thus the displayed tail inequalities are arithmetically sufficient, conditional on the row assumptions. Neither A/T independence nor successful-setup normalization is needed.

In §3, multiplying the joint prerequisite probability by1/3 is justified **only because** T/A and the chosen row are asserted Sigma-measurable in §2 and the singleton probability is constant conditional on Sigma. The subsequent amplification bound is uniform across those singleton blocks. If the measurability/source-disjointness assertion fails, the successor's precise chain-rule route is unvalidated; general union accounting alone would give a different lower bound. This review does not turn that assertion into a source fact.

## 3. Abstract amplification and arithmetic (§3)

Accepted under the abstract accessible-row/full-output-XOR interface. A compute/compare/uncompute marked phase costs two function queries, restores the complete scratch image, and is followed by a query-free uniform reflection. For one marked row index, success after t phases is sin²((2t+1)asin(1/sqrt(N))). The exact finite reflection control agrees with that identity; it also distinguishes whether a final classical check is charged.

The successor explicitly includes a final check and verifier overhead. Its given ledger sums to

    B=6*2^20+3217+1+3224=6297898,
    t=floor((2^64-B)/2),
    B+2t=2^64.

The constituent **source** counts3217/3224 and row-circuit availability are treated as supplied assumptions, not validated here. Their arithmetic is exact. Let s=2^64. Since20(B-1)<s, the singleton angle exceeds19/20. It is at most(s+1)asin(1/s)<=pi/2. The elementary Taylor lower bound gives

    sin(19/20)>=19/20-(19/20)^3/6=38741/48000>4/5.

Hence the squared success is strictly greater than16/25. This analytic argument establishes the inequality independently of a floating-point sine value. The large-budget numerical value merely corroborates it; it is no practical-runtime claim.

## 4. Retained constant and decision

The three conditional factors give exactly

    (15/16)*(1/3)*(16/25)=1/5.

Strict premise bounds make the final **abstract experiment** lower bound strict. The former961/4800 constant uses(31/32)^2 for the joint prerequisite factor and is not licensed by marginal estimates alone. The successor expressly leaves it historical/unpromoted, which is correct.

The probability/AA arithmetic passes. No ordinary source-model forgery theorem, concrete attack, category interpretation, runtime claim or implementation exploit is certified by this lane. Source-to-abstract binding, raw-domain exclusions, latent extension faithfulness and actual row-circuit/query inventory are **OUTSIDE THIS AUDIT** and remain separate source-review obligations.

Reproduce `python -I -B control.py` and `python -I -B check_successor.py`; both exited0. SUCCESSOR-CHECK.json records assumptions, exact budget/Taylor/factor checks and the explicit source-binding exclusion. No source/master/manuscript/peer artifact was modified.

**Outcome: PASS_CONDITIONAL_PROBABILITY_AND_ABSTRACT_AMPLIFICATION; SOURCE_BINDING_OUTSIDE_AUDIT.**
