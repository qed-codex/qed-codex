---
{
  "module": "OAI/Computability/VPVNP/EvaluatorChronologicalLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorChronologicalLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorChronologicalLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Chronological traversal of the evaluator digit table

For every digit column the finite control invokes the Frobenius routine,
initializes a label counter and scans the labels in order. Both counters live
on stacks, so the same control works at every width and every label count.


### `column`

 One column starts with Frobenius, then enumerates the label digits. 

### `traverse`

 The entry consumes one remaining-column mark per column. 

### `columnBudget`

 The elementary control allowance for one complete column. 

### `traverseBudget`

 The elementary control allowance for the entire digit schedule. 

### `column_realizes`

 Correctness of the column scan for callbacks with the indicated state effects. 

### `traverse_realizes`

 The complete scan first composes labels within a column, then composes
the columns chronologically. Both per-call bounds are independent of the indices. 
