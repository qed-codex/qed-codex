---
{
  "module": "OAI/Computability/VPVNP/ParseCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseCoefficients.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extracting squarefree coefficients of parse products

In §8.1 of *VP and VNP differ over every field*, each queried monomial uses each
of its variables once. A product gate partitions those variables between its two
ordered children. For a product of linear forms this amounts to assigning each
leaf one queried variable, using every queried variable exactly once.


### `squarefreeDegree`

 The exponent vector of the squarefree monomial supported on `s`. 

### `coeff_mul_squarefree`

 The coefficient at a squarefree monomial of a product is a sum over subsets.
The first factor uses exactly that subset and the second factor uses its complement. 

### `coeff_prod_linearForms`

 A squarefree coefficient of a product of linear forms is the sum of the
weights of all bijections from the factors to the selected variables. 

### `coeff_prod_linearForms_query`

 Indexed form of the leaf-bijection rule in §8.1. The query is an embedding,
so every chosen variable occurs once even when a leaf could choose any variable
of the ambient polynomial ring. 
