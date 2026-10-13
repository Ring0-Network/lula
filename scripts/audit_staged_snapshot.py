"""Audit staged byte identity, credential patterns and Git identity; no secrets printed."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess
R=Path(__file__).resolve().parents[1]
def git(*args):return subprocess.check_output(['git','-C',str(R),*args])
spec=importlib.util.spec_from_file_location('snapshot_rules',R/'scripts/snapshot_sources.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
manifest=json.loads((R/'snapshot/SOURCE-COPY-MANIFEST.json').read_text(encoding='utf8'))
entries={}
for raw in git('ls-files','--stage','-z').split(b'\0'):
 if not raw:continue
 meta,path=raw.split(b'\t',1);mode,oid,stage=meta.decode().split()
 assert stage=='0' and mode in {'100644','100755'}
 entries[path.decode('utf8')]=oid
assert all(rec['repository_path'] in entries for rec in manifest['files'])
assert all(not any(part in rules.PRUNE for part in Path(rel).parts) for rel in entries)
assert not any(Path(rel).name.lower() in rules.SECRET_NAMES for rel in entries)
hashes={};hits=[]
proc=subprocess.Popen(['git','-C',str(R),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for rel,oid in entries.items():
 if oid in hashes:continue
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush()
 header=proc.stdout.readline().decode().strip().split();assert header[1]=='blob'
 data=proc.stdout.read(int(header[2]));assert len(data)==int(header[2]) and proc.stdout.read(1)==b'\n'
 hashes[oid]=hashlib.sha256(data).hexdigest()
 for kind,pattern in rules.PATTERNS.items():
  if re.search(pattern,data):hits.append({'path':rel,'pattern':kind})
proc.stdin.close();assert proc.wait()==0
for rec in manifest['files']:assert hashes[entries[rec['repository_path']]]==rec['source_sha256']==rec['copy_sha256']
assert not hits,{'credential_pattern_paths_only':hits}
assert git('config','--local','--get','user.name').strip()==b'ring0code'
assert git('config','--local','--get','user.email').strip()==b'341783300+ring0code@users.noreply.github.com'
account=json.loads(subprocess.check_output(['gh','api','user']))
assert (account['login'],account['id'])==('ring0code',341783300)
repo=json.loads(subprocess.check_output(['gh','api','repos/Ring0-Network/lula']))
assert repo['private'] is True
global_config=Path.home()/'.gitconfig'
assert hashlib.sha256(global_config.read_bytes()).hexdigest()=='aec80179de621068e3c3c7f4b66e57f20c42c9797449a91c0f3aa6bc3c110365'
result=dict(status='PASS_STAGED_AUTHORIZED_SNAPSHOT',staged_files=len(entries),source_payload_files=len(manifest['files']),unique_staged_blobs_scanned=len(hashes),source_vs_copy_vs_staged_SHA256_all_equal=True,credential_pattern_hits=hits,gh_account='ring0code',gh_id=341783300,repository_private=True,expected_author_and_committer='ring0code <341783300+ring0code@users.noreply.github.com>',global_gitconfig_sha256='aec80179de621068e3c3c7f4b66e57f20c42c9797449a91c0f3aa6bc3c110365',global_config_unchanged=True,crypto_source_sha256='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210',proof_benchmark_or_attack_runs=0,whole_security_goal_complete=False)
(R/'snapshot/STAGED-AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','staged_files','source_payload_files','unique_staged_blobs_scanned','gh_account','repository_private','global_config_unchanged']}))
