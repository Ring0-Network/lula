# Security matrix (provisional; written 2026-10-12 by the executor, unreviewed)

Rule used: a row enters the security-normalized cohort only if the reduction that applies to the exact instantiation is
identified and read. Names, hash widths and occupancy exponents are not evidence. Labels: [read] read in a file this
session; [recalled] recalled or inherited, not re-read here; [unverified].

| Row | Reduction / source | Q, T, qH budgets | Classical level supported | Capacity | Persistent trusted state | Rollback / detection | Verdict |
|---|---|---|---|---|---|---|---|
| SLH-DSA-SHA2-128s / 128f, OpenSSL 3.5.7 | FIPS 205 and its security analysis [recalled; M2 read FIPS 205 sets and SP 800-230 ipd] | designed for 2^64 signatures per key [recalled] | category-1 level claimed by the standard; the provable-bound reading of the same sets gives 123.2 bits at 2^40 per M2 [read in M2 REPORT] | structurally 2^64 | none | stateless: restoring state changes nothing | eligible, with the two readings stated (standard claim and proof bound). Conformance shown by `openssl` itself and by M2's 18/18 ACVP checks on the same sets (M2's engine, not this adapter) |
| S42 (h42 d7 k20 a8 w16) | Kudinov–Nick parameter search plus the SPHINCS+ bound | 2^40 | 128.00 / 127.36 / 123.2 depending on the reading [read in M2 REPORT] | 2^40 | none | stateless | not measured in this campaign (M2 results are inherited, other core, loaded); not standardized |
| Kudinov–Nick 4,036 B | ePrint 2025/2203 [formula checked by M2; not re-read here] | 2^40 [recalled] | [unverified] for the Go adapter: the adapter is third-party code, not the authors' | 2^40 [recalled] | none | stateless | provisional; excluded from the normalized cohort until adapter conformance and the exact reduction are checked |
| Kudinov–Nick 3,952 B (`KN-3952-RECON`) | same paper; row W+C, h44 d4 a16 k8 w256 l16 S=2040 [read in the paper text copy] | 2^40 [recalled] | [unverified]: the reconstruction is ours; the paper notes that FORS+C security uses the generic attack approach, and this row uses plain FORS | 2^40 [recalled] | none | stateless | provisional; own reconstruction, labeled; excluded from the normalized cohort until the reduction for this exact row is read |
| SHRINCS (author C, B32 parameters) stateful part | draft BIP and author code at the pinned commits [read headers only] | | the stateful part is a counter-based scheme: security needs a never-reused counter | HSF = 210 stateful signatures [read in `include/constants.h`] | the counter | silent rollback reuses a counter: a second message signed under a used index leaks material; the harness scenario `restored` reproduces the state restore but no attack was run | excluded from the normalized cohort: capacity far below 2^40 and rollback is unsafe by design |
| SHRINCS fallback (stateless) | same | | [unverified]: the B32 stateless component's reduction was not read | HSL = 32: the stateless hypertree has 2^32 leaves [read in `include/constants.h`], below the 2^40 filter; PORS+FP with K = 11, B = 17 | none | the fallback does not undo leakage from earlier stateful signatures | provisional; capacity and level unverified |
| LULA I | the reference bound of the signer plus the rollback theorem in `PROOF_AUDIT.md` [read by the kickoff author, not re-checked here] | 2^40 queries [as stated in the paper] | conditional: the theorem's reference bound is a premise. Byte equality and measured timings do not establish it | 2^40 per the paper | none required for security; the cache is acceleration state | honest-restoration model; the paper's tests show equal bytes across prepared, absent and restored caches | provisional; kept out of the security-normalized ranking unless the bound is accepted |

## Scope notes

- Faults, side channels and atomicity of persistence are out of scope for every row.
- Quantum level is not assessed here.
- Nothing in this file is an attack result. No rollback attack was run against SHRINCS or LULA I in this session.
- Capacity is derived structurally where the sources give the tree heights; `2^40` signatures were never executed.
