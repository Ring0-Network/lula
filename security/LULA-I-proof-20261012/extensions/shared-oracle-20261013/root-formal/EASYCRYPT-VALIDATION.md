# Checked fixed candidate-list bounds

**CHECKED.** `SeedGuess.ec`, SHA-256 `f4bb3f768cf63722a8f108708617f6d31cc264bc19fad13a1e148c2284206b8f`, passes the pinned `check_ec.py` command with exit 0. The helper explicitly selects Z3 and disables target verification caching. The successful exact statement text, command, diagnostics, checker binary/configuration hashes and direct library hashes are recorded in `EASYCRYPT-VALIDATION.json` and `easycrypt-current.json`.

Checked declarations:

1. `uniform_atom_bound`: for n>0, each atom of the uniform interval `[0..n−1]` has probability at most 1/n.
2. `one_seed_hit_bound`: for a fixed candidate list C, its membership probability is at most `size(C)/n`.
3. `two_seed_hit_bound`: for independent uniform keys and fixed prefix/suffix lists, either-key hit probability is at most `(size(prefixes)+size(suffixes))/n`.
4. `key_blind_game_bound`: the corresponding `KeyBlind.sample` procedure satisfies the same pHoare bound when its arguments equal those fixed lists and n.

**Preserved statements.** The original assumptions remain n>0 and fixed candidate-list inputs. No axiom, admit, abort or weakened statement was added. The final proof explicitly rewrites **real** distributivity using `RField.mulrDl`, simplifies the interval's weight from n>0, and parenthesizes the intended complete numeric bound in the pHoare syntax. Unqualified `mulrDl` selected an inapplicable rewrite; the parentheses correct parsing without changing the mathematical bound.

**Installed trusted stack.** EasyCrypt `r2026.07-1-g87b6f8b`; Why3 1.8.2; selected Z3 4.8.12. Direct imports are `AllCore`, `List`, `Distr`, `DInterval`. Official lemmas used include `dinter1E`, `mu_mem_le_mu1`, `le_dprod_or`, `weight_dinter`, and the integer/real algebra interfaces. Their distribution and logical foundation are trusted imported mathematics. No full standard-library rebuild or transitive axiom-minimization was performed; the JSON receipt records that limit rather than claiming an axiom-free foundational development.

**Boundary.** This file checks the finite probability/game lemma after the lists have been chosen independently of the unused ideal keys. It does not encode LULA's actual SHA input formats, the source root/signature computation, continued-after-Bad noninterference, setup normalization, adaptive coverage or full EUF-CMA security. Using it for the source-bound joint privatization argument still requires the separately stated manual coupling and interface restrictions.
