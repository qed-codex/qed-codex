---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowFactorLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowFactorLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowFactorLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual diagonal exclusion and factor-record production for a row. 

### `compareIndex_eval`

 Both unary words are copied before comparison; the original index words
and every surrounding stack survive the diagonal test. 

### `loop_eval`

 Every record is parsed and processed by the fixed callback. The statement
records all preserved stacks, not only the emitted factor list. 

### `output_reverse_indices`

 Descending traversal plus prepending restores the given ascending order.
The only discarded entry is the canonical unary word for the outer index. 
