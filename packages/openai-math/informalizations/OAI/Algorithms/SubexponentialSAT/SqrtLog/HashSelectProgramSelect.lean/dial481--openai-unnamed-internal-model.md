---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSelect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSelect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramSelect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Unseeded binary argmin. The first mass evaluation, first score copy and
all remaining candidate evaluations are paid by the same finite program. 

### `best_scored`

 The machine's cached binary scores implement the pure strict argmin. 

### `selectBudget_callback`

 Every candidate, including every failed trial, contributes its callback
bound once. The extra term pays parsing, binary comparisons and queue control. 
