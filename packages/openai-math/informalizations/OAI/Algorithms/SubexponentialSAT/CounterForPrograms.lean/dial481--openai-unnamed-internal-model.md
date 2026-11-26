---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CounterForPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterForPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterForPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite binary-counted callback loop

The loop bound lives on a little-endian Boolean stack.  Fixed finite subroutines
perform zero testing and decrement, and an arbitrary fixed command is the loop
body.  The body may overwrite every register.  All measured evaluations below
compile to traces of a finite instruction table; proof-level state embeddings
are never used as executable instructions.


### `Ports`

 Fixed ports, independent of the represented counter value. 

### `OutsideEq`

 State invariants may ignore every register and both controller stacks. 

### `loopCmd`

 The syntax is independent of the counter word and its value. 

### `Visits`

 Each recorded cost comes from a real execution of the fixed callback. 

### `BodySpec`

 A bound on callback costs, indexed by the number of preceding calls. 

### `budgetSum`

 Sum of the successive callback budgets; a specification, not program data. 

### `Visits.bounds`

 The recorded callback count is exactly the input value, and decrement
preserves the width of every positive counter representation. 

### `visits_exists`

 Every total callback satisfying its invariant has a measured loop trace.
The induction is on the value of the stack data, not on the finite control. 

### `for_correct_measured`

 Complete measured execution, including an explicit record of the actual
callback costs.  The overhead is linear in the count times encoded width. 

### `for_correct`

 Convenient interface with the sum of user-supplied callback budgets. 

### `size_forCmd`

 The control table grows only with the fixed callback program. 

### `program_correct`

 The counted loop's measured evaluation is an actual halted finite-table
trace, with one additional halt instruction. 

### `primitive_correct`

 The existing verified compiler turns the same concrete loop into a
primitive finite-alphabet machine, with its fixed compilation overhead. 
