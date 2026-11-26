---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafBootClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBootClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBootClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Uniform private clock for the complete auxiliary stack initializer 

### `eventually_ticks`

 One eventual bound applies to every input of the auxiliary initializer:
the cache and stride cost 89 ticks, the scalar pass costs at most n^14,
and the full incident copy costs at most n^5. 
