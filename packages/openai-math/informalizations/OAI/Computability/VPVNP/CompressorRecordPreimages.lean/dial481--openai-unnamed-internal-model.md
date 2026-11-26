---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordPreimages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPreimages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPreimages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the placement array into local preimage lists

In the third scan of Appendix E, the selected layout has assigned each old site to one
new owner. Visit the old sites in index order. One fixed RAM call reads the selected
owner, appends the old site's index to that owner's bounded list, and returns the next
old index in the persistent state. The call rejects a malformed owner or an exhausted
row. The local traversal of §13 then has all immediate preimages in directly addressed
order, even when the same old vertex supplied several distinct motif roles.


### `prepareRow`

 Public words give the old-site count, owner-array base, new-site count, count-array
base, row width, and row-array base. Register 3 is the old-site index. 

### `collectPreimage`

 One call per old index. Register 6 is the unit loaded by the append operation. 

### `ownerAt`

 Read the selected new owner of an old site from the placement array. 

### `countAt`

 Address of the current preimage count for one new owner. 

### `rowAt`

 First address of an owner's preimage list, using the public row capacity as its stride. 

### `collectUpdate`

 Exact physical update of the count and data cells by this one scan call. 

### `collectEvents`

 The report of a successful visit includes the two reads and two writes. 

### `after_collectEvents`

 The physical write log implements precisely the two updates used in the next call. 

### `collectPreimage_native`

 A scan visit through the fixed native table, starting with zeroed private state. 
