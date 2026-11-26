---
{
  "module": "OAI/Computability/VPVNP/RegisterTableRoutine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegisterTableRoutine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RegisterTableRoutine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Calling a register table as a returning bit-stack routine

An `accept` opcode returns normally to the caller after completing the final
instruction dispatch. The return changes no register or stack, and the bound
on transient stack height also holds after linking.


### `routine`

 Run a register table from its entry label as a bit-stack subroutine that returns on its
accept callback. 

### `return_run`

 Add the final dispatch to a bounded run which reached an `accept` instruction. 
