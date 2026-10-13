# Refined root numerical crosscheck

**PASS_ALL16_ROOT_REFINED_ROWS_FIELDS_AND_EXPONENTS.** Both root refined outputs agree with the preserved240-digit independent CANDIDATE-BOUNDS.json, SHA256 `b1e7305710268af6a71045449724fc5b7eab46057f1de402acd068c3a070607d`.

| Current artifact | SHA256 |
|---|---|
| Refined theorem | `d28e99570c0b6819f7a45169882252ffedc6e31cfad150751f7084a9fdea02f1` |
| Refined calculator | `4f06f80befae967479a582fb644d4d24bcb40b9051324709f529abcf683a8a81` |
| Refined Qq32 output | `24c6e770835ba269f12ebcb42b1e8c88e21bc498503ecc98ba0b4e1fe85da33e` |
| Refined Qq64 output | `d635fbed31532e66e3be5a8681ef0dad1a643f9c46250cb7be6a2c2ee526fe31` |
| Conservative base calculator | `2e0849d60bde394397ef917d667d8a547c910868b571157d6a26f8140eb338cd` |
| Conservative theorem | `94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607` |
| Base Qq32 output | `95588a3415ca5c328f3a7107cdb47a97f4319f4f7f7cfe842ab8fc4ba8a44593` |
| Base Qq64 output | `fed0563b108525cf18a5569b10b87e8cab994f15cd236faa7ca44a4ffb188a59` |

Run `python -I -B check_refined.py`; exit0. All sixteen q/Qq rows pass96 numeric-field comparisons (HJ union, alias bound, vector gap, event-specific total, conservative total and minimum) and64 exponent comparisons. All hashes are checked before and after reading. Params, q/Qq integers, status fields and category-unestablished labels match the pinned scope.

The root calculator evaluates at220 decimal digits **from serialized45-significant-digit components**. Its qualifier explicitly rejects a formally directed-rounded interval claim. Agreement with the independent240-digit dataset is checked at1e-43 relative tolerance, with2e-12 absolute allowance for stored floating exponents. No claim is made that220 internal digits recover precision absent from serialized inputs.

For Qq=2^32, refined exponents at q=2^40,2^41,2^44 are57.6833598693088,56.8732751077250,31.5210538618119. For Qq=2^64 all eight sufficient totals cap1. These are probability-envelope exponents at named budgets, not work factors, attacks, timing data or category certification. The old conservative outputs and all historical rare-manifest files remain unchanged.

This crosscheck reads existing outputs; it does not rerun root calculators, previous proof/control suites, builds, cache operations or benchmarks. ROOT-REFINED-CROSSCHECK.json stores every field's error and current pins. Any subsequent subject change needs a new receipt.

**Outcome: ACCEPTED_CURRENT_REFINED_FINITE_MODEL_ARITHMETIC; CATEGORY_NOT_ESTABLISHED.**
