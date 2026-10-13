# Ordinary public-parameter private-PRF source adapters

**PROVED — independently reviewed exact manual identities.** Fix one deterministic public full256 hash implementation h, including a public clean quantum evaluation circuit where needed. There is no separately sampled/programmed Raw oracle. Source lib.rs remains ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210. This is a fixed-hash model, distinct from the earlier RO-relative private programs; it closes ordinary private-hop interfaces without importing any old RO scalar bound.

## 1. Exact families and assumptions

**PROVED — definitions; ASSUMED — hardness.** For independent uniform16-byte public S and secret K,P, define

`f_K^S(A22)=prefix128 h(S||zero48||A22||K16)`,

`g_P^S(M)=prefix128 h(P16||S16||M)`.

An ordinary public-parameter challenge gives S to the reduction and one classical private evaluation interface. REAL returns the indicated keyed family; IDEAL returns one independent memoized128-bit random function on addresses or messages. Advantage is the absolute REAL/IDEAL output-one gap, without a1/2 factor. Post-quantum distinguishers are allowed, but source private queries are classical; coherent private-query PRF security would be a stronger assumption. The source consumes only the prefix, so no unused lower-output-limb PRF hypothesis is introduced.

**ASSUMED / OPEN.** These particular SHA-256 compositions are not proved PRFs by their names or by these reductions. Their advantages remain named, unevaluated assumptions. The same public h code remains locally computable on ALL source/adversarial words, including literal private/public aliases and coherent public computations. Public h computation costs are charged; no independent side oracle is supplied.

## 2. Source games and partiality

**PROVED.** SrcReal_h uses both f and g. SrcFideal_h uses independent F for secret-address values and real g for randomizers. SrcFJideal_h uses independent F/J for both. Every other source hash, including full256 H_msg inner/outer and all typed public compressions, uses the SAME fixed h. The strict source parser/final freshness event is preserved. Honest caches and restores retain one logical function. No private keys, cache bytes, timings or internal hash transcripts are exposed.

**PROVED.** The source adversary's pre-key phase has the public h algorithm but no S/pk or private service. The reduction receives S from its primitive challenge, withholds it from A until normal setup release, and preserves A's pre-key continuation. Source searches have at most2^32 distinct trials in this decision experiment; failure/noncompletion yields absorbing nonwinning output0 without a public key if setup fails. This totalizes the cryptographic decision game, not native overflow or panic semantics. Initiated requests and all message bytes remain charged.

## 3. Two explicit ordinary distinguishers

**PROVED — B_K.** Receive S and Eval_f. Sample secret P independently. On secret(A), memoize Eval_f(A); on randomizer(M), compute the prefix of h(P||S||M) locally. Compute all other public hashes with the SAME h. Intercept every source private call, so unknown K is never read from a context placeholder or inserted into a public frame. Run A/pre-key, source setup, release/resume, initiated signing/restores and final verification; return Win. REAL has exactly SrcReal_h law and IDEAL exactly SrcFideal_h law.

**PROVED — B_P.** Receive S and Eval_g. Supply an independent lazy F for all secret-address values. Memoize Eval_g(M) on first randomizer access. Use the SAME full public h everywhere else, with unknown P never reconstructed. Execute identical source phases/freshness/partiality; return Win. REAL has SrcFideal_h law and IDEAL SrcFJideal_h law.

**PROVED — exact gaps and composition.** Let p0,p1,p2 be the Win probabilities of these three source games. The signed challenge gaps equal p0-p1 and p1-p2. Therefore

`|p0-p1|=Adv_PRF(f;B_K)`, `|p1-p2|=Adv_PRF(g;B_P)`,

`p0 <= p2 + Adv_PRF(f;B_K)+Adv_PRF(g;B_P)`.

There is no selector or namespace factor, and no extra seed-zero term in these hops. All literal aliases agree in REAL because the algorithm is identical; IDEAL deliberately removes the corresponding private correlation and the PRF advantage pays for it. These identities preserve the complete interleaved source-facing view, including quantum A's retained memory and local coherent h computation. They are not statements that revealed R is independent of the posterior signature transcript.

**PROVED — parameter averaging precision.** At fixed S the signed gaps are pointwise. For an independently sampled public S, the exact advantage is |E_S[p0(S)-p1(S)]| for that public-parameter challenge, not automatically E_S|p0(S)-p1(S)|. The latter is a valid larger envelope if separately assumed; a worst-case-in-S bound is another stronger assumption. Do not claim an equality between these different conventions. The second hop has the analogous distinction.

## 4. Complete private and public resource accounting

**COMPUTED / PROVED.** Source namespace N_D=19,212,937,084,272,640; setup distinct/invoked secret calls2,181,038,080. Hot distinct/invoked per initiated signature12,816/12,961; cold33,567,232/33,567,393. The private challenge cap is D<=min(N_D,2181038080+q U_mode), and Eval_g<=q. Final verification makes zero private calls. Restoration does not reset dictionaries. These private loop counts were independently rederived; the complete public ledger is inherited from the reviewed private program count audit.

**COMPUTED / PROVED.** With L=2^32,

`H_setup=2^21(19505+L)-1`, `H_hot=82090+5L`,

`H_cold=8,560,574,463+82090+6L`, `R_src=H_setup+qH_mode+3224`.

B_K evaluates at most R_src+q public h calls locally, plus all A's explicit/inlined public computations. B_P evaluates at most R_src locally, plus A's computation. The REAL private challenger itself evaluates at most D complete102-byte f hashes or q hashes of length32+|M|; its IDEAL dictionaries are also charged to complete experiment resources. Do not count the same private hash both as a local reduction call and a challenger call. Message-length and reversible-circuit generation/workspace costs remain explicit; no wall-clock or practically efficient implementation conclusion follows from these enormous finite caps. The full source/A/dictionary/cache/output storage envelope is in the preserved first derivation.

## 5. Smallest remaining public-hash lemma

**PROVED — interface countermodel; not an attack.** Replacing a public full hash by h'(x)=prefix128 h(x)||zero128 preserves every private f/g output pointwise but makes source route bits162–202 identically zero. Thus information about private prefix interfaces alone supplies no theorem of uniformity for the lower output limb used in H_msg routing. This is an abstract interface implication countermodel, not a claim of PRF hardness for a modified function, source forgery or failure of actual SHA-256. The independent reader supplies an exact executable control of this logical separation.

**OPEN — smallest next obligation.** Bound the fixed-hash ideal-private source game's public H_msg/adaptive coverage and addressed graph/PRE/TCR events under properties that actually cover its full output, literal aliases, source-selected targets and adversarial R/counter choices. Only after that bound may p2 be replaced by a quantitative expression in the ordinary PRF composition above. The earlier HJ[O] expressions cannot be silently used for HJ[h]. Private hardness, adequate full-security level/category and certified capacity remain unestablished.

## 6. Evidence and scope

**PROVED / COMPUTED.** The author's first6c44c1b3 and reader's firstce159512 preceded peer inspection. outside-field-check/public-h-private-review/REVIEW.json accepts the exact identities, pre-key interface, full-hash aliases, averaging distinction and resource split. Independent reexecutions of both author controls are byte-identical; the second control actually exercises eight absorbing-bottom worlds. Additional reader controls use actual102-byte private frames and seed-zero aliases. These controls and manual reductions add zero checked whole-source/game declarations. Manuscript, source and old numeric/theorem artifacts are unchanged.
