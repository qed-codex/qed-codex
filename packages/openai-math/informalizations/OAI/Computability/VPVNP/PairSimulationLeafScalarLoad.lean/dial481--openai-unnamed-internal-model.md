---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafScalarLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native private writes for the virtual validator's scalar stack fields

A six-row loop writes one private word per stack cell, in increasing address
order. For a binary word the loop counts down the bit position. For a unary
tally it writes the low bit of the unchanged input word on each iteration.


### `Mode`

 Select either the successive bits of a binary word or repeated copies of its low bit for a
unary tally. 

### `bit`

 Read bit index `i` of the source word in binary mode, or bit zero in tally mode. 

### `payload`

 Order in private memory, starting at the port base. 

### `instruction`

 Registers hold destination, remaining length, value, zero, one and scratch. 

### `Linked`

 The six host instructions at the designated labels implement the scalar write loop for the
chosen mode and continuation. 

### `Result`

 The scalar loop exits at its continuation with all bits stored starting at `dst`, the
destination advanced and the remaining count zero. Only its destination, count and
temporary registers can change. 

### `load_prefix`

 All writes are private. One terminal test and six native transitions
per cell suffice on every input value. 
