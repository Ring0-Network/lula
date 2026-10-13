"""Recompute retained campaign, replay, and summary-source table values.

Python standard library only. No signing, key generation, cache reads, or writes
to data/. Historical summaries cannot recover unrecorded per-call durations.
"""
from pathlib import Path
from decimal import Decimal
from collections import defaultdict
import csv, hashlib, json, math, statistics

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'recomputed/data'
OUT.mkdir(parents=True,exist_ok=True)
def load(p):return json.loads(p.read_text(encoding='utf8'))
def csvrows(p):
    with p.open(newline='',encoding='utf8') as f:return list(csv.DictReader(f))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stats(v,unit='ns',rule='nearest_rank'):
    s=sorted(v);n=len(s)
    if not n:raise ValueError('Empty admitted sample')
    def quant(p):
        i=math.ceil(p*n)-1 if rule=='nearest_rank' else math.floor((n-1)*p+0.5)
        return s[i]
    return {'N':n,'unit':unit,'quantile_rule':rule,'min':s[0],'median':statistics.median(s),'p95':quant(.95),'p99':quant(.99),'max_observed':s[-1]}

A=ROOT/'data/a1';R=A/'raw'
admitted=load(A/'admitted-rows.json');a1=[];checks=[]
for row in admitted:
    v=[];sb=[];hc=[];pk=[]
    for name in row['files']:
        for r in csvrows(R/name):
            if r['operation']!=row['operation']:continue
            ns=int(Decimal(r['ns']))
            if ns<=0 and row['operation'] in ['sign','verify','fixture_load','keygen','fixture_load_or_restore']:
                raise ValueError('Untimed row admitted to elapsed operation '+name)
            v.append(ns)
            if r.get('sig_bytes'):sb.append(int(r['sig_bytes']))
            if r.get('pk_bytes'):pk.append(int(r['pk_bytes']))
            if r.get('hash_calls'):hc.append(int(r['hash_calls']))
    z=stats(v)
    ok=z['N']==row['N'] and all(math.isclose(z[new]/1e6,row[old],abs_tol=1e-9,rel_tol=0) for old,new in [('min_ms','min'),('median_ms','median'),('p95_ms','p95'),('p99_ms','p99'),('max_observed_ms','max_observed')])
    checks.append({'cell':row['cell'],'operation':row['operation'],'matches_retained_admission_summary':ok})
    a1.append({'cell':row['cell'],'operation':row['operation'],'timing_eligible':all(x>0 for x in v),**z,'signature_bytes':sorted(set(sb)),'public_key_bytes':sorted(set(pk)),
               'instrumented_hash_calls':stats(hc,'count') if hc else None,'files':row['files']})
assert all(x['matches_retained_admission_summary'] for x in checks)

fresh=[]
for prefix in ['lula1','shrincsC','kn3952-recon','kn4036']:
    pairs=[];loads=[];signs=[];names=[]
    for f in sorted(R.glob(prefix+'-fresh-32-*.csv')):
        rows=csvrows(f);loadop='fixture_load_or_restore' if prefix=='shrincsC' else 'fixture_load'
        lo=sum(int(r['ns']) for r in rows if r['operation']==loadop)
        si=sum(int(r['ns']) for r in rows if r['operation']=='sign')
        assert lo>0 and si>0
        loads.append(lo);signs.append(si);pairs.append(lo+si);names.append(f.name)
    fresh.append({'candidate':prefix,'load':stats(loads),'first_sign':stats(signs),'paired_load_sign':stats(pairs),'files':names})
branches=[];equality=[]
for n in [32,1024]:
    by={}
    for branch in ['A','B']:
        f=R/f'lula1-snap{branch}-{n}.txt'
        rows=[l.split() for l in f.read_text().splitlines() if l and not l.startswith('#')]
        branches.append({'message_bytes':n,'branch':branch,**stats([int(r[1]) for r in rows]),'file':f.name})
        by[branch]={r[0]:r[3] for r in rows}
        assert all(int(r[2])==5720 and len(bytes.fromhex(r[3]))==5720 for r in rows)
    overlap=set(by['A'])&set(by['B']);identical=all(by['A'][k]==by['B'][k] for k in overlap)
    equality.append({'message_bytes':n,'overlap':len(overlap),'byte_identical':identical})
