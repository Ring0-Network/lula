"""Analytical cache-height illustration; no signing, timing, or security certification.

SPDX-License-Identifier: Apache-2.0
Requires mpmath1.3.0. The four lower heights stay5; top height is21 or20.
"""
import json,math
import mpmath as mp

def row(top_height):
    with mp.workdps(600):
        total_height=20+top_height
        q=1<<40;rho=mp.mpf(2)**(-total_height);beta=mp.mpf(511)/512
        probability=mp.fsum((-1)**j*math.comb(17,j)*
            mp.exp(q*mp.log1p(rho*(beta**j-1))) for j in range(18))/512
        exponent=-mp.log(probability,2)
        return {'top_height':top_height,'total_height':total_height,
                'node_payload_bytes':16*((1<<(top_height+1))-1),
                'counter_payload_bytes':4*(1<<top_height),
                'retained_cache_bytes':36*(1<<top_height)-16,
                'signature_bytes':5720+16*(top_height-21),
                'log2_signing_queries':40,
                'FORS_per_candidate_exponent':mp.nstr(exponent,80),
                'display':round(float(exponent),1),
                'scope':'Independent-uniform-selection FORS component model; not full-signer security.'}

if __name__=='__main__':
    rows=[row(21),row(20)]
    assert [r['retained_cache_bytes'] for r in rows]==[75497456,37748720]
    assert [r['signature_bytes'] for r in rows]==[5720,5704]
    assert [r['display'] for r in rows]==[132.6,125.9]
    print(json.dumps({'status':'ANALYTICAL_ILLUSTRATION_ONLY','rows':rows,
                      'new_measurements':False,'full_security_bound_established':False},indent=2))
