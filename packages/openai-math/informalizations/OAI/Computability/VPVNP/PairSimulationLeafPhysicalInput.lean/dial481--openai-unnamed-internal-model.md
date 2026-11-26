---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafPhysicalInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPhysicalInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPhysicalInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a cursor leaf from the physical DFS arguments

The host decodes its current row pointer with the public row stride and
radices. Its private argument arena contains four consecutive bit vectors.
On a stored cursor packet these operations recover the typed position and
all four half-wires, including independently assigned incoming wires.


### `physicalPosition`

 Decode the descriptor row using the same operands as the native address reader. 

### `portBase`

 The four bases passed to the incident-field mover, in native slot order. 

### `physicalBuffers`

 Read the single private word occupied by each argument bit. 

### `physicalInput`

 The deterministic prefix supplies its trace and resulting scratch.
The input position and buffer bits are projections of its actual operands. 

### `cursorPacket`

 The pending half-wire packet for this site, with its numerical row address. 

### `physicalStored`

 The resident packet satisfies the exact memory precondition of the native
incident-field loader on each of its four ports. 

### `physicalBuffers_eq`

 Reading the private four-port bank yields the semantic half-wire bits. 

### `physicalInput_correct`

 The physical handler input recovers the semantic cursor site and its
independent buffers on each fitted, stored leaf of the DFS. 
