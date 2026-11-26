---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingExtractionSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The records emitted by block extraction have the exact computed packing order. 

### `emitEntries_addresses`

 The address table is prepended in the same order as the storage stream. 

### `typed_extraction_metadata`

 The covered metadata bytes returned by the actual extraction trace. 

### `typed_extraction_addresses`

 Exact address bytes emitted by complete-block extraction, retaining the
initial table and allowing a nonzero initial storage address. 
