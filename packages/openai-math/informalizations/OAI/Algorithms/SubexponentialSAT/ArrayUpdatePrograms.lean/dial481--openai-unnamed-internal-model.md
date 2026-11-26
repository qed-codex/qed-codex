---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ArrayUpdatePrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArrayUpdatePrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ArrayUpdatePrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving access and update of packed arrays

The instruction tables have eight Boolean stacks. The record index and width
are unary stack data, so neither value affects the finite program control.
Stack 7 saves the preceding records in reverse order and restores them after
the selected record is read or replaced.


### `saveRecordCmd`

 Save one runtime-width record on stack 7, consuming neither the width nor
the existing saved records. 

### `saveBeforeCmd`

 The index is consumed; the width is preserved. 

### `readSelectedCmd`

 Copy the selected record in forward order onto stack 1, preserving the
array suffix on stack 0. 

### `replaceSelectedCmd`

 Replace the selected record by the equally wide word in stack 1.
The replacement word itself is preserved. 

### `readCmd`

 The full access command restores all preceding records after reading. 

### `replaceCmd`

 The full update command restores all preceding records after replacement. 

### `readProgram`

 The compiled access program has 38 labels for every runtime width/index. 

### `replaceProgram`

 The compiled replacement program has 44 labels for every runtime width/index. 

### `readProgram_trace`

 Complete execution, including the final halt. 

### `replaceProgram_trace`

 Complete execution replaces exactly one record and preserves its source word. 

### `readStacks_frame`

 This frames the complete array, width, and all four scratch stacks. 

### `replaceStacks_frame`

 This frames the replacement word, width, and all four scratch stacks. 

### `replaceStacks_records`

 In record-list notation the resulting array has exactly the specified
replacement, with the entire lists of preceding and following records intact. 

### `readProgram_primitive`

 The separate verified compiler gives an actual binary-machine execution.
Its multiplier depends only on this fixed program, not on the array data. 
