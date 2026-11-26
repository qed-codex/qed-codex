---
{
  "module": "OAI/Algorithms/SubexponentialSAT/PositiveWordProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PositiveWordProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PositiveWordProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A primitive implementation of the final positivity test

The same seven-label program scans every little-endian Boolean word.  It
returns true exactly when the encoded natural number is positive.  It may
leave an unused suffix after finding a one bit; only the output head is read
by the already verified primitive compiler.


### `positive_eq_true_iff_mem`

 The same concrete scan is an OR over an explicitly materialized list of
leaf answers. Construction of that list is a separate phase. 

### `primitive_outputs`

 A genuine primitive-bit execution, not an arithmetic-operation estimate. 
