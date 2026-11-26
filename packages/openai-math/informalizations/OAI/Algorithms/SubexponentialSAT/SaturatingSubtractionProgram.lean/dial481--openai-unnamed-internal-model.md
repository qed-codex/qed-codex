---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SaturatingSubtractionProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SaturatingSubtractionProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SaturatingSubtractionProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving saturating binary subtraction

Eight Boolean registers and eight stacks suffice. The two operands remain
on stacks 0 and 1; stack 2 receives their natural-number difference and
stacks 3 through 7 return empty. Copied concatenations supply a common
padding shape without computing a numeric width. The final borrow bit
controls a real clear loop. Every copy, pad, subtraction, and clear is
charged in the linear instruction bound.


### `command_eval`

 Both numeric operands are preserved. The sole output is natural-number
subtraction, and its representation length is bounded by the input lengths.
The instruction allowance includes the final compiled halt. 
