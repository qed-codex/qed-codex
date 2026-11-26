---
{
  "module": "src/New/Spanning/Frames/RealBandLimits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealBandLimits.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealBandLimits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The normalized cell integral Ξ and the local bounds at ℂ for cut Bessel functions

This file defines the normalized cell integral Ξ at the chart of the top floor, proves that it is
continuous, and gives the descent from each floor to the one below. It bounds the mass on the bottom
floor by the position ball and remote positions, and proves decay in the frequency and for unequal
last entries. At the end, a cut Bessel function `F` of a Bessel function `W` satisfies the local
bounds `New.HasLocalBounds` read by the sieve, given bounds on the matrix coefficient of `W` and on
volumes of balls. The place ℂ lies over a real place of the totally real subfield, and the
docstrings call it a real place.

`New.HasLocalBounds` asks for a system of forms `New.SieveSystem` on floors `0, …, ϱ + 1`, each
below the top an integral of the next one.

Throughout `F` is the cut of the Bessel function `W`, n = ϱ + 1, k = card κ and r is the rank of G₁.

## Main definitions and results

* `New.Floors.IsCutBessel.norm_floorForm_zero_le`: the mass at a real place, by the position ball
  and remote positions.
* `New.Floors.IsCutBessel.norm_floorForm_wave_le`, `New.Floors.IsCutBessel.norm_floorForm_heads_le`:
  decay in the frequency and for unequal last entries.
* `New.Floors.exists_hasLocalBounds_of_isCutBessel`: the local bounds.

Notions from other files:
* `New.Shape.G₁`: The unitary group of the complex hermitian form made of ϱ hyperbolic planes, the
  standard positive form on κ, and one vector z with h(z, z) = −1. `New.Shape.Form.besselU`: The
  unipotent group 𝖴 of block upper unitriangular elements with middle block 1.
  `New.besselQuotMeasure` computes integrals over 𝖴∖G₁. The frame is (e₀, …, e_{ϱ-1}, z), where e_a,
  e*_a are the hyperbolic pairs of basis vectors, and `New.Shape.top` is the position of z.
  `New.realFrameGram` x is the matrix of the products h(f_a, x f_b) of the frame vectors f_a; its
  entries are the frame entries of x.
* `weylElem j p`: The Weyl element w_p, with e_a ↦ p_a e*_a and e*_a ↦ e_a / p̄_a for a < j.
  `New.wave`: The character c ↦ exp (c - c̄) of ℂ. `New.unitOrOne`: c as a unit if c ≠ 0, and 1
  otherwise.
* `New.Shape.scaledVolumeRatio`: The constant π ^ ((2ϱ + 1) k) · vol U(k) / vol U(r), where k = card
  κ and r is the rank of G₁. `New.dampedPower`: The gain r ^ K min(1, r)⁶.
* `New.Floors.IsCutBessel` (in `New.Spanning.Frames.RealShells`): the cut, at size ρ, of a
  normalised Bessel function of irreducible type, with the numerical constraints.
* `New.Floors.IsCutBessel.formConst` (in `New.Spanning.Frames.RealShells`): the normalising constant
  vol U(k) / vol U(r) / (λ · card I)² of the forms.

## Relation to the literature

The estimates supply the local bounds of the Bessel systems built in
`New.Spanning.Bessel.FillingData`.



## The normalized cell integral Ξ and the top floor


### `normalizedCellIntegral`

 The vector Ξ(p): the tensor J(w_p σ_p) times the real normalising factor of
`New.normalizedOrbitalIntegral`. Here J(γ) = ∫ F(y) ⊗ F(γ⁻¹y)^* dy, w_p is the Weyl element
`weylElem ϱ p`, and σ_p is the chart `New.Floors.cellChart` of floor ϱ at the last entry `p ϱ`. 

### `IsCutBessel.continuous_normalizedCellIntegral`

 The vector Ξ(p) = `normalizedCellIntegral F p` of a cut Bessel function `F` is continuous in the
list `p` of units. 

### `IsCutBessel.inner_embedH_mul`

 The compact group U(κ), embedded in G₁ by `embedH`, acts on the values of a cut Bessel function
by unitary maps, so left translation by it keeps the inner products of these values. 

### `IsCutBessel.inner_normalizedCellIntegral_eq_of_last_entry`

 Let `F` be a cut Bessel function and let `p`, `q` have the same entry at index `ϱ`, `q ϱ = p ϱ`.
Let `σ` fix the hyperbolic basis vectors of floor below `ϱ`, with h(z, σ
z) = `realFrameGram σ 𝔰.top 𝔰.top` equal to `p ϱ`. Then the inner product of
`normalizedCellIntegral F p` and `normalizedCellIntegral F q` equals that of
`normalizedOrbitalIntegral σ F p` and `normalizedOrbitalIntegral σ F q`. 

### `IsCutBessel.partialCorrelationProduct_top_eq`

 The integrand `partialCorrelationProduct` above the top floor ϱ, for a cut Bessel function `F`,
the Weyl elements w_p, w_q = `weylElem ϱ p`, `weylElem ϱ q` and `σ` fixing the hyperbolic basis
vectors, is ⟪F y, F (y x)⟫ ⟪F (σ⁻¹ w_q⁻¹ y x), F (σ⁻¹ w_p⁻¹ y)⟫ at the position `x` and the point
`y`. 

### `IsCutBessel.descent_last_entry_of_norm_le_one`

 Descent on the top floor ϱ. Let `F` be a cut Bessel function, φ a measurable function on ℂ with
|φ| ≤ 1, and `p`, `q` lists of units. Let p_c and q_c be these lists with the entry at position ϱ
set to c (to 1 if c = 0), and let Φ(c) = φ(c) ⟪Ξ(p_c), Ξ(q_c)⟫, where Ξ =
`normalizedCellIntegral F`. Then Φ is Lebesgue integrable on ℂ, and its integral is `formConst`
times the form `floorForm` of floor ϱ at `p`, `q` with the weight x ↦ φ(h(z, x z)). 

### `IsCutBessel.integrable_and_integral_wave_mul_inner_normalizedCellIntegral`

 Descent on the top floor for the character `wave c = exp (c - c̄)`. Give `p` and `q` the common
entry c at position ϱ. The integral over c of `wave (ξ c)` times the Gram form of
`normalizedCellIntegral` converges. It is `formConst` times the form of floor ϱ with the weight
x ↦ `wave` (ξ h(z, x z)). 

### `quotientPairing`

 The matrix coefficient `⟪A, R(x) B⟫` in `L²(𝖴∖G₁)`, where `R(x)` is right translation, 𝖴 is the
unipotent group `besselU` and `besselQuotMeasure` computes integrals over `𝖴∖G₁`. 

### `sq_lintegral_enorm_inner_le`

 Cauchy–Schwarz on `𝖴∖G₁`; right translation keeps the norm of a Bessel function. Let `A` be
strongly measurable, `B` a Bessel function of type `rep`, and `x` in `G₁`. For `besselQuotMeasure`,
the square of the integral of ‖⟪A y, B (y x)⟫‖ is at most the product of the integrals of ‖A y‖² and
‖B y‖². 


## The mass on the bottom floor, decay, and the local bounds


### `isBesselFunction_sub`

 The difference of two Bessel functions of the same type `rep` is a Bessel function. 

### `IsCutBessel.enorm_quotientPairing_sub_le`

 Let `F` be the cut of the Bessel function `W` with base `b` and degree `f`, so that their L²
distance is at most `b ^ (-r ^ 3 f) √(card I)`. Replacing `F` by `W` changes the matrix coefficient
`quotientPairing` by at most `2 b ^ (-r ^ 3 f) card I` at every position `x`. 

### `IsCutBessel.formIntegrandL1Norm_zero_eq`

 For a cut Bessel function `F` and `x` in G₁, the number `formIntegrandL1Norm` that bounds the
form of floor `0` with weight `1` at the position `x` is λ² |∫_{𝖴∖G₁} ⟪F(y), F(y x)⟫ dy|². The
integral is the matrix coefficient `quotientPairing F F x`, and λ = `haarRatio` is the ratio of the
measure of the place datum to the Haar measure of G₁. The value does not depend on the lists `p`,
`q`. 

### `lintegral_add_sq_le`

 Minkowski's inequality in `L²`: if `g` and `h` have `L²` norms at most `α` and `β`, then `g + h`
has `L²` norm at most `α + β`. 

### `IsCutBessel.rho_le_pow`

 The box radius `ρ = b ^ (6 n + 2)` of a cut Bessel function is at most `b ^ (7 n)`. 

### `IsCutBessel.r_eq_add`

 For a cut Bessel function `F` (`IsCutBessel F rep ρ s b W f`), the rank `𝔰.r` = 2ϱ + k + 1 of G₁
equals `s + 5 * 𝔰.n + 5`. This follows from `k = s + 3 n + 6`. 

### `IsCutBessel.norm_le_of_mem_positionBall`

 Let `F` be a cut Bessel function (`IsCutBessel`) with box radius `ρ` and base `b`. Let
n = ϱ + 1, where ϱ is the number of hyperbolic planes of `𝔰`, and let r be the rank of G₁. If `x`
lies in the position ball at the scale `T = b ^ (6 r) * ρ ^ (11 n)`, that is, the entries of `x - 1`
have modulus at most `T ^ (99 n)`, then the matrix of `x` has operator norm at most
`b ^ (700 n r)`. 

### `sq_error_mul_ballBound_le`

 For `2 ≤ b`, `n, r ≥ 1` and `f ≥ 4000 n`, the square of the error `2 b ^ (-r ^ 3 f)` times the
volume bound `T ^ (9 r²) b ^ (99 r²)` at the radius `T = b ^ (700 n r)` is at most `b ^ (-24)`. 

### `IsCutBessel.setLIntegral_quotientPairing_sq_le`

 Let `F` be the cut of `W` in degree `f ≥ 4000 n`, and `deg > 0`. Suppose that the matrix
coefficient `quotientPairing W W` has squared `L²` norm at most `(card I) ^ 2 / deg`, and that the
ball of radius `T ≥ 1` in G₁ has volume at most `T ^ (9 r²) b ^ (99 r²) / deg`. Then on the position
ball at the scale `b ^ (6 r) * ρ ^ (11 n)` the matrix coefficient of `F` has squared `L²` norm at
most `(1 + b⁻¹ ^ 12) ^ 2 (card I) ^ 2 / deg`. 

### `IsCutBessel.scaledVolumeRatio_mul_pow_div_pow_le`

 Let `ρ`, `s`, `b` be the sizes of a cut Bessel function, Θ = `scaledVolumeRatio` the constant of
the local bounds, `deg * Θ ≤ b ^ (4 r²)` and `t = b ^ (6 r)`. Then
`Θ ρ ^ (10⁹ n⁴) ρ ^ (24 k) t ^ (10⁸ n⁴) / t ^ s`, which bounds the contribution of the remote
positions, is at most `b⁻¹ ^ 12 / deg`. 

### `one_add_inv_pow_twelve_sq_add_le`

 For `2 ≤ b`, the sum of the bounds `(1 + b⁻¹ ^ 12) ^ 2` for the positions in the position ball
and `b⁻¹ ^ 12` for the remote positions is at most `1 + b⁻¹ ^ 10`. 

### `IsCutBessel.enorm_formConst_mul_le_one`

 The normalising constant `formConst` = vol U(k) / vol U(r) / (λ · card I)², times
(λ · card I)², is vol U(k) / vol U(r). Its product with the ratio λ = `haarRatio` of the Haar
measures is at most `1`. 

### `IsCutBessel.norm_floorForm_zero_le`

 The mass at a real place. Let `F` be the cut of `W` in degree `f ≥ 4000 n`, and `deg > 0`.
Suppose that the matrix coefficient `quotientPairing W W` has squared `L²` norm at most
`(card I) ^ 2 / deg`, that `deg * scaledVolumeRatio ≤ b ^ (4 r²)`, and that the ball of radius
`T ≥ 1` in G₁ has volume at most `T ^ (9 r²) b ^ (99 r²) / deg`. Then the form `floorForm 0` of
floor `0` with weight `1`, times the normalising constant `formConst`, has modulus at most
`(1 + b⁻¹ ^ 10) / deg` for all lists `p`, `q`. 

### `IsCutBessel.norm_floorForm_wave_le`

 For a cut Bessel function `F`, lists `p`, `q`, a floor `i ≤ ϱ` and a frequency `ν ≠ 0`, take the
form of floor `i`, normalised by `formConst`, whose weight is the character `wave` of `ν` times the
diagonal frame entry number `i`. Its modulus times the dimension `card I` is at most
`scaledVolumeRatio * b ^ (2000 n ^ 9)` times the decay `dampedPower (k - n ^ 7) ‖ν‖⁻¹` times the
weights `headWeight` of `p` and `q`. 

### `IsCutBessel.norm_floorForm_heads_le`

 Decay for unequal last entries at a real place. If `i + 1 ≤ ϱ` and `ν = (p i)⁻¹ - (q i)⁻¹` is
not zero, the modulus of the form of floor `i + 1` with weight `1`, normalised by `formConst`, times
the dimension `card I` is at most `scaledVolumeRatio * b ^ (2000 n ^ 9)` times the decay
`dampedPower (k - n ^ 7) ‖ν‖⁻¹` times the weights `headWeight` of `p` and `q`. 

### `IsCutBessel.integrable_and_integral_wave_mul_floorForm_succ`

 Let `F` be a cut Bessel function (`IsCutBessel`) and `i < ϱ`. Replace the entries of `p` and `q`
at position `i` by the common unit `unitOrOne c`, which is 1 at c = 0. Then the integral over c of
`wave (ξ * c)` times the normalised form of floor `i + 1` converges. It equals the normalised form
of floor `i` with the weight x ↦ `wave (ξ * (realFrameGram x).diag i)`. A normalised form is
`formConst` times `floorForm`, and that of floor `i + 1` has weight 1. Here ϱ is the number of
hyperbolic planes. 

### `exists_hasLocalBounds_of_isCutBessel`

 Let `F` be the cut of `W` in degree `f ≥ 4000 n`, and let `deg > 0` play the part of a formal
degree: the matrix coefficient `quotientPairing W W` has squared `L²` norm at most
`(card I) ^ 2 / deg`. Suppose also that `deg * scaledVolumeRatio ≤ b ^ (4 r²)` and that the ball of
radius `T ≥ 1` in G₁ has volume at most `T ^ (9 r²) b ^ (99 r²) / deg`. Then there are forms `J i`
on pairs of lists with the local bounds `HasLocalBounds`: each form below the top is an integral of
the next, whose `wave` transform in the entry `i` decays in the frequency; `J (i + 1) p q` decays in
`(p i)⁻¹ - (q i)⁻¹` for `i < ϱ`; the bottom form has modulus at most `(1 + b⁻¹ ^ 10) / deg`; and the
top form `J (ϱ + 1)` is continuous, and positive semidefinite on lists with a common last entry. 
