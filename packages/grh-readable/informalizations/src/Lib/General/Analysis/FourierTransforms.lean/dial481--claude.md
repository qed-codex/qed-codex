---
{
  "module": "src/Lib/General/Analysis/FourierTransforms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FourierTransforms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FourierTransforms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fourier inversion for periodic functions and decay of Fourier transforms

This file develops Fourier analysis on a compact quotient `B ⧸ B₀` of a topological abelian group,
for a family of characters given in advance. `New.IsContPeriodic B₀ F` says that `F` is continuous
and `B₀`-periodic, and `New.quotMean B₀ F` is its mean over `B ⧸ B₀` for the Haar probability
measure.

## Main definitions and results

* `New.IsDualFamily`: a family `χ i` of characters of `B` trivial on `B₀`, multiplicative in the
  index, that separates the points of `B ⧸ B₀`.
* `New.IsDualFamily.tsum_coeff_eq_quotMean`: the mean of a series of characters with summable
  coefficients.
* `New.IsDualFamily.fourier_inversion`: Fourier inversion, from `New.stone_weierstrass_span`.
* `New.IsDualFamily.eq_zero_of_quotMean_mul_eq_zero`: a periodic function vanishes if its Fourier
  coefficients vanish at the characters that respect its quasi-periods (`New.RespectsQuasiPeriods`).
* `New.exists_pow_mul_norm_fourier_le`: for smooth `c` and `q`, with `c` supported in a compact set
  `K`, for `0 < ‖a‖ ≤ 1` and every `M`, the norm of the Fourier transform of `c · exp (q / a)` at
  `b` is at most a constant times the supremum over `K` of `‖exp (q / a)‖` divided by
  `(‖a‖ * (1 + ‖b‖)) ^ M`.

## Relation to the literature

The results of this file include the Stone–Weierstrass theorem for a monoid of functions, Fourier
inversion on a compact quotient of an abelian group, and the decay of Fourier transforms by
integration by parts.


 ## Dual families of characters and Fourier inversion 

### `IsDualFamily`

 `IsDualFamily B₀ χ` says that `i ↦ χ i` is an injective homomorphism from `I` to the group of
continuous unitary characters of `B` that are trivial on `B₀`, and that the common kernel of the
`χ i` lies in `B₀`. 

### `IsDualFamily.periodic`

 Each `χ i` is continuous and periodic under `B₀`. 

### `IsDualFamily.add_left`

 `χ i x` is multiplicative in the index `i`. 

### `IsDualFamily.add_right`

 `χ i x` is multiplicative in the argument `x`. 

### `IsDualFamily.norm_eq_one`

 The values have absolute value one. 

### `IsDualFamily.mem_of_forall_eq_one`

 A point at which all the characters are `1` lies in `B₀`. 

### `IsDualFamily.eq_zero_of_forall_eq_one`

 Only the index `0` can give the trivial character. 

### `RespectsQuasiPeriods`

 A quasi-period of `F` is a pair `(a, c)` such that `c * F (x + a) = F x` for all `x`.
`RespectsQuasiPeriods ψ F` says that `ψ a = c` for every quasi-period `(a, c)` of `F`. 

### `stone_weierstrass_span`

 Stone–Weierstrass for monoids: let `M` be a submonoid of `C(K, ℂ)`, `K` compact, that is
closed under conjugation and separates points (two points at which all `f ∈ M` agree are
equal). Then the linear span of `M` is dense in `C(K, ℂ)`. 

 ### First properties of the characters 

### `apply_ne_zero`

 The characters of a dual family do not vanish, having absolute value one. 

### `isContPeriodic_mul`

 The product of a character of a dual family with a continuous `B₀`-periodic function is again
continuous and `B₀`-periodic. 

### `eq_of_forall_apply_out_eq`

 The characters of a dual family separate the points of `B ⧸ B₀` (evaluated at the chosen
representatives `p.out`, `q.out`). 

 ### Orthogonality of the characters 

### `quotMean_eq_ite`

 Orthogonality: for a dual family `χ` of characters of `B` modulo `B₀`, the mean of `χ i` over
`B ⧸ B₀` is `1` if `i = 0` and `0` otherwise. 

### `tsum_coeff_eq_quotMean`

 Let `χ` be a dual family of characters of `B` modulo `B₀` (characters `χ i` trivial on `B₀`,
with `i ↦ χ i` an injective homomorphism, separating `B ⧸ B₀`). For a countable type `ι`, a map
`ξ : ι → I` that vanishes exactly on `S`, and summable coefficients `c`, the mean over `B ⧸ B₀` of
`x ↦ ∑' i, χ (ξ i) x * c i` is the sum of `c` over `S`. 

 ### Fourier coefficients and Fourier inversion 

### `mul_quotMean_translate`

 Let `χ` be a dual family of characters of `B` modulo `B₀` and `F` continuous and `B₀`-periodic.
Translating `F` by `a` divides its Fourier coefficient (the mean of `χ i * F` over `B ⧸ B₀`) by
`χ i a`. 

### `fourier_inversion`

 Fourier inversion for a dual family `χ` of characters of `B` modulo `B₀` (characters `χ i`
trivial on `B₀`, with `i ↦ χ i` an injective homomorphism, separating `B ⧸ B₀`): if `F` is
continuous and `B₀`-periodic and its Fourier coefficients `a i` (the means of `χ i * F` over
`B ⧸ B₀`) are summable, then the series `∑' i, χ (-i) x * a i` has sum `F x` for every `x`. 

### `eq_zero_of_quotMean_mul_eq_zero`

 Let `χ` be a dual family of characters of `B` modulo `B₀`, and let `F` be continuous and
`B₀`-periodic. Suppose that the Fourier coefficient of `F` at `i` (the mean of `χ i * F` over
`B ⧸ B₀`) is zero whenever `χ i` respects the quasi-periods of `F` (that is, `χ i a = c` whenever
`c * F (x + a) = F x` for all `x`). Then `F = 0`. 


## Decay of Fourier transforms by integration by parts

The estimate `New.exists_pow_mul_norm_fourier_le` is proved by induction on the order of decay, with
one integration by parts at each step. Two lemmas prepare that step: a lower bound for the factor
by which the integration by parts multiplies the Fourier transform, and the product rule for
`g * exp (h / a)`.


### `New.one_add_norm_le_norm_I_add_inner`

 For a vector `b` of a real inner product space and `v = ‖b‖⁻¹ • b` (which is `0` if `b = 0`),
the number `i + 2 π i ⟪b, v⟫` has norm at least `1 + ‖b‖`: its imaginary part is `1 + 2 π ‖b‖`. 

### `fderiv_mul_exp_div_apply`

 The product rule for the derivative of `g * exp (h / a)` in the direction `v`. 

### `New.exists_pow_mul_norm_fourier_le`

 Let `c` and `q` be smooth functions of a parameter `s : T` and a point `x : ℂ^n`, with
`c (s, x) = 0` for `x` off the compact set `K`. For each `M` there is a `C` such that, for
`‖s‖ ≤ 1`, `‖a‖ ≤ 1`, `a ≠ 0` and every bound `D` of `‖exp (q (s, ·) / a)‖` on `K`, the Fourier
transform of `c (s, ·) * exp (q (s, ·) / a)` at any `b`, times `(‖a‖ * (1 + ‖b‖)) ^ M`, has norm at
most `C * D`. Proof: induction on `M`, for all parameter spaces `T`. One integration by parts in the
direction `v` of `b` gives a function of the same kind, with `v` and `a` as further parameters. 
