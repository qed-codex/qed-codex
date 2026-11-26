---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan classifying each old outgoing port

The old port's mate selects two of the six input addresses. During the scan
these addresses and their contents agree with their values in the initial
memory. Each old port receives a bucket and a sorting key in separate output
columns. A complete scan costs nine units per old port, including the call.


### `outAddr`

 The bucket and the sorting key, respectively, in the original port order. 

### `field`

 Select the bucket word or the sort-key word produced by classifying an old outgoing port. 

### `Regions`

 The six initial input addresses can overlap freely. Every output cell
has a unique port and column, disjoint from those input addresses. 

### `Regions.packed`

 Two consecutive output regions of capacity `N`. Old columns on either
side of the interval can be shared with other passes. 

### `readAddress_eq`

 The mate read alone determines the choice of input addresses. 

### `scanReports`

 The report sequence in increasing old-position order. Every lookup is
expressed directly in the initial external memory. 

### `scan_native`

 The complete native segment, with no change to the six input addresses. 

### `ScanResult`

 The returned registers, external work and complete memory contents of a
bundle scan, including the untouched portion of each output column. 

### `scan_run`

 Execute the whole interval from its initial memory. Every one of the
two output columns agrees with the classification computed from the six
original input values. 

### `ScanResult.readAddress_stable`

 Following a stored mate after the scan selects the same destination
cells as following it before the scan. 
