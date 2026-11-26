---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterDispatchPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic prefixes of scheduled calls

Each dispatch step contributes only ticks, preserves external memory, and
passes a determined register file to the selected continuation. The relation
below records both directions for every successful execution and its full log.


### `Pref`

 Removing a deterministic prefix of `k` ticks gives exactly the executions
of the residual program on its prepared registers. 
