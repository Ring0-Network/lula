# Parameter-uniform classical joint ledger: independent root derivation

Status: candidate manual theorem; not promoted, not a successful parameter repair. Saved before reading the new independent parameter-uniform derivation. The source and historical fixed-parameter theorems are unchanged.

## 1. Explicit domain

**ASSUMED interface.** Use the exact atomic partial raw-RO source experiment of CLASSICAL-JOINT-RO-THEOREM.md: three independent 16-byte seeds, a full256-bit public raw oracle, classical public queries including pre-key queries, at most q initiated atomic signing requests, absorbing finite-counter noncompletion, strict final verification and honest canonical cache preparation/restoration only. Queries Q count adversarial raw evaluations; honest work is not silently part of Q. This is neither an unconditional SHA claim nor a full-Rust/compiler refinement.

Let n=16, FORS+C be enabled, r=k-1>=1, and let the layer sequence be `(h_i,lw_i,ell_i,S_i)` for i=0,...,d-1. The allowed interpretation keeps lw_i=4 on non-top layers and8 on the top. Choose integer heights with0<=h_i<=31, h=sum_i h_i<=63,1<=d<=256. Require1<=a<=31, r*2^a<=2^32, k*a+h<=256 and r<=94, with `z_i=128/lw_i-ell_i`,1<=ell_i<=128/lw_i. Require0<=S_i<ell_i*(2^lw_i-1). The final strict inequality is a proof guard, not merely a source representation guard. The fixed-source endpoint-only inference does not cover S_i=ell_i*(w_i-1). Keep omitted full-digest digits forced to zero. All required graph/address/buffer/index computations must obey the source integer representation; no unsigned wrap or address truncation is admitted.

The r<=94 bound is the actual tail-buffer requirement for FORS-root compression, not an abstract cryptographic assumption. Fixed lw4/8 and omitted-zero checks ensure accepted ell-tuples encode all128 digest bits. Every retained target has at least one accepted tuple; its row has finite 32-bit counters. Key/sign execution may nevertheless fail to complete and the same absorbing experiment is retained.

## 2. Source invariants that survive the parameter change

**PROVED algebraic/address candidates.** Write b_i=sum_(j<i)h_j and u_i=sum_(j>i)h_j. `tree_leaf` gives tree=floor(idx/2^(b_i+h_i)) and leaf=floor(idx/2^b_i) mod2^h_i. The complete `(layer,tree,leaf)` address therefore identifies one genuine child root, regardless of which external message reaches it. All signatures at that address select the same canonical digest vector. Repeated honest use is not distinct-child WOTS reuse. The layer byte distinguishes neighbouring zero-height layers as well. The height, FORS index and buffer guards above prevent accidental source-level truncation of these labels.

At nonzero public seed the raw private/inner/type geometry in the joint theorem does not depend on heights, r, a, ell or S: private frames still carry zero48, inner words their second block S, outer words have length52 and suffixS, and address type bytes still separate private5/6, public0..4 and7. Variable root-compression payload lengths do not remove the type separation of valid addressed frames. The safe graph remains a finite topological addressed graph. Genuine chain/leaf/public images can be retained while all hidden starts and interior values stay outside the granted surface. A type7 row still takes its child from other graph restrictions. The stopped joint coupling, forward-suffix exposure, atomic unsigned-J chronology and role weights1/3/2 therefore have the same construction, subject to proving this invariant package for the whole guarded domain rather than naming independent hash functions.

**PROVED witness arithmetic candidates.** Let t_i=ell_i*(w_i-1)-S_i, with w_i=2^lw_i. Every accepted vector forces exactly t_i verifier chain steps. Strict target gives t_i>=1; hence the old unexposed genuine-start case still has a nonterminal H opportunity. FORS reveals r secret starts and performs r(a+1) addressed public evaluations in final reconstruction. WOTS compression and Merkle paths add1+h_i public G evaluations per layer. Accordingly

    H_final = r + sum_i t_i,
    G_final = r*(a+1) + 1 + sum_i(t_i+1+h_i),
    D7_final = d,
    C = H_final + G_final + d + 3
      = r*(a+2) + 2*sum_i t_i + h + 2*d + 4.

The three additional constant charges are two final inner opportunities and the single averaged seed-zero charge. Honest inner/outer and overlapping public-slot charges remain2q and3Q; using expected candidate counts in coverage remains invalid.

## 3. Parameterized coverage and composition candidate

Define Z~Binomial(q,2^-h), beta=1-2^-a and

    pF(q;a,k,h)=2^-a * E[(1-beta^Z)^r].

**PROVED counting candidate.** The full256-bit output is partitioned into k*a FORS bits and h route bits; unused bits are ignored. The forced last coordinate consumes a zero-probability filter2^-a, not another secret tree. Distinct full inner labels provide independent counter streams in the ideal ghost. The same adaptive accepted-stream argument then uses route space2^h, r real trees and leaf space2^a, with deterministic candidate cap Q+1. The source pair/inner bridge still has full256-bit denominator N^2, N=2^128. Its coefficient does not become2^(k*a+h); that expression describes selected output bits, not the complete inner label. The FORS forced-coordinate finite-counter failure is bounded by q*beta^(2^32), without rounding it to zero. WOTS setup/signing noncompletion is part of the absorbing experiment, not a new promise of full runtime completion.

**OPEN pending independent full-domain verification.** The proposed complete uniform envelope is

    E_par(q,Q) = min(1,
      (3*Q+2*q+C)/N
      +(q*Q+q*(q-1)/2+q)/N^2
      +q*beta^(2^32)
      +(Q+1)*pF(q;a,k,h)).

It is derived by replaying the common joint construction with the above invariants, not by substituting parameters into an isolated historical numeric formula. Baseline r17,a9,h41,d5,t_lower240,t_top2040 gives H3017,G3217,C6242 exactly. An independent reader must confirm uniformity of the full safe-surface coupling, graph witness cover, selection law and finite representation guards before this becomes an accepted parameterized source theorem. Geometry-only cost alternatives are not security results.

## 4. What this could and could not resolve

**PROVED conditional on the proposed envelope.** For all allowed tuples, its nonnegative public-query fee gives E_par(q,N)=1. Thus this proof family cannot certify the literal tiny failure target at Q=2^128 by varying only the allowed tuple. Even after all other fees are dropped, its half-success certificate is limited by Q<=N/6. This is an obstruction to these sufficient certificates, not a lower bound on actual forgery probability, an actual attack, a universal parameter impossibility or an AES-normalized resource comparison.

**OPEN.** No tuple restoring the requested complete classical/category target, and no parameter-minimality ordering, is established. Candidate rankings by bytes or analytic signing cost must wait for a valid security feasibility predicate. The author-selected2^40 conditional use target is retained; no lower signing capacity is silently substituted.
