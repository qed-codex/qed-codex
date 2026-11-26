---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketProgramArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed binary conditional-add kernel for exact offset signatures. 

### `choiceAdd_eval`

 Port0 is the common offset W, port1 is W+A, port2 is the accumulator,
port3 receives the sum. The selected assignment bit is register0. All input
and scratch stacks are preserved; the returned word is genuine binary data. 

### `offsetSignature`

 Offset summation is exactly the integer signature translated by hW. 
