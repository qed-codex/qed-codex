"""Attach stable anchors to headings emitted by the Lean documentation importer."""
from collections import Counter
from hashlib import sha256
from html import unescape
import re


def index_headings(body, fragment, entry):
    # The importer writes a standalone level-three code heading for each declaration.
    names = iter(re.findall(r"^### `([^`\n]+)`$", body, re.M))
    pending = next(names, None)
    occurrences = Counter()
    indexed = []

    def add_anchor(match):
        nonlocal pending
        name = unescape(match[1])
        if name != pending:
            return match[0]
        occurrences[name] += 1
        digest = sha256((entry + "\0" + name).encode()).hexdigest()[:24]
        anchor = "note-" + digest
        if occurrences[name] > 1:
            anchor += "-" + str(occurrences[name])
        indexed.append((name, name.lower(), anchor))
        pending = next(names, None)
        return match[0].replace("<h3>", f'<h3 id="{anchor}">', 1)

    fragment = re.sub(r"<h3><code>([^<>]+)</code></h3>", add_anchor, fragment)
    if pending is not None:
        raise ValueError(f"Missing rendered declaration-note heading {pending!r} in {entry}")
    return fragment, indexed
