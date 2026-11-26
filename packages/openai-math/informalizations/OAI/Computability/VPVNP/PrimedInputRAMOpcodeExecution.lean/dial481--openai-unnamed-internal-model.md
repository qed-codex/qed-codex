---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native data calls for the primed input passes

Each call reads the three cut lengths, decodes the persistent cursor and computes the
source and owner with private word operations. Only the final action may consume a
branch bit. Its external writes and payload read are the operations of the public
schedule. The three preceding external reads leave the memory unchanged.


### `rawItem`

 The first pass uses only the owner bit; the second pass uses the copy source. 

### `actEvents`

 The skip opcode is a register reset after the two tests. Every other action executes
the same two tests followed by the public item's data events. 

### `dataEvents`

 The reported events record all 28 parameter/coordinate instructions, every private
dispatch tick, and the final choice or copy. 

### `dataCall_exec`

 A complete opcode derivation from a decoded dispatch ABI. The dispatch computation
uses no binary choice, so its tick count can be chosen before the private branch bit. 
