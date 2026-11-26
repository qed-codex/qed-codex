---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The full native incident decoder for a cursor-zero leaf

The two chain fields are loaded first. Two arithmetic rows switch the
source offset and field width to the sorting layout, followed by the
triangular layer scan. All three subgraphs share a descending destination
cursor, so the resulting stack has the logical order of the virtual RAM
validator even when the supplied halves disagree.


### `Stage`

 Successor-field stages, setup instructions and sorting-field stages. 

### `successorRegs`

 Embed the successor loader in the thirty-register incident machine. 

### `sortMap`

 Sorting counters reuse the three successor-class temporaries. 

### `sortRegs`

 Embed the sorting loader in the thirty-register incident machine. 

### `instruction`

 The row that loads the indicated successor or sorting field. 

### `Linked`

 The incident core's relocatable instruction rows occur in the host table. 

### `changed`

 Registers that the incident core may write. 

### `Frame`

 Equality of every register outside the core's write footprint. 

### `ticks`

 Instruction count for the successor and sorting field loads at this site. 

### `Result`

 The materialized incident stack and exact physical continuation of the core. 
