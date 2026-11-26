---
{
  "module": "OAI/Computability/VPVNP/PairRefreshResidentFrontExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentFrontExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentFrontExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact traces of the refresh diagonal and grid/port dispatcher

The operand setup depends only on the six inputs and external memory. The
comparison and dispatch loops add fixed runs of private ticks, so arbitrary
caller registers have no effect on the chronological external reads.


### `setupEvents`

 Chronological register-setup events obtained by evaluating the compiled operand expressions
in the supplied external memory. 

### `frontEvents`

 Trace through diagonal setup, outgoing and incoming bit comparisons, route setup, and
selection of the grid and party handler. 
