# Independent second-reader verdict: quantum joint private-input hop

**Outcome: ACCEPTED_MANUAL_FINITE_QROM_JOINT_PRIVATE_HOP.** The author's conservative state/event-distance lemma is valid in the expressly finite full256 public-oracle, classical atomic-service model. I derived the same constants independently from the source before reading the author. No blocking mathematical defect was found in the stated scope. This accepts one joint private-input hop, not complete QROM signature security, an efficient/PPT simulator, fixed-SHA security, a quantum PRF theorem in the standard model, or a category certificate.

## Subject and independence

`INDEPENDENT_DERIVATION.md` was saved before opening the author packet. The source raw encodings, private derivations, I/E calls and signing counter loop were re-read directly.

| Reviewed object | SHA-256 |
|---|---|
| release/code/lula1/src/lib.rs | ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210 |
| quantum-private-frontier/DERIVATION.md | a70d84506c789ff567969bed77d67d1513722ff570fec004ad9ff757da863adf |
| quantum-private-frontier/quantum_control.py | 1d0669a8448761d723a9fc654b73da1b2bb3342604cbbc9741d86e7f3498e595 |
| quantum-private-frontier/CONTROL-RESULTS.json | 38d104fd95bed2763e483f9ad6595012340058dbd4af3f3d4c3e727a9a218423 |

I read the finished author derivation, controls, receipt, primary-comparison note and handoff after the independent save. The author script was inspected without running its writer in the peer directory. Independent executable controls live only here.

## Per-obligation verdict

| Obligation and author section | Verdict / independent reason |
|---|---|
| Finite source/query register, `Source and finite experiment` | PASS. Full256 XOR output is explicit; the fixed injective length-aware raw encoding covers allowed coherent inputs and all relevant honest inputs. The 598-byte maximum addressed endpoint compressor is correct. Invalid behavior and length caps cannot depend on K/P. This is a finite-interface result; no infinite-register limit or materialization efficiency is claimed. |
| Disjoint private families | PASS for fixed nonzero S. D_K has zero bytes16..31 and M_P has S there. Every raw basis input nominates one key family at most. A factor equal to all private addresses or messages is unnecessary; a gratuitous factor2 in averaged membership is also unnecessary. The degeneracy at S=0 is charged separately. |
| Auxiliary J suffix labels | PASS. The author explicitly samples J for every suffix in the raw private family, including root||m and counter||S. Restricting J to only allowed signing messages would break the coupled public I/E alias cases. |
| Ordinary full256 RO marginal, `Full256 coupling with correct marginals` | PASS. O_1 assigns independent complete images at disjoint injective private points and O_0 elsewhere. Given K/P/S its whole function marginal is ordinary uniform. Prequeries use the same pre-sampled tables and no existing response is overwritten. Source prefixes do not license dropping the unreturned tails. |
| IDEAL key independence | PASS. The continued ideal service uses only F/J/O_0 and key-blind handles; K/P remain unused. Its quantum state may depend arbitrarily on those ideal tables but not on K/P. This is not an independence assertion about a REAL posterior after interaction or after avoiding a hit. |
| One coherent query discrepancy, `One coherent query bound` | PASS. The local operator difference is supported on private inputs and has norm at most2. Its Euclidean action is bounded by2 sqrt(mu), normalized trace distance is no larger, and averaging ideal unused keys plus Jensen gives2/sqrt(N). Work/output ancillas and full images are included. |
| CQ honest source transitions, `Honest classical service calls are not Q coherent calls` | PASS. Once the request register is classical, the key/world/request decomposition is block diagonal. Two ideal P nominees per initiated request cover every public I/E alias, independent of outer-loop length. On good branches real and ideal source handlers agree including termination; bad branches have trace distance at most1. The resulting2/N probability loss per handler is valid even with quantum memory correlated with the measured message. |
| Final verification | PASS. Arbitrary classical transmitted R,c lead to at most one I nominee and one E nominee. Thus the final handler adds2/N. Its later addressed work is outside both private families; local adversarial hashing is already within Q. |
| Adaptive channel telescope, `Adaptive channel telescoping` | PASS. CPTP contraction compares the local channel difference on the IDEAL prefix. Conditional on each measured history block, keys remain independent and local discrepancy has the same bound. Multiplying by block activation probability before summing gives totalQ andq caps, not a square root of activation probability. No estimate is applied to a possibly key-concentrated REAL query state. |
| Partial setup/signing | PASS. Source setup is typed and contributes no private-family public nominations on nonzero S. Noncompletion is absorbing/nonwinning, not an invented failure-return API. Each initiated call has at most two nominees even for every finite prefix of an unbounded/wrapping search. No successful-setup normalization occurs. |
| Single uniform-seed charge | PASS standalone. On S=0 preserve the true ordinary shared RO REAL marginal and allow arbitrary coupling. That branch costs at most1/N. Composition with another zero-seed-conditioned theorem needs explicit common conditioning; one cannot silently subtract charges from separately unconditional statements. |

