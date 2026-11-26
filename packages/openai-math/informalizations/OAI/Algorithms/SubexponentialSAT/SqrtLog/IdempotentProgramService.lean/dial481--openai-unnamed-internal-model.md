---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramService.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramService.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramService.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Lift the common 32-stack arithmetic ABI into the Newton machine and prove
that the source-preserving register wrapper has the exact specified effect. 

### `servicePorts`

 The nine added stacks hold four arrays, negative one, degree, copy scratch,
and the binary loop counter plus its scratch. 

### `ServiceContext`

 The low workspace at rest. No arithmetic input or output is present. 

### `registerService_eval`

 Any proved native add/multiply service can be wrapped without assuming
free copies or unbounded register access. The exact result overwrites target. 
