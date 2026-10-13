# Root numerical cross-check

Outcome: PASS_ALL_16_ROOT_ROWS_AND_CLASSICAL_TERM_LEDGER.

`python -I -B crosscheck_root.py` returned exit 0. Independent interval results were saved before inspecting root output. All eight q values match at each of Q_H=2^64 and 2^128; each root per-term decimal matches the independent result within its serialization precision. Exact integer coefficients 6Q_H+3q+6243 match in all rows.

At Q_H=2^64 the total caps at one for q=2^50 and 2^64. At Q_H=2^128 it caps at one for every tested q. The negative-log totals are upper-bound exponents, not work factors; root leaves classical level 1 uncertified and full QROM/efficient primitive reductions unresolved.

Root identities and all relative-error checks appear in ROOT-CROSSCHECK.json. No root file was changed.
