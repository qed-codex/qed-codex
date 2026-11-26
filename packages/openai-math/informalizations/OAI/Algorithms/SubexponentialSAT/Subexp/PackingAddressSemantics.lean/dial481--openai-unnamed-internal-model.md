---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingAddressSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingAddressSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingAddressSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The emitted storage-address table is the graph of the actual packed
coordinate order. Its lookups produce the existing reordering read plan. 

### `addressRows`

 The physical address emitter increments a unary counter once per key. 

### `storageAddresses`

 This is the reversed table retained by the physical emitter. 

### `mappedRecords_eq_readPlan`

 Reverse queries compensate for the selector's prepending accumulator,
so its actual output is the read plan in original vertex order. 
