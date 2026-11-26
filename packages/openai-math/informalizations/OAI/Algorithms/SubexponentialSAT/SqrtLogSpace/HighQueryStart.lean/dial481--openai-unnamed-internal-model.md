---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryStart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryStart.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryStart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual entry to each high-assignment count. The current frontend mask
survives concrete packing/arithmetic and drives the fixed zero-seed program.
The compact returned boundary is separate from the transient prefix bound. 

### `prepared_mask`

 Concrete preparation preserves the freshly recomputed current-query mask. 

### `prepared_seed_counter`

 The resulting durable seed uses this query's high set, with no common
high-set assumption between different marks. 

### `prepared_kept_frame`

 Every immutable source and suspended selector word survives the actual
packing/arithmetic outputs. No source is assumed unread here. 

### `initialized_lower_counter`

 The reusable lower counter and durable high counter contain the same
fresh zero tuple immediately after the actual initializer. 

### `initialized_register_frame`

 Seed generation touches only scratch registers0/1 and restores the
odometer guard21. In particular the real frontend guard8 remains available. 

### `initialized_mask`

 The current physical high mask itself survives initialization. 

### `initialized_boundary`

 Only the retained zero tuple needs a new boundary-length estimate; the
initializer empties every other changed word and frames all remaining words. 

### `resources`

 Source-only time, full-prefix space and a separately restored compact
boundary all describe the same actual fixed seed call. The empty high set
still produces the singleton encoded zero tuple. 
