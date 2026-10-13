# Restricted global-RO canonical collection: independent first derivation

Saved before reading any new peer quantitative proposal. This is a manual finite-query QROM component lemma, not fixed-SHA hardness, a checked source theorem, or a complete signature-security statement. Existing receipts, source, scalar calculators and manuscript are unchanged.

## 1. Precisely restricted experiment

One global full256 random function O on bounded literal byte strings is sampled; ideal private F/J are independently sampled. The hidden parameter P is uniform128 bits. Fix a valid target type7 address A7 before the target child. Before registration, only classical type0--4 collection calls under P and independent ideal F are permitted; there is NO pre-target adversarial Raw call. Compute the genuine child C16 with the source child_value cone. Register that C and A7. Read the SAME O at words P||zero48||A7||C||BE32(c), c=0,...,2^32-1, until the first accepted128-prefix is found, retaining the full256 target Y; otherwise target=bottom. Release P and permit fullRaw quantum access. No conditioning on target success is part of the game.

For P!=0 define the marked-capable region

R(P,A7,C)={P||zero48||A7||V16||BE32(c):V!=C}.

Every such word has exactly106 bytes. This region, not the entire seed slice or entire row header, is the region resampled in the proof. The complete same-C counter row remains untouched, including rejected earlier counters, accepted Y, unused counters and lower128 limbs.

## 2. Freshness after the permitted conditioning

Condition only on P, the fixed A7, independent F/J, complete outside-type7 collection randomness sufficient to compute C, and the complete SAME-C target row. First condition on P and all non-A7 raw restrictions: C is then fixed without reading any A7 coordinate. At that fixed C, the same-C row and different-base coordinates are independent product-function coordinates. Thus conditioning additionally on the same-C row, c0 and full Y does not alter the law of O on R. This holds pointwise for every nonbottom side-data value with positive probability. Bottom branches contribute zero, with no normalization by their success probability. Do not condition on any source-A quantum transcript, no-hit event, or final success.

Giving this independent side data to a hypothetical search simulator is legitimate auxiliary information. It is not permission to substitute independent keyed rows for the actual shared global function. All aliases of a raw word still refer to one O coordinate.

## 3. Boolean completion and exact query factor

Let N=2^128 and y=prefix128(Y). On the full160-bit payload domain x=(V,c), independently sample f(x)~Bernoulli(1/N). At every x sample independent L(x)128 and G(x) uniformly from128-bit words other than y. For V!=C define the full256 reply as

O_R(x) = (f(x)? y : G(x)) || L(x).

This is exactly an independent uniform256 function on R conditional on the side data. It preserves correlations between prefix equality and the full answer. f also has independent dummy coordinates V=C, which are never used to construct O; a winning output must have V!=C. This embedding supplies the ordinary full160-bit Boolean search domain without claiming a nonuniform-domain version of the cited theorem.

A fullRaw XOR query is simulated by: compute the reversible literal-region flag and payload index; query f into a clean bit; compute the appropriate full256 output using the fixed outside table or the above completion; XOR it into the caller's response; unquery f; uncompute temporary registers. Exactly TWO Boolean oracle calls suffice per logical fullRaw query, including a superposition of selected and outside words. For outside/malformed words any fixed valid160-bit index may be used, since the computed f bit is ignored and then uncomputed. No controlled-f access, coherent support test, or query-history measurement is required. Classical marked-region queries count in the same total.

SPHINCS+C, eprint2022/778 AppendixE, printed35 (PDF index37), Theorem E.3 states Succ_lambda^k <=8 lambda (k+1)^2. Its LemmaE.4 explicitly uses a2q-query Boolean simulator and obtains32(q+1/2)^2/2^n, plus its separate hidden-parameter reprogramming term. Here the selected region is fresh BEFORE A begins, so that reprogramming term is not invoked. With M simulated fullRaw queries that may access R, the exact theorem substitution is

Pr[changed-base target collision] <= min(1, 8(2M+1)^2/N).

It is NOT8(M+1)^2/N. This proof does not establish every collection version of the HK bound or import AppendixE's complete S-TCR oracle automatically.

## 4. Source marked-query cap versus total runtime

Take Q to include ALL adversarial Raw calls, pre-key and post-key, coherent and classical. Honest source calls do not contribute to M before final selected verification, under P!=0 and genuine-cache scope:

