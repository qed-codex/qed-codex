---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordISA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISA.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordISA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite stack routines for every binary word instruction

Every routine uses two distinct operand ports and an explicit result port.
Other local stacks start empty. At a successful return every local stack
contains at most one word's worth of bits, so the caller can reclaim all
scratch space in linear time. The port embeddings leave four of sixteen
workspace slots available for operand staging.


### `operandStacks`

 Place the two operand bit strings on their ports and initialize scratch
ports to empty stacks. 

### `Kernel`

 The finite control table of a binary word routine and its call contract. 

### `Kernel.K`

 Finite type of local bit stacks used by the selected binary word kernel. 

### `Kernel.Q`

 Finite control states of the binary word kernel, fixed independently of the operand
  width. 

### `Kernel.index`

 Inject each kernel stack into one of the twelve reserved arithmetic stack positions. 

### `Kernel.lhs`

 Local stack initially holding the first operand's little-endian bits. 

### `Kernel.rhs`

 Distinct local stack initially holding the second operand's little-endian bits. 

### `Kernel.out`

 Stack containing the fixed-width opcode result at an accepting return. 

### `Kernel.entry`

 Initial control state for invoking the kernel on its two operand stacks. 

### `Kernel.code`

 Bit-stack instructions implementing the selected binary operation at every word width. 

### `Kernel.accepts`

 A successful subroutine halt serves as the caller's return boundary. 

### `wordKernel`

 Select the fixed finite bit-stack implementation of a word RAM opcode. 
