"""Summarize common word AND prefix searches using SQLite's own FTS tokenization."""
from collections import Counter
from functools import lru_cache
from itertools import groupby


@lru_cache(maxsize=65536)
def prefixes(term):
    return tuple(term[:n] for n in (3, 4, 6) if len(term) >= n and term[:n].isascii() and term[:n].isalnum())


def populate_search_counts(db):
    db.execute("CREATE VIRTUAL TABLE temp.words USING fts5vocab(main, 'names', 'row')")
    db.execute("CREATE VIRTUAL TABLE temp.tokens USING fts5vocab(main, 'names', 'instance')")
    frequent = {word: Counter() for (word,) in db.execute(
        "SELECT term FROM temp.words ORDER BY doc DESC, term LIMIT 8")}
    rows = db.execute("SELECT doc,term FROM temp.tokens ORDER BY doc,term")
    for _, group in groupby(rows, key=lambda r: r[0]):
        words = [word for _, word in group]
        broad = frequent.keys() & words
        if broad:
            # Several words of one document may share a prefix. Count the document once.
            starts = {prefix for word in words for prefix in prefixes(word)}
            for word in broad:
                frequent[word].update(starts)
    db.executemany("INSERT INTO search_counts VALUES(?,?,?)", (
        (word, prefix, count) for word in sorted(frequent)
        for prefix, count in sorted(frequent[word].items()) if count >= 128))
    db.execute("DROP TABLE temp.tokens")
    db.execute("DROP TABLE temp.words")
