---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingOutputSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingOutputSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingOutputSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual leftover scan completes the metadata, storage order, and
address table produced by complete-block extraction. 

### `packedSnapshot`

 Exact state after complete-block extraction from empty accumulators. 

### `finish_storage_bytes`

 The final transfer reverses the accumulated bits and appends the list terminator. 

### `finish_extraction_outputs`

 All physical accumulators after extraction and the actual leftover scan. 
