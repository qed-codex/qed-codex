---
{
  "module": "src/Lib/DiscreteSeries/Character/OpenOrbitIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/OpenOrbitIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/OpenOrbitIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Orbital integrals of discrete series coefficients and Weyl characters of U(n)

This file begins the computation of the orbital integrals of the discrete series coefficient
`New.HCParam.dsCoeff l` of `G = U(diag ε)` over the compact torus. Here `l = 2λ` is the parameter,
and `ε` is implicit in its type. If `l` has a gap then, at a point `x` of the torus with
`diag ε * x` accretive (`A` accretive: `A + Aᴴ` positive definite), the orbital integral is, up to a
constant of modulus one, a multiple of Weyl's character of `U(n)` of highest weight `λ - ρ`, minus
an error given by an integral over the unitary matrices outside the open orbit `G B`. Here `B` is
the group of invertible matrices that are upper triangular for `l`, that is, `b i j = 0` whenever
`l j < l i`; they are lower triangular when the coordinates are listed with `λ` decreasing. If `o`
reverses the order of `l`, the error is small at `diag(t ^ o i)` for small `t = 2⁻¹ ^ s`, so a
Laurent polynomial that is a multiple of it has no monomial of low level.

## Main definitions and results

* `New.le_norm_weightMinors_twoPowDiagConj`: for unitary `u`, if `f` decreases along `l` by steps of
  at least `|m|` and `h ≤ |l i - l j|`, a lower bound for `New.weightMinors l` at `u* diag(2^f) u`
  by its value at `diag(2^f)` and the entry `u i j`.
* `New.Orbital.orbital_eq_char_sub_offOrbitIntegral`: the formula for the orbital integral described
  above, with the error `New.Orbital.offOrbitIntegral`.
* `New.Orbital.coeff_eq_zero_of_low_level`: if `l` has a gap and `o` reverses its order, a Laurent
  polynomial that is a multiple of this error has no monomial of low level, by the bound
  `New.Orbital.exists_norm_offOrbitIntegral_le`.

Notions from other files:
* `New.HCParam.HasGap`: `l = 2λ` has distinct entries of the parity of `card n - 1`, and those of
  `λ` with different signs `ε` differ by at least `h`.
* `New.paramAddRho`: The integer vector `λ + ρ`, for ρ the half sum of the roots positive for `l`.
* `New.HCParam.dsCoeff`: The function c_λ on complex matrices given by Flensted-Jensen's integral
  `New.HCParam.flenstedJensen`; on K = U(diag ε) ∩ U(n) it is m_Λ with Λ = λ + ρ − 2ρ_c.
* `New.diagTorus`: For a tuple t of complex numbers of modulus one, the diagonal matrix diag(t) as
  an element of U(diag ε); `New.diagTorusK x` is diag(x) as an element of `maxCompactU 1`, which is
  U(n).
* `New.Orbital.torusEval`: For a tuple x of unit complex numbers, the algebra homomorphism from
  Laurent polynomials to ℂ sending the monomial of exponent ν to ∏ x_a^{ν_a}.

## Relation to the literature

This is part of the known computation of the discrete series character on the compact Cartan
subgroup by orbital integrals, see `Lib.DiscreteSeries.Character.FormalDegree`.



## Principal minors of conjugated diagonal matrices

Conventions: `New.weightMinors l g` is the product over `t ∈ ℤ` of the principal minors
`New.principalMinor` of `g` on `{i | t ≤ l i}`, those with `t ≤ 0` divided by `det g`.


### `twoPowDiagConj`

 The matrix `u* diag(2^f) u`. For unitary `u` it is a positive definite matrix with eigenvalues
`2 ^ (f i)`. 

### `posSemidef_twoPowDiagConj`

 For every invertible `u`, the matrix `u* diag(2^f) u` is positive semidefinite. 

### `norm_principalMinor_twoPowDiagConj_mono`

 The norms of the principal minors of `u* diag(2^f) u` increase with the exponents `f`. 

### `det_twoPowDiagConj`

 For unitary `u`, the determinant of `u* diag(2^f) u` is that of `diag(2^f)`. 

### `inv_twoPowDiagConj`

 For unitary `u`, the inverse of `u* diag(2^f) u` is `u* diag(2^(-f)) u`. 

### `norm_principalMinor_mul_gain_le`

 Let `u` be unitary, let `f a + |m| ≤ f c` whenever `l c < l a`, let `h ≤ |l i - l j|` and
`l j ≤ l i`, and let `t` exceed some value of `l`. The minor of `u* diag(2^f) u` on `{k | t ≤ l k}`
is at least that of `diag(2^f)`, times `|u i j|² 2^m` if this set separates `i` from `j` with
`l i - h < t ≤ l i`. 

### `le_norm_weightMinors_twoPowDiagConj`

 Let `u` be unitary, let `f a + |m| ≤ f c` whenever `l c < l a`, and let the natural number `h`
be at most `|l i - l j|`. Then `|m_l(D)| (|u i j|² 2^m) ^ h ≤ |m_l(u* D u)|`, where `D = diag(2^f)`
and `m_l = New.weightMinors l` is the product of principal minors of weight `l`. 


## The orbital integral as a Weyl character minus an off-orbit error

The level of an exponent `γ` for `o : n → ℤ` is `o ⬝ᵥ γ`.


### `offOrbitIntegral`

 For `l = 2λ` and `J = diag ε`, the integral of `m_{-(λ-ρ)}(kᴴ J k) / m_{-(λ+ρ)}(kᴴ A k)` over
the `k` in `U(n)` outside `New.openOrbit ε l` (the open orbit `G B`), for the Haar
measure of mass one, where `m` is `New.weightMinors`. 

### `isKDominant_neg_compactForm_lowestKType`

 For `l = 2λ` with a gap (see `HCParam.HasGap`), the weight
`-l.compactForm.lowestKType = -(λ - ρ)` is dominant for `U(n)` when the coordinates are listed with
`l` increasing: it is antitone along `l`, as `IsKDominant` asks with all signs `1`. 

### `sign_mul_orbital_eq_integral_weightMinors_div`

 The orbital integral as an integral over `G = U(diag ε)`: let `l = 2λ` have gap `h` (distinct
entries congruent to `card n - 1` mod 2, with `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`), and let `x`
lie on the torus with `A = J x` accretive (`J = diag ε`). If the integrand
`m_{-(λ-ρ)}(gᴴ J g) / m_{-(λ+ρ)}(gᴴ A g)` is integrable, then `σ ∫_G c_λ(g⁻¹ x g) dg` equals its
integral over `G`. Here `ρ` is the half sum of roots positive for `l`, `m_w = weightMinors w` is the
product of principal minors of weight `w`, `c_λ = l.dsCoeff` is `g ↦ Ξ(a, a⁻¹g)` with `a` the
block-diagonal part of `g` and `Ξ` the normalised integral `flenstedJensen`, and
`σ = m_{-(λ-ρ) - Λ}(J)` with `Λ = l.lowestKType = λ + ρ - 2ρ_c`. 

### `integral_weightMinors_inv_mul_mul_weightMinors`

 Schur orthogonality for the coefficient `m_Λ = weightMinors Λ` on `U(n)`, where `l` has gap `h`
and `Λ = l.compactForm.lowestKType = λ - ρ` (`l.compactForm` is `l` with all signs `1`; this is not
the `Λ` of `dsCoeff`): for invertible `a` the integral of `m_Λ(u⁻¹ a) m_Λ(u)` is `N m_Λ(a)`, with
`N = ∫ |m_Λ(u)|² du` the number `Λ.kTypeNormSq`. 

### `kTypeNormSq_mul_kTypeChar_eq_integral`

 Let `l = 2λ` have gap `h` (distinct entries congruent to `card n - 1` mod 2, with
`|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`), and let `x` be on the torus with `A = J x` accretive
(`J = diag ε`). Then the integral of `m_{-(λ-ρ)}(kᴴ J k) / m_{-(λ+ρ)}(kᴴ A k)` over `U(n)` (Haar
measure `haarK 1` of mass one) is `N · χ(x)`, where `χ` is the character of highest weight `λ - ρ`
and `N = ∫ |m_{λ-ρ}(k)|² dk` over `U(n)`. Here `m_w = weightMinors w` is the product over integers
`t` of the principal minor on `{i | t ≤ w i}`, each factor with `t ≤ 0` divided by the
determinant. 

### `weightMinors_conjTranspose_mul_mul_borel`

 For injective `l`, a weight `w` antitone along `l` (`IsKDominant 1 l w`), an invertible `b`
upper triangular for `l`, and invertible `y`, `M`: replacing `y` by `y b` multiplies
`m_w(yᴴ M y)` by `|∏ k, b k k ^ w k| ^ 2`, where `m_w = weightMinors w`. 

### `diagChar_div_diagChar_eq_twoRho`

 For injective `l` and invertible `b` upper triangular for `l`, the quotient of
`diagChar w b = ∏ k, b k k ^ w k` at the weights `-l.compactForm.lowestKType` and `-paramAddRho l`
(these are `-(λ - ρ)` and `-(λ + ρ)` for a parameter `l = 2λ`) is its value at
`twoRho l ⊤ = 2ρ`, the sum of the roots that are positive for `l`. 

### `orbital_eq_char_sub_offOrbitIntegral`

 The orbital integral is the part of Weyl's character over the open orbit. For `l = 2λ` of gap
`h` there is `σ` of modulus one such that, at every point `x` of the torus with `J x` accretive
(`J = diag ε`), `σ ∫_G c_λ(g⁻¹ x g) dg` is `N · χ(x)` minus `offOrbitIntegral l (J x)`. Here `c_λ`
is `l.dsCoeff`, `χ` is the character of `U(n)` of highest weight
`l.compactForm.lowestKType = λ - ρ`, and `N = ∫ |weightMinors (λ - ρ) k|² dk` over `U(n)`, with
`weightMinors ν` the product of principal minors of weight `ν`. Also, `offOrbitIntegral l A` is the
integral of `weightMinors_{-(λ-ρ)}(kᴴ J k) / weightMinors_{-(λ+ρ)}(kᴴ A k)` over the `k ∈ U(n)`
outside `openOrbit ε l`. 

### `analyticAt_offOrbitIntegral`

 The integral `offOrbitIntegral l A` over the unitary matrices outside the open orbit is
complex analytic in the matrix `A` at every accretive `A` (one with `A + Aᴴ` positive definite). 

### `eq_mul_offOrbitIntegral_of_pos`

 Let `P`, `Q` be Laurent polynomials with `P(x) = Q(x) * offOrbitIntegral l (J x)` at the points
`x` of the torus with `J x` accretive, where `J = signMatrix ε`, evaluation at `x` is `torusEval x`,
and `offOrbitIntegral l A` is the integral of `m_{-(λ-ρ)}(kᴴ J k) / m_{-(λ+ρ)}(kᴴ A k)` over the
`k ∈ U(n)` outside `openOrbit ε l`, with `l = 2λ`, `ρ` the half sum of roots positive for `l`, and
`m = weightMinors`. Then for real `z > 0` (written `0 < z` in the order of `ℂ`) and every integer
vector `f`, this identity holds at `x = ε * z ^ f`, by analytic continuation from `|z| = 1`. At that
point `J x = diag (z ^ f)`, and `weightMinors γ J` is the monomial of exponent `γ` at `ε`. 

### `exists_entry_large_outside_orbit`

 For every parameter `l` and natural number `h` there is `r > 0` such that every unitary matrix
`k` outside the open orbit `openOrbit ε l` has an entry `k i j` between opposite signs
(`ε i ≠ ε j`) with `r |weightMinors (-Λ) (kᴴ J k)| < |k i j| ^ (2 h)`. Here `J = signMatrix ε` and
`Λ = l.compactForm.lowestKType`, so that the minor is the numerator of the integrand of
`offOrbitIntegral`. 

### `exists_norm_offOrbitIntegral_le`

 Let `l = 2λ` have gap `h`: its entries are distinct, of the parity of `card n - 1`, and those
with opposite signs `ε` differ by at least `2 h`. Let `o` strictly reverse the order of `l`. Then
for every integer vector `e`, as `s → ∞`, `offOrbitIntegral l A` is `O(2⁻¹ ^ (s L))` at
`A = diag(2⁻¹ ^ (s o + e))`, where `L = o ⬝ᵥ paramAddRho l + h` and `paramAddRho l = λ + ρ`. Here
`offOrbitIntegral l A` is the integral of `m_{-(λ-ρ)}(kᴴ J k) / m_{-(λ+ρ)}(kᴴ A k)` over the
`k ∈ U(n)` outside `New.openOrbit ε l`, with `J = diag ε` and `m = weightMinors`. 

### `coeff_eq_zero_of_low_level`

 Let `l = 2λ` have gap `h`: its entries are distinct, congruent to `card n - 1` mod 2, and
`|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. Let `P`, `Q` be Laurent polynomials with
`P(x) = Q(x) · offOrbitIntegral l (J x)` at every torus point `x` where `J x` is accretive
(`J = diag ε`); here `offOrbitIntegral l A` is the integral of
`m_{-(λ-ρ)}(kᴴ J k) / m_{-(λ+ρ)}(kᴴ A k)` over the `k ∈ U(n)` outside `New.openOrbit ε l`, with
`m = weightMinors`. If `o` strictly reverses the order of `l` (`l j < l i` implies `o i < o j`) and
`o ⬝ᵥ γ < o ⬝ᵥ paramAddRho l + o ⬝ᵥ β + h` for every exponent `β` of `Q` (`paramAddRho l = λ + ρ`),
then the coefficient of `x^γ` in `P` is zero. 
