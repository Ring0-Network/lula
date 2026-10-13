"""Read-only recomputation of supplied data and integer models; no crypto runs."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_EVEN
import csv, hashlib, json, math, statistics
import mpmath as mp

P = Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I')
OUT = Path(__file__).parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p): return list(csv.DictReader(p.open(newline='', encoding='utf-8-sig')))
def median(v):
    v=sorted(v); n=len(v)
    return (Decimal(v[(n-1)//2])+Decimal(v[n//2]))/2
def p99(v): return sorted(v)[math.ceil(len(v)*.99)-1]
def ms(x): return Decimal(x)/10**6
def fmt(x,n): return str(Decimal(x).quantize(Decimal(10)**-n, rounding=ROUND_HALF_EVEN))
pins={}
def pin(p): pins[str(p.relative_to(P))]=sha(p)
for f in ['LULA-I.tex','operating-model.tex','stability-results.tex','comparison-results.tex','references.bib','release/code/lula1/src/lib.rs','release/code/lula1/Cargo.toml']:
    pin(P/f)
raw=P/'release/data/b1/raw'
summary=rows(P/'release/data/b1/results/stability_by_cell.csv')
pin(P/'release/data/b1/results/stability_by_cell.csv')
b1=[]
for alg in ['lula','slh128f','slh128s']:
    for msg in [32,1024,65536]:
        files=list(raw.glob(f'b[1-6]-{alg}*-{msg}.csv'))
        assert len(files)==6, (alg,msg,files)
        allrows=[]
        for p in files:
            pin(p); allrows+=rows(p)
            meta=p.with_suffix('.process.json'); pin(meta)
            j=json.loads(meta.read_text())
            assert j['status']=='completed' and j['exit_code']==0 and j['logical_cpu']==10
        for op in ['sign','verify']:
            v=[int(r['ns']) for r in allrows if r['operation']==op]
            s=next(r for r in summary if r['alg']==alg and int(r['msg'])==msg and r['op']==op)
            assert len(v)==int(s['pooledN'])
            # Published tables use binary floating display formatting; retain the
            # exact integer/Decimal median separately, including halfway cases.
            m,p=f'{float(ms(median(v))):.4f}',f'{float(ms(p99(v))):.4f}'
            assert (m,p)==(s['pooled_median_ms'],s['pooled_p99_ms']), (alg,msg,op,m,p,s)
            ratios=[]
            for f in files:
                bv=[int(r['ns']) for r in rows(f) if r['operation']==op]
                ratios.append(Decimal(p99(bv))/median(bv))
            b1.append(dict(alg=alg,msg=msg,op=op,N=len(v),median_exact_ms=str(ms(median(v))),median_ms=m,p99_ms=p,max_block_p99_over_median=fmt(max(ratios),3)))
fresh=[]; fresh_sign=[]
for p in sorted(raw.glob('w[1-3]-fresh-[0-4].csv')):
    pin(p); r=rows(p)
    load=sum(int(x['ns']) for x in r if x['operation']=='fixture_load')
    sign=sum(int(x['ns']) for x in r if x['operation']=='sign')
    fresh.append(load+sign); fresh_sign.append(sign)
assert len(fresh)==15
assert median(fresh)/10**9==Decimal('5.7000569')
assert median(fresh_sign)/10**9==Decimal('.0035796')
cold=[]
for p in sorted(raw.glob('w[1-3]-cacheloss.csv')):
    pin(p); cold += [str(Decimal(r['ns'])/10**9) for r in rows(p) if r['operation']=='sign']
assert [Decimal(x) for x in cold]==list(map(Decimal,['331.8369642','337.5630796','330.0493122']))
prepare=P/'release/data/a1/raw/lula1-full-prepare.stdout.txt'; pin(prepare)
prep=json.loads(prepare.read_text())
assert fmt(prep['secs'],3)=='2216.118' and prep['cache_bytes']==75497456
aux=[]
specs=[('shrincsC-stateful-32',200,'48.520','0.120',324,3508),('shrincsC-fallback-32',20,'471.961','0.448',3680,3680),('kn3952-recon-hot-32',20,'3613.611','0.542',3952,3952),('kn4036-prepared-32',12,'1897.784','0.905',4036,4036)]
admitted=P/'release/data/a1/admitted-rows.json'; pin(admitted)
ar=json.loads(admitted.read_text())
for cell,N,sm,vm,lo,hi in specs:
    record=next(r for r in ar if r['cell']==cell and r['operation']=='sign')
    data=[]
    for name in record['files']:
        p=P/'release/data/a1/raw'/name; pin(p); data+=rows(p)
    signs=[r for r in data if r['operation']=='sign']
    verifies=[r for r in data if r['operation']=='verify']
    assert len(signs)==len(verifies)==N
    assert fmt(ms(median([int(r['ns']) for r in signs])),3)==sm
    assert fmt(ms(median([int(r['ns']) for r in verifies])),3)==vm
    assert min(int(r['sig_bytes']) for r in signs)==lo and max(int(r['sig_bytes']) for r in signs)==hi
    aux.append(dict(cell=cell,N=N,sign_ms=sm,verify_ms=vm,size_min=lo,size_max=hi))
mp.mp.dps=220
rho=mp.mpf(2)**-41; rr=1-mp.mpf(2)**-9
fors=[]
for qexp,display in [(38,'143.3'),(40,'132.6'),(41,'125.9')]:
    q=2**qexp
    vals=[]
    for poisson in [False,True]:
        acc=mp.fsum((-1)**j*math.comb(17,j)*(mp.exp(q*rho*(rr**j-1)) if poisson else mp.power(1+rho*(rr**j-1),q)) for j in range(18))/512
        bits=-mp.log(acc,2); vals.append(mp.nstr(bits,50))
        assert f'{float(bits):.1f}'==display
    fors.append(dict(q_exp=qexp,binomial_exponent=vals[0],poisson_exponent=vals[1],display=display))
counts=dict(signature_bytes=16+4+17*10*16+4*(4+32*16+5*16)+(4+16*16+21*16),cache_bytes=16*(2**22-1)+4*2**21,small_wpk=32*15+32+9,top_wpk=16*255+16+5)
counts['small_tree']=32*counts['small_wpk']+31
counts['fors_sign_fixed']=17*(512+512+511+1)+5
counts['hot_sign_fixed']=4+counts['fors_sign_fixed']+4*(counts['small_tree']+32+240+1)+16+2040+1
counts['missing_top_extra']=2**21*counts['top_wpk']+(2**21-1)
counts['verify32_suffix']=3+175+4*255+2067
counts['verify32_including_context']=counts['verify32_suffix']+1
assert counts==dict(signature_bytes=5720,cache_bytes=75497456,small_wpk=521,top_wpk=4101,small_tree=16703,fors_sign_fixed=26117,hot_sign_fixed=96082,missing_top_extra=8602517503,verify32_suffix=3265,verify32_including_context=3266)
result=dict(scope='Read-only dataset/model recomputation; no cryptographic execution, attack, benchmark or source changes',b1_cells=b1,auxiliary_rows=aux,fresh_restart_count=15,fresh_load_plus_sign_median_s=str(median(fresh)/10**9),fresh_sign_median_s=str(median(fresh_sign)/10**9),cacheloss_individual_s=cold,keygen_observation_s=prep['secs'],fors_model=fors,counts=counts,pins=pins)
(OUT/'NUMERICAL-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(b1_cells=len(b1),aux_rows=len(aux),fors_rows=len(fors),input_pins=len(pins),counts=counts),indent=2))
