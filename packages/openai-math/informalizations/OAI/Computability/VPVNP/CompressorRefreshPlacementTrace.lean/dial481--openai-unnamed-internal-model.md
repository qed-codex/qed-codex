---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshPlacementTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPlacementTrace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshPlacementTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed placement arrays and the native degree - refresh trace

The owner, count and singleton preimage columns occupy three consecutive arrays.
Each source report writes the three cells of its ordinal and returns the next
ordinal. Thus a complete scan writes every address in the placement arena.


### `packed`

 Sizes and addresses of the three packed placement columns. 

### `log_write_iff`

 An address - value pair is written precisely when it is the cell and payload of
one of the three columns at a visited ordinal. 

### `packed_written_iff`

 Every cell of the full arena occurs as a genuine native write. 
