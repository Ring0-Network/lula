"""Current baseline source-model bounds, separate from all historical calculators.
No signatures, forest generation, runtime measurements, or parameter-proof transplant.
Dependency: installed mpmath 1.3.0. Run python -I -B bounds.py --help.
"""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,importlib.util,json,math,sys
import mpmath as mp
HERE=Path(__file__).resolve().parent
X=HERE.parent.parent
PROOF=X.parent.parent
SOURCE=PROOF.parent.parent/'publications/LULA-I/release/code/lula1/src/lib.rs'
DRIVER=SOURCE.parent/'bin/lula1_driver_original.rs'
HELPER=PROOF/'numerics/bounds.py'
SOURCE_SHA='ac8e67f05af68dd8e1291c5909847f74103903fb7ffa2c70f500c6ec48f14210'
HELPER_SHA='a482536e402e39c970f675abcd3d595e6a3bd43a3ce94d1c2e1dfd4d6fdc0385'
BASE={'n_bytes':16,'r':17,'a':9,'d':5,'heights':[5,5,5,5,21],'lw':[4,4,4,4,8],'ell':[32,32,32,32,16],'S':[240,240,240,240,2040],'cache_policy':'top-only','counter_bits':32}
QS=(24,30,38,40,41,44,50,64)
THEOREMS=('CLASSICAL-JOINT-RO-THEOREM.md','QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md','QUANTUM-RO-THEOREM.md','QUANTUM-EVENT-SPECIFIC-THEOREM.md','SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md','SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md')
EXPECTED_THEOREM_SHAS={'CLASSICAL-JOINT-RO-THEOREM.md': '4fa7c3b63a268bd7535a753813d109a2f768f0089df44b54223a6e34cfaf35f0', 'QUANTUM-POLYNOMIAL-PRIVATE-COMPOSITION.md': '1a9c1896814c51e6f0810e52baf69f2845996b276edcdcea8b44b8d371973c28', 'QUANTUM-RO-THEOREM.md': '94c8f29121760d1a09358257720bb123613084f07a645db9ba9296a43e49a607', 'QUANTUM-EVENT-SPECIFIC-THEOREM.md': 'd28e99570c0b6819f7a45169882252ffedc6e31cfad150751f7084a9fdea02f1', 'SOURCE-PRIVATE-K-POLYNOMIAL-QROM.md': '0e09f51fced6f4a5fc26c8121bfc4f5a91dc3de3af4e93fe4465491e3d03ca73', 'SOURCE-PRIVATE-P-POLYNOMIAL-QROM.md': '72e214e7194c8892502212690ef98ea1996f21b3138708154de6ff0de600544b'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def load_helper():
 if sha(SOURCE)!=SOURCE_SHA:raise ValueError('Source pin mismatch: current baseline not recertified')
 if sha(HELPER)!=HELPER_SHA:raise ValueError('Frozen FORS/count helper pin mismatch')
 for name,pin in EXPECTED_THEOREM_SHAS.items():
  if sha(X/name)!=pin:raise ValueError('Theorem pin changed; manual formula review required: '+name)
 spec=importlib.util.spec_from_file_location('frozen_numerics',HELPER)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def geometry(p):
 if set(p)!=set(BASE):raise ValueError('Parameter keys must match baseline.json exactly')
 for name in ('n_bytes','r','a','d','counter_bits'):
  if type(p[name]) is not int:raise ValueError('Expected integer '+name)
 if p['n_bytes']!=16 or p['counter_bits']!=32:raise ValueError('Only fixed source n=16 bytes and BE32 counters supported')
 if not(1<=p['d']<=256 and 1<=p['r'] and 1<=p['a']<=31):raise ValueError('Invalid dimensions')
 if p['cache_policy']!='top-only':raise ValueError('Only declared top-only cache policy supported; cold diagnostics are included separately')
 for name in ('heights','lw','ell','S'):
  if not isinstance(p[name],list) or len(p[name])!=p['d'] or any(type(v) is not int for v in p[name]):raise ValueError('Invalid '+name)
 if any(not 1<=h<=31 for h in p['heights']):raise ValueError('Source subtree shifts require heights 1..31')
 if sum(p['heights'])>63:raise ValueError('Source tree_leaf shift requires total height at most63')
 if (p['r']+1)*p['a']+sum(p['heights'])>256:raise ValueError('Full message-digest bit geometry exceeds256')
 if p['r']*(1<<p['a'])>1<<32:raise ValueError('Source FORS global index exceeds32 bits')
 if 22+16*p['r']+9>64*24:raise ValueError('Source th buffer bound exceeded')
 if p['lw']!=[4]*(p['d']-1)+[8]:raise ValueError('Authorized retuning domain fixes lower lw4 and final top lw8')
 for lw,ell,S in zip(p['lw'],p['ell'],p['S']):
  if lw not in (4,8) or not 1<=ell<=128//lw:raise ValueError('Fixed lw4/8; ell must fit source128-bit encoding')
  if not 0<=S<=ell*((1<<lw)-1):raise ValueError('Target sum outside exact bounded-composition geometry')
 return p==BASE

IV=mp.iv.mpf

def ends(v):return mp.mpf(v._mpi_[0]),mp.mpf(v._mpi_[1])
def cap(v):
 l,u=ends(v);return IV([min(l,1),min(u,1)])
def scalar(v,kind="probability"):
 l,u=ends(v)
 if kind=="count":return {"status":"COMPUTED analytic count, not a probability", "value_lower":mp.nstr(l,90),"value_upper":mp.nstr(u,90),"lower_dyadic_tuple":list(v._mpi_[0]),"upper_dyadic_tuple":list(v._mpi_[1])}
 return {'status':'COMPUTED','probability_lower':mp.nstr(l,90),'probability_upper':mp.nstr(u,90),'lower_dyadic_tuple':list(v._mpi_[0]),'upper_dyadic_tuple':list(v._mpi_[1]),'negative_log2_probability_lower_approx':float(-mp.log(u,2)) if u>0 else None,'negative_log2_probability_upper_approx':float(-mp.log(l,2)) if l>0 else None,'exponent_meaning':'probability-bound exponent, NOT guaranteed work bits/category'}

def pf_interval(q,H,a,r,helper,dps):
 lo=helper.fors_moment(q,H,a,r+1,dps=dps)
 hi=helper.fors_moment(q,H,a,r+1,dps=dps+100)
 relative=abs(lo-hi)/hi
 assert relative<mp.mpf(10)**(-(dps-100))
 rho=IV(1)/(1<<H);rem=IV((1<<a)-1)/(1<<a)
 v=sum(((-1)**j*math.comb(r,j)*(1-rho+rho*rem**j)**q for j in range(r+1)),IV(0))/(1<<a)
 l,u=ends(v);filt=mp.mpf(1)/(1<<a)
 assert l>0 and l<=hi<=u
 v=IV([l,min(u,filt)])
 mu=mp.mpf(q)/(1<<H)
 if mu>4096:
  low=(1-mp.iv.exp(-IV(q)/(1<<H)/8))*(1-mp.iv.exp((IV(q)/(1<<H)/2)*mp.iv.log(rem)))**r/(1<<a)
  pl,pu=ends(low);pos=IV([max(mp.mpf(0),pl),filt]);method='positive Chernoff saturation bound'
  extra={'mean_occupancy':mp.nstr(mu,40)}
 else:
  stop=min(q,max(320,math.ceil(mu+20*mp.sqrt(mu+1)+300)))
  w=(1-rho)**q;total=IV(0)
  for j in range(1,stop+1):
   w*=IV(q-j+1)*rho/(j*(1-rho));total+=w*(1-rem**j)**r
  L=stop+1;tail=IV(0) if stop==q else mp.iv.exp(-IV(q)/(1<<H)+L*(1+mp.iv.log(IV(q)/(1<<H)/L)))/(1<<a)
  pl,_=ends(total/(1<<a));_,pu=ends(total/(1<<a)+tail)
  pos=IV([max(mp.mpf(0),pl),min(filt,pu)]);method='positive binomial recurrence with analytic Chernoff tail'
  extra={'stop':stop,'weighted_tail_upper':mp.nstr(ends(tail)[1],60)}
 pl,pu=ends(pos);l,u=ends(v);assert max(l,pl)<=min(u,pu)
 return v,{'status':'COMPUTED','moment_dps':dps,'independent_moment_dps':dps+100,'relative_difference':mp.nstr(relative,50),'moment_outward_interval':scalar(v),'positive_method':method,'positive_outward_interval':scalar(pos),'checks':'moment stability and positive enclosure overlap; Poisson is not substituted',**extra}

def acceptance(ell,lw,S,helper):
 count=helper.count_ie(S,[(1<<lw)-1]*ell)
 assert count==helper.count_dp(S,[(1<<lw)-1]*ell)
 theta=IV(count)/(1<<128);bottom=(1-theta)**(1<<32);success=1-bottom
 expected=success/theta
 # Use stable geometric finite sum conditional on success. Extremely small
 # theta cancellation is handled by600-digit interval arithmetic.
 conditional=1/theta-(1<<32)*bottom/success
 return count,theta,bottom,success,expected,conditional

def costs(p,helper):
 n=16;layers=[];height=sum(p['heights'])
 for i,(h,lw,ell,S) in enumerate(zip(p['heights'],p['lw'],p['ell'],p['S'])):
  w=1<<lw;L=1<<h;pkblocks=(22+n*ell+9+63)//64
  tree=L*(ell*w+pkblocks)+(L-1) # PRF, chain and parent tail blocks each1
  cnt,theta,bottom,success,expected,cond=acceptance(ell,lw,S,helper)
  layers.append({'layer':i,'height':h,'w':w,'ell':ell,'z':128//lw-ell,'S':S,'Smax':ell*(w-1),'strict_S_less_than_Smax':S<ell*(w-1),'signature_bytes':4+n*(ell+h),'accepted_vector_count_exact':str(cnt),'raw_acceptance_denominator_exact':str(1<<128),'raw_acceptance_probability':scalar(theta),'counter_bottom_probability':scalar(bottom),'capped_counter_success':scalar(success),'mean_counter_trials_until_success_or_bottom':scalar(expected,'count'),'mean_counter_trials_conditional_on_success':scalar(cond,'count'),'endpoint_compressor_tail_blocks':pkblocks,'subtree_tail_compressions_exact':str(tree),'WOTS_signature_PRF_plus_chain_compressions_exact':ell+S,'one_verifier_chain_PK_auth_tail_compressions_exact':ell*(w-1)-S+pkblocks+h})
 top=layers[-1];L=1<<top['height'];cache_nodes=2*L-1;cache_bytes=cache_nodes*n+4*L
 lower_child=layers[-2]['subtree_tail_compressions_exact'] if len(layers)>1 else str(p['r']*(3*(1<<p['a'])-1)+(22+n*p['r']+9+63)//64)
 top_fixed=int(top['subtree_tail_compressions_exact'])+top['WOTS_signature_PRF_plus_chain_compressions_exact']+1
 hot_fixed=top['WOTS_signature_PRF_plus_chain_compressions_exact']+1
 # Keygen top-only: each top leaf pk, its immediate lower subtree child,
 # row grind; then the top Merkle parents. Expectations below condition on
 # all top rows completing; costs of an absorbing setup are not normalized away.
 pk_leaf=top['ell']*top['w']+top['endpoint_compressor_tail_blocks']
 setup_fixed=L*(pk_leaf+int(lower_child))+(L-1)
 # Recompute interval from exact cardinality, avoiding rounded display reuse.
 _,_,_,succ,expect,cond=acceptance(top['ell'],p['lw'][-1],p['S'][-1],helper)
 return {'status':'COMPUTED exact bytes/integer compression skeleton; ASSUMED fresh uniform distinct type7 row model for grind expectations','signature_bytes_exact':16+4+16*p['r']*(p['a']+1)+sum(a['signature_bytes'] for a in layers),'FORS_signature_bytes_exact':16*p['r']*(p['a']+1),'public_key_bytes_exact':32,'secret_seed_bytes_exact':48,'top_cache_nodes_exact':str(cache_nodes),'top_cache_counters_exact':str(L),'logical_cache_bytes_exact':str(cache_bytes),'driver_fixture_bytes_exact':str(cache_bytes+8+48+16+8+p['d']+8+24),'driver_fixture_warning':'contains48 seed bytes; NOT the public/logical payload experiment','top_subtree_cold_rebuild_tail_compressions_exact':top['subtree_tail_compressions_exact'],'top_cold_sign_tail_fixed_compressions_exact':str(top_fixed),'top_cold_sign_tail_mean_until_success_or_bottom_upper':scalar(IV(top_fixed)+expect,'count'),'top_cold_sign_tail_mean_conditional_on_row_success':scalar(IV(top_fixed)+cond,'count'),'top_hot_sign_tail_fixed_compressions_exact':hot_fixed,'top_only_keygen_fixed_tail_compressions_exact':str(setup_fixed),'top_only_keygen_mean_tail_conditional_all_top_rows_success':scalar(IV(setup_fixed)+L*cond,'count'),'top_only_keygen_all_rows_success_probability':scalar(succ**L),'tail_scope':'optimized public-seed block already precomputed; add1 compression per constructed Ctx (not counted by source CALLS). Cold subtree is a count only, never generated. Conditional means are explicit, not whole-game success normalization.','layers':layers,'geometry_does_not_certify_retuned_security':True,'source_Smax_guard_all_layers':all(a['strict_S_less_than_Smax'] for a in layers)}

def classical(q,Q,pf):
 N=1<<128
 terms={'public_slot_rare_event_ledger':IV(3*Q)/N,'honest_final_inner_fees':IV(2*q+2)/N,'final_H_G_D7_fees':IV(6239)/N,'seed_zero_once':IV(1)/N,'pair_bridge':IV(q*Q+q*(q-1)//2+q)/(N*N),'finite_FORS_exhaustion':q*(IV(511)/512)**(1<<32),'candidate_coverage':(Q+1)*pf}
 total=sum(terms.values(),IV(0));terms.update(uncapped_total=total,complete_joint_bound=cap(total))
 return {k:scalar(v) for k,v in terms.items()}

def quantum(q,Q,pf):
 N=1<<128;M=N*N-N
 D=cap(q*(mp.iv.sqrt(IV(Q+q+1)/M)+IV(Q+q+1)/(2*M)))
 A=cap(D+8*(Q+2)**2*(pf+IV(1)/N+IV(q)/(N*N)))
 c=cap((2*Q+mp.iv.sqrt(IV(q)))**2/N+(IV(2*(Q+2))/(1<<64)+mp.iv.sqrt(A))**2)
 h=cap((2*Q+mp.iv.sqrt(IV(3017)))**2/N);g=cap(IV(8*(Q+3218)**2)/N);d=cap(IV(8*(Q+6)**2)/N)
 public=c+h+g+d;e=cap(public)
 v=cap(IV(4*Q*Q)/(N-4*Q*Q)) if 4*Q*Q<N else IV(1)
 alias=cap((2*Q+mp.iv.sqrt(IV(min(N,2*q+2))))**2/N);ap=cap(v+alias)
 poly=cap(IV(1)/N+v+ap+e)
 oldprivate=cap(IV(2*Q)/(1<<64)+IV(2*q+2)/N)
 old=cap(IV(1)/N+oldprivate+public)
 event=cap(IV(1)/N+(IV(2*Q)/(1<<64)+mp.iv.sqrt(cap(cap(IV(2*q+2)/N)+e)))**2)
 a=[ends(t) for t in (old,event,poly)];best=IV([min(t[0] for t in a),min(t[1] for t in a)])
 terms={'coverage_D':D,'coverage_A':A,'C':c,'H':h,'G':g,'D7':d,'ideal_private_union':e,'K_decision_v':v,'P_decision_v':v,'P_classical_alias':alias,'P_one_sided_aP':ap,'seed_zero_once':IV(1)/N,'complete_polynomial_private':poly,'retained_old_conservative':old,'retained_old_event':event,'complete_best_of_three':best}
 return {k:scalar(v) for k,v in terms.items()}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--params',type=Path,default=HERE/'baseline.json')
 ap.add_argument('--log2-QH',type=int,nargs='+',choices=(64,128),default=[64,128])
 ap.add_argument('--log2-Qq',type=int,nargs='+',choices=(32,64),default=[32,64])
 ap.add_argument('--out',type=Path,default=HERE/'results.json',help='JSON path, or directory receiving results.json')
 ap.add_argument('--dps',type=int,default=600,help='at least500; pF also checked at dps+100')
 a=ap.parse_args()
 if a.dps<500:ap.error('--dps must be at least500')
 p=json.loads(a.params.read_text(encoding='utf-8'));baseline=geometry(p);helper=load_helper()
 mp.mp.dps=a.dps+100;mp.iv.dps=a.dps
 print('Displayed exponents are probability-bound exponents, NOT work bits/category.',flush=True)
 diagnostics=costs(p,helper);rows=[]
 for k in QS:
  q=1<<k;pf,check=pf_interval(q,sum(p['heights']),p['a'],p['r'],helper,a.dps)
  row={'log2_q':k,'q':str(q),'FORS_fixed_instance_moment':scalar(pf),'FORS_validation':check,'complete_bounds_status':'COMPUTED from PROVED manual baseline source envelopes' if baseline else 'REFUSED: retuned diagnostics lack uniform source proof','classical':[],'quantum':[]}
  if baseline:
   for QH in sorted(set(a.log2_QH)):row['classical'].append({'log2_QH':QH,'components':classical(q,1<<QH,pf)})
   for Qq in sorted(set(a.log2_Qq)):row['quantum'].append({'log2_Qq':Qq,'components':quantum(q,1<<Qq,pf)})
  rows.append(row)
  print(f"q=2^{k}: pF exponent {scalar(pf)['negative_log2_probability_lower_approx']:.12f}; "+('baseline complete bounds COMPUTED' if baseline else 'retuned full bounds REFUSED'),flush=True)
 out={'status':'COMPUTED_CURRENT_BASELINE_COMPLETE_SOURCE_ENVELOPES' if baseline else 'ANALYTIC_DIAGNOSTICS_ONLY_COMPLETE_BOUNDS_REFUSED','parameters':p,'baseline_source_parameters':baseline,'params_sha256':sha(a.params),'script_sha256':sha(Path(__file__)),'dependency':{'mpmath':mp.__version__,'dps':a.dps,'moment_crosscheck_dps':a.dps+100},'provenance':{'source_sha256':sha(SOURCE),'source_path':str(SOURCE),'driver_sha256':sha(DRIVER),'frozen_helper_sha256':sha(HELPER),'frozen_helper_path':str(HELPER),'theorems':{name:{'sha256':sha(X/name),'status':'PROVED manual/inherited source-model formula; COMPUTED values here'} for name in THEOREMS},'criterion_audit_sha256':sha(HERE.parent/'adequacy-original-criterion/VERDICT.json')},'assumptions':['ASSUMED inherited finite complete shared random oracle and declared source/seed distribution','ASSUMED classical atomic partial signing, absorbing noncompletion, strict fresh-message verifier and allowed honest cache interface','ASSUMED valid finite register/call budgets, all honest work and circuit/storage separately charged'],'analytic_costs':diagnostics,'rows':rows,'interpretation':'All negative-log2 entries are probability-bound exponents, NOT guaranteed work bits, NIST category, attacks or optimality. Retuned geometry/Smax checks do not transfer baseline theorem.','original_adequacy_verdict':'not established; see own adequacy-original-criterion/VERDICT.md','new_source_game_declarations':0,'whole_goal_complete':False,'source_or_old_calculators_changed':False}
 target=a.out if a.out.suffix else a.out/'results.json';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'output':str(target),'sha256':sha(target),'baseline':baseline,'signature_bytes':diagnostics['signature_bytes_exact'],'logical_cache_bytes':diagnostics['logical_cache_bytes_exact'],'full_target':'not established'}))
 return 0 if baseline else 2
if __name__=='__main__':
 try:sys.exit(main())
 except (ValueError,AssertionError) as err:print('REFUSED: '+str(err),file=sys.stderr);sys.exit(2)
