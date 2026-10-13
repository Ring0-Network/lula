"""Entry point for the independently derived component calculations.

Run python -I -B bounds.py --out results
This does not compute a complete EUF-CMA bound; unknown terms remain null.
"""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).resolve().parent / 'numerics' / 'bounds.py'), run_name='__main__')
