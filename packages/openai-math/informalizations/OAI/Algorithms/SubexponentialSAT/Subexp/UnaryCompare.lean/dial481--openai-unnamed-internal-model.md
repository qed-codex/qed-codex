---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UnaryCompare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UnaryCompare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UnaryCompare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit program for exact conditional-score comparisons

The local conditional scores admit bounded natural numerators. Unary storage
is therefore already polynomial in the growing parameters. This module gives
an actual fixed finite instruction table comparing two stack lengths and
connects its measured execution to those conditional scores.


### `program`

 Compare stack lengths destructively. Register 3 receives `left ≤ right`.
The four registers, two stacks, and seven labels do not depend on the data. 

### `runs`

 The cost counts actual instructions, including the halt instruction. 

### `encode`

 A unary natural is represented only by its stack length. 

### `natural_primitive_runsIn`

 The proved generic compiler supplies an actual primitive-bit-machine run
from this two-stack input boundary. 

### `outputCommand`

 Reuse the comparison subroutine and expose its answer on the output
stack. The linker replaces the old halt with a return. 

### `output_primitive_runsIn`

 A real primitive-machine terminal answer at the prepared two-stack input
boundary. The overhead is a constant of the one fixed output program. 

### `conditional_score_runsIn`

 The fixed program compares the exact conditional scores. Its input size
and actual instruction count are polynomial in the growing parameters. 

### `conditional_score_primitive_runsIn`

 Primitive-machine execution of the same exact score comparison, with a
fixed compiler overhead independent of all layout parameters. 

### `conditional_score_output_primitive_runsIn`

 The primitive output bit is the order of the exact conditional scores. 
