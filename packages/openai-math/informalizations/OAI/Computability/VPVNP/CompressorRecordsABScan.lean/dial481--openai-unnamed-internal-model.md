---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsABScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete rectangular AB-piece scan

One finite program iterates over all piece ranks at all bundles. The total
column remains readable at every visit. Both output rectangles are directly
indexed by bundle and sorted rank; stride padding is untouched.


### `value`

 The two words produced for one AB piece, its equal-split width and its starting offset in
the bundle's concatenated payload. 

### `Regions`

 Separation of the row-total column and the two write rectangles. 

### `Layout`

 A natural address layout may place the total column and both output rectangles
at any pairwise disjoint ranges. Their padding cells require no initialization. 

### `Filled`

 All completed ranks and the exact frame of their writes. 

### `run`

 One call and three external probes per piece in the combined AB rectangle. 
