---
{
  "module": "src/New/Spanning/Frames/RealShells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cut Bessel functions at ℂ: integration of the local estimates over shells

This file integrates pointwise local estimates for Bessel functions at the place ℂ over the group.
Every position lies in a dyadic shell, and the positions outside the position ball at a scale are
the remote positions. The place ℂ lies over a real place of the totally real subfield, and the
docstrings call it a real place. The results are the absolute convergence of the forms, an
integrated bound, and a bound for the form of each floor.

Throughout k = card κ and n = ϱ + 1 (`New.Shape.n`), as in the exponents.
`New.Floors.RealPlaceSizes.complexData` is the place datum at ℂ: box ‖x‖ ≤ ρ, Haar measure
`New.Floors.PlaceData.groupMeasure`. `New.Floors.RealPlaceSizes.gauge` measures sizes by powers of
L. A list p is a head of length j (`New.Floors.Size.IsHead`) if the inverses of p₀ ⋯ p_{l-1}, l ≤ j,
have modulus at most L. `New.Floors.PlaceData.floorForm` is the form of floor j.
`New.Floors.PlaceData.formIntegrandL1Norm` and `New.Floors.PlaceData.formMajorant` bound its
integrand at a position x. `New.Floors.Gauge.weightedSquareProduct` is the weighted product of norms
that their squares are compared to.

## Main definitions and results

* `New.Floors.IsCutBessel`: the cut, at size ρ, of a normalised Bessel function (`New.IsCutPair`) of
  irreducible type, with the numerical constraints.
* `New.Floors.IsCutBessel.lintegral_formMajorant_ne_top`: the forms converge absolutely.
* `New.Floors.IsCutBessel.norm_floorForm_le`: a local bound with gain (π / |y|) ^ (2 (k - 5)) gives
  a bound for the form.

Notions from other files:
* `New.Floors.complexPlace`: The place `ℂ`: `τ = 1/2`, `δ = i/2`, `ν` the image of Lebesgue measure
  under `r ↦ r i`, modulus `‖x‖ ^ 2`, character `x ↦ exp (x - x̄)` and constant
  `kernelBound = π ^ 2`.
* `New.IsCutPair`: Two Bessel functions, full and cut (`New.FullOrCut.select`), with base b and
  degree f. The cut one vanishes where `New.besselLength` exceeds b ^ (6 n + 2), n = ϱ + 1. Their L²
  distance is at most b ^ (-r³ f) √(card I), and f also sets their decay.
* `New.Floors.RealPlaceSizes`: The box radius is ρ = b ^ (6 n + 2) ≥ 8 r with b ≥ 2, the exponent
  s > 10⁹ n³ is fixed by k = s + 3 n + 6, and k ≥ n⁷, ϱ ≥ 10⁸.
* `New.headWeight`: The product of max(1, |δ|⁻¹) ^ K over the products δ = p₀ ⋯ p_l, l < j, if these
  have modulus at most R, and 0 otherwise. `New.dampedPower`: The gain r ^ K min(1, r)⁶.
* `weylElem j p`: The Weyl element w_p, with e_a ↦ p_a e*_a and e*_a ↦ e_a / p̄_a for a < j.
  `New.Floors.PlaceData.IsNear`: g is near at j if the coset `partialUnitriangularGroup j` · g meets
  the box. The frame is (e₀, …, e_{ϱ-1}, z), where e_a, e*_a are the hyperbolic pairs of basis
  vectors, and `New.Shape.top` is the position of z. `New.realFrameGram` x is the matrix of the
  products h(f_a, x f_b) of the frame vectors f_a; its entries are the frame entries of x.
* `New.Shape.scaledVolumeRatio`: The constant π ^ ((2ϱ + 1) k) · vol U(k) / vol U(r), where k = card
  κ and r is the rank of G₁. `New.Floors.PlaceData.headDensity`: A product of powers of |p_a q_a|,
  a < j. A normalised integral is an integral over G₁ times this density and
  `New.Floors.IsCutBessel.formConst`.


 ### Cut Bessel functions and their gauges 

### `IsCutBessel`

 `F` is the cut of the normalised Bessel function `F₀` of irreducible type `rep`: the two form a
cut pair (`New.IsCutPair`) with base `b` and decay rate `f`, and the box radius `ρ`, the exponent
`s` and `b` satisfy the numerical hypotheses `New.Floors.RealPlaceSizes`. 

### `IsCutBessel.irreducible`

 Every matrix that commutes with all `rep h` is scalar. 

### `positionBall`

 The position ball at scale `T`: the entries of `x - 1` have modulus at most `T ^ (99 n)`. 

### `dyadicShell`

 The shell of height `2 ^ i`: the positions `x` for which `2 ^ i` is the least of `1, 2, 4, …`
that bounds the moduli of the entries of `x - 1`. 

### `exists_mem_dyadicShell`

 Every position lies in a dyadic shell. 

### `notMem_positionBall_of_mem_dyadicShell`

 A position `x` in the dyadic shell `dyadicShell 𝔰 i` of height `2 ^ i` is not in
`positionBall 𝔰 T` for a scale `T ≥ 1` with `2 * T ^ (99 * 𝔰.n) ≤ 2 ^ i`. 

### `formConst`

 The normalising constant vol U(k) / vol U(r) / (λ · card I)² of the forms, where k = card κ, r
is the rank of the group and λ = `New.Floors.RealPlaceSizes.haarRatio` is the ratio of the two Haar
measures. 

### `isCut_complexData`

 A cut Bessel function `F` is cut for the place datum at ℂ: it is a Bessel function of frequency
`1` and vanishes off the translates of the box `‖x‖ ≤ ρ` by the Bessel unipotent group. 

### `mem_ofSize_gauge`

 For the gauge of size `L`, a number has size `i` if its modulus is at most `L ^ i`. 

### `isHead_gauge_iff`

 For the gauge of size `L`, the list `p` is a head of length `j` if the products of its first
`l ≤ j` entries have inverse modulus at most `L`. 

### `norm_leadingMinor_le_of_besselOrbitalIntegral_ne_zero`

 If the orbital integral J(γ) = ∫ F(y) ⊗ F(γ⁻¹y)^* dy of a cut Bessel function `F` of box size
`ρ` is not zero, then all leading minors of the matrix `realFrameGram γ` of the products
`h(f_a, γ f_b)` have modulus at most `ρ ^ (9 * 𝔰.n)`, where f is the frame (e₀, …, e_{ϱ-1}, z).


### `mul_pow_four_le_s`

 The exponent `s` is at least `10 ^ 10 * 𝔰.n ^ 4`, since the hypotheses carried by `hF` give
`s + 3 𝔰.n + 6 ≥ 𝔰.n ^ 7` and `𝔰.n > 10 ^ 8`. 

### `volumeExponent_eq`

 The exponent in the weight of the place datum at ℂ is `s`, since `k = s + 3 n + 6`. 

### `max_pow_le_mul_max_one_pow`

 If `1 ≤ L` and `L ^ K ≤ B`, then `max L x ^ K ≤ B * max 1 x ^ K`: replacing `L` by `max L x`
costs at most the factor `max 1 x ^ K`. 

### `headWeight_succ_of_le`

 If the product δ of the first `j + 1` entries of `p` has modulus at most `R`, the weight
`New.headWeight` gains the factor `max 1 ‖δ‖⁻¹ ^ K` from length `j` to length `j + 1`. 

### `exists_gauge_isHead`

 For a cut Bessel function `F` of box radius ρ and lists p, q there is L ≥ ρ such that (a) p and
q are heads of length j for the gauge of size L: the products of their first l terms, l ≤ j, have
inverse modulus at most L; (b) L ^ K ≤ ρ ^ K times the weights `New.headWeight` R K j of p and q,
for every R that bounds the moduli of these products. 

### `pairingNormSq_le`

 For a cut Bessel function `F`, the integral `pairingNormSq` of `|⟪F x, F y⟫| ^ 2` over two
points of the quotient by the Bessel unipotent group is at most λ² · card I, where λ = `haarRatio`
is the ratio of the two Haar measures. 

 ### Support of the forms 

### `formMajorant_eq_zero_of_lt`

 Support: let `F` be a cut Bessel function and `l ≤ j ≤ ϱ`. If the product of the first `l`
entries of `p` or of `q` has modulus above `ρ ^ (9 n)`, then the majorant `formMajorant` of the form
of floor `j`, in which both correlations are replaced by their moduli, vanishes at every
position `x`. 

### `floorForm_eq_zero_of_lt`

 Let `F` be a cut Bessel function (`hF`) and `l ≤ j ≤ 𝔰.ϱ`. If the product of the first `l`
entries of `p` or of `q` has modulus above `ρ ^ (9 * 𝔰.n)`, then the form `floorForm j p q F ω` of
floor `j` at the place datum `hF.complexData` is zero. This holds for every weight `ω` with
`‖ω x‖ ≤ 1` for all `x`. 

 ### Deep vectors and dyadic shells 

### `exists_sq_le_realDepth`

 Let `F` be a cut Bessel function, `p`, `q` heads of length `j ≤ ϱ` for the gauge of size
`L ≥ ρ`, and `x` not in the position ball at a scale `T ≥ L ^ (11 n)`. Suppose `⟪F y, F (y x)⟫ ≠ 0`
and that `w_p⁻¹ y` and `w_q⁻¹ y x` are near at `j`, for the Weyl elements `weylElem j`. Then some
e_a, `a ≥ j`, has `realDepth` at least `T ^ 2`: the infimum of the sum of the squared lengths at `y`
and at `y x`, modulo the e_b with `b < a`, of the vectors ζ orthogonal to these e_b with h(e_a,
ζ) = 1. 

### `hasDeepVector_of_notMem`

 Far means deep at a real place. Let `F` be a cut Bessel function and `p`, `q` heads of length
`j ≤ ϱ` for the gauge of size `L`. A point `y` is active if `⟪F y, F (y x)⟫ ≠ 0` and `w_p⁻¹ y`,
`w_q⁻¹ y x` are near at `j`. If `x` is not in `positionBall` at a scale `T ≥ L ^ (11 n)` and
`T⁻¹ ≤ τ / 2`, then every active point has a vector e_a, `a ≥ j`, whose depth, the inverse area of
the disc `stableProducts a`, is at least `τ⁻²`. 

### `floorMassLe`

 Let `F` be a cut Bessel function of box radius `ρ` and `j ≤ ϱ`. For every `g`, the set of `σ`
with `σ g` near at `j + 1` (`New.Floors.PlaceData.IsNear`) has measure at most
`(π ρ ^ 24) ^ k ρ ^ (9999 n)` for the measure `floorMeasure j` of floor `j`. This is `FloorMassLe`
for the weight `1`. 

### `one_le_massBound`

 The bound `(π ρ ^ 24) ^ k ρ ^ (9999 n)` for the mass of a floor is at least 1. 

### `two_mul_div_pow_le_of_pow_le`

 If `2 ≤ L`, `0 < τ ≤ 1`, `n ≠ 0` and `L ^ (2400 n²) ≤ τ ^ (400 n²) H`, then at the scale
`T = L ^ (11 n + 1) / τ` the number `T ^ (99 n)` is at most half of `H`. 

### `isShell_dyadicShell`

 Let `F` be a cut Bessel function and `p`, `q` heads of length `j ≤ ϱ` for the gauge of size `L`,
whose `loss` is L². The dyadic shell of index `i` is a shell of height H = `2 ^ i` for this gauge.
It is covered by the positions `x` with `x - 1` of size 1 for at most 2 H ^ (9 n) gauges of loss at
most L² H². If σ < 1 and L ^ (2400 n²) ≤ σ ^ (400 n²) H, then at each of its positions every active
point has a vector e_a, `a ≥ j`, of depth at least σ⁻². 

 ### Summation over the shells 

### `formConst_mul_lintegral_le`

 Let `F` be a cut Bessel function, `p`, `q` heads of length `j ≤ ϱ` for the gauge of size `L`,
and `1 ≤ t`. Let `φ` lie below the majorant of the form of floor `j` and, if `1 < t`, have a square
at most `((π ρ ^ 24) ^ k ρ ^ (9999 n) / t ^ s) ^ 2` times the product of norms. Then the normalised
integral of `φ`, times the dimension `card I` of the value space, is at most `scaledVolumeRatio * L
^ (10 ^ 9 n ^ 4) * ρ ^ (24 k) * t ^ (10 ^ 8 n ^ 4) / t ^ s`. 

### `formConst_mul_setLIntegral_compl_positionBall_le`

 Remote positions. Let `F` be a cut Bessel function and `p`, `q` heads of length `j ≤ ϱ` for the
gauge of size `L ≥ ρ`. Let `1 ≤ t`. Integrate the majorant `formMajorant` over the positions `x`
that are not in `positionBall` at the scale `t L ^ (11 n)`, meaning some entry of `x - 1` has
modulus above that scale to the power `99 n`. This integral, times `formConst` and `headDensity`, is
at most `scaledVolumeRatio * L ^ (10 ^ 9 n ^ 4) * ρ ^ (24 k) * t ^ (10 ^ 8 n ^ 4) / t ^ s`. 

### `lintegral_formMajorant_ne_top`

 Absolute convergence: if `F` is a cut Bessel function (`hF`) and `j ≤ 𝔰.ϱ`, then the majorant
`formMajorant j p q F` of the form of floor `j` at the place datum `hF.complexData` has finite
integral over `(𝔰.middleGram 1).G` against `hF.complexData.groupMeasure`. 

### `shell_bound_le_dampedPower`

 Let `ρ`, `s`, `b` be the sizes of a cut Bessel function, `0 < r` and `1 ≤ L`, and let `H ≥ 0`
satisfy `L ^ n ^ 6 ≤ ρ ^ n ^ 6 * H`. At `t = max 1 (ρ ^ 24 * r)`, the bound for the sum over all
shells (`formConst_mul_lintegral_le`) is at most `scaledVolumeRatio * b ^ (2000 n ^ 9) * dampedPower
(k - n ^ 7) r⁻¹ * H`. 

### `pi_sq_div_sq_pow_le`

 For `1 ≤ ρ`, `0 < r`, `1 ≤ ρ ^ 24 * r` and `s ≤ m ≤ k`, the power `(π ^ 2 / r ^ 2) ^ m` is at
most the square of `(π ρ ^ 24) ^ k ρ ^ e / (ρ ^ 24 r) ^ s`. 

### `norm_floorForm_le`

 Let `F` be a cut Bessel function with base `b`, let `j ≤ ϱ` be a floor, `p`, `q` lists of units,
`y` a unit and `ω` a weight of modulus at most one on G₁. At a position `x`, `formIntegrandL1Norm`
is the integral of the modulus of the integrand of the form `floorForm j p q F ω` of floor `j`, and
`Γ.weightedSquareProduct` is the product of the second moments of its two correlations, with the
constants of the gauge `Γ`. Suppose that for every gauge in which `p` is a head of length `j` the
square of the first is at most the second times `(π / ‖y‖) ^ (2 (k - 5))`, which is the value at the
place ℂ of the power in `h_local`. Then the modulus of the form, normalised by `formConst`, times
the dimension `card I` is at most `scaledVolumeRatio * b ^ (2000 n ^ 9)` times
`dampedPower (k - n ^ 7) ‖y‖⁻¹` times the weights `New.headWeight` of `p` and `q`. 
