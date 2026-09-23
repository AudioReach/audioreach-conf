#!/usr/bin/env python3
"""
Validate audioreach-conf folder structure using per-vendor rules.

Each vendor in VENDOR_CONFIG declares:
  required_files  – files that must exist at the vendor root
  file_rules      – one line per allowed file location:
                    <bu>/<chip>/<subdir>/*.ext1,*.ext2
  exceptions      – relative paths (from vendor root) to skip during validation;
                    supports * wildcards, e.g. "bu1/chip1/acdbdata/legacy.acdb"
                    or "bu1/unknown_dir/" to skip an unexpected directory

Usage:
  python3 validate_qcom_conf.py <path/to/repo>
         validates all configured vendors found under the repo root

  python3 validate_qcom_conf.py <path/to/vendor>
         validates a single vendor dir
"""

import sys
import os
import fnmatch


def dbg(msg):
    print(f"[DEBUG] {msg}", file=sys.stderr)

VENDOR_CONFIG = {
    "qcom": {
        "required_files": ["kvh2xml.h"],
        "file_rules": [
            "<bu>/<chip>/acdbdata/*.acdb,*.qwsp",
        ],
        "exceptions": [
            "./qcom/qli/sm8750/*.acdb",  # example: skip a specific file
            # "bu1/unknown_dir/",                # example: skip an unexpected dir
        ],
    },
    "nxp": {
        "required_files": ["kvh2xml.h"],
        "file_rules": [
            "<bu>/acdbdata/*.acdb,*.qwsp",
        ],
        "exceptions": [],
    },
}

VENDORS = tuple(VENDOR_CONFIG)


def is_exception(rel_path, exceptions):
    """Return True if rel_path matches any exception pattern (supports * wildcards)."""
    normalized = rel_path.replace(os.sep, "/")
    for pattern in exceptions:
        if fnmatch.fnmatch(normalized, pattern.rstrip("/")):
            return True
    return False


def subdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def parse_rules(file_rules):
    """Parse rule strings like '<bu>/<chip>/acdbdata/*.acdb,*.qwsp' into dicts."""
    parsed = []
    for rule in file_rules:
        parts = rule.split("/")
        dir_pattern = parts[:-1]
        exts = {g.lstrip("*") for g in parts[-1].split(",")}
        parsed.append({"dir_pattern": dir_pattern, "exts": exts})
    return parsed


def parse_required_entry(entry):
    """Return (wildcard_depth, literal_suffix) for a required_files entry.

    "kvh2xml.h"            -> (0, "kvh2xml.h")        plain file at vendor root
    "<bu>/<chip>/abc.txt"  -> (2, "abc.txt")           file under every bu/chip
    "<bu>/readme.txt"      -> (1, "readme.txt")        file under every bu
    """
    parts = entry.split("/")
    depth = 0
    while depth < len(parts) and parts[depth].startswith("<"):
        depth += 1
    suffix = os.path.join(*parts[depth:])
    return depth, suffix


def derive_depth_leaves(parsed_rules):
    """Map parent_depth -> set of allowed leaf subdir names, derived from rules.

    For <bu>/<chip>/acdbdata/  -> depth 2, leaf "acdbdata"
    For <bu>/acdbdata/         -> depth 1, leaf "acdbdata"
    """
    result = {}
    for rule in parsed_rules:
        dp = rule["dir_pattern"]
        for i in range(len(dp) - 1, -1, -1):
            if not dp[i].startswith("<"):
                result.setdefault(i, set()).add(dp[i])
                break
    return result


def walk_to_depth(base_path, depth):
    """Yield all directory paths exactly `depth` wildcard levels below base_path."""
    if depth == 0:
        yield base_path
        return
    for d in subdirs(base_path):
        yield from walk_to_depth(os.path.join(base_path, d), depth - 1)


def rule_to_path(vendor_name, rule):
    return vendor_name + "/" + "/".join(rule["dir_pattern"]) + "/"


def matches_rule(rel_parts, rule):
    dp = rule["dir_pattern"]
    if len(rel_parts) != len(dp) + 1:
        return False
    if os.path.splitext(rel_parts[-1])[1] not in rule["exts"]:
        return False
    return all(
        pat.startswith("<") or actual == pat
        for actual, pat in zip(rel_parts[:-1], dp)
    )


