---
{
  "module": "OAI/Computability/VPVNP/PairTerminalStageReverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalStageReverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalStageReverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Identifying the first two stages of an arbitrary accepting terminal trace

The bootstrap executes once from the original memory. Its empty-tape
execution fixes the entire report even at a different fuel allowance.
The following deterministic prefix is recovered across the two controller
cells, retaining each actual entry tag and the final physical memory.


### `Phase.force_oneShot`

 On identical starting memory a single accepting empty-tape call determines
the whole stage, including its physical exit. No read footprint is required. 

### `Phase.canonical_empty`

 A closed empty-tape reference determines every tagged report of the stage.
Its linked writes and controller handoffs determine the exact physical image. 

### `FiveTrace.canonical_start`

 Identify the bootstrap and prefix blocks of an actual five-stage accepting
trace using ordinary workers at their own fuel budgets. The bootstrap's
controller handoff supplies the memory agreement needed by the prefix. 
