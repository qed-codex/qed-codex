---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicInputOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicInputOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicInputOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading a fixed operand vector from geometry and a parsed program prefix

The physical operand bank has six inputs. The first four are the parsed
geometry. The remaining two are the length and packed value of the actual
program prefix read from the input tape. The program fills the expression
slots, then copies the two parsed words to each of their designated slots.


### `geometryOnly`

 Replace the two prefix-derived operand forms by literal zero while retaining the geometry
expressions in their own slots. 

### `registers`

 Register count needed for evaluating the geometry part of the input operand vector. 

### `input`

 The six public inputs, in order, are the four geometry words followed by the packed length
and value of the parsed prefix. 

### `embed`

 Embed the geometry interpreter’s four public ports into the first four of six while
retaining its other port names. 

### `slot`

 Register index at which the selected input operand is stored. 

### `program`

 Evaluate the geometry slots, then copy the parsed prefix length or value to each slot that
requests it. 

### `runs`

 Each component of the flattened table is loaded from its prescribed
operand. The time constant depends only on the fixed operand vector. 
