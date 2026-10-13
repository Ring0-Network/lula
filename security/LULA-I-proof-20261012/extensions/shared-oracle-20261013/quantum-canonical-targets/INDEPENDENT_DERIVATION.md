# Quantum first-accepted canonical-target event

**Independent new-obligation derivation.** Saved before opening any canonical-target author report for this quantum obligation. This lane uses my earlier independently derived classical row idea and reviewed Boolean simulation, but reconstructs their composition directly from the pinned source. It does not claim blindness to my own preceding work. No other new proof for this obligation has been read.

**Scope:** a manual information-theoretic quantum-public-oracle event bound, with classical honest signing and a classical final verifier. It is not a complete QROM signature bound, an efficient reduction or a guarantee about fixed SHA-256.

## 1. Source and primary theorem checked anew

Pinned release `code/lula1/src/lib.rs` SHA-256 is `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Direct reads confirmed `digest`/`digits`/`accept`/`grind` at 216–235, child graph construction at 479–495, and final type-7 verification at 719–727.

The [primary ePrint 2022/346](https://eprint.iacr.org/2022/346), Hülsing–Kudinov, was checked online and in the existing cached PDF of SHA-256 `80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3`. Physical page23, Definition9/Theorem4, bounds finding an output marked input in an iid Bernoulli Boolean oracle by

```
Succ <= 8 lambda (Q_B+1)^2.
```

This is an output-search theorem, not a statement about ever touching a marked point in a superposition. No complete SPHINCS+ theorem is imported.

## 2. Fixed graph, rows and exact conditional sampler

For each valid encoded WOTS address A in the selected parameter set, the honest child V_A is fixed by the private maps and types0–6 graph. Chain public keys and Merkle/FORS roots do not use type7 counter outputs. The operational cache may be built alongside counters, but its root values are functions of the other hash restrictions. Honest caches must remain consistent. Seeds and parameters are fixed independently of type7 outputs.

The complete raw type7 input is

```
X_A(V,c) = S16 || zero48 || Addr22(A,type7,w2=0,w3=0)
           || V16 || BE32(c).
```

It is106bytes and injective in the actual compressed address/V/c. The selected five layer numbers fit the one-byte address field. The digest is the first128 bits of the full256-bit image. Widths4/8 consume all128 bits, so equal full digit vectors are equal digest slices. The selected acceptance sets T_A enforce the fixed sum, with no omitted WOTS digits.

Let M=2^128, C=2^32 and p_A=|T_A|/M. For the fixed-child row c in[0,C), the first accepted counter is c_A and its digest slice is y_A. Record bottom for a failed row. Conditional on the graph, rows at different addresses are independent even if children coincide.

An exact sampler first picks the row state:

- Failure with probability `(1-p_A)^C`; every same-child counter slice is then iid uniform outside T_A, and there is no target.
- Success at c_A=j with probability `(1-p_A)^j p_A`; y_A is uniform in T_A independently of j. Earlier same-child slices are iid uniform outside T_A; the canonical slice is y_A; later same-child and every other-child slice are iid uniform on all M values.
- At every raw point, append an independent uniform128-bit full-image suffix. Repeated raw queries reuse full images.

For a successful fixed row table the probability is

```
[(1-p)^j p] / |T| / (M-|T|)^j / M^(C-j-1) = M^-C.
```

For a failed table it is `(1-p)^C/(M-|T|)^C=M^-C`. Thus the complete row has exactly its original random-oracle marginal. Degenerate p=0/1 use the corresponding forced branch. There is no renormalization that silently deletes failed rows.

## 3. Bernoulli factorization after exposing all targets

Let Sigma include keys, the full graph outside type7, every row state `(V_A,c_A,y_A)` or bottom, full canonical images, and the conditioned rejected-row/prefix function values. This is a conceptual information extension; it may be huge. Grant Sigma and all other outside **function tables** at the beginning, rather than conditioning on adaptive query logs. Initial disclosure can only enlarge the adversary's information.

Define eligibility e(x) for a successful A row and a noncanonical payload as follows:

```
e(X_A(V,c)) = 1 iff row A succeeds and
    [V != V_A or (V=V_A and c>c_A)].
