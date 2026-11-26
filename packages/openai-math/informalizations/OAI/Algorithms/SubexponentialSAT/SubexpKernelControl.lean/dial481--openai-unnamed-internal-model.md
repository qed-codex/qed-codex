---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpKernelControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKernelControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKernelControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed controller constructing the separated postfix source

The input contains literal payloads and the three nested lists of blocks,
color groups, and terms.  The controller only parses frames, copies bits,
and emits postfix tags.  It has no arithmetic callback and never builds a
Cartesian product of the inner lists.  Three unary stacks hold the pending
right-fold operators, so the emitted source has exactly the association of
`SubexpAlgorithm.momentExpression`.


 ## Fixed source-constructor control 

### `popTag`

 Every list length is data on stack 0. 

### `captureFrame`

 Copy an already-framed literal without changing its coefficient encoding. 

### `appendPayload`

 The factor expression was constructed by the factor source compiler. 

### `scanLoop`

 The fixed body consumes exactly one unframed payload, then the next marker
is read. The same control table handles every list length. 

### `kernelProgram`

 A concrete finite instruction table; no arithmetic or traversal service
is passed as an argument to the constructor. 

 ## Concrete machine states and elementary traces 

 The following induction rule accounts for actual executions of the fixed
payload body. Its premises will be proved for `termBody`, `groupBody`, and
`blockBody`; the exported whole-controller statement has no callback argument. 

### `kernel_eval`

 Exact execution of the complete three-level source constructor. All
service bodies are the concrete parser, literal emitter, and bit instructions
appearing in `kernel`; no callback correctness is supplied by this theorem. 

### `scanCost_le_input`

 The traversal count sums individual payload costs. No product of inner
list lengths occurs in the actual loop bound. 

 ## Forward-output service boundary 

### `serviceState`

 Data boundary with cleared Boolean registers and explicit constant ports. 

### `sourceConstructor_size`

 The program's control table is fixed independently of every input size. 

### `program_trace`

 The fixed source program emits the interpreter's exact postfix input,
preserving the supplied zero/one payloads and clearing its work ports. 

### `program_runsIn`

 The fixed finite source program has a quadratic upper bound in the
combined encoded data size, including both reusable constant payloads. 
