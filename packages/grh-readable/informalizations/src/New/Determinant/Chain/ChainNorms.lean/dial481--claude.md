---
{
  "module": "src/New/Determinant/Chain/ChainNorms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/ChainNorms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/ChainNorms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Norms along the chain of theta lifts and injectivity of ι_ϑ

This file proves the two commutation relations in the squares of the triangle of lifts and
computes the adjoints of descents. With these, the lifts satisfy the conditions
`New.Exchange.IsTriangle`. This file then compares the chain ι_ϑ (`New.Data.lowerChainAtLevel`)
with the weighted chain of the triangle `z = false`. Here J_M is the principal level at the chosen
places `New.Data.chosenPlace`, and Q is the product of the places of the twist ϑ. The weighted
chain `New.Exchange.weightedChain` is the composite of the lifts `New.Data.triangleLift`, the n-th
multiplied by N_n = `New.Data.triangleGLCard` false ϑ n, an order of GL over a residue ring.

The node `(i, n)` of a triangle is the space of the interval `[i + 1, i + n]`: it has the stem and
the blocks `i + 1, …, i + n`. The nodes `(i, 0)` are the empty intervals; they carry the space at
`(0, 0)` negated `i` times. The lift `triangleLift` goes along a right pair and adds the last block.
The descent `triangleTransposedLift` is a transposed lift along a left pair and removes the first
block; it stands for the adjoint of the map that adds this block. The ascent `triangleReversedLift`
is a transposed lift along the reversed pair and adds the first block. The flag `z = false` selects
the chain Y₀, …, Y_m, and `z = true` the second chain, which is untwisted, has blocks of length
`t - 1` and starts from Y₀ plus a line.

## Main definitions and results

* `New.Data.exists_triangleLift_triangleTransposedLift_comm`,
  `New.Data.exists_triangleTransposedLift_adjoint_comm`: the two commutation relations, with the
  moduli of their constants.
* `New.Data.exists_isTriangle`: with suitable descents these data satisfy the conditions
  `New.Exchange.IsTriangle`; for `z = false` also `New.Exchange.HasSquareModuli`, with the ratios of
  Hecke values `New.Data.quotientRatio` as moduli.
* `New.Data.inner_lowerChainAtLevel`: inner products of lifts are a multiple of those along the
  chain.
* `New.Data.lowerChainAtLevel_injective`: ι_ϑ is injective, because the chain is.

Notions from other files:
* `New.Data.RowIndex`, `New.Data.Y`: The basis index set of Y₀: e₁, …, e_ϱ, the indices of X₀, a
  middle vector, and e*₁, …, e*_ϱ. The basis index set of Y_j: the block `RowIndex`, then j blocks
  of t indices each.
* `New.Data.MFoldTwist`: a twist ϑ whose tame part ψ has ψ_wⁿ non-trivial for all places w in its
  set Q and 1 ≤ n ≤ m.
* `New.Data.chosenLevel`, `New.Data.lastLevel`: The level J_M consists of the elements of
  K₀ = `New.stdLevel` that are 1 modulo the chosen places `New.Data.chosenPlace`. The level J_ϑ(Y_m)
  on Y_m consists of those elements of J_M that are block upper triangular modulo Q.
* `New.Data.triangleModulus`, `New.Data.triangleGLCard`: the modulus 𝔪 of the triangle, and the
  order of the general linear group of a node modulo 𝔪. A lift times this order is the lift for the
  measure that gives the principal level of 𝔪 the volume 1.
* `New.Data.HasAbsUpToNormPower c f`: `‖c ϑ‖²` is `(f ϑ)²` times a constant, possibly zero, and a
  fixed integral power of the norm of Q.

## Relation to the literature

The chain of m theta lifts from U(Y_0) to the definite U(Y_m), mostly outside the range of Rallis's
formula, is injective at level J_M. On target forms its Gram form is that of a product of m Hecke
operators times a scalar whose modulus is a product of ratios of Hecke values. The norm and
injectivity of a single cuspidal theta lift, also below Weil's range, are known in the literature.
Related work: Gan–Qiu–Takeda, Regularized Siegel–Weil formula and Rallis inner product formula (Thm
1.3), 2014; Bruinier–Funke, Injectivity of the Kudla–Millson lift, 2010; He, Compositions of theta
correspondences, 2005.


 ### The two squares 

### `negCount_gridSigns_add`

 The two diagonals of the square with nodes `(i, n + 1)`, `(i, n + 2)`, `(i + 1, n)` and
`(i + 1, n + 1)` have the same number of negative signs. 

### `negCount_gridSigns_add_lt`

 Fewer than half of the signs `gridSigns` at the node `(0, n + 1)`, taken with the offsets `i`
and `i + 1`, are negative; both have the index set `GridIndex z 0 (n + 1)`. Only base entries can be
negative: the added blocks have sign `+1`. 

### `card_gridIndex_add_card_gridIndex`

 The ranks along a row of the triangle form an arithmetic progression. 

### `card_gridIndex_le_quotientPair_negWeight`

 Let `1 ≤ j ≤ D.m` (`LiftIndex`), and let `quotientPair j` be the pair of the quotient of two
characters of the chain at distance `j`, of weight `-c τ = -j * D.gap` at the place `τ`. The rank in
column `j` of the triangle is at most `c τ`. 

### `gridChar_mul_leftPairChar`

 The character of a square of the triangle `z`. Let `1 ≤ n + 1 ≤ D.m` (`LiftIndex`), and let `p`,
`q`, `r` be index types of hermitian spaces, with `card p + card q = card r` even. The character
`gridChar` of U(1)(𝔸) that the lift adding the block `n + i + 2` has at an end of index type `p`,
times the character `leftPairChar` of the left pairs of row `i` at an end of index type `q`, is
`ν * ϑ ^ (n + 1)` times the splitting character `upsilonU1` to the power `card r / 2` (`rankTwist`).
Here `ν`, the character of `quotientPair (n + 1)`, is the quotient of `untwistedLiftChar` at
`j + n + 1` by that at `j`, for any `j`, and `ϑ` is replaced by the trivial twist if `z = true`
(`triangleTwist`). 

### `exists_squareLaw_triangleTransposedLift`

 The square law for point data around the square with nodes `(i, n + 1)`, `(i, n + 2)`,
`(i + 1, n)` and `(i + 1, n + 1)` of the triangle `z`, for `i + n + 1 < D.m`. The transposed lifts
`triangleTransposedLift` go from `(i, j + 1)` to `(i + 1, j)` and are formed with polynomials `Φ₀`,
`Φ₁` that make edges along the left pairs at `(i, n)`, `(i, n + 1)` (`IsLeftPair`). Let `ν` be the
character of `quotientPair (n + 1)`, of weight `-negWeight`, replace `ϑ` by the trivial twist if
`z = true`, and let `(ν * ϑ ^ (n + 1))⁻¹` be tamely ramified exactly at the modulus, where it is
given by the character `χ ϑ` of the residue ring (`IsTameFor`). Apply a linear form `L` to the two
composites around the square, each edge having as datum the indicator function of a block of the
matrix `ξ` or `η`. These functions `A ξ`, `B η` satisfy `SquareLaw` with constant `κ / c`: both
transform by `χ ϑ ∘ det`, and `∑ g B = κ / c * ∑ f A` whenever `f`, `g` are supported on the last
rows of `k⁻¹` and the first columns of `k`, for invertible `k`, with values there in the ratio
`χ ϑ (det k)` (`AreMatched`); `swapFirstTwo` reorders the blocks of indices. Here `‖c‖ ^ 2` is a
constant times `lValueProd`, the product of the `|L(k, (ν * ϑ ^ (n + 1))⁻¹)| ^ 2` off the modulus
for `k` from `1` to the block length `D.t - z.toNat`, times a power of the residue cardinalities at
the modulus. 

### `exists_triangleLift_triangleTransposedLift_comm`

 The first commutation relation, in the square with nodes `(i, n + 1)`, `(i, n + 2)`,
`(i + 1, n)`, `(i + 1, n + 1)` of the triangle `z`, for `i + n + 1 < D.m`, the number of lifts of
the data `D`. The transposed lifts `triangleTransposedLift` go from `(i, j + 1)` to `(i + 1, j)` and
are formed with polynomials at infinity `Φ₀`, `Φ₁` that make edges along the left pairs at `(i, n)`,
`(i, n + 1)` (`IsLeftPair`). For every twist `ϑ` and function `Ψ` on matrices modulo the modulus,
the transposed lift with datum `Ψ` followed by the lift, weighted by the group order
`triangleGLCard z ϑ n`, is a multiple of the lift followed by the transposed lift with datum
`nextDatum Ψ`, weighted by `triangleGLCard z ϑ (n + 2)`. The factor is `conj (β ϑ)⁻¹`, which is `0`
where `β ϑ = 0`. For `z = false`, `‖β ϑ‖²` is the square of `quotientRatio`, a product of ratios of
Hecke values, times a constant and a fixed power of the norm of the modulus Q of `ϑ`. 

### `exists_squareLaw_triangleReversedLift`

 The square law for point data in the square with reversed pairs of the triangle `z = false` (the
twisted one), for `i + n + 1 < D.m`. The reversed lifts `triangleReversedLift` go from `(i + 1, j)`
to `(i, j + 1)` and are formed with polynomials `Φ₀`, `Φ₁` that make edges along the reversed pairs
at `(i, n)`, `(i, n + 1)` (`IsReversedPair`). Let `ν` be the character of `quotientPair (n + 1)`, of
weight `-negWeight`, and let `(ν * ϑ ^ (n + 1))⁻¹` be tamely ramified exactly at the modulus, where
it is given by the character `χ ϑ` of the residue ring (`IsTameFor`). Apply a linear form `L` to the
two composites from `(i + 1, n)` to `(i, n + 2)`, each edge having as datum the indicator function
of a block of the matrix `ξ` or `η`. These functions `A ξ`, `B η` satisfy `SquareLaw` with constant
`κ / c`: both transform by `χ ϑ ∘ det`, and `∑ g B = κ / c * ∑ f A` for all functions `f`, `g`
matched by `χ ϑ` (`AreMatched`). Here `‖c‖ ^ 2` does not depend on `ϑ`. 

### `HasAbsUpToNormPower.of_norm_sq_mul_card_pow_eq_one`

 If `‖c ϑ‖ ^ 2` is the inverse of a fixed power of the number of elements of the residue ring of
`triangleModulus false ϑ`, then `c` has modulus `1` in the sense of `HasAbsUpToNormPower`. 

### `exists_triangleLift_triangleReversedLift_comm`

 The commutation relation in the square with reversed pairs of the triangle `z = false` (the
twisted one), for `i + n + 1 < D.m`, the number of lifts of the data `D`. The reversed lifts
`triangleReversedLift` go from `(i + 1, j)` to `(i, j + 1)`. They are formed with polynomials `Φ₀`,
`Φ₁` that make edges along the reversed pairs at `(i, n)`, `(i, n + 1)` (`IsReversedPair`), and with
`fourierDatum`, the Fourier transform of the complex conjugate, of a datum `Ψ` and of its extension
`nextDatum Ψ` to the next column. The reversed lift followed by the lift is `γ ϑ` times the lift
followed by the reversed lift, where `‖γ ϑ‖²` is a constant times a fixed power of the norm of the
modulus Q of the twist `ϑ` (`HasAbsUpToNormPower γ 1`). 

 ### Adjoints of descents and the triangle conditions 

### `reversalScalar`

 The scalar matrix `Modulus.flipScalar` of the modulus of the triangle, a central element of the
finite adelic unitary group of a node in column `n`. Reversing a theta kernel translates by it. 

### `exists_conj_modKernel_leftPair_eq`

 Reversal of the theta kernel of a left pair of the triangle `z = false` (the twisted one),
between the hermitian spaces `V`, `W` at the nodes `(i + 1, n)`, `(i, n + 1)`, with the characters
`χ ϑ n`, `χ ϑ (n + 1)` given by `leftPairChar`. The kernel `modKernel` depends on a datum `Ψ`, a
function on matrices modulo the modulus (`EdgeDatum`), and a polynomial `Φ` at infinity
(`EdgePoly`). Its conjugate is `τ ϑ ≠ 0` times the kernel from `W` to `V` with datum
`fourierDatum Ψ`, the Fourier transform of the conjugate of `Ψ`, and with the signed transpose
`flipPoly` of the conjugate of `Φ`, translated by the scalar matrix `reversalScalar`. Here `‖τ ϑ‖²`
is a constant times a fixed power of the norm of the modulus Q of `ϑ`. 

### `exists_inner_triangleTransposedLift_eq`

 In the triangle `z = false` (the twisted one), let `Φ` make an edge along the left pair from
`(i + 1, n)` to `(i, n + 1)` (`IsLeftPair`) and `Φ'` in the other direction (`IsReversedPair`). The
adjoint of `triangleTransposedLift` with `Φ` and datum `Ψ`, from forms at `(i, n + 1)` to forms at
`(i + 1, n)`, is `c ϑ` times the following map: right translation (`triangleRep`) by the inverse of
the scalar matrix `reversalScalar`, then `triangleReversedLift` with `Φ'` and `fourierDatum Ψ`, the
Fourier transform of the conjugate of `Ψ`. Here `‖c ϑ‖²` is a constant times a fixed power of the
norm of the modulus Q of the twist `ϑ`. 

### `exists_inner_triangleReversedLift_eq`

 In the triangle `z = false` (the twisted one), let `Φ` make an edge along the left pair from
`(i + 1, n)` to `(i, n + 1)` (`IsLeftPair`) and `Φ'` in the other direction (`IsReversedPair`).
Right translation (`triangleRep`) by the inverse of the scalar matrix `reversalScalar`, followed by
`triangleReversedLift` with `Φ'` and `fourierDatum Ψ`, the Fourier transform of the conjugate of
`Ψ`, is `c ϑ` times the adjoint of `triangleTransposedLift` with `Φ` and `Ψ`. Here `‖c ϑ‖²` is a
constant times a fixed power of the norm of the modulus Q of the twist `ϑ`. 

### `exists_triangleLift_reversalScalar_eq`

 Let `i + n < D.m`, the number of lifts of the data `D`. The theta lift `triangleLift` for the
twist `ϑ`, from forms at the node `(i, n)` of the triangle `z` to forms at `(i, n + 1)`, commutes up
to a scalar of absolute value `1` with the right translations (`triangleRep`) by the inverses of the
scalar matrices `reversalScalar` in the finite adelic unitary groups of the two nodes. 

### `exists_inner_triangleLift_eq`

 For `i + n < D.m`, every form `x` at the node `(i, n + 1)` has an image `x'` at the node
`(i, n)` under the adjoint of the lift `triangleLift`. 

### `exists_triangleTransposedLift_adjoint_comm`

 The second commutation relation in adjoint form, in the triangle `z = false` (the twisted one),
for `i + n + 1 < D.m`, the number of lifts of the data `D`. The transposed lifts
`triangleTransposedLift` go from `(i, j + 1)` to `(i + 1, j)` and are formed with polynomials `Φ₀`,
`Φ₁` that make edges along the left pairs at `(i, n)`, `(i, n + 1)` (`IsLeftPair`). Let `x'` be the
image of `x` under the adjoint of `triangleLift` from `(i, n + 1)` to `(i, n + 2)`. Take the
transposed lift of `x` with `nextDatum Ψ`, the extension of the datum `Ψ` to the next column, and
apply the adjoint of `triangleLift` from `(i + 1, n)` to `(i + 1, n + 1)`. Up to a factor
`conj (κ ϑ)` this is the transposed lift of `x'` with `Ψ`, where `‖κ ϑ‖²` is a constant times a
fixed power of the norm of the modulus Q of the twist `ϑ` (`HasAbsUpToNormPower κ 1`). 

### `exists_isTriangle`

 There are linear maps `d`, the descents, from `(i, n + 1)` to `(i + 1, n)` with the following
properties. With the theta lifts `triangleLift` from `(i, n)` to `(i, n + 1)`, the group orders
`triangleGLCard` as weights and the embeddings `triangleEmbedding` at `(i, 0)` of the forms at
`(0, 0)` fixed by the base level, they form a triangle `IsTriangle` of size `D.m`: each square
commutes up to a constant, on the copies of the base forms the first lift is adjoint to the first
descent, and their composite maps the copy in row `i` injectively to that in row `i + 1`. For
`z = false` the squares satisfy `HasSquareModuli`: their constants have the moduli `quotientRatio`
in the sense of `HasAbsUpToNormPower`, and the descent of the adjoint image of a form under the
upper lift is a multiple of the adjoint image of its descent under the lower lift, by a constant of
modulus `1` in the sense of `HasAbsUpToNormPower`. 

### `index_rangeParabolic_inl_eq`

 The index set `D.Y 1` has two blocks: `blockNumber 1` is `0` on `RowIndex` and `1` on `Fin D.t`.
In `GL (D.Y 1)` over a commutative ring, the group of block upper triangular matrices (`parabolic`)
has the same index as the opposite parabolic `rangeParabolic` of the first block. 

### `stdLevelIndex_lastLevel_eq_prod`

 The index of the level `New.Data.lastLevel` ϑ in K₀ is the product of the orders of the full
`GL (D.Y D.m)` over the residue fields at the chosen places and of the indices of the block upper
triangular groups over the residue fields at the places of ϑ. 

### `triangleGLCard_false_eq_prod`

 The weight `triangleGLCard false ϑ n` is the product of the orders of the general linear group
of the node `(0, n)` over the residue fields at the chosen places and at the places of ϑ. 

### `exists_stdLevelIndex_lastLevel_eq`

 Let m = `D.m` be the number of lifts of the data `D`. There are a constant C and an integer k
such that [K₀ : J] = C·N(Q)^k·δ(ϑ)^m·N_m / (N₀·N₁^m) for every twist ϑ whose tame part has
non-trivial powers up to m at all places of its set Q (`MFoldTwist`). Here N(Q) is the number of
elements of the residue ring of `twistModulus ϑ 0`, the product of the places in Q. The group
K₀ = `New.stdLevel` consists of the integral points, J = `lastLevel ϑ`, and
N_n = `triangleGLCard false ϑ n` is the order of a general linear group over a finite ring, so the
denominator is not zero. The number δ(ϑ) is the `gramFactor` of `descentPair ϑ 1`, a pair of spaces
W and V of ranks r and r + t: the index in K₀ of the level `DescentPair.levelGroup` on V, times
|GL_r| modulo Q and N(Q)^(tr), over |GL_r| modulo the prime divisors `chosenPlace` of `D.piM`. 

### `inner_lowerChainAtLevel`

 Let m = `D.m` be the number of lifts of the data `D`, let ϑ be an m-fold twist, and let x, y be
forms on Y₀ = `spaceY 0` fixed by J_M, the principal level at the prime divisors of `D.piM`
(`principalForms`). Their images ι_ϑ x and ι_ϑ y (`lowerChainAtLevel`) are algebraic forms on the
definite space Y_m, and their inner product, a sum over the classes of the level, is
[K₀ : J]·d·⟨u x, u y⟩. Here J = `lastLevel ϑ`, [K₀ : J] = `stdLevelIndex J`, d is the dimension of
the weight on Y_m with column counts `columnsY`, the cardinality of `WeylIndex`, and u is the chain
of m lifts Y₀ → Y_m of the triangle, each multiplied by its weight `triangleGLCard`. 

### `lowerChainAtLevel_injective`

 For every m-fold twist ϑ, the chain ι_ϑ (`New.Data.lowerChainAtLevel`) from forms of level J_M
on U(Y₀) to forms of level `New.Data.lastLevel` ϑ on U(Y_m) is injective. 
