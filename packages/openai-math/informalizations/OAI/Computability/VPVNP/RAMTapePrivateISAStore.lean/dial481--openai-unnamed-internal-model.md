---
{
  "module": "OAI/Computability/VPVNP/RAMTapePrivateISAStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISAStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISAStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A private store on the architectural stack bank

The instruction copies the address and the value from the architectural
registers, prepends their bits to the private log, and clears the two staging
ports. Since each operand copy restores its source, one register may supply
both operands.


### `storePrivate`

 Execute the private store with its two source registers fixed by the
instruction table. 

### `storePrivate_run`

 The newest write extends the private log and the instruction returns
with an empty workspace. The instruction count is independent of the old
log length and of the address stored in the register. 
