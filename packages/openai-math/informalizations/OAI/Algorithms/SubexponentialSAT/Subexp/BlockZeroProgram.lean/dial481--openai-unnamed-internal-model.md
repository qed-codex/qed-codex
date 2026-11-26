---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockZeroProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockZeroProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockZeroProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed bit program testing whether all payload bits in a sequence of
frames are zero. Frame delimiters are ignored; no scalar arithmetic is hidden
inside this program. 

### `skipProgram`

 Consume a runtime number of complete scalar frames. Stack 0 is the
unary count and stack 1 the framed scalar stream. 

### `classifyProgram`

 Combine the four verified zero predicates. Inputs are zero(y),
zero(coefficients), zero(tail coefficients), zero(M*y); output is register 4. 
