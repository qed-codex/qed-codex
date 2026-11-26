---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Straight-line word code for the preorder counter

Each operation emits one instruction of the finite burst machine. Guards jump to
the program's reject instruction. The same block may occupy any prescribed
sequence of program counters, so stack and counter operations can be inserted
between the loops which read nondeterministic grammar choices.


### `Op`

 Operands of a straight-line instruction, with a two-bit literal format. 

### `Op.emit`

 Translate one line using the successor and rejecting program counters. 

### `Regs`

 Contents of the `r` private registers, each holding a width-`w` word. 

### `Cont`

 Continuation that takes the current register file and external memory and returns an
optional burst report. 

### `Op.effect`

 Register, external-memory and event semantics of one line. 

### `Op.run`

 Execute one straight-line operation, pass the resulting registers and memory to the
continuation, and prepend its event to a successful report. 

### `run`

 Execute the straight-line block in list order before invoking the continuation with its
final registers and memory. 

### `trace`

 Evaluate a whole block, retaining the post-state for a subsequent block. 

### `trace_append`

 Concatenation runs the two blocks with the actual intermediate registers and memory. 

### `Op.destination`

 Registers available to surrounding blocks when no line names them as its destination. 

### `Contains`

 Occurrence of a block inside a possibly larger, looping instruction table. 

### `Contains.execute`

 Native execution consumes one instruction of fuel per line and agrees
with the block semantics on registers, external memory and every event. 

### `template`

 Compile a whole block into a fixed table with a return and a reject instruction. 

### `template_contains`

 The compiler places the complete block before its two terminal instructions. 

### `execute_template`

 Start at the entry of the actual opcode table. Registers may be supplied
by a preceding part of the same call. A standalone call supplies all zeros. 
