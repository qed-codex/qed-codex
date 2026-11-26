---
{
  "module": "src/Lib/Analytic/QuadraticTwist.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A prime `d` in a class whose quadratic twists have no zero in a box

Fix a class modulo `N` whose primes are `≡ 7` modulo `8` and prime to `N`, and a box
`re s ≥ β = 1/2 + 9 δ`, `|im s| ≤ H`. A prime `d` of the class is bad (`IsBadPrime`) if some
`L(s, ξ (·/d))`, with `ξ` modulo `N`, has a zero in the box. The main estimate is the count
`zero_density_quadTwist`: there are `O(X ^ (1 - δ / 2))` bad primes up to `X`. Such a count also
follows from the large sieve inequality for real characters; the proof here needs only the
Pólya–Vinogradov inequality, because theta series keep all sums short.

1. For a primitive character `χ ≠ 1` of conductor `q ≤ T²` let `J(χ, T)` be the integral over
   `u ≥ 1 / T` of `|θ_χ(u)| + |θ_{μχ}(u)|` against `du / u` (`thetaTailIntegral`). If `χ` has parity
   `j`, the Mellin transform of `θ_χ` at `s - 1/2` is `Γ_j L`, and by the functional equation the
   integral of `|θ_χ(u)| du / u` over `u < q ^ (-1/2)` equals that over `u > q ^ (-1/2)`. The
   truncated transform `𝓜` of `θ_{μχ}` (`mollifier`) approximates `Γ_j / L` on `re s = 2`.
2. For large `T` a zero in the box forces `J(χ, T) > T ^ (2 δ)`
   (`eventually_rpow_lt_thetaTailIntegral`). Otherwise `Γ_j L 𝓜 - Γ_j²` is `≪ T ^ (4 δ)` on
   `re s = 1/2` and `≪ 1 / T` on `re s = 2`, so it is small at the zero by the three-lines theorem,
   while it equals `-Γ_j²` there.
3. In the mean over `v ≤ T²` the theta series with coefficients `αₙ (-v/n°)`, where `n°` is the odd
   part of `n`, are small (`sum_sq_thetaSeries_jacobiSym_le`): expand the square, bound the pairs
   with `(n n')°` a square trivially and the others by Pólya–Vinogradov. So the sum of the `J` is
   `≪ T ^ (2 + δ)`.
4. By reciprocity `(n/d) = (-d/n°)`, so 2 and 3 give the count, with `T² = N X`, after passing from
   `ξ` to the primitive character that induces it.
5. If all primes of an invertible class were bad, the sum of `log p / p` over the class would
   converge; it diverges, so some prime of the class is not bad
   (`exists_entireL_quadTwist_ne_zero`).

Notions from other files:
* `gaussianMonomial j` is the weight `w(z) = z ^ j e^(-π z²)` of parity `j`, and `gaussianMellin j`
  is its Mellin transform `Γ_j(s) = ∫_0^∞ w(z) z ^ s dz / z`.
* `thetaSeries j c u` is `θ_c(u) = u ^ (1/2) ∑_{n ≥ 1} c(n) w(n u)`.
* `quadTwist χ d` is the character `χ (·/d)` modulo `N d`, for `χ` modulo `N` and a prime `d`.

## Relation to the literature

Known result: zero density for quadratic twists by mean values over real characters. Sources:
Jutila, On mean values of Dirichlet polynomials with real characters, Acta Arith. 27 (1975);
Heath-Brown, A mean value estimate for real character sums, Acta Arith. 72 (1995). Form here: a weak
density bound for the twists of the characters of a fixed modulus, by a smoothed mean square of
Jacobi symbol sums.


### `thetaTailIntegral`

 The measure of cancellation `J(c, T) = ∫_{1/T}^∞ (|θ_c(u)| + |θ_{μc}(u)|) du / u` of a sequence
`c`, where `θ_c` is its theta series of parity `j`. 

### `mollifier`

 The mollifier `𝓜(s) = ∫_{1/T}^∞ θ_{μc}(u) u ^ (s - 1/2) du / u`, where `θ_{μc}` is the theta
series with the coefficients `c(n) μ(n)`. For a character `c = χ` it is the truncated integral for
`Γ_j / L`. 

### `thetaTailIntegral_eq_add`

 For `|c(n)| ≤ 1` and `T > 0` the tail integral `J(c, T)` (`thetaTailIntegral`) is the sum of
the tail integrals of `|θ_c(u)| / u` and `|θ_{μc}(u)| / u`. 

### `mollifier_differentiableOn_and_bounded`

 For `|c(n)| ≤ 1` and `T > 0` the mollifier `𝓜` of `c`, the transform of the theta series of
`c μ` cut to `u > 1 / T`, is holomorphic in `re s > 0` and bounded on `1/2 ≤ re s ≤ 2`. 

### `norm_integral_cpow_smul_thetaSeries_le`

 On `re z = 1/2` we have `|∫_r^∞ θ(u) u ^ (z - 1/2) du / u| ≤ ∫_r^∞ |θ(u)| du / u` for `r ≥ 0`,
as `u ^ (z - 1/2)` has modulus `1`; here `θ` is the theta series of `c`. 

### `norm_mollifier_le`

 For `|c(n)| ≤ 1` and `T > 0`, on `re z = 1/2` the mollifier `𝓜` is at most the tail integral
`J(c, T)` in absolute value. 

### `norm_cpow_smul_thetaSeries_le`

 For `|c(n)| ≤ 1`, `re z = 2` and `u > 0`, the trivial bound on the theta series `θ` of `c`
gives `|u ^ (z - 1/2) θ(u) / u| ≤ 3 e^(-u)`. 

### `norm_mul_mollifier_sub_le`

 For a Dirichlet character `χ`, `T > 0` and `re z = 2` we have
`|Γ_j(z) L(z, χ) 𝓜(z) - Γ_j(z)²| ≤ 9 / T`. Here `Γ_j(s) = ∫_0^∞ w(x) x ^ s dx / x` is
`gaussianMellin`, the Mellin transform of the weight `w` of index `j`.
`𝓜(s) = ∫_{1/T}^∞ θ(u) u ^ (s - 1/2) du / u` is `mollifier`, with
`θ(u) = u ^ (1/2) ∑_{n ≥ 1} χ(n) μ(n) w(n u)`; it is the truncation at `1/T` of an integral for
`Γ_j / L`. 

### `norm_gaussianMellin_mul_LFunction_le`

 Let `χ ≠ 1` be primitive of parity `j` and conductor `q ≤ T²`. On `re z = 1/2` we have
`|Γ_j L| ≤ 2 J` for `T > 0`, where `Γ_j` is `gaussianMellin` and `J` is `thetaTailIntegral`: the
integral of `|θ_χ(u)| / u` over `u > 0` folds at `q ^ (-1/2) ≥ 1 / T`. 

### `three_lines_bound_of_LFunction_eq_zero`

 For each parity `j` there is a constant `C` with the following property. Let `δ, T > 0`, and let
`χ ≠ 1` be a primitive character of conductor `q ≤ T²` with `χ(-1) = (-1)^j` and
`J(χ, T) ≤ T ^ (2 δ)`, where `J(χ, T) = ∫_{1/T}^∞ (|θ_χ(u)| + |θ_{μχ}(u)|) du / u`
(`thetaTailIntegral`) and `θ_c` is the parity-`j` theta series of `c`. Then every zero `s` of
`L(s, χ)` with `1/2 + 9 δ ≤ re s ≤ 1` satisfies `|Γ_j(s)|² ≤ C T ^ (-2 δ)`, where
`Γ_j(s) = ∫_0^∞ w(z) z ^ s dz / z` (`gaussianMellin`) is the Mellin transform of the parity-`j`
weight `w`. 

### `eventually_rpow_lt_thetaTailIntegral`

 **Three lines.** Let `δ > 0`, let `T` be large in terms of `δ` and the height `H`, and let
`χ ≠ 1` be primitive of conductor `q ≤ T²`, with `χ(-1) = (-1) ^ j`. If `L(s, χ)` has a zero in the
box `re s ≥ 1/2 + 9 δ`, `|im s| ≤ H`, then the integral `J(χ, T)` of `(|θ_χ(u)| + |θ_{μχ}(u)|) / u`
over `u > 1 / T` (`thetaTailIntegral`) exceeds `T ^ (2 δ)`. 

### `exists_dirichletCharacter_eq_jacobiSym`

 For `b ≠ 0` the Jacobi symbol `(·/b)` is a Dirichlet character modulo `b`: it is built by
twisting with one Legendre symbol at a time. 

### `dirichletCharacter_jacobiSym_ne_one`

 If the odd number `m` is not a square, a character modulo `m` whose values are the Jacobi
symbols `(·/m)` is not principal. 

### `norm_sum_jacobiSym_le`

 If the odd number `m` is not a square, the symbol `(·/m)` is a non-principal character, so the
Pólya–Vinogradov inequality gives `|∑_{v ≤ X} (-v/m)| ≤ 2 √m (1 + log m)`. 

### `norm_sum_jacobiSym_ordCompl_le`

 If the odd part `n°` of `n ≠ 0` is not a square, then, for `δ > 0`, the sums of `(-v/n°)` over
`v ≤ X` are at most `2 (1 + 2 / δ) n ^ (1/2 + δ/2)` in absolute value. 

### `exists_abs_gaussianMonomial_le_rpow`

 For every `A > 0` the weight `w(x) = x ^ j e^(-π x²)` (`gaussianMonomial`) is `≪_A x ^ (-A)`
for `x > 0`. 

### `exists_mul_abs_gaussianMonomial_mul_le`

 For `A > 0`, `u > 0` and positive integers `n`, `m` we have
`u |w(n u)| |w(m u)| ≪_A u ^ (1 - 2 A) (n m) ^ (-A)`, with `w = gaussianMonomial j` the weight
`x ^ j e^(-π x²)`. 

### `exists_summable_ge_of_isSquare`

 For `σ > 1/2` and a positive integer `k`, the terms `(k n m) ^ (-σ)` of the pairs `(n, m)` of
positive integers with `k n m` a square have a nonnegative summable majorant. 

### `exists_summable_ge_of_isSquare_ordCompl`

 For `σ > 1/2`, the terms `(n m) ^ (-σ)` of the pairs `(n, m)` of positive integers for which
the odd part `ordCompl[2] (n m)` is a square, that is `n m = l²` or `2 l²`, have a nonnegative
summable majorant. 

### `exists_summable_mul_norm_sum_jacobiSym_le`

 Let `w = gaussianMonomial j` be the weight `z ^ j e^(-π z²)` and `n°` the odd part of `n`. For
`δ > 0` there is a summable `M`, depending only on `δ` and `j`, such that for `T > 0` and
`u ≥ 1 / T` we have `u |w(n u)| |w(m u)| |∑_{v ≤ T²} (-v/(n m)°)| ≤ M (n, m) T² u ^ (-2 δ)`. This
bounds the term of the pair `(n, m)` in the expanded mean square. 

### `sum_sq_thetaSeries_jacobiSym_le`

 **Mean value.** Let `n°` be the odd part of `n`, `w(z) = z ^ j e^(-π z²)` and `δ > 0`. For
`T > 0`, `u ≥ 1 / T` and `|αₙ| ≤ 1`, the theta series `θ_v(u) = u ^ (1/2) ∑ₙ αₙ (-v/n°) w(n u)`
(`thetaSeries`) satisfy `∑_{1 ≤ v ≤ T²} |θ_v(u)|² ≪_δ T² u ^ (-2 δ)`. This is a form of an estimate
of Elliott.

It replaces Heath-Brown's quadratic large sieve: here the coefficients are bounded by `1`, the
weight is fixed, and the effective length `1 / u` of the sums is at most `T`, the square root of the
range of `v`. 

### `sum_integral_norm_thetaSeries_div_le`

 For `|αₙ| ≤ 1` let `θ_v(u) = u ^ (1/2) ∑_{n ≥ 1} αₙ (-v/n°) w(n u)` be the `thetaSeries` with
the weight `w` of index `j`. Here `(-v/n°)` is the Jacobi symbol and `n°` is the odd part of `n`.
For `δ > 0` there is a `C` such that for all `T > 0` and all such `α` we have `∑_{0 < v ≤ T²}
∫_{1/T}^∞ |θ_v(u)| du / u ≤ C T ^ (2 + δ)`, the sum being over all `v`, prime or not: by
Cauchy–Schwarz and the mean value estimate, `∑_{v ≤ T²} |θ_v(u)| ≪ T² u ^ (-δ)` for `u ≥ 1 / T`. 

### `sum_thetaTailIntegral_le`

 For `δ, T > 0` and `|αₙ| ≤ 1`, the sum over `v ≤ T²` of `thetaTailIntegral` (the integral over
`u > 1 / T` of `|θ_c(u)| + |θ_{μc}(u)|` against `du / u`) for the coefficients `cₙ = αₙ (-v/n°)` is
`≪_δ T ^ (2 + δ)`, where `n°` is the odd part of `n`. 

### `legendreSym_eq_jacobiSym_ordCompl`

 For a prime `d ≡ 7 mod 8` and `n ≠ 0`, `(2/d) = 1` and reciprocity give `(n/d) = (-d/n°)`, with
`n°` the odd part of `n`. 

### `isPrimitive_quadTwist`

 The twist `quadTwist ψ d` of a primitive character `ψ` mod `M` by the Legendre symbol of an odd
prime `d` that does not divide `M` is primitive. 

### `IsPrimeWithTwistZero`

 The number `d` is a prime, and the `L`-function of the twist `ψ (·/d)` (`quadTwist ψ d`) has a
zero in the box `re s ≥ β`, `|im s| ≤ H`. 

### `IsPrimeWithTwistZero.prime`

 The number `d` is prime. 

### `IsPrimeWithTwistZero.exists_zero`

 The function `L(s, ψ (·/d))` vanishes at a point of the box. 

### `exists_card_zero_quadTwist_le`

 Let `ψ` be primitive modulo `M`, `δ > 0` and `H` real. Then only `O(T ^ (2 - δ))` primes
`d ≡ 7 mod 8` with `M d ≤ T²` and prime to `M` have a twist `ψ (·/d)` whose `L`-function has a zero
in the box `re s ≥ 1/2 + 9 δ`, `|im s| ≤ H` (`IsPrimeWithTwistZero`): each has
`thetaTailIntegral > T ^ (2 δ)`, and the sum of these integrals is `≪ T ^ (2 + δ)`. 

### `IsBadPrime`

 A prime `d` of the class `a` modulo `N` is bad if some `L(s, ξ (·/d))`, with `ξ` modulo `N`, has
a zero in the box `re s ≥ β`, `|im s| ≤ H`. 

### `zero_density_quadTwist`

 **Bad primes are rare.** Let `β = 1/2 + 9 δ` with `δ > 0`, and let `a` be a class modulo `N` all
of whose primes are `≡ 7 mod 8` and prime to `N` (this holds if `8 ∣ N` and `a ≡ 7 mod 8` is prime
to `N`). The number of primes `d ≤ X` of the class that are bad (`IsBadPrime`: some `L(s, ξ (·/d))`
with `ξ` modulo `N` has a zero with `re s ≥ β`, `|im s| ≤ H`) is `O(X ^ (1 - δ / 2))`. 

### `exists_entireL_quadTwist_ne_zero`

 **Choice of the prime.** Let `β > 1/2`, `H` real and `a` an invertible class mod `N` all of
whose primes are `≡ 7 mod 8` and prime to `N`. For some prime `d` of the class no `L(s, ξ (·/d))`,
`ξ` mod `N`, vanishes in `β ≤ re s`, `|im s| ≤ H`. Here `quadTwist ξ d` is `ξ (·/d)`, and
`entireL` is `L`, as the twists are not principal.

The bound on bad primes is played against the divergence of `∑ log p / p` over the class
(Dirichlet), so the prime number theorem for progressions is not needed. 
