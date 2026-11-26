---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadIncrementalSequential.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadIncrementalSequential.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadIncrementalSequential.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Heads-first sequential ABI for the incremental physical head scorer. 

### `sequentialHead_decomposition`

 The exact factor is two times q^4, where q is the word-alphabet length.
The prefix is the actual reversed fixed-word store; its order does not affect
the sum. The common constant is not an input to the physical scorer. 

### `sequentialHead_factor_constant`

 At the factor stage there is no candidate-dependent head contribution. 
