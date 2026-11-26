---
{
  "module": "OAI/Algorithms/SubexponentialSAT/WeightedSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/WeightedSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/WeightedSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The weighted support bound for the symbolic incidence polynomials

The outer polynomial variable is U, the middle polynomial variable is Z,
and the innermost multivariate polynomial has the formal input coordinates.
An admissible polynomial only has monomials with degX ≤ degU + degZ.


### `Admissible`

 The coefficient form of the weighted monomial support condition. 

### `admissible_monomial`

 A single U/Z monomial is admissible whenever its X coefficient fits. 

### `scalarHom`

 Embed a scalar as a polynomial constant in all three groups of variables. 

### `admissible_eval₂`

 Substituting admissible incidence arguments into any table polynomial
preserves the weighted support condition. 

### `linearForm`

 An actual finite linear form in the formal input coordinates. 

### `markedArgument`

 The symbolic form beta + U defect + positive-Z linear terms. 

### `admissible_factor_product`

 Products of arbitrary table polynomials evaluated at admissible arguments. 

### `retained_degree_bound`

 The surviving U/Z rectangle has strictly smaller X degree than D + μ. 

### `xTrunc`

 Retain only input-coordinate monomials of total degree at most N. 

### `xTrunc_mul`

 Total X degree is monotone under multiplication, so early clipping is safe. 

### `incidenceArgument`

 The exact incidence-argument shape: beta + U (L - beta) + Z-tail. 

### `admissible_incidence_linearForms`

 Actual finite linear forms discharge all the X-degree assumptions. 
