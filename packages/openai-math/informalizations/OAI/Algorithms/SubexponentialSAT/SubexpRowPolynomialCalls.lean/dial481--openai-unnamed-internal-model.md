---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRowPolynomialCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPolynomialCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowPolynomialCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete dense-field arithmetic inside the framed row interpreter.
All hypotheses below describe encoded data, fixed-width operands, or empty
scratch stacks. The arithmetic traces are supplied by the actual published
addition and convolution programs. 

### `add_runsIn`

 The native add service receives the two parsed arrays and no semantic
oracle. Its output is reinserted into the original framed operand stack. 

### `mul_runsIn`

 Multiplication uses the statically relocated native bank, so persistent
source-cache data on 128--137 is untouched. All array lengths are runtime
data, and the service returns exactly D coefficient cells. 
