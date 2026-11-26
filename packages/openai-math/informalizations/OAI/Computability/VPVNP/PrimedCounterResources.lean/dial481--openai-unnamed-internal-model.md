---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Simultaneous resource bounds for the scheduled primed pair parser

For every sufficiently large length the same choice of address multiplier
works for every pair and every grammar whose dense histogram has at most
the prescribed polynomial size. The work bound includes the absolute-cursor
dispatch. The external budget includes all clear, initialize, visit and
comparison calls as well as the two input passes.


### `callCount`

 Exact absolute call count and private instruction allowance of a pair. 

### `privateFuel`

 Uniform per-call instruction budget, taking the larger of the assembler's address-scan
bound and the parser's word-processing bound. 

### `Bounds`

 Capacity inequalities for scratch storage, parser indices, the absolute cursor and the
private instruction clock at a chosen input length and address multiplier. 

### `callCount_eq`

 The calls counted by the absolute cursor use the exact budget above. 

### `eventually_layouts`

 The virtual bucket budget covers every group pair, including endpoint
pairs with an empty exterior cut. The returned layout uses the live word width. 