* Addressed type0--4 calls have a different type byte at offset73. No type5/6 Raw is used by HJ: ideal F supplies those private operations.
* Every honest selected-A7 call uses its fixed genuine C, so lies outside R. This includes setup grinding, signing grinding and digest rechecks. Other A7 addresses are outside the selected address. An unflagged source simulator may execute all of these normally; the proof need not delete their costs.
* H_msg inner is r16||P16||root16||m. If it were a106-byte selected word, bytes16..31 would imply P=0 because the selected word contains zero48 there. Hence impossible for P!=0, even for adversarially chosen106-byte inner words. The outer word is52 bytes and cannot alias106. Ideal J has no Raw query; if concrete PRF_msg were counted, its second16 bytes likewise contain P and the same nonzero exclusion applies, but its independence/security is not proved here.
* Final verification's inner/outer and addressed non7 calls obey the same exclusions. It visits each full row address at most once. Before its selected type7 query, all earlier final operations are outside R.

A conservative simulator retaining that selected final evaluation has M<=Q+1, giving8(2Q+3)^2/N. A tighter NEW search extractor stops immediately BEFORE that selected evaluation when the classical verifier has reached its exposed target row and computed V!=C, and outputs(V,c) directly. Search success is evaluated by the search game, so no final f query is needed. On every source Win&D7_base_final branch this output is marked; outputs from other branches only enlarge search success. Thus M<=Q and the tighter8(2Q+1)^2/N is justified for this stopping variant. It does not claim the stopped program completes source verification. No actual source attack is run.

Runtime still includes the source setup, initiated signing/reconstruction work, all honest canonical search/digest calls, input bytes and private F/J work. A coarse logical raw-evaluation cap is Q+H_setup+q H_mode+3224+17392+2^32, with overlap/shortcut reductions optional, final prefix work bounded by the ordinary final cap, and target preprocessing2^32 charged separately. This bound is an upper cap, not an equality or omission of ordinary honest queries. Distinct private F labels retain min(N_D,8704+2181038080+q U_mode), J<=q. Coherent outside/completion implementations must also charge initialization, storage and lookup gates: full eager finite tables can realize this proof but are huge, including32*2^160 completion bytes and the fixed outside/same-C tables. No efficient oracle implementation follows merely from conditioning on side data or from2M Boolean query accounting.

## 5. Commuting target preparation past the source pre-key phase

For each fixed classical O,F,J,P sample, target preparation/registration is a deterministic computation on reduction-private registers, while A's pre-key algorithm acts on A's own registers and uses the read-only U_O. Both are controlled by the same fixed O sample and neither writes O. These operations commute pointwise on disjoint work registers. Initial A randomness/state is independent of the private target process; C and A7 are not chosen from A's output. Therefore preparing C/c0/Y before running A pre-key, while withholding P/pk from A until the usual setup release, gives the same joint cq state as the source execution plus deferred private target records. This is a static-table statement, not a no-hit argument. Intermediate measurements are on private target records and are retained unconditionally. Bottom may trigger local extractor failure because its selected exposed-successful source event is zero; it is not a global source abort or postselected source distribution. This lemma concerns the specified untimed source interface, not physical timing leakage.

## 6. Consequence and scope

For the restricted primitive, without a source selector, the collision bound is8(2Q+1)^2/N for the pre-evaluation stopping extractor, or8(2Q+3)^2/N for the literal final-evaluation version. Separate lower/top selectors imply at most

Pr_HJ[Win AND D7_base_final AND S!=0] <= min(1, (2^42+2^21)*8(2Q+1)^2/2^128)

for the same Q cap in both component programs. Production S0 is charged once elsewhere. Predicate-specific target noncompletion retains its probability mass; this coarse inequality does not insert1/p or claim capacity/category. This is a manual mathematical component subject to independent review, zero new kernel declarations, no fixed-SHA theorem and no change to prior scalar results. The ordinary fixed-h conditional collection wrapper is a separate previously accepted statement.

Primary/source pins: source lib.rs ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210; SPHINCS+C PDF1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215; cached text833bcca0db93c57c3eff21e7982eb122aa386cdb2cdcdb696721d086cd406078. Primary theorem verified by direct PDF text extraction at PDF index37, not a recalled constant.
