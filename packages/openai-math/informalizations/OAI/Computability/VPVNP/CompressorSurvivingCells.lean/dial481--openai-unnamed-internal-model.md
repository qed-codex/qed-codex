---
{
  "module": "OAI/Computability/VPVNP/CompressorSurvivingCells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingCells.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingCells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cells written for each subdivision of a surviving wire

Every piece writes its own width, offset, interval frame and references. The
source width and source directory header are shared across all pieces. These
repeated writes agree, even when the source width is zero.


### `address`

 The thirteen write destinations for piece `j` in a surviving row. 

### `value`

 The balanced width, prefix, and adjacency data written by piece `j`. 

### `same_field`

 Disjoint header columns and endpoint arrays determine the field number
uniquely. The three interleaved frame columns differ modulo three. 

### `same_value`

 Two writes in the same row can only collide within the same column.
For a piece-specific column the address then determines the piece, and for a
shared header column the value depends only on the row. 
