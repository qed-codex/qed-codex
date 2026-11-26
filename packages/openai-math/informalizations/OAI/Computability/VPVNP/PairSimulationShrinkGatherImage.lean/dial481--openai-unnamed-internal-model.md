---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkGatherImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shrinking map image with both physical layout gathers

The item reader selects its matrix by the recorded grid and party. At that
address a further header read chooses one of two layouts. Its gather copies
the appropriate old-child and surviving fields before entering the writer.
Only completion of the writer and matrix advances the resident row cursor.


### `GatherAddress`

 Instruction labels for the resident map image, each five-row layout branch, and the gathers. 

### `GatherRegister`

 The role's shared registers, handler and gather banks, and layout selection register. 

### `corePC`

 Placement of the resident map image within the full instruction table. 

### `layoutPC`

 Address of row `l` in the layout branch for grid point `z` and party `j`. 

### `gatherPC`

 Placement of the field gather instructions within the full table. 

### `writer`

 Descriptor writer entry reached after gathering operands for grid point `z` and party `j`. 

### `gatherCases`

 Dispatches a resident item's grid and party to the first row of its layout branch. 

### `gatherText`

 Original reader, loop and matrix rows retain their jumps. The dispatch
targets now enter the actual layout branch and field gather for each matrix. 

### `GatherLinked`

 Each constituent's link inside this single installed word-RAM table. 

### `gatherLocations`

 Numbers the instruction labels of the map image with both gathers. 

### `gatherRegisters`

 Numbers the registers used by the map image with both gathers. 

### `gatherShared`

 Embeds the role's shared registers into the combined segment's numbered bank. 

### `gatherMatrix`

 Embeds the map handlers' private registers into the combined segment's numbered bank. 

### `gatherLocal`

 Embeds the field gathers' private registers into the combined segment's numbered bank. 

### `layoutTemp`

 Number of the scratch register that computes the layout field's address and reads its bit. 

### `segmentWithGather`

 The final-vertex instruction segment for the shrinking map list, including
the materialization of every physical operand field in its selected layout. 
