---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPolynomialConstructor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialConstructor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialConstructor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Reusable physical construction of a padded polynomial from two scalar
cells and a cached unary dimension. The native constructor buffers are
cleared on return; an order-preserving move writes the chosen cache slot. 

### `constructAtInputs_run`

 Low and high scalar inputs are consumed; D and the zero coefficient are
retained. This is the actual tape constructor used for constants and linear
factors, including all native-buffer cleanup and output movement. 
