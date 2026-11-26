---
{
  "module": "OAI/Computability/VPVNP/PermanentRingWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentRingWeight.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentRingWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weight of a consistent variable ring

Only position `m` of each ring carries the variable weight. Multiplying the
row weights for a consistent choice therefore contributes one factor for
each variable assigned true.


### `prod_ringWeight`

 For consistent ring orientations the product of all row weights is the
weight of the corresponding Boolean assignment. 
