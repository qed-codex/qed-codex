---
{
  "module": "OAI/Computability/VPVNP/CompressorBaseAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBaseAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBaseAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Fixed Macaulay reader advice at an admissible compressor length

The grammar checker stream, affine pin mask and field values, graded monomial
bounds and row counts are all chosen at the input length. The same bank serves
every coordinate query. Its height bound uses the reader plan fixed before the
prime and slice, including in characteristic zero.


### `plan_registers_fit`

 All three immutable row-decoder parameters fit in the plan's physical
address words, even when an equation block is empty. 

### `rawAdviceFintype`

 Finite enumeration of the ground field used to encode the Macaulay reader's affine pin
values. 

### `rawAdviceDecidable`

 Equality decision for elements of the ground field used in the fixed advice bank. 

### `compressorBaseBank`

 Actual immutable base matrix state before the first call. Its checker
parameters refer to the fixed equation types of both compressor templates. 

### `compressorBaseReady`

 The base advice stacks contain the equation data, modulus, affine pins and encoded pin
values for the chosen compressor instance. 

### `compressorBaseReady_length`

 The bound is uniform over the advised modulus and every ready state.
The original matrix reader's scratch registers need only satisfy its ready predicate. 
