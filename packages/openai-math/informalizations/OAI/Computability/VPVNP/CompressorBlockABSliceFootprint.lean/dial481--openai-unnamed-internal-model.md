---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockABSliceFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockABSliceFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockABSliceFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical footprint of the AB interval calendar inside a block

The fixed graph input begins at its own scratch-table head. The four read
columns lie between that head and the slice table, and the latter has one
bank for each bundle. Thus the typed chronological walk supplies the progress
and external address evidence of all AB stages inside the allocated interval.


### `ab_region`

 Exact external interval enclosing all reads, including the old widths
and both sets of field starts. 

### `ab_guarded`

 Preserve the real stage inputs and report lists and attach the exact
cursor guards, reads and writes to every stage of the admitted block. 
