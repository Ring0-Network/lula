"""Relative release paths; retained inputs and reruns stay separate."""
import os
from pathlib import Path

CODE = Path(__file__).resolve().parents[2]
RELEASE = CODE.parent
def campaign(name, rerun=False):
    return Path(os.environ.get('LULA_CAMPAIGN_ROOT', RELEASE / ('reruns' if rerun else 'data') / name)).resolve()
def results(name):
    p = Path(os.environ.get('LULA_RESULTS_ROOT', RELEASE / 'generated' / name)).resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p
def build():
    p = Path(os.environ.get('LULA_BUILD_ROOT', RELEASE / 'build')).resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p
