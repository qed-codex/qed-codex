---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed bit program generates the power-of-two clearing denominator from
its unary exponent. The exponent is runtime data, never control-table size. 

### `powerCommand_eval`

 The output is the little-endian word for 2^q, prepended to its old tail. 
