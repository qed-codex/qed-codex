---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMultiplyInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the workspace of a slice-field multiplication

The multiplication call starts from empty local stacks. It copies the prime
modulus, zero-word template, polynomial coefficients, multiplier, and degree
markers to their local ports. The query stays on its external stack until the
subsequent digit-order conversion.


### `«initialize»`

 Copy the caller's field parameters, multiplier, and degree markers into the initially empty
Horner workspace. 

### `initialize_runs`

 The entry routine installs the register bank and the coefficient streams.
Each of the fourteen copies has at most `(e+1)*(w+1)` bits. 
