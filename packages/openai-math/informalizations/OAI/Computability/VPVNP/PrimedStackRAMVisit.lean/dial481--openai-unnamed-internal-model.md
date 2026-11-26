---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native preorder visit agrees with the grammar traversal

The complete opcode execution rejects exactly the branch strings rejected by
the mathematical visit. When it succeeds, its external memory represents
the prescribed next pending stack, mark set and common production histogram.


### `Agreement`

 Agreement between a grammar visit and a native node execution. They reject together, or the
final memory represents the resulting visit state, the choice stream is exhausted, and the
trace uses at most fourteen probes. 

### `completeNode_visit`

 Complete correctness at a single scheduled node, including malformed
and truncated bitstrings, repeated locations and exact post-memory. 
