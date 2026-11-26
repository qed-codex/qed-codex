---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafCacheRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCacheRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafCacheRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the auxiliary leaf's cached operands in private RAM

The pair call computes the constant-sized scalar array in private memory.
A leaf loads its words in consecutive address order. The only extra register
written is the cache cursor. Every load and increment is a private tick.


### `readInstr`

 Load a scalar from the private cache at the current cursor. 

### `incInstr`

 Advance the private cache cursor by one word. 
