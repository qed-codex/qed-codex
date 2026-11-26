---
{
  "module": "OAI/Computability/VPVNP/RAMTapeCeilLogCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCeilLogCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCeilLogCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of computing the ceiling binary logarithm on a unary tape

Each round pairs the remaining marks, keeps a mark for an unpaired last one,
outputs `B` marks, and transfers the shortened tally for the next round.


### `roundCost`

 Count the unary scan, pair emission, fixed output and return transfer. 

### `cost`

 The stopping tests take one instruction on an empty tally and two on a singleton. 

### `cost_le`

 For fixed output width the total instruction count is linear in the initial tally. 
