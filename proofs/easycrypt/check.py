#!/usr/bin/env python3
"""Compile the nine supporting EasyCrypt lemmas with the pinned local stack.

No tool or solver installation/configuration is performed. Override executable
locations with CLI flags or LULA_EASYCRYPT/LULA_WHY3/LULA_Z3. A configured Why3
file may be supplied with --why3-config. No verification-result cache is used.
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


def run(argv):
    result = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", timeout=180)
    if result.returncode:
        raise ValueError(result.stdout + result.stderr)
    return result.stdout + result.stderr


def executable(value):
    found = shutil.which(value)
    if not found:
        raise FileNotFoundError("Executable unavailable: " + value)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--easycrypt", default=os.environ.get("LULA_EASYCRYPT", "easycrypt"))
    parser.add_argument("--why3", default=os.environ.get("LULA_WHY3", "why3"))
    parser.add_argument("--z3", default=os.environ.get("LULA_Z3", "z3"))
    parser.add_argument("--why3-config", type=Path)
    args = parser.parse_args()
    tools = json.loads((HERE / "toolchain.json").read_text(encoding="utf-8"))
    inventory = json.loads((HERE / "statements.json").read_text(encoding="utf-8"))
    ec, why3, z3 = map(executable, (args.easycrypt, args.why3, args.z3))
    config_args = ["-why3", str(args.why3_config)] if args.why3_config else []
    config = run([ec, "config", *config_args])
    if "git-hash: " + tools["easycrypt_git_hash"] not in config:
        raise ValueError("EasyCrypt version differs from toolchain.json.")
    if run([why3, "--version"]).strip() != tools["why3_version"]:
        raise ValueError("Why3 version differs from toolchain.json.")
    if run([z3, "--version"]).strip() != tools["z3_version"]:
        raise ValueError("Z3 version differs from toolchain.json.")
    if "Z3@4.8.12" not in config:
        raise ValueError("EasyCrypt's configured prover set does not contain pinned Z3.")
    match = re.search(r"(?m)^\s+<system>@([^\n]+/theories)\s*$", config)
    if not match:
        raise ValueError("Cannot identify the installed standard-library root.")
    libraries = Path(match.group(1).strip())
    for relative, expected in tools["direct_library_sha256"].items():
        source = libraries / relative
        if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            raise ValueError("Direct standard-library hash differs: " + relative)
    results = []
    for entry in inventory["files"]:
        source = HERE / entry["file"]
        original = source.read_bytes()
        if hashlib.sha256(original).hexdigest() != entry["sha256"]:
            raise ValueError("Proof source hash differs: " + entry["file"])
        text = original.decode("utf-8")
        without_comments = re.sub(r"\(\*.*?\*\)", "", text, flags=re.S)
        if re.search(r"\b(axiom|admit|admitted|abort|sorry)\b", without_comments):
            raise ValueError("Admission or custom axiom in " + entry["file"])
        names = re.findall(r"^lemma\s+(\w+)\b", text, re.M)
        if names != [item["name"] for item in entry["declarations"]]:
            raise ValueError("Lemma inventory differs: " + entry["file"])
        run([ec, "compile", *config_args, "-no-eco", "-p", tools["selected_prover"], str(source)])
        if source.read_bytes() != original:
            raise ValueError("Proof source changed during checking.")
        results.append({"file": entry["file"], "lemmas": names})
    count = sum(len(item["lemmas"]) for item in results)
    if count != inventory["expected_lemma_count"]:
        raise ValueError("Unexpected lemma total.")
    print(json.dumps({"status": "CHECKED_SUPPORTING_COMPONENTS", "lemmas": count,
                      "easycrypt_git_hash": tools["easycrypt_git_hash"],
                      "why3_version": tools["why3_version"], "z3_version": tools["z3_version"],
                      "custom_axiom_declarations": 0, "files": results,
                      "trust_scope": inventory["trusted_stack"],
                      "complete_signature_security_checked": False,
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
