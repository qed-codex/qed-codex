---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingWeightProgramBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingWeightProgramBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingWeightProgramBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed binary computation of the reciprocal-error packing coefficients.
Sources 0..3 hold n,s,M,r. Outputs 4,5 hold n²s² and 8M²r².
Ports 6,7 and 8..12 are temporary products and arithmetic scratch. 
