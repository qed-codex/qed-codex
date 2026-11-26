---
{
  "module": "src/Lib/Adelic/TraceFormula/IsotropicStabiliser.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/IsotropicStabiliser.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/IsotropicStabiliser.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stabiliser of an isotropic subspace

Let `J` be a nondegenerate hermitian form and `A` an isotropic subspace, spanned by the columns of
a matrix `X`. An isometry that keeps `A ≠ 0` has a reducible characteristic polynomial. If an
isometry keeps `A`, its characteristic polynomial does not change under left multiplication by the
unipotent radical of the stabiliser of `A`.

Notions from other files:
* `U J` is the unitary group of `J`: the invertible matrices `g` with `gᴴ * J * g = J`.
* `dilationGroup X` consists of the pairs `(g, c)` of an isometry and a unit such that
  `g * X = c • X` and `g` is the identity on `A^⊥` modulo its radical. Its members with `c = 1`
  form the unipotent radical.


### `charpoly_add_mul_of_mul_eq_zero`

 If `γ * A = A * r` and `s * A = 0`, then `γ + A * s` has the characteristic polynomial of
`γ`. In words: `γ` keeps the span of the columns of `A`, and the added matrix has values in this
span and maps it to `0`. 

### `not_irreducible_charpoly_of_mul_eq_mul`

 An invertible matrix `γ` with `γ * X = X * r`, where `X ≠ 0` and `r` is singular, has a
reducible characteristic polynomial. 

### `spanStabilizer`

 The stabiliser in the unitary group `U J` of the span of the columns of `X`: the isometries
`γ` of `J` with `γ * X = X * r` for some matrix `r`. 

### `gram_eq_zero_symm`

 Orthogonality for a hermitian matrix `J` is symmetric: `vᴴ J w = 0` implies `wᴴ J v = 0`. 

### `mul_eq_self_of_mem_dilationGroup`

 If `(ν, 1)` lies in the dilation group of `X`, whose members `(g, c)` satisfy `g * X = c • X`,
then `ν` fixes the columns of `X`. 

### `gram_mul_eq_of_mem_dilationGroup`

 If `(ν, 1)` lies in the dilation group of `X`, whose members act as the identity on the
orthogonal of `X` modulo its radical, then `wᴴ J (ν v) = wᴴ J v` for all `v` and `w` orthogonal to
the columns of `X`. 

### `mem_spanStabilizer_of_mem_dilationGroup`

 An isometry `ν` with `(ν, 1)` in the dilation group of `X` fixes the columns of `X`, so it lies
in the stabiliser of their span. 

### `IsIsotropicFrame`

 For a nondegenerate hermitian form `J`, the columns of `X` span an isotropic subspace `A` and
the columns of `Y` span its orthogonal `A^⊥`. 

### `IsIsotropicFrame.isHermitian`

 The form is hermitian. 

### `IsIsotropicFrame.isUnit`

 The form is nondegenerate. 

### `IsIsotropicFrame.isotropic`

 The subspace `A` is isotropic. 

### `IsIsotropicFrame.orthogonal`

 The columns of `Y` lie in `A^⊥`. 

### `IsIsotropicFrame.spans`

 There are matrices `e` and `b` with `Y * e + b * (Xᴴ * J) = 1`. So every `v` in `A^⊥` is
  `Y * (e * v)`, that is, the columns of `Y` span `A^⊥`. 

### `exists_mul_mul_eq_of_orthogonal_left`

 In an isotropic frame `(J, X, Y)`, every vector orthogonal to the columns of `X` is a
combination of those of `Y`, with coefficients given by one matrix `e`: `Xᴴ J v = 0` implies
`Y * (e * v) = v`. 

### `exists_mul_mul_eq_of_orthogonal_right`

 In an isotropic frame `(J, X, Y)`, every vector orthogonal to the columns of `Y` is a
combination of those of `X`, with coefficients given by one matrix `c`: `Yᴴ J v = 0` implies
`X * (c * v) = v`. 

### `mem_spanStabilizer_iff`

 In an isotropic frame `(J, X, Y)`, where `X` spans `A` and `Y` spans `A^⊥`, an isometry `γ`
keeps `A` exactly if it maps `A` into the orthogonal of `A^⊥`, because `A = (A^⊥)^⊥`. 

### `orthogonal_mul`

 In an isotropic frame `(J, X, Y)`, where `X` spans `A` and `Y` spans `A^⊥`, an isometry `γ`
that keeps `A` also keeps `A^⊥`: it maps the columns of `Y` into the orthogonal of `A`. 

### `det_eq_zero`

 In an isotropic frame `(J, X, Y)`, the matrix `X ≠ 0` is singular, since its columns span an
isotropic subspace for the nondegenerate form `J`. 

### `not_irreducible_charpoly`

 In an isotropic frame `(J, X, Y)` with `X ≠ 0`, an isometry that keeps the isotropic subspace
spanned by the columns of `X` has a reducible characteristic polynomial. 

### `charpoly_radical_mul`

 In an isotropic frame `(J, X, Y)` (a nondegenerate hermitian `J`, the columns of `X` spanning
an isotropic subspace `A` and those of `Y` its orthogonal `A^⊥`), let the isometry `γ` keep `A`
and let the isometry `ν` lie in the unipotent radical of the stabiliser of `A`, that is, `(ν, 1)`
is in the dilation group of `X`: `ν` fixes `A` and is the identity on `A^⊥` modulo `A`. Then
`ν * γ` has the characteristic polynomial of `γ`. 
