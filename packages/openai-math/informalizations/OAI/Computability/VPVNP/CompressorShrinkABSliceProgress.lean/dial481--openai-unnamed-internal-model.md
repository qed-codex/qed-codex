---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceProgress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceProgress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceProgress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local progress of the transposed AB scans

A bundle can be visited at a fixed count, interval or incidence ordinal
after any number of calls on other bundles. Its input fields and its own bank
suffice to continue the three stages from their verified prefixes.


### `BankAt`

 The address belongs to one bundle's contiguous bank for the given old and new field counts. 

### `Cleared`

 The first `k` words of this bundle's slice bank have been reset to zero. 

### `Frames`

 For the first `k` old/new field pairs, memory records each intersection length and both
offsets whenever that length is positive. 

### `Dirs`

 The old- and new-endpoint directories index the first `k` intersection frames, grouping
them by the old and new field ordinals respectively. 