def check_calib_file_locations(vendor_path, parsed_rules, exceptions, failures):
    vendor_name = os.path.basename(vendor_path)
    all_exts = {ext for rule in parsed_rules for ext in rule["exts"]}

    for root, _dirs, files in os.walk(vendor_path):
        before = len(failures)
        for fname in files:
            ext = os.path.splitext(fname)[1]
            if ext not in all_exts:
                continue
            file_path = os.path.join(root, fname)
            rel_parts = os.path.relpath(file_path, vendor_path).split(os.sep)
            if any(matches_rule(rel_parts, rule) for rule in parsed_rules):
                dbg(f"  Checking file: {file_path} ... PASS")
                continue
            rel_path = os.path.relpath(file_path, vendor_path)
            if is_exception(rel_path, exceptions):
                dbg(f"  Checking file: {file_path} ... SKIP (exception)")
                continue
            valid = ", ".join(
                rule_to_path(vendor_name, r)
                for r in parsed_rules if ext in r["exts"]
            )
            dbg(f"  Checking file: {file_path} ... FAIL")
            failures.append(
                f"WRONG LOCATION  {file_path}\n"
                f"              expected inside {valid}"
            )
        dbg(f"Scanning directory: {root} ... {'PASS' if len(failures) == before else 'FAIL'}")


def check_dir_structure(vendor_path, required_files, parsed_rules, exceptions, failures):
    for entry in required_files:
        wildcard_depth, suffix = parse_required_entry(entry)
        for parent_path in walk_to_depth(vendor_path, wildcard_depth):
            target = os.path.join(parent_path, suffix)
            if not os.path.isfile(target):
                rel_path = os.path.relpath(target, vendor_path)
                if is_exception(rel_path, exceptions):
                    dbg(f"Checking required file: {target} ... SKIP (exception)")
                else:
                    dbg(f"Checking required file: {target} ... FAIL")
                    failures.append(f"MISSING  {target}")
            else:
                dbg(f"Checking required file: {target} ... PASS")

    for parent_depth, allowed_leaves in derive_depth_leaves(parsed_rules).items():
        for parent_path in walk_to_depth(vendor_path, parent_depth):
            before = len(failures)
            for d in subdirs(parent_path):
                if d not in allowed_leaves:
                    rel_path = os.path.relpath(os.path.join(parent_path, d), vendor_path)
                    if is_exception(rel_path, exceptions):
                        dbg(f"  Unexpected dir: {parent_path}/{d}/ ... SKIP (exception)")
                    else:
                        failures.append(
                            f"UNEXPECTED DIR  {parent_path}/{d}/  "
                            f"(allowed: {', '.join(sorted(allowed_leaves))})"
                        )
            for leaf in allowed_leaves:
                leaf_path = os.path.join(parent_path, leaf)
                if os.path.isdir(leaf_path):
                    for d in subdirs(leaf_path):
                        rel_path = os.path.relpath(os.path.join(leaf_path, d), vendor_path)
                        if is_exception(rel_path, exceptions):
                            dbg(f"  Unexpected subdir: {leaf_path}/{d}/ ... SKIP (exception)")
                        else:
                            failures.append(
                                f"UNEXPECTED DIR  {leaf_path}/{d}/  "
                                f"({leaf}/ must be flat, no subdirs)"
                            )
            dbg(f"Scanning directory structure: {parent_path} ... {'PASS' if len(failures) == before else 'FAIL'}")


def validate_vendor(vendor_path):
    name = os.path.basename(vendor_path)
    cfg = VENDOR_CONFIG.get(name, VENDOR_CONFIG["qcom"])
    parsed_rules = parse_rules(cfg["file_rules"])
    exceptions = cfg.get("exceptions", [])

    failures = []
    check_dir_structure(vendor_path, cfg["required_files"], parsed_rules, exceptions, failures)
    check_calib_file_locations(vendor_path, parsed_rules, exceptions, failures)
    return failures


def run(path):
    path = os.path.normpath(path)
    if not os.path.isdir(path):
        print(f"FAIL: '{path}' is not a directory")
        sys.exit(1)

    vendor_paths = []
    basename = os.path.basename(path)
    if basename in VENDORS:
        vendor_paths = [path]
    else:
        for v in VENDORS:
            vp = os.path.join(path, v)
            if os.path.isdir(vp):
                vendor_paths.append(vp)
        if not vendor_paths:
            vendor_paths = [path]

    all_failures = {}
    for vp in vendor_paths:
        dbg(f"Validating vendor: {vp}")
        failures = validate_vendor(vp)
        if failures:
            all_failures[os.path.basename(vp)] = failures

    if all_failures:
        print("FAIL")
        for vendor, failures in all_failures.items():
            print(f"\n  [{vendor}]")
            for msg in failures:
                print(f"    {msg}")
        sys.exit(1)
    else:
        print("PASS")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path/to/repo|path/to/vendor>")
        sys.exit(1)
    run(sys.argv[1])
