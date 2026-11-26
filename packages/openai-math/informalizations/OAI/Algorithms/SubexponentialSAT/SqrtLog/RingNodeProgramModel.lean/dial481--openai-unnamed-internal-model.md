---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingNodeProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The physical radix generator emits precisely the coefficient encoding of
nodes in the actual supplied-polynomial unramified ring. 

### `nodeCode`

 A fixed-width coefficient encoding of a base-three index. 

### `nodeCode_decode`

 The physical words decode to the same nodes used by interpolation. 

### `row_command_eval`

 Public one-row hook for callers which frame or process each generated
node before continuing their own loop. Both input masters are preserved. 

### `generated_residue_injective`

 The generated nodes have pairwise distinct, nonzero residues. 
