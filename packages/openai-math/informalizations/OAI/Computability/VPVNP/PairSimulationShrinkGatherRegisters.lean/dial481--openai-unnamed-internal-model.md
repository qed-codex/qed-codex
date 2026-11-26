---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkGatherRegisters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherRegisters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherRegisters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register separation in the hosted shrinking map segment

The combined register enumeration gives independent locations to the site
header, private matrix evaluator, each operand gather and the layout scratch.
Only the host's disjointness from DFS and saved registers is needed below.


### `hosted_banks`

 Both native code families receive their true disjoint register bank. 

### `Protected`

 The item reader writes the motif, party, term pointer and grid, and the
layout and ordinal branches use two further scratch registers. 
