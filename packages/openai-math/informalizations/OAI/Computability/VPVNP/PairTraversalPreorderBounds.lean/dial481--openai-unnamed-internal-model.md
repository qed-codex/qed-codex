---
{
  "module": "OAI/Computability/VPVNP/PairTraversalPreorderBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalPreorderBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalPreorderBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical child-list bounds for every selected DFS visit

Each node in the final preorder originates in a row of its own compression
level. Reading that row gives its actual child pointer and length. Both
header reads and the entire child list fit in the allocated descriptor arena.


### `selected_preorder_row_bounds`

 The two scalar reads and every child-word read in each selected
placement tree lie below the given exclusive bound. 

### `selected_preorder_word_bounds`

 Word-encoded visits in the DFS event log recover the same bounds. 
