---
{
  "module": "OAI/Computability/VPVNP/PairShrinkNodeClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkNodeClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkNodeClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Counts for a complete shrinking visit

All terms outside the selected map list are explicit native instruction
or probe counts. A resident map list contributes its test and increment
per item, its final exit test, and the traces of its actually executed items.


### `scan_cost`

 Counts for a map list that actually succeeded, parameterized by the
concrete resource bounds for each selected row. 

### `native_cost_reached`

 Instruction and probe counts for the child and hidden reads reached by the visit
and the resident map scan starting on their prepared scratch. 

### `native_cost`

 Combined length of the level search, stage selection, child handoff,
child directory, hidden handoff, hidden header and loop, and map reload
and header. The list of per-item map events includes its own loop control. 
