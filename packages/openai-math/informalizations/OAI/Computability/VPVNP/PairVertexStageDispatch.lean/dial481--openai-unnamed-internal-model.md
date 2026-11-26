---
{
  "module": "OAI/Computability/VPVNP/PairVertexStageDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStageDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexStageDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native dispatch on the producing shrink stage

The preceding level locator supplies the zero-based ordinal of the producing
stage. Each compressor block has `N` shrinking stages followed by a refresh.
This finite program constructs the period `N+1` from zero and one, takes the
native word remainder, and tests the `N` shrink ordinals in sequence.


### `Address`

 Instruction labels of the scheduled-stage selector, including ordinal comparison, per-stage
tests, and rejection. 

### `count`

 Total number of instructions reserved for selecting among the fixed number of scheduled
stage bodies. 

### `address`

 The constant loader, three preparation rows, two rows per shrink stage,
and the rejection row occupy consecutive ranges. 

### `entry`

 First instruction label of the stage-selection table. 

### `row`

 Relocatable native selector rows with five literal bits, for all block lengths. 

### `Linked`

 The host contains every width-resized stage-selector instruction under the supplied
placements and jumps. 

### `Frame`

 The stage selector preserves the machine state outside its designated scratch registers. 

### `run`

 The old stage ordinal leads to its actual shrink entry. The only events
are the fixed literal setup, three arithmetic rows and the bounded stage scan. 

### `run_reject`

 The refresh ordinal reaches the physical rejection row of the shrink dispatcher. 

### `run_prefix`

 The tick-only prefix composes with the surrounding depth-first parser
on every external memory and unconsumed binary suffix. 

### `reject_noReturns`

 A refresh residue has no successful continuation through the shrink
dispatcher, at any fuel bound or on any pending choice stream. 
