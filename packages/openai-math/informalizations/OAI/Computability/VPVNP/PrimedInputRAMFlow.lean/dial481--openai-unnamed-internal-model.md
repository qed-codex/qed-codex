---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMFlow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Structured finite jump tables for the auxiliary burst RAM

A straight-line instruction, a branch, a sequence and a loop all have
finite sets of instruction labels. A loop introduces one test and a back
edge to that test. Neither the width of a word nor the number of iterations
affects the table size. Compilation maps local labels to ordinary bounded
program counters of the fixed burst RAM template.


### `Flow`

 Fixed program text. A test reads two register words. `branch` makes one
binary choice even when its two continuations have identical effects. 

### `Jump`

 Instruction addresses are local labels. `none` designates the common
exit and can later be linked to the next block or a return instruction. 

### `Jump.map`

 Relabel the successor targets of a jump while preserving its instruction, operands and
choice branches. 

### `Jump.emit`

 Compile a jump with bounded program counters to a burst instruction, sending failed guards
to the supplied rejection address. 

### `Label`

 Local program-counter type. In a compound block the sum tags identify
the instruction's enclosing branch, body or test. 

### `length`

 Number of labeled instructions in the structured program, counting the tests of branches
and loops. 

### `labels`

 Numerical labels for the fixed instruction table. 

### `entry`

 First label executed when entering the structured control-flow program. 

### `code`

 The complete control graph. Body exits of a loop are wired back to its
test; exits of the first member of a sequence enter its second member. 

### `pc`

 Bounded counter of a real instruction label. 

### `exitPC`

 Program counter reserved for normal exit from the structured code. 

### `rejectPC`

 Program counter reserved for rejecting a failed guard in the structured code. 

### `target`

 Translate an optional local successor to its compiled program counter, mapping the absent
successor to normal exit. 

### `template`

 The table emits exactly one finite private-RAM instruction per label,
plus a normal exit and a rejecting exit. 

### `Linked`

 A block may occupy labels in a larger table. Its local normal and bad
exits need not be the enclosing table's own exits. 
