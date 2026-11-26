---
{
  "module": "OAI/Computability/VPVNP/ComplexityLib/ToUpstream.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/ToUpstream.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ComplexityLib/ToUpstream.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Simulating exact arithmetic circuits in complexitylib

The induction synthesizes all earlier gates at once, so two references to the
same gate can use the same wire. A binary gate needs at most two additional
gates for its scalar operands. Subtraction uses a constant gate for `-1`,
a multiplication, and an addition. A scalar output needs one final gate.


### `WireFunction`

 A polynomial-valued function of the input wires. 

### `gateFunctions`

 The polynomial-valued functions realized by the gates of a program prefix. 

### `synthesizeRef`

 Inputs and previously computed gates are available wires. A scalar
operand needs at most one new gate. 

### `synthesizeBinOp`

 With the operands available, subtraction costs three gates and the other
two binary operations cost one. 

### `synthesizeProgram`

 The upstream program retains every gate of the simulated prefix at a cost
of at most five upstream gates per project gate. 

### `exists_upstream_circuit`

 Every formal polynomial has an upstream circuit whose charged constants
and subtraction expansions cost at most five gates per project binary gate,
plus one gate if the designated output is a scalar. 
