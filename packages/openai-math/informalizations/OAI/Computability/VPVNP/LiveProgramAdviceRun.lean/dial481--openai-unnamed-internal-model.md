---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdviceRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four linked advice stages of the live program

Starting at the length-field stage, the linked machine packs the length,
publishes and validates the four operand frames, packs the evaluator's
actual prefix through its dynamic frame, and packs the ordinal table.
Each transfer writes only the reserved stage tag. The last report returns
cursor zero to the prefix-copy stage with the full prepared memory image.


### `lp`

 The evaluated public operand bank for packing the advised prefix length. 

### `fp`

 The evaluated public operand bank for publishing the four midpoint input frames. 

### `op`

 The evaluated public operand bank for packing the advised label order. 

### `calls`

 Number of burst calls across length packing, the single frame publication, active-prefix
packing and order packing. 

### `finalMemory`

 The prepared advice memory with the outer tag set to enter prefix copying. 

### `work`

 Upper bound on calls plus external probes for the four advice preparation stages, including
the fixed frame-publication charge. 

### `CostLimit`

 Every successful execution of the given number of choice-free calls from cursor zero has
total calls-plus-probes cost at most the supplied limit. 

### `fourStages_budget`

 Execute the complete native advice prefix in the shared machine with its
real tag writes and repeated fetches of the dynamic prefix-packer frame. 

### `fourStages`

 Returning execution and final image of the four stages. 

### `finalImage`

 The end of the four-stage run retains all prepared banks. Its only extra
write is the prefix-copy tag, so the frame statement compares with the
initial memory carrying that same tag. 

### `fourStages_paths`

 These four stages give an equivalence on all accepting choice tapes for any
report cap on the continuation, including caps on the concatenated group. 

### `callCounts`

 The canonical call counts use the actual raw prefix length and the table's
encoded ordinal width, including the empty-bank return when there are no rows. 
