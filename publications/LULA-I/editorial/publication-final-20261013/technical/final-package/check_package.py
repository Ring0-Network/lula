"""Independent read-only delivery check; generated work stays beside this file."""
from pathlib import Path, PurePosixPath
import collections, hashlib, json, re, subprocess, sys, zipfile
import fitz

P=Path(r'C:\Users\angel\Desktop\paper\PAPERS\LUGEL\research\lula22\publications\LULA-I')
O=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
hashfile=lambda p:sha(p.read_bytes())
expected={'LULA-I-source.zip':'0ee172e6b85b983c6cc4995ba48f826323717d0fe58eab57ce1eddf2cac7d140','LULA-I-release.zip':'6546da0a82bae701816ec45b05b7060413a3784c0109d884f76a600bae21cb29','LULA-I.pdf':'bc805dcfd00c4f8b489efba80311cb49fde8835618c719a4136b288484966110'}
for f,h in expected.items(): assert hashfile(P/f)==h, f
root=P/'editorial/publication-final-20261013/root'
pack=json.loads((root/'PACKAGING.json').read_text())
for f,rec in pack['deliverables'].items():
    if f!='LULA-I.pdf': assert hashfile(P/f)==rec['sha256'] and (P/f).stat().st_size==rec['bytes']
def manifest(data):
    pairs=[s.split('  ',1) for s in data.decode('utf8').splitlines()]
    assert len({rel for h,rel in pairs})==len(pairs)
    return {rel:h for h,rel in pairs}
baseline=manifest((P/'editorial/publication-final-20261013/baseline/release-EVIDENCE-MANIFEST.sha256').read_bytes())
def safe_names(z):
    names=z.namelist(); assert len(names)==len(set(names))
    for name in names:
        pp=PurePosixPath(name)
        assert not pp.is_absolute() and '..' not in pp.parts and '\\' not in name and ':' not in name
        assert not any(x in {'private','__pycache__','target','.git','recomputed','build','generated','reruns','output'} for x in pp.parts),name
        assert pp.suffix not in {'.aux','.log','.out','.blg','.cache','.fixture','.pyc','.pem','.key','.exe','.dll','.pdb'},name
    return names
with zipfile.ZipFile(P/'LULA-I-source.zip') as z:
    names=safe_names(z)
    assert set(names)==set(pack['source_members']) and len(names)==9
    for name in names:
        if name!='README.txt': assert z.read(name)==(P/name).read_bytes(),name
    tex=z.read('LULA-I.tex').decode('utf8')
    closure={'LULA-I.tex'}
    todo=['LULA-I.tex']
    while todo:
        name=todo.pop(); t=z.read(name).decode('utf8')
        for inc in re.findall(r'\\(?:input|include)\{([^}]+)\}',t):
            inc=inc if inc.endswith('.tex') else inc+'.tex'
            assert inc in names
            if inc not in closure: closure.add(inc); todo.append(inc)
    for bib in re.findall(r'\\bibliography\{([^}]+)\}',tex):
        assert all(v+'.bib' in names for v in bib.split(','))
    assert not re.search(r'\\includegraphics',tex), 'Unexpected external image dependency'
    source=dict(entries=names,tex_closure=sorted(closure),all_existing_members_byte_identical=True)
