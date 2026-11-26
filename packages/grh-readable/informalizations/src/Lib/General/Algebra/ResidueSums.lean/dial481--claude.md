---
{
  "module": "src/Lib/General/Algebra/ResidueSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/ResidueSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/ResidueSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sums of residues at simple real poles

This file computes sums of residues of rational functions whose denominator has simple real roots.
Let `p = nodal univ x` be the monic polynomial with the distinct roots `x i`. The residue of `F / p`
at `x i` is `F (x i) / p' (x i)`. This file also determines the sign of `p' (x i)` when the roots
are ordered.

## Main definitions and results

* `New.DiscreteSeries.sum_eval_div_eval_derivative_nodal` and
  `sum_eval_div_sub_mul_eval_derivative_nodal`: two sums of residues at simple poles.
* `New.DiscreteSeries.eval_derivative_nodal`: the derivative of `nodal univ x`, the monic
  polynomial with roots `x j`, at the root `x i` is the product of the `x i - x j` over `j ≠ i`.

## Relation to the literature

The residue sums rest on Lagrange interpolation.


### `eval_derivative_nodal`

 The derivative of `nodal univ x`, the monic polynomial with roots `x j`, at the root `x i` is
the product of the `x i - x j` over `j ≠ i`. 

### `sum_eval_div_eval_derivative_nodal`

 Let `p = nodal univ x` be the monic polynomial with the distinct roots `x i` and let `F` be
monic of smaller degree. The residues `F (x i) / p' (x i)` of `F / p` add up to `1` if
`deg F + 1 = deg p` and to `0` otherwise. 

### `sum_eval_div_sub_mul_eval_derivative_nodal`

 Let `p = nodal univ x` have the distinct roots `x i`, let `deg F < deg p` and let `c` not be a
root. The residues of `F / ((t - c) p)` at the roots of `p` add up to minus the residue
`F (c) / p (c)` at the only other pole. 

### `derivative_nodal_sign_of_strictAnti`

 For decreasing roots `x 0 > x 1 > …` of `p = nodal univ x` the number `p' (x i)` has the sign
`(-1) ^ i`. 

### `derivative_nodal_sign_of_strictMono`

 For increasing roots `x 0 < … < x (M - 1)` of `p = nodal univ x` the number `p' (x i)` has the
sign `(-1) ^ (M - 1 - i)`. 
