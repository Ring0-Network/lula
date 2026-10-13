# Independent source-first message-hash / ITSR interface derivation

Saved before reading any NEW selected peer message-hash/subset-resilience proposal. Author: outside-field-check. Source inspected in this turn: `publications/LULA-I/release/code/lula1/src/lib.rs`, SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Scope: exact source interfaces and named conditional covered-coordinate assumption; no hardness number, lower-bit uniformity, source attack, or RO-bound transplant.

## 1. Primary definition checked independently

I read HK22 `eprint_2022_346_hulsing_kudinov_tight.txt` lines1323–1346 (Definition11, printed page30) and the SPHINCS+ r3.1 specification's Section9.1, cached text lines1911–1935 (printed page49). The latter expressly supplies the sampled key, avoiding the extraction ambiguity in HK's compressed text. The primary game takes a public efficient keyed H, G=MAP_(h,k,t) o H, and a classical target oracle. On message M_i the oracle samples a fresh uniform key/nonce R_i, returns R_i and G(R_i,M_i), and records that input pair. The adversary knows G and may evaluate it on arbitrary candidate pairs. It wins if its candidate coordinates lie in the union of registered coordinates and its input pair was not registered. Quantum adversaries are permitted, with a runtime budget and classical target queries.

Sources: https://eprint.iacr.org/2022/346 and https://sphincs.org/data/sphincs+-r3.1-specification.pdf . I opened primary metadata/search results live. Direct fetches of the original SPHINCS+ paper PDF at sphincs.org and eprint2019/1086 failed502/403; no missing theorem from those fetches is assumed. The cached primary specification and HK definition suffice for the interface comparison. HK's Table3 describes its generic ITSR estimate as conjectured; no numerical ITSR estimate is imported here.

## 2. Actual complete source message function

Fix ONE public full256 implementation h. In SrcFJideal_h, sample uniform16-byte S, persistent independent secret-address map F, and persistent independent message map J:M->16-byte strings. Public hashes remain this fixed h. Source setup using F,h,S produces a root Z; setup may fail/noncomplete under its finite partial convention. Z is NOT independently sampled uniform and must not be replaced by such a variable. Its joint distribution with S and retained F is the actual source distribution.

For a requested message M set R=J[M],

U_(S,Z)(R,M)=h(R16||S16||Z16||M),
D_(S,Z)(R,c,M)=h(U32||BE32(c)||S16).

Source lines169–189 implement both full256 stages; inner output is not truncated. Signing lines601–620 searches c=0,...,2^32-1 for the first D with bits153..161 zero. R is drawn once on the first M and reused for every occurrence of that complete message, including after honest restoration. It is not resampled per attempt or per repeated signature. Counter exhaustion is absorbing nonwinning, with no normalized target resampling or invented completion.

Read bits0..152 as17 real9-bit leaf indices j_0,...,j_16. Bits153..161 are the omitted eighteenth index, forced zero. Read bits162..202 as one41-bit route I. The source bottom FORS address is (tree=I>>5,keypair=I mod32); the coverage coordinates can equivalently use (I,i,j_i), i=0,...,16. All coordinates for one digest share I. Bits203..255 are not used for this routing, but all256 U bits enter the outer hash and the actual full D is computed.

Final verification lines679–716 parses an arbitrary transmitted R* and c* and computes these same functions on M*. It checks the zero9 filter, but NOT that R*=J[M*] and NOT that c* is the first passing counter. A fresh-message source forgery has M* outside the permanent Seen set. Its (R*,M*) is consequently unregistered, which is stronger than the primary ITSR pair-novelty condition. A same-message changed-R candidate can win primary ITSR but cannot win the source freshness event; the reduction must keep the stronger source freshness test without claiming the notions identical.

## 3. What can be reconciled without a new cryptographic lemma

Repeated-message target sampling is not a fundamental obstacle: B can call the primary target oracle once per distinct M and retain its returned R/coordinates. Repetitions use that saved reply, producing an exact ideal J on the labels actually reached. There are at most q target calls for q initiated classical signing requests, not q new draws on repeated M.

The actual source parameter/root distribution also need not be replaced by an independent uniform root. One legal approach is a public tagged function on primitive message inputs Enc(S,Z,M), with a fixed injective wrapper encoding for the finite input register model. The hash function parses that wrapper and evaluates the LITERAL source byte frames above; wrapper tags/length encoding are not injected into source hash inputs. B samples S and F, performs exact source setup with h, retains F to supply consistent signatures, then uses this actual (S,Z) tag in every target query and candidate. Primitive R keys remain independent of S,F,Z. Ordinary ITSR allows B to choose messages/tags adaptively, so arbitrary-tag insecurity would cover the actual correlated parameter distribution. A theorem for an independently sampled/hidden uniform root, or an untagged unrelated function, would still need an explicit applicability lemma.

Alternatively the named primitive may explicitly include the actual source joint public-parameter sampler and a retained auxiliary source state. This is a source-relative public-parameter variant, not a verbatim claim about a standard independently sampled public key. B may retain its own independent F for simulation; F is NOT disclosed as adversarial advice to A, and the primitive does not grant A an unrestricted secret-map oracle.

A's pre-key phase can run with fixed public h and S/Z withheld; preserve its full quantum continuation. Setup and release follow the same source chronology. Presampling hidden S/F before that phase changes no visible public h code. Source services remain classical and atomic; public h can be computed coherently with charged gates. Do not expose internal setup/search transcripts or the retained F dictionary.

