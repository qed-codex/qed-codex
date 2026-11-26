---
{
  "module": "OAI/Computability/VPVNP/Hardness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Hardness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Hardness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# VNP-completeness of the integer family

A VNP summand has a polynomial-size ordered-parse CNF presentation. Copying each selected
production flag separates its scalar and variable labels. Witness variables become free Boolean
bits constrained by their selected occurrences. This leaves only variable and scalar projection
weights. The universal coefficient machine can check the resulting CNF by querying its payload.


### `exists_weightedCNF_of_isVNP`

 Every VNP family has a CNF presentation with polynomially many bits and literals.
Each selected bit contributes a single variable or a single scalar. 

### `pProjects_P_of_isVNP`

 Each VNP family is a p-projection of the explicit universal integer family
after casting coefficients to the same field. 

### `P_vnpComplete`

 The VNP-completeness assertion of Theorem 1.1 for every field, with arbitrary field
constants and variable-or-constant projections of formal polynomials. 
