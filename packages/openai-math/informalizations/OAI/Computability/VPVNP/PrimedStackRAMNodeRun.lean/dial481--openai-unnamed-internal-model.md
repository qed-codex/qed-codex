---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMNodeRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNodeRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMNodeRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native execution of the complete preorder-node table

The evaluator below reads the same finite word encodings as the linked loops
and retains the unused choice suffix for the surrounding program. A missing
choice or failed guard aborts the native execution at every sufficient fuel.


### `Output`

 Result of a successful RAM segment, including its event trace, final registers and memory,
and the choice bits available to the continuation. 

### `Output.events`

 RAM events in execution order, including ticks, choices, and memory probes. 

### `Output.regs`

 Register contents passed to the next segment. 

### `Output.mem`

 External memory after the segment has executed its writes. 

### `Output.bits`

 Suffix of the choice stream left for the next segment. 

### `Output.prepend`

 Prefix a successful segment’s trace with the events of an earlier segment. 

### `Kernel`

 Partial execution of a RAM segment from public words, a state word, registers, memory, and
a choice stream. Success returns the trace and the state needed by the continuation. 

### `lineKernel`

 Execute a straight-line list of opcodes and carry the choice stream through to the
continuation. 

### `guessKernel`

 Consume one word’s worth of choice bits, record the guessing loop’s trace, and update its
three registers. A short stream causes rejection. 

### `seqKernel`

 Run two kernels in order, passing the first result’s registers, memory, and unused bits to
the second and appending their traces on success. 

### `eqKernel`

 Compare two registers to select a kernel and prefix its successful trace with the tick
spent on the comparison. 

### `Refines`

 Bounded refinement for every containing table and every continuation. 

### `leafKernel`

 Guess the terminal position into register 2, then run the leaf checks and record its
production. 

### `binaryKernel`

 Guess the split and the two child states into registers 2, 3, and 4, then execute the
binary production and stack updates. 

### `nodeKernel`

 Pop the pending frame, compare its degree with zero, and run the leaf or binary kernel
selected by that comparison. 

### `node_refines`

 Refinement of the complete native node. The continuation receives the
true post-memory and remaining bits. 
