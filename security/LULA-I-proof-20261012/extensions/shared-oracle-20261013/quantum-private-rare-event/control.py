"""Exact CQ submass and failed-normalization/purification controls."""
from fractions import Fraction as F
import json, math
from pathlib import Path

# Two measured histories; query candidate3 is independent of the private key.
N=4
histories=[(F(1,2),{0}),(F(1,2),{0,1,2})]
alive=mass_ref=mass_active=F(0)
for ph,guesses in histories:
    for key in range(N):
        full=ph/N
        active=full if key not in guesses else F(0)
        assert full-active>=0  # each CQ positive block coefficient
        alive+=active
        if key==3:
            mass_ref+=full
            mass_active+=active
assert alive==F(1,2)
assert mass_active==mass_ref==F(1,4)
assert mass_active/alive==F(1,2)>F(1,N)
normalized_negative=F(1,8)-F(1,8)/alive
assert normalized_negative==F(-1,8)

# Pure-state domination is false: rho=|+><+|, sigma=(1/2)|0><0|.
# Test v=(1,-1) in rho-sigma. Dephasing the classical environment fixes it.
rho=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
sigma=[[F(1,2),F(0)],[F(0),F(0)]]
v=[1,-1]
def quadratic(mat,vec):
    return sum(vec[i]*mat[i][j]*vec[j] for i in range(2) for j in range(2))
diff=[[rho[i][j]-sigma[i][j] for j in range(2)] for i in range(2)]
pure_negative=quadratic(diff,v)
assert pure_negative==F(-1,2)
dephased=[[diff[0][0],F(0)],[F(0),diff[1][1]]]
assert quadratic(dephased,v)==F(1,2)>=0

# Stopping a coherent query itself has the same noncommuting obstruction inside
# one classical key block: keep only |1>/sqrt2 rather than a classical history.
quantum_stop=[[F(0),F(0)],[F(0),F(1,2)]]
qdiff=[[rho[i][j]-quantum_stop[i][j] for j in range(2)] for i in range(2)]
coherent_negative=quadratic(qdiff,v)
assert coherent_negative==F(-1,2)

# A finite source-style scalar stop followed by one private-support phase query.
# Unflagged states are keyblind; stopped alive vectors retain original weights.
N2=16
beforeB=pB_ideal=pB_real=pW_ideal=pW_real=F(0)
local_gap_squared=F(0)
for ph,guesses in histories:
    for key in range(N2):
        prob=ph/N2
        if key in guesses:
            beforeB+=prob
            pB_ideal+=prob
            pB_real+=prob
            continue
        # query(|3>+|outside>)/sqrt2. REAL flips|3> iff key3, IDEAL not.
        if key==3:
            local_gap_squared+=2*prob
            pW_real+=prob  # measurement in minus basis
        # A final public nomination0 is harmless on all active histories;
        # key0 was already stopped. IDEAL never outputs the minus outcome.
assert beforeB==F(1,8)
assert pB_ideal==pB_real==F(1,8)
assert pW_real==F(1,16) and pW_ideal==0
assert local_gap_squared==F(1,8)
delta=math.sqrt(float(local_gap_squared))
assert abs(math.sqrt(float(pW_real))-math.sqrt(float(pW_ideal)))<=delta+1e-12
assert local_gap_squared<=F(4,N2)
union_real=pB_real+pW_real
union_ideal=pB_ideal+pW_ideal
assert abs(math.sqrt(float(union_real))-math.sqrt(float(union_ideal)))<=delta+1e-12
single=(delta+math.sqrt(float(union_ideal)))**2
separate=(delta+math.sqrt(float(pB_ideal)))**2+(delta+math.sqrt(float(pW_ideal)))**2
assert float(union_real)<=single+1e-12 and single<=separate+1e-12

out={
 'status':'PASS_EXACT_CQ_AND_RARE_EVENT_CONTROLS_ONLY',
 'active_submass':str(alive),
 'unflagged_private_support_mass':str(mass_ref),
 'stopped_unnormalized_private_support_mass':str(mass_active),
 'invalid_normalized_survivor_mass':str(mass_active/alive),
 'normalized_operator_domination_negative_quadratic':str(normalized_negative),
 'pure_global_domination_negative_quadratic':str(pure_negative),
 'coherent_query_stop_negative_quadratic':str(coherent_negative),
 'scalar_stopped_phase_control_alias_probability':str(pB_real),
 'scalar_stopped_phase_control_ideal_noB_win':str(pW_ideal),
 'scalar_stopped_phase_control_real_noB_win':str(pW_real),
 'purified_local_gap_squared':str(local_gap_squared),
 'single_projector_real_union_probability':str(union_real),
 'single_projector_ideal_union_probability':str(union_ideal),
 'single_projector_bound_using_actual_gap':single,
 'separate_projector_bound_using_actual_gap':separate,
 'scope':'Exact scalar CQ/history support and generic phase-query controls; not a source attack, ordinary-RO marginal or full quantum-security proof'
}
Path(__file__).with_name('CONTROL-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
