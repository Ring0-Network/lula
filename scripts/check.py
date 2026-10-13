"""Run portable repository and Python validation checks without signing."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
commands=[
 [sys.executable,'-I','-B',str(ROOT/'scripts/repository_policy.py')],
 [sys.executable,'-I','-B','-m','unittest','discover','-s',str(ROOT/'tests'),'-p','test_*.py','-v'],
]
for command in commands:
 result=subprocess.run(command,cwd=ROOT)
 if result.returncode:raise SystemExit(result.returncode)
print('PASS Python proof-model and public-vector checks; no full-security certification')
