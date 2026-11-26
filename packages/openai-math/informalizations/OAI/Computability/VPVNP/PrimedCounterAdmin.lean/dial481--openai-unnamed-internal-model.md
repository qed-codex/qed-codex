---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterAdmin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdmin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterAdmin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Administrative calls of the scheduled pair parser

One clear call resets the leaf mark indexed by register 2. One initialization
call installs the root in the first frame and sets the depth to one. Each
comparison reads the dense production count and the corresponding nomination
word indexed by register 7. Every instruction in these calls is deterministic.


### `stackPublic`

 Include the eleven stack-parser operands in the first eleven positions of the fourteen-word
administrative operand table. 

### `clearOps`

 The original mark-clear block installed into the enlarged public-word table. 

### `initOps`

 Instructions that write the root degree and state into the first pending frame and set the
stack depth to one. 

### `compareOps`

 Guard the dense label index, load its accumulated count and nominated count, and require
their equality. 

### `clear`

 Straight-line routine that clears the mark for one terminal position. 

### `init`

 Straight-line routine that initializes the pending parse stack at the root of the current
site. 

### `compare`

 Straight-line routine checking the histogram count for one production against the
nomination. 

### `rootMemory`

 External memory after storing the root degree, root state and initial stack depth at the
parser's public addresses. 
