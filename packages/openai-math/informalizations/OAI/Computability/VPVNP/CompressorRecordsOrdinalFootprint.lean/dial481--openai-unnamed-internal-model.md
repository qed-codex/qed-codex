---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsOrdinalFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOrdinalFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOrdinalFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses of complete ordinal scans

Read and write bounds verified on individual source calls are preserved
when the calls run consecutively. The resulting bounds allow the online
dispatcher to replay a pass after changing its own control words.


### `footprint`

 A native scan reads and writes only the union of its rows' data cells. 

### `successors`

 The report list records every successor cursor in visit order. 
