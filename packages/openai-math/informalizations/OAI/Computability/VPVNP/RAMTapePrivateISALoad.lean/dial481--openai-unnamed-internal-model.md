---
{
  "module": "OAI/Computability/VPVNP/RAMTapePrivateISALoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISALoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISALoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lowering the private-load opcode to finite stack control

The first copy stages the complete address before the destination register is
overwritten. This also implements loads whose address and destination are the
same register. The write log is restored by its kernel and the two staging
ports are emptied before returning to the instruction dispatcher.


### `loadPrivate`

 Stage the address before overwriting the destination, look it up in the private write log,
copy the result to the destination, and clear both staging stacks. 

### `loadPrivate_config_run`

 For an arbitrary private configuration the physical load realizes the
exact private continuation of the opcode. 

### `loadPrivate_cost_le`

 Uniform bound in the width and number of writes. No step loops over the
numeric value of the address. 
