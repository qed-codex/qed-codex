---
{
  "module": "src/Lib/CM/Integrality/IntegralSections.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/IntegralSections.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/IntegralSections.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The integrality principle in one variable

* `New.CMLattice.mem_span_monomialSection`: a section with integral torsion values is an integral
  combination of monomials; `New.CMLattice.exists_polynomial_of_even` treats even sections.
* `New.CMLattice.exists_taylorVia_eq_theta_pow_mul`: its Taylor series lies in `θ ^ m 𝒪[[y]]`.

Write the section as `θ ^ m (P₀(x) + y P₁(x))`, where `P₁ = 0` if the section is even, and
interpolate at the nodes `x(tᵢ)`, where `tᵢ = t / 2 ^ i` and `i ≥ 1`. The numbers `θ[tᵢ]`, `x'(tᵢ)`
and `x(tᵢ) - x(tⱼ)` for `i ≠ j` are units.

Notions from other files:

For a lattice `Λ = C.Λ` with a point `t = C.t` of order two modulo `Λ`:
* `θ` is the normalised twisted translate of the sigma function `σ` by `t`; it vanishes on `t + Λ`.
* `x = translatedX` is `℘(z + t) - ℘(t)` and `y = translatedY` is `(℘'(z + t) - a₁ x(z)) / 2`, where
  `a₁ = C.a₁` is a constant of `C` with `‖ιₚ a₁‖ ≤ 1`; off `t + Λ`,
  `x' ^ 2 = x (4 x ^ 2 + a₁ ^ 2 x + 4)`.
* `sections m` is the space of theta functions of degree `m`; the monomial of `(a, b, c)` is
  `θ ^ (a + 2 b + 3 c) x ^ b y ^ c` off `t + Λ`, with degree
  `monomialDeg (a, b, c) = a + 2 b + 3 c`, and `spanningExponents m` is the set of triples with
  `c ≤ 1` and `a + 2 b + 3 c = m`.
* The value `G[u]` is the value at `0` of the translate of `G` by `u`, twisted by the degree `m`
  (written `torsionValue m G u`); it is called a torsion value if `u` is a torsion point, and
  `HasIntegralValues` says that all torsion values have norm at most `1` in `ℂ_p`, under the ring
  homomorphism `ιₚ : ℂ →+* ℂ_[p]` fixed by the instance `PadicPlace p`.

## Relation to the literature

Known result: integral expansions of theta functions of CM elliptic curves, at ordinary primes
`p ≥ 5`. Here `p` is arbitrary, but `d` is a prime congruent to `7` modulo `8`. Source: Bannai and
Kobayashi, Algebraic theta functions and the p-adic interpolation of Eisenstein-Kronecker numbers,
Duke Math. J. 153 (2010), 229-295, after Norman and Mazur–Tate.

Known result: for a lattice with complex multiplication, the value of the Siegel function at a
torsion point is a unit if two different prime ideals divide the annihilator of the point. Only the
points `t / 2 ^ i` are treated, by doubling. Source: Ramachandra and Robert; Kubert and Lang,
*Modular Units*.


### `norm_coeff_le_one_of_norm_eval_le_one`

 Lagrange interpolation: if the points `x i` are integral and any two have difference of norm
`1`, then a polynomial with integral values at all of them has integral coefficients. 

 ### Sections as polynomials in `x` and `y` 

### `translatedY_sub_translatedY_neg`

 The difference `y(z) - y(-z)` is the derivative of `x = translatedX`, where
`y = translatedY`. 

### `exists_eq_theta_pow_mul_eval`

 A section of degree `m` is `θ ^ m (P₀(x) + y P₁(x))` off `t + Λ`, where `x = translatedX`,
`y = translatedY`, and `P₀`, `P₁` are polynomials whose terms `x ^ i`, `y x ^ i` have pole order
at most `m`. 

### `eq_zero_of_even_of_eq_theta_pow_mul_eval`

 If an even function `f` is `θ ^ m (P₀(x) + y P₁(x))` off `t + Λ`, where `x = translatedX` and
`y = translatedY`, then `P₁ = 0`. 

### `exists_eq_theta_pow_mul_eval_of_even`

 An even section of degree `m` is `θ ^ m P(x)` off `t + Λ`, with `x = translatedX` and
`2 i ≤ m` for every term `x ^ i` of `P`. 

### `eq_of_mem_sections_of_eq_off_translate`

 A section that agrees off `t + Λ` with an entire function `g` equals `g`. 

### `theta_pow_mul_eval_eq_sum`

 If every exponent `i` of `P` has `2 i + 3 e ≤ m`, then `θ ^ m y ^ e P(x)` is the combination of
the monomials of degree `m` with the coefficients of `P`, off `t + Λ`. Here `x = translatedX`
and `y = translatedY`. 

### `theta_pow_mul_eval_eq_sum_range`

 If `P` has degree at most `m / 2`, then `θ ^ m P(x)`, with `x = translatedX`, is the
combination of the monomials of `(m - 2 i, i, 0)`, `i ≤ m / 2`, with the coefficients of `P`, off
`t + Λ`. 

### `exists_mem_span_monomialSection_eq_theta_pow_mul_eval`

 Let `e ≤ 1`, and let `P` have coefficients integral in `ℂ_p` and `2 i + 3 e ≤ m` for each of its
exponents `i`. Then `θ ^ m translatedY ^ e P(translatedX)` agrees off `t + Λ` with an entire
function that is an integral combination of the monomials of the triples `(a, b, c)` with `c ≤ 1`
and degree `a + 2 b + 3 c = m` (the set `spanningExponents m`). 

### `taylorVia_eq_of_eq_theta_pow_mul_eval`

 If `f = θ ^ m P(x)` off `t + Λ`, with `x = translatedX`, then the same identity holds for the
Taylor series at `0`, with `ιₚ` applied to the coefficients. 

 ### Units at the points `t / 2 ^ i`

The lemmas of this part prove the case of the theorem on Siegel units (Ramachandra, Robert) that is
used. The proof follows the pair `w(u) = (ιₚ θ[u] ^ 2, ιₚ σ[u] ^ 2)` of elements of `ℂ_p`, that is
`squarePair u`, under doubling. 

### `HasIntegralValues.norm_le_one_of_eq_theta_pow_mul`

 Let `f` have integral torsion values in degree `m`, and let `u` be a torsion point where
`θ[u]` is a unit. If `f(u) = θ(u) ^ m c`, then `c` is integral. 

### `squarePair_snd`

 If `u + t` is not a period, the second coordinate of the pair
`squarePair u = (ιₚ θ[u] ^ 2, ιₚ σ[u] ^ 2)` is `ιₚ (x(u))` times the first, where
`x = translatedX`. 

### `halvingPoint`

 The points `tᵢ = t / 2 ^ i`, where `t` is the chosen point of order two modulo the lattice. 

### `eq_one_of_sq_mul_eq_one`

 If numbers `a ∈ [0, 1]` and `b ≤ 1` satisfy `a ^ 2 b = 1`, then `a = 1`. 

### `norm_det_squarePair_halvingPoint`

 If `2 ^ j v` is a period and `tⱼ = t / 2 ^ j`, then the pairs `w(tⱼ)` and `w(v)`, where
`w = squarePair`, reduce to distinct points of the projective line (their determinant is a unit):
doubling `j` times takes the first to `(0 : 1)` and the second to `(1 : 0)`. 

### `norm_torsionValue_theta_halvingPoint`

 With `tᵢ = t / 2 ^ i` the torsion value `θ[tᵢ₊₁]` is a unit, as `w(tᵢ₊₁)`, where
`w = squarePair`, does not reduce to `w(t₀) = (0 : 1)`.

This is a local analogue of the unit property of Siegel units (Ramachandra, Robert), only for `θ` at
the points `t / 2 ^ (i + 1)`, at the chosen place above `p`, with `d` prime `≡ 7 mod 8`. 

### `norm_torsionValue_sigma_halvingPoint`

 Let `C` be a CM lattice (`d` a prime `≡ 7 mod 8`) with point `t` of order two, let
`tᵢ = t / 2 ^ i`, and let `ιₚ : ℂ → ℂ_p` be the chosen `p`-adic place. The torsion value `σ[tᵢ]`
(value at 0 of the degree-1 twisted translate of `C.σ` by `tᵢ`) has norm 1, as `w(tᵢ)`, where
`w = squarePair`, does not reduce to `w(2 t) = (1 : 0)`.

This is a local form of the unit property of Siegel units (Ramachandra, Robert), only at the points
`t / 2 ^ i` of these CM lattices and at the chosen place above `p`. 

### `add_t_notMem_of_norm_eq_one`

 A point `u` with `‖θ[u]‖ = 1` does not lie in `t + Λ = -t + Λ`, the zero set of `θ`. 

### `norm_translatedX_le_one`

 At a torsion point `u` where `θ[u]` is a unit, `x(u) = translatedX u` is integral in `ℂ_p`. 

### `norm_translatedY_le_one`

 At a torsion point `u` where `θ[u]` is a unit, `y(u) = translatedY u` is integral in `ℂ_p`. 

### `norm_translatedX_halvingPoint_sub`

 The numbers `x(tᵢ₊₁)`, where `x = translatedX` and `tᵢ = t / 2 ^ i`, are distinct modulo the
maximal ideal of the integers of `ℂ_p`. 

### `norm_deriv_translatedX_halvingPoint`

 For `tᵢ = t / 2 ^ i` the number `x'(tᵢ₊₁) = σ[tᵢ] / θ[tᵢ₊₁] ^ 4` is a unit, where
`x = translatedX`. 

 ### Interpolation and the integrality principle 

### `norm_coeff_le_one_of_norm_eval_halvingPoint_le_one`

 A polynomial whose values at the nodes `translatedX (t / 2 ^ (i + 1))` are integral in `ℂ_p`
has integral coefficients. 

### `norm_coeff_le_one_of_hasIntegralValues`

 Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, with point `t` of order two, and let
`ιₚ : ℂ → ℂ_p` be a `p`-adic place. Suppose `f z = θ z ^ m (P₀(x z) + y z · P₁(x z))` whenever
`z + t ∉ Λ`, where `x = translatedX` is `℘(z + t) - ℘(t)` and `y = translatedY` is
`½(℘'(z + t) - a₁ x(z))`. Suppose also that `f` has integral torsion values in degree `m`, meaning
every torsion value `f[u]` has `‖ιₚ f[u]‖ ≤ 1`. Then every coefficient of `P₀` and `P₁` has image
under `ιₚ` of norm at most `1`. 

### `mem_span_monomialSection`

 Let `d` be a prime `≡ 7 (mod 8)` and fix a `p`-adic place `ιₚ`. Let `f` be a section of degree
`m` (a theta function for `Λ` of degree `m`) with integral torsion values: for every torsion point
`u`, the value `f[u]` satisfies `‖ιₚ f[u]‖ ≤ 1`. Then `f` is a combination, with coefficients
integral in `ℂ_p`, of the monomials of the triples `(a, b, c)` with `c ≤ 1` and degree
`a + 2 b + 3 c = m` (the set `spanningExponents m`); off `t + Λ` these monomials are
`θ ^ m translatedX ^ b translatedY ^ c`. The scalars are the complex numbers whose image under `ιₚ`
lies in the valuation ring `valRingCp p`. 

### `IsIntegralEvenExpansion`

 The polynomial `R` is an integral expansion of `f` in degree `m` in the monomials
`θ ^ (m - 2 i) σ ^ (2 i)`, which are `θ ^ m x ^ i` off `t + Λ`, where `x = translatedX`. 

### `IsIntegralEvenExpansion.norm_coeff_le_one`

 The coefficients of `R` are integral in `ℂ_p`. 

### `IsIntegralEvenExpansion.two_mul_natDegree_le`

 The degree of `R` is at most `m / 2`. 

### `IsIntegralEvenExpansion.eq_sum`

 The function `f` is `∑ Rᵢ θ ^ (m - 2 i) σ ^ (2 i)`, the sum being over `i ≤ m / 2`. 

### `IsIntegralEvenExpansion.taylorVia_eq`

 The Taylor series of `f` at `0`, with `ιₚ` applied to the coefficients, is `θ ^ m R(x)`. 

### `exists_polynomial_of_even`

 Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, with point `t` of order two, and let `ιₚ` be
a `p`-adic place. Let `f` be an even section of degree `m` (a theta function for `Λ` with hermitian
form `m H` and multiplier `χ ^ m`) whose torsion values all have `ιₚ`-norm at most `1`. Then
`f = ∑ Rᵢ θ ^ (m - 2 i) σ ^ (2 i)` for a polynomial `R` with `ιₚ`-integral coefficients and degree
at most `m / 2`, and the Taylor series of `f` at `0` is that of `θ ^ m R(x)`, where
`x(z) = ℘(z + t) - ℘(t)` is `translatedX`; these are the clauses of `IsIntegralEvenExpansion`. 

### `exists_taylorVia_eq_theta_pow_mul_of_mem_span`

 Let `f` be a combination, with coefficients integral in `ℂ_p`, of monomials of degree `m`.
Then `f` is analytic at `0` and its Taylor series lies in `θ ^ m 𝒪[[y]]`, where
`𝒪[[y]] = integralSeriesRing` is the ring of integral power series in the Taylor series of
`y = translatedY`. 

### `exists_taylorVia_eq_theta_pow_mul`

 Let `d` be a prime congruent to 7 mod 8. Let `f` be a section of degree `m` (a theta function
for `Λ` with hermitian form `m H` and multiplier `χ ^ m`) whose torsion values `f[u]` at all torsion
points `u` satisfy `‖ιₚ f[u]‖ ≤ 1`. Then the Taylor series of `f` at `0`, with `ιₚ` applied to its
coefficients, is the `m`-th power of that of the degree-one theta function `θ` times an element of
`integralSeriesRing`, the ring `𝒪[[y]]` of integral power series in the series of
`y(z) = ½(℘′(z + t) − a₁ x(z))` (`translatedY`), where `x(z) = ℘(z + t) − ℘(t)` and `t` is the
chosen point of order two. 
