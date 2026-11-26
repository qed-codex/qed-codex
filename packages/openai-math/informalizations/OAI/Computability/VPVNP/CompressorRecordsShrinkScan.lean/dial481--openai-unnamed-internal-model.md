---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan of the shrinking placement rows

The four input columns are looked up in the original greedy and incidence
directories. Their addresses can vary with the decoded base and arc. Every
visited old position receives four private-to-that-position output cells.
The only restriction on input placement is disjointness from the output
cells, so the scan can use directories produced by earlier passes.


### `readAddr`

 The physical address read from each of the color, offset, mate and
displacement columns when visiting row `i`. 

### `outAddr`

 The four output columns start at public words 10 through 13. 

### `Outputs.field`

 Numerical order of output columns, in the order in which they are written. 

### `Regions`

 The scan needs distinct output cells and persistent access to the old
columns. Different input lookups may freely share an address. 

### `Regions.packed`

 Four consecutive output regions of capacity `N`. The old directory may
be anywhere outside the reserved output interval, on either side of it. 

### `Regions.packedAfterInputs`

 Old directory columns may have any starts below the four new arrays.
Even without a positive radix assumption, each decoded input index is at
most the visiting row index. 

### `Regions.packedEight`

 Eight consecutive arrays of equal capacity, with the four input columns
first and the four newly written columns last. 

### `scanReports`

 The report sequence in increasing old-position order. Every lookup is
expressed directly in the initial external memory. 

### `scan_native`

 The complete native segment, with no change to the four input columns. 

### `ScanResult`

 The returned registers, external work and complete memory contents of a
shrinking scan, including the untouched portion of each output column. 

### `scan_run`

 Execute the whole interval from its initial memory. Every one of the
four output columns agrees with the graph placement computed from the four
original input values. 
