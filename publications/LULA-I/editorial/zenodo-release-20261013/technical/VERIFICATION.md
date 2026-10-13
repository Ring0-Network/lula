# Independent technical check of the requested final additions

**ACCEPT the proposed paragraphs, with the precise “omitting the retained cache” wording.** This review writes only its own editorial technical directory and makes no manuscript, source, archive, dataset or private-proof change. It performs no benchmark, signing, key generation, forest/cache construction or upload. It does not retune parameters, introduce a configuration table or infer new security bits.

## Current source subject

- `release/code/lula1/src/lib.rs`: SHA256 `ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210`.
- Pre-edit `LULA-I.tex`: `3ef61931c2feb57e05ae28171a693801c131a9b1edee59956e477384985d27c8`.
- Pre-edit `stability-results.tex`: `7bf5af933b82d89dab647d784d07598276c0c56693dc795001e4da1aec9671b7`.
- `operating-model.tex`: `9b81563bdee219dd741cc1db49270437290ef2ba9ca07721b153c62da2885add`.

## Source and arithmetic obligations

1. **COMPUTED:** The level-major top-tree payload is `16(2^22−1)=67,108,848` bytes, exactly 64 MiB minus 16 bytes. Its `2^21` 32-bit counters add `8,388,608` bytes, exactly 8 MiB. The combined logical payload is `75,497,456` bytes, exactly 72 MiB minus 16 bytes. This is not a peak-RAM or serialized-fixture-size claim. Source `Subtree` stores all nodes at lines 281–307; `LayerCache` stores the node vectors and counters at lines 450–454. Paper lines 387–392 already state the matching total and overhead exclusion.

2. **PROVED by source comparison, within the existing honest-cache/partial-function theorem:** Current signing supports a complete stored top cache or recomputation when that layer is absent/ignored. Its output fields, verifier and parameter set do not change. The cached counter is the canonical first accepted row for the genuine child; absent-cache signing calls the same canonical `grind` and reconstructs the same tree. Paper lines 309–335 already give the termination-equivalence and conditional reference-bound transfer. Removing storage supplies no new primitive hardness or full-security claim. The unchanged byte accounting gives 5,720-byte signatures.

3. **COMPUTED:** Every one of the `2^21` top leaves costs `16·255+16+5=4,101` suffix compressions to derive and compress its WOTS public key. The Merkle inner nodes add `2^21−1`. Thus the additional full top-tree work is `2^21·4101+(2^21−1)=8,602,517,503` compressions per uncached call. The canonical top counter search is additional. Its number of trials is not fixed by this deterministic arithmetic; it remains conditional on termination. No new seconds/latency estimate is supplied.

4. **PROVED by direct allocation path:** `Signer::compute_subtree` at lines 479–483 creates every leaf and calls `Subtree::build`; lines 291–307 retain every tree node in a `Vec`. Uncached signing calls this path at lines 641–644. It therefore still materializes a temporary tree of height 21. Avoiding a persistent cache does not establish low peak RAM, zero RAM or streaming behavior.

5. **Important wording precision, resolved in the proposed text:** `use_cache=false` at line 635 ignores the cache for lookup; it does not deallocate any cache already stored in `Signer.cache`. A claim of saved retained memory must concern omitting/removing that retained cache, not merely passing that flag. The `cache` field is public at line 461, and the source has an absent-layer `None` path. No experiment or source change is needed to distinguish these behaviors.

6. **ASSUMED design condition / OPEN implementation work:** Partial-node, counter-only, node-only or streaming variants can be discussed as future strategies if their lookup/recomputation preserves the same canonical signing function and honest-cache integrity conditions. The current source and supplied measurements do not implement or evaluate those intermediate regimes. The paragraph explicitly does not present them as implemented or measured. Existing allocation and work formulas cannot be transferred to a streaming variant without deriving that variant's own resource accounting.

## Parameter changes and the component model

