---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKeyCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKeyCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKeyCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source component: IdempotentApplyProgramMultiplierKey. 

 Construction and application of the U monomial by actual native instructions. 

### `uKey`

 The monomial U, with empty Boolean support. 

### `makeUKey_command_eval`

 The shape tape is preserved; the only resulting stack change is the new U key. 

### `shiftU_command_eval`

 The key-map call preserves its key and capacity tapes and all surrounding memory. 

### `uKey_stepBudget_le`

 The U key need not itself survive the truncation (in particular u may be 0 or 1). 

### `uKey_budget_le`

 A linear scan bound with no lower bound on the U truncation capacity. 
