import json
import os

base_out = "/tmp/re9-translate/translations/natives/stm/message/dialog"
os.makedirs(base_out, exist_ok=True)

# Build translations as JSON strings to avoid Python string escaping issues
# We use triple-quoted raw JSON approach

underco_json = r'''
{
  "UnderCO_c520s100_0000_ch0200": "<Sound Team ID>",
  "UnderCO_c520s100_0000_ch0100": "<Sound Team ID>",
  "UnderCO_c520s100_0020_ch0200": "Leone. Jsi v po\u0159\u00e1dku?",
  "UnderCO_c520s100_0030_ch0100": "Jak dlouho jsem byl v bezv\u011bdom\u00ed?",
  "UnderCO_c520s100_0040_ch0200": "N-Nev\u00edm...",
  "UnderCO_c520s100_0050_ch0200": "D-Docela dlouho.",
  "UnderCO_c520s100_0060_ch0200": "Ty skvrny...",
  "UnderCO_c520s100_0070_ch0100": "Je to T-Virus.",
  "UnderCO_c520s100_0080_ch0100": "T\u0159et\u00ed st\u00e1dium infekce.",
  "UnderCO_c520s100_0090_ch0200": "K-Kdy\u017e jsi tak nemocn\u00fd,"
}
'''

# OK this approach is also painful. Let me build it programmatically instead.
