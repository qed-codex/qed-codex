---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairAuxiliary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairAuxiliary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairAuxiliary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The public operands of the two sparse-header preparation stages 

### `sizes`

 Live header sizes obtained by evaluating the fixed length expressions at the group
geometry. 

### `pairLengths`

 Auxiliary input-field lengths for the chosen first-half pair, determined by its index and
the live chain, cut, and advice sizes. 

### `desc`

 Descriptor table’s base address encoded at the RAM word width. 

### `shadow`

 Virtual shadow’s base address encoded at the RAM word width. 

### `counter`

 Label-counter array’s base address encoded at the RAM word width. 

### `source`

 The seven physical source addresses from which the auxiliary header copy reads its fields
and nominated counts. 

### `init_data`

 Every public operand of the initializer agrees with the concrete sparse
header geometry, including its array of seven physical source addresses. 

### `copy_data`

 The guarded copy reads its end cursor from the final descriptor. 
