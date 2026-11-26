---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshPhases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPhases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPhases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native external descriptor construction from an old compressor state

The old outgoing slots index the width column directly. The old base table supplies a target
and a binary lane displacement per arc. Three scans with shared external memory gather the
actual widths, translate the base table into a bundle directory and write the two endpoint
segment tables. The resulting totals and segment rows refer to the same old state and the
same kernel intervals. The resource count includes all three scans.


### `gatherWords`

 The gather and directory tables use the array bases of the ensuing external pass. 

### `directoryWords`

 Assemble the bundle-directory operands from the residual lane count, old base columns, and
three scratch destinations. 

### `baseOutsideGather`

 The old base columns also remain live through the gather's width writes. 

### `outsideLevel`

 A physical address outside all seven arrays at this level. 

### `bundleCount_positions`

 The source-bundle count is the physical position count of the input state. 

### `ExternalReports`

 Native reports, memory and geometric rows produced by the three external passes. 

### `ExternalExecution`

 Existence of a complete deterministic external construction. 

### `external_phases_stages`

 Execute the three native phase tables in succession from the old physical slot records.
For `B` bundles and `S` segments the exact cost is `6B + 12S` calls plus external probes. 

### `external_phases`

 A complete execution of the three native refresh prepasses. 
