---
{
  "module": "src/New/Spanning/MainTerm/BadTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/BadTypes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/BadTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The share of non-allowed polynomials and the bad share

This file bounds the share of the bad types for tuples of polynomials over fields with q elements.
A label is a monic squarefree polynomial of degree `r` that does not vanish at `0`. The file
counts the monic polynomials that are not allowed and the primitive polynomials. It then bounds
the coefficient at the identity of one minus the sum of the idempotents of the good tuples.

## Main definitions and results

* `New.card_not_primitive_mul_le`: for `1 < r < q`, with every polynomial weighted by
  `(1 - r / q) / q ^ r`, the monic polynomials of degree `r` that are not primitive polynomials
  weigh at most `exp (-1 / (2 r (2 r log q + 1)))` in total.
* `New.re_coeff_one_sub_sum_tupleIdem_le`: the bound on the coefficient at the identity of one minus
  the sum of the idempotents of the good tuples.

Notions from other files:
* `New.tupleIdem`: For a tuple (c_w) of polynomials over the fields k_w, the tensor product of the
  polynomial idempotents e_{c_w} in the group algebra of ∏ GL_n(k_w).

## Relation to the literature

In the regular representation of a product of groups GL_r(F_q), types that are not good have share
at most a multiple of 1/q per factor plus a term decaying exponentially in the number of factors. So
the projection to good types discards little when translates of the Poincaré series fill the rows.
It computes the Plancherel shares for GL_r(F_q) from Green's degree formula and counts of squarefree
and primitive polynomials over F_q, followed by a union bound over the factors. Related work: Green,
The characters of the finite general linear groups, 1955; Dudko, Plancherel measures for GL(n,q),
arXiv 0806.1345, 2008; Lidl–Niederreiter, Finite Fields, ch. 3, 1983.


### `New.card_not_isAllowedPolynomial_le`

 Over a field `k` with `q` elements, at most `(1 + M + r) q ^ (r - 1)` monic polynomials of
degree `r` are not allowed polynomials (`IsAllowedPolynomial M r`). Such a polynomial either fails
to be a label, or has a root `x` in `k` with `x ^ M = 1`. 

### `New.totient_le_mul_card_isPrimitivePolynomial`

 Over a field `k` with `q` elements and for `r ≠ 0`, there are at least `φ (q ^ r - 1) / r`
primitive polynomials of degree `r`. These are the irreducible monic polynomials of degree `r`, not
vanishing at `0`, with a root of order `q ^ r - 1`. 

### `New.one_sub_le_card_allowed_mul`

 Over a field with `q` elements and for `1 < r < q`, weight every polynomial by
`(1 - r / q) / q ^ r`. Then the allowed polynomials of degree `r` (monic, squarefree, no root at `0`
or at an `M`-th root of unity in the field) weigh at least `1 - ε` in total if
`(1 + M + 2 r) / q ≤ ε`. 

### `New.card_not_primitive_mul_le`

 Over a field `k` with `q` elements and for `1 < r < q`, weight every polynomial by
`(1 - r / q) / q ^ r`. The monic polynomials of degree `r` that are not primitive polynomials weigh
at most `exp (-1 / (2 r (2 r log q + 1)))` in total. 

### `New.prod_le_re_tupleIdem_coeff_one`

 Let `k w` be finitely many fields with `q` elements, `r = card n < q`, and `c w` a label of
degree `r` over `k w`: a monic squarefree polynomial of degree `r` that does not vanish at `0`. The
idempotent `tupleIdem n c` is the tensor product over `w` of the `labelIdem n (c w)`; it lies in the
complex group algebra of ∏ GL_n(k w). The real part of its coefficient at the identity element of
that group is at least the product of `(1 - r / q) / q ^ r` over all `w`. 

### `New.re_coeff_one_sub_sum_tupleIdem_le`

 Let `k w` be `f` fields with `q` elements each and `r = card n`. A tuple `c` of labels is good
if no `c w` vanishes at an `M`-th root of unity of `k w` and some `c w` is primitive: irreducible
with a root of order `q ^ r - 1`. In the complex group algebra of ∏ GL_n(k w), take one minus the
sum over the good tuples of `tupleIdem n c`, the tensor product over `w` of the idempotents
`∑ g, (Ξ(1) / |G|) conj Ξ(g) • g` of ℂ[G], where G = GL_n(k w) and Ξ is the character `labelChar` of
the label `c w`. Its coefficient at the identity has real part at most `f * ε + exp (-L)` if
`1 < r < q`, `(1 + M + 2 r) / q ≤ ε ≤ 1` and `2 r (2 r log q + 1) L ≤ f`. 
