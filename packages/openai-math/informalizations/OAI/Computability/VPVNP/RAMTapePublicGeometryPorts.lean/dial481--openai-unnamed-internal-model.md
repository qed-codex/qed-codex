---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicGeometryPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometryPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicGeometryPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading parsed public geometry into the arithmetic interpreter

The physical parser supplies the four unary parameters and its zero-bit
template. The converter writes the four public operands of the ISA bank,
copies the template into its persistent word, and initializes its padded
register words and empty private log. The existing processor stacks are
available throughout the expression evaluation.


### `Port`

 Joint bank of parsed processor data and the four-public-input arithmetic interpreter. 

### `prepare`

 Enter the fixed arithmetic routine with an initialized ISA bank.
The number of arithmetic registers belongs to the fixed expression code. 

### `budget`

 Time for loading the four public inputs, padding the persistent word,
and initializing the requested private arithmetic register bank. 
