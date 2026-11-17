# Scan preview and form import

Run `python demo.py`. The current recognizer compares complete grayscale crops
with a fixed font. The importer places each character into one cell of a complete
grid. `fixtures/cases.json` contains ordinary crops, a masked observation and
external glyph evidence for a form with an uncertain internal cell boundary.
The supplied font consists of authored 5×5 synthetic glyphs.
