---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkGreedyHeaderValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkGreedyHeaderValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkGreedyHeaderValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The greedy workers' physical input header after a shrinking substep

The three header calls publish the selected input scalars, initialize the
next level and publish its array heads. The old incidence heads, table-zero
pointer and pitch lie outside those writes. All fields used by the shrinking
planner lie strictly below its first scratch address.


### `Header`

 The memory certificate can be transported through every native greedy
visit using only the write bound at the start of the scratch allocation. 

### `post_header`

 Read the actual old heads through the relabel/advance/publication call
sequence, using its published input fields and its three write intervals. 
