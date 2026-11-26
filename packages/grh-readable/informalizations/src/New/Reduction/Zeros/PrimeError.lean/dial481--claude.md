---
{
  "module": "src/New/Reduction/Zeros/PrimeError.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A weighted prime-counting error term and its poles at zeros of L-functions

Let `d` be a prime and `χ_K = (·/d)` the Legendre symbol. We study the remainder `R_q` of a weighted
sum over the prime powers `n ≡ 1` modulo `q` with `χ_K(n) ≠ 1`. Its Laplace transform sees the zeros
of the Dirichlet `L`-functions modulo `q` and of their twists by `χ_K`.

* `New.lambdaKResidueClass`: the weight `λ(n) = Λ(n) (1 - χ_K(n))` on `n ≡ 1` modulo `q`; it is
  nonnegative.
* `New.logDerivMean`: the mean `G_q` over the characters `ψ` modulo `q` of the differences of the
  logarithmic derivatives of `New.entireL (New.quadTwist ψ d)` and `New.entireL ψ`, less `1 / φ(q)`.
* `New.primeRemainder`: `R_q(x) = ∑_{n ≤ x} λ(n) (1/n - 1/x) - log x / φ(q) - re G_q(1)`.
* `New.LSeries_lambdaKResidueClass_eq_add_logDerivMean`: for odd `d` prime to `q`, the Dirichlet
  series of `λ` is `s / (φ(q) (s - 1)) + G_q(s)` in `re s > 1`.
* `New.isPolar_primeRemainder`: for `d ≡ 7` modulo `8` prime to `q`, the transform of
  `v ↦ R_q(e ^ v)` has at most simple poles in `re s > 0`, none at `1`, and at `s ≠ 1` with the
  residue `(n(s) - n'(s)) / (φ(q) s (1 - s))`, where `n(s)` and `n'(s)` are the sums of the orders
  at `s` of these `L`-functions and of their twists.

Here `New.entireL ψ` is `L(s, ψ)`, times `s - 1` if `ψ` is principal, `New.quadTwist ψ d` is the
character `ψ χ_K`, and `New.chowlaSelbergConst d` is, for odd `d`, `γ - re L'/L(1, χ_K)`, with `γ`
Euler's constant.

## Relation to the literature

The transform of a weighted prime sum in a residue class is computed by orthogonality of characters
and partial summation. Source: Davenport, Multiplicative Number Theory.


 ### The weights, their partial sums and the error term 

### `lambdaKResidueClass`

 The weight `λ(n) = Λ(n) (1 - χ_K(n))` for `n ≡ 1` mod `q`, and `0` for other `n`. Here `Λ` is
the von Mangoldt function and `χ_K = chiK d` is the Legendre symbol `(·/d)`. 

### `lambdaKSum`

 The sum `y ^ (-r) ∑_{1 ≤ n ≤ y} λ(n) n ^ (r - 1)` with `λ = lambdaKResidueClass d q`, used for
`r = 0` and `r = 1`. 

### `logDerivMean`

 The function `G_q` with `φ(q) G_q = (L_q^K)' / L_q^K - L_q' / L_q - 1` away from the zeros of
`L_q` and `L_q^K`, which are the products of the `entireL ψ` and of the `entireL (quadTwist ψ d)`
over all characters `ψ` mod `q`. For odd `d` prime to `q` and `re s > 1` it is
`∑ λ(n) n ^ (-s) - s / (φ(q) (s - 1))`. 

### `primeRemainder`

 The remainder `R_q(x) = ∑_{n ≤ x} λ(n) (1/n - 1/x) - log x / φ(q) - c_q`, with
`λ = lambdaKResidueClass d q` and `c_q = re G_q(1)`, `G_q = logDerivMean d q`; see
`primeRemainder_eq_sum_posPart`. For odd `d` prime to `q` this is the constant for which
`R_q(x) → 0` as `x → ∞`, as `tendsto_primeRemainder` in `New.Reduction.Zeros.PrimeNumberTheorem`
proves. 

### `one_sub_chiK_mem_Icc`

 For a prime `d`, the Legendre symbol `chiK d n = (n/d)` takes the values `0`, `1` and `-1`, so
`0 ≤ 1 - (n/d) ≤ 2`. 

### `lambdaKResidueClass_le_two_mul_vonMangoldt`

 For a prime `d` and any `q : ℕ`, the weight `lambdaKResidueClass d q n`, which is
`Λ(n) (1 - (n/d))` for `n ≡ 1` mod `q` and `0` otherwise, is at most `2 Λ(n)`, where
`Λ = vonMangoldt`. 

### `sum_vonMangoldt_div_le`

 A bound of Mertens's type: `∑_{n ≤ N} Λ(n) / n ≤ 2 log N`. 

### `abs_lambdaKSum_exp_le`

 Growth of the partial sums. Let `d` be a prime, `q` any natural number, and
`λ = lambdaKResidueClass d q` the weight `Λ(n) (1 - (n/d))` on `n ≡ 1` mod `q` and `0` elsewhere,
with `(·/d)` the Legendre symbol. For every `r : ℕ` and real `v`, the sum `lambdaKSum d q r y = y ^
(-r) ∑_{1 ≤ n ≤ y} λ(n) n ^ (r - 1)` at `y = e ^ v` has absolute value at most `2 e ^ v`. 

### `re_logDerivMean_one_eq_add_re_logDeriv`

 Let `d` be a prime and `χ_K = quadTwist 1 d` the Legendre symbol `(·/d)` as a complex character
mod `1 * d`. Let `E = entireL χ_K`, which is `L(s, χ_K)` if `d` is odd and `(s - 1) L(s, χ_K)` if
`d = 2`. For the modulus `q = 1`, `G₁ = logDerivMean d 1` is `E'/E - Z'/Z - 1` with
`Z(s) = (s - 1) ζ(s)`, and `re G₁(1) = -1 - γ + re E'/E(1)`. 

### `re_logDerivMean_one`

 For a prime `d` and the modulus `q = 1`, the value at `s = 1` of `G₁ = logDerivMean d 1` has
real part `-1 - chowlaSelbergConst d`. 

### `analyticAt_logDerivMean_of_one_le_re`

 The function `G_q = logDerivMean d q` is analytic in `re s ≥ 1`, where no `entireL χ`
vanishes. 

### `abs_primeRemainder_exp_le`

 Growth of the remainder: for a prime `d`, `q ≥ 1` and `v ≥ 0`,
`|R_q(e ^ v)| ≤ (|re G_q(1)| + 5) e ^ v`. 

### `primeRemainder_eq_sum_posPart`

 In the remainder `primeRemainder d q z = ∑_{1 ≤ n ≤ z} λ(n) (1/n - 1/z) - log z / φ(q) - re
G_q(1)` with `z > 0`, the sum equals `∑_{1 ≤ n ≤ A} λ(n) (1/n - 1/z)⁺` for any integer `A ≥ ⌊z⌋`. 

### `primeRemainder_eq_sum`

 In the remainder `primeRemainder d q z = ∑_{1 ≤ n ≤ z} λ(n) (1/n - 1/z) - log z / φ(q) - re
G_q(1)` with `z > 0`, the sum equals `A⁻¹ ∑_{1 ≤ n ≤ A} λ(n) (A/n - A/z)⁺` for any integer
`A ≥ z`. 

 ### The Dirichlet series and the Laplace transform 

### `LSeries_lambdaKResidueClass`

 Partial summation. For every `r : ℕ` and `re s > 2`, the series `∑ λ(n) n ^ (-s)` is `s + r - 1`
times the Laplace transform at `s - 1` of `v ↦ lambdaKSum d q r (e ^ v)`. 

### `LSeries_lambdaKResidueClass_eq_add_logDerivMean`

 Let `d` be an odd prime coprime to `q ≥ 1`, `χ_K = (·/d)` the Legendre symbol, and
`λ = lambdaKResidueClass d q` the weight `Λ(n) (1 - χ_K(n))` on `n ≡ 1` mod `q` and `0` elsewhere.
For `re s > 1`, `∑ λ(n) n ^ (-s) = s / (φ(q) (s - 1)) + G_q(s)`. 

### `integral_primeRemainder`

 For an odd prime `d` coprime to `q ≥ 1` and `re s > 2`, the Laplace transform of
`v ↦ R_q(e ^ v)` at `s - 1` is `(G_q(s) / s - re G_q(1)) / (s - 1)`. 

### `ofReal_re_logDerivMean_one`

 For an odd prime `d` coprime to `q ≥ 1`, the number `G_q(1)` is real, so it equals the constant
`re G_q(1)` subtracted in `primeRemainder d q`. Here `G_q = logDerivMean d q` is
`(∑_ψ (E_{ψ χ_K}' / E_{ψ χ_K} - E_ψ' / E_ψ) - 1) / φ(q)`, summed over the characters `ψ` mod `q`,
where `χ_K = (·/d)` is the Legendre symbol and `E_χ = entireL χ` is `L(s, χ)`, times `s - 1` if `χ`
is principal. 

 ### The poles of the Laplace transform 

### `tendsto_sub_mul_logDerivMean`

 Let `d` be a prime, `q ≥ 1`, `χ_K = (·/d)` the Legendre symbol, `quadTwist ψ d = ψ χ_K`, and let
`E_χ = entireL χ` be `L(s, χ)`, times `s - 1` if `χ` is principal. The function
`G_q = logDerivMean d q`, that is `(∑_ψ (E_{ψ χ_K}' / E_{ψ χ_K} - E_ψ' / E_ψ) - 1) / φ(q)` summed
over the characters `ψ` mod `q`, has at most a simple pole at `ρ`. Its residue is the mean over `ψ`
of `ord_ρ E_{ψ χ_K} - ord_ρ E_ψ`. 

### `tendsto_logDerivMean_residue`

 Let `d` be a prime, `q ≥ 1`, `χ_K = (·/d)` the Legendre symbol, `quadTwist ψ d = ψ χ_K`, and let
`E_χ = entireL χ` be `L(s, χ)`, times `s - 1` if `χ` is principal. At `ρ ≠ 0, 1` and for any
constant `κ`, the function `(G_q(z) / z - κ) / (z - 1)` has at most a simple pole, of residue `∑_ψ
(ord_ρ E_ψ - ord_ρ E_{ψ χ_K}) / (φ(q) ρ (1 - ρ))`. 

### `isPolar_primeRemainder`

 **Poles.** Let `d ≡ 7 mod 8` be a prime coprime to `q ≥ 1`, `χ_K = (·/d)` the character of
`K = ℚ(√-d)`, and `R_q = primeRemainder d q`. The conclusion `IsPolar` says three things. The
function `v ↦ R_q(e ^ v)` is measurable. There is a constant `C` with `|R_q(e ^ v)| ≤ C e ^ v` for
`v ≥ 0`. The transform `∫₀^∞ R_q(e ^ v) e ^ ((1 - s) v) dv` continues from `re s > 2` to a
meromorphic function on `ℂ` with at most simple poles in `re s > 0` and the following residues
there. It has no pole at `1`, where the formula below is a division by zero, of value `0`. The
residue at `s ≠ 1` is `∑_ψ (ord_s E_ψ - ord_s E_{ψ χ_K}) / (φ(q) s (1 - s))`, summed over the
characters `ψ` mod `q`, where `quadTwist ψ d = ψ χ_K` and `E_χ = entireL χ` is `L(s, χ)`, times
`s - 1` if `χ` is principal. 
