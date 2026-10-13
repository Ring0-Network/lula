# Runs and isolation receipt

Only this `numerics` output directory was written. Original scripts, Rust source, benchmarks, and manuscript were read only. No other agent's proof/report was read before the independent derivation was saved.

| Command | Result | Evidence |
|---|---|---|
| `python -I -B bounds.py` | exit 0 | Eight q rows; exact count checks; two toy confidence-interval checks; `bounds.json` / `bounds.md` |
| `python -I -B bounds.py` after strengthening precision comparison to compare mpmath values rather than rounded float bits | exit 0 | Relative 160-vs-220-digit error below 1e-90 in every row |
| `python -I -B crosscheck_originals.py` initial attempt | exit 1 | Isolated mode removes the local module path, causing `ModuleNotFoundError: bounds` |
| `python -I -B crosscheck_originals.py` after loading local module by explicit file path | exit 0 | `ORIGINAL_CROSSCHECK.json`: all q rows; four independent count routines agree on actual-parameter pairs |

The original R6 model's q=2^64 assertion failure is captured as a model limitation in the crosscheck JSON, not a failure of the independent numeric script. No worker pool, benchmark launcher, cache builder, external prover, or signature signer was run in this numerical subtask. Python loops here use one thread. Source hashes in `ORIGINAL_CROSSCHECK.json` identify the exact six original inputs inspected.
