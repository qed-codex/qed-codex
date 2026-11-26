---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterFoldOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFoldOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFoldOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Order and prefix capacity of the parser slots

The expanded loops run through all absolute cursor values consecutively.
Only node calls increase counts. The other calls preserve the histogram,
and the root initializer reinstates a stack representing at most `n` leaves.


### `items_order`

 Reading the assembled inputs and then following the logical parser loops
gives exactly the increasing absolute cursor. 

### `isNode`

 Detect the parser-node slots, the only post-assembly calls that can increment production
counts. 

### `prefix_bounds`

 Bounds hold for every executed prefix, regardless of later rejection.
Each component increases by at most the number of node items. 

### `next_increment_le`

 Immediately before a scheduled node, the next increment is bounded by
the number of node calls in the whole rectangle. 
