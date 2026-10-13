"""Check that tracked files contain only the maintained proof/test package."""
from pathlib import Path, PurePosixPath
import argparse
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
ROOT_FILES={'.gitignore','.gitattributes','README.md','LICENSE','NOTICE','requirements.txt'}
DIR_SUFFIXES={
 'models':{'.py'}, 'tests':{'.py','.json'}, 'scripts':{'.py'},
 'verifiers':{'.py'}, 'LICENSES':{'.txt'}, 'proofs':{'.py','.json','.lean','.ec','.toml'},
}
FORBIDDEN_PARTS={'hypotheses','editorial','attempts','drafts','work','snapshot','receipts',
 '.lake','target','node_modules','__pycache__','.venv','.git'}
FORBIDDEN_NAME=re.compile(r'(?i)(?:^|[-_])(audit|handoff|hypothes(?:is|es)|kickoff|provenance|draft|first-derivation|worklog)(?:[-_.]|$)')
PROOF_METADATA={'proofs/lean/lean-toolchain','proofs/lean/lakefile.toml',
 'proofs/lean/lake-manifest.json','proofs/lean/statements.json',
 'proofs/easycrypt/statements.json','proofs/easycrypt/toolchain.json'}
SECRET_PATTERNS={
 'private key':re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
 'GitHub token':re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})'),
 'API token':re.compile(rb'sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{45,}'),
 'local profile path':re.compile(rb'(?i)[A-Z]:[\\/]+Users[\\/]+(?!PUBLIC(?:[\\/]|$)|<)[A-Za-z0-9_.-]+[\\/]'),
}

def allowed(name):
 p=PurePosixPath(name)
 if p.is_absolute() or '..' in p.parts or any(s.lower() in FORBIDDEN_PARTS for s in p.parts):return False
 if name in ROOT_FILES:return True
 if p.name.startswith('.env') or FORBIDDEN_NAME.search(p.name):return False
 if p.parts[0]=='.github':
  return name=='.github/CODEOWNERS' or (len(p.parts)==3 and p.parts[1]=='workflows' and p.suffix in {'.yml','.yaml'})
 if name in PROOF_METADATA:return True
 if p.parts[0]=='proofs' and p.suffix in {'.json','.toml'}:return False
 if p.parts[0]=='tests' and p.suffix=='.json' and not (len(p.parts)==3 and p.parts[1]=='fixtures'):return False
 return p.parts[0] in DIR_SUFFIXES and p.suffix in DIR_SUFFIXES[p.parts[0]]

def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])

def inspect_names(names):
 errors=[]
 for name in names:
  if not allowed(name):errors.append((name,'not an allowed proof/test path'))
  path=ROOT/name
  if path.is_symlink():errors.append((name,'symlinks are not allowed'));continue
  if not path.is_file():errors.append((name,'tracked file missing'));continue
  data=path.read_bytes()
  if len(data)>2_000_000:errors.append((name,'unexpectedly large proof/test file'))
  for label,pattern in SECRET_PATTERNS.items():
   if pattern.search(data):errors.append((name,label))
  if path.suffix=='.json':
   import json
   try:json.loads(data)
   except (ValueError,UnicodeError):errors.append((name,'invalid JSON'))
  if name.startswith('.github/workflows/'):
   for action in re.findall(r'^\s*-?\s*uses:\s*([^\s#]+)',data.decode('utf8'),re.M):
    if not action.startswith('./') and not re.fullmatch(r'[^@]+@[0-9a-f]{40}',action):
     errors.append((name,'action is not pinned to a full commit'))
 return errors

def check_commit():
 expected=('ring0code','341783300+ring0code@users.noreply.github.com')
 fields=git('show','-s','--format=%an%n%ae%n%cn%n%ce%n%B','HEAD').decode('utf8').splitlines()
 assert tuple(fields[:2])==expected and tuple(fields[2:4])==expected,'Author and committer must be ring0code'
 assert not any(s.lower().startswith('co-authored-by:') for s in fields[4:]),'Coauthor trailer is not allowed'

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--commit',action='store_true');args=ap.parse_args()
 names=[s.decode('utf8') for s in git('ls-files','-z').split(b'\0') if s]
 errors=inspect_names(names)
 for path,reason in errors:print(f'{path}: {reason}',file=sys.stderr)
 if errors:return 1
 if args.commit:check_commit()
 print(f'PASS repository policy: {len(names)} tracked proof/test files')
 return 0

if __name__=='__main__':raise SystemExit(main())
