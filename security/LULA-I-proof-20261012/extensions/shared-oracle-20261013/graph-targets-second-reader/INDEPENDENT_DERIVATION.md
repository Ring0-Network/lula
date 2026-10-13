# Independent typed-graph target derivation

This derivation was saved after reading the actual release Rust library in full and BEFORE reading `graph-targets/DERIVATION.md` or its controls. Only this second-reader directory is written. Scope is a same-address honest-graph target-collision event in the classical complete-SHA random-oracle joint ideal game, not a full EUF game or a signature attack.

## One honest payload per target address

**PROVED (source).** Fix parameters and seed-derived chain starts. Each public target-family address contains the entire 22-byte ADRS and the fixed 64-byte public-seed prefix. For types 0..4, the seed and address define one honest payload:

- Type 0: at `(layer,tree,keypair,chain,step)`, the payload is the honest chain value before that step. Step zero uses an ideal secret derivation; later steps use the preceding step's output at a DIFFERENT complete address. Used steps are 0..w-2.
- Type 1: the fixed tuple of honest chain endpoints, at that WOTS keypair's compression address. Endpoint calculations do not depend on the message certified by WOTS or on its search counter.
- Type 2: the honest ordered children of one hypertree node, with level and parent index in the address. Leaves are type-1 outputs; higher nodes depend on children with lower heights and different complete addresses.
- Type 3: at height zero, one fixed ideal FORS secret; at higher heights, one ordered child pair. Tree-global index `j*2^(a-height)+local` prevents aliasing between the 17 real trees.
- Type 4: the fixed tuple of the 17 honest FORS roots for one complete FORS-instance address.

**PROVED (source DAG).** These dependencies are acyclic and do not read the target address's own function restriction. Order WOTS steps, endpoint compression and Merkle heights; separately order FORS leaves, heights and root compression. WOTS endpoints depend on chain-start material, not on the lower child value eventually signed. No type-7 digest or canonical-counter result is an ancestor of a type-0..4 honest payload. Collisions between node VALUES do not collapse distinct address domains.

**PROVED — exclusion.** Type 7 has one address per WOTS keypair and many payloads `child||counter`. Its canonical counter depends on its OWN address-restricted random function. Treating a canonical type-7 payload/image as an independent honest target is invalid; first-accepted output distribution is also biased by the target-sum predicate. Types 5/6 are private ideal maps in the joint game, not public target restrictions of O.

## Eager sampling and residual independence

**PROVED under the random-oracle model.** Conditional on fixed external seed/ideal-map coins, sample an independent full 256-bit target image Y_a per legitimate type-0..4 address in DAG order. Compute honest payload v_a from predecessor target prefixes. Complete each function O_a by setting O_a(v_a)=Y_a and independently sampling every other payload point. Because v_a is determined without inspecting O_a's own images, this produces the same ordinary random-function marginal. A finite-table proof assigns each completed table the ordinary product probability; the actual countable RO follows by consistent finite projections, with only finite input sets queried in any bounded execution.

**PROVED (precise information scope).** Given all ideal-map coins, all honest target pairs `(v_a,Y_a)`, and the full functions of all OTHER address domains plus non-target domains, the off-target residual entries of O_a remain mutually independent uniform values. The completed other-domain functions depend only on their own residual coins and the shared honest graph's target images, not on O_a's off-target entries.

**FALSE if 'outside information' means arbitrary transcript.** An adversary can read O_a(z) at an off-target point, then encode that answer in a query at another domain. Conditioning on that other-domain query INPUT reveals the residual value. Thus independence is not conditional on arbitrary adaptively generated outside-query transcripts. The useful next-query statement conditions on the actual previous history: a genuinely new off-target point's answer remains uniform, while previously queried entries are already known and cannot be charged again.

**PROVED — target-event budget.** Give the adversary the entire honest target graph and all outside-domain functions as additional side information, and count its actual target-family residual queries. Each new query at address a and payload z!=v_a reproduces the honest 128-bit target prefix with probability 2^-128. It tests one address's target, not every target in the conceptual forest. Union-bound the at-most Q_H such opportunities, plus target-family calls newly evaluated by final verification. Query adaptivity and altered-path dependencies do not change freshness: use the later fresh evaluation and count old successful collisions at their earlier evaluation.

**Important scope:** full graph exposure includes secret chain-start payloads and can enable full signature generation. This strong side-information experiment is suitable ONLY for bounding the specified off-target collision event; it must never be relabeled as the real EUF-CMA game.

## Shared-input and pre-key qualifications

**PROVED (source).** On public seed S!=0, an unaddressed inner input has bytes16..31=S; target-addressed inputs require zeros there. Outer inputs have length52, target-addressed inputs have length at least102. Address types separate target families from types7 and private5/6. Hence intended outside functions really are restrictions to disjoint complete encoded inputs in this branch. Charge the S=0 branch explicitly for an unconditional claim; do not silently divide by or condition away its probability.

**PROVED — pre-key queries.** The eager construction can sample S and the whole graph first but withhold them to preserve the real chronology. Its conditional-on-S completed O marginal is ordinary, so pre-key raw evaluations remain consistent; later disclosure cannot resample or overwrite their values. Alternatively a target-search upper bound may give the adversary the graph earlier as extra information. Prior successful target collisions still count against the total Q_H. An efficient real reduction must account for the enormous graph construction separately; an information-theoretic graph-event bound does not prove an efficient primitive embedder.

## Exact final-verifier call caps

**COMPUTED from the source, not runtime measurement.** Fixed signature length permits early rejection; reaching all accepting digit predicates maximizes calls. A complete SHA invocation is counted once regardless of its number of compression blocks. Prepared compression state is not a separate complete SHA query.

| Family | Complete hash calls |
|---|---:|
| Message inner and outer, unaddressed | 2 |
| FORS type3 leaf/path hashes:17*(1+9) | 170 |
| FORS type4 root compression | 1 |
| Four lower WOTS reconstructions/type2 paths:4*(240+1+5) | 984 |
| Top WOTS reconstruction/type2 path:2040+1+21 | 2062 |
| Five WOTS type7 digest checks | 5 |
| All complete SHA calls | **3224** |
| Target-family types0..4 only | **3217** |

Lower chain completion is32*15-240=240; top completion is16*255-2040=2040. All target-family verification addresses fall inside the legitimate fixed-parameter graph; modified values/path siblings alter payloads but not those bounded address ranges. Instrumented compression count3265 for32-byte input and prefix initialization are different accounting units and are not the complete-hash cap.

**PROVED event bound under declared premises:** fixed nonzero S gives `P(target collision in adversarial/final queries) <= min(1,(Q_H+3217)/2^128)`. An unconditional conservative graph-event bound adds2^-128 for S=0. This does not assert that every fresh-message forgery causes this target event; that classifier and the remaining digest/chain routes require separate proof.
