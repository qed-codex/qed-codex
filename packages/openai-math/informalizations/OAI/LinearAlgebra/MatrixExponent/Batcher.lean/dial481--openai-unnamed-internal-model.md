---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Batcher.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Batcher.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Batcher.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trivalent realization of Batcher's sorting network

Splitting applies one layer of comparators to corresponding records.
Merging adds at most one such layer per level. Sorting merges at every level.
The cost includes identities on single records. Reversals and the
permutations between layers only relabel ports.

