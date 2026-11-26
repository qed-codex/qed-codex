---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Replaying calls of the nested compressed pair table

A call begins with five private instructions, scans to the tag, and then
executes one unrelocated component with the original bit stream. Its
accepting exit can require three transfer instructions. The exact amount of
fuel left at that point characterizes all successful reports, including
arbitrary continuing words. Out-of-range tags reject.


### `overhead`

 Number of entry ticks and tag-dispatch events preceding a source-stage call in the
compressed pair. 

### `execute_ready`

 A native call at an in-range tag returns exactly a linked source report
whose possible handoff also fits within the remaining fuel. 

### `execute_stage_iff`

 Exact replay for every cap, including clocks too short to reach the tag. 

### `execute_bad_tag`

 Invalid tag words reject for any input stream and continuing word. 

### `preserves_word`

 The pair dispatcher preserves a protected word whenever each applicable
source component preserves it and the inner transfer tag has another address.
The statement applies to every successful call, even if later calls reject. 