## 4. The unresolved primary-ITSR counter interface

Using H_can(R,M)=the first accepted D for this nonce/message makes the HONEST target law match after nonce-key sampling; B can recover c0 by local evaluation. Bottom could be totalized with a deterministic dummy output in the primary total-function interface and B could abort on detection: on that branch the source completed-signature event is zero, so no success normalization is needed. This is an event-specific construction, not an assertion of full source transcript law on a noncompleting branch.

But H_can also maps the final candidate (R*,M*) to its FIRST accepted c0*. Source verification accepts D(R*,c*,M*) for ANY passing supplied c*. A covered source candidate at c* need not make H_can(R*,M*) covered. Thus source fresh-message coverage does not automatically yield a primary ITSR witness for H_can.

Using instead H(R,(M,c))=D(R,c,M) matches arbitrary final c, but target-oracle nonce R is sampled only AFTER B specifies (M,c). The honest source c0 depends on the newly sampled R and may require2^32 local tests. B cannot retroactively register (M,c0) under that same R in the primary oracle. Further oracle queries sample fresh R, not the needed reused one. Packaging R and c together as a uniform primary key is wrong because source c0 is a message/nonce/hash-dependent first-success variable, not an independent uniform32-bit key component. No assertion of output uniformity fixes this interface chronology.

The smallest missing lifting lemma is therefore **canonical-target / arbitrary-valid-counter ITSR compatibility** for this exact two-stage full256 h, literal BE32, finite first-zero9 search and source tag/nonce distribution. It must turn a covered valid D(R*,c*,M*) into a legal candidate in the claimed primary game, or prove a bound directly for the named variant with the same resource accounting. Published ITSR for H_can alone is not that lemma; ITSR for H on arbitrary (M,c) inputs alone does not register the source target law.

## 5. Exact named assumption and source component program

Define CTAC-ITSR_h (canonical-target/arbitrary-counter interleaved subset resilience), with the full source parameters or the tag construction above:

1. h is fixed public full256. Generate the actual S,F and setup root Z, retaining consistent F only in the simulator; setup noncompletion is nonwinning. Run A's source pre-key interface at the proper point with S/Z withheld until normal release.
2. A classical target service takes complete M. On its first use draw uniform R=J[M], then compute the first zero9 passing c0<2^32 using the SAME h. Return R,c0 and D/coordinates on success; bottom yields the same absorbing nonwinning service outcome. Repeated M uses the same R/c0/result. Internal full rejected digests are not fresh oracle objects.
3. Define the exposure union ONLY from completed source signing targets, with17 real tuples(I,i,j_i). A target request alone that never returns a complete source signature does not expose FORS secrets in the original atomic experiment.
4. Candidate is (M*,R*,c*) with M* fresh, R* arbitrary16 bytes, c* arbitrary32 bits. It is eligible only when D's zero9 condition holds. It wins if all17 coordinate tuples lie in the completed exposure union. No final source forgery, hidden-key recovery or lower-bit uniformity is part of this primitive's coordinate predicate.

B simulates SrcFJideal_h with its retained F and the target service, public h and consistent source cache, creates exact signature responses only on completion, then evaluates the actual final verifier/classifier. If the source's covered-coordinate final event C occurs, output its M*,R*,c*. This gives Pr[SrcFJideal_h C] <= Succ_CTAC-ITSR_h(B), or equality if B outputs only when its exact coordinate event and source Win occur. The inequality is a program/interface identity conditional on the NAMED assumption, not evaluated hardness. It supplies no bound for other forgery events arising from public graph/FORS/WOTS replacements; those require their own H/G/public-component analysis.

This definition includes source auxiliaries, so it must not be presented as a already-proved conventional ITSR reduction. A cleaner abstract primitive can return one fresh uniform nonce per unique M and canonical full coordinates and allow a simulator-controlled commit only after complete signing; B's independent F then simulates the other source services locally. The exact legality and quantitative transfer of this cleaner game to primary ITSR remain the lifting obligation above, not a hardness conclusion.

## 6. Resources and a discriminating finite control to construct

Every message inner hash, every at-most2^32 outer trial, setup/FORS/WOTS service hash, private-map operation, final verifier/classifier hash, quantum public-h circuit and all message bytes are charged. q bounds initiated classical signatures across both repeated messages and restored branches. The primitive target service's canonical preprocessing is not a free adversarial hash budget. Input/parameter sampling is ex ante and retains actual S/root/F correlation. Final R/c/M searches are computations of known h, with no oracle-programming privilege.

A finite logical discriminator should have one nonce, two messages, two counters, one route, one real coordinate and a predicate accepting both counters. Let D(M,0)=M for M in{0,1}, and D(M,1)=0. Signing M=0 canonically exposes leaf0. A fresh candidate M*=1,c*=1 is valid and covered, but H_can(1)=D(1,0)=1 is NOT covered. With a singleton nonce domain, primary ITSR for the canonical map has no fresh-input covered candidate, while the arbitrary-counter variant succeeds. This is an abstract interface separation, not the actual LULA predicate or an attack on SHA. A second control can show fresh-per-request nonces versus memoized per-message nonces differ on repeated requests, while B memoization exactly repairs that mismatch. A third can show replacing a source-derived root by independent uniform root alters joint raw/auxiliary views.

No new peer proposal has been read at this save. No earlier RO/QROM or fixed-h numerical estimate is used. The immediate result is an explicit named assumption-parametric source component and a sharply specified primary-game lifting frontier.
