---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyMoment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyMoment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyMoment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A concrete polynomial envelope for the stored sparse moment algorithm.
These are algebra/key-scan costs; primitive bit overhead is an additional
multiplicative resource supplied by the machine refinement. 

### `momentWork`

 The exact right hand side of `Moments.Stored.run_cost`, for all M supports. 

### `momentWork_le`

 Four powers of M suffice; no enumeration of global assignment tuples
is hidden in this bound. N counts the sum of the head bucket sizes. 

### `momentWork_le_dimension`

 A single explicit dimension parameter can dominate every ordinary
polynomial resource, while M is kept separate to preserve entropy. 
