---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMultiplyCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A reusable multiplication call on packed extension-field elements

The caller supplies two low-degree-first limb streams, a prime modulus, its
advised polynomial, the unary degree and a zero word giving the register width.
The subroutine consumes the query operand, overwrites the accumulator with the
product and clears its entire local workspace.


### `machine`

 Execute packed field multiplication by setting up the workspace, reversing the query's limb
order, running Horner rounds, and returning the product. 

### `callCap`

 Total bit-stack time, including port setup, digit ordering and final cleanup. 

### `callCap_le`

 A simple quadratic bound in both the number of limbs and their working width. 

### `prefix_stack_length`

 A prefix of the actual instruction execution uses only polynomial storage
on each of the finitely many ports of the multiplier. 
