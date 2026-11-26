---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramMatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSearchProgramMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete prime-field matrix application used by both search predicates.
All row/column counts and operands are runtime data for the same 359-label
program. The format is the actual scalar-frame stream, not a free matrix
oracle. Input recoding is kept separate from this application theorem. 

### `matrix_apply_trace`

 The field result is connected to the exact bytes produced by the program.
The theorem includes parsing, every failed or successful arithmetic step,
the runtime row loop, and reversal into forward output order. 
