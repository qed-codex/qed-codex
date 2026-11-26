---
{
  "module": "src/Lib/Analytic/DirichletTheta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta series of Dirichlet characters, Poisson summation, and `L(s, χ)` as a Mellin transform

For a parity `j ∈ {0, 1}`, the weight `w(z) = z ^ j e^(-π z²)` and coefficients `c(n)`, this file
studies the theta series `θ(u) = u ^ (1/2) ∑_{n ≥ 1} c(n) w(n u)`. It bounds `θ` and expresses its
Mellin transform through the Dirichlet series of `c`. For a Dirichlet character `χ ≠ 1` of parity
`j`, Poisson summation bounds the series near `0` and so gives the formula for `L(s, χ)` in
`re s > 0` (`hasMellin_thetaSeries_char`); if `χ` is also primitive, it gives the transformation
formula of `|θ|` (`norm_thetaSeries_inv`).

## Relation to the literature

Known result: the transformation formula and the Mellin transform of the theta series of a Dirichlet
character. Sources: Davenport, Multiplicative Number Theory; Montgomery–Vaughan, Multiplicative
Number Theory I, ch. 10. Form here: the transformation is proved in absolute value only, so no root
number appears.


### `gaussianMonomial`

 The weight `w(z) = z ^ j e^(-π z²)` of parity `j ∈ {0, 1}`. 

### `gaussianTheta`

 The series `∑_{n ≥ 1} c(n) w(n u)`. 

### `thetaSeries`

 The theta series `θ(u) = u ^ (1/2) ∑_{n ≥ 1} c(n) w(n u)`. 

### `gaussianMellin`

 The Mellin transform `Γ_j(s) = ∫_0^∞ w(z) z ^ s dz / z` of the weight `w`. 

### `mellinConvergent_and_differentiableAt`

 If a measurable function `f` satisfies `‖f(t)‖ ≤ D e^(-t)` for `t > 0`, then at every `s` with
`re s > 0` the Mellin integral of `f` converges absolutely and `mellin f` is differentiable at
`s`. 

### `mellin_differentiableOn_and_bounded`

 If a measurable function `f` satisfies `‖f(t)‖ ≤ D e^(-t)` for `t > 0`, then its Mellin
transform is holomorphic in `re s > 0` and bounded on `1/2 ≤ re s ≤ 2`. 

### `norm_gaussianMonomial_le`

 For `t ≥ 0` the weight `w(t) = t ^ j e^(-π t²)` satisfies `|w(t)| ≤ 3 e^(-2t)`. 

### `summable_and_norm_gaussianTheta_le`

 If `|c(n)| ≤ 1` and `t > 0`, the series `∑_{n ≥ 1} c(n) w(n t)`, with
`w(z) = z ^ j e^(-π z²)`, converges and is at most `3 e^(-t) / t` in absolute value. 

### `norm_thetaSeries`

 The absolute value of `θ(u) = u ^ (1/2) ∑_{n ≥ 1} c(n) w(n u)` is `u ^ (1/2)` times that of
the sum. 

### `norm_thetaSeries_le`

 The trivial bound: if `|c(n)| ≤ 1` and `t > 0`, then the theta series
`θ(t) = t ^ (1/2) ∑_{n ≥ 1} c(n) w(n t)` is at most `3 t ^ (-1/2) e^(-t)` in absolute value. 

### `integrableOn_norm_thetaSeries_div`

 For `|c(n)| ≤ 1` and `r > 0` the integral `∫_r^∞ |θ(u)| du / u` converges, by the trivial bound
on `θ`. 

### `cpow_smul_thetaSeries`

 For `t > 0` we have `t ^ (s - 1/2 - 1) θ(t) = t ^ (s - 1) ∑_{n ≥ 1} c(n) w(n t)`: the
integrands of the Mellin transforms of `θ` at `s - 1/2` and of the series at `s` agree. 

### `mellin_thetaSeries_sub_half`

 The Mellin transform of `θ(u) = u ^ (1/2) ∑_{n ≥ 1} c(n) w(n u)` at `s - 1/2` is that of the sum
at `s`. 

### `mellin_pow_mul_comp_sq`

 By the substitution `u = t²`, the Mellin transform of `t ^ k F(t²)` at `s` is half that of
`F` at `(s + k) / 2`. 

### `gaussianMellin_eq`

 For `re s > 0` the Mellin transform `Γ_j` of `w(z) = z ^ j e^(-π z²)` is
`Γ_j(s) = π ^ (-(s + j) / 2) Γ((s + j) / 2) / 2`. 

### `mellin_gaussianTheta`

 Integration term by term: if `|c(n)| ≤ 1` and `re s > 1`, the Mellin transform of
`∑_{n ≥ 1} c(n) w(n u)` at `s` is `Γ_j(s) L(s, c)`, where `Γ_j` is the Mellin transform of the
weight `w(z) = z ^ j e^(-π z²)`. 

### `mellin_thetaSeries`

 Riemann's formula `∫_0^∞ θ(u) u ^ (s - 1/2) du / u = Γ_j(s) L(s, c)` for `re s > 1` and
`|c(n)| ≤ 1`, where `θ` is the theta series of `c` and `Γ_j` the Mellin transform of its weight
`w(z) = z ^ j e^(-π z²)`. 

### `norm_mul_moebius_le_one`

 If `|c(n)| ≤ 1` for all `n`, then also `|c(n) μ(n)| ≤ 1`, where `μ` is the Möbius function. 

### `mellin_thetaSeries_moebius`

 Riemann's formula for `1 / L`: if `re s > 1`, then the theta series `θ` with coefficients
`χ(n) μ(n)` satisfies `∫_0^∞ θ(u) u ^ (s - 1/2) du / u = Γ_j(s) / L(s, χ)`, where `Γ_j` is the
Mellin transform of the weight `w(z) = z ^ j e^(-π z²)`. 

### `two_mul_gaussianTheta`

 If `Φ : ZMod q → ℂ` has parity `j` and vanishes at `0`, then the sum of `Φ(n) w(n t)` over `ℤ`,
where `w(z) = z ^ j e^(-π z²)`, is twice the sum over `n ≥ 1` that defines `gaussianTheta`. 

### `poisson_summation_gaussianMonomial`

 Poisson summation for `w(z) = z ^ j e^(-π z²)`: for `t > 0` and real `a`,
`∑_{n ∈ ℤ} e^(2πi a n) w(n / t) = i ^ j t ∑_{n ∈ ℤ} w((n + a) t)`, both series being convergent. 

### `gaussianMellin_differentiableOn_and_bdd`

 The Mellin transform `Γ_j` of the weight `w(z) = z ^ j e^(-π z²)` is holomorphic in
`re s > 0` and bounded on `1/2 ≤ re s ≤ 2`. 

### `exists_pos_le_norm_gaussianMellin`

 On a compact subset `K` of the half plane `re s > 0` the Mellin transform `Γ_j` of
`w(z) = z ^ j e^(-π z²)` is bounded away from zero in absolute value. 

### `hasSum_mul_gaussianMonomial_of_classes`

 A sum over `ℤ` may be taken class by class modulo `q`: if `∑_m w((m + a / q) q t) = S a` for
every class `a`, where `w` is `gaussianMonomial j`, then `∑_n Φ(n) w(n t) = ∑_a Φ(a) S a`. 

### `hasSum_invDFT_mul_gaussianMonomial`

 If `∑_n e^(2πi a n / q) w(n / (q t)) = i ^ j q t S a` for every class `a` modulo `q`, where `w`
is `gaussianMonomial j`, then `∑_n 𝓕⁻ Φ(n) w(n / (q t)) = i ^ j t ∑_a Φ(a) S a`, as
`𝓕⁻ Φ(n) = q⁻¹ ∑_a Φ(a) e^(2πi a n / q)`. Here `n` runs over `ℤ` and `a` over `ZMod q`. 

### `gaussianTheta_poisson_summation`

 For a Dirichlet character `χ ≠ 1` modulo `q` of parity `j ∈ {0, 1}`, primitive or not, Poisson
summation in the classes modulo `q` gives `t |∑ χ(n) w(n t)| = |∑ 𝓕⁻ χ(n) w(n / (q t))|` for
`t > 0`, where `w(z) = z ^ j e^(-π z²)`, the sums are over `n ≥ 1` (`gaussianTheta`) and
`𝓕⁻ χ(n) = q⁻¹ ∑_a χ(a) e^(2πi a n / q)`. 

### `norm_thetaSeries_inv`

 **Symmetry.** For primitive `χ ≠ 1` of conductor `q` with `χ(-1) = (-1) ^ j` and `t > 0` we have
`|θ_χ(t)| = |θ_χ(1 / (q t))|`, where `θ_χ(u) = u ^ (1/2) ∑_{n ≥ 1} χ(n) (n u) ^ j e^(-π n² u²)` is
`thetaSeries`. This is the functional equation of the theta series of a primitive character, in
absolute value. 

### `norm_gaussianTheta_char_le`

 For `χ ≠ 1` of parity `j ∈ {0, 1}` modulo `q` and `t > 0` the sum `∑_{n ≥ 1} χ(n) w(n t)`, with
`w(z) = z ^ j e^(-π z²)`, has absolute value at most `3 e q e^(-t)`: trivially for `t ≥ 1`, by
Poisson summation for `t ≤ 1`. The character need not be primitive. 

### `mellin_gaussianTheta_char`

 For `χ ≠ 1` of parity `j` and `re s > 0`, the Mellin transform of `∑_{n ≥ 1} χ(n) w(n u)` at `s`
is `Γ_j(s) L(s, χ)`, where `Γ_j` is the Mellin transform of `w(z) = z ^ j e^(-π z²)`. This extends
`mellin_gaussianTheta` by analytic continuation. 

### `hasMellin_thetaSeries_char`

 **Riemann's formula.** For `χ ≠ 1` with `χ(-1) = (-1) ^ j` and `re s > 0` the
identity `∫_0^∞ θ_χ(u) u ^ (s - 1/2) du / u = Γ_j(s) L(s, χ)` holds with absolute convergence
(`HasMellin`), where `θ_χ` is `thetaSeries` and `Γ_j` the Mellin transform of
`z ^ j e^(-π z²)`. 

### `image_inv_const_mul_Ioo`

 For `b, r > 0` with `1 / (b r) = r`, the map `u ↦ 1 / (b u)` takes the interval `(0, r)` onto
`(r, ∞)`. 

### `integral_norm_thetaSeries_div`

 The fold: for primitive `χ ≠ 1` of conductor `q` with `χ(-1) = (-1) ^ j`,
`∫_0^∞ |θ_χ(u)| du / u = 2 ∫_{q ^ (-1/2)}^∞ |θ_χ(u)| du / u`, where
`θ_χ(u) = u ^ (1/2) ∑_{n ≥ 1} χ(n) (n u) ^ j e^(-π n² u²)` is `thetaSeries`. 
