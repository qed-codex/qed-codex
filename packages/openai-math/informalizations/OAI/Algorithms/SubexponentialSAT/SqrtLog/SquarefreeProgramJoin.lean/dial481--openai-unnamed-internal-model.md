---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramJoin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramJoin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SquarefreeProgramJoin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A single finite primitive program joins encoded sparse indices. Unary
exponents are added by scanning their fields; support bits are unioned by the
fixed OR scanner. The complete output is reversed for direct record emission. 

### `indexJoin_trace`

 Actual primitive execution, with an exact count linear in key size. 
