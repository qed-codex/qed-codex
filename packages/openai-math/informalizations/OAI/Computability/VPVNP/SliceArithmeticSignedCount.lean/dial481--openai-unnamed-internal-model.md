---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticSignedCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticSignedCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticSignedCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Converting signed witness counts into an extension-field coefficient

Each arbitrary-width little-endian count is reduced independently modulo the
advised prime. Their difference occupies the constant coordinate of the power
basis, with a zero word for every higher coordinate. The input counts, field
advice and the caller's output suffix survive the conversion.


### `emitPorts`

 Route constant emission through the residue holding the signed difference, the caller's
degree and zero word, and the result port. 

### `machine`

 Reduce both counts modulo the prime, subtract the residues, emit their difference in the
constant coordinate, and clear the residues. 

### `callCap`

 Step bound for signed-count conversion with input bit lengths `n` and `m`, extension degree
`e`, and limb width `w`. 

### `difference`

 The coefficient emitted from the two binary counters. 

### `callCap_le`

 A single quadratic bound in all bit lengths and the number of coordinates. 
