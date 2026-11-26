---
{
  "module": "OAI/Computability/VPVNP/RankQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering rank from a weighted determinant

Appendix D.2 uses the degree in `u` of `det(1 - u D₁(z) M D₂(z) Mᵀ)` to
query the rank of a rectangular matrix. At the rank, every nonzero minor
comes from a row basis and a column basis. The first basis of each kind has
strictly smaller total index weight than any other. Its squared minor
therefore supplies an isolated nonzero coefficient in `z`, in every
characteristic.


### `weight_sum_nonzero`

 A unique nonzero summand at a specified weight prevents cancellation,
including over fields of characteristic two. 

### `isolated_maximal_minor`

 At maximum rank the term indexed by the first row and column bases has a
unique weight among all nonzero terms in the minor expansion. 

### `rankPolynomial_natDegree`

 The determinant rank test of Appendix D.2, including characteristic two
and matrices with zero rows, zero columns, or rank zero. 
