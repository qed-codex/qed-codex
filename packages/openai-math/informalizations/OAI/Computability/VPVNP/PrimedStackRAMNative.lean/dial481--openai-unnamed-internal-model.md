---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Acceptance of the native preorder-node program

At ordinary burst-call entry the private workspace is zero. The program
loads the row offset from the persistent word and executes the finite node
table. Its accepting choice streams agree exactly with the grammar visit,
including the end-of-call test for unused bits.


### `entryRegs`

 Private register file after loading the persistent input-row offset into register 5 of the
initially zero workspace. 

### `nodeTemplate_accepts_iff`

 Native accepting paths for this call, with no per-input changes to the instruction table. 
