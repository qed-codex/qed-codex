---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSortFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSortFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSortFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native triangular scan of the sorting fields at cursor zero

Phase and step count upwards. Each step reads one outgoing and one incoming
block from the common arc offset. Both selections depend on the cross-site
bit, equal to phase minus step. The incoming selection tests that bit against
the last cursor. Every row below is independent of the number of phases.


### `Stage`

 Control locations of the triangular sorting-field traversal and its copy loops. 

### `port`

 Select an outgoing or incoming half-wire by the endpoint bit. 

### `subRegs`

 Place the field loader's eleven registers inside the sorting traversal. 

### `instruction`

 The shared mover uses registers 0–10. The remaining registers hold D,
D−1, phase, step, stride bit and zero. 

### `Linked`

 The host table contains the sorting traversal's physical instructions. 

### `arcStart`

 Start of this sorting layer's field in one half-wire payload. 

### `side`

 Endpoint bit chosen for the outgoing or incoming field of a sorting layer. 

### `field`

 Bits of the selected resident sorting field. 

### `block`

 Concatenate a layer's outgoing field with its incoming field. 

### `index`

 Index of a field-loader register in the sorting register file. 

### `Fixed`

 Constant operands for a complete sorting-layer traversal. 

### `changed`

 Register operands that can change in a sorting-field scan. 

### `Frame`

 Registers preserved while one sorting-field step executes. 

### `layer_run`

 Both physical fields of one layer, before the address and loop counters advance. 
