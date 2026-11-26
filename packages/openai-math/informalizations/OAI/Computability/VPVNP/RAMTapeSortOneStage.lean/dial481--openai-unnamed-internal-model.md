---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortOneStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOneStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortOneStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executing one sorting stage of the transcript validator

The finite routine splits the incident field when the stride crosses sites,
visits every row, then reverses the accumulated output into the current block.
The entire operation uses the live unary phase and stride of the schedule.


### `program`

 Prepare the stage's incident streams, visit every row under its phase and stride, then
expose the selected next block in forward order. 

### `layer`

 A single callback for the schedule's nested phase and stride loops. 

### `runs`

 The validator returns the selected local block, the unconsumed tail of
the incident stream, and the comparator flags in reverse row order. 
