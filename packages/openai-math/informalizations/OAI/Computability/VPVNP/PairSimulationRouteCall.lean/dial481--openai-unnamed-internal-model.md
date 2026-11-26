---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One native call checking a cursor routing field

The geometry block selects the two side bits and the payload test. A second
block adds the field offset to the corresponding resident buffer bases. The
field loop checks the unused outgoing bit and the selected payload test at
each bit position, accumulating any mismatch into the caller's mask.


### `Good`

 The bit tests belonging to one successor or sorting field. 

### `startOffset`

 The scheduler's running offset at entry to this field. 

### `Resident`

 Each of the four local half-wire buffers resides at its own base.
The bases and memory addresses are host words. 

### `geometryRegs`

 The first twelve slots carry the geometry inputs and outputs. 

### `outSlot`

 Register holding the base of the indicated outgoing buffer. 

### `inSlot`

 Register holding the base of the indicated incoming buffer. 

### `addressRegs`

 Connect the side flags, buffer bases and selected cursors to the address block. 

### `fieldRegs`

 Connect the selected cursors, width, mode and sticky mask to the field scanner. 

### `Scratch`

 All register slots written by at least one block of the call. 

### `Preserved`

 The register is outside the scratch slots of the three blocks. 

### `Linked`

 The geometry exit enters the address block, whose exit enters the field scan. 

### `Ready`

 Live cursor and scheduler inputs at the entry to a routing field. 

### `ticks`

 Clock for geometry, the five address-selection instructions, and the scan. 

### `Result`

 The final mask records the field tests and preserves earlier failures. 

### `run`

 Run geometry and address selection, then check the entire resident field.
The mask remains zero exactly when the initial mask was zero and every bit
test at this system accepts. 
