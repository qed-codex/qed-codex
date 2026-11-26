---
{
  "module": "OAI/Computability/VPVNP/PairSimulationWorkspaceSelectorPost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationWorkspaceSelectorPost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationWorkspaceSelectorPost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The selected term packet at its physical workspace boundary

The script's selector occurrence determines the native worker input and
the private clock. Its workspace interval consumes the term's worker tapes.
A source packet with those tapes therefore describes the memory and cost
of that particular branch.


### `SelectorSite`

 Inputs and clock bounds at the actual calendar occurrence of the native term selector. 

### `SelectorSite.I`

 Native worker input for the term selector at this occurrence in the scheduled block. 

### `SelectorSite.j`

 Index of this term-selector occurrence in the block planner's script. 

### `SelectorSite.start`

 Certificate that the selected calendar occurrence starts this worker on its intended row,
  with the recorded table, fuel, bounds, and input memory. 

### `interval`

 Execute the installed selector from calendar state zero at its two clocks. 

### `interval_bits`

 A physical branch consumes the entering control tapes, one worker tape per motif,
and the empty return tape. 

### `interval_post`

 Identify the memory and private-clock work of this physical branch with its source packet. 
