---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One finite instruction table for arbitrary dynamic coefficient degree,
ring precision, node count, and jet order. All such parameters reside on
input tapes. The scalar and polynomial services here are concrete programs. 

### `localCode`

 Fixed local correction producer, with native scalar and array services. 

### `middle`

 Fixed arithmetic stage used by every outer-node iteration. 

### `command`

 Cache preparation, physical initialization, node traversal, and cleanup. 

### `program_run`

 The final compilation contributes exactly the ordinary return step. 
