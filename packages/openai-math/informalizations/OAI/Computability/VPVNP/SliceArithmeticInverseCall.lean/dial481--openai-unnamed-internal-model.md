---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticInverseCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticInverseCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticInverseCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit-stack routine for inversion in the advised field

The saved exponent is the binary expansion of `p^e-2`, independent of the
coordinate query. Zero starts with a zero accumulator, while a nonzero input
starts with one. The same powering loop then handles every field size,
including the empty exponent when the field has two elements.


### `machine`

 Initialize the base and accumulator from the packed input, then run binary powering with
the saved inverse exponent. 

### `wordCap`

 Bound on inversion steps for degree `e`, limb width `w`, and `z` stored exponent bits,
including initialization. 

### `callCap`

 The canonical Fermat exponent fits in the total working width of the limbs. 

### `machine_runs`

 The input base and exponent advice are retained and the inversion result
is available in the multiplier's accumulator. 

### `callCap_le`

 A polynomial clock uniform in both input dimensions. 
