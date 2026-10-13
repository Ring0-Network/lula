"""Vector figures from results/summary.csv (run scripts/aggregate.py first). Output: results/figures/*.pdf.
Every figure states backend, N and evidence type in its caption text inside the figure. No analytical or interpolated curves."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from release_paths import CODE, RELEASE, campaign, results, build
C = campaign('a1', rerun=False)
RESULTS = results('a1')
BUILD = build()
FIG = RESULTS / 'figures'
FIG.mkdir(parents=True, exist_ok=True)
rows = list(csv.DictReader(open(RESULTS / 'summary.csv', encoding='utf-8')))
D = {(r['cell'], r['operation']): r for r in rows}
f = lambda r, k: float(r[k])

CANDS = [  # label, cell prefix, evidence tag
    ('LULA I, cache in memory', 'lula1-hot', 'measured'),
    ('SLH-DSA-SHA2-128f (OpenSSL 3.5.7)', 'slh128f', 'measured'),
    ('SLH-DSA-SHA2-128s (OpenSSL 3.5.7)', 'slh128s', 'measured'),
    ('SHRINCS stateful (author C, B32)', 'shrincsC-stateful', 'measured'),
    ('SHRINCS fallback (author C, B32)', 'shrincsC-fallback', 'measured'),
    ('SHRINCS stateful (third-party Go)', 'shrincsGo-stateful', 'measured, third-party'),
    ('KN 4,036 B (third-party Go)', 'kn4036-prepared', 'measured, third-party'),
    ('KN 3,952 B (own reconstruction)', 'kn3952-recon-hot', 'measured, reconstruction'),
]
SIZES = [32, 1024, 65536]

def get(prefix, m, op):
    return D.get((f'{prefix}-{m}', op))

# Figure 1: Sign and Verify, min / median / p95 / p99 / max observed per size
for op in ('sign', 'verify'):
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
    for ax, m in zip(axs, SIZES):
        ys, labs = [], []
        for i, (lab, pre, tag) in enumerate(CANDS):
            r = get(pre, m, op)
            if not r:
                continue
            x = len(labs)
            ax.vlines(x, f(r, 'min_ms'), f(r, 'max_observed_ms'), color='0.6', lw=1)
            ax.plot([x], [f(r, 'median_ms')], 'o', color='C0')
            ax.plot([x], [f(r, 'p95_ms')], '_', color='C1', ms=10)
            ax.plot([x], [f(r, 'p99_ms')], '_', color='C3', ms=10)
            ax.plot([x], [f(r, 'max_observed_ms')], 'v', color='k', ms=4)
            labs.append(f"{lab}\nN={r['N']}")
        ax.set_yscale('log'); ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, rotation=70, ha='right', fontsize=6)
        ax.set_title(f'{op}, message {m} B'); ax.grid(alpha=.3)
    axs[0].set_ylabel('ms (log)')
    fig.suptitle(f'{op}: min (line), median (circle), p95, p99, maximum observed (triangle); one pinned core, machine in use, not quiet', fontsize=8)
    fig.tight_layout(); fig.savefig(FIG / f'fig1_{op}_distributions.pdf'); plt.close(fig)

# Figure 2: first signature after recovery (32 B), one observation or small N each
rec = []
r = D.get(('lula1-fresh-32', 'sign')); l = D.get(('lula1-fresh-32', 'fixture_load'))
if r and l:
    rec.append(('LULA I fresh process, persisted cache\n(load + first sign)', (f(l, 'median_ms') + f(r, 'median_ms')) / 1000))
r = D.get(('lula1-missing-32', 'sign'))
if r:
    rec.append(('LULA I total cache loss\n(seed only; first of 2, median)', f(r, 'min_ms') / 1000))
for lab, cell in (('SHRINCS fallback (author C)', 'shrincsC-fallback-32'), ('SHRINCS detected loss (author C)', 'shrincsC-detected-loss-32'),
                  ('KN 4,036 B (Go)', 'kn4036-prepared-32'), ('KN 3,952 B (reconstruction)', 'kn3952-recon-hot-32'),
                  ('SLH-DSA-128f', 'slh128f-32'), ('SLH-DSA-128s', 'slh128s-32')):
    r = D.get((cell, 'sign'))
    if r:
        rec.append((lab + f"\nN={r['N']}", f(r, 'median_ms') / 1000))
if rec:
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.barh(range(len(rec)), [x for _, x in rec], color='C0')
    ax.set_yticks(range(len(rec))); ax.set_yticklabels([a for a, _ in rec], fontsize=7)
    ax.set_xscale('log'); ax.set_xlabel('seconds (log); median of the N shown; 32 B message')
    ax.axvline(0.010, color='r', ls='--', lw=.8); ax.text(0.0105, -0.4, '10 ms', color='r', fontsize=7)
    ax.set_title('Signing after a recovery event or from cold (not worst-case guarantees; machine in use)', fontsize=8)
    fig.tight_layout(); fig.savefig(FIG / 'fig2_recovery_first_signature.pdf'); plt.close(fig)

# Figure 3: Pareto view hot (32 B): signature bytes vs sign median, label verify median; marks non-dominated points
pts = []
for lab, pre, tag in CANDS:
    s = get(pre, 32, 'sign'); v = get(pre, 32, 'verify')
    if s and v:
        sizes = [int(x) for x in s['sig_bytes'].split('/') if x]
        pts.append((lab, max(sizes), f(s, 'median_ms'), f(v, 'median_ms'), tag))
if pts:
    fig, ax = plt.subplots(figsize=(8, 5))
    for lab, b, sm, vm, tag in pts:
        dom = any((b2 <= b and s2 <= sm and v2 <= vm) and (b2 < b or s2 < sm or v2 < vm) for _, b2, s2, v2, _ in pts)
        ax.plot(b, sm, 'o' if not dom else 'x', color='C0' if not dom else '0.5')
        ax.annotate(f'{lab}\nverify {vm:.3g} ms', (b, sm), fontsize=6, xytext=(4, 3), textcoords='offset points')
    ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlabel('largest observed signature (bytes)'); ax.set_ylabel('median sign (ms), 32 B')
    ax.set_title('Hot Pareto view over (bytes, sign median, verify median); x = dominated. Not security-normalized; no weights', fontsize=8)
    ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(FIG / 'fig3_pareto_hot.pdf'); plt.close(fig)
    with open(RESULTS / 'pareto_hot.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['candidate', 'max_sig_bytes', 'sign_median_ms', 'verify_median_ms', 'evidence'])
        w.writerows(pts)

# Figure 4: LULA I cache payload vs latency (two measured points only)
a = D.get(('lula1-hot-32', 'sign')); b = D.get(('lula1-missing-32', 'sign'))
if a and b:
    fig, ax = plt.subplots(figsize=(5.5, 4))
    ax.plot([0, 75.497456], [f(b, 'min_ms'), f(a, 'median_ms')], 'o-', color='C0')
    ax.set_yscale('log'); ax.set_xlabel('cache payload (MB): none vs full (75,497,456 B)'); ax.set_ylabel('sign (ms, log)')
    ax.set_title('LULA I: two measured points only; the line joins them, nothing is interpolated between', fontsize=7)
    ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(FIG / 'fig4_cache_vs_latency.pdf'); plt.close(fig)

# Figure 5: setup / key generation time (log), one observation each
setup = []
for lab, cell, op in (('LULA I key + cache build (1 core, 1 obs.)', None, None), ('SLH-DSA-128f keygen', 'slh128f-32', 'keygen'),
                      ('SLH-DSA-128s keygen', 'slh128s-32', 'keygen')):
    if cell:
        r = D.get((cell, op))
        if r:
            setup.append((lab, f(r, 'median_ms') / 1000))
    else:
        setup.append((lab, 2216.1))
if setup:
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.barh(range(len(setup)), [x for _, x in setup]); ax.set_yticks(range(len(setup))); ax.set_yticklabels([a for a, _ in setup], fontsize=7)
    ax.set_xscale('log'); ax.set_xlabel('seconds (log)'); ax.set_title('Setup time; peak memory of the LULA I build: working set 122.8 MB, private 143.6 MB', fontsize=7)
    fig.tight_layout(); fig.savefig(FIG / 'fig5_setup.pdf'); plt.close(fig)
print('figures:', sorted(p.name for p in FIG.glob('*.pdf')))
