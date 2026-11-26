---
{
  "module": "OAI/Computability/VPVNP/CompressionProcedure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionProcedure.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionProcedure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composing exact compressor procedures

A procedure consumes a fixed number of lane coordinates and carries bounds
independent of the input widths and network order. Its execution tree
retains the exact local kernel at every substep. The position divisors
multiply under composition, as do the leading energy coefficients.


### `Procedure`

 Uniform cost and output bounds on an exact execution tree. 

### `Procedure.error`

 Nonnegative coefficient multiplying the square of the input position count in the energy
  bound for every output branch. 

### `Procedure.run`

 Construct the execution tree from a state with `n = k + g` lane coordinates. Every
  terminal state has degree exponent `b` and `g` lane coordinates. 

### `ofPass`

 A single exact tensor substep with input-independent energy and count estimates. 

### `id`

 An empty schedule preserves the entire state. 

### `seq`

 The later step's order error is bounded by the squared original order,
since the earlier step has a positive integer position divisor. 
