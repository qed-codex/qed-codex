---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotOperandFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOperandFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotOperandFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reads of the twenty-two shrinking slot planners

All level-dependent counts and column heads are computed arithmetically
from the seven inputs to the sorted-slot passes. The remaining reads come
from the chosen layout, the split-width head, and the six destination heads.
These are footprints of the planner operands in their entry memory.


### `Roots`

 All expressions from the surrounding block that can supply a slot planner. 

### `Stage.reads`

 Every expression in the active worker's chronological operand row reads
only the supplied region. 
