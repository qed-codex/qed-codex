---
{
  "module": "src/Lib/ClassField/HeckeL/EulerProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/EulerProduct.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/EulerProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Euler products over primes of a number field and densities at primes of degree one

This file treats Hecke characters of a number field `K`, given by their finite part `ψ`, a
character of the finite ideles `(𝔸f K)ˣ`, and Euler products with coefficients `a v`, `‖a v‖ ≤ 1`,
over the primes `v` of `K`, as functions of a real variable `s > 1`.

* `New.IsHeckeOfType`: `ψ` has open kernel and `ψ x * ∏ w, (Φ w x / ‖Φ w x‖) ^ n w = 1` on `Kˣ`;
  `New.heckeCoeff ψ S` is the value of `ψ` at the local idele of the chosen uniformiser for `v ∉ S`,
  and `0` for `v ∈ S`.
* `New.eulerProd`: the product `∏ (1 - a v * q ^ (-s))⁻¹`, defined as `exp` of a sum of logarithms;
  `New.hasProd_eulerProd` says that it is the limit of the partial products.
* `New.hasSum_eulerProd`: for a completely multiplicative function on ideals, of modulus at most
  `1`, the product equals the Dirichlet series.
* `New.HasPrimeDensity`: the Dirichlet mean of `a` over the primes of degree one. Densities are
  linear and monotone (`New.HasPrimeDensity.sum`, `New.HasPrimeDensity.re_le_re`).
* `New.hasPrimeDensity_of_tendsto`: the density is read off from the order of the pole or zero of
  the product at `1`.

Up to a bounded error, the logarithm of the product is the sum of `a v * q ^ (-s)` over the primes
of degree one (`New.norm_log_one_add_neg_mul_cpow_sub_ite_le_of_norm_le_one`,
`New.sum_inv_minFac_sq_le_finrank`). Here `New.FinPlace K` is the type of nonzero primes of `𝓞 K`,
`q = v.q` is the absolute norm of `v`, and degree one means that `q` is prime.

Notions from other files:
* `New.locIdele v`: sends `x ∈ K_vˣ` to the finite idele with component `x` at `v` and `1`
  elsewhere; `New.uniformizer v` is a chosen uniformiser of the completion `K_v`.
* `Φ w` (class `New.PlaceEmbedding`): a chosen complex embedding of `K` inducing the infinite
  place `w`.

## Relation to the literature

Known; see `Lib.ClassField.HeckeL.ContinuationAtOne` for sources.


### `IsHeckeOfType`

 The character `ψ` of the finite ideles is the finite part of a Hecke character of type `n`,
where `n` gives an integer exponent `n w` to each infinite place `w`: the kernel of `ψ` is open,
and `ψ x * ∏ w, (Φ w x / ‖Φ w x‖) ^ n w = 1` for `x ∈ Kˣ`, with `Φ w` the chosen complex embedding
inducing `w` and `x` read as a finite idele by the diagonal embedding. 

### `CharUnramifiedAt`

 `ψ` is unramified at the finite place `v`: it is `1` on the units of the completion `K_v` of
valuation `1`, read as finite ideles by `New.locIdele v`. 

### `heckeCoeff`

 The function on finite places sending `v ∉ S` to the value of `ψ` at the local idele of the
chosen uniformiser `uniformizer v` of `K_v`, and `v ∈ S` to `0`. 

### `eulerProd`

 The Euler product `∏ (1 - a v * q ^ (-s))⁻¹` over the primes `v` of `K`, with `q = v.q` the norm
of `v`, as a function of real `s`. It is written `exp (-∑' v, log (1 + -(a v * q ^ (-s))))`, in the
form `log (1 + w)` of Mathlib's bounds for the logarithm. The value at `s` is the limit of this
expression at `s` within `(1, ∞)`: for `‖a v‖ ≤ 1` and `s > 1` it is the expression itself
(`New.eulerProd_eq_exp`, `New.hasProd_eulerProd`), at `s = 1` it is the limit from the right if that
exists, and for `s < 1` it has no meaning. With `a = heckeCoeff ψ S` and `ψ` unramified at every
`v ∉ S` it is the Euler product of the Hecke `L`-function of `ψ` without the factors at `S`. 

### `HasPrimeDensity`

 The Dirichlet mean of `a` over the primes of degree one (those of prime norm `q`) is `l`, with
a bounded error: for `s > 1` near `1` the series `∑ a v * q ^ (-s)` over these primes converges,
and its sum is `l * log (1 / (s - 1)) + x s` with `x` bounded as `s → 1⁺`. 

### `ncard_primesOver_le_finrank`

 At most `[K : ℚ]` primes of `K` lie over a maximal ideal of `ℤ`. 

### `sum_inv_minFac_sq_le_finrank`

 For a finite set `u` of primes of `K`, the sum over `v ∈ u` of `1 / p ^ 2`, with `p` the least
prime factor of the norm `v.q`, is at most the degree `[K : ℚ]`. 

### `summable_absNorm_rpow`

 For real `s > 1` the series of `N(I) ^ (-s)` over all ideals `I` of `𝓞 K` converges, with
`N(I) = absNorm I` (the zero ideal has norm `0` and term `0`). 

### `norm_neg_mul_cpow_le_rpow_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `t ≤ s`, the term `-(a v * q ^ (-s))` of the Euler factor has norm at
most `q ^ (-t)`, with `q = v.q` the norm of the prime `v`. 

### `norm_neg_mul_cpow_le_inv_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `s ≥ 1`, the term `-(a v * q ^ (-s))` has norm at most `1 / q`. 

### `norm_log_one_add_neg_mul_cpow_sub_ite_le_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `s ≥ 1`, the logarithm of the Euler factor `1 - a v * q ^ (-s)`
differs from `-(a v * q ^ (-s))` (if `q` is prime) or from `0` (if not) by at most `2 / p ^ 2`, with
`p` the least prime factor of `q`. 

### `one_add_neg_mul_cpow_mem_slitPlane_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `s ≥ 1`, the Euler factor `1 - a v * q ^ (-s)` lies in the slit plane,
where the logarithm is continuous. 

### `norm_log_one_add_neg_mul_cpow_le_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `1 ≤ σ ≤ s`, the logarithm of the Euler factor `1 - a v * q ^ (-s)` has
norm at most `2 * q ^ (-σ)`. 

### `eulerProd_eq_exp`

 If `‖a v‖ ≤ 1` and `s > 1`, the series `∑ v, log (1 - a v * q ^ (-s))` converges, its sum is
continuous at `s`, and `New.eulerProd a s` is the exponential of minus this sum. 

### `eulerProd_eq_exp_neg_tsum_log_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `s > 1`, `New.eulerProd a s` is the exponential of minus the sum of
the logarithms of the Euler factors `1 - a v * q ^ (-s)`. 

### `summable_log_one_add_neg_mul_cpow_of_norm_le_one`

 For `‖a v‖ ≤ 1` and real `s > 1`, the logarithms of the Euler factors `1 - a v * q ^ (-s)` are
summable over the primes `v`. 

### `hasProd_eulerProd`

 If `‖a v‖ ≤ 1` for all primes `v` of `K` and `s > 1` is real, the Euler product
`∏ v, (1 - a v * q ^ (-s))⁻¹` converges unconditionally to `New.eulerProd a s`. 

### `eulerProd_erase`

 For `‖a v‖ ≤ 1`, a finite set `Q` of primes and `P s = ∏ w ∈ Q, (1 - a w * q_w ^ (-s))`: `P` is
analytic at the real point `1`, `P 1 ≠ 0`, and for real `s > 1` setting the coefficients at `Q` to
zero multiplies the Euler product by `P s`. 

### `hasPrimeDensity_of_tendsto`

 If `‖a v‖ ≤ 1` for all `v` and `(s - 1) ^ l * eulerProd a s` tends to some `c ≠ 0` as real
`s ↓ 1`, with `l` a complex number, then `a` has density `l` over the primes of degree one. This
means `HasPrimeDensity a l`: the sum of `a v * q_v ^ (-s)` over the primes `v` of prime norm `q_v`
equals `l * log (1 / (s - 1))` plus a term bounded as `s ↓ 1`. (A pole of order `m` is the case
`l = m`, a zero of order `m` the case `l = -m`.) 

### `eulerProd_ne_zero_and_abs_log_norm_le`

 If `‖a v‖ ≤ 1` for all `v` and `s ≥ σ ≥ 2` are real, the Euler product with coefficients `a` is
nonzero at `s`, and the logarithm of its modulus has absolute value at most
`2 * [K : ℚ] * 2 ^ (2 - σ)`. 

### `hasSum_eulerProd`

 Euler product: for `χ` multiplicative on the ideals of `𝓞 K` with `‖χ I‖ ≤ 1` and real `s > 1`,
the series `∑ I, χ I * N(I) ^ (-s)` converges to the Euler product with coefficients `χ v`. 

### `HasPrimeDensity.sum`

 Densities are linear: if each `a i` has density `l i` over the primes of degree one, then
`∑ i, w i * a i` has density `∑ i, w i * l i`. 

### `HasPrimeDensity.re_le_re`

 Suppose `a` has density `l` and `b` has density `l'` in the Dirichlet sense of
`HasPrimeDensity`: over the primes `v` of degree one (prime norm `q_v`),
`∑ a v * q_v ^ (-s) = l * log (1 / (s - 1)) + O(1)` as `s ↓ 1`, and likewise for `b` and `l'`.
Suppose also that `Re (a v) ≤ Re (b v)` for all but finitely many primes `v` of degree one. Then
`Re l ≤ Re l'`. 

### `hasPrimeDensity_const`

 For `c ∈ ℂ` the constant family `v ↦ c` has density `c` over the primes of degree one of `K`, in
the sense of `New.HasPrimeDensity`. 

### `frequently_prime_q`

 A number field `K` has infinitely many primes of degree one, that is, finite places `w` whose
absolute norm `w.q` is a prime number. 

### `hasPrimeDensity_card_degree_one`

 Let `L/K` be an extension of number fields and `c ∈ ℂ`. Consider the family that sends `v` to
`c` times the number of places `w` of `L` above `v` whose residue field has the same cardinality
`q_w = q_v`, that is, those of relative residue degree one. This family has density `c` over the
primes of degree one of `K`: the sum of its values times `q_v ^ (-s)` over the `v` of prime norm is
`c * log (1 / (s - 1))` plus a term bounded as `s ↓ 1`. 
