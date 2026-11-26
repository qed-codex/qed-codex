---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Canonical prime-field words for the local matrix checker. 

### `word`

 The same fixed-bit encoding as `encodeBase` with exponent one, written
directly over `ZMod p` to avoid casts in the basis-checker interface. 

### `word_unique`

 A canonical machine output of the expected width is exactly the
corresponding field word, not merely a congruent numeric representative. 
