---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GatherProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GatherProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GatherProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed program gathering runtime-selected rows

The packed assignment is on stack 0 and its unary row width on stack 3.
Stack 8 contains `ProgramEncoding.encodeRecords` of unary index words.
The program preserves the assignment and width and writes the selected rows,
in plan order, to stack 1. All widths and indices are stack data.


### `lookupPort`

 The existing eight-stack persistent lookup occupies the first eight ports. 

### `callback`

 The parser supplies a reversed unary index. Only its length is read.
Each selected row is reversed into the growing accumulator on stack 9. 

### `callbackCost`

 An exact per-record callback budget in actual bit-program instructions. 

### `traceCost`

 The concrete trace budget, including the final reversal and halt. 

### `command_eval`

 Execution of the single fixed command. The only input hypotheses are
uniform row widths and validity of the runtime plan indices. 

### `program_run`

 The full, halted trace of the generated finite instruction table. 

### `traceCost_le_serialized`

 A polynomial bound in actual serialized width and plan data. In particular,
even a zero-width array needs no unencoded row-count parameter in the bound. 

### `primitive_run`

 Refinement to the project's primitive binary-machine transitions; the
compiler overhead is a constant of this fixed program. 
