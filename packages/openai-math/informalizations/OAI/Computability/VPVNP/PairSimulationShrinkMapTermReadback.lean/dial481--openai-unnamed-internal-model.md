---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkMapTermReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapTermReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkMapTermReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Agreement of the selected and retained shrinking grid words

The native term worker and the later table readback identify the same demand
grid point for every resident motif. The fixed grid enumerates each point
once, so the actual word indices agree.


### `termReadbackBaseDecEq`

 Classical equality decision for base vertices used to compare retained term grid words with
the words written by the term-selection worker. 

### `term_readback`

 The retained grid word equals the one selected by the native term worker. 
