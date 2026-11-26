---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical AB/CD demand inputs of a shrinking pass

The balanced AB pieces and the original CD widths are stored in distinct
rectangles. The paired gather visits their common bundle and rank. Its
two output cells form the exact input to the six-party term reader.


### `operands`

 The two rectangle heads and strides are the ones used by the prefix and
balanced-piece passes. The first word is the common number of CD ranks. 

### `Pairs`

 The dense scan order is the CD ordinal used at both AB endpoints.
Cell zero holds the balanced AB width and cell one the original CD width. 

### `pairInputs`

 Read a dense array of pairs using the fixed two-coordinate order of the block. 

### `motifCount`

 Number of CD motifs in the input state's packing data. 

### `demand`

 The two shrinking demand widths for the motif at a given dense physical ordinal. 

### `statePairs`

 The memory readback that identifies dense demand pairs with their actual motifs and packing
widths in this state. 

### `termRows`

 Term records have two headers and eight supply coordinates. A larger
stride leaves the padding available to the surrounding record directory. 
