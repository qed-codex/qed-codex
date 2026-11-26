---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ModularQuotientArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularQuotientArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularQuotientArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The quotient bits emitted by binary long division

These bit/list functions specify the output of the finite division program.
Each quotient bit is the complement of the actual subtraction borrow; neither
the recurrence nor the bit selector calls natural-number division.


### `divide`

 Return the little-endian quotient and padded remainder, in that order. 

### `quotientBit_step`

 One subtraction records exactly the multiple of the modulus removed. 

### `divide_identity`

 The division identity itself only requires words, including a zero modulus. 
