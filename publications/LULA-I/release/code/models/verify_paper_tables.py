"""Check current-paper rows and archived extended rows separately; no new benchmarks.

SPDX-License-Identifier: Apache-2.0. Summary-source and specification checks
remain distinct from reaggregation of raw per-call observations.
"""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
SOURCE_NAMES=['LULA-I.tex','comparison-results.tex','stability-results.tex','operating-model.tex','replay-results.tex']
def load(p):return json.loads(p.read_text(encoding='utf8'))
def norm(t):return re.sub(r'\s+','',t)
def collect_tables(directory):
    sources={n:(directory/n).read_text(encoding='utf8') for n in SOURCE_NAMES}
    tables={}
    for name,text in sources.items():
        for body in re.findall(r'\\begin\{table\*?\}.*?\\end\{table\*?\}',text,re.S):
            label=re.search(r'\\label\{(tab:[^}]+)\}',body)[1]
            assert label not in tables, ('Duplicate table label',label,directory)
            tables[label]={'file':name,'body':body,'sha256':hashlib.sha256(body.encode('utf8')).hexdigest()}
    return sources,tables
def audit_archival():
    paper=ROOT/'docs/research/extended-evaluation/source'
    sources,tables=collect_tables(paper)
    assert len(tables)==21
    a=load(ROOT/'recomputed/data/RECOMPUTED_DATA.json'); b=load(ROOT/'recomputed/stability-audit/VALIDATED_STABILITY.json')
    checks=[]
    def row(label,prefix,values,kind='RAW_REAGGREGATION'):
        expected=prefix+' & '+' & '.join(str(v) for v in values)
        assert norm(expected) in norm(tables[label]['body']), (label,expected)
        checks.append({'table':label,'row':prefix,'values':values,'evidence_class':kind,'status':'PASS'})
    data={(r['cell'],r['operation']):r for r in a['a1']['admitted_cells']}
    for label,candidates in [('tab:comparison-latencies',[('lula1-hot','L'),('slh128f','F'),('slh128s','S')]),('tab:comparison-b32',[('shrincsC-stateful','SF'),('shrincsC-fallback','FB')]),('tab:comparison-kn',[('kn3952-recon-hot','R'),('kn4036-prepared','G')])]:
        for stem,display in candidates:
            for size,message in [(32,'32 B'),(1024,'1 KiB'),(65536,'64 KiB')]:
                for op,symbol in [('sign','S'),('verify','V')]:
                    r=data[stem+'-'+str(size),op]
                    row(label,display+'/'+message+' & '+symbol,[r['N']]+[f"{r[k]/1e6:.3f}" for k in ['min','median','p95','p99','max_observed']])
    for r in a['a1']['branches']:
        row('tab:comparison-branches',('32 B' if r['message_bytes']==32 else '1 KiB')+'/'+r['branch'],[r['N']]+[f"{r[k]/1e6:.3f}" for k in ['min','median','p95','p99','max_observed']])
    names={'lula1':'LULA I, full cache','shrincsC':'C B32, key/state','kn3952-recon':'KN-R, key material','kn4036':'KN-G, key material'}
    for r in a['a1']['fresh']:
        row('tab:comparison-fresh',names[r['candidate']],[r['load']['N']]+[f"{r[k]['median']/1e6:.3f}" for k in ['load','first_sign','paired_load_sign']])
    names=['LULA I, prepared','SLH-DSA SHA2-128f','SLH-DSA SHA2-128s','C B32, stateful','C B32, forced fallback','KN-R reconstruction','KN-G third-party']
    for name,r in zip(names,a['a1']['memory']):row('tab:comparison-memory',name,[f"{r[k]/2**20:.3f}" for k in ['working_set_bytes','private_bytes']])
    for r in a['historical']:
        if 'values_ms' in r: continue
        title=r['scenario'].replace('Lifecycle prepared','Lifecycle prepared').replace('Lifecycle restored','Lifecycle restored')
        row('tab:history',title,[r['n']]+[f"{r[k]:.3f}" for k in ['min','median','p99','max']], 'SUMMARY_SOURCE_ONLY')
    cold=next(r for r in a['historical'] if 'values_ms' in r)['values_ms'][0]
    assert f'{cold:,.3f}' in tables['tab:history']['body']
    for r in b['cells']:
        symbol={'lula':'L','slh128f':'F','slh128s':'S'}[r['alg']]; op='S' if r['op']=='sign' else 'V'
        msg={32:'32 B',1024:'1 KiB',65536:'64 KiB'}[r['msg']]; p=r['pooled']
        vals=[p['N'],f"{p['min_ns']/1e6:.4f}",f"{p['median_ns']/1e6:.4f}",f"{100*r['spread_over_mean']:.2f}"]+[f"{p[k]/1e6:.4f}" for k in ['p95_ns','p99_ns','max_ns']]
        row('tab:stability-latencies',symbol+'/'+msg+' & '+op,vals)
        vals=[f"{r['block_median_min_ns']/1e6:.4f}--{r['block_median_max_ns']/1e6:.4f}",f"{100*r['spread_over_mean']:.2f}",f"{r['max_p99_over_median']:.3f}",f"{100*r['key_effect']:.2f}" if r['key_effect'] is not None else '--',r['verdict']]
        row('tab:stability-verdicts',symbol+'/'+str(r['msg'])+' B & '+op,vals)
    for display,key in [('Fresh process: cache load','fixture_load'),('Fresh process: first Sign','sign'),('Paired load plus first Sign','paired_load_sign')]:
        r=b['fresh'][key];row('tab:stability-recovery',display,[r['N']]+[f"{r[k]/1e9:.7f}" for k in ['min_ns','median_ns','max_ns']])
    for r in b['cache_loss_first_calls']:assert f"{r['first_sign_ns']/1e9:.7f}" in tables['tab:stability-recovery']['body']
    r=a['publication_replay'];row('tab:replay','Verification (ms)',[f"{r[k]/1e6:.4f}" for k in ['min','median','p95','p99','max_observed']])
    r=next(r for r in a['a1']['fresh'] if r['candidate']=='lula1')
    for display,key in [('Fresh process: fixture load','load'),('Fresh process: first Sign after load','first_sign'),('Paired load plus first Sign','paired_load_sign')]:
        z=r[key];row('tab:comparison-recovery',display,[z['N'],f"{z['median']/1e9:.6f}",f"{z['min']/1e9:.6f}--{z['max_observed']/1e9:.6f}"])
    for z in a['a1']['cache_loss_consecutive_calls']:assert f"{z['ns']/1e9:.6f}" in tables['tab:comparison-recovery']['body']
    model=load(ROOT/'recomputed/models.json')
    for r in model['wire']:
        assert re.search(r'&\s*'+str(r['offset'])+r'\s*&\s*'+str(r['bytes'])+r'\\',tables['tab:wire']['body'])
    for display,values in [('Randomizer',[x[0] for x in model['components'].values()]),('FORS-family evidence',[x[1] for x in model['components'].values()]),('Hypertree chain values',[x[2] for x in model['components'].values()]),('Hypertree authentication',[x[3] for x in model['components'].values()]),('Explicit search counters',[x[4] for x in model['components'].values()]),('Total',[sum(x) for x in model['components'].values()])]:
        row('tab:comparison-bytes',display,[f'{v:,}' if v>=1000 else v for v in values], 'DERIVED_ARITHMETIC')
    for display,key in [('Message inner hash and outer digest','message_digest_m32'),('FORS leaves, paths, and root compression','fors_leaves_paths_root'),('Four lower WOTS+C reconstructions and paths','lower_wots_paths'),('Top WOTS+C reconstruction and path','top_wots_path')]:
        row('tab:work',display,[model['verification_compressions'][key]],'DERIVED_ARITHMETIC')
    row('tab:work','Instrumented total',[model['instrumented_total']],'DERIVED_ARITHMETIC')
    row('tab:work','Prefix-context initialization',[1],'DERIVED_ARITHMETIC')
    row('tab:work','Executed total',[model['executed_total']],'DERIVED_ARITHMETIC')
    for i,display in enumerate(['Sibling component root','Randomizers','Few-time revealed secrets','Few-time authentication','Hypertree chain values','Hypertree authentication','Layer search counters']):
        values=[x[i] for x in model['auxiliary_components'].values()]
        row('tab:comparison-aux-bytes',display,[f'{v:,}' if v>=1000 else v for v in values],'DERIVED_FROM_SOURCE_ALLOCATION')
    row('tab:comparison-aux-bytes','Total',[f'{sum(x):,}' for x in model['auxiliary_components'].values()],'DERIVED_FROM_SOURCE_ALLOCATION')
    overview=re.sub(r'\\textsuperscript\{[^}]+\}','',tables['tab:comparison-overview']['body'])
    for cell in ['lula1-hot-32','slh128s-32','slh128f-32','shrincsC-stateful-32','shrincsC-fallback-32','kn3952-recon-hot-32','kn4036-prepared-32']:
        s=data[cell,'sign'];v=data[cell,'verify']; sizes=s['signature_bytes']; size=f'{sizes[0]:,}' if len(sizes)==1 else f'{min(sizes):,}--{max(sizes):,}'
        expected=' & '.join([size,'32',f"{s['median']/1e6:.3f}",f"{v['median']/1e6:.3f}",str(s['N'])])
        assert norm(expected) in norm(overview),(cell,expected)
        checks.append({'table':'tab:comparison-overview','row':cell,'values':expected,'evidence_class':'RAW_MEASURED_FIELDS_ONLY','status':'PASS'})
    # Recover fixed parameter fields from the retained historical source tuple.
    history=load(ROOT/'data/history/session-a.json')
    fors,layer_spec=history['spec'].split(';')
    k,aheight,forced=map(int,fors.split(','))
    layers=[list(map(int,x.split(':'))) for x in layer_spec.split('|')]
    n=model['public_key_bytes']//2
    low,top=layers[0],layers[-1]
    assert all(x==low for x in layers[:-1]) and len(layers)==5
    for title,spec in [('Layers 0--3, each',low),('Layer 4',top)]:
        h,bits,unused,target,cache=spec
        row('tab:params',title,[h,bits,2**bits,8*n//bits,target,'Yes' if cache else 'No'],'PARAMETER_SOURCE_TUPLE')
    row('tab:params','Node bytes $n$',[n,'Total height $h$',sum(x[0] for x in layers)],'PARAMETER_SOURCE_TUPLE')
    row('tab:params','FORS digest trees $k$',[k,'FORS height $a$',aheight],'PARAMETER_SOURCE_TUPLE')
    row('tab:params',"Transmitted trees $k'$",[k-forced,'Hypertree layers $d$',len(layers)],'PARAMETER_SOURCE_TUPLE')
    assert f"{model['signature_bytes']:,}-byte format" in tables['tab:falsifiers']['body']
    assert f"{model['executed_total']:,} executed verification compressions" in tables['tab:falsifiers']['body']
    assert '32-byte message' in tables['tab:falsifiers']['body']
    checks.append({'table':'tab:falsifiers','row':'Numeric constants only','values':[model['signature_bytes'],model['executed_total'],32],'evidence_class':'DERIVED_CONSTANTS_IN_QUALITATIVE_CLAIMS','status':'PASS'})
    contexts=tables['tab:execution-contexts']['body']
    assert '2,000 / 1,000 / 200; cold 1' in contexts
    assert [load(ROOT/'data/history'/f)[field]['n'] for f,field in [('session-a.json','sign_ms'),('session-b.json','sign_ms'),('lifecycle.json','prepared_ms')]]==[2000,1000,200]
    assert a['publication_replay']['N']==1000 and '1,000 verifies' in contexts
    assert [data[c,'sign']['N'] for c in ['lula1-hot-32','slh128f-32','slh128s-32','shrincsC-stateful-32','shrincsC-fallback-32','kn3952-recon-hot-32','kn4036-prepared-32']]==[1000,1000,100,200,20,20,12]
    assert 'L/F: 1,000; S: 100; SF: 200; FB/R: 20; G: 12' in contexts
    assert all(r['blocks_total']==6 and all(z['N']==(200 if r['alg']=='slh128s' else 1000) for z in r['blocks']) for r in b['cells'])
    assert 'L/F: 1,000/block; S: 200/block; six blocks' in contexts
    checks.append({'table':'tab:execution-contexts','row':'Sample-count fields','values':'History source counts; replay 1000; a1 32-byte counts; b1 six blocks','evidence_class':'SOURCE_COUNTS_AND_RAW_REAGGREGATION','status':'PASS'})
    digest_files=list((ROOT/'data').rglob('binary-digests.txt'))
    known=set(re.findall(r'(?i)\b[0-9a-f]{64}\b','\n'.join(f.read_text(encoding='utf8') for f in digest_files)))
    displayed=[''.join(parts) for parts in re.findall(r'D[1-6]\s*&\s*([0-9a-f]{32})\s*&\s*([0-9a-f]{32})',sources['LULA-I.tex'])]
    assert len(displayed)==6 and set(displayed)<=known
    # Remaining tables combine specification fields, observed lengths, query-count
    # targets and nonnumeric claim prose. They need the documented source map.
    touched={r['table'] for r in checks}|{'tab:wire','tab:security-model'}
    remaining=[label for label in tables if label not in touched]
    assert len(checks)==141, ('Changed archival checking scope',len(checks))
    return {'status':'PASS_ARCHIVED_EXTENDED_ROWS','checked_rows':len(checks),'table_count':21,'checks':checks,'table_body_hashes':{k:{'file':v['file'],'sha256':v['sha256']} for k,v in tables.items()},'source_hashes':{n:hashlib.sha256((paper/n).read_bytes()).hexdigest() for n in SOURCE_NAMES},'source_mapped_additional_tables':remaining,'source_directory':str(paper.relative_to(ROOT)),'scope':'ARCHIVAL long-manuscript rows only. Direct raw reaggregation, derived arithmetic and explicitly summary-source checks. Additional parameter/specification/claim tables use their source map; these are not current-paper tables, new measurements or proofs.'}

def tabular_rows(body):
    """Parse these simple retained tables, rejecting unknown row material."""
    rows=[]
    for segment in re.findall(r'\\begin\{tabular\}(.*?)\\end\{tabular\}',body,re.S):
        assert r'\toprule' in segment
        chunks=segment.split(r'\toprule',1)[1].split(r'\\')
        for chunk in chunks[:-1]:
            chunk=re.sub(r'\\(?:midrule|bottomrule|hline)\b','',chunk).strip()
            assert '&' in chunk, ('Unexpected retained row',chunk)
            rows.append([norm(cell) for cell in chunk.split('&')])
        tail=re.sub(r'\\(?:midrule|bottomrule|hline)\b','',chunks[-1]).strip()
        assert not tail, ('Unterminated or unaccounted retained row',tail)
    assert rows, 'No retained tabular rows'
    return rows

def audit_current():
    sources,tables=collect_tables(ROOT/'paper')
    labels={'tab:params','tab:wire','tab:work','tab:security-model','tab:eval-warm','tab:eval-aux'}
    assert set(tables)==labels, ('Unexpected current-paper tables',set(tables)^labels)
    assert not any(re.search(r'\\begin\{(?:longtable|tabularx|tabular\*)\}',text) for text in sources.values()), 'Unsupported retained table environment'
    assert sum(text.count(r'\begin{tabular}') for text in sources.values())==sum(t['body'].count(r'\begin{tabular}') for t in tables.values()), 'Tabular outside accounted current table'
    a=load(ROOT/'recomputed/data/RECOMPUTED_DATA.json')
    b=load(ROOT/'recomputed/stability-audit/VALIDATED_STABILITY.json')
    model=load(ROOT/'recomputed/models.json')
    expected={label:[] for label in labels};checks=[]
    def header(label,cells):expected[label].append([norm(str(c)) for c in cells])
    def row(label,cells,kind,locator):
        cells=[str(c) for c in cells]
        expected[label].append([norm(c) for c in cells])
        checks.append({'table':label,'row':cells[0],'values':cells[1:],'evidence_class':kind,'input_locator':locator,'status':'PASS'})
    history=load(ROOT/'data/history/session-a.json')
    fors,layer_spec=history['spec'].split(';')
    k,aheight,forced=map(int,fors.split(','));layers=[list(map(int,x.split(':'))) for x in layer_spec.split('|')]
    n=model['public_key_bytes']//2;low,top=layers[0],layers[-1]
    assert all(x==low for x in layers[:-1]) and len(layers)==5
    header('tab:params',['Component','$h_j$','$b_j$','$w_j$',r'$\ell_j$','$S_j$','Cache'])
    for title,spec in [('Layers 0--3, each',low),('Layer 4',top)]:
        h,bits,unused,target,cache=spec
        row('tab:params',[title,h,bits,2**bits,8*n//bits,target,'Yes' if cache else 'No'],'PARAMETER_SOURCE_TUPLE','data/history/session-a.json:spec')
    for cells in [['Node bytes $n$',n,'Total height $h$',sum(x[0] for x in layers)],['FORS digest trees $k$',k,'FORS height $a$',aheight],["Transmitted trees $k'$",k-forced,'Hypertree layers $d$',len(layers)]]:
        row('tab:params',cells,'PARAMETER_SOURCE_TUPLE','data/history/session-a.json:spec')
    header('tab:wire',['Field','Offset','Bytes'])
    wire_titles=['Randomizer $R$','FORS+C counter $c_F$','17 FORS secrets and nine-node paths']+[f'Layer {i}: counter, 32 values, 5 siblings' for i in range(4)]+['Layer 4: counter, 16 values, 21 siblings']
    assert len(model['wire'])==len(wire_titles)
    for title,r in zip(wire_titles,model['wire']):
        row('tab:wire',[title,r['offset'],r['bytes']],'DERIVED_ARITHMETIC',f"recomputed/models.json:wire/{r['field']}")
    row('tab:wire',['Total','',model['signature_bytes']],'DERIVED_ARITHMETIC','recomputed/models.json:signature_bytes')
    header('tab:work',['Operation','Compressions'])
    for title,key in [('Message inner hash and outer digest','message_digest_m32'),('FORS leaves, paths, and root compression','fors_leaves_paths_root'),('Four lower WOTS+C reconstructions and paths','lower_wots_paths'),('Top WOTS+C reconstruction and path','top_wots_path')]:
        row('tab:work',[title,model['verification_compressions'][key]],'DERIVED_ARITHMETIC','recomputed/models.json:verification_compressions/'+key)
    row('tab:work',['Verification subtotal',model['instrumented_total']],'DERIVED_ARITHMETIC','recomputed/models.json:instrumented_total')
    row('tab:work',['Prefix-context initialization',1],'SOURCE_CONTEXT_INITIALIZATION','one fixed context-prefix compression; archived work table')
    row('tab:work',['Total including prefix setup',model['executed_total']],'DERIVED_ARITHMETIC','recomputed/models.json:executed_total')
    header('tab:security-model',['Signing queries',r'$-\log_2 p_{\mathrm{raw}}$'])
    for q in [38,40,41]:
        values=[r for r in model['component_model_rows'] if r['construction']=='LULA I' and r['log2_queries']==q]
        assert len(values)==1
        row('tab:security-model',[f'$2^{{{q}}}$',f"{values[0]['display']:.1f}"],'DERIVED_COMPONENT_MODEL_ONLY',f'recomputed/models.json:component_model_rows/LULA I/{q}')
    cells={(r['alg'],r['msg'],r['op']):r for r in b['cells']}
    assert len(cells)==len(b['cells'])==18
    header('tab:eval-warm',['Implementation','Message','$N$','Sign median','Sign p99','Verify median','Verify p99'])
    for alg,title in [('lula','LULA I'),('slh128f','SHA2-128f'),('slh128s','SHA2-128s')]:
        for msg,display in [(32,'32 B'),(1024,'1 KiB'),(65536,'64 KiB')]:
            sign=cells[alg,msg,'sign']['pooled'];verify=cells[alg,msg,'verify']['pooled']
            assert sign['N']==verify['N']
            values=[title if msg==32 else '',display,sign['N']]+[f'{r[key]/1e6:.4f}' for r,key in [(sign,'median_ns'),(sign,'p99_ns'),(verify,'median_ns'),(verify,'p99_ns')]]
            row('tab:eval-warm',values,'STABILITY_RAW_REAGGREGATION',f'recomputed/stability-audit/VALIDATED_STABILITY.json:cells/{alg}/{msg}/sign+verify/pooled')
    data={(r['cell'],r['operation']):r for r in a['a1']['admitted_cells']}
    header('tab:eval-aux',['Implementation','Signature bytes','$N$','Sign median','Verify median'])
    for cell,title in [('shrincsC-stateful-32','SHRINCS C B32, stateful'),('shrincsC-fallback-32','SHRINCS C B32, forced fallback'),('kn3952-recon-hot-32','Compact C reconstruction'),('kn4036-prepared-32','Compact third-party Go')]:
        sign=data[cell,'sign'];verify=data[cell,'verify'];sizes=sign['signature_bytes']
        assert sign['N']==verify['N']
        size=f'{sizes[0]:,}' if len(sizes)==1 else f'{min(sizes):,}--{max(sizes):,}'
        row('tab:eval-aux',[title,size,sign['N'],f"{sign['median']/1e6:.3f}",f"{verify['median']/1e6:.3f}"],'FIRST_CAMPAIGN_RAW_REAGGREGATION',f'recomputed/data/RECOMPUTED_DATA.json:a1/admitted_cells/{cell}/sign+verify')
    assert len(checks)==37, ('Current checking scope changed',len(checks))
    for label in sorted(labels):
        actual=tabular_rows(tables[label]['body'])
        assert actual==expected[label], ('Retained table rows differ or are unaccounted',label,actual,expected[label])
    return {'status':'PASS_CURRENT_RETAINED_TABLE_ROWS','source_directory':'paper','table_count':len(tables),'checked_rows':len(checks),'checks':checks,'table_body_hashes':{k:{'file':v['file'],'sha256':v['sha256']} for k,v in tables.items()},'source_hashes':{n:hashlib.sha256((ROOT/'paper'/n).read_bytes()).hexdigest() for n in SOURCE_NAMES},'scope':'All retained data rows and headers matched exactly to existing reaggregation/source/model values. Caption and narrative claims are not proved by this checker; FORS values remain component models.'}

def main():
    archival=audit_archival();current=audit_current()
    inputs=['recomputed/data/RECOMPUTED_DATA.json','recomputed/stability-audit/VALIDATED_STABILITY.json','recomputed/models.json','data/history/session-a.json']
    result={'status':'PASS_CURRENT_AND_ARCHIVED_TABLE_SCOPES','current_paper':current,'archived_extended_evaluation':archival,'input_file_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},'scope':'Current-paper and archived checks are separate. No new measurements, mathematical recomputations, or security proofs.'}
    out=ROOT/'recomputed/PAPER_TABLE_CHECKS.json';out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':result['status'],'current_tables':current['table_count'],'current_checked_rows':current['checked_rows'],'archived_tables':archival['table_count'],'archived_checked_rows':archival['checked_rows'],'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
if __name__=='__main__':main()
