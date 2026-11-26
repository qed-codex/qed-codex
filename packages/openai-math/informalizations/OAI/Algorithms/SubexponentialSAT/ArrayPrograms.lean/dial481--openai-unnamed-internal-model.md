---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ArrayPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArrayPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArrayPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dynamic counted operations on Boolean stacks

The counter is a stack whose *length* is the requested number of bits. Its bit
values are ignored. In particular, bounds are data, not control-label counts.


### `countedTransferStacks`

 Exact result of consuming a counted segment and reversing it onto `dst`. 

### `counted_transfer_trace`

 The counter controls a fixed four-instruction loop. The precondition names
the segment it will consume, and proves the source contains enough data. 

### `counted_skip_trace`

 Skip precisely the number of data bits supplied by a unary counter,
restoring the initially empty discard buffer. 

### `counted_copy_trace`

 Counted preserving copy. Only the unary counter and destination change in
the final state; the source and temporary buffer are restored exactly. 

 ## Indexed fixed-width records

The seven stacks are: source 0, output 1, unary index 2, unary width 3,
temporary counter 4, copy scratch 5, and data scratch 6. Their contents can be
arbitrarily long. The program always has exactly 31 control labels.


### `lookup_skip_record_trace`

 One dynamic-width skip inside the lookup program. The width is preserved,
and all three scratch stacks return to empty. 

### `lookup_take_record_trace`

 Copy the selected record, preserving the width and source and restoring all
scratch stacks. The selected record is returned in forward order. 

### `lookupStacks`

 The source is left at the selected record, the selected record is prefixed
to output, and the unary index is consumed. 

### `lookupProgram_trace`

 Actual dynamic-width, dynamic-index lookup. `earlier` describes the records
preceding the requested record. Both its length and the common record width are
represented by stack data; the program has 31 labels for every input. 
