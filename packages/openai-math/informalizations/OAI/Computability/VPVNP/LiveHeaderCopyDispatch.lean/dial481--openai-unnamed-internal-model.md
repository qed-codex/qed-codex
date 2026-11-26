---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderCopyDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderCopyDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderCopyDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native dispatch over the seven auxiliary header segments

Each three-word descriptor contains its cumulative end, source base and destination
base. A call uses the persistent cursor to find the first descriptor whose end
exceeds it, copies one word at the corresponding offset, and advances the cursor.
The entire dispatch table is fixed independently of the input length and word size.


### `Descriptor`

 One entry in the seven-segment auxiliary copy table, specifying its exclusive end and its
two array bases. 

### `Descriptor.endOffset`

 The cumulative exclusive cursor bound for this copy segment. 

### `Descriptor.sourceBase`

 The source address of the first word in this segment. 

### `Descriptor.targetBase`

 The destination address of the first word in this segment. 

### `address`

 Three consecutive descriptor words, addressed in the RAM word arithmetic. 

### `Spec`

 The external table stores the exclusive end, source, and destination for each of the seven
copy descriptors at its assigned addresses. 

### `prevEnd`

 The cumulative end of the preceding descriptor, or zero for the first, used to form a
segment-relative offset. 

### `Code`

 Native header-copy dispatch code over twelve registers and the public descriptor-table
base. 

### `setup`

 Load the persistent cursor and descriptor pointer, initialize the previous end to zero, and
set the word and descriptor strides. 

### `hit`

 Copy the word at the cursor's relative position in the selected descriptor and compute the
next cursor. 

### `skip`

 Remember the current descriptor's end and advance the pointer by three words to inspect the
next descriptor. 

### `scan`

 An exhausted table rejects by comparing a register strictly with itself. 

### `flow`

 Initialize the copy dispatcher and search its seven descriptors for the segment containing
the cursor. 

### `program`

 Instantiate the seven-segment copy dispatcher at the supplied external table base. 

### `row_native`

 The first descriptor ending strictly above the cursor performs one word copy.
At most eleven probes are needed, including the descriptor reads and the data access. 

### `flow_reject`

 No successful structured execution starts beyond the cumulative ends. 

### `reject_outside`

 Every state past the last occupied descriptor fails, including with arbitrary
fuel and an arbitrary branch tape. The rejecting comparison also covers an empty sweep. 

### `reject_ge_last`

 For cumulative ends in order, the last end is the exclusive upper bound on the cursor. 
