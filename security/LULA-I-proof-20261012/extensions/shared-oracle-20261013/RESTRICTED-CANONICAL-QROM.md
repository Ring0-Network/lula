# Restricted canonical collection in the linked full random oracle

**PROVED — independently reviewed manual component theorem.** This successor concerns the source-specific linked-global-RO canonical-row experiment, not arbitrary collection adversaries, fixed SHA-256, or the whole signature scheme. The source hash is ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. Both independent two-query first derivations remain immutable; the one-query circuit is a separately reviewed improvement. No existing complete probability calculator is changed.

## 1. Experiment and factorization

**PROVED — definition.** Sample one full256 static byte-string RO O, uniform P16, and independent ideal private maps F/J. Choose a valid target type7 address before its child C. Before registration only classical type0–4 collection queries under hidden P and F computations are allowed: no pretarget Raw or type7 call. Register C16. Search the SAME O on P||zero48||A7||C||BE32(c), c<2^32, in increasing order, retaining first accepted counter and fullY, or bottom. Release P. The source adversary's pre-key/fullRaw phase then runs with P/pk still withheld until normal source key release. Quantum memory persists. The outcome remains unconditional, including bottom branches.

**PROVED — fresh restriction.** First condition on P, address, F/J and the outside type0–4 data that determine C. These data never inspect the selected type7 coordinates. C is therefore fixed without reading them. Condition additionally on all full values in the SAME-C counter row, including rejected counters, acceptedY and later counters. The disjoint region

`D={P||zero48||A7||V16||BE32(c): V!=C}`

remains an independent product of uniform full256 words, pointwise for each positive-probability side-data value. Do not condition on A's queried state, a no-hit event or source success. On bottom branches the collision event is zero; no 1/tau normalization occurs. Target completion has mass tau_kind=1-(1-p_kind)^(2^32), where p_kind is the exact accepted128-prefix fraction for the lower/top predicate.

**PROVED — pre-key ordering.** In each fixed O,P,F/J block, hidden child/target preparation acts on reduction-private registers and A's pre-key computation acts on disjoint A registers through the same read-only O. They commute, preserving the JOINT cq state and private flags. This is not a marginal-uniformity or no-hit argument. Precomputing a key-only selected target does not depend on a message selected by A.

## 2. Exact one-query full-output simulation

**PROVED.** For each changed payload x=(V,c), sample an independent Bernoulli f(x) with probability1/N, N=2^128. Independently sample full256 hit/miss completion values having target prefix y or a prefix different from y. Their f-selected mixture is exactly uniform full256. Same-child, outside and malformed responses are the fixed side functions, preserving all literal aliases. Dummy Bernoulli coordinates for V=C keep the full160-bit search domain; they are ineligible outputs.

**PROVED — circuit identity.** For known f-independent replies r0(x),r1(x), Delta=r0 xor r1, response Fourier variable z and d=<z,Delta>, compute d into scratch0, Hadamard scratch, query ordinary U_f once, Hadamard scratch and uncompute d. Apply known phase (-1)^<z,r0> and invert the response Fourier transform. The accumulated phase is the character of r0 xor f Delta; the complete XOR response is exact and scratch resets0. On outside branches r0=r1 and scratch is |+>, so the same UNCONDITIONAL query is ineffective. There is no controlled-oracle assumption, history measurement or discarded lower limb. Linearity preserves any entangled reference. ONE-QUERY-COMPLETION.md supplies the complete program and general amplitude proof.

**CITED.** SPHINCS+C, https://eprint.iacr.org/2022/778, Appendix E Theorem E.3 (printed page35), bounds k-query Bernoulli-lambda search by8 lambda(k+1)^2. Applying it to the circuit above gives

`Pr[changed-base target collision] <= tau_kind * U(M), U(M)=min(1,8*(M+1)^2/N)`.

**PROVED.** Independent completion/side tables may be enormous; arbitrary known interquery gates/advice are allowed by this query upper bound. Their gate/initialization/storage costs are not declared efficient or free for an implementation. The conservative original two-query identity remains a valid weaker result, but does not forbid this different one-query circuit.

## 3. Source extraction and query budget

**PROVED.** For P!=0, honest source calls do not inspect D: addressed types0–4 differ in the address type; every honest call at the selected type7 tweak uses its genuine C; other addresses differ; H_msg's inner frame can equal a106-byte selected word only if its public seed P equals the zero block; its outer frame has52 bytes. Ideal F/J contribute no Raw calls. All these honest computations remain charged to source runtime and global evaluation resources.

**PROVED — NEW extractor.** Q counts all adversarial Raw calls, classical and coherent, across pre-key and later phases. The new extractor executes the genuine source until final verification reaches the selected exposed row and has computed a candidate V!=C,c, then outputs that classical candidate BEFORE the selected digest query. It does not first recognize full acceptance or collision. Every source Win&D7_base_final branch yields a marked output; additional branches only enlarge search success. Thus M<=Q. The preserved final-evaluation adapter has M<=Q+1, with bound U(Q+1)=min(1,8*(Q+2)^2/N); its count is not silently changed.

**PROVED / COMPUTED.** The two fixed predicates require lower42-bit and top21-bit selectors. An unconditional source component consequence is

`Pr_HJ[Win AND D7_base_final AND S!=0] <= min(1,(1-1/N)*(2^42*tau4+2^21*tau8)*U(Q))`.

Dropping eta or tau yields a looser valid bound. Seed-zero is paid once in any complete union, not again inside both predicates. The source events retain exposed successful rows, final acceptance and changed base. A selected failed row cannot supply that event. This uses the linked RO experiment HJ[O]; it is distinct from the conditional fixed-public-hash assumption-parametric component.

**COMPUTED / PROVED — work accounting.** Child preprocessing is at most17,392 public calls and8,704 F labels (upper:15,423/1,024). Challenge target preprocessing is at most2^32 full evaluations. A coarse total logical public-work envelope is Q+H_setup+qH_mode+3224+17392+2^32, with target/challenger/source work explicitly distinguished. M measures only unknown Boolean mark accesses, not that complete runtime. The prefix before the selected final digest needs no unknown marked-region query. Whole storage includes source/A/private dictionaries and any known completion tables.

## 4. Review, controls and open obligations

**PROVED / COMPUTED.** Independent first arguments 74d25d6b and44dcb6ac were saved before peer exchange. Their reciprocal review and a third source/primary-based review accept factorization, source exclusions and both extraction resource cases. Two reviewers separately accept root's one-query improvement. Root exact Q(sqrt2) controls checked1,024 worlds and8,192 clean basis states; an independent mixed-region3-bit reply control covers256 worlds,8,192 basis and256 coherent test states. These supplement the manual proof, not a checked whole-source QROM theorem. A terminated larger optional control is not counted as evidence.

**OPEN.** The accepted bound is a restricted ideal-function component; no quantitative theorem for arbitrary pretarget Raw collection adversaries or actual SHA-256 is imported. It does not replace the stronger already reviewed direct D7 model bound, change the complete numeric tables, certify category/capacity, or establish an efficiently represented full completion table. Ordinary private and fixed-h public graph/message-hash security remain separate. New kernel declarations: zero.
