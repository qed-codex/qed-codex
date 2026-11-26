---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticCallCopies.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCallCopies.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCallCopies.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying the input stacks of an arithmetic call

The fixed list of source and destination ports determines the control table.
Sources may repeat, so an advised word can initialize several ports in one call.
One empty scratch stack serves the entire sequence.


### `copyPlan`

 Each pair specifies a source and its destination. 

### `Valid`

 Destinations are distinct, sources are read-only, and scratch is separate. 

### `copied`

 The destinations contain the corresponding original source values. 

### `copyPlan_runs`

 Each destination starts empty and receives one source copy. Each source
bit costs five instructions, each copy tests for the end twice, and the
final return costs one instruction. 
