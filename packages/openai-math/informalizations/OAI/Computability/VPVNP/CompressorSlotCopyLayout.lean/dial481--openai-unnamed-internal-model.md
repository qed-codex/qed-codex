---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotCopyLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotCopyLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotCopyLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Address bounds for copying the shrinking incidence directory

The three base columns occupy shorter intervals than the three lane columns.
The destination reserves one full lane column per field. A single interval
comparison therefore suffices to schedule the six canonical copy scans.


### `shrink_rows`

 The native copy worker scans exactly the initialized part of each output column. 

### `shrink_column_bounds`

 Every live source cell lies between the first base target and the last outgoing width. 

### `packed_column_bounds`

 The descriptor's fixed column stride reserves all live rows of the selected state. 

### `Regions.shrink_to_level`

 The selected shrinking directory can be copied to the next descriptor
level whether the canonical output is below or above the scratch allocation. 
