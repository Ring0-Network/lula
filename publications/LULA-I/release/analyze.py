"""Portable retained-data analysis; does not launch benchmark or signing jobs."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
for script in ['aggregate_a1.py','analyze_b1.py','recompute_data.py','audit_stability.py']:
    subprocess.run([sys.executable,'-I','-B',str(ROOT/'code/python'/script)],cwd=ROOT,check=True)
