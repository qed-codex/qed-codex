---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderWidthCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderWidthCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderWidthCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native word code for the five first-half cut widths

Each output word uses two reads from the index-scan scratch and one
write. Word division computes the two indicator bits: `1 / count` for
a power of two and `high / high` for a group other than the first.
The RAM uses natural division with zero quotient on a zero divisor.


### `Parameters`

 Public words containing the two geometric parameters and three addresses. 

### `Parameters.height`

 The public operand index supplying the cut-schedule height. 

### `Parameters.delta`

 The public operand index supplying the basic block width that scales the computed cut
  length. 

### `Parameters.highestAddress`

 The public operand index for the cell containing the highest set position in the group
  index. 

### `Parameters.populationAddress`

 The public operand index for the group index's population-count cell. 

### `Parameters.outputAddress`

 The public operand index for the destination of the computed cut width. 

### `setup`

 Load the two small summary words and compute the two unshifted block
counts. The live group index itself is distributed over header bits. 

### `select`

 Place the appropriate block count in register 13. 

### `commit`

 Multiply the selected block count by the basic block width and write the resulting cut
length. 

### `block`

 Load the scanned index summary, compute the requested live or primed block count, and
publish its width. 

### `table`

 The physical instruction and public-field table is independent of word width. 

### `events`

 Exact external probes and arithmetic ticks, including the final write. 

### `unconditional_exec`

 On groups outside the first half, unused primed lengths are still
computed by the same straight-line table. Its only write is its output. 

### `needed_exec`

 Execution from arbitrary registers computes the true paper width. The
height, block size, highest set bit and population count are read at runtime.
The bound on the output word follows from the largest possible cut length. 

### `block_exec`

 First-half groups may request any of the five lengths. 
