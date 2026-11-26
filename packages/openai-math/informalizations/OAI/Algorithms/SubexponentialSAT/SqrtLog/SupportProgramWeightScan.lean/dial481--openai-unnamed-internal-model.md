---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramWeightScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramWeightScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramWeightScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed finite bit program testing a mask's weight against a unary budget.
Both the mask and the budget are runtime stack data. 

### `core_eval`

 The inner scan consumes one budget token for each true bit, even after
budget exhaustion. No machine instruction computes a population count. 

### `command_eval`

 Actual fixed-code execution; the last register reports strict weight bound. 
