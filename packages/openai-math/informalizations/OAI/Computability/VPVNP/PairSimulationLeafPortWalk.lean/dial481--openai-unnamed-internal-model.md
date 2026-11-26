---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafPortWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPortWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPortWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling the validator's fixed scalar-port list in a single private call

The scalar pass visits each port exactly once. The caller can reuse its
private arena at the next leaf. The incident port remains available for
the separate copy from the four half-wire buffers.


### `scalarBank`

 The completed scalar stack contents of each port, obtained by encoding its field for the
given site and operands. 

### `pending`

 The intermediate scalar bank with the unvisited ports empty and the visited ports holding
their completed fields. 

### `ticks`

 The instruction count to stage one port's scalar field and run the six-row fill loop for
its bits. 

### `StageLabels`

 Program labels for each port's field-specific staging sequence, including the index used
for its continuation. 

### `first`

 The first staging label of the next port to fill, or the exit label once the traversal list
is empty. 

### `ScalarRows`

 The host machine implements each port's field-specific staging and fill rows, with
continuations that visit the list in order. 

### `sourceWord`

 Scalar input registers furnished by the enclosing private call. 

### `scalar_startup`

 The deterministic pointer and scalar tables are consecutive subprograms
of the same native RAM. No pre-initialized stack bank is required. 
