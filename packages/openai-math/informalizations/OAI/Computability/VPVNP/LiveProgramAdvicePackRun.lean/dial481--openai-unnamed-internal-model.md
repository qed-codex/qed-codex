---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdvicePackRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdvicePackRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdvicePackRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The three advice pack sweeps in the outer live program

The fixed component dispatches its row cells on the shared external memory.
Every intermediate cursor preserves the stage tag. The last report replaces
the tag by the destination and returns zero. The indirect prefix stage reads
its five public operands from a stable external frame on every call.


### `tagAddr`

 External address of the outer stage tag used when the packed advice stages transfer
control. 

### `LinkedPack`

 Endpoint and resource specification of the linked advice stage. 

### `linkedPack_direct`

 The linked program executes a directly supplied row packer and advances
to the next stage with its destination tag and zero cursor. 

### `linkedPack_framed`

 Loading five public operands on every call preserves the same output
memory. The frame remains readable throughout because each of its five
addresses lies outside the bank being written. 
