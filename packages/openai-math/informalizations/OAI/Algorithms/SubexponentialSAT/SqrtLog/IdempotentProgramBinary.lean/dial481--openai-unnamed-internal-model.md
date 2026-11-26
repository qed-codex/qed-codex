---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramBinary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramBinary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramBinary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Negation through multiplication by a cached negative unit. This permits
the native implementation to use only addition and multiplication services. 

### `minusOneRun`

 This array is constructed once and cached on the native constant port. 

### `binaryArrayLift_correct`

 The seven-register instruction sequence remains valid when its negation
instruction dispatches to the multiplication service with the cached unit. 
