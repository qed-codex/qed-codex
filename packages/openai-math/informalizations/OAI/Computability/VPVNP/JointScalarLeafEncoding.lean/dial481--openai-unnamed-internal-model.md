---
{
  "module": "OAI/Computability/VPVNP/JointScalarLeafEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Packing the exponent coordinates of a signed original-row query 

### `packed`

 Concatenate the low `W` bits of each exponent in coordinate order, least significant bit
first within each coordinate. 

### `query_bits`

 The little-endian binary words sent to the interpreter are the inputs
of the gate checker in the order of its formal wires. 
