---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisDataLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisDataLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisDataLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical local-table lookup and decoding

This fixed command selects a color record from the current type's actual
batch and parses its three fields.  The batch and unary color index remain
intact.  The result is dimension, split, coordinate-major table, and
complement dimension; no matrix is constructed from a semantic lookup.

