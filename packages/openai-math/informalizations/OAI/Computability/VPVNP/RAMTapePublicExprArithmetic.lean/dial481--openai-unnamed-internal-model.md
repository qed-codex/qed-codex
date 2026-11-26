---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical word operations for the length-only public expressions

All arithmetic uses the fixed RAM word kernels. Natural subtraction tests
the unsigned order first, since the expression language truncates at zero.
Powers of two shift a literal unit and constant division uses the physical
word divider.


### `packed`

 Represent a natural number as a word by reduction modulo two to the word width. 

### `geometryNat`

 The four geometry inputs in register order, namely input length, site address width, bucket
capacity, and RAM word width. 

### `geometryWords`

 Encode the selected geometry parameter at the RAM word width. 

### `load`

 Copy one geometry word into an arithmetic register. 

### `subtract`

 Compare unsigned operands and return zero on underflow, otherwise compute their word
difference. 

### `Arithmetic`

 Binary operations of the public expression language, namely addition, truncated
subtraction, and multiplication. 

### `Arithmetic.eval`

 Interpret the binary operation on natural numbers, with subtraction truncated at zero. 

### `Arithmetic.code`

 Compile the binary operation to a word routine, using an unsigned comparison for truncated
subtraction. 

### `ConstantOp`

 Unary public-expression operations that need an auxiliary literal, namely division by a
fixed natural and raising two to a power. 

### `ConstantOp.literal`

 The auxiliary literal loaded for a constant operation, either its divisor or the unit to
shift left. 

### `ConstantOp.eval`

 Interpret the fixed-divisor or power-of-two operation on a natural input. 

### `ConstantOp.code`

 Load the auxiliary literal, then divide the destination word or shift a unit left by its
value. 
