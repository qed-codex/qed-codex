---
{
  "module": "OAI/Computability/VPVNP/PairVertexLevelReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Read footprint of the traversal-level locator 

### `trace_reads`

 The boot reads four terminal fields. Each tested level contributes a
read of its start cell at offset 14, and the arithmetic exit has no reads. 

### `trace_worker_reads`

 All reads avoid the terminal control cells at offsets 0 and 31.
The level scalars precede the terminal header, and their word addresses
agree with the natural addresses of their published fields. 
