---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkKernelSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkKernelSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkKernelSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical slice records of the six-party shrinking kernel

AB reads use the two bundle numberings at both endpoints. Surviving wires
use the selected payload-plus-selector width and the fixed subdivision count
of their role edge. The live frame stores the source offset, target offset
and length used by the local kernel.


### `thickWidths`

 The old array uses the rank among thick wires, the new array the rank
among CD motifs assigned to this bundle. 

### `abWidths`

 AB piece widths of one bundle listed in its motif numbering, the order used to compute the
target offsets of the thick-wire slices. 

### `ab_build`

 Consume both sorted width rows of a real packed bundle. 

### `ab_build_from_total`

 From only a sorted thick row and its computed total, construct the AB
pieces and both incidence directories, preserving the exact local cost. 

### `ab_sliceAt`

 The frame selected by the rank pair is the typed AB copy slice. 

### `ab_stored_bits`

 The physical offset and length words implement the AB demand-bit bijection.
This characterizes both local A and local B reads, even when a field is empty. 

### `surviving_sliceAt`

 A singleton supply word intersects each subdivision in that entire
subdivision. Its local source offset is the sum of preceding widths. 

### `surviving_frame`

 The target width, copied length and offsets left by the descriptor builder
are the word sections consumed by the source and target role maps. 

### `supplyRoles`

 The fixed order of the two groups of four supply roles, as in the term reader. 

### `survivingRowBase`

 Rectangular width rows indexed by absolute CD arc, role type and
subdivision. The larger common stride admits direct addressing for every role. 

### `fields_record`

 The whole term scan supplies all fields needed to reconstruct its image in
one row; earlier input memories and the saved headers need not be retained. 

### `surviving_build`

 A row read from the selected six-party term is written at the physical
address decoded by the new-slot scan. Both lists of slice references and the
widths survive the descriptor pass. 
