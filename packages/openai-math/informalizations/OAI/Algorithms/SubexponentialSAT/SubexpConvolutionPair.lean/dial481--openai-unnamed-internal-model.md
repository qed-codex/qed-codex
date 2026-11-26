---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPair.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One actual product-and-accumulate step for packed jet convolution

The global state has sixteen Boolean registers and 256 Boolean-word stacks.
The multiplier occupies the fixed high bank beginning at 128. Its result is
moved, with order preserved, to the low-bank jet-cell accumulator service.


### `Ready`

 Readiness is a concrete assertion about the current tapes and encoded
array. The operand, coefficient, and index values remain runtime data. 

### `command_eval`

 Actual product, order-preserving transfer, and packed-cell accumulation.
Only the two consumed operands and the selected accumulator cell change. 

### `run_value`

 The pair service as an actual halted finite bit program. 

### `primitive_value`

 The same concrete routine in the primitive machine model. The compiler
overhead is a fixed constant because the pair program is fixed. 
