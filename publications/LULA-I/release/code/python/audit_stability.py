"""Read-only b1 arithmetic/telemetry/vector audit; writes only beside this script."""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction
import csv, datetime as dt, hashlib, importlib.util, json, math, re, statistics

P=Path(__file__).resolve().parents[2]
BASE=P/'data/b1'
OUT=P/'recomputed/stability-audit'
OUT.mkdir(parents=True,exist_ok=True)
RAW = BASE/'raw'
def utc(x): return dt.datetime.fromisoformat(x.replace('Z','+00:00'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def median(v):
    s=sorted(v); n=len(s)
    return Fraction(s[n//2]) if n%2 else (Fraction(s[n//2-1])+Fraction(s[n//2]))/2
def stats(v):
    s=sorted(v); n=len(s)
    return {'N':n,'min_ns':s[0],'median_ns':float(median(s)),
            'p95_ns':s[math.ceil(n*.95)-1], 'p99_ns':s[math.ceil(n*.99)-1], 'max_ns':s[-1]}
def sample_stats(rows):
    return {'rows':len(rows),**{f'{k}_mean':statistics.mean(r[k] for r in rows) for k in ['total','c10','c11','freq']},
            **{f'{k}_mean_exact_rational':str(sum((Fraction(str(r[k])) for r in rows),Fraction(0))/len(rows)) for k in ['total','c10','c11']},
            **{f'{k}_max':max(r[k] for r in rows) for k in ['total','c10','c11']}}
sources={}
def record(p):
    if p.stat().st_size>10_000_000: raise RuntimeError('Unexpected large audit input')
    sources[str(p.relative_to(BASE))]={'bytes':p.stat().st_size,'sha256':sha(p)}
sam=[]
with (RAW/'sampler.csv').open(newline='',encoding='ascii') as f:
    for r in csv.DictReader(f):
        sam.append({'t':utc(r['utc']),'total':float(r['total_utility']),'c10':float(r['cpu10_utility']),
                    'c11':float(r['cpu11_utility']),'freq':float(r['cpu10_freq_mhz']), 'busy':r['busy_processes']})
sam.sort(key=lambda r:r['t'])
gates=[json.loads(l) for l in (RAW/'gate.jsonl').read_text().splitlines()]
passg={g['job']:g for g in gates if g.get('pass')}
gate_checks=[]
for g in gates:
    if not g.get('pass'):continue
    t=utc(g['utc']); rows=[r for r in sam if t-dt.timedelta(seconds=20)<=r['t']<=t]
    z=sample_stats(rows)
    gate_checks.append({'job':g['job'],'utc':g['utc'],'logged_rows':g['rows'],'recomputed':z,
                        'thresholds_pass':len(rows)>=3 and z['total_mean']<=30 and z['c10_mean']<=8 and z['c11_mean']<=8,
                        'means_match_logged_rounding':all(abs(z[k+'_mean']-g[k])<=.051 for k in ['total','c10','c11'])})
jobs=[]; cells=defaultdict(list); expected=[]
for b in range(1,7):
    for size in [32,1024,65536]:
        expected.extend([f'b{b}-lula-k{1 if b%2 else 2}-{size}',f'b{b}-slh128f-{size}',f'b{b}-slh128s-{size}'])
for w in range(1,4):expected.extend([f'w{w}-fresh-{i}' for i in range(5)]+[f'w{w}-cacheloss'])
for name in sorted(expected):
    pj=RAW/(name+'.process.json'); m=json.loads(pj.read_text()); p=RAW/(name+'.csv')
    ops=defaultdict(list); controls=Counter(); validity=Counter()
    with p.open(newline='',encoding='utf8') as f:
        for r in csv.DictReader(f):
            op=r['operation']; controls[op]+=1
            if op in ['sign','verify','fixture_load']:ops[op].append(int(r.get('ns',r.get('elapsed_ns'))))
            validity[(op,r.get('valid',r.get('verified','unknown')))]+=1
    t0=utc(m['start_utc']); t1=utc(m['end_utc']); ss=sample_stats([r for r in sam if t0<=r['t']<=t1])
    contaminated=ss['rows']<3 or ss['c11_mean']>15 or ss['total_mean']>45
    hot=re.fullmatch(r'b(\d+)-(lula)-k(\d)-(\d+)',name) or re.fullmatch(r'b(\d+)-(slh128[fs])-(\d+)',name)
    if hot:
        b=int(hot[1]);alg=hot[2];key=int(hot[3]) if alg=='lula' else 0;size=int(hot[4] if alg=='lula' else hot[3])
    else:
        b=int(name[1]);alg='fresh' if 'fresh' in name else 'cacheloss';key=1;size=32
    j={'job':name,'block':b,'alg':alg,'key':key,'msg':size,'status':m['status'],'exit_code':m['exit_code'],
       'start':m['start_utc'],'end':m['end_utc'],'pid':m['pid'],'wall_s':m['wall_seconds'],
       'metadata_pinning_pass':m['logical_cpu']==10 and m['affinity_mask']==1024 and m['priority']=='BelowNormal' and m['memory_limit_bytes']==2952790016,
       'gate_pass_record':name in passg,'gate_to_start_s_floor':(t0-utc(passg[name]['utc'])).total_seconds(),
       'sampler':ss,'contaminated':contaminated,'operations':{op:stats(v) for op,v in ops.items()},
       'row_counts':dict(controls),'validity_counts':{f'{a}:{b}':n for (a,b),n in validity.items()}}
    jobs.append(j)
    expected_n=200 if alg=='slh128s' else (1000 if hot else 1)
    j['expected_timing_count']=expected_n
    j['expected_sign_verify_counts_pass']=len(ops['sign'])==expected_n and len(ops['verify'])==expected_n
    if hot:
        for op in ['sign','verify']:cells[(alg,size,op)].append((j,ops[op]))
    else:j['_raw_ops']=ops
cellout=[]
for (alg,size,op), entries in sorted(cells.items()):
    clean=[(j,v) for j,v in entries if not j['contaminated']]
    medians=[float(median(v)) for j,v in clean]; mean=statistics.mean(medians)
    spread=(max(medians)-min(medians))/mean;cv=statistics.pstdev(medians)/mean
    ratio=max(stats(v)['p99_ns']/float(median(v)) for j,v in clean)
    allg=all(j['gate_pass_record'] for j,v in clean)
    verdict='inconclusive' if len(clean)<4 else ('stable' if spread<=.05 and ratio<=3 and allg else 'unstable')
    kmed={str(k):float(median([float(median(v)) for j,v in clean if j['key']==k])) for k in [1,2] if any(j['key']==k for j,v in clean)}
    effect=abs(kmed['1']-kmed['2'])/statistics.mean(kmed.values()) if len(kmed)==2 else None
    cellout.append({'alg':alg,'msg':size,'op':op,'blocks_total':len(entries),'blocks_clean':len(clean),
                    'blocks':[{**{k:j[k] for k in ['job','block','key','gate_pass_record','contaminated']},**stats(v)} for j,v in entries],
                    'key_block_counts':dict(Counter(j['key'] for j,v in clean)),
                    'block_median_min_ns':min(medians),'block_median_max_ns':max(medians),
                    'spread_over_mean':spread,'cv_block_medians':cv,'max_p99_over_median':ratio,
                    'key_effect':effect,'verdict':verdict,'pooled':stats([x for j,v in clean for x in v])})
fresh=[j for j in jobs if j['alg']=='fresh'];loss=[j for j in jobs if j['alg']=='cacheloss']
freshstats={op:stats([j['_raw_ops'][op][0] for j in fresh]) for op in ['fixture_load','sign','verify']}
freshstats['paired_load_sign']=stats([j['_raw_ops']['fixture_load'][0]+j['_raw_ops']['sign'][0] for j in fresh])
freshstats['per_process']=[{'job':j['job'],'load_ns':j['_raw_ops']['fixture_load'][0],'first_sign_ns':j['_raw_ops']['sign'][0],
                          'paired_ns':j['_raw_ops']['fixture_load'][0]+j['_raw_ops']['sign'][0]} for j in fresh]
lossstats=[{'job':j['job'],'pid':j['pid'],'first_sign_ns':j['_raw_ops']['sign'][0],'signs_in_process':len(j['_raw_ops']['sign']),
            'load_ns':j['_raw_ops']['fixture_load'][0]} for j in loss]
for j in fresh+loss:del j['_raw_ops']
# Compare every published by-job statistic at its printed precision.
jindex={j['job']:j for j in jobs}; comparisons=[]
with (BASE/'results/stability_by_job.csv').open(newline='') as f:
    for r in csv.DictReader(f):
        actual=jindex[r['job']]['operations'][r['op']]
        ok=int(r['N'])==actual['N'] and all(r[k+'_ms']==f"{actual[k+'_ns']/1e6:.4f}" for k in ['min','median','p95','p99','max'])
        ss=jindex[r['job']]['sampler']
        telemetry_ok=int(r['sampler_rows'])==ss['rows'] and all(r[k]==f'{ss[k]:.1f}' for k in ['total_mean','c10_mean','c11_mean']) and r['c11_max']==f"{ss['c11_max']:.0f}" and r['freq10_mean']==f"{ss['freq_mean']:.0f}"
        comparisons.append({'job':r['job'],'operation':r['op'],'all_printed_statistics_match':ok,'all_printed_telemetry_matches':telemetry_ok})
cindex={(c['alg'],c['msg'],c['op']):c for c in cellout};cellchecks=[]
with (BASE/'results/stability_by_cell.csv').open(newline='') as f:
    for r in csv.DictReader(f):
        c=cindex[(r['alg'],int(r['msg']),r['op'])]; p=c['pooled']
        ok=int(r['pooledN'])==p['N'] and r['verdict']==c['verdict'] and all(r['pooled_'+k+'_ms']==f"{p[k+'_ns']/1e6:.4f}" for k in ['median','p95','p99','max'])
        ok &= all(r[k]==f'{c[k]:.3f}' for k in ['spread_over_mean','cv_block_medians']) and r['max_p99_over_median']==f"{c['max_p99_over_median']:.2f}"
        ok &= int(r['blocks_total'])==c['blocks_total'] and int(r['blocks_clean'])==c['blocks_clean']
        ok &= r['block_median_min_ms']==f"{c['block_median_min_ns']/1e6:.4f}" and r['block_median_max_ms']==f"{c['block_median_max_ns']/1e6:.4f}"
        ok &= r['key_effect']==('' if c['key_effect'] is None else f"{c['key_effect']:.3f}")
        cellchecks.append({'cell':[c['alg'],c['msg'],c['op']],'matches':bool(ok)})
# Replay verification without invoking the campaign writer or creating files there.
vpath=P/'code/python/verify_lula.py'
module=importlib.util.spec_from_file_location('lula_independent_verify',vpath);v=importlib.util.module_from_spec(module);module.loader.exec_module(v)
spec='18,9,1;5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|5:4:0:240:0|21:8:0:2040:1'
vectorresults=[];groups=defaultdict(list)
for p in sorted(RAW.glob('*.vec.txt')):
    d=dict(l.split() for l in p.read_text().splitlines() if len(l.split())==2)
    pkseed,pkroot,msg,sig=[bytes.fromhex(d[k]) for k in ['pk_seed','pk_root','msg','sig']]
    good=v.verify(spec,pkseed,pkroot,msg,sig);badmsg=v.verify(spec,pkseed,pkroot,bytes([msg[0]^1])+msg[1:],sig)
    b=bytearray(sig);b[len(b)//2]^=1;badsig=v.verify(spec,pkseed,pkroot,msg,bytes(b))
    vectorresults.append({'file':p.name,'valid':good,'changed_message_rejected':not badmsg,'changed_signature_rejected':not badsig,
                          'msg_bytes':len(msg),'sig_bytes':len(sig),'public_key_seed':d['pk_seed'],'public_key_root':d['pk_root'],'signature_sha256':hashlib.sha256(sig).hexdigest()})
    groups[(d['pk_seed'],d['pk_root'],d['msg'])].append((p.name,sig))
vg=[{'key_seed':seed,'key_root':root,'msg_bytes':len(bytes.fromhex(msg)),'message_sha256':hashlib.sha256(bytes.fromhex(msg)).hexdigest(),
     'files':[f for f,s in vs],'distinct_signatures':len({s for f,s in vs})} for (seed,root,msg),vs in groups.items()]
gaps=[(b['t']-a['t']).total_seconds() for a,b in zip(sam,sam[1:])]
orders=[]
for b in range(1,7):
    o=json.loads((RAW/f'b{b}-order.json').read_text());jj=sorted([j for j in jobs if j['alg'] not in ['fresh','cacheloss'] and j['block']==b],key=lambda j:j['start'])
    orders.append({'block':b,'seed':o['seed'],'key':o['key'],'order_matches_process_start':o['order']==[j['job'] for j in jj],
                   'first_start':jj[0]['start'],'last_end':jj[-1]['end']})
for a,b in zip(orders,orders[1:]):b['gap_from_prior_block_s']=(utc(b['first_start'])-utc(a['last_end'])).total_seconds()
for p in sorted(BASE.rglob('*')):
    if p.is_file() and p.suffix.lower() in ['.md','.py','.ps1','.json','.jsonl','.csv','.txt'] and p.stat().st_size<10_000_000:record(p)
result={'campaign_path':'data/b1','audited_utc':None,'method':'Independent integer-nanosecond arithmetic, nearest rank, midpoint median; native HTTPS not needed; no benchmark reruns',
        'expected_jobs':72,'jobs':jobs,'cells':cellout,'fresh':freshstats,'cache_loss_first_calls':lossstats,'order_validation':orders,
        'published_by_job_checks':comparisons,'published_by_cell_checks':cellchecks,'gate_checks':gate_checks,
        'printed_telemetry_rounding_difference_jobs':sorted({c['job'] for c in comparisons if not c['all_printed_telemetry_matches']}),
        'gate_timeout_count':sum(bool(g.get('gate_timeout')) for g in gates),'sampler_summary':{'rows':len(sam),'first':sam[0]['t'].isoformat(),'last':sam[-1]['t'].isoformat(),
                'gap_s':{'min':min(gaps),'median':statistics.median(gaps),'max':max(gaps),'above_2s':sum(g>2 for g in gaps)},'frequency_values':sorted({r['freq'] for r in sam}),
                'busy_processes_populated_rows':sum(bool(r['busy']) for r in sam)},
        'vectors':vectorresults,'vector_byte_groups':vg,'independent_verifier_sha256':sha(vpath),'source_files':sources,
        'documented_limits':['Stability is the declared median-spread/p99 criterion, not guaranteed maximum runtime',
          'Telemetry averages whole-process intervals and has roughly one-second temporal resolution',
          'Sampler measures time busy, not frequency-scaled processor utility',
          'busy_processes column is empty, unlike original protocol description',
          'Controller has no explicit five-second settle delay before each gate',
          'Gate failure attempts are logged periodically, not on every failed attempt',
          'Fresh and cache-loss trials use only key1; only two deterministic fixture keys in hot cells',
          'Commit metadata start/end are whole-second UTC; gate log carries finer precision',
          'Recorded CurrentMhz does not measure instantaneous hardware cycles or turbo frequency',
          'No security-normalized or compiler/backend-equivalent ranking follows']}
(OUT/'VALIDATED_STABILITY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
lines=[
 '# Independent numerical review: stability campaign b1',
 '',
 '**Verdict: elapsed-statistics PASS; experimental-control claims require the qualifications below.** The campaign is complete as a retained set of 72 scheduled jobs. Every per-job and pooled elapsed-latency statistic printed in its two result CSVs agrees with independent recomputation at the reported precision. Three workload-mean presentation roundings differ by 0.1 percentage point as detailed below, without changing a gate or contamination decision. This is an implementation comparison under a declared workload gate, not an equivalent-backend or common-security ranking.',
 '',
 'Reviewed PROTOCOL.md (including Amendment 1), RUNS.md, all 72 job CSV/process records, gate.jsonl, sampler.csv, all six shuffled-order manifests, analysis/controller/sampler/verifier scripts, results and 36 saved vectors. No benchmark was rerun. No campaign file, cache file, public manuscript or measurement was changed. The existing independent Python verifier was loaded read-only to replay verification and its two bit-flip controls, without running the campaign scripts that write to raw/results.',
 '',
 'Exact unrounded nanosecond statistics, per-block medians, key assignments, telemetry, gates, vector results and source-file SHA-256 hashes are in VALIDATED_STABILITY.json. The companion independent_stability.py reproduces this audit and writes only in its own editorial folder. Cache files were neither copied nor loaded.',
 '',
 '## Completion, sample counts, keys and order',
 '',
 '- 54 hot jobs: 6 blocks × 3 implementations × 3 message lengths. LULA I and SHA2-128f have 1,000 signing and 1,000 verification observations per job; SHA2-128s has 200 each. All expected counts match.',
 '- 15 fresh jobs: five in each of three windows; one fixture load, one signing interval, one verification interval per job. Three cache-loss jobs: one recorded first signing interval per separate process, with distinct PIDs 16244, 10556 and 37924.',
 '- All 72 records say completed, exit code zero, logical processor 10, affinity mask 1024, BelowNormal priority, and 2.75 GiB committed-memory ceiling. Key-2 preparation is an additional setup process outside this 72-job count.',
 '- LULA I uses key 1 in blocks 1, 3, 5 and key 2 in blocks 2, 4, 6. Each hot message-length/operation cell therefore has three blocks for each of two distinct public keys, not six independent keys. Recovery uses key 1 only.',
 '- Every saved shuffled order agrees with process-start order. Seeds are 20261012 + block number, rather than one identically replayed shuffle. Inter-block gaps from retained whole-second timestamps are 186, 195, 234, 180 and 226 seconds.',
 '',
 '## Independently recomputed pooled elapsed times',
 '',
 'Milliseconds. Midpoint median for even N; p95/p99 use nearest rank. Every maximum below is an observed maximum. Per-block exact statistics are retained in JSON, rather than discarded behind these pooled summaries.',
 '',
 '| Implementation | Message B | Operation | N | Min | Median | p95 | p99 | Observed max | Declared verdict |',
 '|---|---:|---|---:|---:|---:|---:|---:|---:|---|'
]
for c in cellout:
    p=c['pooled'];label={'lula':'LULA I, prepared','slh128f':'OpenSSL SHA2-128f','slh128s':'OpenSSL SHA2-128s'}[c['alg']]
    lines.append(f"| {label} | {c['msg']} | {c['op']} | {p['N']} | "+' | '.join(f"{p[k+'_ns']/1e6:.6f}" for k in ['min','median','p95','p99','max'])+f" | {c['verdict']} |")
lines.extend([
 '',
 'All six LULA I cells satisfy the declared stability criterion. Signing block-median spread/mean is 4.195706%, 1.410885% and 2.272409% for 32 B, 1 KiB and 64 KiB. Corresponding maximum block p99/median ratios are 2.635346, 1.777765 and 2.609198. The two unstable cells are SHA2-128s verification at 1 KiB and 64 KiB: their maximum block p99/median ratios are 3.372464 and 3.426218. They are retained, not excluded.',
 '',
 'This verdict requires at least four clean gated blocks, median spread/mean ≤5%, and each block p99 ≤3× its median. All six blocks passed the gate for every hot cell; the analyzer does not itself consume gate.jsonl in its verdict logic, but this audit separately verified every pass. That missing generic gate linkage does not change the present verdicts because all 72 actual job gates are present and pass. Stable medians/p99 do not imply small or bounded maxima: substantial isolated observed maxima remain in the raw data and pooled table.',
 '',
 'The descriptive key-effect ratios are computed from the medians of three block medians per fixture key. This is not a population estimate over independently sampled keys, nor a causal key-effect test; key alternates with block time.',
 '',
 '## Restart and complete cache loss',
 '',
 '- Fresh-process N=15: load median **5.6962471 s**, observed range **5.5610664–6.0908076 s**; first signing median **3.5796 ms**, range **3.5377–3.8098 ms**.',
 '- Per-process paired load-plus-first-signature median **5.7000569 s**, range **5.5646460–6.0943592 s**. The pair is calculated within each same process before taking the median. This is not the sum of marginal medians. OS launch is outside these API intervals.',
 '- Separate-process cache-loss first-signature observations: **331.8369642 s**, **337.5630796 s**, **330.0493122 s**. Each job contains exactly one recorded signing interval; seed/root loading is separately 0.1509, 0.1362 and 0.1204 ms. Three points warrant reporting each value, not claiming a dependable latency distribution or worst-case bound.',
 '',
 '## Workload gate and actual sampling',
 '',
 '- Recomputed all 72 passing gates from the previous 20 seconds of the retained sampler. Every gate has at least three rows; total busy-time mean ≤30%, logical-10 mean ≤8%, logical-11 mean ≤8%. Means also agree with each rounded logged gate value. Zero gate-timeout records exist.',
 '- Whole-process telemetry spans have 5–337 rows. Independently applying contamination rules finds zero contaminated jobs: maximum total mean is 14.491667%, maximum sibling mean 6.533333%. The maximum individual sibling sample is 31.2%; the sibling was not completely idle throughout every job.',
 '- Sampler has **12,737 rows**, spanning 16:56:39.355638–20:29:07.536262 UTC. Inter-sample gaps: median **1.000777 s**, minimum **1.000236 s**, maximum **2.010287 s**; one gap exceeds two seconds. Nominal 1 Hz is supported by observed cadence, but subsecond contention cannot be excluded.',
 '- These telemetry means use the runner start/end interval, including fixture loads and other process setup, not only the timed signing/verification phase. A short spike may be diluted by loading or by a long call. Each row measures the busy fraction accumulated since the preceding sample, not an instantaneous point measurement; boundary rows can include up to roughly one sample interval outside the nominal process interval.',
 '- The runner timestamps are whole-second UTC; gate records have subsecond timestamps. Computed start-minus-gate can appear as low as −0.930074 s because of flooring, although the controller invokes the runner after gate acceptance. Do not infer time travel or precise subsecond alignment from these records.',
 '- Three jobs show a one-decimal presentation difference depending on floating-point summation versus statistics.mean: b4-lula-k2-32 sibling mean is exactly 3.45% (CSV 3.5; independent float format 3.4), w2-fresh-0 total exactly 9.05% (CSV 9.0; independent 9.1), and w2-fresh-4 total exactly 8.45% (CSV 8.5; independent 8.4). These are repeated across three operation rows each. Exact means derived from the retained decimal samples are included as rationals in JSON; no raw observation or contamination status was altered. Do not mistake these formatting ties for changed workload thresholds.',
 '',
 '## Protocol discrepancies and limits that must accompany publication',
 '',
 '1. The replacement Python sampler measures **CPU busy-time fractions** from idle/kernel/user deltas. It does not measure the frequency-scaled processor “utility” of the original WMI sampler. Retain the actual measurement definition when stating the amended gate; do not call this a measured Task Manager utility guarantee.',
 '2. The actual busy_processes column is empty in every row. The protocol originally promised names/counts of processes above 3% CPU, but the replacement sampler explicitly does not collect them. Therefore this campaign cannot attribute an outlier to a named competing process.',
 '3. No explicit five-second settle sleep exists in the final controller before each gate. The preceding-20-second mean gate is real and verified, but the separate “after a 5-second settle” procedure is not implemented as written. Do not assert literal full-protocol compliance.',
 '4. Failed gate attempts are logged every twentieth qualifying attempt, not every failed decision. Every successful job pass is logged. Failed attempts from the first busy-machine controller are retained separately and were not pooled into the measured campaign.',
 '5. The sampler records reported CurrentMhz values of 1,500 or 2,000 MHz from the Windows power-information API. This is not a direct cycle counter, nor proof of invariant instantaneous/turbo frequency. Temperature, power throttling, scheduler interruptions and subsecond workloads are not fully controlled.',
 '6. “Zero contaminated” means none exceeded the declared **mean** thresholds and minimum-row rule; it does not certify absent noise or uninterrupted core exclusivity. The measured job itself is expected to occupy logical 10, so contamination uses total and sibling means, not a low in-job logical-10 requirement.',
 '7. Two deterministic fixture keys and repeated message schedules improve coverage over the earlier one-key campaign but do not establish a distribution over production keys. OpenSSL and Rust compiler/hash backends remain different; no security-normalized superiority claim follows.',
 '',
 '## Independent vector verification and byte invariance',
 '',
 'Replayed **36/36 saved vector files** with the existing independent Python verifier: each valid vector accepted; each tested message-bit flip and signature-byte flip rejected. Every signature is 5,720 bytes. These are the first retained vectors from jobs, not independent replay of all 18,018 LULA I timing repetitions.',
 '',
 'Grouped by the complete public key (seed plus root) and complete message, yielding six groups. Every group has exactly one distinct serialized signature. Key 1/32 B has 21 vectors: three prepared jobs, fifteen fresh jobs and three cache-loss jobs. The other five groups each have three prepared vectors. Therefore same-key/message equality across all three cache regimes is directly established for key 1 at 32 B; hot repeat equality is established for both keys at all three message lengths. Do not extend cross-regime coverage to key 2 or larger-message recovery that was not run.',
 '',
 'All sign/verify CSV validity fields are successful. The retained OpenSSL negative-control sentinel rows are excluded from latency aggregation. Verification controls remain finite correctness checks; they do not supply a cryptographic reduction, adaptive rollback forgery analysis, or universal cache integrity guarantee.',
 '',
 '## Publication-safe formulation',
 '',
 'A separate six-block follow-up campaign used a recorded preceding-load gate and approximately one-second telemetry. Under its declared median-spread and per-block p99 criterion, all LULA I prepared cells were stable across two fixture keys, with pooled signing medians 3.5917, 3.56105 and 3.6371 ms. Its fresh-process load-plus-first-signature median was 5.7000569 seconds over fifteen processes; three independently launched cache-loss jobs recorded 330.0493122–337.5630796 seconds each. These observations supplement rather than overwrite the earlier loaded-host campaign, and retain the formal security-bound and backend-comparability limitations.',
 '',
 'No proof status, construction, parameter, or prior measurement is changed by this audit. Exact result reconciliation is complete; full experimental-protocol compliance is qualified by the documented differences above.'
])
(OUT/'NUMERICAL_REVIEW.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
assert len(jobs)==72 and all(j['status']=='completed' and j['exit_code']==0 and j['metadata_pinning_pass'] and j['expected_sign_verify_counts_pass'] and j['gate_pass_record'] for j in jobs)
assert len(gate_checks)==72 and all(g['thresholds_pass'] for g in gate_checks)
assert all(c['all_printed_statistics_match'] for c in comparisons) and all(c['matches'] for c in cellchecks)
assert len(vectorresults)==36 and all(r['valid'] and r['changed_message_rejected'] and r['changed_signature_rejected'] for r in vectorresults)
assert all(g['distinct_signatures']==1 for g in vg)
print(json.dumps({'jobs':len(jobs),'all_completed_zero':all(j['status']=='completed' and j['exit_code']==0 for j in jobs),
 'contaminated':sum(j['contaminated'] for j in jobs),'all_gate_records':all(j['gate_pass_record'] for j in jobs),'gate_recomputed_pass':sum(g['thresholds_pass'] for g in gate_checks),
 'job_stats_mismatch':sum(not c['all_printed_statistics_match'] for c in comparisons),'cell_mismatch':sum(not c['matches'] for c in cellchecks),
 'vectors':len(vectorresults),'all_vectors_pass':all(r['valid'] and r['changed_message_rejected'] and r['changed_signature_rejected'] for r in vectorresults),
 'groups':len(vg),'all_groups_identical':all(g['distinct_signatures']==1 for g in vg),'sampler':result['sampler_summary']},indent=2))
