---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputOperandStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputOperandStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputOperandStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing parsed prefix and geometry operands in the site processor

The first arithmetic registers are the actual public ports of the burst
interpreter. Two site scratch stacks hold the packed prefix and its length
during initialization, then a fixed routine clears both stacks before the
successor guard. The sorting workspace remains available at entry.


### `Expr`

 Geometry expressions for operand slots, with zero placeholders for slots supplied from the
actual program prefix. 

### `Target`

 Combined site-processor bank for the private table and its parsed operand vector. 

### `Source`

 Bank on which the physical prefix and operand initialization routines execute before their
ports are renamed. 

### `ports`

 Map computed operands to the interpreter’s public registers and map the two temporary
prefix words to site scratch stacks. 

### `program`

 Initialize the operand vector from the parsed site, clear the two prefix-word scratch
stacks, and return on the processor’s own ports. 

### `clockCoefficient`

 Fixed coefficient in the operand-startup clock bound, including the final scratch cleanup. 

### `result`

 The geometry arithmetic bank is kept apart from the site and sort work
stacks. Only the first arithmetic registers become site operands. 

### `frame_runs`

 The installed public bank is ready for the successor guard, the native
call interpreter, and the physical sorter. 
