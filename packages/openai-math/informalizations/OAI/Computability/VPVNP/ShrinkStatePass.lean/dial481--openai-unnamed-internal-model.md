---
{
  "module": "OAI/Computability/VPVNP/ShrinkStatePass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStatePass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStatePass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A shrinking pass on a compressor state

Both numberings of each thick bundle are fixed before the local identities
are applied. The term choices then determine the layout and the widths of
the indexed output slots. The resulting state has the output degree and
unconsumed lane length required by the block schedule.


### `noncomputable local instance : DecidableEq X.Base`

 Classical equality test on base sites used in the dyadic shrinking pass. 

### `two_le_packingColors`

 The dyadic coloring has enough coordinates for two distinct endpoint colors. 

### `shrinkBaseOrder`

 Use the same finite base enumeration as the dyadic coloring and offset scans. 

### `shrinkStateIndex`

 Number surviving slots by the mixed-radix keys of the lane-zero IDs. 

### `shrinkNumber`

 Order the CD pieces by their lane-relative old arc identifiers. 

### `shrinkOrder`

 Concatenate old thick wires in the common binary coordinate order. 

### `ShrinkSelection`

 A choice of one admitted local term on each CD occurrence. 

### `shrinkNext`

 The next state determined by one entire list of motif selections. 

### `shrinkNext_energy`

 Equation (7.2) in the coordinates retained between compressor substeps. 

### `shrinkStatePass`

 The exact shrinking identity on a compressor state. Every term carries
its own subsequent state with the prescribed output degree and remaining lane. 
