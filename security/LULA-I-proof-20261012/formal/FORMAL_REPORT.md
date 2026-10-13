# Formal artifacts and exact scope

**PROVED:** seven declarations in `LulaLemmas.lean` checked locally with Lean 4.28.0 and independently through AXLE's lean-4.28.0 environment. No source placeholder, `native_decide`, custom axiom or admission was added. This is a small abstract model and combinatorial proof package; no proof of the Rust signer or its EUF-CMA bound is claimed.

| Declaration | What is checked | Local transitive axioms |
|---|---|---|
| `Lula.sum_monotone` | Pointwise ordered lists have ordered sums | `propext` |
| `Lula.fixed_sum_antichain` | Pointwise order plus equal natural-number sums implies equal lists | `propext`, `Quot.sound` |
| `Lula.restored_cache_same` | Two states satisfying exact reference-outcome consistency give equal outcomes | none |
| `Lula.adaptive_transcript_equal` | Equal response oracles give equal finite adaptive histories | `Quot.sound` |
| `Lula.adaptive_restoration_equal` | An arbitrary history-dependent restoration selector preserves the adaptive transcript when every selected cache is consistent | none |
| `Lula.no_changed_success` | A successful-return safety hypothesis excludes a changed successful result | none |
| `Lula.equal_or_first_divergence` | Equal lists or first differing optional element after an equal prefix | `propext` |

**PROVED / scope:** `consistent` means all reference and cached completion outcomes coincide. `outputSafe` is a separate stronger hypothesis on the implementation. It is not proved by `no_changed_success`. In particular `Option.none` is only an abstract absence-of-success outcome; a finite model cannot distinguish a returned abort from a nonterminating grind by itself. The real `u32` search may wrap or panic depending on build semantics. Reference/cached termination correspondence for honest states needs the code argument; arbitrary corrupted states are excluded.

**PROVED (manual coupling, conditional):** fix the key, random oracle and adversary's coins; allow only signing outputs and opaque atomic restore handles, without cache bytes or timing. If every restored state is consistent, `adaptive_restoration_equal` identifies the completed signing histories under any finite adaptive query sequence. Therefore the same adversary's fresh-message acceptance event is unchanged. Averaging over the common coins preserves its probability: `Adv_cached = Adv_reference`, so the transfer loss is `δ=0` for this interface. This is a transfer of a reference bound, not a proof of one. No formal measure-theoretic probability theorem is encoded in Lean here.

**CITED / COMPUTED environment:** local WSL Ubuntu-24.04, Lean binary `/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean`, version 4.28.0 / commit `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`, Mathlib commit `8f9d9cff6bd728b17a24e163c9402775d9e6a365`, manifest SHA-256 `a89b59a9c917d113c32b931cc82a6b919d50be80ec1a701612f571bcd34f245a`. The existing environment was reused; no toolchain or package installation was performed. `lean-local.json` records exit 0, source hash and all `#print axioms` output.

**PROVED / remotely checked:** `axle-check.json` records a second check of the exact narrow-import source, with `ignore_imports=False` and matching source SHA-256. Its provider emits advisory messages recommending aggregate Mathlib imports, but no Lean errors or warnings. Earlier exploratory checks replaced imports by the provider default; only the final explicit-false-import run and the local pin check support this exact-source verdict. Tool version `axiom-axle` 1.5.0; server executor/digest metadata is preserved in the response. No private cryptographic source or credentials were transmitted.

## Aristotle independent antichain proof

**PROVED / independently checked:** the user-authorized Aristotle project `8088c406-8395-494b-a4d4-7f8642dc0bc8` received only the abstract antichain statement and hint. It returned `IndependentLula.lean` with the identical declaration and no new assumption. AXLE `check` and `verify_proof` both accepted the returned source (`aristotle-independent-recheck.json`), and `#print axioms` gives `{propext, Quot.sound}`. The comparator's placeholder statement is an input template only; the accepted candidate contains no placeholder.

**COMPUTED (local import adaptation):** `IndependentLulaLocal.lean` replaces aggregate `import Mathlib` with the same available narrow imports used for the other file, and replaces the unavailable generic lemma alias `le_rfl` by `Nat.le_refl _`. Its declaration is unchanged. This adaptation is separately locally checked and recorded in `aristotle-local-check.json`; it is distinguished from the exact original returned file. The downloaded archive is preserved as `aristotle-returned`; its name does not imply a directory. Aristotle SDK version 2.1.0.

## EasyCrypt

**PROVED (model):** `CacheModel.ec` has three checked lemmas: `consistent_equivalence`, `abort_or_reference`, and `successful_response`. EasyCrypt `r2026.07-1-g87b6f8b` runs from the existing `/root/.opam/ec` WSL switch; configured solvers are Alt-Ergo 2.4.3 and Z3 4.8.12. Final source check, exit status, absence of critical diagnostics, checker/solver/config hashes are in `ENVIRONMENT.json` and `easycrypt-final.log`. Operations `reference` and `valid` are abstract symbols, without axioms asserting any cryptographic property. No admitted or aborted proof appears.

**ASSUMED — model/code boundary:** the modeled invalid-cache branch returns `Abort`. This is a specification for a guarded wrapper and is not the actual Rust corruption handling. The real Sign trusts authentication paths, roots and any accepted cached counter. The independently recorded native control produces a different valid same-message signature for a noncanonical accepted counter. Thus the EasyCrypt theorem cannot justify a universal abort-or-recompute claim about the actual library. Only consistent-cache equivalence has a matching honest-source argument. This development contains no PRF, random-oracle or EUF-CMA reduction and no QROM proof.

## K operational model

**UNCHECKED:** `CacheSemantics.k` is a small boundary specification with honest, guarded and trusted modes and explicit `pending` for an unfinished reference computation. It distinguishes invalid-state rejection as a proposed guard from trusting arbitrary cache-influenced results. K tools were absent from the inspected actual Ubuntu WSL executable path; the historical skill's Debian environment is not installed. No global installation/configuration change was attempted.

Expected checks in a K installation: `kompile CacheSemantics.k --backend haskell --main-module CACHE --syntax-module CACHE-SYNTAX`, followed by `krun` of explicit small commands. None ran here; no K parse, reachability or invariant proof is claimed.

## Remaining proof obligations

**OPEN:** selected-counter hash security, one-fixed-child-message WOTS security, exact addressed chain/compression assumptions, shared-SHA input-domain hybrid, lazy honest-graph tree extraction, totality/search-failure probability, cache-exposure auxiliary-information simulation and complete hybrid composition. `QUANTUM.md` gives the exact primary-source formulas and the missing QROM embeddings. A checked antichain or conditional simulation does not settle any of these cryptographic terms.

**PROVED (delivery boundary):** this lane wrote only the `formal/` output directory. It ran no timing campaign, generated no full-size key/cache, changed no cryptographic implementation or manuscript, and uploaded only small abstract mathematical source to the two authorized Lean services.
