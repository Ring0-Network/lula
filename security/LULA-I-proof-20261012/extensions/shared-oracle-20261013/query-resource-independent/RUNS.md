# Independent threshold reproduction

Run locally with the installed Python 3.13 runtime; no dependencies or installations are required:

    C:\Users\angel\AppData\Local\Programs\Python\Python313\python.exe -I -B thresholds.py
    C:\Users\angel\AppData\Local\Programs\Python\Python313\python.exe -I -B crosscheck.py

Both commands exited 0. The second command imports and reexecutes the primary independent calculation, then adds exact affine inversions and square-root precision checks. Its full stdout is `run-output.txt`. `THRESHOLDS.json` and `CROSSCHECK.json` contain script/data/input hashes; rerunning changes only the elapsed time and resulting data digest, not any thresholds.

The main run uses 1024-bit outward square-root intervals. It certifies 32 adjacent integer crossings across eight signing caps and four accepted bound expressions. The cross-check recovers eight classical thresholds by exact affine inversion, verifies all 64 endpoint comparisons at 128-bit precision, and all 64 again at 256-bit precision. The 64-bit precision probe reports 30 inconclusive endpoint comparisons without guessing. `PRECISION-64.json` also preserves the earlier equivalent probe output.

Read-only inputs were the three reviewed theorem files and the older independent FORS occupancy interval dataset. All writes were confined to this directory. No new root query-threshold output was read, no real source-valid forgery construction was attempted, and no source/manuscript/runtime/parameter file was modified.
