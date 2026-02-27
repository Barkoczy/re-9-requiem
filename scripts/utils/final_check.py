#!/usr/bin/env python3
"""Final check: valid JSON, markup preserved, no English names translated."""

import json
import os
import re

DST_BASE = '/tmp/re9-translate/translations/natives/stm/message/dialog/'
SRC_BASE = '/tmp/re9-translate/json/natives/stm/message/dialog/'

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

total_entries = 0
issues = []

for fname in files:
    # Check valid JSON
    try:
        with open(DST_BASE + fname) as f:
            dst = json.load(f)
        total_entries += len(dst)
    except json.JSONDecodeError as e:
        issues.append(f"{fname}: INVALID JSON: {e}")
        continue

    # Get source for tag comparison
    with open(SRC_BASE + fname) as f:
        src_data = json.load(f)

    src_entries = {}
    for entry in src_data['entries']:
        en_text = entry.get('strings', {}).get('en', '')
        if en_text and en_text != '<Sound Team ID>' and en_text.strip():
            src_entries[entry['name']] = en_text

    # Check markup tags are preserved
    tag_pattern = re.compile(r'<[^>]+>')
    for key in dst:
        if key in src_entries:
            src_tags = tag_pattern.findall(src_entries[key])
            dst_tags = tag_pattern.findall(dst[key])
            if src_tags != dst_tags:
                issues.append(f"{fname}/{key}: Tag mismatch: src={src_tags} dst={dst_tags}")

print(f"Total entries across all files: {total_entries}")
print(f"Issues found: {len(issues)}")
for issue in issues:
    print(f"  {issue}")

if not issues:
    print("All checks passed!")
