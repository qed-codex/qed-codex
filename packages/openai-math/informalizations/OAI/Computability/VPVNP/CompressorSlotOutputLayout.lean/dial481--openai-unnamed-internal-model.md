---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOutputLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOutputLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOutputLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The six shared columns of a shrinking output

The sorted slot pass already writes the base mate and displacement. Allocate
the base inverse, actual forward and inverse, and outgoing widths in the
following address ranges. Their lengths are the actual numbers of base or
lifted slots. The full six-column directory then supplies subsequent passes.


### `actualCount`

 Number of outgoing ports in the next graph across all packed sites and residual lanes. 

### `inverseBaseHead`

 First address after the base displacement table, reserved for the inverse base matching. 

### `outHead`

 Start of the outgoing actual mate column, immediately after the inverse base matching. 

### `inHead`

 Start of the incoming actual mate column, immediately after the outgoing actual mates. 

### `widthHead`

 Start of the outgoing actual width column, immediately after the incoming actual mates. 

### `finish`

 First free address following the last outgoing width in the shrinking output directory. 

### `inverseBank`

 Source and destination addresses for scattering the forward base matching into its inverse. 

### `actualBank`

 Public degree, lane count, matching, displacement, and destination parameters for lifting
the forward or inverse base matching to actual ports. 

### `widthBank`

 The radices, genuine range bound, and row, split-width, and output addresses used to gather
widths in actual outgoing-port order. 

### `directory`

 Assemble the six public column addresses for the next state's base mates, displacements,
actual mates, and widths. 

### `Stored`

 Natural-address readback of the six arrays in their canonical finite port orders. 

### `Stored.represents`

 The numeric arrays are precisely the common incidence directory expected
by the next cursor, shrink or refresh calculation. 
