---
{
  "module": "OAI/Computability/VPVNP/BalancedCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedCoefficients.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting a coefficient over a cut of the parties

In §4 of *VP and VNP differ over every field*, a homogeneous product contributes
to the coefficient tensor through a sum of products across party cuts. Choosing one
variable at each party makes the queried monomial squarefree. The degree of the first
factor fixes the size of the first side of the cut.


### `partyExponent`

 Exponent vector selecting the variable `(i, a i)` for each party `i ∈ S`. 

### `partyExponent_congr`

 An exponent on one side of the cut depends only on assignments on that side. 

### `coeff_mul_partyExponent`

 Coefficient of a product on all parties, expressed as a sum over cuts of the
parties themselves. Each term uses the assignments on its respective sides. 

### `coeff_mul_partyExponent_homogeneous`

 If the first factor is homogeneous of degree `d`, only cuts of size `d`
contribute. The product for each such cut is separated across its two sides. 
