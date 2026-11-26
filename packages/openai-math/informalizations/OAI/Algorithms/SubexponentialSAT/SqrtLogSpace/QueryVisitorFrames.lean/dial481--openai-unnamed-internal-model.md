---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Static register frames for the concrete tuple visitor. The frame follows
from the actual instructions and embeddings, including the ambient overlay.
The retained tuple-controller flags require no save stack. 

### `replay_not_mem_writes`

 Replay overwrites both retained traversal copies on every pass. 

### `tupleMultiply_not_mem_writes`

 The original multiplication runs inside its actual low-register map. 

### `tupleMultiply_register_frame`

 Every source prefix of the actual multiplier retains the caller flags. 