```

Canonical points and earlier same-child counters have e=0. The latter cannot match accepted y_A because their slices are rejected. Failed fixed-child rows have no target. Points of other unused/invalid addresses likewise are ineligible. Thus this eligibility definition contains every possible same-address noncanonical target hit in the conditioned row model.

For every word of a finite injectively length-encoded raw-query register, independently sample B(x)~Bernoulli(1/M), including words whose marks will be ignored. For eligible x, independently sample full images

```
V1(x)=y_A || uniform128 suffix,
V0(x)=uniform256 image with first128 bits != y_A.
O_B(x)=V_{B(x)}(x).
```

For ineligible words use the correct fixed/conditioned/outside image and ignore B(x). All pair tables, Sigma and outside function tables are independent of B in this sampler. The mixture is uniform256 at every eligible point, preserving the exact conditional residual table, and the previous row calculation restores the unconditional original marginal.

This factorization does not assert independence of the canonical target from its earlier counters; those points are explicitly conditioned and masked. Nor does it assert that revealing arbitrary outside query logs preserves independence: their queried input names may encode residual images. Entire sampled functions/advice, independent of B, are the permitted data.

Because row success/failure is sampled into Sigma before B, conditioning on successful top-cache setup can also leave B iid. This is an exact completed-key conditional row experiment, not a casual survivor-posterior assertion. Its target-event inequality does not by itself justify conditioning other game hops or their transcripts in the same way.

## 4. Clean coherent simulation

For eligible x, put delta_x=V0(x) XOR V1(x), nonzero since the target prefixes differ. Choose a pivot j with delta_j=1. The reversible fanout `T(z)=z XOR z_j(delta XOR e_j)` is involutory and conjugates X_j^B into XOR by B delta. XOR V0 into the response, apply T, swap the pivot with a work qubit in |+>, call the ordinary Boolean XOR oracle once, swap back and undo T. The work returns exactly to |+>; its preparation can be undone.

On ineligible branches, do not swap: the Boolean call on |+> is identity. The entire construction works coherently over different x and masks, with no measurement, uncomputed mark garbage or free controlled-query assumption. It implements one full256 XOR oracle query using one Boolean query. A standard compute/control/uncompute alternative costs two queries.

The independent tables and transforms can be exponentially large but finite. Only query complexity is bounded. Efficient source/primitive simulation and challenge embedding remain open.

## 5. Adaptive exposure, prequeries and honest calls

The oracle and row sampler are fixed at time zero. Giving all canonical targets and failures early reproduces an information-enlarged version of their eventual adaptive exposure; the original adversary can ignore unused information. No post-query reprogramming or quantum query-history measurement is needed. Q includes all adversarial complete-hash quantum queries before key disclosure and afterward; repeated queries remain charged in the quantum query budget.

Classical honest signing/preparation uses same-child rejected counters and the canonical point only, hence depends on Sigma and outside tables, not B. A failed row prevents successful completion or causes the source's overflow behavior; the model does not invent an exhaustion-return API. Timing, interrupted retries and corrupted cache values are not extra free interfaces. Exposing in-flight residual type7 answers or signing an adversarially altered child would require additional mark-query accounting.

For nonzero S, message-inner and actual secret-prefix message-randomizer raw inputs have S at bytes16–31, whereas addressed type7 inputs have zeros there. Outer message strings are52bytes. Other addressed types differ literally. These separations let the other honest interfaces be simulated from outside functions. In a joint F/J ideal game, F/J are already separate maps; this event proof does not show that replacing actual private derivations by those maps is sound against quantum queries. A direct outside-function version may grant keys/type5–6 tables and use the graph's independence from type7, but that deliberately strong side information proves no hidden-secret unforgeability.

## 6. Observable event and bound

After classical adversary output, run the actual final verifier and record its type7 calls. Define E7 to mean that one call at successful row A has `(V,c)!=(V_A,c_A)` and returned slice y_A. Earlier same-child points cannot cause E7. Every remaining E7 point is eligible and has B(x)=1. A reduction knowing Sigma outputs the first such raw point as its classical marked search answer.

Final verification reaches at most d=5 type7 calls, one per layer; preceding graph hashes and two message hashes are outside the type7 event and use known independent functions. Their input values can depend adaptively on prior type7 answers, which is allowed oracle adaptivity. A rejected signature may stop earlier, and an ultimately invalid trace containing an E7 witness is still included. Canonical/repeated calls could be optimized, but counting all five is safe.

The one-query reduction has Q_B<=Q+5 and therefore

```
Pr(E7 | fixed nonzero S) <= min(1,8 (Q+6)^2 / 2^128).
```

The two-query fallback is `min(1,8[2(Q+5)+1]^2/2^128)`. For independently uniform S without successful-setup normalization, a conservative unconditional bound adds `2^-128` before capping at1. Sharing this seed-zero event with other hops requires a joint coupling.

The same inequality holds in the exact conditional completed-top-cache row experiment, because its conditioning is encoded in Sigma independent of B. It is not a signing-capacity or category1 certificate. It bounds equal canonical accepted digit evidence from changed V/c; unequal-digit chain routes, FORS coverage, node binding, secret inversion, private-map replacement and full QROM composition remain separate. It says nothing about a marked point merely having occurred in a query superposition.
