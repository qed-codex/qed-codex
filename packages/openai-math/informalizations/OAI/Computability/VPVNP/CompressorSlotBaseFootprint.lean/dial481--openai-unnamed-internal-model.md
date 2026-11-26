---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBaseFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBaseFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses of the lane-zero base matching scan

Each base arc uses the real outgoing row to locate the adjacent incoming
field in the inverse table. Both lookups precede the output columns, so
the same sorted endpoint tables remain valid on every visit. The native
reports read within the row and inverse tables and write within the target
and displacement columns.


### `BaseReadRegion`

 The sorted endpoint rows and inverse field directory. 

### `BaseWriteRegion`

 The target and displacement columns written by the base matching scan. 

### `scan_regions`

 Lift read bounds on a single visit to its full segment. All earlier
writes are above the two input tables. 

### `base_footprint`

 In the memory left by scatter, the sorted source row contains the field of
the lane-zero outgoing end. Its successor is the incoming field of the same
arc. These two fitting addresses account for every external read of the pass. 

### `selected_base_footprint`

 The native reports and final tables supplied by `run_selected` suffice:
the base pass writes only above the scatter tables, so the final table
readback also holds at entry to this pass. 
