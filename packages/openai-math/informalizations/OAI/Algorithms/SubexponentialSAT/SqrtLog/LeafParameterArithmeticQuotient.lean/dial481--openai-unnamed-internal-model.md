---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticQuotient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticQuotient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticQuotient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A source-preserving floor quotient call using the audited finite binary
long-division program. Operands are runtime padded Boolean words. 

### `quotientAt_eval`

 The only final stack change is the quotient output. All work and both
source words are preserved, including arbitrary leading-zero padding. 
