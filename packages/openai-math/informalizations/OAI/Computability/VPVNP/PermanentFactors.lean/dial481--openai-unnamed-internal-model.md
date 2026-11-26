---
{
  "module": "OAI/Computability/VPVNP/PermanentFactors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentFactors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentFactors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient extraction on disjoint variable blocks

When a product has one factor for each block of variables, each choice of monomials
in the factors contributes to a different monomial of the product.


### `coeff_fullDegree_prod_rename`

 Each block must supply exactly its own squarefree monomial. 

### `coeff_fullDegree_sum`

 Squarefree coefficient extraction across a sum of variable types can be performed
in two steps, first in the left block and then in the right block. 
