---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSortWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSortWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSortWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the complete sorting-field traversal of a virtual RAM leaf

The native scan visits the two fields of each layer in triangular order.
Its private-memory result puts the concatenation of those fields into the
descending part of the incident stack, preserving the resident half buffers.


### `At`

 The physical control and counters match a sorting-layer ordinal, or have reached the return. 

### `advanceTicks`

 Number of instructions to advance the triangular pair of counters. 

### `advance_run`

 Advance from the end of a field pair to the next ordinal or the exit.
The two cases of a triangular row boundary are handled by genuine comparisons. 

### `stream`

 Logical stream of a consecutive interval of layer ordinals. 

### `streamTicks`

 Total number of native instructions for the indicated consecutive sorting layers. 

### `sort_run`

 The full finite-control triangular scan on four resident half buffers. 
