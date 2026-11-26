---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionOuter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionOuter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionOuter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed outer loop extracts all complete blocks in block-major order. 

### `program_trace`

 Extract the first `n` entries of every bucket by an actual nested loop.
The storage accumulator is retained in reverse-bit form for appending leftovers. 