assert all(r['byte_identical'] for r in equality)
memory=[]
for cell in ['lula1-hot-32','slh128f-32','slh128s-32','shrincsC-stateful-32','shrincsC-fallback-32','kn3952-recon-hot-32','kn4036-prepared-32']:
    f=R/f'job-{cell}.process.json';m=load(f)
    assert m['exit_code']==0 and m['status']=='completed'
    memory.append({'cell':cell,'working_set_bytes':m['peak_working_set_bytes'],'private_bytes':m['peak_private_bytes'],'source':f.name})
setup=load(R/'lula1-full-prepare.stdout.txt')
assert 'seed_hex' not in setup
loss=csvrows(R/'lula1-missing-32.csv')
loss=[{'rep':int(r['rep']),'first_or_second_in_same_process':int(r['rep'])+1,'ns':int(r['ns']),'instrumented_compressions':int(r['hash_calls'])} for r in loss if r['operation']=='sign']
result={'a1':{'admitted_cells':a1,'retained_summary_checks':checks,'fresh':fresh,'branches':branches,'branch_equality':equality,'memory':memory,'setup':setup,'cache_loss_consecutive_calls':loss}}

H=ROOT/'data/history';historical=[]
for file,label,fields in [('session-a.json','Session A', [('sign_ms','signing'),('verify_ms','verification')]),('session-b.json','Session B',[('sign_ms','signing'),('verify_ms','verification')]),('lifecycle.json','Lifecycle',[('prepared_ms','prepared'),('restored_older_snapshot_ms','restored')])]:
    h=load(H/file)
    for key,operation in fields:
        historical.append({'scenario':label+' '+operation,'evidence_class':'retained_summary_source_only','source':file,'source_field':key,**h[key]})
    if file=='lifecycle.json':historical.append({'scenario':'Lifecycle absent','N':len(h['absent_ms']),'values_ms':h['absent_ms'],'source':file,'evidence_class':'retained_summary_source_only'})
result['historical']=historical
replay=csvrows(ROOT/'data/replay/native-replay-final.json.raw.csv')
# Retained CSV is in decimal milliseconds. Convert exactly to nanoseconds first.
# Minor decimal representations such as .14889999999999998 differ far below 1 ns.
ns=[round(Decimal(r['verify_ms'])*Decimal(1000000)) for r in replay]
assert len(ns)==1000 and all(int(r['instrumented_compressions'])==3265 for r in replay)
result['publication_replay']={**stats(ns,rule='nearest_index_rust_ties_up'),'source':'data/replay/native-replay-final.json.raw.csv','compressions_unique':sorted({int(r['instrumented_compressions']) for r in replay}),'decimal_csv_conversion':'round decimal milliseconds to nearest integer ns; binary formatting residue below one ns'}
summary=load(ROOT/'data/replay/native-replay-final.json')['full_verify_ms']
assert all(math.isclose(result['publication_replay'][key]/1e6,summary[key],abs_tol=1e-12) for key in ['min','median','p95','p99'])
assert math.isclose(result['publication_replay']['max_observed']/1e6,summary['max'],abs_tol=1e-12)
result['source_hashes']={p.relative_to(ROOT).as_posix():digest(p) for p in sorted((ROOT/'data').rglob('*')) if p.is_file()}
(OUT/'RECOMPUTED_DATA.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'admitted_a1_rows':len(a1),'a1_summary_checks':sum(c['matches_retained_admission_summary'] for c in checks),'fresh_candidates':len(fresh),'branch_overlaps':equality,'replay_N':len(ns),'historical_summary_rows':len(historical),'output':'recomputed/data/RECOMPUTED_DATA.json'}))
