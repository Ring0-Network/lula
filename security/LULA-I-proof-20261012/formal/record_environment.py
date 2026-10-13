from pathlib import Path
import subprocess, json, hashlib, re, importlib.metadata
BASE=Path(__file__).resolve().parent
LINUX='/mnt/c/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/security/LULA-I-proof-20261012/formal'
records={}
def run(name,args):
    p=subprocess.run(args,text=True,encoding='utf-8',capture_output=True,timeout=120)
    records[name]={'command':args,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    return p
run('lean_pin',['wsl','-d','Ubuntu-24.04','--','bash','-lc',
 '/root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean --version; git -C /root/jolt-lean-20261001/mathlib rev-parse HEAD; sha256sum /root/jolt-lean-20261001/mathlib/lake-manifest.json /root/jolt-lean-20261001/lean-4.28.0-linux/bin/lean'])
run('easycrypt_configuration',['wsl','-d','Ubuntu-24.04','--','/root/.opam/ec/bin/easycrypt','config'])
p=run('easycrypt_final',['wsl','-d','Ubuntu-24.04','--','/root/.opam/ec/bin/easycrypt','compile','-no-eco',LINUX+'/CacheModel.ec'])
records['easycrypt_final']['checked_without_diagnostics']=p.returncode==0 and not re.search(r'\[(critical|error)\]|unknown variable|unproved',p.stdout+p.stderr,re.I)
(BASE/'easycrypt-final.log').write_text(p.stdout+p.stderr,encoding='utf-8')
run('solver_and_checker_hashes',['wsl','-d','Ubuntu-24.04','--','bash','-lc',
 '/usr/bin/z3 --version; /root/.opam/ec/bin/alt-ergo --version; sha256sum /root/.opam/ec/bin/easycrypt /root/.config/easycrypt/why3.conf /usr/bin/z3 /root/.opam/ec/bin/alt-ergo'])
run('K_available',['wsl','-d','Ubuntu-24.04','--','bash','-lc','command -v kompile; command -v kprove'])
records['K_available']['verdict']='UNCHECKED K development; no install/configuration changes'
records['source_hashes']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in BASE.glob('*') if f.suffix in ['.lean','.ec','.k','.py']}
records['sdk_versions']={'aristotlelib':importlib.metadata.version('aristotlelib'),'axle':[(x.metadata['Name'],x.version) for x in importlib.metadata.distributions() if 'axle' in x.metadata.get('Name','').lower()]}
(BASE/'ENVIRONMENT.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'easycrypt_final_pass':records['easycrypt_final']['checked_without_diagnostics'],'K_available':records['K_available']['exit_code'],'sdk_versions':records['sdk_versions']},indent=2))
if not records['easycrypt_final']['checked_without_diagnostics']: raise SystemExit(1)
