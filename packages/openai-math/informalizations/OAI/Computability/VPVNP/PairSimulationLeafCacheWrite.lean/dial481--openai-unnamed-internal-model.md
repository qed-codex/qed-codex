---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafCacheWrite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCacheWrite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCacheWrite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Storing the coefficient counter's scalar cache once per pair call

Each register produced by the operand evaluator is written into its
prescribed private cache cell. The two-instruction store and increment
sequence has no external actions and preserves the source registers.


### `storeInstr`

 Store one computed operand at the private cache cursor. 

### `Stored`

 The exact consecutive output words, final cursor and unchanged surrounding private state. 
