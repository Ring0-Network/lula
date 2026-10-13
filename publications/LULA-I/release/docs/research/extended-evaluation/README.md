# Extended evaluation and reproducibility record

The manuscript presents the mechanism, its assumptions, and the principal experimental results. This directory preserves the detailed material that accompanies those results without turning the article into an execution log.

`source/` is the frozen, contact-free pre-cleanup source record. It retains the complete original tables, captions, numerical conventions, historical cohorts, binary identities, protocol diagnostics and claim map. It is an extended record, not the current manuscript. The current manuscript is in `paper/` at the bundle root.

## What remains in the article

- Six-block prepared signing and verification medians and p99 values, by message length, with timed-call counts and workload/backend limitations.
- A short paragraph reporting complete one-worker key generation with cache preparation, paired restart measurements from fifteen processes, and three individual first signatures after cache loss.
- A separately identified four-row snapshot of auxiliary SHRINCS and compact implementations on 32-byte inputs.
- The fixed wire format and verification-work accounting, and three FORS+C component-model reference points.

## Extended material here and elsewhere in the bundle

The frozen source record contains all 21 previous tables, including full minimum/median/p95/p99/maximum distributions, block variation, memory peaks, byte decompositions, branch schedules, prior sessions and fixed-fixture replay. It also preserves the complete analytical scenario grid. None of these measurements or source values was changed by the manuscript cleanup.

Raw observations, process records, gate/sampler logs and public verification vectors remain in `data/`. Experimental protocols, build/dependency pins and analysis instructions remain in `docs/` and the bundle README. Controller logs, completion markers, hash manifests, exact operational timestamps and invocation commands belong to this reproducibility record.

Run `python -I -B code/models/verify_paper_tables.py` after retained-data analysis and model checks. Its output separates the six current article tables and 37 checked rows or fields from the 21 archived tables and their 141 previous checks. Archive checks must not be presented as the current article's table count. The current article has no execution-procedure section, evidence manifest, public-deposit placeholder or author TODO.

These records preserve the distinction between sampled observations, analytical models, published parameter targets and unproved security assumptions. They establish no new experiment, cryptographic reduction, public deposit or worst-case latency guarantee.
