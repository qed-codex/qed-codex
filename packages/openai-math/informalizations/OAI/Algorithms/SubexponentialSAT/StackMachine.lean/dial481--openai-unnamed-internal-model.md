---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StackMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


Actual primitive tape programs for encoded stacks. Every instruction below is
one move or one write of `Computation.PrimitiveMachine`; the measured traces
are derived from that transition function.


### `program`

 A completely specified finite-control primitive program. Its last control
state is a return boundary; executing once more halts with `false`. 

### `program_trace`

 Exact, rather than annotated, cost of the straight-line primitive program. 

### `dataTape`

 All cells left of this representation are blank. There is no extra binary
sentinel, so a width-one Boolean code agrees with the actual raw input tape. 

 Reindexing a genuinely finite controller changes no primitive actions. 

### `controlStep_write_self`

 A finite-control dispatch may preserve every tape by writing back the
single cell that its transition actually observes. This still costs one step. 

 A block reader uses one right move per bit, stores the observed bit in its
finite control, then performs the same number of left moves. 

### `reader`

 This finite machine reads a fixed number of cells and restores the head. 

 Connecting the physical routines to the fixed alphabet encodings. 

### `popSymbol_trace`

 Includes empty-stack pop: traversing blank cells leaves the canonical
empty tape unchanged. 

### `registerBits`

 A function on a fixed finite register space; not an unbounded list read. 

### `decode_read_registers`

 The fixed block reader's final registers determine the exact source top
symbol, including `none` for an empty stack. 

### `decode_registers`

 Decoder-independent form, allowing the raw width-one input code and the
other work-stack codes to coexist in a single simulator. 

### `readSymbol_trace`

 One actual primitive reader run, together with the correctness of the
finite-control decoding of its output registers. 

 Inlining into a larger finite controller. The hypotheses below are
single-instruction transition-table equations, not assumed execution bounds.
They allow the final local control index to denote any caller continuation. 
