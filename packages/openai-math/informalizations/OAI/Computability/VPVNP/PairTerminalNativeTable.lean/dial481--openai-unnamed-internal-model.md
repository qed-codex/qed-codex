---
{
  "module": "OAI/Computability/VPVNP/PairTerminalNativeTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalNativeTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalNativeTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete fixed opcode table for a compressed pair's terminal phase

The same parameter numbering is used in every shrinking matrix and every
refresh matrix. The refresh tie and slice ordering comes from the actual
block planner. All five terminal workers share the eleven public operands of
the enclosing pair. Their finite instruction and register counts depend only
on the schedule, the fixed live constants and the label enumeration.


### `nativeSegments`

 The actual map, leaf, shared-wire, geometry and DFS segments on one
fixed register allocation. 

### `nativeTable`

 The input-independent terminal table in the paper's live pair machine. 

### `nativeTable_eq`

 Its instruction image is the actual five-stage program for each packed
level directory, with the concrete finite role handlers installed. 
