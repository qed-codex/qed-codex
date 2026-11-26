---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafSourceLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSourceLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafSourceLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading the fixed public register vector of an auxiliary leaf

The live program supplies the virtual address width and bucket, its own word
width, the auxiliary clock, and all 34 auxiliary operands. Two of the latter
are taken from the live program's literal prefix. The current leaf address
and its full header word are dynamic and enter through separate registers.


### `Static`

 Fields fixed for all auxiliary leaf visits in one pair invocation. 

### `Static.dest`

 The register-bank field receiving a fixed scalar or public operand. 

### `slots`

 Cache order for the four geometry scalars followed by the public operands. 

### `expr`

 The expression that computes a fixed leaf scalar from the live pair operands. 

### `setStatic`

 Update the scalar's destination register while preserving the other registers. 

### `Static.offset`

 The field's offset in the private scalar cache. 
