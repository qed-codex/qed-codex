---
{
  "module": "OAI/Computability/VPVNP/PairNativeOperandBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native register computation of the compressed pair's static operands

The first twelve registers belong to the geometry and logarithm kernels.
Expression registers follow those registers in increasing order. Computing
a right operand one register higher leaves the left operand available for
the arithmetic instruction.


### `registerCount`

 Size of the operand register bank, with twelve fixed registers followed by temporary slots
numbered from zero through `r`. 

### `Code`

 Native operand flows with temporary slots up to `r` and access to the eleven public
pair-stage words. 

### `fixed`

 Locate a geometry or logarithm register at the same index in the enlarged operand bank. 

### `fixedEmbedding`

 The injective register map used to lift executions of twelve-register routines into the
native operand bank. 

### `temp`

 Locate a temporary operand register after the twelve fixed registers, reducing the slot
index modulo `r+1`. 

### `words`

 The six input words shared with the tape operand evaluator, encoding length, address width,
bucket size, word width, prefix length and packed prefix value. 

### `inputSlot`

 Register assignment for the six operand inputs in logical order. The bucket precedes the
word width in that order and occupies register 7. 

### `inputReg`

 Locate the fixed register holding logical input `i` in an operand bank with temporary slots
up to `r`. 

### `Ready`

 The six designated registers already contain the encoded geometry and prefix words required
by operand evaluation. 

### `Keeps`

 The output agrees with the input on registers from 4 up to but excluding `12+base`,
protecting the fixed inputs and all earlier temporary results. 

### `Eval`

 From any ready bank the code produces the word for `v` in temporary slot `base` within the
tick budget, preserves the protected registers and returns the original memory. 

### `literal`

 Build the literal `n` in the destination register by loading one into scratch register 0
and adding that unit `n` times from zero. 
