---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native dense-polynomial arithmetic with arbitrary runtime ring
coefficient width. Native ring multiplication and every convolution scan are
included in the cost, and the output has the usual polynomial meaning. 

### `nativeMulCommand`

 One finite instruction table, independent of all dimensions. 

### `nativeMulBudget_polynomial`

 An explicit polynomial upper bound for the fully native trace. 

### `nativeMulBudget_width`

 With nonempty coefficients, the bound is polynomial in the actual
serialized coefficient width W=degree*B and the runtime array length. 

### `native_mul_eval`

 Cached multiplication, with its local native ring contract discharged. 

### `modelTable`

 The cached multiplication table belonging to the supplied ternary model. 

### `model_mul_trace`

 Complete model-ring multiplication: one fixed native trace and the exact
truncated polynomial product under the model's coefficient decoder. 

### `native_mul_primitive`

 The compiler cost is a fixed multiplicative constant for this fixed
instruction table; arbitrary tape states are allowed at both endpoints. 
