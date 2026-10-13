# Independent identification of canonical type7 challenges with keyed notions

**PROVED / ASSUMED / CITED / OPEN — own argument saved before reading any NEW peer identification proposal.** The existing TYPE7-REDUCTION-PROGRAM.md is a finite RO-relative source-model result. This document examines its standard-primitive boundary; it does not relabel its independently sampled selected restriction as an ordinary shared-key function. No manuscript, implementation, previous receipt or scalar theorem is edited.

## Primary definitions actually checked

**CITED.** [Hülsing–Kudinov, 2022/346](https://eprint.iacr.org/2022/346), Definition2 and Definition7: ordinary SM-TCR registers targets before revealing the public parameter; the collection extension permits classical evaluations under that same hidden parameter at tweaks disjoint from challenged tweaks. This extension was introduced precisely to allow a target to depend on other hash computations. I read the cached primary PDF/text; PDF SHA80dcd11e56448d07e2a2465a11ef1a9ca8f4561387abeb3fabdd6d40d4ffe3c3.

**CITED.** [Kudinov–Hülsing–Ronen–Yogev, 2022/778](https://eprint.iacr.org/2022/778), DefinitionC.1, printed page30: S-TCR(Prop) supplies an accepted digest and counter, and its collision requires a different base message. I visually checked the definition. It specifies a counter satisfying Prop but does not explicitly specify first BE32 counter, finite32-bit exhaustion or a bottom response. Section5.1/Algorithm5 use an r-bit enumeration space with r set to the security parameter and assume a satisfying counter exists. This is different from the source's bounded32-bit format. The collection discussion and AppendixE are separate parts of the primary paper. PDF SHA1d24bcee44b6a719004cf6da5fd22275a06e2dac8a3a72acd8f8caa823a29215.

**CITED.** [Kudinov–Nick, 2025/2203](https://eprint.iacr.org/2025/2203), Definitions2.2–2.3, distinguish keyed and tweakable functions with a shared public parameter; they do not give a theorem declaring every source row independently keyed. Cached primary PDF SHA3c58f81a6a0b7e8e040134be1a0013b3977edefdc889e1636d4dfe79cf0e225e.

The three primary ePrint metadata pages were checked live on2026-10-13. All mathematical conclusions below are my deductions, not quotations or a claim that a published theorem already proves them.

## 1. The chronology obstruction is narrower than previously stated

**PROVED — interface observation.** 'The source child depends on S, therefore it cannot be registered before S is revealed' is false in the presence of the published collection oracle. A reduction can choose the full type7 address A7, sample the ideal-private F map, and compute C through type0–4 collection queries under the hidden public parameter. Source C computation never calls a type7 tweak. Thus all its collection tweaks are disjoint from A7 and meet Definition7's restriction.

After registration and parameter release, the reduction may start the signature adversary's PRE-KEY phase, while itself already knowing P=S. It withholds S/pk from that adversary until actual source setup completes. This changes the reduction's private computation order but not the adversary's source interface: C is a key-only fixed child, not chosen from an earlier signature-adversary message. No pre-key source oracle transcript needs to be served before primitive registration.

This observation supplies a possible new source-specific standard wrapper. It is NOT a black-box equivalence between the already accepted RO-relative row challenger and any arbitrary keyed family: that challenger independently creates a selected restriction after C, whereas a keyed family's entire joint function is fixed by its sampled key and implementation.

## 2. Precise bounded-first collection primitive

**ASSUMED — named additional property where not supplied by a primary definition.** Fix a public full-output hash implementation h:{bytes}->256bits. Define the actual shared-parameter collection

`Th_m(P,T,M) := prefix128 h(P || zero48 || Encode22(T) || M)`

for each required message length m. T includes layer/tree/type/keypair/height-or-chain/index fields; it is not a separately sampled key. All raw source hashes use this SAME h, including unaddressed words and literal aliases. There are no independent row functions in this definition.

For a fixed digit predicate Prop and Lc=2^32, define **CF-BS-TCR-collection(h,Prop,Lc)** (canonical-first bounded special target collision resistance with collection access):

1. Sample one uniform128-bit parameter P, hidden from B1. B1 can make classical Th_collection(P,T,M) queries at tweaks outside the eventual target set.
2. B1 registers one target tweak A7 and base C16. Its challenge oracle examines the SAME function's inputs C||BE32(c), c=0,...,Lc-1 in that order. It returns its first accepted prefix/counter, or bottom if all fail. It does not condition the parameter/function on success.
3. Reveal P. B2 has the public function algorithms. It returns V16,c32 and wins when target exists, V!=C, and Th20(P,A7,V||BE32(c)) equals the supplied canonical target prefix.

The lower128 target limb is not an extra security assumption in the PUBLIC-IMPLEMENTATION standard model: after P is revealed B can compute h on the exact canonical raw word and retain its full output. Its prefix equals the oracle value by the collection definition. All other source raw calls are also computations of that same h. Their time/gates, input bytes and work are charged, not treated as independent ideal functions.

**OPEN — QROM black-box distinction.** If h is instead an externally supplied global quantum RO, its coherent full256 interface must be explicitly available to the primitive adversary and tied to the prefix collection. A definition giving only an opaque128-prefix oracle does not automatically grant full256 raw oracle access. Computing a public implementation and querying an unknown oracle are different resource/interfaces. Name the global-RO extension explicitly or prove its simulator; do not fill unknown lower limbs independently for fixed SHA.

## 3. Source-specific wrapper under that property

**PROVED — conditional program specification, not hardness certification.** Work in HJ[h], the source signature experiment with ideal independent F/J and the concrete shared full implementation h. This is a separate instantiation from the existing random-oracle HJ[O] theorem; no equality between fixed SHA and RO is claimed.

The primary C.1 predicate is fixed, whereas LULA rows use two predicates. Split the final first-D7 witness into lower rows (layers0–3; Prop4 is32 width4 digits summing240) and top rows (layer4; Prop8 is16 width8 digits summing2040). Let D_lower=2^41+2^36+2^31+2^26=2,269,957,324,800, D_top=2^21. Use a42-bit padded lower-row selector and an exact21-bit top selector in TWO primitive adversaries. A single challenge with a selectable layer predicate would be an explicit larger property, not automatically C.1 with one fixed Prop.

For either adversary B_b:

- Before P release, choose its row and sample consistent ideal F/J. Compute its genuine child via the permitted collection oracle at type0–4 tweaks. Lower selected layer0 needs17,392 collection calls and8,704 F labels; every upper selected row needs15,423 collection calls and1,024 F labels. No challenged type7 tweak is queried through the collection.
- Register C and the selected A7. On bottom return failure. Receive P, and fail locally if P=0 when using the existing nonzero component scope. Otherwise run A's pre-key phase with P withheld, then the actual source setup/sign/restore/final interface using full h and the same sampled F/J. Supplied canonical data are used only for the selected row's genuine C; all other values/functions remain the actual implementation.
- On a selected final changed-base collision, output that V/c to the primitive. Early valid collision extraction may add success. The source event still requires a reached honestly exposed successful row and final root acceptance. A selected bottom row has zero such event and does not add a global source abort.

Every valid selector's unflagged source view is the same HJ[h] view under one P; no row independence is needed. First qualifying final witness selection therefore proves

`Pr_HJ[h][Win AND D7_base_final AND S!=0] <= 2^42 Succ_CF-BS-TCR-collection(h,Prop4)(B_lower) + 2^21 Succ_CF-BS-TCR-collection(h,Prop8)(B_top)`.

This is an explicit assumption-parametric reduction with source-relative resource caps, not an evaluated probability bound. Registration count is1 per B, and challenge preprocessing is at most2^32 Th evaluations, separately charged. Phase2 time includes source setup, q initiated signing jobs, final verification and every raw h evaluation made to simulate A. Private distinct labels conservatively add8,704 to2,181,038,080+q*U_mode before namespace capping; J<=q. Phase1 collection calls and all honest hashes must be included in the standard adversary's time/global-oracle budget. They are not merely A's Q_H/Q_q. Consequently a published bound with query/time parameter Q cannot be instantiated using only source adversarial Q while dropping B's honest work.

## 4. Exact missing refinement to the published property

**OPEN — smallest counter-policy lemma.** To invoke published S-TCR(Prop) directly, prove that its challenge oracle has a specified counter policy whose restriction to C||BE32(0),...,C||BE32(2^32-1) agrees with the canonical-first source oracle, including bottom handling. If its chosen accepted counter differs, a source equality to the canonical c0 digest need not collide with the challenger's chosen target. A generic phrase 'some accepted counter' is not this lemma.

One sufficient refinement uses an oracle that searches these32-bit encodings first, in order, and continues a defined larger counter domain only after their exhaustion; B fails when its returned counter lies beyond the32-bit range. Then the selected source final event is zero on precisely the truncated-row failure branch, so the reduction incurs no1/tau normalization. This is conditional on that explicit selection/encoding policy; it is not established by merely noting C.1 writes an integer counter. Another sufficient route is to adopt the named bounded property above as an additional assumption.

In particular, appending a128-bit counter to C16 queries a different message-length member than source C16||BE32(c). Leading-zero padding is not an equality of hash inputs. The refinement must explicitly preserve the literal20-byte digest payloads; a generic search over C16||BE128(c) is not their extension. The paper's larger-counter existence convention therefore does not close the source exhaustion/encoding lemma by itself.

Collection access must also be extended from Definition7 to the accepted-counter oracle and the actual source collection. Its disjoint-tweak restriction is satisfied structurally by C computation, but legality and resource counting of the complete full raw interface must be specified. Predicate4/8 separation, mixed message lengths, full-output/raw linkage and global parameter distribution are additional explicit interface fields, not independent-key assumptions.

## 5. Simple countermodel to predicate-only identification

**PROVED — abstract mathematical countermodel, not an actual source attack.** For N=2^n and public key P in[n-bit strings], define the target tweak's base hash F_P(M)=M except F_P(P xor1)=P. Ignore a counter and take Prop identically true with canonical counter0. Its only changed-base collision pair is {P,P xor1}.

An ordinary stand-alone pre-key one-target S-TCR adversary chooses C without knowing P. It can collide after key release only when C lies in that pair, probability2/N. A post-key target chooser sets C=P and succeeds with V=P xor1 with probability1. A separate collection tweak returning P allows the hidden-parameter collection target chooser to do the same. The latter correctly violates COLLECTION security while stand-alone target security remains2/N. Finally, replacing the target row's key by an independent freshly sampled R after C=P restores target-hit probability2/N; that independent-row game does not describe the shared-key source family.

Thus matching V!=C and target equality does not imply challenge-interface equivalence. Public-before-target and correlated collection dependencies can change security by factor N/2. This countermodel does not refute the proposed collection wrapper: it explains why the collection property and global function link must be actual assumptions, and why stand-alone target resistance or fresh-row security alone is insufficient.

**OPEN — final verdict.** The hidden-parameter collection route removes one genuine chronology obstacle and gives a precise bounded-first assumption-parametric wrapper. Direct identification with the published oracle's unspecified counter policy and the original QROM/global-full-function game remains unproved. Existing complete source RO/QROM bounds, all scalar numerics, forty supporting declarations and original level/category verdict remain unchanged. No claim of actual SHA hardness or source insecurity is made.

## 6. Exact separation of two valid accepted-counter policies

**PROVED — abstract countermodel to an unspecified-policy implication.** Let registerable base messages be{0,1}, counters be nonnegative integers, and outputs be{0,1,2}. Let the keyed function ignore its key and return H(M,c)=0 if c=0, otherwise M+1. Let Prop be true on every output. Both counter policies 'return0' and 'return1' satisfy the written requirement that the counter's output meets Prop.

Under canonical-first policy the target is0 for either base, and the other base with counter0 is always a different-base collision: success1. Under policy returning1 the target is M+1; the other base can output only0 or its own different label, so a different-base collision is mathematically impossible: success0. Thus there is no universal finite-factor implication from special-TCR security under an arbitrary valid-counter policy to canonical-first special-TCR security. This separation concerns selection policy, not a hash implementation or a source forgery. It also survives any finite counter cap that contains0 and1. It explains exactly why the named first-counter refinement is a mathematical gate rather than merely a runtime convention.

## 7. Ordinary collision-resistance fallback and its limited meaning

**PROVED — another conditional primitive reduction.** Without any accepted-counter challenge, D7_base_final directly gives a collision for the UNKEYED TRUNCATED function h128=prefix128 h. A simulator runs HJ[h] under one actual shared h and its own ideal F/J, retaining each exposed row's genuine C/canonical c0. A successful final changed-base witness supplies the two distinct literal raw words `(S||zero48||A7||C||BE32(c0))` and `(S||zero48||A7||V||BE32(c*))`. Their h128 values agree and V!=C makes the words distinct. An ordinary collision-resistance adversary can output those words. This reduction needs no42-bit selector and makes no row-independence claim.

Its time includes all source setup/signing/final/raw computations and private-map work; at most five canonical records per completed signature are retained before namespace capping. It is a conventional assumption-parametric fallback, not a stronger quantitative result. The collision is for the128-bit truncation, NOT necessarily full SHA-256. Generic collision work for a128-bit output does not yield the requested128-bit classical signature guarantee. Equally, generic truncated-hash collisions are not automatically source signature forgeries. This fallback neither proves that LULA has a64-bit attack nor closes the original capacity/category goal.

The three distinct routes are therefore: a precise additional bounded-first collection property; a proved canonical-counter/full-raw refinement of the published property; or a weaker ordinary truncated-hash collision assumption. Each carries its own quantitative resource/security implications. They must not be silently substituted for one another.
