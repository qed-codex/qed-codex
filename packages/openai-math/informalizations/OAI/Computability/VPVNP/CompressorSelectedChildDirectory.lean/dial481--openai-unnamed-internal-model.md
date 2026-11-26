---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedChildDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedChildDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedChildDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The seven child-scan operands at a selected level

The child decoder reads its old-level directory in one contiguous block
at scalar 14. The following six scalar words come from the pass metadata
packet. Its first word is the carried DFS base, supplied at traversal by
the chronological directory history.


### `Stored`

 All seven words at the actual header pointer. The first word may be
given as any natural representative of the stored DFS row base. 

### `Stored.keep`

 Term, map, and later live scheduler writes preserve the child operands
when they preserve these seven actual cells. 

### `Stored.of_shrink`

 The actual shrinking metadata writer publishes the old child directory. 

### `Stored.of_shrink_tail`

 The shrinking term and data publishers follow the metadata writer in
the same pass and preserve all seven child-scan operands. 

### `Stored.of_refresh`

 The selected refresh metadata writer publishes the same child operand
bank for its singleton placement. 
