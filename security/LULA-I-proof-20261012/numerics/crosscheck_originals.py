"""Read-only crosscheck against original analytical scripts; outputs only here."""
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import mpmath as mp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    global bounds
    bounds=load('independent_bounds',HERE/'bounds.py')
    files=dict(r6opt=ROOT/'R6/R6A-state-as-accelerator/work/r6opt.py',
               ia_model=ROOT/'R8/R8B-immutable-authority/work/ia_model.py',
               H1=ROOT/'H-hash/H1-frame-bounds/work/rollback_reuse.py',
               CE=ROOT/'critics/CE-empirical/work/ce02_reuse_bits.py',
               rust=ROOT/'M-measure/LULA-I-comparison-20261011-a1/sources/ra-r6a/src/lib.rs',
               driver=ROOT/'M-measure/LULA-I-comparison-20261011-a1/sources/ra-r6a/src/bin/m3_ra.rs')
    r6=load('original_r6opt',files['r6opt'])
    ia=load('original_ia_model',files['ia_model'])
    h1=load('original_h1',files['H1'])
    ce=load('original_ce',files['CE'])
    rows=[]
    for logq in bounds.Q_EXPONENTS:
        own=bounds.bits(bounds.fors_moment(1<<logq,41,9,18))
        try:
            old=-r6.forsc_log2_forge(18,9,41,1<<logq)
        except (AssertionError,OverflowError,ValueError) as error:
            old=None
            err=type(error).__name__
        else:
            err=None
        oldpois=9-ia.log2_fors_p(41,9,17,logq)
        rows.append(dict(logq=logq,independent_binomial_bits=own,original_r6opt_bits=old,
                         original_r6opt_error=err,original_ia_poisson_bits=oldpois,
                         r6_difference_bits=None if old is None else old-own,
                         ia_difference_bits=oldpois-bounds.bits(bounds.fors_moment(1<<logq,41,9,18,True))))
        print(rows[-1],flush=True)
    assert abs(rows[3]['r6_difference_bits'])<0.01
    assert abs(rows[3]['ia_difference_bits'])<0.01
    import random
    rng=random.Random(bounds.SEED+3)
    counts=[]
    for w,ell,S in ((16,32,240),(256,16,2040)):
        # H1 uses depths from chain top: depth=(w-1)-position. Complement sum unchanged here.
        slice_n=bounds.count_dp(S,[w-1]*ell)
        assert slice_n==h1.layer_size(S,ell,w-1)==ce.count(S,[w-1]*ell)
        for trial in range(20):
            xs=[bounds.layer_sample(rng,w,ell,S) for _ in range(2)]
            m=list(map(min,zip(*xs)))
            d=S-sum(m)
            cap=[w-1-v for v in m]
            maximum_depth=cap
            ours=bounds.count_dp(d,cap)
            # H1 in complemented coordinates has fixed target depth sum S (central slice).
            assert ours==h1.count_bounded(S,maximum_depth,w-1)
            assert ours==ce.count(d,cap)==bounds.count_ie(d,cap)
        counts.append(dict(w=w,ell=ell,S=S,slice_count=str(slice_n),crosschecked_pairs=20,
                           note='Inclusive counts. CE main experiment subtracts k; H1 does not.'))
    result=dict(source_receipts=[dict(role=role,path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest()) for role,path in files.items()],
                rows=rows,count_crosschecks=counts,status='PASS_COMPONENT_CROSSCHECKS',
                caveat='Original high-load float windows are not an exact numerical certificate; q64 R6 model rejects its lgamma path.',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'ORIGINAL_CROSSCHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
