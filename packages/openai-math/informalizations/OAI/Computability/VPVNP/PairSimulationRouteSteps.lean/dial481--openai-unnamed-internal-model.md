---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSteps.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking the sorting fields of one cursor-routing phase

Phase `a` visits its `a + 1` fields in ordinal order. Each iteration checks
the current block of resident buffer bits and advances the common offset by
the block width. The loop returns to the outer phase increment.


### `steps_exact`

 Execute the sorting steps of a phase and collect their acceptance tests in the running mask. 
