---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact runtime parameter semantics. Every definition below uses natural
arithmetic; the executable refinements are separate from these specifications.
The original ambient dimension is retained through high-incidence branching. 

### `Guard`

 All runtime guards are integer comparisons. Spectral feasibility follows
from the proved schedule and is never tested by a real-number oracle. 

### `guard_hermite`

 Division plus one gives strictly more Hermite conditions than the degree. 
