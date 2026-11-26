---
{
  "module": "OAI/Computability/VPVNP/CompressorLevelCounts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLevelCounts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLevelCounts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sizes of the actual arrays scanned at a selected compressor level

Shrinking indexes motifs by old arcs and refresh indexes motifs by port blocks.
The bounds here follow the chosen term through its original state pass. They
control the base, site, arc, motif and resulting slot scans uniformly along
the execution, as well as the largest input field of every intermediate level.


### `motifCount`

 Number of physically distinct demand vectors for this pass. 

### `slotDegree`

 All degree exponents occur in a single fixed finite schedule. 

### `oldSlots`

 Number of input incidence slots, counting each incident port at every input position. 

### `outputSites`

 Number of positions in the successor state produced by the selected term. 

### `outputSlots`

 Number of successor incidence slots, obtained by multiplying output positions by output
degree. 

### `executeLevels_length`

 The level directory needs one header for each elementary substep on this branch. 

### `executeLevels_limits`

 Every site and field in every intermediate input stays within the branch envelope. 
