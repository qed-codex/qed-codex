---
{
  "module": "OAI/Computability/VPVNP/MacaulayReduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReduction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prime-characteristic descent of the label equations

Section 8.2 applies prime reduction to the Macaulay matrix of all monomial
multiples of the integer equations. A characteristic-zero solution excludes the
row of one from its rational row space. The finite matrix argument supplies a
prime of controlled bit length with the same exclusion. Given the uniform
effective weak Nullstellensatz multiplier bound, the reduced equations then
have a common zero over the algebraic closure of that prime field.


### `macaulayMatrix_map`

 Base change commutes with the entire bounded Macaulay matrix. 

### `exists_prime_one_notMem`

 At the selected prime the constant polynomial one has no certificate with
multiplier degree at most `H`. This matrix statement needs no effective
Nullstellensatz hypothesis. 

### `commonZero_of_one_notMem`

 A uniform weak certificate degree bound turns a failed Macaulay row test
over the base field into a common zero in the extension where the bound holds. 

### `exists_prime_solution_of_weakCertificateBound`

 The characteristic-zero case of the choice-of-characteristic step in
Theorem 8.1, conditional on the stated effective weak Nullstellensatz bound. 
