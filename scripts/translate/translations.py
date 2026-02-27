#!/usr/bin/env python3
"""Translate RE9 dialog files from English to Czech."""
import json
import os

RN = "\r\n"
base_out = "/tmp/re9-translate/translations/natives/stm/message/dialog"
os.makedirs(base_out, exist_ok=True)


def write_json(filename, data):
    path = os.path.join(base_out, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written {path}: {len(data)} entries")


def build_underco():
    d = {}
    d["UnderCO_c520s100_0000_ch0200"] = "<Sound Team ID>"
    d["UnderCO_c520s100_0000_ch0100"] = "<Sound Team ID>"
    d["UnderCO_c520s100_0020_ch0200"] = "Leone. Jsi v po\u0159\u00e1dku?"
    d["UnderCO_c520s100_0030_ch0100"] = "Jak dlouho jsem byl v bezv\u011bdom\u00ed?"
    d["UnderCO_c520s100_0040_ch0200"] = "N-Nev\u00edm..."
    d["UnderCO_c520s100_0050_ch0200"] = "D-Docela dlouho."
    d["UnderCO_c520s100_0060_ch0200"] = "Ty skvrny..."
    d["UnderCO_c520s100_0070_ch0100"] = "Je to T-Virus."
    d["UnderCO_c520s100_0080_ch0100"] = "T\u0159et\u00ed st\u00e1dium infekce."
    d["UnderCO_c520s100_0090_ch0200"] = "K-Kdy\u017e jsi tak nemocn\u00fd,"
    d["UnderCO_c520s100_0100_ch0200"] = "pro\u010d jsi sem v\u016fbec p\u0159i\u0161el?"
    d["UnderCO_c520s100_0110_ch0100"] = "Tohle m\u00edsto..."
    d["UnderCO_c520s100_0120_ch0100"] = "Raccoon City je m\u00edsto, kde to pro m\u011b v\u0161echno za\u010dalo."
    d["UnderCO_c520s100_0130_ch0100"] = "Kdy\u017e se to v\u0161echno stalo, n-nemohl jsem\u2014"
    d["UnderCO_c520s100_0140_ch0100"] = "Nemohl jsem nic zm\u011bnit."
    d["UnderCO_c520s100_0150_ch0100"] = "Tak jsem tady. Te\u010f."
    d["UnderCO_c520s100_0160_ch0200"] = "Z-Zena nem\u016f\u017eeme zastavit."
    d["UnderCO_c520s100_0170_ch0100"] = "P\u0159\u00edkal n\u011bco o tom, \u017ee zn\u00e1\u0161 heslo."
    d["UnderCO_c520s100_0180_ch0100"] = "O \u010dem to mluvil?"
    d["UnderCO_c520s100_0190_ch0200"] = "N-Nev\u00edm!"
    d["UnderCO_c520s100_0200_ch0200"] = "Promi\u0148, j\u00e1..."
    d["UnderCO_c520s100_0210_ch0200"] = "Tady."
    d["UnderCO_c520s100_0220_ch0100"] = "Jdu zp\u00e1tky."
    d["UnderCO_c520s100_0230_ch0100"] = "Zni\u010d\u00edm Elpis."
    d["UnderCO_c520s100_0240_ch0200"] = "P-P\u016fjdu s tebou."
    d["UnderCO_c520s100_0250_ch0100"] = "Ne, nep\u016fjde\u0161."
    d["UnderCO_c520s100_0260_ch0200"] = "Nechci u\u017e \u017e\u00e1dn\u00e9 v\u00fd\u010ditky!"
    d["UnderCO_c520s100_0270_ch0200"] = "A\u0165 to stoj\u00ed cokoliv, po\u010d\u00edtej se mnou."
    d["UnderCO_c520s100_0280_ch0100"] = "Kdyby se mi n\u011bco stalo..."
    d["UnderCO_c520s100_0290_ch0100"] = "Slib mi..."
    d["UnderCO_c520s100_0295_ch0100"] = "\u017ee to ukon\u010d\u00ed\u0161."
    d["UnderCO_c520s100_0300_ch0200"] = "Slibuju."
    d["UnderCO_0300_0010_ch0100"] = "Poj\u010f."
    d["UnderCO_0500_0010_ch0200"] = "Pod\u00edvej, t\u00e1mhle jsou dve\u0159e."
    d["UnderCO_0500_0020_ch0100"] = "Jen\u017ee je blokuje je\u0159\u00e1b."
    d["UnderCO_c520s200_0000_ch0200"] = "<Sound Team ID>"
    d["UnderCO_c520s200_0000_ch0100"] = "<Sound Team ID>"
    d["UnderCO_c520s200_0010_ch0200"] = "M\u016f\u017eu se tam pod\u00edvat za n\u00e1s."
    d["UnderCO_c520s200_0020_ch0200"] = "Mysl\u00ed\u0161, \u017ee bys m\u011b mohl vyhodit nahoru?"
    d["UnderCO_c520s200_0030_ch0100"] = "To se asi brzy dozv\u00edme."
    d["UnderCO_c520s200_0040_ch0100"] = "Poj\u010f."
    d["UnderCO_c520s200_0050_ch0100"] = "D\u00e1vej tam na sebe pozor, jo?"
    d["UnderCO_c520s200_0060_ch0200"] = "Budu."
    d["UnderCO_0600_0010_ch0200"] = "Jakmile slezu dol\u016f...u\u017e se zp\u00e1tky nedostanu."
    return d

# This approach with unicode escapes is too painful. Let me just write
# the JSON files directly using a cleaner method.
print("Building translations...")
