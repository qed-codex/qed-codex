---
{
  "module": "OAI/Computability/VPVNP/SlotSeparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotSeparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotSeparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Separation of the three bases in each shrinking motif

Appendix C of *VP and VNP differ over every field* assigns one base and
tag to each packed position. Both layouts keep the three roles of a motif
at distinct such pairs. The binary tag group makes an arc displacement
the same in both directions.


### `packedBase`

 The base after packing consists of the old base and the packed tag. 

### `tagShift`

 The tag component of the old arc displacement. 

### `tag_ne_placed`

 Excluding the unary and binary shifts keeps either bundle tag distinct
from the placed tag of the other endpoint, for each choice of layout. 

### `distinct_roleBases`

 The packed bases of the three roles are pairwise distinct in every
motif, simultaneously for the source and target layouts. 
