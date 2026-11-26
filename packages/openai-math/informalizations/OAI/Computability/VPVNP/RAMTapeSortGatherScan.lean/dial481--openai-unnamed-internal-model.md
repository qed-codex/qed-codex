---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortGatherScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Scanning to a unary record offset

Five invocations of the word mover remove a physical record. An offset loop
repeats this fixed subprogram for the records preceding the selected one.
All skipped bits accumulate in reverse order for restoration.


### `store`

 Place the block, skipped prefix, selected record and output on their gather ports with
unary offset and width counters and empty width scratch. 

### `skip`

 The skipped prefix is saved bit-for-bit on a single reverse buffer. 

### `select`

 The selected record moves to its own reverse buffer, separate from the prefix. 
