---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Control tables for the cursor routing checker

The machine first visits the successor classes in order. Then it visits
each sorting phase and its steps in triangular order, advancing the same
bit offset after each field. The program text is independent of all four
buffer lengths and the number of systems.


### `CallLabels`

 Labels of a copy of the fixed three-part field checker. 

### `CallLabels.geom`

 Geometry calculation. 

### `CallLabels.addr`

 Selection of the three addresses. 

### `CallLabels.field`

 The field-bit scan. 

### `Program`

 The outer cursor checker has three counted loops and two copies of a
field call, which return to the appropriate loop increment. 

### `Program.reg`

 Routing register bank. 

### `Program.pc`

 Initialization, transition, offset updates and final dispatch. 

### `Program.succ`

 Successor class counter. 

### `Program.phase`

 Sorting phase counter. 

### `Program.step`

 Sorting step counter. 

### `Program.sCall`

 The successor field call. 

### `Program.lCall`

 The sorting field call. 

### `Program.yes`

 All four input buffers pass the routing checks. 

### `Program.no`

 At least one routing check fails. 

### `Program.instruction`

 Seven scheduler instructions. Register 28 is the current sorting step
bound, and register 29 supplies the fixed sorting block width. 

### `Program.Linked`

 Every link from a loop into a field call and back is fixed once. 

### `RangeKeep`

 A one-dimensional field scan may write the index, the offset and the
field-call scratch registers. 

### `PhaseKeep`

 A sorting phase adds the outer index and step bound to the writable registers. 

### `Keep`

 The whole program additionally switches the field width between passes. 

### `narrowFrame`

 Restrict a register frame to a subset of its preserved registers. 

### `Inputs`

 Fixed inputs supplied by the leaf expansion. The original four buffers
occupy private words and may have arbitrary contents. 

### `layer`

 A sorting step with its phase and zero-based step counter. 
