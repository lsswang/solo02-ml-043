import json
from pathlib import Path
from recognizer import recognize
from table_import import import_table

case = json.loads((Path(__file__).parent/'fixtures/cases.json').read_text())
glyphs = []
for entry in case['ordinary']['glyphs']:
    out = recognize(entry['image'], case['templates'])
    glyphs.append({'id': entry['id'], 'box': entry['box'], **out})
print(json.dumps({'recognition': glyphs, 'cells': import_table(1, 2, glyphs)}, indent=2))
