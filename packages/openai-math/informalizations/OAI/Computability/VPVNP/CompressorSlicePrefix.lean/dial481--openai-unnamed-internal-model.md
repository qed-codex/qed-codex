---
{
  "module": "OAI/Computability/VPVNP/CompressorSlicePrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native prefix scans for Appendix E

A fixed table visits the external width array in increasing index order.
Its persistent word carries the index across calls. An external cell holds the
running total, so the next call can start with fresh private registers. Each
visit records the start of one field and adds its width to the total.


### `prefixOps`

 Public words name the width-array base, start-array base and accumulator cell.
Register zero carries the persistent field index. 

### `prefixEvents`

 The two read answers are obtained before either of the two writes. 

### `after_prefixEvents`

 Replay stores the old total at the field's start and the new total in the accumulator. 

### `prefixVisit_native`

 The actual opcode table executes one field visit in fourteen instructions. 

### `PrefixRegions`

 The input and output arrays fit and are disjoint. The accumulator can be
any other word address. 

### `PrefixAt`

 The first `k` start cells have been filled. Every other cell apart from the
accumulator retains its initial contents. 

### `prefixSegment_run`

 An uninterrupted segment may start at any completed prefix. All probes
read or write exactly the two cells specified for their current visit. 

### `prefixPass_run`

 Starting from a zero accumulator, the native pass computes all field
starts, preserves the widths and returns the field count. Its final accumulator
contains the full width sum, including when the list is empty. 
