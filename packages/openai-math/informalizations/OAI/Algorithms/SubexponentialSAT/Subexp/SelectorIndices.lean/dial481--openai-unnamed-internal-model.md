---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SelectorIndices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorIndices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorIndices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The encoded first-match selector implements the actual local read-plan
index map, using an explicit table and a unary query. 

### `scanBudget_selectionEntries_le`

 A uniform polynomial bound for the actual key scan. 

### `budget_selectionEntries_le`

 No exponent in this source-instruction bound depends on the parameters. 

### `selected_index_trace`

 This is a genuine instruction trace computing the selected current- or
candidate-row index, rather than a unit-cost abstract table lookup. 
