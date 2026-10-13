"""Exact symbolic reduction counts; no signing/key/cache construction."""
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = HERE.parents[2]
# private-challenge-program -> shared-oracle extension -> extensions -> frozen S
LIB = S.parents[1] / "publications" / "LULA-I" / "release" / "code" / "lula1" / "src" / "lib.rs"
EXPECTED = "ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210"
assert hashlib.sha256(LIB.read_bytes()).hexdigest() == EXPECTED
parent = json.loads((S / "code-review" / "SOURCE_AND_COUNTS.json").read_text(encoding="utf-8"))
L = 2**32
small = 32 * (32 * 15 + 1) + 31
top = 2**21 * (16 * 255 + 1) + 2**21 - 1
fors = 17 * (512 + 511) + 1
base = fors + 4 * small + 4 * 240 + 2040 + 5 + 1
setup = 2**21 * (16 + 32 * 32)
hot_distinct = 17 * 512 + 4 * 32 * 32 + 16
cold_distinct = 17 * 512 + 4 * 32 * 32 + 2**21 * 16
hot_invocations = 17 * (512 + 1) + 4 * (32 * 32 + 32) + 16
cold_invocations = hot_invocations + 2**21 * 16
verify = 2 + 17 * (1 + 9) + 1 + 5 + 4 * (32 * 15 - 240) + (16 * 255 - 2040) + 5 + 41
assert small == 15423 and top == 8560574463 and base == 82090 and verify == 3224
for key, value in {
    "keygen_top_cache_prf_calls": setup,
    "prepared_sign_distinct_prf_locations_max": hot_distinct,
    "uncached_sign_distinct_prf_locations_max": cold_distinct,
    "prepared_sign_prf_invocations": hot_invocations,
    "uncached_sign_prf_invocations": cold_invocations,
}.items():
    assert parent[key] == value, (key, parent[key], value)

# Toy joint access: derive(a)=raw at hidden key's designated coordinate.
# Compare the exact challenge and exact adapter across every function table/key.
# The independent-plus-fixed-raw replacement fails the real correlation test.
alphabet = range(2)
matches = 0
worlds = 0
real_agreements = 0
independent_agreements = 0
for table in itertools.product(alphabet, repeat=4):
    for key in range(2):
        # Two addresses, two keys: coordinate index 2*a+key.
        direct = tuple(table[2 * a + key] for a in range(2))
        memo = {}
        def derive(a):
            if a not in memo:
                memo[a] = table[2 * a + key]
            return memo[a]
        queried = (derive(1), derive(0), derive(1))
        assert queried == (direct[1], direct[0], direct[1])
        matches += 1
        for independent in itertools.product(alphabet, repeat=2):
            worlds += 1
            real_agreements += int(direct[0] == table[key])
            independent_agreements += int(independent[0] == table[key])
assert Fraction(real_agreements, worlds) == 1
assert Fraction(independent_agreements, worlds) == Fraction(1, 2)

q_columns = {}
namespace = parent["all_secret_prf_locations"]
Hsetup = 2**21 * (19505 + L) - 1
Hhot = base + 5 * L
Hcold = top + base + 6 * L
for logq in (24, 30, 38, 40, 41, 44, 50, 64):
    q = 2**logq
    q_columns[str(logq)] = {
        "K_challenge_cold": min(namespace, setup + cold_distinct * q),
        "K_challenge_hot": min(namespace, setup + hot_distinct * q),
        "P_challenge": q,
        "K_Raw_cold_excluding_QH": Hsetup + q * (Hcold + 1) + verify,
        "K_Raw_hot_excluding_QH": Hsetup + q * (Hhot + 1) + verify,
        "P_Raw_cold_excluding_QH": Hsetup + q * Hcold + verify,
        "P_Raw_hot_excluding_QH": Hsetup + q * Hhot + verify,
    }
result = {
    "status": "EXACT_SYMBOLIC_COUNTS_AND_SMALL_JOINT_ACCESS_CONTROL_PASS",
    "not_a_source_security_or_Rust_refinement_proof": True,
    "source_sha256": EXPECTED,
    "parent_counts_sha256": hashlib.sha256((S / "code-review" / "SOURCE_AND_COUNTS.json").read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "setup_private_distinct_and_invocations": setup,
    "hot_private_distinct": hot_distinct,
    "cold_private_distinct": cold_distinct,
    "hot_private_invocations": hot_invocations,
    "cold_private_invocations": cold_invocations,
    "public_setup_cap": Hsetup,
    "public_hot_cap": Hhot,
    "public_cold_cap": Hcold,
    "public_final_verifier_cap": verify,
    "q_columns": q_columns,
    "toy_tables_keys_checked": matches,
    "toy_comparison_worlds": worlds,
    "real_correlation_probability": str(Fraction(real_agreements, worlds)),
    "independent_fixed_raw_correlation_probability": str(Fraction(independent_agreements, worlds)),
}
(HERE / "COUNT-CHECKS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "source_sha256": EXPECTED, "toy_worlds": worlds, "q_rows": len(q_columns)}))
