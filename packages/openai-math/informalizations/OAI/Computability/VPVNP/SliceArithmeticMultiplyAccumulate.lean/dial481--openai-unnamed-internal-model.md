---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMultiplyAccumulate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyAccumulate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyAccumulate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A clean multiply-and-add call on extension-field coefficients

This subroutine adds the product of the two saved factors to the accumulator.
The caller supplies all three in the low-degree-first polynomial basis.


### `machine`

 One finite control copies the factors, multiplies and adds. 

### `callCap`

 Step bound for copying two packed factors, multiplying them, and adding the product to the
accumulator. 

### `machine_runs`

 Both operands and the field advice are preserved, and the private
workspace is empty again when the updated accumulator returns. 

### `callCap_le`

 A polynomial bound in the extension degree and working limb width. 
