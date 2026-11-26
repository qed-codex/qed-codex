---
{
  "module": "src/New/Determinant/Chain/SquareLaw.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite square law for theta lifts: special data, matched functions and Fourier form

This is linear algebra over a finite ring `R` with a multiplicative character `χ`, behind the
commuting squares of theta lifts. A square law relates a function `L` on `a × n` matrices to a
function `L'` on `n × b` matrices. The rule for a square is the law written out for the weights `p`
and `nextDatum p`, and a second identity follows by applying the rule to a Fourier transform.

## Main definitions and results

* `New.Exchange.SquareLaw`: `L` and `L'` transform by `χ ∘ det`, and `∑ Ψ L' = c ∑ Φ L` for all
  matched functions `Φ`, `Ψ`.
* `New.Exchange.pointDatum`, `New.Exchange.nextDatum`: the point datum, which is the indicator
  function of the matrix `(1; 0)`, and the datum built from a function `p` on `n × a` matrices,
  which has the value `p (-η)`, divided by the number of blocks `s`, at `(η s; 0 1)`.
* `New.Exchange.SquareLaw.sum_eq_nextDatum`: the square law for `p` and `nextDatum p`.
* `New.Exchange.SquareLaw.exists_sum_matrixFourier_eq_sum_nextDatum`: for primitive characters and
  the shapes `n = N`, `a = N ⊕ T`, `b = T`, an identity of the same kind between the Fourier
  transforms of the weights, with a constant of known modulus in place of the group orders.

Notions from other files:
* `New.firstCols e k`, `New.invLastRows e k`: for `k` invertible and indices split by
  `e : b ⊕ a ≃ n`, the columns `b` of `k` and the rows `a` of `k⁻¹`.
* `New.AreMatched ⊤ e χ Φ Ψ`: `Φ` vanishes off the matrices `invLastRows e k`, `Ψ` vanishes off the
  matrices `firstCols e k`, and `Φ (invLastRows e k) = χ (det k) Ψ (firstCols e k)` for all `k`.
* `New.inclMatrix R u`: for a map `u : m → n` of index sets, the `n × m` matrix whose `j`-th column
  is the standard basis vector of index `u j`.
* `New.Exchange.matrixFourier ψ f`: the function `ρ ↦ ∑ v, f v * ψ (tr (ρ v))`.
* `New.Exchange.IsPrimitiveMulChar χ`: for every `a ≠ 0` some `χ (1 + c * a)` is neither `0` nor
  `1`.

## Relation to the literature

See `New.Determinant.Exchange.OneSquare` and `New.Determinant.Chain.ChainNorms` for related work.


 ### The square law and the data 

### `SquareLaw`

 The square law with constant `c` for a function `L` on `a × n` matrices and a function `L'` on
`n × b` matrices over the finite ring `R`, the indices being split by `σ : b ⊕ a ≃ n`: both
functions transform by `χ ∘ det`, and `∑ Ψ L' = c ∑ Φ L` for all matched functions `Φ`, `Ψ` in the
sense of `New.AreMatched`. In the application `L x` and `L' y` are values of the two composites of
theta lifts around a commuting square. 

### `SquareLaw.left_mul`

 `L` transforms by `χ ∘ det` under left multiplication by invertible matrices. 

### `SquareLaw.right_mul`

 `L'` transforms by `χ ∘ det` under right multiplication by invertible matrices. 

### `SquareLaw.sum_eq_of_areMatched`

 For matched functions `Φ`, `Ψ` the sum of `Ψ L'` is `c` times the sum of `Φ L`. 

### `pointDatum`

 The point datum: the indicator function of the inclusion matrix `(1; 0)` among the
`(a ⊕ b) × a` matrices. 

### `nextDatum`

 The datum built from a function `p` on `n × a` matrices. It is a function on
`(n ⊕ b) × (a ⊕ b)` matrices. At a block matrix `(η s; 0 1)`, with `η` of size `n × a` and `s` any
`n × b` matrix, its value is `p (-η)` divided by the number of all `n × b` matrices over `R`; it
vanishes at all other matrices. 

### `swapFirstTwo`

 The order of the basis of `n ⊕ a ⊕ b` that puts the block `a` first. 

### `sum_eq_sum_fromRows`

 A sum over matrices with rows `N ⊕ n` is a double sum over the two blocks of rows. 

### `sum_eq_sum_fromCols`

 A sum over matrices with columns `N ⊕ n` is a double sum over the two blocks of columns. 

### `sum_eq_sum_fromBlocks`

 A sum over `(N ⊕ n) × (a ⊕ b)` matrices is a fourfold sum over the blocks. 

### `inclMatrix_inl`

 The matrix of the inclusion of `a` in `a ⊕ b` is `(1; 0)`. 

### `sum_nextDatum_mul`

 A sum of `F` weighted by `nextDatum p` is the sum of `F (η s; 0 1)` over all `n × a` matrices
`η` and all `n × b` matrices `s`, weighted by `p (-η)` divided by the number of `n × b` matrices. 

### `star_nextDatum`

 Complex conjugation commutes with `nextDatum`. 

### `sum_inv_det_mul_eq_card_mul`

 If `f g = χ (det g) v` for all invertible `g`, the sum of `χ⁻¹ (det u) f u` over all square
matrices `u` is `v` times the order of the general linear group. 

 ### Consequences of the square law 

### `SquareLaw.card_mul_apply_fromRows_eq`

 The square law at a point. The hypothesis `hL` says that `L (k x) = χ (det k) L x` and
`L' (y k) = χ (det k) L' y` for invertible `k`, and that `∑ Ψ L' = c ∑ Φ L` for all matched `Φ`,
`Ψ`: they vanish off the rows `a` of `γ⁻¹`, resp. the columns `b` of `γ`, for invertible `γ`, and
there `Φ` is `χ (det γ)` times `Ψ`. Then for an `a × b` matrix `w`, the value of `L'` at `(1; -w)`
times `#GL b R` is `c` times the value of `L` at `(w 1)` times `#GL a R`; the index set `b ⊕ a` of
these two block matrices is identified with `n` by `σ`. 

### `SquareLaw.sum_eq_nextDatum`

 Split `n ⊕ a ⊕ b` into `a` and `n ⊕ b` (`swapFirstTwo`). Let `L`, `L'` satisfy the square law
with constant `c`: they transform by `χ ∘ det` on the left, resp. right, and `∑ Ψ L' = c ∑ Φ L`
whenever `Φ`, `Ψ` vanish off the rows `n ⊕ b` of `γ⁻¹`, resp. the columns `a` of `γ`, for invertible
`γ`, and there `Φ` is `χ (det γ)` times `Ψ`. Evaluate `L'` at `y` stacked on the inclusion matrix
`(1; 0)` of `a` in `a ⊕ b`, and `L` at the inclusion matrix of `n` in `n ⊕ b` placed left of `x`.
Then `#GL a R` times the sum of `L'` weighted by `p y` is `c` times `#GL (n ⊕ b) R` times the sum of
`L` weighted by `nextDatum p x`. 

 ### The matched function of a function, and blocks of invertible matrices 

### `blockInlGL`

 The embedding `g ↦ g ⊕ 1` of `GL b R` in `GL n R`, in the order of the basis given by `e`. 

### `matchOf`

 The function on `a × n` matrices that is `0` off the matrices `invLastRows e γ` (the rows `a`
of `γ⁻¹`) and has the value `χ (det γ) Ψ (firstCols e γ)` at `invLastRows e γ`, for a chosen `γ`.
The choice is immaterial if `Ψ` transforms by `χ⁻¹ ∘ det` on the right. 

### `exists_firstCols_eq_mul_of_invLastRows_eq`

 If the rows `a` of `γ⁻¹` and `γ'⁻¹` agree, then the columns `b` of `γ'` are those of `γ`
multiplied on the right by an invertible `h` with `det γ' = det γ * det h`. 

### `areMatched_matchOf`

 If `Ψ` vanishes off the matrices `firstCols e γ` (the columns `b` of an invertible `γ`) and
satisfies `χ (det h) Ψ (y h) = Ψ y` for invertible `b × b` matrices `h`, then `Φ = matchOf χ e Ψ` is
matched with `Ψ`: it vanishes off the matrices `invLastRows e γ` (the rows `a` of `γ⁻¹`) and has
there the value `χ (det γ) Ψ (firstCols e γ)`. 

### `_root_.New.AreMatched.unique`

 If `Φ` and `Φ'` are both matched with `Ψ` (`AreMatched ⊤ e χ`), then `Φ = Φ'`. Both vanish off
the matrices `invLastRows e γ` (the rows `a` of `γ⁻¹`), for invertible `γ`. There both take the
value `χ (det γ) * Ψ (firstCols e γ)`. 

### `_root_.New.AreMatched.translate`

 Let `e : b ⊕ a ≃ n` split the index set `n` into `b` and `a`, let `Φ` be a function on `a × n`
matrices and `Ψ` one on `n × b` matrices over `R`, and let `g` be invertible. Suppose that they are
matched over all of `R` (the `⊤`): they vanish off the rows `a` of `γ⁻¹`, resp. the columns `b` of
`γ`, for invertible `γ`, and there `Φ` is `χ (det γ)` times `Ψ`. Then `x ↦ c χ (det g) Φ (x g)` and
`y ↦ c Ψ (g⁻¹ y)` are matched functions. 

### `hasLeftInv_submatrix_invLastRows`

 Let `k` be invertible. If `firstCols e k` has a left inverse `s` whose columns indexed by an
injection `f` vanish, then the columns indexed by `f` of `invLastRows e k` form a matrix with a left
inverse. 

### `hasLeftInv_toCols_of_hasLeftInv_toRows`

 Let `e` split the index set `N ⊕ n` into `b` and `a` and let `k` be invertible. Consider the
columns `b` of `k` (`firstCols e k`) and the rows `a` of `k⁻¹` (`invLastRows e k`). If the rows `N`
of the former have a left inverse, so have the columns `n` of the latter, and likewise with `N` and
`n` exchanged. 

### `exists_eq_firstCols`

 Let any two elements `r`, `s` of `R` be multiples of `(1 - ε) r + ε s` for some idempotent `ε`
(the hypothesis `hR`), and let `e` split the index set `N ⊕ n` into `b` and `a`. If the rows `N` or
the rows `n` of an `(N ⊕ n) × b` matrix `y` have a left inverse, then `y` is the block
`firstCols e γ` of the columns `b` of an invertible matrix `γ`. 


## The square law after Fourier transform

`New.Exchange.SquareLaw.exists_sum_matrixFourier_eq_sum_nextDatum` is the second of two identities
over a finite ring `R` deduced from the square law `New.Exchange.SquareLaw`. It is the first,
`New.Exchange.SquareLaw.sum_eq_nextDatum`, applied to a Fourier transform
(`New.Exchange.matrixFourier`); the Gauss sum of `χ ∘ det`
(`New.Exchange.exists_matrixFourier_eq_mul_inv_det`) gives the constant, through
`New.Exchange.exists_sum_matrixFourier_nextDatum_eq`.


### `matrixFourier_nextDatum_fromBlocks`

 Let `ψ` be a primitive additive character. For a function `p` on `n × a` matrices, `nextDatum p`
is the function on `(n ⊕ b) × (a ⊕ b)` matrices that takes at each `(η s; 0 1)`, with `η` of size
`n × a` and `s` any `n × b` matrix, the value `p (-η)` divided by the number of `n × b` matrices,
and is `0` elsewhere. Its Fourier transform `ρ ↦ ∑ v, nextDatum p v * ψ (tr (ρ v))` takes at a block
matrix `(A B; C D)` the value of the transform of `p` at `-A` times `ψ (tr D)` if `C = 0`, and the
value `0` otherwise. 

### `exists_sum_matrixFourier_nextDatum_eq`

 Let the additive character `ψ` and the multiplicative character `χ` of the finite ring `R` be
primitive. There is `γ`, with `‖γ‖² = #R ^ (#T (#T + 2 #N))`, such that the following holds for all
`p` and all `L` that transform by `χ ∘ det` on the left. Let `ι = inclMatrix R Sum.inl`, the
`(N ⊕ T) × N` matrix `(1; 0)` with the identity in the rows `N`, and evaluate `L` at `(ι x)`. The
sum weighted by the Fourier transform of the conjugate of `nextDatum p` is `γ` times the sum
weighted by `nextDatum` of the Fourier transform of the conjugate of `p`. 

### `SquareLaw.exists_sum_matrixFourier_eq_sum_nextDatum`

 Let the additive character `ψ` and the multiplicative character `χ` of the finite ring `R` be
primitive. There is `γ`, with `‖γ‖⁻² = #R ^ (#T (#T + 2 #N))`, such that the following holds for all
`p`, `c`, `L` and `L'`. Split `N ⊕ (N ⊕ T) ⊕ T` into the middle block and the two outer blocks
(`swapFirstTwo`), and assume the square law: `L`, `L'` transform by `χ ∘ det` on the left, resp.
right, and `∑ Ψ L' = c ∑ Φ L` whenever `Φ`, `Ψ` vanish off the outer rows of `k⁻¹`, resp. the middle
columns of `k`, for invertible `k`, and there `Φ` is `χ (det k)` times `Ψ`. Evaluate `L'` at `y`
stacked on the matrix `(1; 0)` of the inclusion of `N ⊕ T` in `(N ⊕ T) ⊕ T`, and `L` at that of the
inclusion of `N` in `N ⊕ T` placed left of `x`. The sum of `L'` weighted by the Fourier transform of
the conjugate of `p` is `γ c` times the sum of `L` weighted by the transform of the conjugate of
`nextDatum p`. 
