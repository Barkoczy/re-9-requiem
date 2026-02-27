#!/usr/bin/env python3
"""Fix typographic quotes in the translation script."""
with open('/tmp/re9-translate/translate_all.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Czech/typographic quotes with escaped unicode sequences
content = content.replace('\u201e', '\\u201e')
content = content.replace('\u201c', '\\u201c')
content = content.replace('\u201d', '\\u201d')

with open('/tmp/re9-translate/translate_all.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done fixing quotes')