**PROVED within the stated uniform-selection model, not the actual full signature game:** Fix a positive signing-query count `q`, FORS height 9 and 17 real trees. The paper's model uses `rho=2^(−h)` and `N~Bin(q,rho)`, with per-candidate probability `2^(−9) E[(1−r^N)^17]`, `r=511/512`. Lowering only the top height lowers total `h`, increasing `rho`. Coupling the Bernoulli occupancy trials by shared uniforms makes the new occupancy at least the old one. Since `(1−r^N)^17` is increasing in `N`, the modeled coverage probability increases. The corresponding Poisson approximation has the same monotonicity by adding an independent nonnegative Poisson increment. This does not establish a distribution theorem for the deterministic signer or a full-security decrease of a quantified size.

**PROVED from the parameter definitions:** Reducing top height also changes routing and the top authentication path length; with other parameters fixed, each removed height level removes 16 path bytes, so one cannot retain the old 5,720-byte accounting for a retuned scheme. Redistributing height while preserving total `h` leaves this particular occupancy parameter unchanged but changes subtree/preparation/storage/online-work costs and addresses. The old partial-function and primitive-security analyses do not by themselves provide a new concrete reference bound. The proposed paragraph therefore requests fresh security/performance analysis and supplies no retuned row or security-bit number.

## Privacy and repository reference

**COMPUTED by narrow live-source search:** The exact CPU model and OS occur in the included `stability-results.tex:2`, not in the other live TeX inputs or abstract metadata. Replacing its hardware sentence with the supplied generic host/32 GiB sentence removes those identifiers while retaining processor pinning as a methodological statement. The remaining non-isolation and unmatched-backend qualifications do not reveal an exact model or OS and should remain because they limit the performance comparison. This is a paper-text privacy edit, not a claim that historical campaign protocols lack hardware provenance.

**CITED live observation:** An anonymous read-only request to the intended [project repository](https://github.com/Ring0-Network/lula) returned HTTP 404 on October 13, 2026. The requested neutral repository label can be inserted without claiming verified availability. Public deposit or repository access must not be inferred from the existence of local ZIP files. This observation does not authorize or perform any remote change.

The addition preserves the accepted mechanism-paper scope: honest-cache transparency and conditional rollback transfer, not a full 128-bit/category claim. No original full-security objective is declared complete.

## Independently computed optional height illustration

The subsequent requested analytical illustration was evaluated independently by `height_illustration.py` at **600 and 900 decimal digits**. All 160 reported digits agree between precisions. No source parameter, timing sample or manuscript was changed. The JSON binds the unchanged release source.

For `q=2^40`, keeping four lower height-5 layers, FORS height 9 and 17 real FORS trees:

- Baseline top height 21 / total height 41: exact Binomial exponent `132.5634199441180315178825876057856101356983926174068987501711230325`; Poisson exponent `132.5634199440962571136005610457167613260067191770443047766383080286`. Both display **132.6**.
- Analytical top height 20 / total height 40: exact Binomial exponent `125.9025303847814609692006569771198492992763563737411219515998237000`; Poisson exponent `125.9025303847512243590229737153447637219782991576893298619431886435`. Both display **125.9**.

The previously displayed `q=2^41,h=41` row has the same Poisson mean as the analytical `q=2^40,h=40` row, but its exact Binomial exponent is `125.9025303847663426641118102843878835666278836845387515484469873604`. The two exact Binomial distributions must not be identified merely because their displayed values agree.

Integer arithmetic gives node payload `33,554,416` bytes (32 MiB minus 16), counters `4,194,304` bytes (4 MiB), total `37,748,720` bytes (36 MiB minus 16), and signatures `5,704` bytes. The optional cold-tree cost is `4,301,258,751` suffix compressions, plus the top counter search. The new payload is not exactly half the old payload: it is half minus eight bytes.

**ACCEPT as a labeled analytical illustration only:** these arithmetic and component-model statements require no already-proved full reference-signer bound. They do require preserving the uniform-selection model premise and the explicit unevaluated/unimplemented status, and cannot certify capacity or a full-signature security level. Changing “fixed throughout this paper” to “single evaluated parameter set” is then necessary to keep the construction section consistent with the separate illustration. A new retuned configuration table, fresh timing estimate or security-bit label is neither needed nor supplied.
