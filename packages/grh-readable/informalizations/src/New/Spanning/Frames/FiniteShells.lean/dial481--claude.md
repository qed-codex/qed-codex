---
{
  "module": "src/New/Spanning/Frames/FiniteShells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiniteShells.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiniteShells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shells, decay and mass at the finite places

The positions `x` are sorted by the ideal of the denominators of `(x - 1) / g`, and into dyadic
shells by its index. The sum over the shells gives the decay of the forms in the frequency and the
mass. Here `R = P.integers` is the ring of integers of `A`, `g = F.levelUnit` is the level unit of
the place datum `F`, `ϱ = 𝔰.ϱ`, `n = 𝔰.n = ϱ + 1` and `k = 𝔰.k`.

Notions from other files:
* `New.Floors.IntegralPlace.IsLargeLatticeData.gauge`: the gauge of scale `α`, for a unit `α` of `A`
  that is integral and fixed by the involution; size `j` means `α ^ j * x ∈ R`, and the loss is
  `2 / modulus α`.
* `New.Floors.Size.IsHead`: `p` is a head of length `j` if the inverses of the products
  `p 0 ⋯ p (l - 1)`, `l ≤ j`, have size 1.
* `New.Floors.PlaceData.HasDeepVector`: at a given position, every active point has a vector after
  the head of at least the given depth.
* `New.Floors.PlaceData.formIntegrandL1Norm`, `New.Floors.PlaceData.formMajorant`: the modulus of
  the integrand of the form of floor `j` at a position, and a majorant of it that does not depend on
  the weight.
* `New.Floors.PlaceData.IntermediateGroup`: an integral group `Z` that contains the congruence group
  `K(g) = F.congruenceSubgroup`.

## Main definitions and results

* `New.Floors.PlaceData.dyadicShell`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.isShell_dyadicShell`: the shells; each collects few
  ideals.
* `New.Floors.IntegralPlace.IsLargeLatticeData.lintegral_shells_le`: the sum over the shells.
* `New.Floors.IntegralPlace.IsLargeLatticeData.enorm_floorForm_le`: the decay in the frequency.
* `New.Floors.IntegralPlace.IsLargeLatticeData.setLIntegral_compl_congruenceSubgroup_le`,
  `New.Floors.IntegralPlace.IsLargeLatticeData.massIntegral_le_main_add_error`: the positions
  outside `K(g)` contribute little to the mass.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `_root_.New.Floors.PlaceData.idealShell`

 The shell of an ideal `J` of `R = P.integers`: the positions `x` for which `J` is the set of the
common denominators in `R` of the entries of `(x - 1) / g`, where `g = F.levelUnit`. 

### `exists_denominator_ideal`

 For `x` in the group `T.G` and `g = F.levelUnit`, the common denominators in `R = P.integers` of
the entries of `(x - 1) / g` form a principal ideal `J = c R`, where `c ∈ R` is a unit of `A`, and
`J` has finite index `(modulus c)⁻¹`. 

### `exists_generator_of_mem_idealShell`

 If the shell `F.idealShell J` has a point `x`, then `J = c R` for a unit `c` of `A` that lies in
`R = P.integers`, and the index of `J` is `(modulus c)⁻¹`. 

### `hasDeepVector_of_mem_idealShell`

 An ideal of denominators of large index forces a deep vector. Let `F` be a large lattice datum
with level unit `g = F.levelUnit`, and let `Γ = h.gauge α` be the gauge of scale `α`. Let `p`, `q`
be heads of length `j ≤ 𝔰.ϱ` for `Γ`, and let `g⁻¹` have size 1 if `j ≠ 0`. Let `x` lie in the shell
`F.idealShell J` of the ideal `J` of `R = P.integers`. Suppose `σ < 1` and
`Γ.loss ^ (990 𝔰.n²) ≤ σ ^ (400 𝔰.n²) · J.cardQuot`. Then
`F.HasDeepVector j p q Z.besselVector x (σ²)⁻¹` holds: at every point `y` that is active at `x` for
the Bessel vector of `Z`, the depth `F.depth a y x` is at least `σ⁻²` for some index `a ≥ j`. 

### `exists_gauge_idealShell_subset`

 Let `F` be a large lattice datum, `Γ` a gauge and `J` an ideal of finite index of
`R = P.integers`. Then some gauge `Γ'` contains the shell `F.idealShell J` in `Γ'.positionsOfSize`:
for every position `x` in it, the matrix `(x - 1) / F.levelUnit` has size 1 for `Γ'`. Moreover
`Γ'.loss ≤ Γ.loss · J.cardQuot²`, where `J.cardQuot = [R : J]`. 

### `_root_.New.Floors.PlaceData.dyadicShell`

 The dyadic shell of height `2 ^ t`: the positions for which `2 ^ t` is the least of `1, 2, 4, …`
that bounds the index of the ideal of the common denominators of the entries of `(x - 1) / g`. 

### `two_pow_clog_le_two_mul`

 For `N ≠ 0`, the least power of two that is at least `N` is at most `2 N`. 

### `isShell_dyadicShell`

 Let `F` be a large lattice datum with level unit `g = F.levelUnit`, let `Γ = h.gauge α` be the
gauge of scale `α`, let `p`, `q` be heads of length `j ≤ ϱ` for `Γ`, and let `g⁻¹` have size 1
unless `j = 0`. Then `F.dyadicShell t` is a shell of height `2 ^ t` for the Bessel vector of `Z`: it
is covered by the position balls of few gauges `Γ'` with `Γ'.loss ≤ Γ.loss (2 ^ t)²`, and a large
height forces a deep vector. 

### `lintegral_shells_le`

 The sum over the shells at the finite places. Let `F` be a large lattice datum with level unit
`g = F.levelUnit`, let `Γ = h.gauge α` be the gauge of scale `α`, let `p`, `q` be heads of length
`j ≤ 𝔰.ϱ` for `Γ`, let `g⁻¹` have size 1 if `j ≠ 0`, and let `r + 10⁸ 𝔰.n⁴ ≤ 𝔰.k`. Let `f` lie below
the majorant `F.formMajorant` of `p`, `q` and the Bessel vector of `Z` and, if `e < 1`, have a
square at most `(e ^ s)²` times `Γ.weightedSquareProduct` at every position, where
`s = F.volumeExponent`. Then `F.headDensity j p q` times the integral of `f` is at most
`min 1 e ^ r · Z.massRatio · Γ.loss ^ (10⁹ 𝔰.n⁴)`. 

### `lintegral_formMajorant_ne_top`

 Let `F` be a large lattice datum, let `Z` be a group with `F.congruenceSubgroup` ≤ `Z` ≤ K,
where K is the integral unitary group, let `p`, `q` be any sequences of units of `A`, and let
`j ≤ 𝔰.ϱ`. Suppose `r + 10⁸ 𝔰.n⁴ ≤ 𝔰.k` for some `r`, so the rank `𝔰.k` is large. Then the majorant
`F.formMajorant j p q Z.besselVector` of the form of floor `j` has a finite integral over the group
`T.G` for `F.groupMeasure`. 

### `exists_unit_common_divisor`

 Two units `ξ`, `β` of `A` have a common divisor `η` over the ring `R = P.integers` of integers.
That is, `ξ η⁻¹ ∈ R` and `η⁻¹ β ∈ R`. This `η` is a unit of `A` and is congruent to `ξ` modulo
`β R`: `η = ξ + c β` for some `c ∈ R`. 

### `exists_unit_formIntegrandL1Norm_sq_le`

 The unit that gives the gain for the weights of `enorm_floorForm_le`. Let `F` be a large lattice
datum with level unit `g = F.levelUnit`, let `α` be a unit of `A` that is integral and fixed by the
involution, and measure sizes in the gauge `Γ = h.gauge α` of scale `α`. Let `p` be a head of length
`j ≤ ϱ`, let `g⁻¹` have size 1 if `j ≠ 0`, and let `1 / p i - 1 / q i` have size 1 for `i < j`. Let
the weight `ω` and the unit `ξ` be of one of two kinds: (a) `ω x = ψ (ξ h(f_j, x f_j))` for the
frame vector `f_j`, or (b) `ω = 1`, `j = i + 1` and `ξ = (1 / p i - 1 / q i) / g`. Then there are
units `η` and `w` such that `w`, `ξ w` and `ξ / η` are integral, at every position the square of
`F.formIntegrandL1Norm` for the Bessel vector of `Z` is at most
`(kernelBound / modulus η) ^ card F.FreeIndex` times `Γ.weightedSquareProduct`, and
`min 1 √(genIndex η) ^ 2` is at most `modulus w / modulus (α ^ (200 n²))`. Here `genIndex η` is the
inverse of the modulus of `η` and `kernelBound` is the constant in Plancherel's formula. 

### `modulus_le_inv_denomIndex`

 If `ξ`, `w` are units of `A` with `w` and `ξ w` in `R = P.integers`, then `P.modulus w` is at
most the inverse of `denomIndex R ξ = [R : R ∩ ξ⁻¹ R]`. 

### `min_sqrt_genIndex_pow_le`

 Let `ξ`, `η`, `w` be units of `A` with `w`, `ξ w` and `ξ / η` in `R`, and put
`e = √(genIndex η)`. If `min 1 e ^ 2 ≤ modulus w · L`, then `min 1 e ^ (t + 12)` is at most
`√(genIndex ξ) ^ t` times the sixth power of `L / denomIndex R ξ`, where
`denomIndex R ξ = [R : R ∩ ξ⁻¹ R]`. 

### `enorm_floorForm_le`

 The bound for the form of floor `j ≤ 𝔰.ϱ`. Let `F` be a large lattice datum with level unit
`g = F.levelUnit`, let `Z` be an integral group that contains the congruence subgroup
K(g) = `F.congruenceSubgroup`, let `R` = `integers` be the ring of integers of `A`, let `p`, `q` be
sequences of units of `A`, and let `t + 10¹⁰ 𝔰.n⁴ ≤ 𝔰.k` and `10¹⁰ 𝔰.n⁴ ≤ K`. The weight `ω` and the
unit `ξ` are of one of two kinds: (a) `ω x = P.ψ (ξ ⟨f_j, x f_j⟩)` for the hermitian form of `T` and
the frame vector `f_j`, or (b) `ω = 1`, `j = i + 1` and `ξ = (1 / p i - 1 / q i) / g`. Then the form
`F.floorForm` of `p`, `q` and the Bessel vector of `Z` has norm at most the product of
`Z.massRatio = vol(Z) vol(K(g)) / F.unipotentMass ^ 2`, of `√(genIndex ξ) ^ t`, of the sixth power
of the inverse of `denomIndex R ξ = [R : R ∩ ξ⁻¹ R]`, of `(2 / P.modulus g) ^ K` and of the weights
`New.finHeadWeight K j` of `p` and `q`. 

### `modulus_le_inv_of_le_cardQuot`

 Let `Q` be at most the index of every proper ideal of finite index of the ring of integers `R`.
A unit `c` of `A` with `c ∈ R` and `c⁻¹ ∉ R` has modulus at most `Q⁻¹`: it generates a proper ideal
of index `(modulus c)⁻¹`. 

### `modulus_le_half`

 Let `R = P.integers` be the ring of integers of `A`. A unit `c` of `A` with `c ∈ R` and
`c⁻¹ ∉ R` has modulus at most `1 / 2`. 

### `modulus_le_volume_nonunits`

 Let `R = P.integers` be the ring of integers of `A`. For a unit `c` of `A` with `c ∈ R` and
`c⁻¹ ∉ R`, the ideal `c R` consists of non-units of `R`, so the modulus of `c` is at most the volume
of the set of non-units. 

### `hasDeepVector_of_notMem_congruenceSubgroup`

 Let `F` be a large lattice datum with level unit `g` and congruence subgroup
K(g) = `F.congruenceSubgroup`, let `Z` be an integral group that contains K(g), and let `e` bound
the modulus of every integral unit of `A` whose inverse is not integral. If the point `x` of the
group `T.G` is not in K(g), every point `y` that is active at `x` has an index `a` with
`e⁻¹ ≤ F.depth a y x`. 

### `setLIntegral_compl_congruenceSubgroup_le_pow`

 Let `F` be a large lattice datum with congruence group K(g) = `F.congruenceSubgroup`, and let
`Z` be a group with K(g) ≤ `Z` ≤ K. Let `e` bound `P.modulus c` for every unit `c` of `A` in
`integers` whose inverse is not in `integers`, and let `r + 10⁸ 𝔰.n⁴ ≤ 𝔰.k`. Then the majorant
`F.formMajorant 0 1 1 Z.besselVector` has integral at most
`min 1 e ^ r · Z.massRatio · 2 ^ (10⁹ 𝔰.n⁴)` outside K(g). 

### `setLIntegral_compl_congruenceSubgroup_le`

 **Outside the congruence subgroup.** Let `F` be a large lattice datum with congruence group
K(g) = `F.congruenceSubgroup`, and let `Z` be a group with K(g) ≤ Z ≤ K, where K is the integral
unitary group. Let `Q ≥ 2` be such that every unit `c` of `A` with `c ∈ R` and `c⁻¹ ∉ R` has modulus
at most `Q⁻¹`. If `t + 2 · 10⁹ n⁴ ≤ k`, where n = `𝔰.n` and k = `𝔰.k`, then the integral of
`F.formMajorant 0 1 1 Z.besselVector` over the complement of K(g), against `F.groupMeasure`, is at
most `Q⁻¹ ^ t * Z.massRatio`. 

### `massIntegral_le_main_add_error`

 Let `F` be a large lattice datum with congruence group K(g) = `F.congruenceSubgroup`, where
`g = F.levelUnit`, and let `Z` be a group with K(g) ≤ `Z` ≤ K. Let `vol` be the Haar measure
`F.groupMeasure`. Let `Q ≥ 2` be such that `Q⁻¹` bounds `P.modulus c` for every unit `c` of `A` in
`integers` whose inverse is not in `integers`, and let `t + 2 · 10⁹ 𝔰.n⁴ ≤ 𝔰.k`. Then
`F.massIntegral Z = ∫_G |∫_Z extendedBesselChar g (y x y⁻¹) dy|² dx` is at most `vol(Z) vol(K(g))`
times the sum of `vol(Z)`, which comes from K(g), and the error `Q⁻¹ ^ t`, which comes from its
complement. The function `extendedBesselChar g` is `New.Floors.IntegralPlace.extendedBesselChar
F.levelUnit`. 
