"""Recompute published component models and exact arithmetic, never sign messages.

Copyright 2026 Ring0 Labs contributors. SPDX-License-Identifier: Apache-2.0
The occupancy and uniform-selection assumptions are premises. Passing these checks
does not establish the complete signer's security or a signing-capacity certificate.
"""
from pathlib import Path
import argparse, json, math, re, hashlib
import mpmath as mp

ROOT=Path(__file__).resolve().parents[2]

def exponent(logq,h,a,k,forced,binomial=False,dps=240):
    with mp.workdps(dps):
        q=mp.power(2,logq); rho=mp.power(2,-h); r=1-mp.power(2,-a)
        terms=[]
        for j in range(k+1):
            delta=r**j-1
            moment=mp.exp(q*mp.log1p(rho*delta)) if binomial else mp.exp(q*rho*delta)
            terms.append((-1)**j*math.comb(k,j)*moment)
        p=mp.fsum(terms)*(mp.power(2,-a) if forced else 1)
        assert 0<p<=1
        return -mp.log(p,2)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--paper',type=Path,default=ROOT/'paper')
    parser.add_argument('--output',type=Path,default=ROOT/'recomputed'/'models.json')
    args=parser.parse_args(); paper=args.paper
    specs=[('LULA I',41,9,17,True,[24,30,38,40,41,42,44,50,56,64]),
           ('Draft SHA2-128-24',22,24,6,False,[24,30,40,64]),
           ('SHA2-128s',63,12,14,False,[24,30,40,64]),
           ('SHA2-128f',66,6,33,False,[24,30,40,64])]
    rows=[]
    for name,h,a,k,forced,queries in specs:
        for q in queries:
            e=exponent(q,h,a,k,forced)
            high=exponent(q,h,a,k,forced,dps=480)
            with mp.workdps(240): assert abs(e-high)<mp.mpf('1e-110')
            if forced:
                exact=exponent(q,h,a,k,forced,True)
                assert round(float(e),1)==round(float(exact),1)
            rows.append({'construction':name,'log2_queries':q,'raw_candidate_exponent':mp.nstr(e,80),'display':round(float(e),1),'status':'DERIVED_COMPONENT_ONLY'})
    text=(paper/'operating-model.tex').read_text(encoding='utf8')
    pat=r'\$2\^\{(\d+)\}\$\\textsuperscript\{[SD]\} & (.*?)\\textsuperscript\{S\} &\s*([0-9.]+)\\textsuperscript\{D\}'
    found={(name,int(q)):float(v) for q,name,v in re.findall(pat,text)}
    expected={(r['construction'],r['log2_queries']):r['display'] for r in rows}
    assert len(found)==22 and found==expected
    n=16; layers=[(5,32)]*4+[(21,16)]
    fields=[('Randomizer',n),('FORS counter',4),('FORS evidence',n*17*(9+1))]+[(f'Layer {j}',4+n*(chains+h)) for j,(h,chains) in enumerate(layers)]
    offset=0; wire=[]
    for name,length in fields:
        wire.append({'field':name,'offset':offset,'bytes':length}); offset+=length
    assert offset==5720
    components={'LULA I':[16,16*17*10,16*(4*32+16),16*(4*5+21),4*6],
                'SHA2-128s':[16,16*14*13,16*35*7,16*63,0],
                'SHA2-128f':[16,16*33*7,16*35*22,16*66,0]}
    assert [sum(x) for x in components.values()]==[5720,7856,17088]
    # 111 and 118 are fixed padded PORS authentication-node allocations in the
    # pinned auxiliary encodings, source facts rather than security parameters.
    auxiliary={'B32 FB':[16,32*(4+1),16*11,16*111,16*16*4,16*32,4*4],
               'KN-R':[0,16*2,16*8,16*8*16,16*16*4,16*44,4*4],
               'KN-G':[0,32,16*11,16*118,16*16*5,16*40,4*5]}
    assert [sum(x) for x in auxiliary.values()]==[3680,3952,4036]
    work={'message_digest_m32':3,'fors_leaves_paths_root':17*10+math.ceil((22+17*16+9)/64),
          'lower_wots_paths':4*(32*15-240+9+1+5),
          'top_wots_path':16*255-2040+5+1+21}
    # Accepted digest recomputation is one compression in each WOTS group.
    assert list(work.values())==[3,175,1020,2067]
    instrumented=sum(work.values()); assert instrumented==3265
    tree_pk=16*255+16+5
    cold=(2**21)*tree_pk+2**21-1
    cache=(2**22-1)*16+2**21*4
    hot_constant=4+26117+4*(16703+32+240+1)+16+2040+1
    assert (cold,cache,hot_constant)==(8602517503,75497456,96082)
    result={'status':'PASS_WITHIN_LISTED_DERIVATIONS','mpmath_version':mp.__version__,'component_model_rows':rows,'wire':wire,'signature_bytes':offset,'public_key_bytes':2*n,'components':components,'auxiliary_components':auxiliary,'auxiliary_allocation_status':'Derived sizes conditional on the pinned source allocations of 111/118 padded authentication nodes; no interoperability proof.','verification_compressions':work,'instrumented_total':instrumented,'executed_total':instrumented+1,'top_public_key_compressions':tree_pk,'cold_subtree_compressions':cold,'cache_payload_bytes':cache,'hot_fixed_compressions_m32':hot_constant,'caveat':'No full reference-signer bound, capacity certificate, new benchmark or real SHRINCS attack.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':result['status'],'model_rows':22,'signature_bytes':offset,'cache_payload_bytes':cache,'instrumented_total':instrumented,'output_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest()}))

if __name__=='__main__': main()
