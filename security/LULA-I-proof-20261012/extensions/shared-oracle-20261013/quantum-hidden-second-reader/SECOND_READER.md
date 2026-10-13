# Independent decision: dynamic quantum hidden-input overlay

Outcome: **ACCEPTED_MANUAL_FINITE_DYNAMIC_HIDDEN_EVENT_LEMMA; FULL_QROM_OPEN**.

I saved `INDEPENDENT-DERIVATION.md` from the source-specific model before reading root `DYNAMIC-QUANTUM-HIDDEN-DRAFT.md` or the peer quantum-hidden lane. I subsequently reviewed the root draft, re-read its complete current version, and inspected the peer's narrower FORS argument and version note. The reviewed root draft SHA256 is `1b139a3cdd93621c4ebc05f98145807f1bbd23a19d7892440df9d42b3ed0560d`. Source hash remains `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`. Exact subjects are recorded in `REVIEWED-HASHES.json`.

No blocking defect found in the **stronger purified-query-slot and stopped-examiner** argument under the draft's finite classical atomic JOINT-ideal interface. The accepted local statement is

    Pr_HJ[H_final | fixed S!=0]
       <= min(1,(2Q+sqrt(3017))^2/2^128).

Here H_final is a genuine still-legitimately-undisclosed predecessor/secret used in the final **classical** source verification. This does not introduce or count a history of quantum-query hits. It is not a complete forgery probability, fixed-SHA theorem, machine-checked source refinement, efficient reduction or QROM security certification.

## Source/model checklist

| Obligation | Decision and exact condition |
|---|---|
| Fixed ordinary G marginal | ACCEPTED MANUAL using the reviewed typed topological sampler. Chain values are independent coordinate samples, but their position-specific G images are programmed consistently; FORS leaf images are independent of secrets. Private F prefixes and suffixes are consistent. The modified ghost oracle itself is not claimed ordinary or static. |
| Safe surface | REQUIRED and correctly stated. Endpoint/leaf/internal/root images and independent suffix noise may be public; interior chain prefixes, FORS secret payloads and the whole private F table may not be conditioned on or disclosed. |
| No protected-address aliases | VERIFIED for fixed parameters. Source chain239–245 uses full key/chain/position type0 addresses. FORS344–364 and396–408 use height0 plus global leaf index for protected secrets, separating them from internal nodes. Numerical value collisions do not merge coordinates. |
| Predictable FORS selection | VERIFIED. Source601–624 selects route/indices from J and message I/E hashes; sign383–394 returns selected secrets and a fixed-root forest. On S!=0, I has nonzero S in bytes16–31; E is52bytes. Neither can equal a protected raw typed input. |
| Predictable WOTS suffix selection | VERIFIED. Child486–496 is a FORS PK/subtree root in the safe surface. Type7 digest216–236 has a different domain and selects digits without reading hidden predecessors. `sign`264–266 emits X_e; upper child at664 is the fixed subtree root. Honest counter/root integrity is essential; corrupt-cache interfaces are excluded. |
| Monotone suffix-closed Known | REQUIRED and correctly stated. Each completed canonical signature exposes e,...,w−1 per chain; endpoints are initially public. Completed FORS disclosures add selected coordinates. Repetition/restoration cannot erase adversarial exposure. Only directly serialized X_e is insufficient for the invariant. |
| Partial service | ACCEPTED MODEL. Secret buffers remain private until completed return. Noncompletion is absorbing/nonwinning; its mathematical cause is outside-protected metadata, not secret-driven disclosure. This is not an implemented abort response or an OS-totality theorem. |
| Honest services | COMMON CHANNEL. Both comparison worlds evaluate fixed G privately. They emit the same function of shared environment and classical message on the same input state and update Known identically. Real and ghost input states can differ; no claim of identical overall histories is needed. |

## Quantum independence and the dynamic overlay

The continued ghost query unitary depends on residual/nonprotected data and Known values, with no remaining hidden coordinate. The exact full image at a known WOTS input has successor prefix in Known by suffix closure; its remaining128 suffix is independent nuisance randomness. Thus a known-point answer does not accidentally read a remaining coordinate.

Predictably selecting a coordinate set, revealing its values and closing suffixes preserves the iid distribution of the other coordinates. The adversary retains its earlier quantum state unchanged. That state can depend on newly known values after controlled operations, but the other coordinate values remain independent. This argument does not condition on avoiding previous guesses. An analytical flag cannot alter ghost answers, disclosed data or control flow.

