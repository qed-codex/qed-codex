---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Constant-control preparation of the padded radix and the final node stream.
The only supplied words are zero padding, binary Q, and unary d. 

### `prepareRadix`

 The second successful pop leaves `present = true`, reused for both pushes. 

### `preparedProgram_nodes`

 Physical generation of the exact reconstruction input ABI from runtime
sizes, including radix construction and every loop/control instruction. 

### `preparedProgram_lifted`

 Caller-independent relocation: every register and stack outside the fixed
workspace is framed by the checked lifting theorem. 

### `preparedProgram_control_size`

 The entire generator has a fixed control table, independent of t,d,Q. 

### `preparedProgram_primitive`

 The measured bit-program execution refines to the primitive machine. 
