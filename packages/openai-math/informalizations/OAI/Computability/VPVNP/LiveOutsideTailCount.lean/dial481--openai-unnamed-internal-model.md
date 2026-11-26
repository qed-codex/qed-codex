---
{
  "module": "OAI/Computability/VPVNP/LiveOutsideTailCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTailCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveOutsideTailCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Applying the actual outside-stage budgets to the tail path count

The cost of the completed prefix is charged before counting the transition.
The gathered bit words and the endpoint sentinel have their canonical linked
logs. Thus a single numerical budget suffices for all paths of a noninitial
group, including groups whose cut fields decode to malformed configurations.


### `routeCost`

 A common bound for either exit of the last router. 

### `transitionCost`

 The cost allowance for transition preparation and all cell checks, including a dispatch
charge for every call. 

### `lastCount_capped`

 Count starting at the last router, from an already accounted prefix. 

### `nonfirstCount_capped`

 Count from the first router of every noninitial tail group. The
incoming gather, outgoing route, and complete linked transition fit the
same cap chosen before the choices of that transition. 
