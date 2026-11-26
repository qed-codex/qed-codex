---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A denominator constructor consuming the actual ring-setup certificate.
The inverse-half fact comes from that executed setup, and the power is then
computed by the fixed native multiplication loop in the private bank. 

### `produced_command_eval`

 The actual per-query call after ring setup and interpolation. No
inverse-denominator word is an input: stack 728 starts empty and is filled by
an executed binary-to-ring lift followed by R-1 native multiplications. 

### `budget_polynomial`

 The storage cost is linear in the largest physically present word. The
remaining budget is the checked polynomial native denominator budget. 
