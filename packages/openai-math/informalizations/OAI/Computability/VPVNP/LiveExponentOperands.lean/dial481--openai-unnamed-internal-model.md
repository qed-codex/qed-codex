---
{
  "module": "OAI/Computability/VPVNP/LiveExponentOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public operands of the live exponent table

These five expressions are evaluated from the processor's public geometry.
The header scan and the pair subroutine refer to the very same bit and
counter buffers. The stage dispatcher sits below the header workspace.


### `operands`

 Public expressions for the incoming and outgoing digit arrays, increment counters, digit
width, and total digit count. 

### `words`

 Evaluate the exponent stage's five public address and size expressions as machine words for
the supplied geometry. 
