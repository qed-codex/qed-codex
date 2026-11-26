---
{
  "module": "OAI/Computability/VPVNP/FixedProgramReaderData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramReaderData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramReaderData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tail obligations supplied by the literal scalar evaluator

The choice of a monomial basis is part of the length-specific advice.
Re-present the slice model in the order used by the two deterministic
matrix readers. The same raw binary advice then works for every vector
of exponents, with exact monomials on the required range.


### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 Enumerate the finite ground field of the selected slice. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Algebra (Ground p t d) (Ambient p)`

 View the ambient field as an algebra over the ground field through the slice embedding. 

### `canonicalModel`

 Present the selected slice in the canonical coordinates used by the scalar evaluator. 

### `scalarDataOfReader`

 Turn the encoded matrix readers and their resource bounds into scalar data for the canonical model. 
