---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SelectorMapProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorMapProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorMapProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed loop applying the selected-index map to query records

The selector uses ports 0--5.  Port 6 is the framed query cursor, port 7
preserves the raw key/payload table, and port 8 accumulates framed answers.
Answers are prepended, so the returned record list reverses query order.


### `program_trace_from`

 The fixed record loop invokes the proved callback for every query. Its
output is the selected payload list in reverse order, and the table survives. 

### `budget_bound`

 A polynomial bound in the literal serialized table and query lengths. 

### `selected_plan_trace`

 Reverse the input plan once to obtain selected indices in the original
head/slot order expected by the gather program. 
