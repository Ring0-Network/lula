"""Copy authorized research sources exactly; no cryptographic or benchmark runs.

Run only with explicit --source-root. Existing authoritative files are read-only.
The repository is private; provenance manifests may retain source-machine paths.
"""
from pathlib import Path
import argparse,collections,hashlib,json,os,re,shutil,sys

REPO=Path(__file__).resolve().parents[1]
PRUNE={'target','build','node_modules','.git','__pycache__','.venv','venv','go-cache','deps','vendor','dependencies','dist','unpacked-release','source-archive-build'}
BUILD_SUFFIX={'.exe','.dll','.pdb','.lib','.obj','.o','.a','.so','.dylib','.pyc','.pyo','.cache','.fixture','.aux','.out','.blg','.toc','.fls','.synctex'}
SECRET_NAMES={'.env','.env.local','.env.production','.npmrc','.pypirc','credentials','credentials.json','id_rsa','id_ed25519','id_ecdsa'}
EXTRACTED={'zhandry-tr12-140.txt','jaeger-2511.16009.txt','shadrin-markov.txt','markov-mendeleev-translation.txt','beals-quant-ph-9802049v3.txt','beals-author-polynomials.txt','sphincs-round3-specification.txt','primary-ar-theorem-excerpt.txt','primary-ar-pages.txt','e4-pages.txt','dm-pages.txt'}
PATTERNS={
 'private_key_block':rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
 'github_token':rb'(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})',
 'openai_token':rb'sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{45,}',
 'aws_access_key':rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
 'slack_token':rb'xox[baprs]-[A-Za-z0-9-]{20,}',
 'credential_url':rb'https?://[^\s/:@]+:[^\s/@]+@',
 'stored_secret_hex_field':rb'(?i)"(?:sk_seed|sk_prf|master_seed|secret_key|private_key|seed_hex|sk_hex)"\s*:\s*"[0-9a-f]{32,}"',
}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source-root',type=Path,required=True);args=ap.parse_args();R=args.source_root.resolve()
 if R==REPO or not REPO.is_relative_to(R/'github'):raise ValueError('Expected dedicated authorized research clone')
 records=[];excluded=[];hits=[]
 def omit(src,why,hashed=True):
  z={'source':str(src),'relative_source':src.relative_to(R).as_posix(),'reason':why,'kind':'file' if src.is_file() else 'directory'}
  if hashed and src.is_file():z.update(bytes=src.stat().st_size,sha256=sha(src))
  excluded.append(z)
 def copy(src,category):
  rel=src.relative_to(R);dst=REPO/rel
  if not dst.resolve().is_relative_to(REPO):raise ValueError('Destination escaped repository')
  data=src.read_bytes();before=hashlib.sha256(data).hexdigest()
  for name,pat in PATTERNS.items():
   if re.search(pat,data):hits.append({'path':rel.as_posix(),'pattern':name})
  if hits:return
  dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data)
  if sha(src)!=before or sha(dst)!=before:raise RuntimeError('Source changed or copy mismatch: '+str(rel))
  records.append({'source':str(src),'repository_path':rel.as_posix(),'bytes':len(data),'source_sha256':before,'copy_sha256':before,'category':category})
 def tree(src,category,editorial=False):
  for base,dirs,names in os.walk(src):
   for d in list(dirs):
    if d.lower() in PRUNE or (editorial and ('render' in d.lower() or d.lower().startswith(('fresh-clone','candidate-git')))):
     omit(Path(base,d),'build/dependency/redundant generated working tree',False);dirs.remove(d)
   for name in sorted(names):
    f=Path(base,name);suffix=f.suffix.lower();low=name.lower()
    if low in SECRET_NAMES or low.startswith('.env') or suffix in {'.pem','.key','.p12','.pfx'}:omit(f,'credential or stored key filename');continue
    if suffix in BUILD_SUFFIX or suffix=='.zip':omit(f,'compiled/generated/archive/cache artifact');continue
    if suffix=='.pdf':omit(f,'third-party reference or redundant generated PDF; retain original hash/citation, not redistribution');continue
    if low in EXTRACTED:omit(f,'third-party extracted reference text; retain hash/citation, not full text');continue
    if editorial and suffix in {'.png','.log'}:omit(f,'generated render/build output; source/review receipt retained');continue
    copy(f,category)
 P=R/'publications/LULA-I';S=R/'security/LULA-I-proof-20261012'
 # Curated release: use its authoritative manifest, not unreviewed build dirs.
 manifest=P/'release/MANIFEST.sha256';listed={}
 for line in manifest.read_text(encoding='utf8').splitlines():
  digest,rel=line.split('  ',1)
  if rel in listed or '..' in Path(rel).parts:raise ValueError('Invalid curated manifest')
  listed[rel]=digest
 for rel,digest in sorted(listed.items()):
  f=P/'release'/rel
  if sha(f)!=digest:raise RuntimeError('Curated release mismatch: '+rel)
  copy(f,'curated reproducibility bundle')
 copy(manifest,'curated reproducibility bundle')
 # Main published pair plus editable source/support docs, never old duplicate ZIPs.
 for f in sorted(P.iterdir()):
  if not f.is_file():continue
  if f.name=='LULA-I-source.zip' or f.name=='LULA-I.pdf' or f.suffix.lower() in {'.tex','.bib','.bbl','.md','.json'}:copy(f,'main finalized publication/source/support')
  else:omit(f,'unselected historical archive or generated paper scratch')
 for name in ['publication-final-20261013','zenodo-release-20261013']:
  f=P/'editorial'/name
  if f.exists():tree(f,'current publication review provenance',True)
 tree(S,'security proof/model/numerics/review/results')
 for f in P.iterdir():
  if f.is_dir() and f.name not in {'release','editorial'}:omit(f,'outside requested current publication bundle',False)
 # Gather citations to omitted reference objects without copying their full text.
 citation_paths=[]
 for rec in records:
  path=REPO/rec['repository_path']
  if path.suffix.lower() in {'.md','.json','.txt','.bib'} and '/security/' in '/'+rec['repository_path']:
   text=path.read_text(encoding='utf8',errors='replace')
   urls=sorted(set(re.findall(r'https?://[^\s<>"\]\[{}]+',text)))
   if urls:citation_paths.append({'repository_path':rec['repository_path'],'urls':urls})
 out=REPO/'snapshot';out.mkdir(exist_ok=True)
 (out/'SOURCE-COPY-MANIFEST.json').write_text(json.dumps({'status':'BYTE_IDENTICAL_AUTHORIZED_PRIVATE_SNAPSHOT','source_root':str(R),'files':records,'copied_files':len(records),'copied_bytes':sum(x['bytes'] for x in records),'no_portable_fresh_reproduction_claim':True},indent=2)+'\n',encoding='utf8')
 (out/'EXCLUSIONS.json').write_text(json.dumps({'exclusions':excluded,'third_party_reference_urls_from_retained_proof_citations':citation_paths,'reason_counts':dict(collections.Counter(x['reason'] for x in excluded))},indent=2)+'\n',encoding='utf8')
 (out/'SECRET-SCAN.json').write_text(json.dumps({'scope':'Copied source byte content; patterns and suspect filenames; values never printed','patterns':list(PATTERNS),'hits':hits,'candidate_files_checked':len(records),'operational_secret_clearance':'No pattern hit found' if not hits else 'STOP_REQUIRED','not_universal_entropy_proof':True},indent=2)+'\n',encoding='utf8')
 if hits:
  print(json.dumps({'status':'STOP_SECRET_PATTERN_HIT','paths_and_pattern_names_only':hits}));sys.exit(1)
 print(json.dumps({'status':'COPIED_EXACT_BYTES','files':len(records),'bytes':sum(x['bytes'] for x in records),'exclusions':len(excluded),'secret_pattern_hits':0}))
if __name__=='__main__':main()
