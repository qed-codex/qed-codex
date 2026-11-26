---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapCallArg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallArg.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallArg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word fields of the private motif-call descriptor

Every map initializer reads a fixed set of addresses and widths. Its callers
use this same field order to compile their descriptor writes.


### `Arg`

 A fixed descriptor with no derived ends, offsets, or per-copy selector sequence. 
