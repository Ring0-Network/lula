"""Campaign Go build: one worker, local caches, QPC timer patch in sources/hashsig-go/go/cmd/hashsig_driver."""
import importlib.util, json
from pathlib import Path
from release_paths import CODE, RELEASE, campaign, results, build
ROOT = campaign('a1', rerun=True)
RESULTS = results('a1')
BUILD = build()
(ROOT / 'raw').mkdir(parents=True, exist_ok=True)
(ROOT / 'vectors').mkdir(parents=True, exist_ok=True)
import os, shutil
GO = Path(os.environ.get('LULA_GO', shutil.which('go') or 'go'))
HASHSIG_SOURCE = Path(os.environ.get('LULA_HASHSIG_SOURCE', RELEASE / 'external' / 'hashsig-go' / 'go'))
spec = importlib.util.spec_from_file_location('bounded_run', Path(__file__).with_name('bounded_run.py'))
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
env = {'GOMAXPROCS': '1', 'GOMEMLIMIT': '2560MiB', 'GOCACHE': str(BUILD / 'go-cache'),
       'GOMODCACHE': str(BUILD / 'go-modcache'), 'GOPATH': str(BUILD / 'go-path'),
       'GOENV': 'off', 'GOTOOLCHAIN': 'local', 'CGO_ENABLED': '0', 'GOFLAGS': '-mod=mod', 'GOPROXY': 'off'}
r = mod.run([str(GO), 'build', '-p=1', '-trimpath', '-buildvcs=false', '-o', str(BUILD / 'hashsig_driver.exe'),
             './cmd/hashsig_driver'], ROOT / 'raw' / 'go-qpc-build', HASHSIG_SOURCE, cpu=4,
            timeout=900, env=env)
print(json.dumps(r, indent=1))
