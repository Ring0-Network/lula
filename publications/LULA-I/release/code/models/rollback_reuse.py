"""Uniform-encoding one-time chain-reuse proxy with exact finite counts.

For a fixed reused chain transcript, this model counts target encodings below the
coordinatewise disclosed maximum. It assumes uniform encodings on the specified
constant-sum layer. Fixed-seed transcript samples and a toy brute-force control
exercise the model. This is not an executed SHRINCS forgery or a reduction for the
full SHRINCS implementation. Reported bit fields describe this per-encoding proxy,
not whole-scheme security. Numerical functions and experiment definitions are
unchanged. Default output is generated/models/rollback_reuse.out.json.
"""
import itertools
import json
import math
import random
import statistics

SEED = 20261009


def count_bounded(d0, ub, cap=None):
    """#{b in Z_{>=0}^v : sum b = d0, b_i <= ub_i}; optional per-chain cap (chain length - 1)."""
    v = len(ub)
    u = [min(x, cap) if cap is not None else x for x in ub]
    if d0 <= 100000:  # dynamic programming with prefix sums, O(v * d0)
        dp = [1] + [0] * d0
        for ui in u:
            pre = [0] * (d0 + 2)
            for s in range(d0 + 1):
                pre[s + 1] = pre[s] + dp[s]
            dp = [pre[s + 1] - pre[max(0, s - ui)] for s in range(d0 + 1)]
        return dp[d0]
    total = 0
    for r in range(v + 1):
        for S in itertools.combinations(range(v), r):
            rest = d0 - sum(u[i] + 1 for i in S)
            if rest < 0:
                continue
            total += (-1) ** r * math.comb(rest + v - 1, v - 1)
    return total


def layer_size(d0, v, cap=None):
    return count_bounded(d0, [d0] * v, cap)


def sample_layer(rng, d0, v, cap=None):
    """Uniform composition of d0 into v non-negative parts (each <= cap if given)."""
    while True:
        bars = sorted(rng.sample(range(d0 + v - 1), v - 1))
        parts, prev = [], -1
        for b in bars + [d0 + v - 1]:
            parts.append(b - prev - 1)
            prev = b
        if cap is None or max(parts) <= cap:
            return parts


def brute_force_check():
    v, d0, cap = 3, 9, None
    layer = [b for b in itertools.product(range(d0 + 1), repeat=v) if sum(b) == d0]
    worst = 0.0
    for a in layer:
        for a2 in layer:
            m = [max(x, y) for x, y in zip(a, a2)]
            brute = sum(all(bi <= mi for bi, mi in zip(b, m)) for b in layer)
            worst = max(worst, abs(brute - count_bounded(d0, m, cap)))
    return {"toy": "v=3, d0=9, all pairs", "layer_size": len(layer), "max_abs_error": worst}


def experiment(name, v, d0, cap, reuses, trials, rng, digest_bits=None):
    """digest_bits: for WOTS+C the digest is a uniform digest_bits-bit string and only digests
    on the target layer are usable, so each forger hash lands on the layer with probability
    |layer| / 2^digest_bits; that grinding factor is added to the bits left per hash."""
    L = layer_size(d0, v, cap)
    grind = 0.0 if digest_bits is None else digest_bits - math.log2(L)
    res = {"scheme": name, "v": v, "layer_d0": d0, "chain_cap": cap, "log2_layer": math.log2(L),
           "grinding_bits_per_try": round(grind, 2)}
    for k in reuses:
        bits = []
        for _ in range(trials):
            sigs = [sample_layer(rng, d0, v, cap) for _ in range(k)]
            m = [max(col) for col in zip(*sigs)]
            p = count_bounded(d0, m, cap) / L
            bits.append(-math.log2(p) + grind)
        res[f"k={k}"] = {"median_bits_left": round(statistics.median(bits), 2),
                         "min_bits_left": round(min(bits), 2),
                         "max_bits_left": round(max(bits), 2),
                         "bits_left_for_mean_p": round(-math.log2(statistics.fmean(2 ** -b for b in bits)), 2)}
    return res


def main():
    rng = random.Random(SEED)
    out = {"seed": SEED, "validation": brute_force_check(), "experiments": []}
    # TSL, lam = 128, v = 7 chains (128-byte one-time evidence), d0 from wots_size_work.py
    out["experiments"].append(experiment("TSL v=7 (lam=128)", 7, 7910340, None, (2, 3), 200, rng))
    out["experiments"].append(experiment("TSL v=8 (lam=128)", 8, 1080104, None, (2, 3), 200, rng))
    # SHRINCS-B one-time layer: l=16 chains, w=256 (depth <= 255), target sum 2040 => d0 = 2040
    out["experiments"].append(experiment("WOTS+C SHRINCS-B (l=16,w=256,S=2040)", 16, 255 * 16 - 2040,
                                         255, (2, 3), 200, rng, digest_bits=128))
    from pathlib import Path
    import os
    output = Path(os.environ.get("LULA_MODEL_OUTPUT", Path(__file__).resolve().parents[2] / "generated" / "models" / "rollback_reuse.out.json"))
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
