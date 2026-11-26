---
{
  "module": "OAI/Computability/VPVNP/PairNativeOperandArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native word arithmetic for the pair's private operand bank 

### `Arithmetic`

 The four binary operations available when combining two native operand values. 

### `Arithmetic.value`

 Natural-number interpretation of the binary operand operations, using truncated subtraction
and integer division. 

### `Arithmetic.op`

 Instruction flow that combines `dst` with `rhs` in place. The subtraction branch writes
zero when the right operand exceeds the left. 

### `combine`

 Run the two operand flows in order, then combine the values in temporary slots `base` and
`base+1` and leave the result in `base`. 

### `pow2`

 Evaluate the exponent at `base` and replace it with a left shift of one by that exponent. 
