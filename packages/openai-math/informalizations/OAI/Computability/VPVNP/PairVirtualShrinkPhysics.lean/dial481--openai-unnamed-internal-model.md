---
{
  "module": "OAI/Computability/VPVNP/PairVirtualShrinkPhysics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualShrinkPhysics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualShrinkPhysics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Addresses and public tags for shrinking in the linked vertex memory

All site readers at one selected vertex see the same role image. Its tag
offset is the selected row count plus the total final-wire width. The
private buffers, histogram and node array use the corresponding packed
terminal allocation, including after previous vertices have updated their
counter words.


### `Physics`

 The selected shrinking rows' budget, their published role words in linked memory,
and the address bounds for the role table, vertex header, frames, histogram and nodes. 
