---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramReady.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramReady.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ReconstructionProgramReady.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Static readiness obtained from the physically prepared input tapes.
No arithmetic, program trace, or canonicality hypothesis is hidden here. 

### `emptyPorts`

 Exactly the empty physical ports used by the two native arithmetic banks
and the dense base-word adder. Ports5/10 are populated by the paid entry code. 

### `base`

 Definitionally the same store as `NativeState.arithmeticBase`. 

### `lowFrame`

 The six unmodified low frame cells are unrestricted input bytes. 
