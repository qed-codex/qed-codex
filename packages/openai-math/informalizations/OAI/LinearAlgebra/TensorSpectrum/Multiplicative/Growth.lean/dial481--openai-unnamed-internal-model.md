---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Growth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Growth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Growth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite orbit weights for the projective fixed-point argument

For a positive sequence with exponential upper bounds, choose its critical
geometric growth rate. Finite geometric weighted sums then have arbitrarily
large mass and arbitrarily small final-term fraction at rates approaching the
critical rate from below. This is the scalar ingredient of the compact convex
projective fixed-point proof; it uses no general fixed-point theorem.

The sums include indices `0, ..., n`. The terminal term is indexed by `n + 1`.


### `weightedSum`

 The normalization of a finite geometrically weighted orbit. 

### `exists_pow_gt`

 Bernoulli's elementary inequality is enough for the only unboundedness
argument below. 

### `not_geometric_domination`

 A positive multiple of a strictly faster geometric sequence cannot be
bounded above by any fixed multiple of a slower one. 

### `geometricRates`

 Rates that give a uniform geometric upper bound for the scalar orbit. 

### `weightedSum_unbounded`

 Below the critical rate, the normalizing masses are unbounded. 

### `near_rate_weights`

 Fix any rate below the critical rate whose relative distance is small.
There are arbitrarily large normalizing masses with a small terminal fraction.
The proof is a contradiction between two distinct geometric growth rates. 

### `exists_approximate_weights`

 The scalar approximate-eigenvector selection used in Appendix A.2.
The rate `r` is fixed before the error tolerance and required mass are chosen. 
