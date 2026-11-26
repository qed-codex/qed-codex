---
{
  "module": "OAI/Computability/VPVNP/ShrinkStateWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parameter witnesses of the shrinking pass on a compressor state

The change of coordinates that packs the old site and its lane for the
shrinking step pulls the old half-wire arguments back to their packed
forms. Every surviving local witness has the same formal exponent vector.


### `noncomputable local instance : DecidableEq X.Base`

 Classical equality test on base sites used to construct monomial witnesses for the
shrinking kernels. 

### `shrinkStateKernelWitness`

 Every entry of every selected kernel in the dyadic shrinking state
pass is a finite sum of parameter monomials. The witnesses enumerate the
absorbed words and the accepted resident matrix checks. 

### `shrinkStateKernelWitness_degree_le`

 The parameter degree bound survives the coordinate change on the
old half-wire inputs of the state pass. 
