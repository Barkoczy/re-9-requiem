#!/usr/bin/env python3
"""Audit translation files against repository translation rules.

Checks:
- matching translation/source files
- forbidden typographic quotes
- markup tag preservation (<...>)
- placeholder preservation ({0}, %d, %s...)
- protected game terms that should stay in English
- banned Czech replacements from glossary rules
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
TRANSLATIONS_ROOT = ROOT / "translations"
SOURCE_ROOT = ROOT / "json"

TAG_RE = re.compile(r"<[^>]+>")
FORMAT_RE = re.compile(r"\{\d+\}|%(?:\d+\$)?[\-+0 #]*\d*(?:\.\d+)?[sdif]")
CURLY_QUOTES_RE = re.compile(r"[„“”«»]")

PROTECTED_TERMS = [
    "Leon S. Kennedy",
    "Grace Ashcroft",
    "Emily",
    "Victor Gideon",
    "Spencer",
    "Chloe",
    "Sherry",
    "Alyssa",
    "Zeno",
    "Chris Redfield",
    "Jill Valentine",
    "Albert Wesker",
    "Raccoon City",
    "R.P.D.",
    "Wrenwood Hotel",
    "Rhodes Hill",
    "Spencer Mansion",
    "Matilda IMP",
    "S&S M232",
    "MSBG 500",
    "Requiem",
    "First Aid Spray",
    "Green Herb",
    "Red Herb",
    "Mortal Edge",
    "Hunting Knife",
    "R.I.P. Knife",
    "Kotetsu",
    "Body Armor",
    "Hatchet",
    "BSAA",
    "FBI",
    "DSO",
    "S.T.A.R.S.",
    "The Connections",
    "T-Virus",
    "Elpis",
    "Plant 43",
    "Licker",
    "Chunk",
    "Titan Spinner",
    "Tyrant",
    "Mr. Raccoon",
]

# Canonical check for source terms where flexible variants are acceptable in Czech text
PROTECTED_VARIANTS = {
    "Umbrella Corporation": ["Umbrella Corporation", "Umbrella", "Umbrelly"],
    "Umbrella": ["Umbrella", "Umbrelly"],
}

BANNED_TRANSLATIONS = {
    "kolimační hledáček": "kolimátor",
    "infikovaná krev": "nakažená krev",
    "koncepční art": "koncepty",
}

NAME_CZECHIZED_PATTERNS = {
    r"\bLeone\b": "Leon",
}


@dataclass
class Issue:
    kind: str
    file: str
    key: str
    detail: str


def load_translation_file(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Translation file is not a JSON object map")
    return data


def load_source_entries(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries")
    if not isinstance(entries, list):
        return {}

    result: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        strings = entry.get("strings") or {}
        en_text = strings.get("en", "") if isinstance(strings, dict) else ""
        if isinstance(name, str) and isinstance(en_text, str):
            result[name] = en_text
    return result


def non_crlf_newline_count(text: str) -> int:
    # Count bare LF, not CRLF pairs.
    return text.count("\n") - text.count("\r\n")


def contains_term(text: str, term: str) -> bool:
    return term.lower() in text.lower()


def check_protected_term(src: str, dst: str, term: str) -> bool:
    if term in PROTECTED_VARIANTS:
        variants = PROTECTED_VARIANTS[term]
        return any(contains_term(dst, v) for v in variants)
    return contains_term(dst, term)


def audit_file(trans_path: Path) -> list[Issue]:
    issues: list[Issue] = []

    rel = trans_path.relative_to(TRANSLATIONS_ROOT)
    src_path = SOURCE_ROOT / rel

    if not src_path.exists():
        issues.append(Issue("missing_source_file", str(rel), "*", str(src_path)))
        return issues

    try:
        trans = load_translation_file(trans_path)
    except Exception as e:  # noqa: BLE001
        issues.append(Issue("invalid_translation_json", str(rel), "*", str(e)))
        return issues

    try:
        src_entries = load_source_entries(src_path)
    except Exception as e:  # noqa: BLE001
        issues.append(Issue("invalid_source_json", str(rel), "*", str(e)))
        return issues

    for key, dst_text in trans.items():
        if not isinstance(key, str) or not isinstance(dst_text, str):
            issues.append(Issue("invalid_entry", str(rel), str(key), "Entry must be string:string"))
            continue

        src_text = src_entries.get(key)
        if src_text is None:
            issues.append(Issue("extra_key", str(rel), key, "Key not present in source entries"))
            continue

        if CURLY_QUOTES_RE.search(dst_text):
            issues.append(Issue("curly_quotes", str(rel), key, "Contains forbidden typographic quotes"))

        src_tags = TAG_RE.findall(src_text)
        dst_tags = TAG_RE.findall(dst_text)
        if src_tags != dst_tags:
            issues.append(Issue("tag_mismatch", str(rel), key, f"src={src_tags} dst={dst_tags}"))

        src_formats = FORMAT_RE.findall(src_text)
        dst_formats = FORMAT_RE.findall(dst_text)
        if sorted(src_formats) != sorted(dst_formats):
            issues.append(
                Issue(
                    "format_token_mismatch",
                    str(rel),
                    key,
                    f"src={sorted(src_formats)} dst={sorted(dst_formats)}",
                )
            )

        # Preserve explicit line break style/count where source uses escaped line breaks.
        if src_text.count("\r\n") != dst_text.count("\r\n"):
            issues.append(
                Issue(
                    "crlf_mismatch",
                    str(rel),
                    key,
                    f"src_crlf={src_text.count('\\r\\n')} dst_crlf={dst_text.count('\\r\\n')}",
                )
            )
        if non_crlf_newline_count(src_text) != non_crlf_newline_count(dst_text):
            issues.append(
                Issue(
                    "lf_mismatch",
                    str(rel),
                    key,
                    (
                        "src_lf="
                        f"{non_crlf_newline_count(src_text)} dst_lf={non_crlf_newline_count(dst_text)}"
                    ),
                )
            )

        # Protected terms must remain in English where they appear in source.
        for term in PROTECTED_TERMS:
            if contains_term(src_text, term) and not check_protected_term(src_text, dst_text, term):
                issues.append(
                    Issue(
                        "protected_term_missing",
                        str(rel),
                        key,
                        f"source contains '{term}'",
                    )
                )

        for term, variants in PROTECTED_VARIANTS.items():
            if contains_term(src_text, term) and not any(contains_term(dst_text, v) for v in variants):
                issues.append(
                    Issue(
                        "protected_term_missing",
                        str(rel),
                        key,
                        f"source contains '{term}', expected one of {variants}",
                    )
                )

        # Banned terminology from glossary constraints.
        for banned, expected in BANNED_TRANSLATIONS.items():
            if contains_term(dst_text, banned):
                issues.append(
                    Issue(
                        "banned_term",
                        str(rel),
                        key,
                        f"contains '{banned}', expected '{expected}'",
                    )
                )

        for pattern, expected in NAME_CZECHIZED_PATTERNS.items():
            if re.search(pattern, dst_text):
                issues.append(
                    Issue(
                        "czechized_name",
                        str(rel),
                        key,
                        f"matches '{pattern}', expected '{expected}'",
                    )
                )

    # Missing keys from translation
    missing = set(src_entries) - set(trans)
    for key in sorted(missing):
        en_text = src_entries.get(key, "")
        if en_text.strip():
            issues.append(Issue("missing_key", str(rel), key, "Non-empty source entry missing in translation"))

    return issues


def collect_translation_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.json")))
        elif path.is_file() and path.suffix == ".json":
            files.append(path)
    return sorted({p.resolve() for p in files})


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit translation rules")
    parser.add_argument(
        "--paths",
        nargs="*",
        default=[str(TRANSLATIONS_ROOT)],
        help="Translation paths to audit",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=200,
        help="Maximum issue lines to print",
    )
    parser.add_argument(
        "--report",
        type=str,
        default="",
        help="Optional file path to write full report",
    )
    args = parser.parse_args()

    files = collect_translation_files([Path(p).resolve() for p in args.paths])
    all_issues: list[Issue] = []

    for file in files:
        all_issues.extend(audit_file(file))

    by_kind: dict[str, int] = {}
    for issue in all_issues:
        by_kind[issue.kind] = by_kind.get(issue.kind, 0) + 1

    print(f"Scanned files: {len(files)}")
    print(f"Total issues: {len(all_issues)}")
    for kind in sorted(by_kind):
        print(f"  {kind}: {by_kind[kind]}")

    lines = [f"{i.kind}\t{i.file}\t{i.key}\t{i.detail}" for i in all_issues]
    for line in lines[: args.max_lines]:
        print(line)
    remaining = len(lines) - args.max_lines
    if remaining > 0:
        print(f"... {remaining} more issues not shown")

    if args.report:
        report_path = Path(args.report).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", encoding="utf-8") as f:
            f.write("kind\tfile\tkey\tdetail\n")
            for line in lines:
                f.write(line + "\n")
        print(f"Report written: {report_path}")

    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
