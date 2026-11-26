---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkGatherRoute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherRoute.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherRoute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entering the selected shrinking party's field gather

The count and ID tables use the same ordered list as the compression pass.
The selected term determines the grid and the old header determines the
layout. The chronological trace here depends only on those published words.


### `noncomputable local instance : DecidableEq X.Base`

 Classical equality on base vertices for looking up the selected resident row. 

### `enterGather`

 Execute the real map-ID read, term read, grid and party cases, and layout
read at the indicated resident-row address. All operand base registers survive. 
