#!/usr/bin/env python3
"""Check every supporting theorem and its printed axioms; never install tools.

Use a prepared local Lake project, or --mathlib-project for an existing pinned
Mathlib checkout. Tool paths can be supplied with --lake or LULA_LAKE.
Exit 0: all checks passed; 1: failed check; 2: unavailable prerequisite.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(argv, cwd, env):
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True,
                            text=True, encoding="utf-8", timeout=180)
    if result.returncode:
        raise ValueError(result.stdout + result.stderr)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib-project", type=Path,
                        default=os.environ.get("LULA_MATHLIB_PROJECT"))
    parser.add_argument("--lake", default=os.environ.get("LULA_LAKE", "lake"))
    args = parser.parse_args()
    inventory = json.loads((HERE / "statements.json").read_text(encoding="utf-8"))
    project = args.mathlib_project.resolve() if args.mathlib_project else HERE
    mathlib = project if args.mathlib_project else HERE / ".lake/packages/mathlib"
    if not mathlib.is_dir():
        raise FileNotFoundError("Prepared Mathlib dependency missing; supply --mathlib-project or prepare this Lake project.")
    lake = shutil.which(args.lake)
    if not lake:
        raise FileNotFoundError("Lake unavailable; supply --lake or LULA_LAKE.")
    env = dict(os.environ)
    env["PATH"] = str(Path(lake).resolve().parent) + os.pathsep + env.get("PATH", "")
    revision = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"], project, env).strip()
    if revision != inventory["mathlib_revision"]:
        raise ValueError("Mathlib revision differs from the pinned inventory.")
    version = run([lake, "env", "lean", "--version"], project, env).strip()
    if not re.search(r"Lean \(version 4\.28\.0,", version):
        raise ValueError("Lean 4.28.0 is required.")
    allowed = set(inventory["axiom_allowlist"])
    results = []
    for entry in inventory["files"]:
        source = HERE / entry["file"]
        original = source.read_bytes()
        if hashlib.sha256(original).hexdigest() != entry["sha256"]:
            raise ValueError("Source hash differs: " + entry["file"])
        text = original.decode("utf-8")
        if re.search(r"\b(sorry|admit|native_decide|sorryAx)\b|^\s*axiom\s", text, re.M):
            raise ValueError("Forbidden admission or axiom in " + entry["file"])
        declarations = re.findall(r"^theorem\s+(\w+)\b", text, re.M)
        if declarations != [item["name"].split(".")[-1] for item in entry["declarations"]]:
            raise ValueError("Declaration inventory differs: " + entry["file"])
        output = run([lake, "env", "lean", str(source)], project, env)
        axioms = {}
        for declaration in entry["declarations"]:
            name = declaration["name"]
            match = re.search(re.escape("'" + name + "'") +
                              r" depends on axioms: \[([^\]]*)\]", output)
            if match:
                used = {item.strip() for item in match.group(1).split(",") if item.strip()}
            elif "'" + name + "' does not depend on any axioms" in output:
                used = set()
            else:
                raise ValueError("Missing printed axiom check: " + name)
            if not used <= allowed:
                raise ValueError("Unexpected axioms for " + name + ": " + repr(sorted(used)))
            axioms[name] = sorted(used)
        if source.read_bytes() != original:
            raise ValueError("Source changed during check: " + entry["file"])
        results.append({"file": entry["file"], "theorems": len(axioms), "axioms": axioms})
    count = sum(item["theorems"] for item in results)
    if count != inventory["expected_theorem_count"]:
        raise ValueError("Unexpected theorem total.")
    print(json.dumps({"status": "CHECKED_SUPPORTING_COMPONENTS", "theorems": count,
                      "lean_version": version, "mathlib_revision": revision,
                      "files": results, "complete_signature_security_checked": False,
                      "source_or_Rust_refinement_checked": False}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, PermissionError) as error:
        print(json.dumps({"status": "UNCHECKED", "reason": str(error)}), file=sys.stderr)
        sys.exit(2)
    except (ValueError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"status": "FAILED", "reason": str(error)}), file=sys.stderr)
        sys.exit(1)