with zipfile.ZipFile(P/'LULA-I-release.zip') as z:
    names=safe_names(z); mf=manifest(z.read('MANIFEST.sha256')); ev=manifest(z.read('EVIDENCE-MANIFEST.sha256'))
    assert len(names)==887 and len(mf)==886 and len(ev)==872
    assert set(names)==set(mf)|{'MANIFEST.sha256'}
    assert set(ev)==set(baseline)
    for rel,h in mf.items(): assert sha(z.read(rel))==h, rel
    for rel,h in ev.items(): assert sha(z.read(rel))==h, rel
    changes={rel:dict(before=h,after=ev[rel]) for rel,h in baseline.items() if h!=ev[rel]}
    assert changes==pack['evidence_changes']
    assert set(changes)=={'README.md','code/models/verify_paper_models.py'}
    assert sha(z.read('code/lula1/src/lib.rs'))=='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
    main=(P/'LULA-I.tex').read_text(encoding='utf8'); repo=z.read('paper/LULA-I.tex').decode('utf8')
    diffs=[]
    a,b=main.splitlines(),repo.splitlines(); assert len(a)==len(b)
    for i,(x,y) in enumerate(zip(a,b),1):
        if x!=y: diffs.append(dict(line=i,main=x,repository=y))
    assert [x['line'] for x in diffs]==[40],diffs
    # Exact permitted change: omit contact line, with no technical body change.
    assert main.replace(r'\email{angel@r-0.org}\\','')==repo
    for f in ['references.bib','operating-model.tex','stability-results.tex','comparison-results.tex','replay-results.tex','LULA-I.bbl']:
        assert z.read('paper/'+f)==(P/f).read_bytes(),f
    text_ext={'.md','.txt','.json','.csv','.py','.rs','.c','.h','.go','.toml','.lock','.tex','.bib','.bbl','.sha256','.html','.ps1','.sh'}
    host_hits=[]; material_hits=[]; sensitive_fields=[]
    for name in names:
        if PurePosixPath(name).suffix in text_ext:
            raw=z.read(name)
            if re.search(rb'(?i)(?:C:\\Users\\|C:/Users/|/home/[^/\s]+/|angel@r-0\.org)',raw): host_hits.append(name)
            if re.search(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',raw): material_hits.append(name)
            if PurePosixPath(name).suffix=='.json':
                try: data=json.loads(raw)
                except (ValueError,UnicodeDecodeError): continue
                def walk(v,path=''):
                    if isinstance(v,dict):
                        for k,w in v.items():
                            if re.search(r'(?i)^(?:sk_seed|sk_prf|master_seed|secret_key|private_key|seed_hex|sk_hex)$',k) and isinstance(w,str) and re.fullmatch('[0-9a-fA-F]{32,}',w): sensitive_fields.append([name,path+k])
                            walk(w,path+k+'.')
                    elif isinstance(v,list):
                        for i,w in enumerate(v):walk(w,path+str(i)+'.')
                walk(data)
    assert host_hits==material_hits==sensitive_fields==[],(host_hits,material_hits,sensitive_fields)
    unpack=O/'unpacked-release'
    # Safe, verified names only, copied within this reviewer's authorized subtree.
    for name in names:
        target=unpack.joinpath(*PurePosixPath(name).parts)
        target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(z.read(name))
    release=dict(members=len(names),manifest_entries=len(mf),evidence_entries=len(ev),evidence_changes=changes,unchanged_evidence_entries=len(ev)-len(changes),tex_differences=diffs,host_path_hits=host_hits,private_key_block_hits=material_hits,secret_hex_json_fields=sensitive_fields)
commands=[]
for script in ['analyze.py','code/models/verify_paper_models.py','code/models/verify_paper_tables.py','check_manifest.py']:
    argv=[sys.executable,'-I','-B',script]
    p=subprocess.run(argv,cwd=unpack,capture_output=True,text=True)
    commands.append(dict(argv=argv,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode==0,commands[-1]
model=json.loads((unpack/'recomputed/models.json').read_text())
assert model['checked_component_table_scope']=={'article':'current mechanism paper','checked_rows':3,'separate_archived_rows':22}
mainpdf=fitz.open(P/'LULA-I.pdf'); repopdf=fitz.open(unpack/'paper/LULA-I.pdf')
assert len(mainpdf)==len(repopdf)==21
pdfchecks=[]
for i,(m,r) in enumerate(zip(mainpdf,repopdf)):
    mt,rt=m.get_text(),r.get_text()
    mp,rp=m.get_pixmap(matrix=fitz.Matrix(1,1)),r.get_pixmap(matrix=fitz.Matrix(1,1))
    same=mp.samples==rp.samples and mp.width==rp.width and mp.height==rp.height
    if i: assert same and mt==rt,i
    else:
        assert 'angel@r-0.org' in mt and 'angel@r-0.org' not in rt
        assert mt.replace('angel@r-0.org\n','')==rt
        mp.save(O/'main-page-01.png'); rp.save(O/'repository-page-01.png')
    pdfchecks.append(dict(page=i+1,text_identical=mt==rt,pixels_identical=same))
assert 'angel@r-0.org' not in str(repopdf.metadata)
result=dict(status='PASS_LOCAL_PACKAGE_WITHIN_MECHANISM_SCOPE',deliverable_sha256=expected,packaging_json_sha256=hashfile(root/'PACKAGING.json'),source=source,release=release,commands=commands,model_scope=model['checked_component_table_scope'],pdf=dict(pages=21,checks=pdfchecks,first_page_text_diff_only_contact=True,main_metadata=mainpdf.metadata,repository_metadata=repopdf.metadata),new_signing_keygen_benchmark_or_attack_runs=0,retained_public_vector_replays=36,retained_vector_bitflip_checks=72,remote_publication=False,full_signature_security_established=False,whole_goal_complete=False)
result['packaging_pdf_pin_current']=pack['deliverables']['LULA-I.pdf']['sha256']==expected['LULA-I.pdf'] and pack['deliverables']['LULA-I.pdf']['bytes']==(P/'LULA-I.pdf').stat().st_size
if not result['packaging_pdf_pin_current']: result['status']='ALL_CONTENT_CHECKS_PASS_AWAITING_ROOT_PDF_INDEX_REFRESH'
(O/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(status=result['status'],members=release['members'],manifest_entries=release['manifest_entries'],evidence_entries=release['evidence_entries'],changed_evidence=list(changes),commands=[dict(script=c['argv'][-1],exit_code=c['exit_code']) for c in commands],model_scope=result['model_scope'],pdf_pages=21,checks_sha256=hashfile(O/'CHECKS.json')),indent=2))
