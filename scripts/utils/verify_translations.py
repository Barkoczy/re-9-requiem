#!/usr/bin/env python3
"""Verify all translation files have correct entries."""

import json
import os

SRC_BASE = '/tmp/re9-translate/json/natives/stm/message/dialog/'
DST_BASE = '/tmp/re9-translate/translations/natives/stm/message/dialog/'

files = [
    'dialog_mangm2.msg.23.json',
    'dialog_movie.msg.23.json',
    'dialog_mangua.msg.23.json',
    'dialog_ff2nd.msg.23.json',
    'dialog_underhb.msg.23.json',
    'dialog_battlepl.msg.23.json',
    'dialog_manlc.msg.23.json',
    'dialog_centba.msg.23.json',
    'dialog_mange.msg.23.json',
    'dialog_platform.msg.23.json',
    'dialog_centuc.msg.23.json',
    'dialog_centhw.msg.23.json',
    'dialog_ending.msg.23.json',
    'dialog_reactionspl.msg.23.json',
]

all_ok = True

for fname in files:
    with open(SRC_BASE + fname) as f:
        src = json.load(f)

    with open(DST_BASE + fname) as f:
        dst = json.load(f)

    # Get source entries with translatable text
    src_entries = {}
    for entry in src['entries']:
        en_text = entry.get('strings', {}).get('en', '')
        if en_text and en_text != '<Sound Team ID>' and en_text.strip():
            src_entries[entry['name']] = en_text

    # Compare
    src_keys = set(src_entries.keys())
    dst_keys = set(dst.keys())

    missing = src_keys - dst_keys
    extra = dst_keys - src_keys

    if missing:
        all_ok = False
        print(f"\n{fname}: MISSING {len(missing)} entries:")
        for k in sorted(missing):
            print(f"  {k}: {src_entries[k]}")

    if extra:
        all_ok = False
        print(f"\n{fname}: EXTRA {len(extra)} entries:")
        for k in sorted(extra):
            print(f"  {k}: {dst[k]}")

    # Check for empty translations
    empty = [k for k, v in dst.items() if not v.strip()]
    if empty:
        all_ok = False
        print(f"\n{fname}: {len(empty)} EMPTY translations:")
        for k in empty:
            print(f"  {k}")

    status = "OK" if not missing and not extra and not empty else "ISSUES"
    print(f"{fname}: src={len(src_entries)} dst={len(dst)} [{status}]")

if all_ok:
    print("\nAll files verified successfully!")
else:
    print("\nSome issues found - see above.")
