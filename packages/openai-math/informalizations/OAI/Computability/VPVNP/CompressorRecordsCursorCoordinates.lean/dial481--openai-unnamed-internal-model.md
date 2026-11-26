---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorCoordinates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numerical coordinates for the initial compressor graph

The RAM visits outgoing slots in cursor, base-address, lane and slot order.
Physical address bits have increasing significance, whereas the compressor
numbers each binary block with its first coordinate most significant. Reversing
the coordinates within each designated block identifies the cursor's one-bit
flip with the corresponding power of two in its RAM word.


### `cursorCoordinateLabels`

 Designate a low base-address block and a high lane block. Each compressor
block is ordered most significant bit first. 

### `cursorBaseIndex`

 Cursor-major base numbering. 

### `cursorActualIndex`

 Base-major numbering of positions, with consecutive lanes. 

### `cursorBaseSlotNumber`

 Source or destination slot in the base records. 

### `cursorActualSlotNumber`

 Source or destination slot in the actual-wire records. 

### `cursorState_baseIndex_val`

 The record numbering agrees with the indexed vertex order used by
the greedy scans on the initial compressor state. 

### `cursorNextBase`

 Numeric destination vertex of a base slot. 

### `cursorLaneMask`

 Numeric lane displacement of the slot. 

### `cursorBaseTargetNumber`

 Each outgoing base slot writes its own incoming slot number at the
rotated cursor and the updated base address. 

### `cursorDisplacementNumber`

 The stored displacement is the translated physical bit of the lane block. 

### `cursorActualTargetNumber`

 Flattening the actual graph's target into a record address updates
the base and lane separately and preserves the slot. 

### `cursorSlotWidth`

 Stay and flip wires reserve all fields. Each further slot is a zero-width copy. 
