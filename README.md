# LULA proofs and tests

Reproducible mathematical components, numerical checks and public verification vectors for **LULA I**, part of Ring0 Labs' hash-based signature research family.

[Paper on Zenodo](https://doi.org/10.5281/zenodo.23353281) · [Research note](https://lugel.org/blog/lula)

## Contents

| Directory | Purpose |
|---|---|
| `proofs/lean/` | 38 supporting statements, pinned Lean/Mathlib project, statement inventory and axiom checker |
| `proofs/easycrypt/` | 9 supporting lemmas, pinned tool/solver requirements and executable checker |
| `models/` | Finite-binomial coverage, guarded classical probability envelopes and the fixed baseline QROM envelope |
| `verifiers/` | Independent Python signature verifier |
| `tests/` | 53 public cases referencing 9 signatures, 6 messages and 3 public keys; rejection/equality checks and numerical fixtures |
| `scripts/` | Test entry point and tracked-file publication policy |

## Run Python checks

Use Python 3.13 and the pinned dependency:

```sh
python -m pip install --require-hashes -r requirements.txt
python -I -B scripts/check.py
```

The checks verify saved public signatures, selected modified-message/signature/key rejections, exact wire sizes, and saved same-key/message equality across cache scenarios. Numerical checks cover signing-query caps 2^24, 2^30, 2^38, 2^40, 2^41, 2^44, 2^50 and 2^64, including independent finite-probability calculations. They do not generate signing keys, rebuild caches or run benchmarks.

## Check formal sources

The Lean project pins `leanprover/lean4:v4.28.0` and an exact Mathlib revision. With Elan/Lake available:

```sh
cd proofs/lean
lake update
lake exe cache get
lake build
python -I -B check.py
```

The checker compiles all 38 statements and checks their printed axiom sets against `{propext, Classical.choice, Quot.sound}`. It rejects admissions and added axiom declarations. An existing matching Mathlib checkout can be selected with `--mathlib-project`.

The EasyCrypt checker requires the exact installed EasyCrypt, Why3 and Z3 identities in `proofs/easycrypt/toolchain.json`, together with a configured Why3 prover. From the repository root:

```sh
python -I -B proofs/easycrypt/check.py
```

Use `--easycrypt`, `--why3`, `--z3` and `--why3-config` for installed tools outside PATH. These checkers do not install or reconfigure tools. An unavailable prerequisite is reported as unchecked, with a nonzero exit status. EasyCrypt checks depend on the pinned EasyCrypt/Why3/SMT trusted stack. GitHub Actions runs the Python and Lean checks; EasyCrypt has a separate explicit checker.

## Scope

The formal sources prove supporting mathematical statements. They do **not** mechanize the complete signature game, establish a Rust refinement, or prove full-signer 128-bit security, category 1 or signing capacity. Numerical probability bounds and per-candidate coverage exponents are not attack work factors. The rational classical certificates are exact; the mpmath coverage/envelope evaluations are high-precision numerical calculations, not directed-rounding proofs. Saved cache-equality cases are finite observations. The paper's rollback-security transfer remains conditional on its stated reference-signer and honest-cache assumptions.

## Repository policy

Only maintained proof sources, executable checks, their required fixtures, configuration and this README belong here. Hypothesis notes, draft derivations, editorial reviews, handoffs, audit logs, research snapshots, local paths, private keys and cache files stay in the local research workspace. Run `python -I -B scripts/repository_policy.py --commit` to check tracked files and maintainer identity; the policy supplements `.gitignore`.

Maintainer commits use **ring0code** as both author and committer, without coauthor trailers. Keep changes small, run the affected checkers, and preserve the scope of every statement. Do not convert an unavailable or failing check into a successful result.

The verifier and reused model software retain Apache-2.0 terms; public verification vectors retain CC BY 4.0 attribution. See [LICENSE](LICENSE) and [NOTICE](NOTICE) for the exact scope. No new license grant is inferred for the formal proof sources.
