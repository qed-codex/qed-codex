---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticPowerMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPowerMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPowerMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary powering on a bit stack

For every exponent bit the machine squares its current packed accumulator.
A set bit triggers a second multiplication by the preserved packed base.
Both uses of the multiplier enter and return with its entire workspace clean.


### `multiplyFrom`

 Copy the selected source to the consumed operand and run the reusable multiplier. 

### `powerMachine`

 Consume the exponent in high-bit-first order, squaring at every bit and multiplying by the
base for each set bit. 

### `bitCap`

 Step bound for processing one exponent bit, allowing both a square and a multiplication by
the base. 

### `powerMachine_runs`

 The finite powering control consumes every bit of its input stack. 

### `power_runs`

 The canonical binary expansion computes the vector power. 

### `power_word_runs`

 A most-significant-bit-first exponent may retain its leading zero bits. 

### `power_zero_runs`

 A zero base and a zero initial accumulator stay zero, including the empty exponent. 
