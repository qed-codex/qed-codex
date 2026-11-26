---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkRowAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkRowAction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkRowAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trace and acceptance of one shrinking resident map row


### `rowAction`

 Trace and final scratch for a successful row, including the route to its gather.
A rejected matrix entry yields `none`. 

### `rowAction_isSome`

 An indexed resident row succeeds exactly when its underlying grouped matrix succeeds. 

### `rowAction_noChoices`

 The dispatch and map add no guesses to a physical operand gather. 
