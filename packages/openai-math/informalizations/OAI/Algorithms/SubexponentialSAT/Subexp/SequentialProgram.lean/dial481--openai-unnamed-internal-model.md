---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SequentialProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SequentialProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SequentialProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed sequential assignment control

The loop counter, processed index, word width, alphabet, and assignment are
runtime stack data. A fixed score-building command is composed with the
verified minimum selector and preserving packed-array operations.


### `selectAndUpdate`

 The selected unary index is consumed by the alphabet lookup. The
processed index is copied before the assignment update consumes its copy. 

### `wordUpdate_eval`

 A preserving alphabet lookup followed by a preserving assignment write.
All indices and widths are runtime unary stacks. 

### `Memory`

 All mathematical values in this invariant describe concrete packed
arrays or lengths of concrete unary stacks. 

### `HighState`

 Runtime read-only tables and restored scratch outside the controller ABI. 

### `StepRefines`

 A compositional contract for the displayed, fixed step code. Its
premise is an actual instruction execution, never an atomic score oracle. 

### `program_runsIn`

 Every step is supplied by the actual composed instruction table. The
complete fixed loop produces the natural-choice assignment in packed form. 
