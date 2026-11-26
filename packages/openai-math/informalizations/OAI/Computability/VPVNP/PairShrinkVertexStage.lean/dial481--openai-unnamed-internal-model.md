---
{
  "module": "OAI/Computability/VPVNP/PairShrinkVertexStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVertexStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkVertexStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Child, absorbed-field, and map code in one shrinking stage

The old level determines the child degree and the fixed capacity of its absorbed-field
rows. After loading the hidden operands, the stage saves the actual hidden base in
locator register eight, for the subsequent map's supply-half reads.


### `prepare`

 Load the four hidden-field operands and cache the private field base for the map. 

### `withHidden`

 Place the hidden-field preparation in front of the supplied located body and lift its
locator into the enlarged private register bank. 

### `stage`

 The selected stage reaches its map after scanning the child list and the hidden rows. 

### `image`

 All stage constants are chosen before the live traversal. The modulo selector chooses
the appropriate body for each occurrence of a shrinking level in the repeated schedule. 
