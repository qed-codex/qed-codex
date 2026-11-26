---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed preparation of candidate tables, split dimensions, and coefficient
tuples for the universal block search. All three dimensions are runtime data. 

### `inputState`

 Runtime inputs occupy alphabet 1, table depth 8, and two explicit copies
of the unary vector dimension on 9 and 21. 
