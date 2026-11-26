---
{
  "module": "src/New/UpperBound/Kernels/DefiniteKernelSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/DefiniteKernelSize.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/DefiniteKernelSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rational equivariance, integrality and size of definite theta kernels

This file studies the theta kernels `New.modKernelStdSpace` of a pair of standard definite spaces
`I_L`, `I_N`, whose real datum is determined by a polynomial `Q`. The kernels are evaluated at
finite points. Moving these points by rational elements acts through the two-sided substitutions
`New.Rows.twoSidedSubst`. Here `p` is a number whose prime divisors in `E` are the places at which
integrality is asked. The file builds the normalising constant `New.Rows.modKernelScale` and bounds
the conjugates of a polynomial `Q` homogeneous of degree `d` on polydiscs.

## Main definitions and results

* `New.Rows.modKernelStdSpace_embFin_mul`: moving the points by rational elements substitutes the
  variables of `Q` (`New.Rows.twoSidedSubst`) and multiplies by determinants.
* `New.Rows.IsModKernelScale`, `New.Rows.exists_ne_zero_isModKernelScale`: after one
  normalising constant, kernels with `p`-integral input are `p`-integral and, under bounds on the
  sizes of the input, their conjugates are bounded.

Notions from other files:
* `New.stdSpace`: the definite space `I_n`, the sum of `n` norms with its standard lattice.
* `New.Gf`, `New.integralAbove`: the finite adelic unitary group, and its subgroup of points whose
  components at all primes above `p` are integral invertible matrices.
* `New.modKernelStdSpace`: the theta kernel of the datum made of a function `Ψ` on matrices modulo
  `𝔪` and the Fock vector of a polynomial `Q`, for the Weil action twisted by two characters of
  `U(1)`.
* `New.Space.jetSeries`, `New.jet`: the Taylor series of a theta function in Fock's coordinates, and
  the pairing `P(∂) F (0)` of a polynomial `P` with a power series `F`.
* `New.Rows.twoSidedSubst`: the substitution `x_τ ↦ c_τᵀ x_τ g_τᵀ` on complex polynomials in the
  entries of `N × L` matrices `x_τ`.


### `modKernelStdSpace_embFin_mul`

 Let `a`, `b` be automorphic characters of `U(1)` (`AutChar`) with exponents `e`, `e'` at the
infinite places and residue characters `ψ`, `ψ'`. Translating the finite adelic points `g`, `h` by
the finite parts (`embFin`) of rational points `γ`, `γ'` substitutes
`x_τ ↦ (Φ τ γ'⁻¹)ᵀ x_τ (Φ τ γ)ᵀ` in `Q` (`twoSidedSubst`) and multiplies the kernel by
`∏ τ, Φ τ (det γ') ^ (-e τ) * Φ τ (det γ) ^ e' τ`. Here `(1, g)` has trivial real part, and `Φ τ` is
the complex embedding of `E` that the CM type chooses at the place `τ`. 

### `blockSumOne_mem_integralAbove`

 If the finite adelic points `g`, `g'` have integral invertible components at all primes above
`p`, so does their block sum `diag(g, g')`. 

### `stdEmbFin_blockSumOne`

 The embedding of rational points into finite adelic points commutes with block sums. 

### `blockSumOne_mul_mem_integralAbove`

 Let `γ`, `γ'` be rational unitary points, embedded in the finite adelic groups by `stdEmbFin`,
and let `g`, `g'` be finite adelic points. If `γ g` and `γ' g'` have integral invertible components
at all primes above `p`, so does the product of the block sums `diag(γ, γ')` and `diag(g, g')`. 

### `modKernelScale`

 The constant that normalises the theta kernels of the standard definite spaces `I_L`, `I_N`
over the field `D.E = P.E s` of the data `D`, where `s = D.towerExp` is its exponent in the tower
over `K = ℚ(√-P.d)`, for polynomials homogeneous of degree `d`. It is built from the principal
level `D.M` (a product of two primes), the number `P.vacuumScale s` that makes the values of the
vacuum of rank one (`Space.vacElem`) integral, and the scale `P.jetScale s` of the Taylor series. 

### `jet_jetSeries_pairWeil_vacuumDatum`

 Let `Q` be homogeneous of degree `d`. Take `s` times the datum (`vacuumDatum`) that is `Ψ` at
the places dividing `𝔪` and elsewhere the vacuum, and translate it (`pairWeil`) by the adelic points
`(1, g)`, `(1, h)` with trivial real parts and finite parts `g`, `h`. The pairing `Q(∂) F (0)`
(`jet`) of `Q` with the Taylor series `F` of its theta function at scale `t` is `s * t ^ d` times
the theta kernel `modKernelStdSpace`. 

### `norm_modKernelScale_mul_modKernelStdSpace_le_one`

 Let the automorphic characters `a`, `b` of `U(1)` have exponents `ea`, `eb` at the infinite
places and residue characters `ψ`, `ψ'`, let `𝔪` contain `q * D.M ^ 2`, let the values of `Ψ` be
integral at all primes coprime to `q`, and let `Q` be homogeneous of degree `d`. Let `p` be a prime
coprime to `q`; the instance `PadicPlace p` chooses an embedding `ιₚ : ℂ → ℂ_p`, with valuation ring
`embValRing ⊆ ℂ`. If the finite adelic points `g`, `h` are integral above `p` and `Q` has
coefficients in `embValRing`, then the kernel times `modKernelScale L N D d` has `p`-adic norm at
most `1`. 

### `norm_map_eval_le_of_isHomogeneous`

 Growth of a homogeneous polynomial `Q` of degree `d` under an automorphism `σ` of `ℂ`: a bound
`B` for `‖σ (Q z)‖` on the polydisc `‖σ (z i)‖ ≤ ρ` gives the bound `B * t ^ d` on the polydisc
`‖σ (z i)‖ ≤ t * ρ`. 

### `norm_map_sq_div_bigOmega_mul_le`

 Let `M = D.M` be the principal level of the data `D` and `d ≤ M`. For every automorphism `σ` of
`ℂ`, the number `‖σ (M ^ 2 * P.d)‖ ^ 2 / Ω` times `2 * d + 2` is at most `(M ^ 4) ^ 2`. Here `P.d`
is the prime with `K = ℚ(√-P.d)`, and `Ω = P.bigOmega D.towerExp` is
`exp (γ - Re L'/L(1, χ_K)) * 2π` divided by the root discriminant of the field `D.E` (`γ` is Euler's
constant). 

### `hasConjugateGrowth_of_isHomogeneous`

 The parameters `P` fix a prime `P.d` and `K = ℚ(√-P.d)`; the data `D` fix a field `D.E`, the
step `D.towerExp` of a cyclotomic tower over `K`, and a level `M = D.M`, a product of two primes.
Let `σ` be an automorphism of `ℂ`, and `Q` homogeneous of degree `d ≤ M` with `‖σ (Q z)‖ ≤ B`
whenever all `‖σ (z i)‖ ≤ M ^ 4`. Put `T = ‖σ (M ^ 2 * P.d)‖ ^ 2 / Ω`, where
`Ω = P.bigOmega D.towerExp` is `exp (γ - Re L'/L(1, χ_K)) * 2π` divided by the root discriminant
of `D.E` (`γ` is Euler's constant). Then `HasConjugateGrowth σ Q T d 0 B` holds: for all `z` and
real `R` with `∑ ‖σ (z i)‖ ^ 2 ≤ T * (2 * d + 2) * R`, we have `‖σ (Q z)‖ ≤ B * exp (0 + d * R)`. 

### `M_pow_mul_card_mul_exp_le`

 The constants in the bound for the conjugates of the theta kernel are at most `exp D.x₁`. The
data `D` for the parameters `P` fix a cut-off `D.x₁` (a large integer), a rank `D.r` (a power of
`3`), a level `D.M` and a CM field `D.E = P.E s` with `s = D.towerExp`, generated over
`K = ℚ(√-P.d)` by a root of unity of order `P.q₁ s`; `P.Φ s` is the set of its infinite places, and
`P.constantBound` bounds the constants that depend on `P` only. Let `L`, `N` have at most
`D.gap = 2 * D.r ^ 8` elements, let `d ≤ D.M`, and let the ideal `𝔪` of `𝓞 D.E` contain `D.M ^ 2`.
The three factors are the cleared denominator, the number of matrices over
`𝔪.ResidueRing = 𝓞 D.E / 𝔪`, and the exponential in `Parameters.jetSizeBound`. 

### `norm_modKernelScale_mul_modKernelStdSpace_le`

 Let `L`, `N` have at most `D.gap = 2 * D.r ^ 8` elements and let `d ≤ D.M`. Let the automorphic
characters `a`, `b` of `U(1)` have exponents `ea`, `eb` at the infinite places and residue
characters `ψ`, `ψ'` (`HasWeight`), and let `𝔪` contain `D.M ^ 2`. Let all conjugates of the values
of `Ψ` have norm at most the integer `A`, and let `Q` be homogeneous of degree `d` with
`‖σ (Q z)‖ ≤ B` whenever all `‖σ (z i)‖ ≤ D.M ^ 4`. Then the `σ`-conjugate of
`modKernelScale L N D d` times the kernel has norm at most `exp D.x₁ * A * B`. 

### `IsModKernelScale`

 The constant `c` is a scale for the theta kernels `modKernelStdSpace` of the standard definite
spaces `I_L`, `I_N` over the field `D.E` of the data `D`, for polynomials `Q` homogeneous of degree
`d` and characters `a`, `b` with exponents `ea`, `eb` at the infinite places and tame parts `ψ`,
`ψ'` (`HasWeight`): `c` times the kernel is integral at `p` when the input is, and its conjugates
are bounded when `L`, `N`, `d` and the input are. Here the principal level `D.M` is a product of
two primes, `D.gap = 2 * D.r ^ 8` with `D.r` the rank of the target (a power of `3`), and `D.x₁`
is the second cut-off of `D`, a large integer. 

### `IsModKernelScale.norm_le_one`

 Let `𝔪` contain `q * D.M ^ 2` and let the values of `Ψ` be integral at the primes coprime
  to `q`. If `p` is such a prime and `g`, `h` and the coefficients of `Q` are integral at `p`, then
  `c` times the kernel has `p`-adic norm at most `1`. 

### `IsModKernelScale.norm_map_le`

 Let `L`, `N` have at most `D.gap` elements, let `d ≤ D.M` and let `𝔪` contain
  `D.M ^ 2`. If `A` bounds all conjugates of the values of `Ψ`, and `B` bounds `σ ∘ Q` on the
  polydisc `‖σ (z i)‖ ≤ D.M ^ 4`, then the `σ`-conjugate of `c` times the kernel has norm at
  most `exp D.x₁ * A * B`. 

### `exists_ne_zero_isModKernelScale`

 Integrality and size of the theta kernels `modKernelStdSpace` of the standard definite spaces
`I_L`, `I_N` over the field `D.E` of the data `D`, built from a function `Ψ` on matrices modulo `𝔪`
and a polynomial `Q` homogeneous of degree `d`. There is a constant `c ≠ 0`, depending only on `L`,
`N`, `D` and `d`, with the two properties of `IsModKernelScale`. If `𝔪` contains `q * D.M ^ 2`, the
values of `Ψ` are integral away from `q`, and the points `g`, `h` and the coefficients of `Q` are
integral at a prime `p` coprime to `q`, then `c` times the kernel is integral at `p`. If `L`, `N`
have at most `D.gap` elements, `d ≤ D.M`, `𝔪` contains `D.M ^ 2`, `A` bounds the conjugates of the
values of `Ψ` and `B` bounds `σ ∘ Q` on the polydisc `‖σ (z i)‖ ≤ D.M ^ 4`, then the `σ`-conjugate
of `c` times the kernel has norm at most `exp D.x₁ * A * B`. 
