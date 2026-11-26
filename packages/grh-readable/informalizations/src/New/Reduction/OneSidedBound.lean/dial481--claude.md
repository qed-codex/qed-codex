---
{
  "module": "src/New/Reduction/OneSidedBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The one-sided bound, and the theorem in half-plane form

For admissible data at an integer `x`, the main inequality and the prime number theorem at a much
larger cut-off `x₁` give the bound `R_{q₀}(x) ≤ x ^ (-1/2 + ε)` for large `x`; the one-sided
criterion turns it into the non-vanishing of all Dirichlet `L`-functions in `re s > 1/2`.

Notions from other files:
* `Parameters`: a multiple `q₀ = P.q₀` of `18480` and a prime `d = P.d ≡ q₀ / 2 - 1` modulo `q₀`.
* `primeRemainder d q x`: the remainder `R_q(x) = ∑_{n ≤ x} λ(n) (1/n - 1/x) - log x / φ(q) - c_q`.
  Here `λ(n) = Λ(n) (1 - chiK d n)` for `n ≡ 1` modulo `q` and `0` otherwise, with `chiK d` the
  Legendre symbol modulo `d`; for odd `d` prime to `q`, `c_q` is the constant with `R_q(x) → 0`.
* `Data P`: admissible data, among them the scales `x`, `x₁`, `b`, `a = x b`, the number of lifts
  `m` and two finite sets of places of a number field, `Φ_a = D.aPlaces` and `Φ_b = D.bPlaces`.


### `Data.primeRemainder_le`

 Let `q₀ = P.q₀` and `d = P.d` be the modulus and the prime of the parameters `P`. Let
`R_q(y) = primeRemainder d q y = ∑_{n ≤ y} λ(n) (1/n - 1/y) - log y / φ(q) - c_q`. Admissible data
`D` for `P` include scales `x = D.x`, `x₁ = D.x₁` and `b` (`D.logB = log b`) with
`(log b) ^ 100 ≤ x`, `x ^ 10⁶ ≤ x₁`, `x₁ ^ 10⁶ ≤ b` and `log log b ≥ 10¹² P.constantBound`, and an
integer `m = D.m` in `[√x, 2 √x]`. Then `R_{q₀}(x) ≤ φ(q₀) log⁶ b / m + |R_{q₀}(x₁)| + log
b · |R₁(x₁)|`. 

### `eventually_exists_data_scales`

 Let `0 < ε < 1/100`. A term `D : Data P` (admissible data) bundles all the choices that the main
inequality needs, among them integer scales `x`, `x₁`, `b` with `x ^ 10⁶ ≤ x₁` and `x₁ ^ 10⁶ ≤ b`
(`D.logX₁ = log x₁`, `D.logB = log b`) and a power of two `m = D.m` in `[√x, 2 √x]`. For every large
integer `x` such data exist with `D.x = x`, `log b ≤ 2 x ^ ε`, `√x ≤ m` and
`x ^ (ε / 12) ≤ log x₁`. 

### `eventually_abs_primeRemainder_exp_le`

 Let `q₀ = P.q₀` and `d = P.d` be the modulus and the prime of the parameters `P`, and let
`ε > 0`. Let `R_q(y) = primeRemainder d q y = ∑_{n ≤ y} λ(n) (1/n - 1/y) - log y / φ(q) - c_q`. For
all large integers `x` and all `l ≥ x ^ (ε / 12)`, the values `|R_{q₀}(exp l)|` and `|R₁(exp l)|`
are at most `x ^ (-2)`, by the prime number theorem. 

### `eventually_primeRemainder_natCast_le`

 The one-sided bound at integers. Let `q₀ = P.q₀` and `d = P.d` be the modulus and the prime of
the parameters `P`, and let `0 < ε < 1/100`. Let
`R(y) = primeRemainder d q₀ y = ∑_{n ≤ y} λ(n) (1/n - 1/y) - log y / φ(q₀) - c`, where
`λ(n) = Λ(n) (1 - (n/d))` for `n ≡ 1` modulo `q₀` and `0` otherwise, `(·/d)` is the Legendre symbol,
and `c` is the constant with `R(y) → 0`. Then `R(x) ≤ (64 φ(q₀) + 3) x ^ (-1/2 + 6 ε)` for all large
integers `x`. 

### `primeRemainder_sub_primeRemainder_floor_le`

 Let `d` be a prime, `q > 0`, and `R_q(y) = primeRemainder d q y = ∑_{n ≤ y} λ(n) (1/n - 1/y) -
log y / φ(q) - c_q`. Then `R_q(y) - R_q(⌊y⌋) ≤ 26 / y` for `y ≥ 2`. 

### `natFloor_rpow_le_two_mul_rpow`

 For `y ≥ 2` and `-1 ≤ t ≤ 0` we have `⌊y⌋ ^ t ≤ 2 y ^ t`, since `y / 2 ≤ ⌊y⌋`. 

### `dvd_two_mul_succ_and_not_dvd_succ`

 If `q₀ > 0` is even and `d ≡ q₀ / 2 - 1` modulo `q₀`, then `q₀` divides `2 (d + 1)` but not
`d + 1`. This is the form of the congruence in `Parameters`. 

### `eventually_primeRemainder_le_rpow`

 **One-sided bound.** Let `q₀ > 0` be a multiple of `18480`, let `d ≡ q₀ / 2 - 1` modulo `q₀` be
a prime, and let `ε > 0`. Then `R = primeRemainder d q₀` satisfies `R(y) ≤ y ^ (-1/2 + ε)` for all
large real `y`. 

### `grh`

 **Main theorem**, in half-plane form: no Dirichlet `L`-function vanishes in `re s > 1/2`
(with `s ≠ 1` for a principal character). 
