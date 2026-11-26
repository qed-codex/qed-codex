---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteValidator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteValidator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteValidator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the native routing checker on a cursor vertex

The scheduler starts by clearing the mask and offset. After the successor
fields it switches to the sorting-block width. The final jump tests the mask
accumulated over both passes. All inputs, including inconsistent four-port
buffers, reach their continuation within the same clock bound.


### `native_exact`

 Run the linked scheduler on the resident buffers. It consumes only local ticks,
preserves both memories, and jumps according to the exact routing predicate. 

### `native`

 Every resident input reaches its routing continuation within the scheduler clock. 

### `native_reject`

 With a rejecting instruction at the failed exit, every failed route rejects
on every branch tape and external memory, including at budgets shorter than its scan. 
