---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPrepareRowsAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareRowsAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareRowsAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses of greedy row preparation

Each row reads the chosen incidence's mate and then writes the operand
addresses in order. The addresses written into the row may name shifts or
labels. The preparer itself only accesses the two mate arrays and its own
consecutive destination cells.


### `rows`

 The complete initializer reads only at directed mate cells and writes
only in the half-open interval of the actual row words. 
