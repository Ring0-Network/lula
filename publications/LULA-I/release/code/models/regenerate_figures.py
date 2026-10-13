"""Reproduce publication figure data/styles from saved observations only.

SPDX-License-Identifier: Apache-2.0. Writes recomputed/figures, never paper/.
"""
from pathlib import Path
import csv,json,statistics,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'recomputed/figures';OUT.mkdir(parents=True,exist_ok=True)
A=ROOT/'data/a1/raw';B=ROOT/'data/b1/raw'
def records(path):
    with path.open(newline='',encoding='utf8') as f:return list(csv.DictReader(f))
def samples(path,op):return [int(r['ns'])/1e6 for r in records(path) if r['operation']==op]
def main():
    audit=json.loads((ROOT/'recomputed/data/RECOMPUTED_DATA.json').read_text(encoding='utf8'))
    lookup={(r['cell'],r['operation']):r for r in audit['a1']['admitted_cells']}
    def admitted(cell,op):
        r=lookup[cell,op];v=[x for name in r['files'] for x in samples(A/name,op)]
        assert len(v)==r['N']; return v
    plt.rcParams.update({'font.size':9,'axes.labelsize':9,'legend.fontsize':8,'pdf.fonttype':42,'ps.fonttype':42})
    fig,axs=plt.subplots(2,1,figsize=(4.8,4.5),layout='constrained')
    for ax,op in zip(axs,['sign','verify']):
        for cell,label,color in [('lula1-hot-32','LULA I (prepared)','#126b70'),('slh128f-32','SLH-DSA SHA2-128f','#bb6600'),('slh128s-32','SLH-DSA SHA2-128s','#634595')]:
            x=sorted(admitted(cell,op));ax.step(x,[(i+1)/len(x) for i in range(len(x))],where='post',label=label,color=color)
        ax.set_xscale('log');ax.xaxis.set_minor_formatter(NullFormatter());ax.set_ylim(0,1.02);ax.set_ylabel('Fraction of samples');ax.set_xlabel(op.capitalize()+' elapsed latency (ms)');ax.grid(alpha=.18);ax.legend(loc='lower right')
    fig.savefig(OUT/'comparison-distributions.pdf');plt.close(fig)
    fresh=next(r for r in audit['a1']['fresh'] if r['candidate']=='lula1')
    paired=[];sign=[]
    for name in fresh['files']:
        r=records(A/name);l=sum(int(x['ns']) for x in r if x['operation']=='fixture_load')/1e9;s=sum(int(x['ns']) for x in r if x['operation']=='sign')/1e9
        paired.append(l+s);sign.append(s)
    cold=audit['a1']['cache_loss_consecutive_calls']
    data=[('Prepared Sign; N=1,000',[x/1000 for x in admitted('lula1-hot-32','sign')]),('First Sign after load; N=10',sign),('Paired load + first Sign; N=10',paired),('Cache absent: first; N=1',[cold[0]['ns']/1e9]),('Cache absent: second; same process',[cold[1]['ns']/1e9])]
    fig,ax=plt.subplots(figsize=(4.8,3.3),layout='constrained')
    for i,(label,vals) in enumerate(data):
        med=statistics.median(vals);ax.plot([min(vals),max(vals)],[i,i],color='#126b70',linewidth=2);ax.scatter(med,i,s=32,color='#126b70',zorder=3);ax.annotate(f'{med:.6g} s',(med,i),xytext=(5,8),textcoords='offset points',fontsize=8)
    ax.set_yticks(range(len(data)),[a for a,b in data]);ax.set_ylim(len(data)-.5,-.65);ax.set_xscale('log');ax.xaxis.set_minor_formatter(NullFormatter());ax.set_xlim(.001,1500);ax.set_xlabel('Elapsed time (seconds, logarithmic scale)');ax.grid(axis='x',alpha=.18)
    fig.savefig(OUT/'comparison-recovery.pdf');plt.close(fig)
    follow=json.loads((ROOT/'recomputed/stability-audit/VALIDATED_STABILITY.json').read_text(encoding='utf8'))
    plt.rcParams.update({'pdf.fonttype':42,'ps.fonttype':42,'font.size':10,'axes.labelsize':10,'axes.titlesize':11,'legend.fontsize':9})
    fig,axs=plt.subplots(1,2,figsize=(6.8,2.9),sharey=True)
    colors={'lula':'#173f5f','slh128f':'#b45d15','slh128s':'#236b42'};names={'lula':'LULA I, prepared','slh128f':'OpenSSL SHA2-128f','slh128s':'OpenSSL SHA2-128s'}
    for ax,op in zip(axs,['sign','verify']):
        for alg in names:
            jobs=[j for j in follow['jobs'] if j['alg']==alg and j['msg']==32 and not j['contaminated']]
            x=sorted(v for j in jobs for v in samples(B/(j['job']+'.csv'),op));y=[(i+1)/len(x) for i in range(len(x))]
            ax.step(x,y,where='post',color=colors[alg],linewidth=1,label=f"{names[alg]} ($N={len(x):,}$)");ax.plot(x[-1],1,'o',color=colors[alg],markersize=2.4)
        ax.set_xscale('log');ax.set_ylim(0,1.025);ax.set_xlabel('Elapsed time (ms, log scale)');ax.set_title('Signing' if op=='sign' else 'Verification');ax.grid(True,which='major',alpha=.2)
    axs[0].set_ylabel('Empirical cumulative probability');handles,labels=axs[1].get_legend_handles_labels();fig.tight_layout(pad=1,rect=(0,.17,1,1));fig.legend(handles,labels,loc='lower center',ncol=2,frameon=False,bbox_to_anchor=(.5,-.005))
    fig.savefig(OUT/'stability-distributions.pdf',bbox_inches='tight',metadata={'Title':'LULA I gated follow-up empirical latency distributions','Author':'Ring0 Labs'});plt.close(fig)
    print(json.dumps({'status':'REGENERATED_FROM_RETAINED_OBSERVATIONS','figures':[{ 'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(OUT.glob('*.pdf'))],'limit':'Separate cohorts; no normalized ranking or intermediate cache-size curve.'}))
if __name__=='__main__':main()
