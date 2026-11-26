---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafScalarTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite scalar-startup template and its virtual-leaf clock 

### `PC`

 The instruction labels of the scalar startup table together with one additional return
label. 

### `rowPC`

 The numbered program counter of a labeled allocation, staging or fill instruction in the
scalar startup template. 

### `returnPC`

 The numbered return label reached after the final scalar port in the standalone startup
template. 

### `registers`

 Assign the scalar-loader registers consecutive indices in the standalone startup template. 

### `template`

 The code depends only on the static port set and assignment. Its inputs
are the caller's source words, the arena cursor and its runtime stride. 

### `cost`

 The total instruction count for allocating three rows per port, finishing allocation in two
steps, and staging and writing every requested field. 
