---
{
  "module": "src/Lib/Analytic/Primes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Primes congruent to `1` modulo `M ^ k` with logarithm in a prescribed window

Let `4 ∣ M` and let `A` be fixed. For large `W` there is a prime `p ≡ 1` modulo `M ^ k` with `log p`
in `[U, U + W]`, uniformly for `1 < k`, `M ^ k ≤ W ^ A` and `W ≤ U ≤ W ^ A`
(`New.exists_prime_modEq_one_log_mem`).

The characters modulo `M ^ k` with trivial square come from the fixed modulus `M ^ 2`, so the
zero-free region gives a disc about `1` without zeros, uniformly in `k`. Newman's contour argument
on its boundary yields the prime.

Independently, the first section proves `n ≤ φ n * (2 * log n + 1)` (`New.le_totient_mul_log`).

Notions from other files:
* `entireL χ` is `L(s, χ)`, times `s - 1` if `χ` is principal;
* `regularL χ` is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal.

## Relation to the literature

Known result: primes congruent to `1` modulo `M ^ k` with logarithm in a prescribed window. It is a
consequence of the Siegel–Walfisz theorem. Only one prime is found, in a long window, and only for
moduli that are powers of a fixed multiple of `4`. Source: Montgomery and Vaughan, Multiplicative
Number Theory I, 2007, Cor. 11.19.


 ## A lower bound for Euler's totient 

### `New.div_add_card_le_prod_one_sub_inv`

 If every element of a finite set `S` of natural numbers exceeds `a`, then
`∏ p ∈ S, (1 - p⁻¹) ≥ a / (a + #S)`. 

### `New.le_totient_mul_log`

 Every positive integer satisfies `n ≤ φ n * (2 * log n + 1)`. 


## Primes congruent to 1 mod M^k in a logarithmic window via Newman's method


### `New.factorsThrough_sq_of_sq_eq_one`

 If `4 ∣ M` and `2 ≤ k`, a character mod `M ^ k` whose square is trivial factors through modulus
`M ^ 2`, since every unit congruent to `1` mod `M ^ 2` is a square. 

### `New.exists_regularL_eq_of_sq_eq_one`

 If `4 ∣ M` and `2 ≤ k`, then for a character `χ` mod `M ^ k` with trivial square there is a
character `χ₀` mod `M ^ 2` with `regularL χ = regularL χ₀`, as the two moduli have the same prime
factors. Here `regularL χ` is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal. 

### `New.eventually_norm_logDeriv_entireL_le_near_one`

 For `4 ∣ M` and `A` fixed, for all large `X` the following holds for every `k > 1`, every
Dirichlet character `χ` mod `M ^ k` with `M ^ k ≤ X ^ A`, and every `s` with `|s - 1| ≤ 1 / X`:
`entireL χ s ≠ 0` and `|logDeriv (entireL χ) s| ≤ X`. Here `entireL χ` is the entire function equal
to `L(s, χ)` for non-principal `χ`, and to the continuation of `(s - 1) L(s, χ)` for principal `χ`.
No exceptional zero can occur, because the real characters come from the fixed modulus `M ^ 2`. 

### `New.norm_term_le_exp_mul`

 If `log n * (σ - re z) ≤ E`, then moving the `n`-th term of the Dirichlet series of `a` from
`1 + z` to the real point `1 + σ` costs at most the factor `exp E`. 

### `New.summable_vonMangoldt_not_prime`

 The Dirichlet series of the function that is `Λ n` at the numbers `n` that are not prime and
`0` at the primes converges absolutely at `3 / 4 = 1 + -4⁻¹`, because Chebyshev's functions satisfy
`ψ - θ = O(√x)`. 

### `New.hasSum_residueClass_one`

 For `0 < re z` the Dirichlet series of `Λ` on the class `1` mod `q` has at `1 + z` the sum
`(1 - z * ∑ χ, L_χ'/L_χ (1 + z)) / φ(q) / z`. Here `L_χ = entireL χ` is `L(s, χ)` with the pole
removed. 

### `New.norm_one_sub_mul_sum_div_totient_le`

 There are `φ(q) ≥ 1` characters mod `q`, so `‖1 - ∑ χ, z * c χ‖ ≤ 2 φ(q)` if each term of the
sum has norm at most `1`. 

### `New.exists_shift_le_re_exponent`

 On the circle `‖z‖ = 1 / X` the real part of `2 - U z - X (1 + X z)² / 4`, the exponent in
Newman's method, is at least (in fact equal to) that of `2 - (U + t) z` for some `t ∈ [0, X ^ 2]`,
namely `t = X ^ 2 / 2 * (1 + X * re z)`: the quadratic term acts as a shift of `U` by `t`. 

### `New.norm_le_of_term_le_majorant`

 Let `a ≥ 0` have the Dirichlet series `F z / z` at `1 + z` for `0 < re z`, with `‖F‖ ≤ 2` on
`‖z‖ ≤ 1 / X`, and let the series of `b` at `3 / 4` have absolute sum `C ≤ X`, where `200 ≤ X` and
`X² ≤ U`. If on a set of `n` the terms of the series of `a` at `1 + z` are at most `e ^ E` times
the sum of those of `a` at `1 + 1 / U` and those of `b` at `3 / 4`, then this part of the series is
at most `3 U e ^ E`. 

### `New.norm_sub_mul_sum_term_le`

 The bound on the circle in Newman's method. Let `a ≥ 0` have the Dirichlet series `F z / z` at
`1 + z` for `0 < re z` (here `term a s n` is the summand `a n / n ^ s`), with `‖F‖ ≤ 2` on
`‖z‖ ≤ 1 / X`. Let the series of `b` at `3 / 4` have absolute sum `C ≤ X`, let `200 ≤ X` and
`X² ≤ U`, and let `|a n| ≤ |b n|` whenever `log n` lies in `[U, U + X²]`. Then on `‖z‖ = 1 / X` we
have `‖F z - z P z‖ ≤ 3 U e ^ E`, where `P z` is the part with `n < e ^ U` of the series of `a`
and `E` is the real part of `2 - U z - X (1 + X z)² / 4`. 

### `New.analyticOnNhd_sub_mul_sum_term`

 The function `F z - z P z` of Newman's method is analytic on a disc on which no
`entireL χ (1 + z)` vanishes: here `F z = (1 - z * ∑ χ, L_χ'/L_χ (1 + z)) / φ(q)`, with
`L_χ = entireL χ`, and `P z` is the part with `n < N` of the Dirichlet series at `1 + z` of `Λ` on
the class `1` mod `q` (`residueClass`). 

### `New.exists_prime_modEq_one_log_mem`

 Let `4 ∣ M` and let `A` be fixed. For all large `W` there is a prime `p ≡ 1` mod `M ^ k` with
`U ≤ log p ≤ U + W`, whenever `1 < k`, `M ^ k ≤ W ^ A` and `W ≤ U ≤ W ^ A`. This is a consequence
of the Siegel–Walfisz theorem, proved here directly by Newman's contour method. 
