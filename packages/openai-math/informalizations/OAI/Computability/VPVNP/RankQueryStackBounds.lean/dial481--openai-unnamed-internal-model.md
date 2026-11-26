---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Time and live stack depth for determinant coefficient queries

The product and the matrix-power phases contribute their two binary logarithms
to the stack cap. Three intervening query tags connect a Schur factor to its
power query. The loop bounds include matrix indices and both coefficient
degrees.


### `Below`

 Every child of a branch has depth strictly below the given limit. Leaves satisfy the bound
unconditionally. 

### `width`

 Number of product terms in a branch, with width zero for a leaf. 

### `depth`

 Depth measure on Schur query keys used to bound the stack of recursive calls. 

### `arityBound`

 Uniform bound on the number of child pairs in any Schur query with parameters `n`, `U` and
`Z`. 

### `run`

 The complete Schur stack machine computes the specified coefficient,
with a bound on the length of every intermediate continuation. 

### `rankCoefficientRun`

 A rank scan queries the same machine with scalar reads in the input
matrix. The weighted Gram coefficient requires at most two such reads. 
