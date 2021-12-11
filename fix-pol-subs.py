import sys
from pathlib import Path

TRANSLATION_MAP = {
  "Ä…": "ą",
  "Ĺą": "Ź",
  "Ĺ‚": "ł",
  "Ĺ›": "ś",
  "Ăł": "ó",
  "ĹĽ": "ż",
  "Ä‡": "ć",
  "Ä™": "ę",
  "Ĺ„": "ń",
  "Ĺ�": "Ł",
  "Ĺ»": "Ż",
  "Ĺş": "ź",
  "Ĺš": "Ś",
  "Ä�": "Ę",
  "Ă“": "Ó",
  "Ä„": "Ą",
  "â€ž": "„",
  "â€ť": "”"
}

input_file = sys.argv[1]

if not input_file:
    raise FileNotFoundError('Input file not found')

input_abspath = Path.absolute(Path(input_file))
backup_abspath = Path(str(input_abspath) + '.old')

print(f"reading: {input_abspath}")
with open(input_abspath, 'r', encoding='utf-8') as f:
    txt = f.read()

print(f"saving backup: {backup_abspath}")
with open(backup_abspath, 'w', encoding='utf-8') as bkp:
    bkp.write(txt)

for k,v in TRANSLATION_MAP.items():
    print(f"fixing {k} -> {v}")
    txt = txt.replace(k, v)

print(f"saving fixed file: {input_abspath}")
with open(input_abspath, 'w', encoding='utf-8') as out:
    out.write(txt)

print('done!')