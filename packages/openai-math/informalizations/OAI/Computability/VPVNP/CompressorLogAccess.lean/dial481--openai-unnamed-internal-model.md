---
{
  "module": "OAI/Computability/VPVNP/CompressorLogAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLogAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLogAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Read and write bounds for native report lists

The bounds compose when report lists are concatenated. A scan that writes
one cell at each ordinal accesses exactly its addressed column.


### `LogAccess`

 Bounds on every address actually read or written, including repeated
writes to cells whose eventual values agree with the input. 

### `directEvents`

 Event trace of one direct external write surrounded by specified numbers of tick events. 

### `direct_scan`

 One external write per ordinal, with a fixed number of ticks on each side. 
