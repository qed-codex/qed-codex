---
{
  "module": "src/Lib/SiegelWeil/Tower/FunctionalEquation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/FunctionalEquation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Tower/FunctionalEquation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The functional equation of the `L`-function of a tamely ramified character

Tate's argument for the base change of a character of `[U(1)]` of positive weight `μ` that is tamely
ramified at split places. The zeta integral `𝒵` of `exists_zetaIntegral`, whose values `𝒵(x)` and
`𝒵(1 - x)` are for `x ≥ 1` the same expression in `x` up to a constant factor, is evaluated at the
test function `∏ conj (a w) ^ (2 μ w) exp (-|a w|²)` (see `Lib.SiegelWeil.Tower.TestVector`). It
continues `L` to real `x > -min μ` and compares the absolute values at `z` and `1 - z` for
`1 ≤ z < min μ + 1`. As `L` has no zero at real `x ≥ 1`, the extension has no zero at the integers
`j > -min μ` (`exists_analytic_extension_ne_zero`). The file also computes the theta kernels of
pairs in which one space is `0`.

Notions from other files:
* `Space E n s`: a hermitian space over the field `E` with basis indexed by `n` and signs `s`;
  `stdSpace E Empty` is the space `0`, `W.θ` the theta functional and `W.vacElem` the vacuum.
* `pairTheta W V α β f`: the theta kernel of `(W, V)` twisted by the characters `α` and `β`;
  `localDatum W V v Φ 𝔠.readsAt` is the datum with archimedean part `v`, the function `Φ` at the
  ramified places of `𝔠` and the vacuum elsewhere; `thetaLarge W V 𝔠 v Φ` integrates the kernel at
  this datum over `[U(V)]`.
* `SplitTameChar E μ`: a character `ν` of `[U(1)]` of positive weight `μ`, tamely ramified exactly
  at a non-empty set `S` of split places; `ν.L S` is its `L`-function without `S ∪ S̄`.

## Relation to the literature

Known result: analytic continuation and functional equation of Hecke `L`-functions. Only real
arguments `x > -min μ` and absolute values are treated. Source: J. Tate, Fourier analysis in number
fields and Hecke's zeta-functions (thesis, 1950), §2.5 and Main Theorem 4.4.1.


### `exists_exp_neg_sq_mul_rpow_mul_one_add_log_sq_le`

 For `c > 0`, the function `exp (-y²) y ^ (2 c) (1 + log² y)` is bounded above on `y > 0`. 

### `integrable_prod_exp_neg_sq_mul_rpow`

 For exponents `c x > 0`, the function `a ↦ ∏ x, exp (-|a x|²) |a x| ^ (2 c x)` is integrable for
the Haar measure of the group `(ι → ℂ)ˣ`: the integrals that define the `Γ`-factors converge. 

### `gammaWeight`

 The test function times the archimedean component of a character of weight `m`: the integrand
of the archimedean zeta integral without the factor `|a| ^ x`, where `|a| = ∏ w, |a w|²`. 

### `gammaIntegral`

 The archimedean zeta integral `∫ gammaWeight E m a * |a| ^ x` of the test function at real `x`,
where `ideleAbs (realIdele a) = |a| = ∏ w, |a w|²`. Classically (not proved here), for `x > -min m`,
it is a constant times `∏ Γ(x + m w)`; only its positivity and analyticity are proved and used. 

### `integrable_gammaWeight_mul_rpow`

 The integrand `gammaWeight E m a * |a| ^ x` of the archimedean zeta integral is integrable for
`x > -k`, where `k ≤ m w` for every infinite place `w` and `|a| = ∏ w, |a w|²`. 

### `gammaIntegral_pos`

 The archimedean zeta integral `gammaIntegral E m x` is positive for `x > -k`, where `k ≤ m w`
for every infinite place `w`. 

### `analyticOnNhd_gammaIntegral`

 The archimedean zeta integral `gammaIntegral E m x` is analytic in the real variable `x > -k`,
where `k ≤ m w` for every infinite place `w`. 

### `stdColDatum_one_one`

 For the tame part `χ` of a split tame character `𝔠`, the standard datum
`stdColDatum 𝔠.semilocalChar 1`, which sends an integral matrix `y` with unit determinant to
`χ⁻¹ (det y)` and all other matrices to zero, has the value `1` at the identity matrix. 

### `schrodingerOp_vacElem_of_isEmpty`

 For a space `W` of rank zero, the operator `W.schrodingerOp 𝔠.ramifiedPlaces Φ` (a combination
of Heisenberg operators at the ramified places `𝔠.ramifiedPlaces` that represents the function `Φ`
of finite adelic vectors) sends the vacuum `W.vacElem` to `Φ 0` times the vacuum. 

### `thetaLarge_smul`

 The theta integral `thetaLarge W V 𝔠 v Φ g` is homogeneous in the archimedean part `v` of the
datum. 

### `integral_coneIntegrand_tateVector`

 Let `A` be an adapted splitting (orthonormal at the infinite places, integral at the finite
ones) of `W'` into a hyperbolic plane and a space `W` of rank zero, and let the signs `s'` of `W'`
take each of the values `1` and `-1` once. On either side `β` of Poisson's formula, the integral
over the maximal compact subgroup and the archimedean ideles of the cone integrand with exponent
`x`, at the test vector `tateVector s' m` (the product of the `m w`-th powers of the diagonal Fock
variables), is the vacuum `vacVector` of the archimedean Fock space times `gammaIntegral E m x`
times the volume of the compact subgroup. 

### `theta_vacElem_of_isEmpty`

 For a hermitian space `W` of rank zero (`n` empty) over a CM field `E` with Weil data, the theta
functional `W.θ` takes the value `1` on the vacuum `W.vacElem` (the Gaussian times twisted lattice
indicator, as an element of 𝒮(W)). 

### `pairTheta_target_zero`

 Take the datum with the Fock vector `x` as archimedean part and the function `Φ` at the ramified
places of `𝔠`. The theta kernel of the pair `(W, 0)`, twisted by characters `α`, `β` of `[U(1)]`,
at this datum and at adelic unitary elements `(g, h)` is `β (det g)⁻¹ * Φ 0` times the theta
functional of the space `Hom(W, 0)` at the image of the vacuum under the integrated operator of
`x`. 

### `pairTheta_source_zero`

 The theta kernel of the pair `(0, W)` twisted by `α` and `β`, at the datum with the vacuum as
archimedean part and the function `Ψ` at the ramified places of `𝔠`, is `α (det g) * Ψ 0`. 

### `thetaLarge_stdSpace_empty_vacVector_one`

 For the pair `(W, 0)`, the theta integral at `1` of the datum with the vacuum as archimedean
part and the function `Φ` at the ramified places of `𝔠` is the volume of `[U(0)]`, the domain of
integration, times `Φ 0`. 

### `exists_analyticOnNhd_eq_L_mul_gammaIntegral`

 For each weight `m` there are positive reals `a`, `a'` with the following property for every
split tame character `𝔠 = (ν, S)` of weight `m` (weight positive everywhere, tame part nontrivial
exactly on a nonempty finite set `S` of places disjoint from its conjugate). There exist `κ ≠ 0`,
`ε` with `‖ε‖ = a`, `ε'` with `‖ε'‖ = a'`, and a function `𝒵` analytic on all of ℝ (in the proof,
the zeta integral of the test function) such that for `x ≥ 1` both `𝒵(x)/ε` and `𝒵(1 - x)/ε'` equal
`|α₀| ^ x ∏_{w ∈ S} q_w ^ (x - 1/2) L^S(x, ν) · gammaIntegral E m x · κ`. Here `α₀ = scaleIdele E`
is the idele of the Weil data that fixes the measures, `q_w` is the order of the residue field at
`w`, and `gammaIntegral E m x` is the archimedean zeta integral; classically, though not proved or
used here, it is a constant times `∏_w Γ(x + m w)`. 

### `analyticAt_ideleAbs_rpow_mul_prod_rpow`

 The factor `|α₀| ^ x ∏ q_w ^ (x - 1/2)` of the zeta integral is analytic in `x`. Here `α₀` is
`WeilData.scaleIdele E` and `q_w` is the order of the residue field at the ramified place `w` of
`𝔠`. 

### `exists_analytic_extension_functional_equation`

 Functional equation in absolute values, on a real interval (a special case of the main theorem
of Tate's thesis). Let `k ≤ μ w` for every infinite place `w`. For a split tame character
`𝔠 = (ν, S)` of weight `μ` the function `L^S(x, ν)` of `x ≥ 1` extends to an analytic function `Λ`
of real `x > -k`, and `L♯(1 - z) = C z * L♯(z)` for real `1 ≤ z < k + 1`. Here
`L♯(z) = ‖L^S(z, ν)‖ ∏_{w ∈ S} q_w ^ (z - 1/2)` is `lSharp 𝔠 z`, `L♯(1 - z)` is formed with `Λ`,
and `C z > 0` does not depend on the character. 

### `exists_analytic_extension_ne_zero`

 Let `k ≤ μ w` for every infinite place `w`, and let `𝔠 = (ν, S)` be a split tame character of
weight `μ`. The `L`-function `L^S(x, ν)` of `x ≥ 1`, written `𝔠.character.L 𝔠.ramifiedPlaces x`,
extends to an analytic function `Λ` of real `x > -k` that has no zero at the integers `j > -k`. 
