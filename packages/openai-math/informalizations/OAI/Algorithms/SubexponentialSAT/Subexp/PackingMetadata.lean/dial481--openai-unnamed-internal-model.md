---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingMetadata.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingMetadata.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingMetadata.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact lookup semantics for the storage-ordered packing metadata table.
The physical extraction proof identifies its emitted records with this table. 

### `records`

 The actual emitter prepends pairs while traversing storage order. 

### `lookup_covered_iff`

 Covered metadata identifies exactly the computed block/type inverse. 

### `lookup_leftover`

 An uncovered vertex carries its actual rank in the original-order leftover list. 

### `covered_filter_eq_leftovers`

 The physical missing-key filter selects exactly the typed leftovers. 
