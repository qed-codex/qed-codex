---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapEntryExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successful grouped map calls have an exact clock and private state

The successful selector sequence fixes the tag checks, row dispatches and group
widths. The endpoint bits fix the label comparisons. The same deterministic
path writes the two staging arrays and increments exactly the emitted labels.


### `successTicks`

 Every successful call on the same input uses this tick count at all ready
configurations, including calls with different initial histogram counts. 

### `native_success_exact`

 Execute the three linked phases. The successful prefix, tick bound, continuation,
persistent state, and equality of every private word refer to the same endpoint. 
