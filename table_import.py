"""Grid import for forms whose lines and single-cell characters are complete."""


def import_table(rows, cols, glyphs):
    cells = {(r, c): [] for r in range(rows) for c in range(cols)}
    for glyph in glyphs:
        x0, y0, x1, y1 = glyph['box']
        if not (x0 < x1 and y0 < y1):
            raise ValueError('empty box')
        r, c = int((y0+y1)/2), int((x0+x1)/2)
        if (r, c) not in cells:
            raise ValueError('outside grid')
        char = max(glyph['log_probabilities'], key=glyph['log_probabilities'].get)
        cells[r, c].append((x0, y0, glyph['id'], char))
    return [{'rect': [r, c, r+1, c+1],
             'glyph_ids': [g[2] for g in sorted(items)],
             'text': ''.join(g[3] for g in sorted(items))}
            for (r, c), items in cells.items()]
