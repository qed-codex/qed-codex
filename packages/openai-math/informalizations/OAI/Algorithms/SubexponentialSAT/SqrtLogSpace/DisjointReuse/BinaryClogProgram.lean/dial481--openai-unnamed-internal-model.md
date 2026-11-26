---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryClogProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryClogProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryClogProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual floor and ceiling logarithm bit programs, without packing or schedule imports. 

### `trimTail`

 Consume leading zeroes and the first one of a most-significant-first word. 

### `log2_value_append_true`

 A most-significant one followed by `m` bits has binary logarithm `m`. 

### `trimProgram`

 Four low bits are discarded; the two read registers are then cleared. 

 ## Concrete input reversal 

 ## Reindex and call the checked binary word-length counter 

### `log_correct`

 Actual fixed-table logarithm program, correct for arbitrary padded words. 

### `logSucc`

 The floor binary logarithm plus one, with zero mapped to one. 
