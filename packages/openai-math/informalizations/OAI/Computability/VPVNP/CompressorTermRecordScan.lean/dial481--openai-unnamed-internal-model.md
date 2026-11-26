---
{
  "module": "OAI/Computability/VPVNP/CompressorTermRecordScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermRecordScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermRecordScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordered native term-record scans for a compressor pass

Each motif has a contiguous input demand row and a disjoint output descriptor.
The scan threads the post-call memory into the next motif. Every legal outer
choice is therefore counted once and all emitted rows are still available to
the later score and slice scans.


### `Layout`

 The rows may have arbitrary identifiers. Demand words are read-only and
term rows have two headers followed by the supply coordinates. 

### `Layout.source`

 First address of the contiguous input demand widths for each motif. 

### `Layout.base`

 First address of the disjoint output term descriptor for each motif. 

### `Layout.Outside`

 The address lies outside the grid index, repetition count, and payload columns of motif
`i`'s descriptor. 

### `strided`

 A dense or strided directory of demand rows followed by disjoint
descriptor rows is a concrete instance of the scan's address layout. 

### `Inputs`

 Expected demand vectors of a pass, read from the given memory. 

### `Fields`

 Exact row contents for an individual motif. 

### `tape`

 Canonical branch bits for an individual descriptor. 

### `prepFuel`

 Instruction cap for computing the repetition count from `d` demand widths bounded by `M`. 

### `eventsPerRow`

 One uniform event budget and one probe budget apply to every motif in the pass. 

### `probesPerRow`

 Probe bound for constructing one term record, including grid search, repetition
preparation, and payload stores. 

### `walk`

 Execute the five reset calls at each visited motif, threading the physical
external memory and preserving every report in order. 

### `Choices`

 Supply-index assignments for all motifs in the pass, with independently
admitted sets defined by each actual demand row. 

### `run_spec`

 The full pass has exactly the admissible term choices as successful
streams. Every output row survives to the end of the pass, and outside all
term rows the external memory is preserved. 

### `walk_site_bound`

 Each individual report obeys the same local instruction cap, even in
a pass with an arbitrarily large number of motifs. 
