---
{
  "module": "src/Lib/General/Measure/HaarNormalisation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/HaarNormalisation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/HaarNormalisation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniqueness of Haar measure, integrals over subgroups and Gaussian normalisation of volumes

The file treats three topics of measure theory. Two additive Haar measures on a locally compact,
second countable group agree if some real function has integral 1 for both. Integrals over compact
or open subgroups are computed by translation invariance, orthogonality of characters and reduction
to finite sums. A normalisation of volumes by Gaussian integrals is defined. It holds for `ℝ` and
`ℂ` and passes to binary products and finite powers under σ-finiteness assumptions.

## Main definitions and results

* `New.addHaar_eq_of_integral_eq_one`: uniqueness of additive Haar measure, with the constant fixed
  by the integral of one test function.
* `New.setIntegral_char`: orthogonality for a multiplicative function over an open subgroup.
* `New.setIntegral_eq_finsum`: over a compact `M`, a function constant on the cosets of an open
  subgroup `L` integrates to `ν (L ∩ M)` times a finite sum over `M ⧸ (L ∩ M)`.
* `New.HasGaussianIntegral`: the Gaussian normalisation of a volume.
* `New.HasGaussianIntegral.pi`: the normalisation on a finite power.
* `New.lintegral_inv_add_rpow`: the integral of `(c + q x) ^ (-s)`, computed through the Gamma
  function.


 ## Uniqueness of Haar measure 

### `New.addHaar_eq_of_integral_eq_one`

 Let `μ` and `ν` be additive Haar measures on a locally compact, second countable group. If some
real function has integral 1 for both, then `μ = ν`. 


## Integrals over subgroups

Integrals over a subgroup `M` of a topological abelian group `V`, for a translation-invariant Borel
measure `ν`.


### `setIntegral_add_left_eq_self_of_mem`

 For a left-invariant measure `ν` and a subgroup `M`, the integral over `M` is unchanged by
translating the integrand by an element of `M`. 

### `setIntegral_char`

 Orthogonality: let `ν` be a left-invariant measure on `V` and `χ : V → ℂ` satisfy
`χ (x + y) = χ x * χ y`. The integral of `χ` over an open subgroup `M` is the measure of `M` (read
as `0` if infinite) when `χ = 1` on `M`, and `0` otherwise. 

### `setIntegral_eq_finsum`

 Let `M` be a compact and `L` an open subgroup of `V`, and `ν` a left-invariant measure that is
finite on compact sets. If `F` is constant on the cosets of `L ∩ M` in `M`, its integral over `M` is
`ν (L ∩ M)` times the sum of its values on these cosets; `q.out` is a chosen representative of the
coset `q`. 


## Volumes normalised by a Gaussian integral

A way to fix the normalisation of a volume without choosing a basis. For σ-finite volumes it passes
to binary products and finite powers, with the sum of the functions and the sum of the exponents.


### `lintegral_ofReal_eq_of_integral_eq`

 If `f` is nonnegative almost everywhere and its Bochner integral is `v ≠ 0`, then its lower
Lebesgue integral is `v`. No integrability is assumed: it follows from `v ≠ 0`. 

### `lintegral_const_mul_rpow_mul_exp_neg_mul_Ioi`

 The Gamma integral as a lower integral: for positive `b`, `r` and `K`, the integral of
`K t ^ (b - 1) exp (-r t)` over `t > 0` is `K r ^ (-b) Γ(b)`. 

### `HasGaussianIntegral`

 Gaussian normalisation of the volume on `V` for the real function `q` with exponent `a`: for
every `t > 0`, the integral of `exp (-t * q x)` over `V` equals `(π / t) ^ a`. 

### `HasGaussianIntegral.integral_exp_eq`

 For `t > 0`, the integral of `exp (-t * q x)` over `V` is `(π / t) ^ a`. 

### `lintegral_inv_add_rpow`

 Let the volume on `V` be σ-finite with `∫ exp (-t q) = (π / t) ^ a` for all `t > 0`, and let
`q ≥ 0` be measurable. For `c > 0`, `s > 0` and `a < s`, the lower integral of `(c + q) ^ (-s)` is
`π ^ a c ^ (a - s) Γ(s - a) / Γ(s)`. 

### `instance : HasGaussianIntegral (1 / 2) fun x : ℝ ↦ x ^ 2`

 The Gaussian integral on `ℝ`: the integral of `exp (-t x²)` is `(π / t) ^ (1 / 2)`. 

### `instance : HasGaussianIntegral 1 fun z : ℂ ↦ ‖z‖ ^ 2`

 The Gaussian integral on `ℂ`: the integral of `exp (-t ‖z‖²)` is `π / t`. 

### `instance [h : HasGaussianIntegral a q] [h' : HasGaussianIntegral b q'] : HasGaussianIntegral (a + b) fun x : V × W ↦ q x.1 + q' x.2`

 If the volumes on `V` (σ-finite) and `W` (s-finite) satisfy `∫ exp (-t q) = (π / t) ^ a` and
`∫ exp (-t q') = (π / t) ^ b` for all `t > 0`, then the volume on `V × W` satisfies the same with
exponent `a + b` for the sum of `q` and `q'`. 

### `HasGaussianIntegral.pi`

 If the volume on `V` is σ-finite and satisfies `∫ exp (-t q) = (π / t) ^ a` for all `t > 0`,
then the volume on `ι → V` satisfies the same with exponent `a * card ι` for `x ↦ ∑ i, q (x i)`. 
