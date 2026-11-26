---
{
  "module": "src/New/Spanning/SecondMoment/PositiveType.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Functions of positive type and singular minors

A function `Θ` on a finite group `G` is of positive type if `Θ (a⁻¹ * b) = ⟪u a, u b⟫` for some
vectors `u a` of a complex inner product space.

Notions from other files:

* `New.invTransposeGL` is the automorphism `g ↦ (gᵀ)⁻¹` of `GL n R`.

## Main definitions and results

* `New.card_mul_sum_det_eq_zero_le`: let `k` be a field with `q` elements, `π` a representation by
  `n × n` matrices over `k`, `A₀` and `A₁` two `n × m` matrices and `Θ ≥ 0` of positive type.
  Suppose that, for `v ≠ 0`, the stabilisers of `A₀ v` under `π` and of `A₁ v` under the
  contragredient of `π` have `Θ`-mass at most `Y ≥ 0`. Then the set where `det (A₁ᵀ π(s) A₀)`
  vanishes has mass at most `(2 Θ(G) + q ^ (|m| + |n| / 2) Y) / q`. The proof counts the kernel with
  an additive character and uses Cauchy–Schwarz.

## Relation to the literature

See `New.Spanning.Unfolding.Moments` for related work.


### `inner_sum_sum_eq_card_mul`

 If the inner product of two families of vectors indexed by a finite group `G` has the form
`⟪u a, v b⟫ = f (a⁻¹ * b)`, then `⟪∑ a, u a, ∑ a, v a⟫ = |G| · ∑ s, f s`. 

### `norm_sq_sum_tmul_eq_card_mul_sum`

 Let `Θ` be of positive type, `Θ (a⁻¹ * b) = ⟪u a, u b⟫`, let `ρ` be a matrix representation of
`G`, and let `c` be an orthonormal family indexed by the vectors of `kⁿ`. Then the squared norm of
`∑ a, c (ρ a x) ⊗ u a` is `|G|` times the sum of `Θ` over the `s` with `ρ s` fixing `x`. 

### `expect_addChar_dotProduct`

 Orthogonality of characters as a mean: for a primitive additive character `ψ` of a finite field,
the mean of `ψ (z ⬝ᵥ x)` over `x` is `1` if `z = 0` and `0` otherwise. 

### `orthonormal_addChar_div_sqrt`

 For a primitive additive character `ψ` of a finite field with `q` elements, the functions
`ζ ↦ ψ (-x ⬝ᵥ ζ) / √(q ^ |n|)`, one for each `x : kⁿ`, are orthonormal. 

### `inner_addChar_invTranspose_smul_single`

 For an additive character `ψ`, the inner product of the function
`ζ ↦ ψ (-((gᵀ)⁻¹ x) ⬝ᵥ ζ) / r` with the indicator of `g' z` is `ψ (x ⬝ᵥ g⁻¹ g' z) / r`. 

### `re_sum_addChar_dotProduct_mul_le`

 Let `π` be a representation of `G` by `n × n` matrices over a field with `q` elements, `π' s`
the inverse transpose of `π s`, `ψ` a primitive additive character, and `Θ` of positive type,
`Θ (a⁻¹ * b) = ⟪u a, u b⟫`. If the `Θ`-mass of the stabiliser of `x` under `π'` and that of
`z` under `π` are at most `Y`, then `Re ∑ s, ψ (x ⬝ᵥ π(s) z) Θ s ≤ q ^ (|n| / 2) Y`. 

### `card_le_card_filter_vecMul_eq_zero`

 The left kernel of a singular matrix over a field with `q` elements has at least `q`
elements. 

### `card_mul_sum_det_eq_zero_le`

 Let `π` be a representation of a finite group `G` by `n × n` matrices over a field with `q`
elements, and let `π' s` be the inverse transpose of `π s`. Let `A₀` and `A₁` be two `n × m`
matrices, and let `Θ ≥ 0` be of positive type: `Θ (a⁻¹ * b) = ⟪u a, u b⟫`. Suppose that, for every
`v ≠ 0`, each of two sums of `Θ` is at most `Y ≥ 0`: the sum over the `s` with `π s` fixing `A₀ v`,
and the sum over the `s` with `π' s` fixing `A₁ v`. Then `q · Θ {s | det (A₁ᵀ π(s) A₀) = 0} ≤ 2
Θ(G) + q ^ (|m| + |n| / 2) Y`. 
