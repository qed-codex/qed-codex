---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SelectionTableProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectionTableProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectionTableProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Building the selector table at runtime

A fixed program scans framed unary seed indices, pairs each with the current
unary candidate-array position, and increments that position. The output is
the raw sequence `frame key ++ frame value`, with no outer list tags.


### `emitToAcc`

 Remove the emitter's record tag, then reverse the raw frame into the
stream accumulator. 

### `loop_eval`

 The actual framed-record loop preserves its growing counter and the raw
table accumulator in the exact input order. 

### `program_trace`

 Full halted trace of one fixed instruction table, with the table bytes
on output stack 3 and the incremented unary counter preserved on stack 2. 

### `traceCost_quadratic`

 A fixed quadratic bound in the unary input size parameters. 
