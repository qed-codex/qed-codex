---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafImagePreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImagePreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImagePreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Running the actual finite cursor-leaf image on a stored DFS packet 

### `storage`

 The auxiliary stack layout in the leaf's private arena, assigning capacity n^40 to each
port in the fixed port order. 

### `trace`

 The whole deterministic prefix, including the seven operand-transfer
instructions on a cursor-zero visit. 

### `loaded`

 Decode the node and its private buffers into a leaf handler input, including the prefix
trace and the initialized auxiliary scratch for a cursor-zero visit. 

### `cacheWords`

 The static words cached for the leaf initializer, giving the cursor dimension, word width,
bucket size, auxiliary fuel, and public operands. 

### `Domain`

 Data actually stored by the parent node and the final-site cache writer.
The buffers need no compatibility condition across distinct wires. 

### `fields`

 Read the address decoder's public operands from the linked machine through the leaf's port
assignment. 

### `preparation`

 Every row of the concrete finite leaf image executes the deterministic
prefix required by the DFS hook, including the malformed-route exit. 
