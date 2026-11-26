---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramCacheWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramCacheWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramCacheWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid binary metadata for the integer entry cache. The centered interval
start on port46 is produced by `SubexpIntervalStartProgram.program`; its
semantic identification is `SubexpIntervalStart.value_eq_intervalStart`.
This stage preserves that word and the parameter table while forming Qr and
the sufficient scalar width 1+2*A*R+Q. 

### `code`

 Inputs r18, Q21, R29 and A46. Outputs Qr47 and cache width50;
48 and49 are paid temporary product words. 

### `budget_polynomial`

 A polynomial in actual padded input lengths pays every operation here. 
