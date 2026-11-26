---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMFlowComplete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowComplete.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowComplete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering structured traces from successful native execution

Every successful run of a linked block has a finite structured execution. The exit
receives exactly the unused fuel and branch suffix. In a standalone template the exit
is a single return instruction, so the recovered trace contains the entire event log.


### `Exits`

 Successful execution separates into a structured trace and its continuation. 

### `Linked.complete`

 Recover the structured execution from any successful entry, before the normal exit's
continuation. This applies to arbitrary linked code, even when the enclosing program has
further branches after the block. 

### `template_execute_iff`

 A standalone compiled template accepts exactly its finite `Exec` derivations with
all bits consumed, sufficient fuel for the return, and the indicated returned register.
With `result = none` the exit is an accepting halt. 
