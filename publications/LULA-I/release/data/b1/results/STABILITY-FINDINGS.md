STATUS: COMPLETE

# Stability findings, campaign b1

Generated 2026-10-12T20:30:47+00:00. Protocol: `PROTOCOL.md` (including Amendment 1). Times are elapsed milliseconds unless stated; the maximum is the maximum observed latency, not a bound.

Jobs completed: 72; failed or incomplete: 0; contaminated (kept, flagged, excluded from verdicts): 0; gate timeouts: 0.

## Per-cell stability (blocks pooled; LULA I uses two keys, 3 blocks each)

| Cell | Op | Clean blocks / total | Verdict | Block medians min–max (ms) | Spread/mean | Max p99/median | Key effect | Pooled N | Pooled median / p95 / p99 / max (ms) |
|---|---|---|---|---|---|---|---|---|---|
| LULA I prepared 32 B | sign | 6/6 | stable | 3.517–3.667 | 4.2 % | 2.64 | 0.015 | 6000 | 3.592 / 4.131 / 6.318 / 57.262 |
| LULA I prepared 32 B | verify | 6/6 | stable | 0.118–0.119 | 1.3 % | 2.38 | 0.003 | 6000 | 0.119 / 0.130 / 0.204 / 1.870 |
| LULA I prepared 1024 B | sign | 6/6 | stable | 3.532–3.582 | 1.4 % | 1.78 | 0.009 | 6000 | 3.561 / 4.018 / 4.966 / 26.237 |
| LULA I prepared 1024 B | verify | 6/6 | stable | 0.119–0.120 | 0.9 % | 2.52 | 0.004 | 6000 | 0.119 / 0.129 / 0.263 / 4.574 |
| LULA I prepared 65536 B | sign | 6/6 | stable | 3.590–3.673 | 2.3 % | 2.61 | 0.003 | 6000 | 3.637 / 4.136 / 5.623 / 87.917 |
| LULA I prepared 65536 B | verify | 6/6 | stable | 0.145–0.146 | 0.9 % | 2.35 | 0.006 | 6000 | 0.145 / 0.156 / 0.270 / 9.798 |
| SLH-DSA-128f 32 B | sign | 6/6 | stable | 10.698–10.863 | 1.5 % | 1.99 | n/a | 6000 | 10.775 / 11.639 / 16.922 / 125.575 |
| SLH-DSA-128f 32 B | verify | 6/6 | stable | 0.626–0.638 | 1.8 % | 2.37 | n/a | 6000 | 0.631 / 0.778 / 1.083 / 91.704 |
| SLH-DSA-128f 1024 B | sign | 6/6 | stable | 10.772–10.943 | 1.6 % | 2.37 | n/a | 6000 | 10.833 / 11.990 / 20.132 / 122.242 |
| SLH-DSA-128f 1024 B | verify | 6/6 | stable | 0.622–0.644 | 3.5 % | 1.85 | n/a | 6000 | 0.633 / 0.804 / 1.107 / 113.781 |
| SLH-DSA-128f 65536 B | sign | 6/6 | stable | 10.711–10.929 | 2.0 % | 1.60 | n/a | 6000 | 10.837 / 11.569 / 15.924 / 122.818 |
| SLH-DSA-128f 65536 B | verify | 6/6 | stable | 0.686–0.698 | 1.7 % | 2.10 | n/a | 6000 | 0.691 / 0.858 / 1.146 / 115.934 |
| SLH-DSA-128s 32 B | sign | 6/6 | stable | 230.750–234.761 | 1.7 % | 2.04 | n/a | 1200 | 232.165 / 266.828 / 330.254 / 605.569 |
| SLH-DSA-128s 32 B | verify | 6/6 | stable | 0.227–0.232 | 2.1 % | 2.23 | n/a | 1200 | 0.230 / 0.266 / 0.460 / 0.800 |
| SLH-DSA-128s 1024 B | sign | 6/6 | stable | 229.707–233.514 | 1.6 % | 1.45 | n/a | 1200 | 231.764 / 264.728 / 324.011 / 619.127 |
| SLH-DSA-128s 1024 B | verify | 6/6 | unstable | 0.225–0.232 | 2.8 % | 3.37 | n/a | 1200 | 0.228 / 0.278 / 0.494 / 1.600 |
| SLH-DSA-128s 65536 B | sign | 6/6 | stable | 228.563–233.941 | 2.3 % | 1.48 | n/a | 1200 | 231.175 / 260.303 / 312.087 / 591.605 |
| SLH-DSA-128s 65536 B | verify | 6/6 | unstable | 0.294–0.299 | 1.8 % | 3.43 | n/a | 1200 | 0.297 / 0.345 / 0.650 / 10.973 |

## Fresh process and cache loss (LULA I key 1, 32 B)

- Fresh process, clean jobs N = 15 (windows: [1, 2, 3]): load median 5.696 s (range 5.561–6.091); first sign median 3.580 ms; paired load plus first sign median 5.700 s (range 5.565–6.094).
- Cache loss, one first signature per independent process: window 1: 331.837 s; window 2: 337.563 s; window 3: 330.049 s. Each value is a single observation; three observations do not support a distribution estimate.

## Reading this file
- *stable* / *unstable* / *inconclusive* are defined in `PROTOCOL.md`; a cell is judged on uncontaminated blocks only.
- *Key effect* is |median(key 1 blocks) − median(key 2 blocks)| over their mean, LULA I only.
- Nothing here is a worst-case guarantee, a security-normalized ranking, or a statement about other machines.
