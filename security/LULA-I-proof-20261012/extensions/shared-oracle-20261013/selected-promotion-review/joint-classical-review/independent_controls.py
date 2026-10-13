"""Finite analytical/safe-surface controls, never source hash or signature calls."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
B=Path(__file__).resolve().parent
X=B.parents[1]
peer=X/'pre-start-second/interior-ud/quantitative-boundary/joint-classical'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='ed747c50d39d6c301d55bb25fec8a590b48cb089f166b75360dc42d149123ab9'
assert sha(peer/'INDEPENDENT-FIRST.md')==expected
assert sha(B/'INDEPENDENT-FIRST.md')=='95eb6761332435bbb9044c97ab997fa5d1eb4aa4840a5f678001006ed5969c93'
mirror=B/'peer-reexecution';mirror.mkdir(exist_ok=True)
for n in ['INDEPENDENT-FIRST.md','byte_role_controls.py']:shutil.copyfile(peer/n,mirror/n)
run=subprocess.run([sys.executable,str(mirror/'byte_role_controls.py')],capture_output=True,text=True)
assert run.returncode==0,run.stderr
assert (mirror/'BYTE-ROLE-CONTROLS.json').read_bytes()==(peer/'BYTE-ROLE-CONTROLS.json').read_bytes()
checks=[]
for N in [2,4,8]:
    triple=F(sum(p==0 or j==0 or z==1 for p,j,z in product(range(N),repeat=3)),N**3)
    double=F(sum(x==0 or (x!=0 and z==1) for x,z in product(range(N),repeat=2)),N**2)
    assert triple==3*F(1,N)-3*F(1,N*N)+F(1,N**3)>F(1,N)
    assert double==2*F(1,N)-F(1,N*N)>F(1,N)
    # Distinct restrictions let an endpoint be safe even though its predecessor is hidden.
    # Disclosure threshold is a function only of endpoint and ghost reply, not hidden nodes.
    groups={}
    for x0,x1,x2,z in product(range(N),repeat=4):
        digit=1 if (x2+z)%2==0 else 2
        observation=(digit,x2,z,x1 if digit==1 else None)
        counts=groups.setdefault(observation,[0]*N);counts[x0]+=1
    assert all(len(set(v))==1 for v in groups.values())
    # Unsafe whole-secret advice permits predicting a still-hidden predecessor with certainty.
    unsafe=F(sum(guess==x for x in range(N) for guess in [x]),N)
    assert unsafe==1>F(1,N)
    # A later residual row value disclosed as metadata yields an uncharged different-counter hit.
    # First counter target=0; reject prefix=1; later residual=0 with probability 1/N.
    surplus=F(sum(later==0 for later in range(N)),N)
    assert surplus==F(1,N)>0
    # No-survival postselection: conditioning on a failed first guess destroys uniformity.
    assert F(1,N-1)>F(1,N)
    checks.append(dict(N=N,inner_triple=str(triple),hidden_graph_double=str(double),
        safe_suffix_groups=len(groups),unsafe_secret_advice_success=str(unsafe),
        surplus_postaccepted_metadata_hit=str(surplus),
        postselected_next_guess=str(F(1,N-1))))
# Exposure state is high with probability1/16, conditional coverage probability1/4.
# Request4 candidate draws only in the high state, plus one padded final opportunity.
# Independent candidates do not permit replacing their adaptive PATHWISE cap by expectedcount.
success=F(1,16)*(1-F(3,4)**5)
pF=F(1,16)*F(1,4)
expected_count=F(4,16)
false_bound=(expected_count+1)*pF
true_bound=5*pF
assert success>false_bound and success<=true_bound
assert 3017+3217+5+2==6241 and 6241+1==6242
out=dict(classification='FINITE_SUPPORTING_CONTROLS_NOT_SOURCE_GAME_CHECK',exit_code=0,
    peer_reexecution_identical=True,peer_first_sha256=expected,
    peer_clarification_sha256=sha(peer/'CONDITIONING-CLARIFICATION.md'),
    peer_script_sha256=sha(peer/'byte_role_controls.py'),
    peer_controls_sha256=sha(peer/'BYTE-ROLE-CONTROLS.json'),toy_checks=checks,
    adaptive_coverage_negative=dict(actual=str(success),false_expected_cap_bound=str(false_bound),
        valid_pathwise_cap_bound=str(true_bound),pF=str(pF),expected_candidates=str(expected_count)),
    new_source_game_declarations=0,new_checked_declarations=0,whole_goal_complete=False)
(B/'INDEPENDENT-CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
