import json
import sys

base = '/tmp/re9-translate/json/natives/stm/message/dialog/'

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

for fname in files:
    with open(base + fname) as f:
        data = json.load(f)

    print(f"=== {fname} ===")
    for entry in data['entries']:
        en_text = entry.get('strings', {}).get('en', '')
        if en_text and en_text != '<Sound Team ID>' and en_text.strip():
            print(f'{entry["name"]}|{en_text}')
    print()
