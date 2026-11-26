---
{
  "module": "OAI/Computability/VPVNP/HardnessWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Generating polynomials of satisfying assignments

Weights may live in any commutative semiring. When each weight is a variable or
a scalar, the literal CNF test realizes this polynomial by a projection of the
universal integer family. Its source index is polynomial when the number of
Boolean variables and the total number of literals are polynomial.


### `weightedCNF`

 Sum of assignment weights over the satisfying assignments of a CNF. 
