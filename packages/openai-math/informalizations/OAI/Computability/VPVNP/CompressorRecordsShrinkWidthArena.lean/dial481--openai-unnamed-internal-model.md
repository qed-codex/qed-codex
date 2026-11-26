---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkWidthArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkWidthArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkWidthArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Widths and field starts in the shrinking arena

Scatter the widths of the ranked old ports, scan the two sorted row families,
and split the thick totals into balanced AB pieces. All four workers run in
sequence on a fresh arena after the rank and incidence directories.


### `scatterBank`

 Public words for scattering old port widths into sorted bundle rows, giving the owner,
rank, and old-width columns, row stride, and output base. 

### `prefixBase`

 First address of the field-start rectangles, immediately after the two families of sorted
width rows. 

### `abBase`

 First address of the AB piece-width rectangle, following both start rectangles and both
columns of bundle totals. 

### `stop`

 First free address after the dense AB piece-width and field-start rectangles. 

### `prefixBank`

 Parameters for scanning sorted widths into field starts and bundle totals. The motif flag
selects the CD rows when true and the thick-wire rows when false. 

### `abBank`

 Parameters for splitting each thick-wire bundle total into balanced AB pieces and storing
their widths and starting offsets. 

### `scatterLayout`

 The owner, rank and old width columns can be anywhere before the fresh arena. 

### `prefixedMemory`

 Memory after scattering the widths and applying first the thick-wire and then the motif
prefix-scan reports. 

### `finalMemory`

 Memory after the AB piece reports have written widths and starts on top of the completed
scatter and prefix scans. 

### `Run`

 Four native executions, readbacks at their joint endpoint, and their cost. 

### `build`

 Starting with the native rank directory, materialize all widths and starts.
The original directories and every other address below the allocation survive. 
