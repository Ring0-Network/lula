"""Record the local checked candidate-list theorem and exact installed dependencies."""
from pathlib import Path
import hashlib,json,re,subprocess

HERE=Path(__file__).resolve().parent
source=HERE/'SeedGuess.ec'
current=json.loads((HERE/'easycrypt-current.json').read_text(encoding='utf-8'))
assert current['exit_code']==0
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
assert current['source_sha256']==source_hash
src=source.read_text(encoding='utf-8')
assert not re.search(r'(?m)^\s*(axiom|admit|admitted|abort)\b',src)

def wsl(*args):
    cmd=['wsl','-d','Ubuntu-24.04','--',*args]
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=30)
    assert p.returncode==0,(cmd,p.stderr)
    return (p.stdout+p.stderr).strip()

config=wsl('/root/.opam/ec/bin/easycrypt','config')
git_hash=next(x.split(':',1)[1].strip() for x in config.splitlines() if x.startswith('git-hash:'))
libs=[
 '/root/.opam/ec/lib/easycrypt/theories/core/AllCore.ec',
 '/root/.opam/ec/lib/easycrypt/theories/datatypes/List.ec',
 '/root/.opam/ec/lib/easycrypt/theories/distributions/Distr.ec',
 '/root/.opam/ec/lib/easycrypt/theories/distributions/DInterval.ec',
]
paths=['/root/.opam/ec/bin/easycrypt','/root/.opam/ec/bin/why3','/usr/bin/z3',
       '/root/.config/easycrypt/why3.conf',*libs]
raw=wsl('sha256sum',*paths)
hashes=[{'path':line.split(None,1)[1],'sha256':line.split(None,1)[0]} for line in raw.splitlines()]
statements=[]
for name,body in re.findall(r'(?ms)^lemma\s+(\w+)\s+(.*?)^proof\.',src):
    statements.append({'name':name,'statement':body.strip()})
assert [x['name'] for x in statements]==['uniform_atom_bound','one_seed_hit_bound','two_seed_hit_bound','key_blind_game_bound']
out={
 'status':'CHECKED_FIXED_KEY_BLIND_CANDIDATE_LIST_MODEL_NOT_FULL_LULA_SECURITY',
 'source_sha256':source_hash,'checker_command':current['command'],'checker_exit':current['exit_code'],
 'easycrypt_git_hash':git_hash,'why3_version':wsl('/root/.opam/ec/bin/why3','--version'),
 'selected_smt_prover':'Z3','z3_version':wsl('/usr/bin/z3','-version'),
 'direct_imports':['AllCore','List','Distr','DInterval'],
 'dependencies':hashes,'checked_declarations':statements,
 'custom_axioms_admits_aborts_added':False,
 'proof_helpers':['dinter1E','mu_mem_le_mu1','le_dprod_or','weight_dinter','fromintD','RField.mulrDl'],
 'scope':'Candidate lists and n are fixed as procedure inputs before uniform independent keys are sampled. No adaptive source transcript or RO coupling is encoded.',
 'trusted_stack':'Installed EasyCrypt logic and official distribution/real/list libraries; Why3 1.8.2 and selected Z3 4.8.12 SMT proofs. No transitive axiom-minimization or full standard-library rebuild was performed.',
 'repair':'Qualify real distributivity as RField.mulrDl, explicitly simplify interval weight from n>0, and parenthesize the intended full phoare numeric bound; no assumptions weakened.'
}
(HERE/'EASYCRYPT-VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','source_sha256','checker_exit','easycrypt_git_hash','why3_version','z3_version','custom_axioms_admits_aborts_added']},indent=2))
