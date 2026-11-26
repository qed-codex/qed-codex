---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentSerialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentSerialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentSerialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The physical assignment array and the semantic seed assignment have
the same order. The sequential search stores its chosen values in reverse;
decoding at the supplied seed indices restores their original list order. 

### `reverse_eq_map_decode`

 A duplicate-free index list recovers the whole reversed value array
from the existing decoder, provided the two lists have equal lengths. 

### `naturalValues_reverse_eq_map`

 The assignment's physical rows are in the exact supplied index order. 

### `naturalValues_reverse_map_eq_seedRows`

 The row encoding expected by packing is exactly the array produced by
the sequential assignment controller. 