The oracle changes **future** answers at new Known points while retaining past quantum memory. This is a deliberately time-dependent ghost; no retroactive overwrite in memory is claimed. Its prior disturbance relative to G was already charged in earlier oracle differences. The root draft correctly rejects a static residual oracle after reveal.

## Purified schedule and amplitude bound

For each ghost input state, the difference-support projector contains only its currently hidden designated inputs. One raw word nominates one protected coordinate. Averaging its independent uniform128-bit value gives support mass at most1/N, N=2^128, without a graph-size multiplier. The full-output XOR-unitary difference has norm at most2 on that support.

Copies of classical coins, measured history and service-work records give common Stinespring dilations. The per-query squared global vector error is at most4/N. Pack common service/local operations between consecutive adversarial coherent-query slots, padding halted branches with an actual identity action. This avoids summing square roots of randomly sparse activations. There are Q slots, and product telescoping gives a vector gap at most2Q/sqrt(N). q imposes a service/history cap but contributes no direct discrepancy because the service and reveal operations are common.

This is stronger than merely a trace-distance bound: the common terminal projector needs the vector inequality to compare square-root success probabilities. The root explicitly supplies that refinement; it is not inferred from trace distance alone.

## Stopped examiner and 3017 candidates

The terminal examiner checks the genuine/undisclosed predicate immediately before a protected classical hash and stops on its first success. Prior to that point, G and the ghost overlay return identical answers: known points are overlaid, non-genuine hidden-domain inputs use the same residual values, and nonprotected domains agree. At the success point it stops before a differing reply. It is therefore a common terminal channel, and its REAL indicator equals the source's H_final event.

For the ghost probability, a separate unflagged overlay-only verifier continues without branching on the analytical equality tests. Its nominated coordinates/inputs depend only on residual tables, safe surface, Known and the candidate state, independently of remaining coordinates. First-hit agreement identifies the same stopped-examiner event. This provides an unconditional candidate union bound; it does **not** assume the survival posterior stays uniform after earlier misses.

Source acceptance tests fix the exact maximum:

    four lower chains: 4*(32*15−240)=960,
    top chains:16*255−2040=2040,
    FORS leaf calls:17,
    total:3000+17=3017.

Rejection decreases the count. Endpoints and already known suffix coordinates are exempt. These are complete hash calls, not compression counts. The final hashes need not add3017 coherent-query slots: the common stopped examiner bypasses a differing reply at its first witness. Its classical candidate count contributes3017/N to ghost probability instead. The peer's separate Q+17 FORS budget is a conservative narrower result and does not refute this common-examiner improvement.

Hence the same projector on the paired purifications gives

    |sqrt(p_REAL)−sqrt(p_GHOST)|<=2Q/sqrt(N),
    p_GHOST<=3017/N,

which proves the accepted local formula. Seed S=0 belongs to the overall joint/source bridge and must be charged once there, not silently re-added to every component.

## Independent executable controls

`python -I -B dynamic_control.py` exited0. A two-bit-output finite model checks **1,024** secret pairs with two coherent queries, retained first-query memory, an intervening Walsh transform and known-value-controlled permutation, and one predictable FORS reveal. Every remaining-B value gives the identical ghost state at fixed revealed A. Averaged second-query hidden mass0.013671875 is below1/32; the coupled global vector gap0.2636429382 is below4/sqrt(32)=0.7071067812. One final ghost genuine-input nomination has probability1/32. The square-root probability gap is0.0004638868, below the vector gap.

Two negative controls passed:

* Static residual answers after a legitimate reveal differ at a now-known point with probability3/4 in the toy two-bit model, although its hidden support is empty. A static-after-reveal bound based only on hidden mass is false.
* A programmed known predecessor while its successor remains classified hidden reveals that successor with probability1. Closing the suffix removes the erroneous hidden event. This confirms the need for closure rather than merely a constant-sum condition.

These are finite discriminators and numerical controls. They do not certify the full source or replace the manual induction.

## Scope that remains open

The local manual model lemma is accepted. Formal source semantics/checking, bounded efficient simulation, physical leakage interfaces, coherent signing, arbitrary cache corruption, quantum adaptive FORS coverage, graph-image/canonical-digest target bounds and full QROM composition remain separate. No 128-bit complete-signer claim or capacity guarantee is licensed. Nothing in this review changes source, manuscript, root/peer drafts or the frozen proof packet.
