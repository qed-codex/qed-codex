---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramHalf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramHalf.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramHalf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `halfValue`

 Integral half recurrence: h_0=1, h_(s+1)=3h_s-1. Thus 2h_s=3^s+1. 

### `halfRun`

 This computes the inverse of two modulo 3^t without dividing a natural
number or invoking an inverse oracle. It uses t iterations of four callbacks. 
