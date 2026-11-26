---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotLevelRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevelRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevelRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical base matching produced by a shrinking level

The first four passes construct the absolute endpoint tables. The fifth
visits each base slot at lane zero and writes its matching base slot and
its lane displacement. These are exactly the words that serve as the old
base tables of the following compression level.


### `BaseMatching`

 Exact readback of both base tables under their common numeric base-arc enumeration. 

### `materialize`

 The fifth native pass, including the range checks for both of its data-dependent reads. 

### `Reports`

 Reports of the five actual passes, in directory order. 

### `Reports.genuine`

 Reports assigning each genuine candidate field to its endpoint owner or its reserved hole
  row. 

### `Reports.dummy`

 Reports assigning the outgoing and incoming fields of padding arcs to their packed site
  owners. 

### `Reports.append`

 Reports that append each absolute field identifier to its owner's row. 

### `Reports.scatter`

 Reports that invert the real endpoint rows to recover the rectangular slot of each field. 

### `Reports.bases`

 Reports that follow lane-zero endpoints to write the base matching and its lane
  displacements. 

### `Reports.all`

 The five slot-directory report lists in chronological order from the first owner scan
through base matching. 

### `Reports.final`

 Memory after replaying all five slot-directory scans in sequence. 

### `Reports.Native`

 The public banks and local cursor stops used by all five successive scans. 

### `Reports.Cursors`

 Exclusive stops are also the values returned by the last visits. 

### `run_selected`

 Starting from the selected records and fresh counters, construct the
absolute endpoint arrays and the next base graph in physical RAM. No rank
oracle or sorted input rows are required. 
