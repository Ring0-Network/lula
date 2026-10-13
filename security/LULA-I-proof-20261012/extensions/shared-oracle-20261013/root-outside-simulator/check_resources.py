"""Root arithmetic check of compiled bounded-query simulator caps.

This is not a blind proof derivation, source execution, or security estimate.
The program caps are inherited from the reviewed PRE/type7 adapters.
"""
from pathlib import Path
import hashlib
import json

P = Path(__file__).resolve().parent
X = P.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
qs = (24, 30, 38, 40, 41, 44, 50, 64)
hs = 2**21 * (19505 + 2**32) - 1
hm = {'hot': 82090 + 5 * 2**32,
      'cold': 8560574463 + 82090 + 6 * 2**32}
nd = 19212937084272640
old = json.loads((X/'selected-promotion-review/T7-CONTROL-RESULTS.json').read_text(encoding='utf8'))
assert len(old['q_resource_rows']) == 8
for e, r in zip(qs, old['q_resource_rows'], strict=True):
    q = 2**e
    assert r['q_exponent'] == e
    for mode, u in (('hot', 12816), ('cold', 33567232)):
        assert r[f'{mode}_F_cap'] == min(nd, 8704 + 2181038080 + q*u)
        assert r[f'{mode}_honest_outside_plus_C'] == hs + q*hm[mode] + 3224 + 17392

# An example preinteraction profile, not a universal restriction on raw queries.
b = 598
v = (256**(b+1)-1)//255
m = 1 << (max(256, 8*b+1)-1).bit_length()
assert m == 8192 and v <= 2**m
rows = []
for e in qs:
    q = 2**e
    for qe in (32, 64):
        for mode in hm:
            for adapter, extra in (('PRE', 254), ('ROW', 17392)):
                total = 2**qe + hs + q*hm[mode] + 3224 + extra
                k = min(2*total, v)
                assert k == 2*total
                rows.append({'log2_q': e, 'log2_Q_adversarial': qe,
                             'mode': mode, 'adapter': adapter,
                             'T_all_outside_evaluations': total, 'k': k,
                             'm': m, 'coefficient_bits': k*m,
                             'coefficient_bytes': k*m//8})
assert len(rows) == 64
out = {'status': 'PASS_ROOT_INTEGER_RESOURCE_IDENTITIES_NOT_SECURITY_BOUNDS',
       'inherited_type7_receipt_sha256': sha(X/'selected-promotion-review/T7-INTEGRATION-REVIEW.json'),
       'profile': {'b': b, 'm': m, 'scope': 'Example only; b must cover all source/adversary messages and raw registers before interaction.'},
       'setup_public_cap': hs, 'hot_public_per_sign': hm['hot'],
       'cold_public_per_sign': hm['cold'], 'eight_inherited_q_rows_checked': 8,
       'family_rows': rows, 'original_numeric_bound_changes': False,
       'resource_complexity': 'Uniform circuit generation O(k*m^2+b^2), sampling/init O(k*m+b^2), T evaluations O(T*(k*m^2+b^2)); practical feasibility not claimed.'}
(P/'RESOURCE-CHECK.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf8')
print(json.dumps({'status': out['status'], 'inherited_rows': 8, 'family_rows': len(rows), 'm_example': m}))
