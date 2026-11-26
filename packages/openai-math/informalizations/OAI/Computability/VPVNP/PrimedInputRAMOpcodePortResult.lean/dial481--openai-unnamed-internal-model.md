---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodePortResult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodePortResult.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodePortResult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Converting a transcript sender into the physical scratch address

The routing block returns either an absent port or a sender's site and offset.
The final arithmetic block computes its row-major scratch address. It marks
a bit as owned exactly when the current site and offset both match the sender.


### `PortResultRegisters`

 Registers carried through the routing block, below its workspace. 

### `once_portResult`

 No copy source yields a clamped zero. A live copy source uses at most 14
private instructions, including the two comparisons for its owner flag. 

### `exec_portResult`

 Executing the physical block realizes the source and owner returned by
the scalar port dispatcher and preserves all other registers and memory. 
