---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafOuterProgramParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual outer-leaf parameter stage: input copies, native arithmetic,
output copies, and complete worker cleanup, with every command charged. 

### `WorkerEmpty`

 All 768 reusable worker stacks are empty. 

### `Metadata`

 Persisted search metadata. The seven indexed values are D,t,tD,d,r,rD,N. 

### `parameters_eval`

 Native parameter preparation on the actual outer-leaf machine. Its bound
includes input copies, arithmetic and unary generation, output copies, and
clearing every worker stack and register. No prepared-metadata premise occurs. 
