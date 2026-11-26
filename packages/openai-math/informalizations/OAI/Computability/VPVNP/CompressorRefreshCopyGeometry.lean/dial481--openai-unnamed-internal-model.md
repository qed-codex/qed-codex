---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshCopyGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCopyGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCopyGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed copy geometry for a selected degree refresh

The scratch columns and canonical successor columns use the full number of
output slots as their common stride. Only the populated prefix of each
column participates in the copy. The first three prefixes end after the
base ports, and the last three include all residual lanes.


### `Packed`

 The output allocation and the canonical successor have the same
column stride, and the scratch output fits before the successor arrays. 

### `source`

 Natural intervals of all live source and destination cells, in the
form used by the native copy worker's event footprint. 

### `packed`

 For the actual branch, the old level's array head locates the scratch
plan above the controller, and the two bounded allocations justify every
source and destination address in the copy. 
