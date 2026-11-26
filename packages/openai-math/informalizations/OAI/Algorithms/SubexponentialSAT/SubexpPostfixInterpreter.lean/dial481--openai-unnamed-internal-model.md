---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPostfixInterpreter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixInterpreter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixInterpreter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite postfix interpreter with linked arithmetic services

The interpreter contains the concrete tag dispatcher and literal loader, two
initialization instructions, and the supplied finite arithmetic instruction
tables. Arithmetic correctness is required as a local Boolean-machine trace
contract; an arithmetic operation is never added to the instruction language.


### `cfg`

 Scratch stack 3 is empty. Additional stacks carry the fixed arithmetic
context, including empty scratch slots and persistent ring parameters. 

### `program`

 A finite table, with actual jumps into and out of both arithmetic services. 

### `push_trace`

 The literal loader and all dispatcher transitions are the previously
checked instructions, relocated into this finite program. 

### `bootProgram`

 The empty operand-list marker is written by two real instructions. 

### `Implements`

 The service contract is a trace of supplied finite Boolean instructions.
The fixed context is preserved, so it may contain modulus and width data. 

### `costs`

 Costs are the proven literal trace and actual arithmetic-service bounds,
plus the thirteen dispatcher transitions and one service-call jump. 

### `compile_runsIn`

 The loop invariant includes the untouched code suffix, the complete operand
list, matching unary depth, and the unchanged arithmetic context. 

### `complete_runsIn`

 Complete execution includes writing the initial list marker, all compiled
instructions, detecting EOF, and executing the actual halt. Arithmetic context
is supplied once and preserved. 
