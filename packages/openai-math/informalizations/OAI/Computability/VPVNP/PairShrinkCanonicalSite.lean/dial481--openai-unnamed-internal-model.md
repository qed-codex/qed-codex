---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCanonicalSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical directories and workspace bounds at a selected shrinking site 

### `CanonicalSite`

 Addresses, field directories and workspace bounds for one selected site. 

### `CanonicalSite.workspace`

 Base word address of the compressor's descriptor workspace. 

### `CanonicalSite.positions`

 Number of processor positions used when laying out the compressor's workspace. 

### `CanonicalSite.blocks`

 Number of complete scheduled blocks in the compressor's workspace layout. 

### `CanonicalSite.cur`

 Chronological pass index used to locate the producing level and its tables. 

### `CanonicalSite.rowEnd`

 Exclusive end address of the selected traversal's node rows. 

### `CanonicalSite.older`

 Base address of the input layer's node rows. 

### `CanonicalSite.later`

 Base address of the output layer's node rows. 

### `CanonicalSite.limit`

 Upper address bound on the canonical jobs' private workspaces. 

### `CanonicalSite.mem`

 Physical memory read by the vertex handler at this site. 

### `CanonicalSite.level`

 Word address of the header for the producing compressor level. 

### `CanonicalSite.term`

 Word address of the shrinking term records for the producing level. 

### `CanonicalSite.source`

 Published map directory and term data read at this site from the specified memory. 

### `CanonicalSite.publicData`

 The eleven public operand words of the terminal vertex program. 

### `CanonicalSite.levels`

 Number of passes in the selected chronological execution. 

### `CanonicalSite.passIndex`

 Pass ordinal supplied to the vertex handler for this row. 

### `CanonicalSite.incidence`

 Directory of the packed incidence columns used to recover the old wire endpoints. 

### `CanonicalSite.descriptor`

 Child-argument descriptor selected by the popped node address. 

### `CanonicalSite.hiddenArgs`

 Addresses and row parameters for guessing the hidden fields at this site. 

### `CanonicalSite.seed`

 Initial assignment of the hidden fields placed at this site. 
