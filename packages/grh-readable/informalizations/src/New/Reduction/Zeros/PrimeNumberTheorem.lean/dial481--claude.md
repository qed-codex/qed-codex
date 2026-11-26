---
{
  "module": "src/New/Reduction/Zeros/PrimeNumberTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The prime number theorem for the remainders `R_q`

Let `d` be a prime and `q ≥ 1`. The remainder `R_q(y)` is an integral of the error `𝓔_q(t)` in the
weighted count (`primeRemainder_eq_integral_countError_sub`), so it varies slowly. For odd `d` prime
to `q` its absolute value is at most `(log y) ^ (-B)` for all large `y`, for every natural number
`B`; so it tends to `0`, which characterises the constant `c_q` in its definition.

Notions from other files:
* `lambdaKResidueClass d q n` is `λ(n) = Λ(n) (1 - (n/d))` for `n ≡ 1` mod `q`, and `0` for other
  `n`.
* `entireL ψ` is `L(s, ψ)`, multiplied by `s - 1` if `ψ` is principal; `quadTwist ψ d` is the
  product of `ψ` and the Legendre symbol `(·/d)`.
* `logDerivMean d q` is the function `G_q` that continues `∑ λ(n) n ^ (-s) - s / (φ(q) (s - 1))`
  when `d` is odd and prime to `q`.
* `primeRemainder d q y` is `R_q(y) = ∑_{n ≤ y} λ(n) (1/n - 1/y) - log y / φ(q) - c_q` with
  `c_q = re G_q(1)`.

## Relation to the literature

Known result: Prime number theorem in arithmetic progressions with an error term that saves every
power of the logarithm. It is a case of the Siegel–Walfisz theorem. Source: Montgomery and Vaughan,
Multiplicative Number Theory I, 2007, Cor. 11.19. Form here: the modulus is fixed, and the count is
the smoothed sum `∑_{n ≤ y} λ(n) (1/n - 1/y)` over the prime powers `n ≡ 1` mod `q`; for `d ≡ 3` mod
`4` the primes that split in `ℚ(√-d)` have weight zero.


### `sum_Icc_vonMangoldt_le_six_mul`

 Chebyshev's bound with a round constant: `∑_{n ≤ z} Λ(n) ≤ 6 z` for `z ≥ 0`. 

### `countError`

 The error `𝓔_q(t) = ∑_{n ≤ t} λ(n) - t / φ(q)` in the count with the weights
`λ = lambdaKResidueClass d q`, that is `λ(n) = Λ(n) (1 - (n/d))` for `n ≡ 1` mod `q` and `λ(n) = 0`
otherwise. 

### `abs_countError_le`

 Let `d` be a prime and `q ≠ 0`, and let `λ(n) = lambdaKResidueClass d q n` be `Λ(n) (1 - (n/d))`
for `n ≡ 1` mod `q` and `0` otherwise. The error `𝓔_q(t) = countError d q t`, that is
`∑_{n ≤ t} λ(n) - t / φ(q)`, satisfies `|𝓔_q(t)| ≤ 13 t` for `t ≥ 0`, by Chebyshev's bound. 

### `intervalIntegrable_countError_div_sq`

 Let `d` be a prime and let `λ(n) = lambdaKResidueClass d q n` be `Λ(n) (1 - (n/d))` for `n ≡ 1`
mod `q` and `0` otherwise. For the error `𝓔_q(t) = countError d q t`, that is
`∑_{n ≤ t} λ(n) - t / φ(q)`, the function `𝓔_q(t) t⁻²` is integrable on every interval `[y, z]` with
`1 ≤ y ≤ z`. 

### `primeRemainder_eq_integral_countError_sub`

 For `y ≥ 1` the remainder `R_q = primeRemainder d q`, that is `R_q(y) = ∑_{n ≤ y} λ(n) (1/n -
1/y) - log y / φ(q) - c_q` with `c_q = re G_q(1)`, equals `∫₁^y 𝓔_q(t) t⁻² dt - c_q`, where
`𝓔_q(t) = countError d q t` is `∑_{n ≤ t} λ(n) - t / φ(q)`. 

### `abs_primeRemainder_sub_le`

 Let `d` be a prime and `q ≠ 0`, and let `λ(n) = lambdaKResidueClass d q n` be `Λ(n) (1 - (n/d))`
for `n ≡ 1` mod `q` and `0` otherwise. The remainder `R_q = primeRemainder d q`, that is
`R_q(y) = ∑_{n ≤ y} λ(n) (1/n - 1/y) - log y / φ(q) - c_q`, varies slowly:
`|R_q(z) - R_q(y)| ≤ 13 (z - y) / y` for `1 ≤ y ≤ z`. 

### `abs_primeRemainder_exp_sub_le`

 Let `d` be a prime and `q ≠ 0`. In the variable `v = log y` the remainder
`R_q = primeRemainder d q` is Lipschitz: `|R_q(e^v) - R_q(e^u)| ≤ 26 (v - u)` for
`0 ≤ u ≤ v ≤ u + 1`. 

### `analyticAt_logDerivMean`

 For a character `ψ` mod `q` let `L_ψ = entireL ψ` be `L(s, ψ)`, times `s - 1` if `ψ` is
principal, and let `ψ' = quadTwist ψ d` be `ψ (·/d)`. The function `logDerivMean d q`, that is
`(∑_ψ (logDeriv L_ψ' - logDeriv L_ψ) - 1) / φ(q)`, is analytic at every point where no `L_ψ` and no
`L_ψ'` vanishes. 

### `norm_logDerivMean_le`

 For a character `ψ` mod `q` let `L_ψ = entireL ψ` be `L(s, ψ)`, times `s - 1` if `ψ` is
principal, and let `ψ' = quadTwist ψ d` be `ψ (·/d)`. If all `logDeriv L_ψ` and `logDeriv L_ψ'` have
norm at most `C` at `s`, then `logDerivMean d q = (∑_ψ (logDeriv L_ψ' - logDeriv L_ψ) - 1) / φ(q)`
has norm at most `2 C N + 1` at `s`, where `N` is the number of characters mod `q`. 

### `eventually_norm_logDerivMean_div_le`

 Let `d` be a prime and `q ≠ 0`. Let `G_q = logDerivMean d q` be the mean over the characters `ψ`
mod `q` of the logarithmic derivatives of `L(s, ψ (·/d)) / L(s, ψ)`, less `1 / φ(q)`; here the
`L`-function of a principal character is multiplied by `s - 1`. For all large `l` the function
`G_q(s) / s` is holomorphic and of norm at most `l²⁶` on `re s ≥ 1 - l⁻²⁶`, `|s| ≤ e^l`. 

### `eventually_abs_primeRemainder_le`

 **Prime number theorem** in the class `1` mod `q`, with weights `λ(n) = Λ(n) (1 - (n/d))`. Let
`d` be an odd prime and `q` prime to `d`. For every natural number `B` the remainder
`primeRemainder d q`, that is `R_q(y) = ∑_{n ≤ y, n ≡ 1} λ(n) (1/n - 1/y) - log y / φ(q) - c_q`,
satisfies `|R_q(y)| ≤ (log y) ^ (-B)` for all large `y`, by a Tauberian theorem applied to the
Laplace transform of `v ↦ R_q(e ^ v)`; it also follows from the Siegel–Walfisz theorem. 

### `tendsto_primeRemainder`

 For an odd prime `d` and `q` prime to `d` the remainder `primeRemainder d q` tends to `0` at
infinity. Thus the constant `c_q = re (logDerivMean d q 1)` subtracted in it is the limit of
`∑_{n ≤ y, n ≡ 1 mod q} Λ(n) (1 - (n/d)) (1/n - 1/y) - log y / φ(q)`. 
