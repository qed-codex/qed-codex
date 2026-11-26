---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native mask geometry at a cursor position

The successor entry constructs its low-bit mask and tests the site against
the unique nonwrapping successor. The sorting entry constructs a one-bit
mask from phase and step. Both entries extract the outgoing and incoming
bits from that mask, including the last cursor on arrival at cursor zero.


### `outerIndex`

 Value of the outer counter at this field, either a successor class or a sorting phase. 

### `entry`

 Entry row for the system's geometry calculation. 

### `ticks`

 Number of native instructions executed along the selected entry path. 

### `mode`

 At cursor zero a failed successor test clamps the selected outgoing
field. Every other cursor compares the two selected fields. 

### `row`

 Rows 0–13 generate a successor mask and the inactive-source flag.
Rows 14–17 generate a sorting mask and clear that flag. Rows 18–29 select
the mode, form the cyclic predecessor, and read the two mask bits. 

### `instruction`

 The finite native geometry table with relocated register operands and continuations. 

### `Linked`

 Every row of the geometry table occurs in the enclosing machine. 

### `Preserved`

 Registers outside the three results and four scratch slots. 

### `Ready`

 Position, dimension and loop counters supplied by the routing scheduler. 

### `Result`

 The selected sides and mode at the continuation, together with the register and memory frame. 

### `native`

 The two fixed entry paths compute every field's side flags and test mode
from the live system counters and position words. 
