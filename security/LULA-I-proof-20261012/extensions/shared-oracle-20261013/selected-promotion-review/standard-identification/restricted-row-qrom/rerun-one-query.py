import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2] / "root-keyed-review"
SCRIPT = ROOT / "one_query_completion.py"
assert hashlib.sha256((ROOT / "ONE-QUERY-COMPLETION.md").read_bytes()).hexdigest() == "7def78f7f5e771e397373f7ad81c7977674669d2064a3b2ce1a31e13d31bf1f0"
DEST = HERE / "one-query-rerun"
DEST.mkdir(exist_ok=True)
text = SCRIPT.read_text(encoding="utf-8")
needle = "(E/'ONE-QUERY-CONTROL.json').write_text"
assert text.count(needle) == 1
text = text.replace(needle, "(ROOT_REVIEW_DEST/'ONE-QUERY-CONTROL.json').write_text")
exec(compile(text, str(SCRIPT), "exec"), {"__file__": str(SCRIPT), "ROOT_REVIEW_DEST": DEST})