## Accepted lemma, constants and conventions

**PROVED (reviewed scope).** Let normalized trace distance be D(rho,sigma)=||rho-sigma||_1/2 and N=2^128. On a fixed nonzero seed,

    D(REAL_final, JOINT_IDEAL_final)
      <= min(1, 2Q/sqrt(N) + (2q+2)/N).

Averaging uniform S and assigning distance at most1 to S=0 gives

    Delta_joint,quantum
      <= min(1, 2Q/2^64 + (2q+3)/2^128).

The first term is a state-distance bound for coherent raw public queries. The2q+2 term is a classical CQ rare-branch contribution for initiated source calls plus final verification. The +1 is seed degeneracy. This does not bound forgery in JOINT_IDEAL or certify any quantum signature category. At Q=2^64 the sufficient distance bound caps at1; that vacuity is not an attack or an actual work-factor measurement.

The proof can be written as the exact product identity with real suffix channels and ideal prefix channels, as in my independent derivation. The author's incremental contraction inequality is equivalent. Reversing the roles without separately proving real-state key independence would invalidate the query-mass argument.

## Independent exact controls

`python -I -B control.py` returned exit0 and wrote `CHECKS.json`.

- 65,536 tiny latent worlds give exactly equal full-output programmed and ordinary random-function marginals, conditional on every two-key pair. This includes coincident numeric keys in disjoint domain tags and both output bits.
- Exact rational complex-amplitude calculations checked16 key pairs,17 raw inputs, two-bit complete XOR outputs and an ancilla. Averaged private-support mass is exactly491/2100, equal to eligible mass divided by4. Each local squared Euclidean difference is <=4mu; squared pure-state trace distance is no larger. Average squared trace distance is62179/183750 <=4/4. These are finite inequalities, not formal verification of the general quantum channel theorem.
- The two-step product/channel telescope holds exactly in a marked-phase control using rational amplitudes. After one Grover step the next REAL marked-key mass is1 while the IDEAL mass remains1/4. Thus replacing ideal query weight with an assumed real uniform weight is invalid. The generic marked-oracle control is not the full ordinary-RO source coupling and is not a LULA attack.
- Two distinct classical P nominations among four unused keys give exact CQ discrepancy1/2. An undephased coherent phase handler instead has averaged observable trace distance3/4 for a one-point modification, exceeding the probability-only1/4 charge. This is a contrary toy for quantum signing scope, which the author excludes.
- After conditioning on one classical no-hit, a next key guess is1/3 rather than1/4. The proof correctly avoids such conditioning.
- Two complete images with identical prefix but different tail are perfectly distinguishable by a basis XOR query. Prefix-only coupling is insufficient.
- Two independent private image maps at the same raw point conflict with probability3/4 in the tiny full-output alphabet; disjointness/zero-seed handling cannot be dropped.

## Primary-source comparison and remaining boundaries

I directly checked the [BBBV author paper](https://arxiv.org/pdf/quant-ph/9701001), Section3.1, Definition3.2 and Theorem3.3/proof (printed pages7-8): it supplies the query-magnitude hybrid precedent. The local2/sqrt(N) constant is independently derived using normalized trace distance and full-output XOR unitaries, rather than copied from its different variation-distance convention. No O2H theorem constants or unverified semi-classical-oracle instantiation are needed for this conservative local result.

**OPEN (not supplied by this hop).** Quantum adaptive FORS coverage, hidden-value acquisition with disclosure, and complete source-game QROM composition remain separate obligations. Already reviewed quantum graph/canonical target branches do not substitute for those missing signer terms. Efficient/PPT simulation, formal channel/source verification, tighter specialized O2H losses, actual fixed SHA-256 and a resource/category interpretation remain outside this result. No full QROM total is promoted.

**Final status: ACCEPTED_MANUAL_FINITE_QROM_JOINT_PRIVATE_HOP; FULL_QROM_SIGNER_SECURITY_OPEN.** No source, manuscript, frozen packet, root output or peer file changed.
