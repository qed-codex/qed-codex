---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSurvivingFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying one resident surviving interval back into its supply operand

The descriptor bank contains one source field and one target per subdivision.
The reverse copy reads the subdivision at offset zero and deposits it at the
sum of the preceding subdivision widths in the unsplit operand.


### `start`

 Bit offset of a subdivision in its unsplit word. 

### `head`

 Physical location of the first of the frame's three public cells. 

### `execute_piece`

 The actual reverse header and private copy loop read this subdivision
from its native slot and write it at its designated unsplit offset. 
