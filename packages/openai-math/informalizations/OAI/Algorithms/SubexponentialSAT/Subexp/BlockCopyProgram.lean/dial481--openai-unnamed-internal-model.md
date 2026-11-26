---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockCopyProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockCopyProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockCopyProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit program for copying a local table into every block

Stack 0 contains the encoded local table, stack 1 the output suffix, stack 2
is empty scratch, and stack 3 contains the unary number of blocks.  The same
finite program handles all table lengths and block counts.  It preserves the
local table and prefixes one copy per block to the output.  This is the compact
block-major representation of the repeated local basis/complement arrays;
scattering their coordinates through the packing is a separate operation.


### `copies`

 An encoded table repeated in block order. 

### `loopState`

 The loop state includes a pending copy when the active flag is true. 

### `program`

 Twelve control labels, independent of the runtime block count/table size. 

### `loop_eval`

 Exact loop cost: every copied bit executes the already verified copy
routine, and every iteration includes the counter pop and loop guard. 

### `program_trace`

 The compiled finite Boolean-stack machine has the claimed exact trace. 

### `program_primitive`

 The verified compiler supplies a run of the fixed binary machine. Its
constant overhead is independent of both input lengths. 

### `trace_bound`

 In particular the global work is linear in the block count and encoded
local-table length; neither changes the program's finite control. 
