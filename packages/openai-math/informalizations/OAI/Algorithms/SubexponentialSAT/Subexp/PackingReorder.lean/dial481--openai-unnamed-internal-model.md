---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingReorder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingReorder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingReorder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Represented reordering of packed coordinates

The input table contains block-major scalar records followed by the residual
coordinate records. A concrete `idxOf` plan reorders this table into the original
vertex order. The value proof connects the represented records with the actual
computable packing split; the fixed gathering program executes the read plan.


### `packedVertices`

 Coordinates in the same block-major order as the copied local tables. 

### `storageVertices`

 Actual input-table coordinate order: complete blocks, then leftovers. 

### `readPlan`

 Explicit index plan; it is data, not part of the finite program control. 

### `assembledRecord`

 A vertex obtains its record from its computed block position or its
residual value. The same executable lookup is used to construct the packing. 

### `records`

 The represented table before reordering. 

### `gatherRows`

 Functional specification of the fixed gathering program. 

### `gathered_records`

 Exact represented output in original vertex order. 

### `assembledRecord_eq_encode_assemble`

 The lookup-based represented value equals the proved coordinate assembly. 

### `gathered_eq_encode_assemble`

 End-to-end semantic refinement of represented reordering to the actual
linear reconstruction from blocks and residual coordinates. 
