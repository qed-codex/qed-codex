---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildScanCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildScanCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildScanCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Work of the child argument scan

Every old port requires one width probe. Each incoming port also requires
one inverse-incidence probe. Each guessed bit uses six local instructions.
The row scan adds one descriptor probe and ten instructions per child and
two final exit instructions, including for an empty row.


### `events_cost`

 Exact guessed bits, probes, and instructions of the native scan. These
counts include the exit after the last child. 
