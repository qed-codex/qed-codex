---
{
  "module": "OAI/Computability/VPVNP/CompressorChoiceGrid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceGrid.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoiceGrid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native lookup of the rounded demand-grid point

For a fixed rational grid, the public data list the address offsets and the
two cleared coefficients of every comparison. The instruction table reads the
demand widths, tests each row in order and returns the first covering index.
The table length is the sentinel for a failed search.


### `coefficients`

 Fixed public words, ordered by grid row, demand coordinate and field. 

### `OperandsFit`

 Word-fit conditions on the final products, allowing modular intermediate
products because the register arithmetic is a ring. 

### `operandConstant`

 This grid-dependent coefficient bounds all comparison operands after
multiplication by the squared input-width scale. 

### `compareCoordinate`

 One coordinate comparison. The sign of a fixed rational is resolved at
table generation. A negative coordinate clears the row's validity bit. 

### `grid`

 Ordered first-cover search starting with the energy in register zero.
The first covering index, or the length sentinel, is returned in register one. 

### `grid_length`

 The text size depends only on the dimensions of the fixed grid. 

### `firstRow`

 Row number returned by the grid instruction table. 

### `grid_exec`

 Exact row-selection semantics and worst-case work for an arbitrary finite
ordered table, including empty tables and grids with negative coordinates. 
