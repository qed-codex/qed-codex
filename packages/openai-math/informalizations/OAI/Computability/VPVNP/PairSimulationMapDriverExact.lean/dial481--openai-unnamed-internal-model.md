---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapDriverExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriverExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriverExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact ticks of the successful row driver

The number of comparisons for a copy is the position of its selector in the
fixed dispatch table. The selected row supplies its own input-dependent tick
count. The same path stores every label and carries the offset and register
invariants to the width check.


### `visitSteps`

 Test, selector load, dispatch, selected row, label store and two increments. 

### `exactSteps`

 The final exit test follows the last copy. 

### `native_exact_framed`

 The complete exact path preserves the exterior registers, delivers each label at
its private array position, and leaves all other private cells unchanged. 
