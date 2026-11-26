---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpParameterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpParameterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpParameterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual finite programs for the growing packing parameters

Numbers are little-endian Boolean stacks, with leading zeroes allowed. The
programs below manipulate only bits and stacks; natural-number quantities in
their specifications and cost bounds are not machine registers.


### `trimTail`

 Consume leading zeroes and the first one of a most-significant-first word. 

### `log2_value_append_true`

 A most-significant one followed by `m` bits has binary logarithm `m`. 

### `atoms`

 Straight-line syntax for a fixed list of primitive operations. 

### `shiftFourOps`

 Four low bits are discarded; the two read registers are then cleared. 

 ## Consume a most-significant zero prefix and the leading one 

 ## Concrete input reversal 

 ## Reindex and call the checked binary word-length counter 

### `log_correct`

 Actual fixed-table logarithm program, correct for arbitrary padded words. 

### `doubleLogProgram`

 Two calls to the same finite logarithm table. 

### `parameterProgram`

 The entire `n -> s(n) -> u(n)` computation has 55 fixed control labels. 
