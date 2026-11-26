---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StackRoutines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackRoutines.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackRoutines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-alphabet stack routines

This module records stack-state transformations and proves instruction traces
for concrete programs over Boolean stacks. The number of symbols in a stack is
runtime data; no growing alphabet is used.


### `clearStacks`

 Specification of emptying one stack. 

### `transferStacks`

 Specification of popping a source onto a destination. 

### `fanoutStacks`

 Specification of popping a source onto each of two destinations. 

### `copyStacks`

 Specification of a preserving copy, with the copied word prefixed to `dst`. 

### `clearResult`

 The exit state of the clear loop; only its read registers are clobbered. 

### `clear_trace_aux`

 Exact execution of the two-instruction clear loop. Local code equations
allow the routine to be placed inside any finite caller program. 

### `clearProgram`

 A complete concrete three-label clear program. Label `2` is its halt. 

### `transfer_trace_aux`

 A concrete transfer loop, with one pop, one branch, and one push per bit.
The final empty read and branch account for the additional two transitions. 

### `transferProgram`

 A complete four-label transfer program; label `3` is its halt. 

### `fanout_trace_aux`

 Pop one source and push its bits onto two destinations, using four actual
instructions per nonempty iteration. 

### `copy_trace`

 Preserving copy through one initially empty temporary stack. The source is
restored; its original word is prefixed in forward order to the destination. 

### `copyProgram`

 An eight-label program implementing preserving copy. Label `7` halts. 

### `reverseProgram`

 In-place reversal through two initially empty temporary stacks. The
program has ten fixed labels independently of the word length. 

### `halt_after_trace`

 A routine boundary can be turned into a terminating execution by executing
the caller's halt instruction, with exactly one additional transition. 
