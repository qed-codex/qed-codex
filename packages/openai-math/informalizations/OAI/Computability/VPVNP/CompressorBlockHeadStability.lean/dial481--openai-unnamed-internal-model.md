---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockHeadStability.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeadStability.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeadStability.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory read by the published term and DFS heads

The address formulas use four scalar words of the old level, its table
heads and the block pitch. The selected shrinking layout needs one more
read from the score table. Each of these cells is outside the fields
published at offsets 36 through 53.


### `Inputs`

 The only old-header reads in the compiled expressions. 

### `pitch_before`

 A block pointer places its pitch cell before every graph header. 

### `layoutCell_after`

 The selected score bit lies after the publication window whenever the
term region starts beyond the header and the final score offset fits. 

### `shrinkTerms`

 RHS expressions at offsets 36 through 39 on a shrinking substep. 

### `refreshTerms`

 RHS expressions at offsets 36 through 39 on the degree refresh. 

### `shrink_layoutCell_stable`

 The address of the selected score bit survives all head publications. 
