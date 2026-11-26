---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafPortTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPortTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPortTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite instruction table allocating and filling every scalar leaf port 

### `Label`

 Rows for allocating a port, finishing allocation, staging its scalar field and filling its
private stack. 

### `followers`

 Construct the successor-port lookup for a fixed traversal list, using the head of the
remaining suffix at each port. 

### `Follows`

 The successor lookup agrees with the traversal list at every port, including the final
port's empty successor. 

### `stagePC`

 Map a staging index to that port's staging row, with the final index pointing to the first
scalar fill instruction. 

### `instruction`

 The allocation, staging or fill instruction for one labeled row of the port list, including
its continuation to the following port. 

### `startup`

 Native scalar startup from the fixed rows. Its label set, register wiring,
and instructions are independent of the input values and widths. 
