---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CollisionStreamProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionStreamProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionStreamProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed collision callback with a persistent output stream

The runtime ABI reserves stack 0 for a packed row table, stack 3 for its unary
word width, stacks 8 and 10 for the two read plans, and stack 11 for the output
stream. Stacks 1 and 12 hold the two gathered type encodings. The remaining
stacks are gathering scratch. All sizes, plans, and encoded words are data.

The equality stage below uses the existing fixed equality program, clears its
possibly unconsumed input suffixes, and pushes one collision bit. In particular,
an early mismatch cannot leave stale type bytes in the next callback's scratch.


### `equality_eval`

 The actual equality trace, including preserved external stacks and bounds
on the suffixes which the cleanup stage must consume. 

### `seal_eval`

 Comparing, cleaning, and emitting is a fixed-code operation. Every stack
outside the two type buffers and the stream is preserved. 

### `stageState`

 State at a callback boundary. The two plan arguments are serialized bytes;
after a gather its plan is consumed. Only the row table, width, and stream are
persistent at this boundary. 

### `planBudget`

 The source bound can be read from the unary plans and word width alone;
the table contents do not affect it. 

### `program_trace`

 One actual fixed-program run gathers both types, emits their collision bit,
and restores the scratch stacks and registers for the next callback. 

### `primitive_runs`

 The primitive compiler sees the streamed bit on the designated output stack. 

### `gathered_assignmentType`

 ReadPlan's word-array refinement applies to the bytes actually gathered by
the fixed machine, including head/slot order and one-hot color encoding. 

### `assigned_primitive_runs`

 An actual primitive execution computes the collision leaf from the packed
seed rows and two runtime read plans. Encoding the whole type is done by the
two gather programs during this trace. 

### `completed_primitive_runs`

 Runtime-selected reads from the current-array/candidate-tuple table compute
the completed assignment's collision leaf. Selection indices and the table are
explicit input data; no function-valued callback is supplied to the program. 

### `leaf_primitive_runs`

 Specialization to the exact optional-update assignment at a padded tuple
leaf. Dummy tuple coordinates do not change its selected words. 
