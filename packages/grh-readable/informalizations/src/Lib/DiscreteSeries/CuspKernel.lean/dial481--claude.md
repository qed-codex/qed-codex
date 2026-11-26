---
{
  "module": "src/Lib/DiscreteSeries/CuspKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/CuspKernel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/CuspKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kernels kill bounded radical-invariant functions; dilations along isotropic subspaces

The file proves that, under hypotheses stated below, integration against an idempotent kernel kills
bounded continuous functions that are left invariant under a radical, namely the elements `r` with
`(r, 1) ∈ D` for a subgroup `D` of `G × ℂˣ`
(`New.DiscreteSeries.integral_idempotentKernel_mul_eq_zero`). It also proves that, for unitary
groups, dilations along an isotropic subspace meet every conjugate of a neighbourhood of `1`
(`New.DiscreteSeries.exists_conj_mem_dilationGroup`). The second result is used for the hypothesis
`hD_near` of the first.

The imported notions used in the statements are:
* `IsIdempotentKernel e`: `e` is continuous, integrable and self-adjoint, `e 1 ≠ 0`, and the
  convolution `e * δ_x * e` is `(e x⁻¹ / e 1) • e`;
* `U J`: the group of invertible matrices `g` with `gᴴ * J * g = J`;
* `dilationGroup A`: the pairs `(g, c)` with `g ∈ U J` and `c` a unit, such that `g * A = c • A`
  and `wᴴ * J * g * v = wᴴ * J * v` whenever the columns of `v` and `w` are `J`-orthogonal to
  those of `A`.

## Relation to the literature

Known result: coefficients of integrable discrete series are cusp forms. The vanishing of constant
terms is proved for any continuous self-adjoint integrable minimal idempotent `e` with `‖e‖ * ℓ`
integrable, tested on bounded continuous functions invariant under the radical, under the
hypotheses on `H`, `ℓ` and `D` stated below. Source: R. Godement, C. R. Acad. Sci. Paris 225
(1947) 521-523, 657-659; N. Wallach, Real Reductive Groups I (1988), ch. 7; the closest to the proof
here are B. Barnes, Proc. Edinburgh Math. Soc. 23 (1980), and A. Valette, Math. Ann. 294 (1992)
277-287.



## A kernel kills bounded functions left invariant under a radical

`New.DiscreteSeries.integral_idempotentKernel_mul_eq_zero` is the abstract form of the vanishing of
constant terms that makes forms cuspidal. In the application `D` consists of dilations along an
isotropic subspace paired with their scale factors, and `H` is a logarithmic height.


### `eq_zero_of_anticommute`

 An element `X` of a normed algebra that anticommutes with an element `U` within `1 / 2` of
`1` is zero. 

### `integrable_mul_translate`

 The product of an integrable function `k` with a translate of a bounded continuous function
`φ` is integrable. 

### `norm_integral_mul_translate_le`

 The integral of an integrable function `k` against a translate of a bounded continuous
function `φ` is at most the `L¹` norm of `k` times the supremum norm of `φ`. 

### `norm_integral_mul_translate_sub_le`

 The integrals of an integrable function `e` against the translates of `φ` by `y` and by `y * b`
differ by at most the `L¹` distance of `e` and its translate by `b`, times the norm of `φ`. 

### `norm_integral_mul_phase_sub_le`

 If `H (y * g)` differs from `H y` by at most `ℓ g`, then the integral of `e` against
`φ (y * g)` times the variation of the phase `circleMap 0 1 (H * θ)`, that is `exp (i H θ)`, is at
most `|θ|` times the integral of `‖e‖ * ℓ` times the norm of `φ`. 

### `exists_kernel_operator`

 Integrating the right translates of `φ` against an integrable function `e` is a bounded
operator on the bounded continuous functions. 

### `kernel_operator_idempotent`

 Integration against a minimal idempotent kernel `e` (continuous, integrable, self-adjoint, with
`e * δ_x * e` a multiple of `e`) is an idempotent operator. 

### `exists_left_translation_operator`

 Left translation by `a`, where `(a, z) ∈ D`, preserves the space `V` of the functions fixed by
the kernel operator `T` and left invariant under the elements `r` with `(r, 1) ∈ D`. 

### `norm_one_sub_left_translation_le`

 Let `D` be a subgroup of `G × ℂˣ` and `V` the space of functions fixed by the kernel operator
`T` and invariant under the radical, the `r` with `(r, 1) ∈ D`. If `(a, z) ∈ D` and for every `y`
some `b y` with `(y * b y * y⁻¹, z) ∈ D` translates `e` by less than `1 / 2` in `L¹`, then the
translation `U` of `V` by `a` is within `1 / 2` of the identity. 

### `eq_zero_of_map_phase_mul_eq_zero`

 Let `T φ y = ∫ g, e g * φ (y * g)` and `χ = exp (i H θ)`, where `|H (y * g) - H y| ≤ ℓ g` and
`|θ| * ∫ g, ‖e g‖ * ℓ g < 1`. If `T` fixes `φ` and kills `χ * φ`, then `φ = 0`. 

### `eq_zero_of_mem_fixed_invariant`

 Let `G` be a second countable topological group with a left-invariant Borel measure. Let `e` be
integrable and `T` the operator on bounded continuous functions with `T φ y = ∫ e g * φ (y * g)`,
and let `D` be a subgroup of `G × ℂˣ`. Let `V` be the functions fixed by `T` and invariant under
left translation by every `r` with `(r, 1) ∈ D`, where `T` maps such invariant functions into `V`.
Let `H` be continuous with `|H (y * g) - H y| ≤ ℓ g`, where `‖e‖ * ℓ` is integrable, and with
`H (r * g) = H g - log ‖c‖` for `(r, c) ∈ D`. If `log ‖z‖ ≠ 0`, `(a, z) ∈ D`, and for every `y` the
element `b y` has `(y * b y * y⁻¹, z) ∈ D` and `‖e - e ((b y)⁻¹ * ·)‖` in `L¹` is less than `1 / 2`,
then `V = 0`. 

### `integral_idempotentKernel_mul_eq_zero`

 Vanishing of constant terms. Let `G` be a second countable locally compact group with left Haar
measure and let `e` be a minimal idempotent kernel (continuous, integrable, self-adjoint, with
`e * δ_x * e` a multiple of `e`) with `‖e‖ * ℓ` integrable, where `H` is a continuous function with
`|H (x * g) - H x| ≤ ℓ g`. Let `D` be a subgroup of `G × ℂˣ` such that `H (r * g) = H g - log ‖c‖`
for `(r, c) ∈ D`. Suppose that every neighbourhood `W` of `1` has a `c` with `log ‖c‖ ≠ 0` such that
for every `x` some `b ∈ W` has `(x * b * x⁻¹, c) ∈ D`. Then `∫ e g * f (x * g) = 0` for every
bounded continuous `f` with `f (r * g) = f g` whenever `(r, 1) ∈ D`.

This is meant as a step toward Harish-Chandra's theorem that `K`-finite discrete series coefficients
are cusp forms; that theorem itself is not stated here. It applies to every minimal idempotent
kernel `e` with the hypotheses on `H`, `ℓ` and `D`, and shows that `e` integrates to zero against
bounded continuous invariant functions. 

 ## Dilations along an isotropic subspace meeting conjugates of balls about 1 

### `New.DiscreteSeries.exists_isStarProjection_mul_eq_zero_iff`

 Every complex matrix `B` has the same kernel as some orthogonal projection, namely the
projection onto the orthogonal complement of the kernel of `B`. 

### `New.DiscreteSeries.exists_conj_mem_dilationGroup`

 Dilations near `1`. Let `J` be a hermitian involution, let the columns of `A` be isotropic for
`J`, and let `c > 0` and `x ∈ U J`, the group of `g` with `gᴴ * J * g = J`. Then some `y ∈ U J` is
within distance `c` of `1` for the operator norm, and `x * y * x⁻¹` is a dilation along `A` by the
factor `1 + c`: this element `g` has `g * A = (1 + c) • A`, and `wᴴ * J * g * v = wᴴ * J * v`
whenever `Aᴴ * J * v = 0` and `Aᴴ * J * w = 0`. 
