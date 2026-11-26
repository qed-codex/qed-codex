---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSelectedPreimages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedPreimages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedPreimages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Two-pass native preimage directory following the selected role rows 

### `countStart`

 The first address after the selected role records, reserved for the new sites' preimage
counts. 

### `rowStart`

 The address immediately after the count column where the directory stores the old site
identifiers. 

### `stop`

 The exclusive upper bound of the preimage directory, after space for every old site
identifier. 

### `counts`

 Encode the base address of the selected preimage count column as a machine word. 

### `rows`

 Encode the base address of the selected preimage rows as a machine word. 

### `Passes`

 The chronological RAM reports for clearing the new sites' counts and collecting their
old-site preimages. 

### `Passes.clear`

 Reports of the pass that zeros one preimage count per new site. 

### `Passes.collect`

 Reports of the pass that appends each old site's identifier to its selected owner's
  preimage row. 

### `Passes.middle`

 The memory handed to the collection pass after the counts have been cleared. 

### `Passes.final`

 The memory after the clearing and collection passes have both run. 

### `params`

 The public operands for collecting preimages, including the placement data and the
addresses of the counts and rows. 

### `Collected`

 Evidence that the two preimage scans ran, produced the selected layout's directory,
preserved memory outside it, and incurred their stated cost. 

### `collect`

 Both loops start from the live memory left by the selected placement and
role scans. The count clear makes arbitrary old scratch contents harmless. 
