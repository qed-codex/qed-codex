---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-table outer Hermite traversal for arbitrary coefficient width.
Only the arithmetic middle is parameterized; this module charges all input
copying, node/jet transport, indexing, iteration and final cleanup. 

### `controller_run`

 Join physical initialization, ordered traversal and final cleanup. The
sole remaining service premise is the arithmetic middle's actual execution
on each exact loaded state, for the binary exponent produced by initialization. 
